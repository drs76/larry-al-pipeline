# /mnt/models/bonsai/bonsai-env.sh  — systemd EnvironmentFile (bare KEY=value, NO export)
# Ternary-Bonsai-27B llama-server (Mode B: time-shares GPU with the ollama coder)
BONSAI_HOME=/mnt/models/bonsai/Bonsai-demo
BONSAI_FAMILY=ternary
BONSAI_MODEL=27B
BONSAI_HOST=127.0.0.1
BONSAI_KV4=1
BONSAI_CTX=8192
BONSAI_NGL=999
BONSAI_SPECULATIVE=0
# Port is hardcoded to 8091 via sed on start_llama_server.sh (8090 = larry-dashboard).
