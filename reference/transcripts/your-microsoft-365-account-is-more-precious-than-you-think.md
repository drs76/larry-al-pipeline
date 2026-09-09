# Your Microsoft 365 account is more precious than you think

- **Source:** https://www.youtube.com/watch?v=8ZMV55SYR-4
- **Video ID:** 8ZMV55SYR-4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 73m40s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you for being here this is my
first time as a speaker here at BCT Tech
days ever so you might be witnessing
something great for the future I hope at
least uh the session is called your
Microsoft 365 account is more precious
than you think but because I'm a new
speaker it might be appropriate to uh
firstly introduce myself so my name is
Kevin rosenal I am from the Netherlands
I work as a technical League consultant
for a business Central partner in the
Netherlands called Bliss software uh
I've been with with the company for
about 9 years now doing everything from
n 2015 implementations and development
as well as Azure with on Prem uh on Prem
NV hosting or business Central hosting
as well as security the last couple of
years uh I also have a LinkedIn page
that's the only social media profile
that I actively use so if you want to
follow me go ahead and you might
recognize me from one of my site
projects which is BC status.net which is
where I U monit
several business Central environments
for um for
availability so the goal of the session
today this the goal of the session today
is to create uh awareness around account
security in Microsoft entra we often
talk about account security within
business Central itself for example with
permission sets but there's more more to
it and I think with the shift we made
from the on Prem world to Business
centrer Online we have a shared
responsibility to do this right uh and
also because more and more business
Central features are moving away from
within business Central towards entra uh
for example API registrations app
registrations are now done in entra
instead of uh what we had before with
with web service Keys um other otherwise
uh the group uh user groups are now
moved towards the security groups
recently which is also an entra ID
feature so this this session is mainly
about
what entra id is how it protects our
data what different types of attacks we
can do in in entra and what protection
me methods that we can
use so session timeline first we talk a
little bit about authentication which is
verifying who you are to a system uh the
second topic is authorization which is
about who what are you able to do within
a system and thirdly uh user protection
which is about the how uh what add-ons
you can use to help you protect your end
users against uh potential
threats so first question for the
audience uh who has ever configured an
on Prem instance of any or business
Central
before yeah quite a few quite a few
hands you might recognize this at some
point during the project we had to
choose some sort of credential type
whether that was a Windows or username
when the customer was using an on Prime
active directory structure or Access
Control service when it was was entra or
n user password when there was no
identity provider at
all now Business Center Online is
slightly different as it is entra
authentication only so what is Microsoft
entra anyway uh it is the identity and
access management system which is the
core of authentication and authorization
by Microsoft so it's the single sign on
solution that you can use to log in to
business Central to Outlook to teams to
one drive uh even uh external developers
can Implement Andra as an identity
provider into their app so you can use
your account there as well now some of
you in the audience may be like uh
authentication what is it all about well
it looks something like this way back uh
so we have a username we have a password
and then you are signed in now for
Microsoft Partners it might look
slightly different because they are
required to use multiactor
Authentication
and multiactor authentication is the way
that we use to provide two or more
verification factors which has been
around for a while uh as I said it's
mandatory for all partners and it
protects very well against password
based attacks so that means boot forcing
uh Microsoft latest numbers on this uh
at the msignite was announced that it
protects against 4,000 plus attacks
every second uh it protects well against
data breaches I highly suggest uh taking
a look at haveb pone.com to check your
email address whether your account has
been compromised in a data leak or not
and of course it works against fishing
emails or or QR codes or something like
that now it's also the most hated
security feature by end users because
every company recommends their own app
if you try to enable multifactor
authentication with a Google account
Google uh really want you to use their
uh their account their their
authenticator app if you do so with with
L PA for example L PA will recommend
their own app and even Microsoft does
the same as well with the Microsoft
authenticator app so for some of you
maybe in the audience here your phone
might look like this whose phone looks
like this who has multiple authenticator
apps on their phones yeah exactly this
made my point so another difference is
difficulty is there are many different
implementations so Microsoft for example
uses number matching for a very good
reason that I will show later
uh there is the six-digit codes that you
can that's time based and there are the
approved in I uh uh sort of structure
and there already the old very
oldfashioned SMS Voice or email MFA uh
features
now this is notable in the statistics
because only 38% of the monthly active
entra ID users that is both personal as
well as business accounts for entra uh
are you using MFA at any time in the
month which is a very very low number so
Microsoft decided to do something about
this they wanted to improve uh the
number so what they do they created for
enter ID free users they created a
security defaults functionality that you
can enable 10 and wide which means uh MF
MFA is now enforced for all users
without any exception uh MFA is required
based on signals so uh for example if
you check change location or device you
have you are required to use or to to
fulfill the MFA requirement otherwise it
will accept it anyway because they
recognized you from before and Legacy
Protocols are disabled such as SMTP POP
3 Etc now if you go higher up in the
hierarchy so if you have an ENT idp1
license you unlock a feature called
conditional access and with conditional
access you can create policies and in
those policy you can create exceptions
so it's much more customized able than
the free security default functionality
is you cannot combine those two however
so you have to choose either between do
I want to implement un conditional
access to enforce uh MFA or do I want to
use uh security
defaults and there are policy templates
available which I will show you in a
demo in a second to um uh to uh to get
you started with
this so let's go to the first
demo yep
so this is my personal tenant as you can
see it's an Microsoft entro ID free
licensed tenant uh I'm in the entra
admin Center by the way which is simply
ent.
microsoft.com and if we go to properties
here in the identity overview
page we'll see that I have security
defaults enabled for my own uh for my
own tenant and if
we uh to click on this button here you
can see that is enabled and it protects
against 99% 99.9% of the accounts uh
compromised that could be stopped by
using MFA so there's an option here to
either enable it or disable it and I'll
leave it
on now in enter idp1 it's slightly
different
um I've got a P2 license here because
this is a CDX environment which I'm
going to use some functionality for
later on um but as you can see here I've
got a conditional access policy in
enabled so I cannot configure any uh
security default policy here so in order
to do in order to enforce MFA within um
within within the conditional access
policy we go to
protection then we go to conditional
access and here we can create
policies there's already a standard or
default policy enabled because this is a
CDX environment and Microsoft enforces
us to um to have MFA enabled by default
so I cannot remove this but otherwise in
a regular production tenant this
wouldn't be uh wouldn't be the case um
so if we create a
new uh policy and let's call it MFA and
I've got a test user called John so I'm
going to call this MFA for John and here
we can uh create an assignment so which
basically means to what or to who does
this policy apply to so we can say for
example we can include all users so this
is the flexibility we can include all
users but exclude some users or some
groups or whatever we think it's
necessary to exclude um or we can simply
select the users that we want so we can
say for example
John hit select and now this policy will
only apply uh to John next we have to
specify our Target resource so by
default we can say
include everything exclude whatever we
want again and we can also say all Cloud
apps so now it's applied to all
Microsoft 365 services and we can also
specify uh select apps so for example we
can say this policy only applies to
Microsoft admin portals for example but
also specifically to uh business Central
which is also an app in here so we can
specify which policies we want for for
um Business Center for example
um in this case I'm going to say all
Cloud apps because we want to apply uh
to
everything um next up is Network so if
we want to exclude certain networks from
being in this policy because for example
you have a static IP address in the
office and you don't want to bother
people with doing certain stuff inside
of uh inside of the office network uh
you can enable or disable it here and
next up is uh uh conditions which you
can specify certain device platform for
example which where this policy applies
to and next in the oops next in the
ground controls we can then say we want
to require multiactor authentication so
we select multifactor authentication
required enable and then here is a nice
feature where you can say do you want to
enable this policy and turn it on or off
but you can also say report only so can
firstly uh view in the signin logs uh
what is actually happening before
rolling out the
policy so if we say on and we create the
policy we should now be able
to if I take the second
browser and it will now ask us for more
information because that's what we
require and I have to for some reason
when my laptop went
idle the connection to my phone went
off there we
go so now we can register the account
for MFA this should look familiar
hopefully
so we say yes we have the authenticator
app work or school account is good so we
go to my phone open the authenticator
hit the plus symbol work or school scan
the QR code
here click next and now we should be
able to number
match so 39
next
done right and as know now we signed in
and we have multifactor authentication
uh enabled for U for
John so we are uh how many minutes into
the session like 50 minutes or so we
have MFA enabled so we're safe right
right oh sorry I I forgot to switch so
with MF we're safe right well uh not
quite because password based attacks are
not the only uh threats we have in this
world unfortunately there are also the
MFA attacks anti post authentication
attacks uh for example with MFA attacks
we have SIM swapping which used to be
quite a big problem in the Netherlands
back in the day uh famous people uh
would get their Sims SIM cards swapped
of their mobile phones uh how did that
happen the attacker would simply call
the phone carrier tell them the phone
carrier employee that they were the
famous person and the phone the phone
carrier would simply ask what is your
date of birth and what are the last
three digits of your bank account number
and send them a new SIM card so it
happened quite often nowadays it's a
little bit better protected but it's one
of the reasons why SMS or voice is no
longer recommended as a multiactor
authentication method uh a fatigue was a
technique used to Simply spam the end
user until they hit a proof uh this is
also the reason why Microsoft changed
the implementation from the deny approve
approach to the number matching approach
um uh the third one adversary in the
middle which is something that will show
in the next demo but it's basically a
proxy between the uh end user the Target
website and there's a proxy sitting in
between which the attacker can intercept
and uh take control of
um then in the post authentication
attack methods we have token theft uh
simply install a piece of malicious
software on your notebook and your uh
tokens which are stored in your computer
locally might get stolen and uh replayed
by the by the attacker and consent
fishing is the one uh you see on the
right here where a malicious application
would get access to your account because
you simply approve permission to do
so so what if if we can combine those
three methods into one attack so from
the password based attacks we take a
fishing mail from the MFA based attack
we take the adversary in the middle and
from the post authentication attacks we
take uh token theft what could possibly
go wrong eventually in part seven the
website will return a session cookie and
we will be able to replay the token in a
different uh browser and you will see
that we can take over the
account now in disclaimer up front
this is merily a demo of what a
potential attacker can do this is all
open on the public Internet it's nothing
nothing dark web or something like that
uh but I wouldn't advise to do this on
your your friends or colleagues for
example
um let's
see so I'm logged in here as John and we
can go to his
email and there's this uh Curious email
of of Kevin and he forwarded an email
from Peter and Peter said hi Mr Kevin
you can find the very confidential new
business agreement at the following URL
hope to hear from you soon and John is a
very naive CEO so he clicks the
link and it looks like he's going to
something that is the Microsoft login
portal so he enters his
credentials because he's very curious
about the new business even the theme
changes so that's even more
convincing he has to do MFA matching on
his phone so that's
good stay signed in yes please that's
very
helpful and then he gets redirected back
to office.com and he has no clue what
just happened and he will he might even
do it again or contact Kevin saying you
know I don't know what this was but it's
not really working so um what's going on
here now if we go to uh the attacker's
point of
view let's
see I forgot to sign it
in um I don't know maybe it's
not so the attacker on his side of view
he has a teams Channel which is very
handy uh he gets the notifications of
the uh people who actually clicked on
the link so um let's see if there's
something in
here two new notifications
okay so the first one is the captured
login information so this password is
apparently bctd 2024 dollar dollar so
that's already very helpful but he has
MFA enabled so he cannot do a whole lot
with this the second um notification
here is is quite interesting because
this uh has the authentication cookies
from the from the session that John just
created in the Microsoft service so if
we close up this browser and start a
clean one I can go to
portal.
office.com and you'll see I'm not signed
in right now we basically copy this
string
get into the developer
tools and paste it in and I have
to I want to allow pasting now I close
this page hit refresh and I'm signed in
as
John
now John is a CEO with global admin
permission so we can actually go into
the um into the admin portal and to the
active users and we we can create a user
for for ourselves so uh uh so Peter
Peter attack for
example it's all
good next so we can do basically
everything anything that we
want and give ourselves Global
upman just for
fun so now we sto his account and we've
created a new admin account to
um to manage his tenant for
him so how did this work uh it's quite
simple actually there is a there is an
Azure function underneath so it's a
serverless serverless structure and if I
really go to the um to the Azure portal
with a different account
there's a function app here called bctd
with with uh simply two functions and
underneath there is a there is an an
um application Insight Service attached
to it as well and if we go to the logs
of the application
insights resource we can see if
we run the traces we've got both the the
captured login and the captured cookies
again so that's how this works and this
is how we do the notification in teams
simply capture the information in
application insights from the user
forward it back to uh to another
service so how do we combat this it
turns out there are differences in MFA
strength so what we just did what we
just configured so the default number
matching is in fact regular MFA so it's
a password plus something that we have
like a phone and which we can use to do
number matching on uh the second degree
is passwordless MFA which is somewhat
identical to the first method except for
the fact that we wouldn't have the
password which we didn't need anyway so
there's no uh there's no improvement in
in that case um the third one is fishing
resistant MFA and that's the interesting
technology here and this contains for
example Windows hello for business has
this functionality so you can use uh
your Windows device with a Windows hello
compatible webcam or a fingerprint
scanner or or or um or a pin code uh
this the second one is the certificate
based authentication which is also
device based and working with a a public
private key structure uh the third one
is a PH2 security key which is something
that I have physically here which is a
physical key that you plug into your
computer with a PIN code and the fourth
one is the most interesting one because
this is the most recent uh development
in entra which are pys which I would
like to tell about a little more uh it's
a new standard by the pho Alliance and
it's supported by many large companies
so Apple Google Microsoft Amazon
everyone is basically implementing this
solution and it's aimed to eliminate
passwords so no more usernames no more
uh no more
passwords it's based on a public private
key uh certificate structure so the
public key is unique for each so the
pair the public private key pair is
unique for every account you have online
so if uh if and the public key gets
stored obviously with the with the
service so if the database gets stolen
or your public key leaks in a data
breach it doesn't matter because it's
Unique and it's not usable with without
the private key anyway um as I said it's
fishing resistant and it's synchronized
between devices unlike uh physical keys
so that's one downside of of physical
keys and there's a public preview now in
uh in entra and if you want to learn
more about what services support report
p keys you can go to P keys. directory
and you'll find many services um it's a
relatively new feature so there are not
many services yet uh but the
expectations are that this will be a
very big uh big change in How We Do
authentication in the in the
future so let's register aosi in
entra um what's this account this is
John here
yeah so in order to do so we go to my
account.
microsoft.com and we go to security
info within the security info
panel please
we hit add sign in method and we choose
for a pass key right now it's only
compatible with the Microsoft
authenticator app but I assume this will
change in the in the future because a
lot of password managers are already
supporting uh pass Keys as well as a
storage
option uh next so what devices do we
want to use I have an iPhone here so
I'll choose an iPhone and this is
something that you have to set up on
your device as well which I've already
done so in the settings app you'll go
to uh password
options
passwords and you'll select uh password
options select autofill with the
authenticator app which is this one you
cannot see it and this and you set up
the codes in the authenticator app so we
hit next open up the camera okay
I
understand so we'll scan the QR code and
then it says save a pass key so that's
what I
do
hopefully
right do I want to create a pass key for
John it'll be saved and available on
devices where authenticator is installed
continue hit
done and there we go we've got our first
uh b key installed so now the
authentication flow looks a bit
different so if we try to sign in
now we have to explicitly tell the
system that we want to use a pass key so
we choose sign in options on the bottom
here then we go to face fingerprint pin
or security
key then we choose uh user phone tablet
or security key and then we get this uh
QR code again so get the camera sign in
with apy
then we can choose what account that we
want because I've got two pass Keys
configured on this
phone and that way we can sign in
without entering a username or uh or a
password so if we try the same trick
again that we did before
or
not oh that's
interesting
right if you go to sign in options here
you will notice that the option isn't
isn't here which is basically the part
where uh where the URL doesn't match the
technology that is implemented here and
it's simply not uh not showing up that's
what makes it fishing
resistant all right so short recap on
authentication so it's verifying who the
user is token theft can still happen
when you are using less secure
multiactor authentication methods and
strong Authentication methods are either
Windows hello for business certificate
based authentication PH2 security keys
or a b key and you can use a combination
of those of any of those uh together so
for example on my work laptop I use
Windows hello business but I also got a
physical uh security key and you can use
them in uh in different
ways so this is already a good start uh
but as you may have noticed I've created
a new account because John was a global
admin and we should ask ourselves why is
JN a global administrator because token
theft even though we have configured uh
a fishing resistant uh MFA method now
it's still a possibility because local
admins are always vulnerable to
malicious software as I've mentioned
earlier so we should apply the principle
of least privilege which means we should
revoke unused access so if John is only
doing some user administ rtion he
shouldn't be a global admin instead we
should configure reducible access so we
should configure John to be a user
administrator instead and enable just in
time access which means if John wants to
if if if John is not doing user
Administration all day every day he
shouldn't have that permission he should
only have this permission if he wants to
create a user right now for a certain
amount of time and this is also a nice
way to Monitor and audit access between
those different privileged uh roles so
in order to accomplish this uh we have
uh a nice feature in Microsoft entra
which is called privileged identity
management or Pim for short uh which I'm
going to show you uh
now so going back to
entra and this is a P2 licensed uh
functionality by the way
um in entra we go to Identity governance
and then we can go to privileged
identity
management and from here we can
configure different uh different
different functionalities so first we
can configure entra roles we can
configure groups which are security
groups and we can configure uh Azure
resources but before we going to do that
I'm going to
remove the admin rights from John first
so he has an assigned role which is the
global administrator and I'm going to
say remove
yes so now let me show you how to
configure an ENT roll for example so if
we want to manage an entra roll we can
click on entra roll and we can show the
rules that are available to
us for example we take uh folks uh
business Central administrator which is
one of the uh one of the new entro rules
that are available to us and then we go
to
settings and this is where we can
configure all kinds of interesting
things so for example we can specify how
long a certain role can be active at a
given time so if we say for example four
hours this means if I activate it now
the role can only be available for a
total amount of four hours or shorter if
the user specifies so we can say on
activation do we require something for
example we can enable uh Azure
multifactor authentication if we want or
we can uh enable conditional access
authentication uh context which is a
pretty neat feature that you can combine
with conditional access policies which I
will show
later um if you want you can require a
justification for Activation or
something like ticket information so if
you are working for a certain customer
and you want to provide a ticket number
giving the reason uh uh why you are
accessing their environment you can do
so and if you want you can even uh uh
require approvals before activating so
if you uh if you want to have a 4 I
system where someone else approves your
request instead of
uh enabling it without without uh
without checking with someone else uh
you can disable this but this is a nice
functionality if you want uh want to
want to have approvals as
well so we say next and this allows us
to set the uh if the if the uh
permission or if it can be permanent or
not and uh eligible means uh can someone
be uh permanently eligible to do to get
a certain role or do I want to limit a
certain time and active assignment is
basically what we had before the
situation where there uh it is the
assignment is always active or it can
expire after a certain amount of time if
you
desire
um we can still require MFA if we want
on active assignments and of course we
have to give a justification if we set a
permanent or if we set an active
assignment then there are some
notifications that we can send on all
kinds of roles which uh I'll leave the
defaults for now and then we say
update so now we can assign a user to a
certain rule so if we say add
assignment we select a member we can say
John for
example and hit
next and here is the assignment type
again so if he's if he's active
permanently if he's eligible of eligible
then he can activate when he needs it
which is the preferred way to do
it and then we hit
assign so now John is eligible
to uh become a Dynamics 365 business
Central administrator but that obviously
doesn't work out of the box so if I now
turn this side by side so on the left
side I've got my admin uh sort of view
and on the right side is my my John view
so if we now go to uh business
central. dynamics.com
admin this shouldn't work because even
though he is eligible to be a business
Central administrator he is not right
now so in order to become one he has to
go to
entra
microsoft.com navigate G to Identity
governance privileged identity
management and then we choose activate
just in
time and here we can see what access we
have and there is the business Central
admin again so we can hit
activate this validates the request and
we can set a duration or a for a maximum
of four hours which is exactly what we
have configured but in this case I only
want it for 1 hour which which is fine
and if you want a custom activation time
so you say for example I want to be able
to do this at 6:00 in the evening you
can activate it in that point in
time the reason is uh demo
obviously and then we can hit
activate now sometimes with activating
roles like this sometimes it works
immediately and other times you have to
word wait a few seconds or a few minutes
rather so hopefully it will be quick
today right so as we can see now we have
now an active assignment as well as
the eligible one um so let's go to
business central. dynamics.com
let's see if it works now yeah so now we
do have the permission and we can access
the admin uh admin
portal
um there's something else that I want to
show you uh which I cannot do in this
demo environment which I've prepared a
video for this so um the way this this
can also work work with for example
accessing customer environments uh you
all might know or or or may or may or
not know that we can access customer
tenants using uh granular delegated
admin permissions and in order to do so
we have an admin relationship and to
this admin relationship we uh we link a
certain Security Group and privileged
identity management also works with
security groups so if we create a
security group uh we make people
eligible to become a member of this
Security Group we can also make sure
that our users cannot simply go in any
environment without uh doing this kind
of authentication before which I
hopefully if this works I'll have a
video of
it so this is a security group
called PC tech days demo and there are
no direct members assigned to this uh to
this group at this moment in time and
within the privileged identity
management submenu we see that
the uh BC Tech days user is eligible
to um to become a member of this
group so within the partner Center here
we have a customer called Bliss software
test and Bliss software test uh as an
active admin relationship to with our
tenant um called the Bliss 365 test
consultants and to this we you can see
we have the Dynamics 365 uh business
Central administrator role enabled with
the security group uh
together so now if
we if if you try to access the customers
admin portal now without uh without
enabling or without becoming a member of
the group you'll see that it won't work
as you can see we have no permission
because the user does not exist in the
partner tenant which
is fair enough
and if I Now activate Just In Time by
navigating
to the um the user group or the security
group
rather and I'll activate the uh
permissions or becoming a member
sometimes validating the request can
take some
time but eventually it will
work for
so now I am a member of the group and if
I try to access the the same URL so the
same business Central admin cender of in
the uh in the company's in in the
customers tenant sorry then you can see
we can access it through uh through uh
the delegated admin permissions
so
recap on authorization it's about what a
user has access to and with privileged
identity management you can reduce
access to admin resources or uh other
resources if you uh if you want to uh
just in time access insurance
permissions can be granted to a user
when it's necessary but only with
fishing resistant MFA and this is
something that I haven't shown you yet
but I will do so uh after this slide uh
time based access ensures that
permissions are revoked uh when uh when
expired so let me show you how you can
enforce fishing resistant multifactor
authentication real quick because I
forgot to do so um so if we go
to entra
again um navigate to protection
conditional access we can configure a
authentication context in here uh which
is nothing more than just some name it's
it doesn't really do anything by its own
so if we say for example here strong
strong MFA for example and we save
this you'll be able to
configure H to configure a conditional
access policy with a Target resource
that's applied to an authentication
context so here's the strong MFA again
that we've just created and if we save
this and we go to Grant
we can if we disable the uh the standard
required multifactor authentication one
that we did before we can select require
authentication strength and here we have
the options multifactor authentication
which is the default passwordless MFA or
fishing resistant MFA so if we do it
this way and we save
this um we have a policy that we can
apply to uh if this policy is being used
uh it will require us to use strong uh
strong MFA and the way we configure uh
the conditional access policy and and
and and tied it to um uh to the to the
to the uh Pim roll we can go to the pin
rolles again uh to the management of it
so if I say if I do this to Global admin
for
example if we hit
settings edit we can on activation
require the same uh conditional access
authentication context that we've seen
before so if you configure it this way
and I'll add John to the user list John
won't be able to active activate the
global admin uh permissions unless he
has uh authenticated himself with a
strong strong MFA
so if I now try
to and this might work because we just
did so but eventually it
should it will give us a notification
here where it says a conditional access
policy is enabled and may require
additional verification click to
continue so here we is here is the
additional step that we have to do in
order to uh to get the permissions that
we uh that we've asked
for um third one Defender for Office
365 is a very helpful tool to protect
your end users from all kinds of malware
fishing and spam in email or in teams
and it's enabled by simply uh flipping a
switch uh it blocks email B based on on
IP or and or domain reputation uh zero
Auto zero hour auto Purge is is quite
good for for those scenarios because uh
malware that's actually delivered into
your inbox can be removed if Microsoft
decided that it was malware or fishing
after all uh and it also contains
content filtering such as uh safe
attachments in Outlook and in uh teams
uh but also in in in in one drive uh and
it and it contains safe link so what
this does is if you click on a link in
an email or in in teams it will scan the
link first or the attachment for that
matter before actually giving you access
to it and another very nice
functionality of this uh of this uh um
of this yeah of this of this add-on is
that you can do attack simulation and
training for your uh for your end
users so I've got a small demo of uh an
attack simulation
so what we can configure and this is
within a different portal this is in
security.
microsoft.com hopefully
so in the bottom here we have email and
to show you real quick how easy it is to
set up the threat protection policies
it's basically going to email and
collaboration policies and rules and
then clicking threat
policies uh preset policy uh preset
security policies and simply flipping
the switches here depending on whatever
you like uh so it's very easy to uh to
uh to configure once uh once the add-on
is in
place a tech simulation
training um we can create a new
simulation and the goal of this is to
create user awareness for all kinds of
uh all kinds of scenarios that you want
so for example uh if you want to train
your users on not clicking on a fishing
email you can send them a fake one uh in
order to train them afterwards if they
have clicked the link uh what to look
out for it look for the domain name look
for uh recipient or look for the sender
uh for example um and we can create a
new uh new simulation
here uh there different techniques
available the most useful I think is the
credential Harvest because this is
actually a simulation where the user has
to enter his or her credentials into the
system but there are also different ones
like a malware attachment and Link in
attachment and link to malware and
Etc um so if we go for a credential
harvest in this
demo and call this demo as
well we have uh quite a few uh
payloads available that you can choose
from or you can decide to create your
own payload if that's what you uh if
that more uh if that works for
you um to give you an example so there's
for example the reset password
one so then the user will receive an
email with uh hello username password
for email address expires today marked
for deletion if not conf today change or
rather keep using the same password and
there's a button where they have to sign
in on the on the
website
um yeah for this demo can take the same
one so we take the reset password one
there's a login page attached to it
which also looks like the Microsoft
login
portal uh and we can see when the
simulation was launched last but
obviously there's none of this one so we
can take the reset password and hit
next here we can uh include or exclude
the users that we want to that we want
to uh test with this basic
test um so for example we can say John
again
here there he
is add one
user next and then we can exclude some
Target users of the ulation if we
like uh and then we can assign training
so for when when John clicks the link uh
he can automatically be uh be uh be
advised to do some training and the
training is is usually a video of of
someone explaining what a what a fishing
email is and what to look out
for um we can do the recommended one and
they will assign trainings for you if
you if you like because you can also
customize this the way the way you
desire
so we hit
next then we have a custom landing page
we can choose different landing pages
you can customize them with your own uh
with your own logo if you want it looks
a little bit like uh like this uh if if
after they've entered their credentials
you get a message like hey username you
were just fished by your security team
it's okay you're human you'll learn from
this and there's all as well the um
there's the tips uh tips to identify
fishing messages as well so in this case
it's the from and the
subject uh here we want to see the
notification preferences for this uh for
this campaign the default is usually
good uh so you get feedback whether you
did good or whether you did bad so if
you report a fishing email uh before
before clicking the link you'll get a
notification saying you know well done
you've you spotted a fishing email or
keep it up something like
that I have to select the
language
um doing is
fine and how often you this is for the
um once you get a training assigned you
can uh here specify how often you want
users to be reminded of the training
that they have to follow
now we can say launch as soon as I'm
done which is
good
next
submit so now if we go to
the office portal to Outlook here we
should receive an email soon
come on now there we go so there is the
uh there is the fishing email and if we
click the link we'll get redirected to a
something that looks like a Microsoft
login portal and it actually doesn't
matter what you do here if you click
next you'll see that it simply continues
and if you click sign in I think you're
you're getting you're getting fished so
um it doesn't even it doesn't matter
what what the user enters here uh but
it's it's it's likely that they they
enter the actual username and password
when uh when doing
this so from the uh
simulation uh from the admin
perspective we can
see uh what users clicked on the uh what
users clicked on the link which was
inside of the
email and apparently we have to wait for
it now
there we go so we can see what users
were compromised uh with this with this
simulation we can see how many clicked
the message link we can see if they
supplied the credentials we can see how
many read the message we can see deleted
replied to forward it who was out of
office even and uh also who who the user
was so we can
see uh click the message read the
message Etc supplied credentials and so
on now I've did this before apparently
uh with this account so hopefully I can
show you what the training looks like as
well because it might be in the deleted
items
here yeah it's in it's in it's in Dutch
but it doesn't really matter so we can
click on the link that we got assigned
uh for
us and and we can see there are two of
them here so internet fishing and Moss
fishing if we click the internet fishing
we'll get a nice a nice video of
uh of of someone who is uh getting
fished apparently and what to look out
for
so you might be
wondering what does it all cost uh
security defaults is obviously free
because it's in the Microsoft entra ID
free package uh conditional access
policies are part of entra
idp1 which is
a560 a user a month uh subscription or
comes with Microsoft 365 E3 if you have
an Enterprise subscription
um privileged identity management is
part of entra ID P2 which is 840 for
each user a month and is included in the
Microsoft 365 E5 Enterprise subscription
Al the defender for Office 365
capabilities are available for €4 and 80
uh for each user a month or
70c I think I made a typo
there um so there there's one more thing
that I want to talk about and apparently
I have a lot of time left uh we share
secrets whether that's API keys or
whether that's passwords uh but how do
we share them with with Partners or how
do we share them with with how do we ask
a customer to give us a certain secret
uh how to do it safely uh my advice is
always never in ticketing systems never
on email and never on teams because it's
uncontrollable if you PST a secret if
you paste a secret on on one of those uh
one of those platforms I would always
advise to use a self use a onetime
self-destruct solution to Simply enter
your password once then share it via a
link and if the you if the link has been
opened once uh the secret is
automatically deleted from from the
system uh so the user has a chance to or
the partner or whoever is receiving the
link has one uh one chance to save it
the correct way in in a password manager
for example um so last year I came
across something called solution called
yopal it's very simple and easy to set
up you can do it in in a Docker
deployment it's like 50 minutes and
you're good to go it's by a software
developer from Spotify and it's also
trusted by uh by Spotify so um um I'll
show you that last and uh then we'll
head off to the beers I guess to the Q
and a
first um
so this is it it's fairly simple uh the
idea is that here is you can write a
secret message and you can say how long
it will stay there until it gets
automatically deleted so you can say for
example 1 hour one day or one week and
you can specify whether it's uh onetime
download or not um and also you can
generate a custom decryption key if you
like so if we say for
example uh PC tech
days
secret and we say this is valid for one
day but it's a one time download we can
equip the message now we simply forward
the following link to whoever is uh to
receive the uh the secret from
you um you can open it once there's the
value and if you open it again it is
gone
uh that's how easy it is um and this
helps I think with with with uh Secrets
just flying around on every platform uh
that you basically uh basically don't
want want to happen um because sharing
Secrets is secrets in the open is is
almost as worse as the secrets in the in
the
code so I've got 28 minutes for for Q&A
which is quite a while uh so are there
any questions in the audience someone up
front I've got t-shirts have you do you
have a
t-shirt I was told there was a box
somewhere but where is
it ah
there you go thank you thank you for the
demonstration uh I have one question
about um what are your views on creating
separate accounts for
administrators uh that's a very good
question uh the the the downside of
account sharing is always that there are
shared
accounts uh so one of one of the one of
the possible issues is licensing
obviously so when you have multiple
business Central accounts in in the
customer tenant for example you need a
license to access the environment or you
need some some kind of Dynamics
administrator uh role within the system
so I would always uh use
um uh just the the same account using
the uh the the partner benefits that we
have or the admin relationship that we
can set up with uh with one of the
customers that was my that would be my
recommendation because it's a lot easier
to do to do connect with other
environments with your own account
rather than with a different account
every
time any other questions I've got two
more
t-shirts I want to get rid of the
t-shirts um you showed uh that you saved
the pass key
before uh in on your computer and and
you said they are synchronized also over
different
um um Hardware or systems but if someone
gets um uh the hand into your password
manager then he has the keys to the
kingdom isn't it like that is it better
to have the pass key also saved with an
MF a to prevent that is this possible um
I don't think it is I don't think it is
possible uh but the idea is obviously
that once you have your pass key saved
uh within a password manager that the
password manager is your your your your
secret so for example when I showed the
uh you cannot get in the authenticator
for example without using phase ID so
that's the that's the second factor that
you are using at all times so without
without the fa without my face the
authenticator app wouldn't work uh so
that's the that's the idea behind it but
if it shared is it if you share this
over different devices then U the the
data itself is not only on your device
so it must be on a server somewhere and
if you have a breach like last pass for
Server only has the the public key in
the in the in the pass key structure
okay so there's nothing more than a than
a than a than a public key and how it
cryptographically works I don't know
because I'm not smart enough for that uh
but uh the the way both devices require
an internet connection that's one of the
things uh and by scanning the QR code
somehow they are able to make a
connection between the two uh and uh
your phone is is actually confirming
that you are who you say you are in this
case at least there are other ways as
well with with physical uh physical
security Keys rather than a phone uh
which work in a similar similar way but
those are protected with with a pin
code instead of the the face of your
face okay
thanks do you want a
t-shirt I'll take it come all the way
up it's a nice exercise
there you
go so could you elaborate on the or
repeat the example that you did with the
when you grab the C cookie information
to to have the Microsoft uh session
open do you want to see it
again yeah like it went a bit fast for
me the how how did you open the console
and
uh so the idea is that maybe I'll just
show you
uh uh the source what is it called
again uh aure aitm I think it was yeah
it's by this
guy
um so this is the source for the Azure
function you simply clone the repository
and publish it to to an Azure function
that's how easy it is basically and how
this is done is actually uh pretty well
documented in his uh in his blog post
here so you can see select the
subscription select no GS a runtime
stack select the region consumption
based is enough and then simply push the
Azure function and then you are good to
go um so
simply it is the
the Azure function is nothing more than
I'm making typos
already this is nothing more than a
proxy between the user trying to sign in
into the on into his Microsoft account
and the Microsoft website itself or the
login portal itself so we're sitting in
between right now so every request that
I'm doing right now is going to the
proxy and the proxy forwards it to the
Microsoft login portal um so this is not
some sort of fake portal it's the actual
uh it's the actual Microsoft portal
otherwise I wouldn't have been able to
uh get the theme out of it either so if
I do this
again I'm not sure if I is the password
correct yeah that's
it so now we get the number matching
63 and in the background all it does is
log the the credentials that I got from
the Microsoft service into the into the
console of the Azure function so when I
moved back to uh to uh uh and and and
and the output of the aure function is
also pushed towards teams that's why
it's in in in teams right here so it it
captured then it was able to capture the
the login name and the password and the
cookie that we got from the uh from the
U Microsoft service and now I can
basically copy the content of this uh
this
post then simply navigate to uh to the
uh to the office
portal without any credentials because
there are now no cookies because
Incognito um and then I go to the page
inspector of the browser so this is a
local then if I try to paste what I got
here from the teams
post a warning appears telling me that
if I don't be careful and I know what
I'm doing uh I have to type allow
pasting allow pasting
first uh before uh being being able to
paste actually and and this simply sets
the cookie so now there are no cookies
which is in uh where is it again
application I
think yeah there are still cookies but
uh not this
one so now the cookie has been set for
the specific Microsoft uh
service and I simply I have to refresh
now and it will recognize that this is a
cookie this is a valid cookie that we
have just created and um for reps us to
uh to the portal
itself does that answer the answer the
question yeah
thanks let me give you the last
t-shirt if there are no more questions
may I ask another one sure uh I've got
no more t-shirts
though uh not sure if this applies but
I'm going I'm going to tell throw you
the question and see what you can make
of it
so we have a business center client in
bc14 on premises mhm and they want they
were in Windows authentication and they
wanted to have the multiactor yeah so we
were trying to to move them to single
sign on and
um eventually left it because we were
not able to connect it to the
aure app that they needed to re to
register I have done it in other bc14
customers so it could be could be just a
mistake we left it because there was no
time but um there was one thing that we
noticed when we review their the rer uh
application uh I'm not sure what I'm
speaking about here
but the V the other installations I
working were s
ML and apparently this was oidc
so we were kind of blaming that uh for
because what happened is it was not able
to reach
the to find the the port the application
when it tried to
authenticate uh so I don't know all I
could see is okay this is different this
is probably the reason why it's not
being able to connect with business
Central so you went from Windows
Authentication into Access Control
service yeah that's it yes and that
didn't work yes yes it could be it could
be a wrong parameter somewhere but we
noticed that the the way they build the
asur Ws had this difference with other
installations I had done before so I
don't know if there could be maybe a
incompatibility between business Central
not being able to to get to to this uh
application because because of this
difference of some sort of SEC security
setting
not using S but using
oidc I don't honestly I'm not sure to be
honest I've done it yeah I've I've done
the access control service
implementation on Prem only a handful I
think like four to five times uh same
here which is quite a long time ago
which was in the NV days so um I'm not
sure what uh what was going wrong there
no yeah okay okay that's okay thanks
all
right so if there are no further
questions uh I wish you all the best for
the rest of the conference and thank you
for for being here today
[Applause]
