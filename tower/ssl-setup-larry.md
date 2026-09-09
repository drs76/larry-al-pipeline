# SSL Setup — larry.home.arpa

**Machines:** Deb (cert generation) → Larry (Nginx + services) → Nemesis/Pi-hole (DNS)

---

## Step 1 — Create Local CA on Deb

```bash
mkdir -p ~/certs/ca ~/certs/larry
cd ~/certs
```

**Generate CA key** (pick a strong passphrase, you'll need it each time you sign a cert):
```bash
openssl genrsa -aes256 -out ca/ca.key 4096
```

**Generate CA root cert** (valid 10 years):
```bash
openssl req -new -x509 -days 3650 -key ca/ca.key -out ca/ca.crt \
  -subj "/C=US/ST=Home/L=Home/O=HomeLabCA/CN=HomeLabCA"
```

---

## Step 2 — Create Server Cert for larry.home.arpa

**Server key** (no passphrase — Nginx reads it automatically):
```bash
openssl genrsa -out larry/larry.key 2048
```

**SAN config file** (required for modern browsers — CN alone is not enough):
```bash
cat > larry/larry.ext << 'EOF'
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
prompt = no

[req_distinguished_name]
C = US
ST = Home
L = Home
O = HomeLab
CN = larry.home.arpa

[v3_req]
subjectAltName = @alt_names
keyUsage = digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth

[alt_names]
DNS.1 = larry.home.arpa
DNS.2 = *.larry.home.arpa
EOF
```

**Create CSR:**
```bash
openssl req -new -key larry/larry.key -out larry/larry.csr \
  -config larry/larry.ext
```

**Sign with your CA:**
```bash
openssl x509 -req -days 825 -in larry/larry.csr \
  -CA ca/ca.crt -CAkey ca/ca.key -CAcreateserial \
  -out larry/larry.crt \
  -extensions v3_req -extfile larry/larry.ext
```

> 825 days is the browser-enforced max. Renew annually.

**Verify SANs are present:**
```bash
openssl x509 -in larry/larry.crt -text -noout | grep -A3 "Subject Alternative"
```

---

## Step 3 — Push Certs to Larry + Install Nginx

**From Deb, copy certs to Larry:**
```bash
scp ~/certs/larry/larry.crt user@larry:~/
scp ~/certs/larry/larry.key user@larry:~/
```

**SSH into Larry, move into place:**
```bash
sudo mkdir -p /etc/nginx/ssl
sudo mv ~/larry.crt /etc/nginx/ssl/
sudo mv ~/larry.key /etc/nginx/ssl/
sudo chmod 600 /etc/nginx/ssl/larry.key
sudo chown root:root /etc/nginx/ssl/larry.key
```

**Install Nginx:**
```bash
sudo dnf install nginx -y
sudo systemctl enable --now nginx
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

**Create Nginx config:**
```bash
sudo tee /etc/nginx/conf.d/larry.conf << 'EOF'
server {
    listen 80;
    server_name larry.home.arpa;
    return 301 https://$host$request_uri;
}

# Open WebUI
server {
    listen 443 ssl;
    server_name larry.home.arpa;

    ssl_certificate     /etc/nginx/ssl/larry.crt;
    ssl_certificate_key /etc/nginx/ssl/larry.key;
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_ciphers         HIGH:!aNULL:!MD5;

    location / {
        proxy_pass         http://127.0.0.1:7000;
        proxy_set_header   Host $host;
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
    }
}

# Ollama API (remove if not needed externally)
server {
    listen 11443 ssl;
    server_name larry.home.arpa;

    ssl_certificate     /etc/nginx/ssl/larry.crt;
    ssl_certificate_key /etc/nginx/ssl/larry.key;
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_ciphers         HIGH:!aNULL:!MD5;

    location / {
        proxy_pass         http://127.0.0.1:11434;
        proxy_set_header   Host $host;
        proxy_set_header   X-Real-IP $remote_addr;
    }
}
EOF
```

```bash
sudo nginx -t && sudo systemctl reload nginx
```

---

## Step 4 — Pi-hole DNS (on Nemesis)

1. Pi-hole admin → **Local DNS → DNS Records**
2. Domain: `larry.home.arpa` | IP: Larry's LAN IP
3. Save

Test from Deb:
```bash
dig larry.home.arpa @<pihole-ip>
```

---

## Step 5 — Install CA Root Cert on Clients

### Deb (cert already here, just install it)

```bash
sudo cp ~/certs/ca/ca.crt /usr/local/share/ca-certificates/larry-ca.crt
sudo update-ca-certificates
```

> **Chrome/Chromium** uses system store — no extra step.

> **Zen Browser** (Firefox-based) — uses NSS store, not system store. Import with certutil:
> ```bash
> certutil -A -d ~/.config/zen/'e5u067ob.Default (release)' -n "HomeLabCA" -t "CT,c,c" -i ~/certs/ca/ca.crt
> certutil -A -d ~/.config/zen/'iek5s33z.Default Profile' -n "HomeLabCA" -t "CT,c,c" -i ~/certs/ca/ca.crt
> ```
> Restart Zen after.

---

### Windows

Copy `ca.crt` to the Windows machine (SMB share or USB).

**Double-click method:**
1. Double-click `ca.crt` → Install Certificate
2. Store Location: **Local Machine** → Next
3. "Place all certificates in the following store" → Browse → **Trusted Root Certification Authorities** → OK
4. Finish → Yes

**Or PowerShell (Admin):**
```powershell
Import-Certificate -FilePath "C:\path\to\ca.crt" `
  -CertStoreLocation Cert:\LocalMachine\Root
```

> Firefox on Windows: same manual import as Linux above.

---

## Step 6 — Verify

```bash
curl -v https://larry.home.arpa
# Expect: 200 OK, no cert errors

curl -v https://larry.home.arpa 2>&1 | grep -E "subject|issuer|expire"
```

Browser: navigate to `https://larry.home.arpa` — padlock, no warnings.

---

## Annual Cert Renewal (on Deb)

```bash
cd ~/certs
openssl x509 -req -days 825 -in larry/larry.csr \
  -CA ca/ca.crt -CAkey ca/ca.key -CAcreateserial \
  -out larry/larry.crt \
  -extensions v3_req -extfile larry/larry.ext

scp ~/certs/larry/larry.crt user@larry:~/
ssh user@larry "sudo mv ~/larry.crt /etc/nginx/ssl/ && sudo systemctl reload nginx"
```

CA root valid 10 years — no need to re-install on clients at renewal.

---

## File Map

| File | Machine | Path | Notes |
|------|---------|------|-------|
| `ca.key` | Deb | `~/certs/ca/ca.key` | Never share |
| `ca.crt` | Deb + clients | `~/certs/ca/ca.crt` | Install on all clients |
| `larry.key` | Larry | `/etc/nginx/ssl/larry.key` | Server private key |
| `larry.crt` | Larry | `/etc/nginx/ssl/larry.crt` | Server cert |
| `larry.ext` | Deb | `~/certs/larry/larry.ext` | Keep — needed for renewals |
