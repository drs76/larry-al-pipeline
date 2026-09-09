# BC TechDays 2022 - OAuth revealed

- **Source:** https://www.youtube.com/watch?v=vabiOlBGo9s
- **Video ID:** vabiOlBGo9s
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 100m21s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
but
[Music]
okay
ladies and gentlemen welcome in this
afternoon session your presenter for
today is agrant yan
[Music]
look at those spotlights
hello everybody
so
you all had lunch
and now looking for some sleep
i guess so i mean after lunch
everybody's gonna fall asleep
that would always happen so i'm not
going to blame your topic
just to blame the lunch
so hello
my name is
aaron john kaufman from the netherlands
freelance technical consultant and also
trainer
always been on the technical side for
more than 20 years in dynamic nav
business central
um and you know special focus on web
services apis security etc
and in the netherlands also try to keep
up with the dutch dynamic community
all right so
why do we need to talk about oauth
well microsoft helped me this morning in
the keynote because
there was this slide this is what i took
from the screen so
i added it after the keynote
uh we are moving to oauth
very soon first of october
so that is um
in two weeks from now
so if you have not moved to oauth you
better move
fast
with a lot of work oh maybe not maybe
hopefully after this session you have an
idea how to do that
now one of the reasons microsoft gave
here or the reason is security
security security
yep
you see what i saw that's on that
picture beneath
for those who have already worked with
oauth they probably recognize
uh that
oh so
they recognize here
an access token
you know what this is
i'm going to click on it
so you can read it for yourself
microsoft teams stores the tokens as
clear text in windows
how about security microsoft
i mean
this can be
simply leaked
with a simple attack
and then attacker has full access
so
what can we learn from this
oauth is not secure in itself
or auth is as secure
as you understand and apply it
if you don't understand and apply it in
the correct way it will still be
insecure
and even microsoft is sometimes getting
it wrong
okay so i proved my point
and now i have to get
get it right myself of course
so
you know this meme
how to draw an oil
people give you two circles and they say
okay
now you draw the rest of that all
yeah
to translate that to
oauth they say okay we're going to do
our art
you create a an app registration you
have a secret and you get an access
token that's it
and all the steps in between
to get from those two circles to that
all
to get from an app registration to an
access token
yeah you have to figure out yourself
to read here read there read the blog
post and
well that cannot be that simple because
there are a lot of terms
going on
and i hope to
well
catch most of those words that are on
this slide
so odd
what is it
oh old this is the definition of a world
i don't understand exactly definitions
not for me but okay this is the official
definition and
this is not managed by microsoft it's
managed by an external group
of companies it is an authorization
framework
to enable and that is what it is about a
third-party application
to get limited access to an http service
in terms of business central
to get an external
application to get access to
business central
data over an api
call a request
but it could also be the other way
around
from al code get access to something
outside business central like sharepoint
email
onedrive you name it
so it is a authorization framework
and it has many faces
in oh art we have four different roles
that are important
and i will build the story on these four
roles
we start with the resource server in
this case we put the name business
central on it
resource he means something that has
data
so the business central server is the
resource server exposing data to the
outside world by means of http apis
then we have a client application not
being the web client that is a
application of business central itself
that has access
now an external application created by a
third party
and that client application wants to get
access to those resources
because there is a user
who is an owner of the resources so that
is a business central user who wants
that application
to read data or maybe send data from
business central
so he's going to use an external
application not a web client
and
business central knows that
user of course but it doesn't know that
application
and that is where
azure active directory comes in that's
the authorization server
business central
is
does have a
registration in azure active directory
created by microsoft we will see more
about that in the middle in a minute
now that client application
also needs to get a registration in
azure active directory
and then
the client application can request to
that resource owner please
give me access to your resource
and azure active directory can store
the granted permission from the user to
that client application
and if that client application can prove
to azure active directory that it is
really the resource owner that is trying
to get access
the resource owner can prove that by
logging in
and if the client application can prove
that he is really the client application
that he says he is
then azure active directory gives him an
access token
and that access token is then sent to
business central together with a request
with an http request and business
central can check that token and then
revoke access or give access
so that app registration that is an
important part
it starts there
it starts in the azure portal azure
active directory and there we have a
option in the left menu app
registrations of course you're going to
see that in a demo later
in that app registration we have the
definition
of the application
the definition
so that includes the name maybe your
logo the publisher so the company was
publishing it
it contains redirect uris it contains
secrets it contains
api dependencies
which
resource
is hikong to need
without a required resource he has no
access so you can store there which
application
do he wants to access
it can have published apis
the application on itself could also
expose resources
which is for example the case with the
business
central app registration
it exposes data
now that app registration only exists in
a single directory an azure active
directory
that is called its home directory
then we have another
thing in azure active directory and that
is the service principle
in the menu in azure portal that one is
called enterprise applications
don't ask me why they have give it a
different name in the menu but sometimes
they do as we will see later in other
places that is happening as well
anyway the enterprise application or
service principle and i prefer to use
the word service principle
that is an instance of the app
registration
so
think of it
in terms of al code
we have a code unit
written
in an al file
but that doesn't mean that that code
unit is loaded into memory
it is loaded in into memory when we have
a variable of type code unit for that
code unit that is the instance of the
code unit and we can have many instances
of one code unit as many as we have
variables pointing to their code unit
so the same happens with a service
principle it is an instance of
the application registration the app
registration
and on that instance
we have the granted permissions
now this is an important difference from
the required permissions
in the app registration we
can
configure which permissions which access
does it need
in the service principle we store which
access has been granted
and based on the granted permissions he
can get an access token
and that service principle can only
grant access to something
that is in the very same azure active
directory it cannot grant access to
something else outside the azure active
directory
let's see that in a picture
there's going to be a lot of pictures
here so we have an azure active
directory the blue box
and inside there we have an azure app
registration
in the top and that one is also a link
to an
service principle that's its instance
that's how it starts
the moment that you create an app
registration in your home directory you
also get that service principle
now
the next thing
hey
okay i was hoping
okay sorry this is what we call a single
tenant
so a single tenant everything is inside
the single tenant
we also have something that is called
multi-tenant
when we have an
app registration that is multi-tenant
then the app registration stays in the
home directory
but the service principle can be created
in
other
azure active directories
and in the other active directories it
can be granted permissions to resources
inside the other azure active directory
now
when we create an app registration this
is one of the choices that we need to
make is it going to be a single tenant
or a multi-tenant
and the answer to that depends on
which users are going to use that app
are they only inside
this home directory then you have a
single tenant application
but if users here
also needs to
make use of this app
this app this client application then
you can create a multi-tenant
app and then a service principle can be
created in this azure active directory
how that happens i'll talk about that of
course
so what do we use that app registration
for
what is the purpose of an app
registration
actually we have three possibilities
here
first of all we can use it for user
authentication
just
getting access to the details of a user
reads it details
who is he what is his email address
whatever is stored in azure active
directory
another access that we can have is
saying i want to have access to other
resources
data that is exposed by other
applications think business central
because will be sharepoint could be
email
that access that he requires
needs to be granted just saying that you
need access is not enough
then on the other side it could also
expose resources it could be
a server that
as a server application is data behind
it that wants to expose the data with an
api
and then it can also register
the api endpoint the name of it and say
okay
another application can get access to my
api endpoint
under this and this name and with this
and this permissions and rules
there's another part of app registration
that's actually what microsoft is doing
with the business central app
registration they created an
api uh
exposing so it's exposing an api and
saying okay we have an impersonation
scope here and we have an
api.redry.all
row a role there
we will talk about it more detail but
that is what happening with the business
central
application
so
when the application wants to access a
resource
he needs to
get permissions to the other resource in
fact
that is the other resource is just
another service principle in the azure
active directory and then between
the service principles there is a
granted permission
now the question is where does that
other service principle come from
well from another app registration
and if it is single tenant
that's obviously then the other app
registration is also in the same tenant
then for example we could have a client
application let's say
it could be a powershell script it could
be a console app it could be whatever
application
that wants to get access to an
internally developed application for
example
a portal where somebody can
enter time registration or other
on the service principal level the
permission is granted
now if
we put that with some bullets here and
um
that's too fast if you put some bullets
here in the top we have the required
permissions so that is only on the app
registration doesn't mean that the
permission has been granted but the
granted permission that is between the
two service principles
this is the single tenant part
now what about the
multi-tenant part
then
we can have a multi-tenant
app registration let's say in a in
another
azure active directory
that app registration is multi-tenant
and that app registration can have a
service principle
in your home directory and you can grant
permissions
to put some names on that
business central
is registered in the azure active
directory managed by microsoft
and it is a multi-talent application
exposing
apis and
the app registration in your home
directory says i want to get access to
that exposed api
and
then the permissions if they are granted
are registered on the service principle
and the service principle here
this one
represents the application of microsoft
regis that is registered in their active
directory
to make this a little bit more
complicated we can also have this
scenario
what do we have here
we have an azure active directory where
we have
an app registration
it has a service principle
but also here a service principle
and let's say
this directory is a directory from an
isv or a partner
creating an app
and that app needs access to the
business central resource
of the customer
so the middle one here is the customer
this app registration is not done here
it's done in the isv app at the isphere
home directory
but
the moment
that
somebody here
grants access to this app registration
to
this app registration
we have a granted permission on service
principle level
so we have a service principle from
business central and a service principle
from the web shop
so let's
make that picture a little bit more
clear
it's this because we're not talking
about
an application that we're using
ourselves we're talking about an
application that is sitting in that or
sitting in the home directory on a
microsoft directory with a service
principle in both customer in the
customer directory
but hey
this piece
where does that come from
because that service principle
is created
in the home directory the moment that
the app registration is created you get
that service principle there
automatically
but how do we get that service principle
in that customer directory how does that
service principle from business central
come there and how is our webshop
service principle
being created there
that is actually the question
so how are the servers principle created
in the home directory
they are created the moment that the
application is created that app
registration is done
if you use the azure portal
app registration
if you would not use that but you go
with the graph api there's also a
possibility
then you need to do it yourself
then you do one a craft api call to
create the app registration and the
second one to create the service
principle
in fact azure portal is doing two calls
and not only one
in the foreign directory let's say that
customer directory
it can only create a server's principle
if
the app registration is multi-tenant
otherwise it stays inside the
home directory and does never leave it
and it is created the first time when
permissions are granted
that app registration
starts with requesting
permissions
requesting consent
from the user do you allow me to get
access to your data
and the first time
it starts with business central
is
asking the user
do you allow me to read your data
otherwise you cannot authenticate them
so
the moment that the user says to
business central app yes you may read my
details the service principle for
business central is created in the
customer directory
that service principle comes from an app
registration that also says hey i have
apis exposed
then the web web shop example
comes next it says hey you have the
resource please give me access
and at that moment that the user says
yes
you get access to it the service
principle for that webshop application
which could again be anything
is the server principle is then created
and together with it
permissions are granted
to the service principle of business
central
okay permissions
so
permissions and are granted and what is
all of that what does that exactly mean
permissions
are
well something that an application
requires an application requires access
to a specific resource that you have the
term resource again
a resource is just another app
registration that is exposing data
exposing data usually done with a rest
endpoint
it could may be something else but
usually it is an http rest endpoint
access to that endpoint to that exposed
data is managed by scopes and roles
there is something that is done on the
app registration there
the person who manages that can set
different access levels
if
another user
is allowed
to access the data
with a third-party application on behalf
of that user
then we call that a scope
that's the official term for it
we also have roles
and roles is something that is widely
used in azure active directory or in the
azure portal actually for access
management somebody can have a role and
then get access to certain parts
well there are two types of roles
that play a role
you have the user role which can be
assigned to a user or a group of users
and we have a application role
which is a specific rule type because
you do not assign it to a user
now you see the user role line is gray
that's for a reason because that does
not play a role here
the user role
is in fact not used because we have
scopes for that
with a scope
it is possible for an application to
access
business central on behalf of the user
with an application role
there is no user behind that application
but instead
he accesses the data with his own
application account his app registration
account in fact
well you may think okay
this is a little bit confusing and
i i don't get the picture here you will
get it later hopefully when i going to
do the demo and point you out in a demo
what
exactly is related to these slides
to give you some examples of scopes and
rules and hopefully you already
recognize this here something
a scope could be api business central
dynamics.com slash user impersonation
that is a scope defined by the business
central app registration in the
microsoft directory
another scope could be
craft.microsoft.com
mail.read
well what in fact
this is built up as a
url as you see here in fact it's a uri
and up to here
this identifies
one app registration
and the second part is in fact the
permission together we call it a scope
this is one time
app registration that is done and this
can be multiple types
in the graph we have not only mail read
but you also have mail read write and
mail.send
file dot read file dot read write
there's a huge list of scopes
you also see an application role here
api.readwrite.all on that same
resource here so this resource and this
resource at exactly the same
but
this one here is api read write.all
which is an application role it's just
because that has been registered under a
different page on a different
property in azure portal
we also have mail.read and that looks
the same as scope
well
that is because in the graph
environment i have chosen to
[Music]
give the application role the same name
as the scope
so we have the same name but it could be
two different types they're gonna be a
little bit confusing
business central chose to have user
impersonation and api rewrite.all
as two different names it could have
been api read write all
on the scope as well
the user impersonation is actually what
it is about
well
you see the two pictures a little bit
blurry but
i hope you can see and read that here
request api permissions this is inside
the azure portal and here it says
delegated permissions and over here it
says application permissions
delegated permissions is in fact another
word
for scopes
i cannot help it here we have another
example where
being behind the scenes it's called a
scope
but in the azure portal ui it's called
delegated
sorry about that
you also see on the
right screenshot
and trust me we're gonna be there
later on when the demo but you see here
type and application and delegated is
exactly the same thing
now the moment
that
the service sorry the application
requests
to the user
grant me those permissions i've not only
told you which permissions i require but
now i want you to grant me those
permissions
that is called the consent though
consent flow
and you probably are familiar with
this
picture the pop-up that is asking
consent to the user
now there are many
consent flows
we have a user consent flow which is the
process where a user is granting
authorization to an
application only for his user account so
on his behalf
that's what we call a user consent flow
we also have an admin consent flow
and that happens when an admin is
granting consent because an admin
can grant permissions
on behalf of the whole organization
so the individual users do not get this
question anymore
that's what we call an admin consent
and it is a different page that the user
can be sent to please log in as an admin
and grant as an admin for the whole
organization
if
and that is
the difference between uh well the the
different
flavors of the consent flow
if there is a user consent flow so
asking a user for permission for his
resources
but if that user is an admin
then there will be this little box here
consent on behalf of your organization
optionally if he doesn't tick it
he's only granting for his
personal user account
but if he ticks the box then he's
certainly in the admin consent
granting permissions for everybody
i hope you see how many different
flavors we can here
we can have here then we have the
application role type
where it is not a delegated
permission is not linked to a user but
the application role that an application
is using his own account to get access
that can only be done by an admin
not a user
think of that
as creating a new user account in azure
active directory
users cannot do that
only an admin
can create new user accounts
an application role is in fact another
user
type application a new service principle
and not a user
principle something that also exists in
azure
so he's creating a new application user
in fact and that
is only be possible with an admin
user
well you see that a link and
actually i found that one
when i was looking for for this and yeah
i didn't want to go there now
this one is actually a very good
overview of all the different flows
completely explain what every part of
that page means
and not only that one but this is the
next one
and the next one and the next one and
another one
all kind of different situations that
can happen during the
requesting authorization so
actually a very good resource to read
now so far i have been talking about
server principles permissions there are
some other parts in the app registration
that also play a role they didn't touch
yet
we're talking about
the difference between a public app
versus a confidential app
which is related to something that is
called redirect uri
something i believe most people are
struggling with that one what exactly is
a redirect uri and how
what what does it do
i've not talked about secrets
well that's a secret so let's keep it a
secret oh i need to talk about secrets
of course i've not talked about dynamic
permissions versus static permissions
and of course
the access token itself
because whatever we do at the end we
need an access token
and that is actually what i want to talk
about now
and then later on i come back to the
redirect uri
the and public and confidential clients
the access token is used to prove that
an external application in fact has the
permissions
it contains all required information who
is the user in which azure tenant id
is he um what kind of access does he
have is this a user or maybe an
application
what role does he have
when did he require when then when did
he acquire that token when is the token
expiring all of that information is
inside that token
you see here and
a call how that looks like api business
center nemours.com there's v2 we know
that endpoint hopefully it's less
production or could be less sandbox less
development whatever name you have for
your environments and then slash api
okay
what you do not see in this url is the
tenant id the azure tenant id
that is not required because the azure
tenant id is in fact in the access token
so this long string here
contains that information so we don't
have to put it in the url anymore
well what is that token
it is a so-called json web token
which is a base 64
encoded value well in fact a url encoded
value
a url encoded value means that
it does not contain slashes
it will be placed with i think a dash
top of my head it does not contain
now there are two characters actually
removed and the equals sign is removed
from it but you can replace them back
this is just encoded so that it can
travel over a url
it is base64 encoded which means that
you can just decode it to read it
it is not a secret
what is inside the json web token
you can just decode it
you can even write code in business
central i've done that to decode a json
web token
it's just a matter of splitting it up
because it consists of three parts
divided with a dot
then
you take the middle part out of it
and in the middle part
that looks like this is a json structure
you can do this yourself also at
jwt.io
or dot ms i usually go with the first
one because that gives me a little more
information
but okay if that json web token is that
simple then everybody can create it
right
well yes you can create it of course
but
the json web token is a secure token
because it is signed
signed with a private key from a
certificate
and that means
that somebody some application that
receives the json web token
can
check and verify if their token is valid
and really created by the owner
of that private key
it's in fact done with hashing
information and encrypting the
information
and that is in the bottom of the json
web token as a signature
and the signal tool can then be
it with the public key that belongs to
that private key
and you can check the hash
if the hash does not match
then it is not a valid token
you can even do that in al i've done
that
last week actually creating json web
tokens with a certificate in alco al
code and sign it and it works like a
charm actually
if i have time at the end i can show you
the code
business central uses this json web
token to identify the user and to see
hey what does he have for permissions
and inside that uh that token
um we have for example the
let me see organization id we have a
scope you see here hopefully you can
read it user impersonation
the the name of the user
we have
the audience
api business center the nimbus.com so
for which application is that json web
token meant
all of that is inside that json
okay so the question is how do we get
that access token
well there's a
list of flows here and with flow we mean
a
series of steps
that you can follow in order to get a
token
and every flow has a different purpose
and i cannot discuss all the flows here
i have to make some
choices
so the only two flows that i want to
talk about is the authorization code
grant flow and a client credentials flow
because the others are for specific
situations
there's one flow that
many of you have also experienced
from the others
i guess you all have seen that if you
publish an app
in vs code
to a business central online sandbox
you get that little pop-up that says
here is a code
please click on the link and paste the
code in the website
and then the website says okay are you
this and this user trying to log in etc
and in the meantime vs code is waiting
for you to finish that process and when
you have finished
he will continue publishing the app to
business central
that is the device code flow
a specific flow for applications that do
not have access to a browser or do not
have their own
browser window
especially and that's why it's called
device code flow for tv screens
okay but i want to focus on the
authorization code grant flow
and the client credentials flow because
the first one authorization code grant
flow
is used to get
delegated access on behalf of a user
that is where the word authorization
code comes from
he's asking the user to give him access
to
business central for example
and if he has the access then
azure is going to give an authorization
code
and with that authorization code he can
get an access token and that is the
actually the
the flow that most people are struggling
with
because
a redirect uri is
involved here with secret is involved
you have user interaction that can be
really
confusing how all of that works
the client credentials flow on the other
hand is the easiest one
just one call and you have access and
you have an access token
so should we all go with client
credentials flow then because the other
one is so difficult no because the
authorization code cranflow is to access
data on behalf of the user
and the client credentials flow is to
get access on behalf of an application
account
and you don't know who the user is
so
the authorization code grant flow
is used in a user interactive session
you're going to access the data on
behalf of the user and that requires
that a user is locked in
so the first step in that process would
be to let the user log in if he is not
already locked in and recognized by the
browser
of course you can say but wait a second
i don't want him to automatically be
recognized and you can add an extra
parameter say always prompt to login
you're going to access the resource on
behalf of that user this is when we use
the authorization code cranflow that
means that the permission type that we
are talking about is of type scope
aka delegated that is what is named in
the azure portal
that also means that in the target
application business central for example
there must be a user account
for the same user that is logging in
into the application
the client credentials flow
is also known as the service to service
authentication
you don't see that in the docs for
microsoft but that is the authentication
type that
microsoft likes to talk about but at
least from business central perspective
um mostly used by a background session
where there is no signed in user
thing an
azure function or
a web shop application where
the users of the web shop are not users
in business central but are the
customers of the customer
so they cannot log in into business
central they cannot give access but the
web shop needs to get access to business
central in order to get inventory
information create sales orders shipping
information stuff like that
the permission type in that case is then
application role and not
scope or delegated but that also means
that there must be an account
in business central and we call that an
application account it's just another
record in the user table that is not
linked to a normal regular user but is
linked to an application
an app registration
type user type application
well how does that authorization code
grant flow work
if you look it up in the docs you're
going to see this
schema
this flow
yeah i don't know about you but if i see
this kind of pictures
most cases i just skip it
it's way too complex
unfortunately i have to come back to
this picture because every everything
that i need is in here
so
let me try to explain it a little bit
in the top here
you see two blue boxes authorized and
token
that are two
different endpoints
on the azure api
the azure api which starts with
login.microsoftonline.com
and then it is even less tenant or less
common well slash organization should be
used but that's on the next slide
but two end points
the first endpoint authorized
is something that is opened in a browser
it displays a web page
a webpage that
asks the user to log in
ask the user for permission
if he grants that application permission
which is by the way and one time
question the next time he would not ask
that again
so then the second in order uh times
that he logs in he will just
skip the
grant permission question
and that is what happens here the
application
opens a browser dialog pointing the user
sending the user to the authorized
endpoint
with some parameters i am this
application requesting access to this
resource
with this scope
the user
follows the flow
in that web page to log in
maybe give permissions the first time
and then
that authorized endpoint
is going to send the user back to the
application where he came from
that is the
redirect sending user back to the
application
because
azure
does have something for that application
an authorization code
telling the application hey this code
tells you that you have got
permissions from the user to get access
to his resources
now that application needs to grip that
code
out of that redirect page that is opened
in the browser is the final
place where the user goes to
and then
he goes with that authorization code to
the token endpoint
and he gives some details to the token
endpoint hey
this is the code that i got from the
first step
this
is my application id this is my secret
please give me an access token
and if everything is verified and okay
by the token end point
then the token endpoint replies
with an access token
so this first part authorized is a user
interactive browser
this is just showing a web page
series in the browser the second one
is an api call behind the scenes the
user doesn't see it
so this is just an api call to the rest
endpoint
of the the token endpoint of the
azure api
and then when you have the access token
you can use it together to call business
central
explained in more detail
here you see the full call for the first
step to the authorized endpoint
this is a url that needs to be created
by the application
and
there must be a browser
dialog opened somehow
so that the user is opening that login
page
you see here
inside that url log into
microsoftonline.com you see the domain
name in this case chronos.company
there's a domain name that i put in
there by the way that one really exists
chronos dot company is a domain
you see at the end authorize here
if
it is a multi-tenant
application
then you do not know
which user is going to log in
it could be a user in your active
directory it could be a user in another
active directory
in that case you do not
provide the domain name in the url
you provide the word
organizations
you may have seen common
instead
that's also possible the word common
also works the common is
more
broader that is also used for non-work
accounts also for
personal accounts but we don't support
that so
you should go with organizations and you
will see in the demo that actually
microsoft is also doing that
the second
part is the client id
that client id is assigned to that app
during the app registration you just
create an application and you get a
client id
the third part is the code
response type i expect to get back a
code
an authorization code that can later be
redeemed for a access token
this redirect uri is the place where you
want the authorization code to be
returned now this uri
needs to be
a web page
that your application owns
because otherwise he does not have
access to that page and the
authorization code would be sent to a
different application
so it is very important that you have
access to that redirect uri
or
if you have an application that likes a
desktop application that opens up its
own browser window
of course it can be any url in that case
because the application can just see if
that browser window is navigating to
another url and then say okay thank you
i grabbed that url on that url i will
find the code and i'm done but that is
for
desktop applications only for web
applications working in a browser
this url
must be a url
that is hosted by the same application
otherwise you do not have access
this property just says that the
authorization code needs to be added to
that url from step from number four
in a query parameter meaning it's going
to be question mark code is
and this one is the scope
the permission that we request
a this permission in this case user
impersonation on the resource
well
this is opened in a browser window
somehow
the user is logging in
as your active frequency says hey
do you want to grant access first time
to
that application he knows the name
because the client id is here
knows the name of that application do
you grant him access to this resource
they say yes that's okay and then azure
is going to send
the user back in that browser window to
this redirect uri
and it looks like this
in the browser window or in that
application window there is a redirect
to this app to this url
with an app a question mark code equals
and then a very long code
and a session state so the redirect uri
from step one
an authorization code that is important
for that application because that needs
to be used in step number three
that authorization code will be valid
for 10 minutes
so in ten minutes he must take step
three otherwise that code is expired
and there is a session state which
cannot be used for single sign in but
for single sign out
when usually ignoring that one that's
for web applications who wants to log
out a user everywhere he can they can
use that session state logout
and this is kind of a cookie that you
can store somehow
then we get step number three the
application
retrieve that code from that url from
that
redirect uri and then it's going to make
an
http post request to the token endpoint
so a post request to the token endpoint
of
azure
it is exactly the same url as in step
one but only the last word is different
so here
oops
i need to go a lot of click here
here you see the authorized endpoint
and this part is exactly the same as in
step number three but now it is called
token
that is not a user interactive thing is
it a real api
he's going to post some data which is
always in the
format in the content type
[Music]
form url encoded this just tells him
that this body
is in this format
the grand type that i want to use is
authorization code
you will see when we talk about client
credentials that
is going to call this the very same url
but then grant type is suddenly client
credentials and not authorization code
on number four we see the code that we
retrieved in the previous step
on that redirect uri
then we provide also the identify the
the credentials of the application what
is the client id what is the redirect
uri
that was used
in the previous steps so where did you
get that authorization code from
because one application could
potentially have more than one redirect
uri
and you need to use the same redirect
uri here is where you got that
authorization code from do not pick one
of the others because the azure will say
sorry but this code does not match that
redirect uri
the scope must be repeated here
and then we get a client secret
the client secret that identifies the
client
there is more to that secret i will come
to that in detail later but the client
secret is in fact used as a password
in the you as your portal you will see
the word secret
if you look into the graph api
it is not called secret it is called
password
and when you click on add new secret
azure portal is calling the api add
password
just saying
now i have a question for you just to
think about it
i will come to an answer later but the
question is this
if basic authentication is not secure
that's what microsoft says right basic
authentication is not secure
why is it not secure
because the
password
is in the request basic authentication
passes in a username and a password
inside the request in the header
base64 encoded so that's not so secure
because the password travels over the
internet over the network
okay fair enough
but what happens here
there is a password a secret in this
call okay it's not in the header
it's in the
body but that makes no difference in
terms of security
there is still a secret a password we
call it a secret with this effective
password
still traveling over the internet
and somebody would be able to unencrypt
this
they have their hands on the secret
how secure is that
compared to basic authentication does
that really add a lot of security
i will come to that later just think
about it
okay
it is demo time
what i'm going to do is
switching to azure portal
creating an app registration making some
calls to get all of this what you just
have seen
so let me switch to the demo
okay
demo god thank you
it was a joke
just to see if you're all awake
okay
this morning i saw a tweet that's saying
pro tip
add randomly somewhere in your
presentation a blue screen of death
forget where it was
because the adrenaline will keep you
sharp
okay
what would be really prank is if you
have a co-presenter you don't tell him
that you put it in there
i tried to convince other presenters but
they didn't want it okay so
i'm here in
an admin
user and i'm going to the azure portal
and
in the azure portal i go to the azure
active directory
and
in there i go to
app registrations
and i'm going to create a new app
registration
i'm going to call that a bc
tag days
demo
now we see already here the first
thing that we need to decide on
which who can use this application
this organizational directory
kronos company only so by the way the
chronos dot company is really what we
are in here so i own that domain
do you want to have any organizational
directory which is multi-tenant
or
is it going to be accounts plus personal
microsoft accounts or only personal
microsoft accounts now the
last two options should be ignored we're
not working with personal accounts like
skype xbox outlook.com
hotmail and all these kind of accounts
so only talking about the first two
options and in this case i'm going to
use a single account a single tenant
only
and i have a reason for that because a
multi-tenant
is a little bit more secure
and can only be used if i have a
verified publisher
but that means that i need to register
my kronos company name with microsoft as
a verified publisher and you want to see
a document that is really an existing
company and it doesn't exist this is
demo so
i'm not going to do this so i choose
accounts organization directly only
single tenant that will do for the demo
and i get here redirect uri which i will
now skip
for this moment
and go to register
so i have now registered for my
application
um if i need to zoom in by the way just
say the word is it can everybody read
this
perfect okay thank you
then um i see here the application or
client id
both are used application id or client
id both terms are used
everywhere and they just mean the same
sometimes you see client id sometimes
you see application id
you also see here object id object id
you should ignore that object id is in
fact the primary key of this record in
the azure active directory ignore it we
are talking about the application id
that identifies him to everybody
so i copy that one because that is the
one that i need to use in my requests
so i have prepared some of the requests
here this is my client id
this um
because i'm going to
use a delegated flow
that means that i need to have a
redirect uri i need to have an
interactive login and the user needs to
be redirected somewhere
so
that is done i skipped that in the first
place but now i have to do this
that is added under platform
configurations
now
here i have a couple of options
and i have also a slide about it but
24 minutes left so let me already
explain what the difference is here
we have the option web
if the option is web
then i indicate to azure that i'm
working with a web application
now obviously what is the characteristic
of a web application
that
it runs with a client in the browser
right
and in most cases there is a back-end
server
that is then accessing the data
which means that i'm going to use the
browser to let the user login
and
let him redirect to a uri to a url that
is hosted by the very same application
in the browser
that means that the authorization code
ends up in the browser
and needs to travel from the browser to
the server back
so the server can use it to get an
access token so there is an additional
traveling of that authorization code to
the server
at the same time the server
needs to use their code to get an access
token now if
somebody could get that access token in
between then he would get the keys to
the kingdom
because he could just know okay this is
this client id and blah blah blah
i get a token
and to um
make sure that that attack it's an
official attack
that is documented in the oauth
documentation
that that attack does not succeed
the web application on the server
needs to have a secret
to identify himself that is really the
application that belongs to that login
page
we call that in other words a
confidential client
and a confidential client is a client
that can keep a secret because it's on
the server users don't have access
so if i choose here
web
that also implies that i need a secret
in the final step
i skip single page application mac os
androids but this
mobile and desktop applications is the
other type that i want to point out
a desktop application is not
confidential
because a desktop application can never
keep a secret
you see even teams from microsoft cannot
keep secrets
don't be like microsoft
don't store any secret data somewhere on
a desktop computer there will be
somebody who finds out where you put it
registry an encrypted file whatever they
will find it
that means that a desktop application
cannot use a secret
but
a desktop application usually is capable
of
opening its own browser window
that means that everything stays inside
that application
ah okay
that's nice because then it's still safe
you do not need a secret in that case
because that authorization code
comes back into that application and
never leaves it anymore so it cannot be
sniffed anyway
so i'm going to have
a web application and a redirect uri i'm
going to use a very simple one just for
the demo
localhost
the only
uri that i can use without https
otherwise it must be https
so i configure that
and i see now here under web
one redirect uri i can have multiple if
i want to
then
i have a certificate and secret
and here i can create a new client
secret that i need the password
um expiration excel okay six months
and here i have my
secret value
that i also need in my demo
there we go
you cannot take pictures now and do the
same because now we have full access to
my
environment
so rest assured i'm gonna recycle this
after the the demo of course
okay so here you see the scope that i
want to have access to
it looks maybe a little bit weird but
that is because it is url encoded what
the full value is in readable human
readable characters as this one
well here i have my authorization code
the request
the full request that i actually need to
send a user to in a browser window
that's what we are going to do
and just
click on send request here
this is the output oh this is not a
browser window
okay so let me
get the full url
here it is
this is my browser window that there's a
user in the same active directory that
is going to login
so i
click on that one
and there we go
logging in
entering my password
there we have the permissions requested
this is already something that many
people struggle with but now you see how
easy it is
apparently
my user is an admin user so he could
click on consent on behalf of the
organization not going to do that but
here you see the permissions
full access to business central
ok full access
does that mean that he is a super user
no
it just means that he can have access to
business central on with his user
account still restricted by the
permissions assigned to the user account
in business central
so i say accept now he is trying to open
localhost
that does not work because nothing is
waiting at localhost
so
give him a few seconds to figure that
out
the browser will
come up with not found something
yeah come on you can do it
please
come on
usually it doesn't take that long oh
there we go localhost could not find
localhost let me copy
that
[Music]
url
paste it in notepad
and here you see that he's opening
localhost
with a code
which travels all the way up to here to
session state this is my
authorization code
this is the value that i need to grab
with an application from that url
whether it's a web application or a
desktop application this code needs to
be read from the
from that redirect uri
so i'm copying that so i got it
everything is manual here and i go back
into my
demo here
and
[Music]
i want to get an access token
and
delete that code and paste a new one
this is exactly the same
request that you saw on the slides
the client id is here the redirect uri
scope secretary
variables
i sent that request
and
here i have an access token
if i grab this access token
all way to here
ctrl c
go to
jwt dot io
paste it in here
and here you see the details
audience that's the target resource ap
is identified with api business center
on demos.com
i am
this user
and
i was asking for
let me see
user impersonation this is my scope
so this should be a valid access token
that will expire by the way in 60
minutes
so i still wonder why teams is storing
those access tokens because they expire
anyway
so you should keep them in memory
so this is my access token is already
stored here in this variable
and that means that i can now get
well
a company id
together with the authorization header
bearer and that access token
let us see
let me make the request a little bit
easier there we go
this is my company id
ctrl c so let's add that one to the end
of the url
and then
take customers
send a request
and there we go we have a list of
customers
so
it just works
okay so this is the authorization code
grant flow and it depends on your
application how you are getting
the authorization code and how you are
getting access uh of how you are
using that redirect uri
okay so let me resume
ah come on
we should be
much farther in the presentation
where is it
yeah
this is the place where we finished
right
okay
that redirect uri
explained to you
is required for user interactive flows
used by azure to send back that
authorization code back to the
application
and there are some extra parameters
added to it
now you register the redirect uri under
one of the platforms
and the platform type defines if a
secret or a certificate is required in a
final step
and that is confidential or public app
web application is a confidential app
it could be a single page application
mobile desktop
sorry confidence app in a single page
application a mobile or a desktop
application they are public apps they
cannot keep a secret
confidential app runs on the server
user has not direct access to it
and the authorization code that is a
characteristic of it
goes from the browser from the client to
the server in order to
let the server
exchange it for an access token while
the public application russell usually
runs on a device on a desktop and
runs in a web browser
sorry in an application window
of course
there could be an interaction with a
browser that's a little bit more
technical how that works but at least
the authorization code could not be
sniffed
that is the correct characteristic of a
public application
then we have something that is called
client credentials flow
that is um
the same
uh post as we saw earlier on the token
endpoint but
now
it is a
only one request that we need to make
in that url we must provide
the domain name that is mandatory we
cannot use common or organization
because we are logging in as one
application inside a specific azure
active directory
content type same thing the grant type
is now client credentials and not
authorization code
we provide the client id and the secret
and the scope and that's it
and we will be greeted with a access
token now let me do a quick demo of this
i see i have 10 minutes left so i need
to speed up a little bit
so how does that work
here i'm back in my app registration
what i need for client credentials is an
api permission here
hey
i did not touch this before but i did
get access with the delegated permission
didn't i
well that is because i used something
that's called dynamic permissions
request the permission the moment that
you ask the user to log in
we define here on the app registration
level
is called a static permission
that is register the required
permissions upfront
the static is in the definition of the
app registration
for delegated permissions is actually
not required we can access them or ask
them to the user the moment that we need
it
we don't have to do it up front
but for a client credentials flow and
application permission it is required
so i add
click on add a permission choose
business central
choose application permission here
and then
grab api read write dot all
i added permission
and i have it here in my list
and i get an exclamation mark here
saying um
not granted
well i can do that here grand admin
consent
oops there we go
and
now i have
everything
to get an access token
so i go back to this one here
grab client id in a secret that i have
already
from the previous call go to my client
credentials flow here
there you go
and this is my
request to the token endpoint
and here i have a access token
let's go to
jwt
dot io
paste it in here
and here i see a
row api read write total
so now i can use this access token to
call business central
well this kind of fail i can tell you
already
because i will now get authentication
invalid credentials rejected
and that is because
in business central i need to
register this user
this application user
otherwise he does not know him
and i'm using a demo account so that's
perfect
this is my client id i'm gonna quickly
do that i've only a few minutes left and
i need to open up for q a so
i will speed up now
a id
create a new one
this is my client id
and
enable it
okay
what is your problem two errors
i need to
our description is mandatory probably is
sorry
this is demo bc take days
whatever
yes
a new user has now been created in the
user table
only need to give him some access
let's be easy here super uh-huh
oh that does not work super cannot be
applied
well i know a small
book around for this but
[Music]
for now i'm going to
add another one
like
[Music]
full
give him full access
this you do it
go back to
this one here
make the request again oh that was the
token
center request and there we go
now i have the data back from
business central
so
all of that works
final slides then
[Music]
yeah
so what i just did was creating the
application account in business central
that is linked to the application
account
from the app registration
then
the secret i promise you to come back to
that one
secret is a password proof to identity
has a lifetime of maximum 24 months
so it could be
narrowed down to maybe one month or six
months or whatever so it's a little bit
more secret if it leaks
you should never store it in coat
anywhere
and it's recommended for especially dogs
and only development or test scenarios
the better way to use is certificates
because with certificates
it never leaves the application you sign
a request with a private key and it
never travels over the internet
so
certificates is actually the way to go
luckily
the
libraries and net for example fully
support this
and
we can also use it from al code the
other way around to the outside world
i'm writing some code actually
right now to enable all of that
static permissions versus dynamic i've
already explained that
very quickly if you want to use oauth
and c sharp i recommend you to get a new
get package microsoft.identity.client
and you don't have to work with all
those details
because
you just create
a client application either public or
confidential
in the code with the client id with the
secret
and you grab it with the acquire token
interactive or acquire token for client
call
and that will make everything work
i have an example of that but i have
three minutes left and i need to open up
for q a
so that demo
may be another time
i hope at the end of this we have seen
at least
the steps in between to draw on all
these the pieces that put that one
together i hope so
are there any questions
and i have something to throw to the
person who has a question so
a little bit too far that's a heavy one
so i have a question about the
multi-tenant multi-tenant yes if you
have an app which is accessing more than
one business central environment for
more customers would you rather say it's
best best practice to have one app
registration or have more registration
for every customer because if the guide
secret is leaked
you would have access to all customers
yeah very good question so
i would prefer to have multiple app
registrations
in the customer
as your active directory
the only moment that i would not do that
is when i own the code on my own
platform and nobody else has access to
it
but as soon as there's a distributed
application running on different
uh application different sites so on
premise then definitely
have multiple app registrations yes
okay thank you yep
you have a question
you need another one
well this one works
okay some exercise here okay uh
for me it's a little uh
review you can say because i don't uh
quite understood
the difference between the dynamic and
the static permissions yeah so
dynamic permissions are not registered
in the app registration so you do not
select them in the azure portal
but you
request them together with that
authorized endpoint so when you
send the user to the authorized endpoint
you add a scope
in that request
and it is then a scope that is not part
of the app registration
and at that moment if the user say yes
it is dynamically added to the
service principle
so it's not in the app registration and
only on the service principle
yeah
that partly uh i understood but um where
does the
the scope for this come because um the
dynamic ones are not always the same
requests for the customer i think
so
yeah you so they're not always the same
because
one time you need scope a and the second
time you need code b so the moment you
ask the um the user to authorize
you tell them which scope you need at
that moment
okay so so it's a molecule and then the
user decided what scope we want to
enter to narrow down the access token
that you get
because if you get an access token for
all the permissions that you have been
granted that access token would give you
too much access for the purpose that you
may need at that moment
okay yeah i think i'm now a little bit
better okay good
i see somebody there
thank you
um
so let's say we have uh multiple
applications uh that uh require
basically the same the same permissions
to access um
the the objects in business central is
it better to create uh
to register each app individually or can
we just reuse one average registration
so let's say we have five azure
functions that are all basically
required the same the same permissions
um you can you can reuse it in that case
okay yeah i would say so yeah
thank you
any
further questions
come on
please pause it on
so did you say you had a working example
with
certificates instead of client secrets
that you're willing to share in the
future of course i'm going to do that
so that example that i created
is this
in al code
i i know there is a wizard for example
the microsoft has a small wizard which
says okay please enter here your app id
your client id and your secret yes yeah
and then there's a link to docs to say
okay you need to create an app
registration you need to add these in
these permissions you need to
do this and this and this and and then
you get an app id and a secret you enter
it here
i have two problems with that approach
first of all it requires the end user to
do that
and it works with a secret
so what i have created in the first
place is an application an al app that
does not ask to use a foreign client id
it creates
the client epic at the app registration
in the graph api so the only thing he
asks to the user is please give me
access to your azure active directory
i do it for you i create the app
registration i can create a secret or
i can create a certificate
as a self-signed certificate all in al
code
and i'm going to use dead certificate to
make the calls
and all of that in al code
without any external module
it's all there you just have to put the
pieces together
so i've done that and it works
i just need to
write a blog post and finish it and blah
blah blah
so gonna take a couple of weeks but it
will be there
hallelujah
okay
be careful with that thingy
i just want to ask
token expiry is 24 hours normally right
yes token expires in about 60 minutes
could be a little bit less a little bit
more you never know exactly but it's
about 60 minutes
60 or 24 hours
12 24 hours or 16. no no no 60 minutes
or sometimes it's 70 minutes or 75 but
sometime in between okay let's say 60
minutes yeah so
between the applications we have like
multiple uh calls yeah right so
every time when we request one
let's say every time we have one call we
have to request one token basically so
there's a limit for the tokens which is
actually costly you know if you have the
multiple
thing and do you recommend that token
buffering for 60 minutes so
um
azure does not care if you request
multiple
exa multiple access tokens in a short
time
they would rather have you make multiple
calls instead of storing the token
somewhere that it can leak
but the token is valid for 60 minutes so
that means that you can keep the token
in memory for 60 minutes and after 60
minutes say okay sorry now token doesn't
work anymore so i need to have a new one
that getting the new token can be in two
ways
number one you just pop up a new window
saying please log in
and do the whole exercise again
the user will probably even not even
notice it
and if you're doing it in the right way
it can even be without any pop-up
microsoft decided to go with the pop-up
anyway
in business central you can also use the
refresh token
and a refresh token
is something you can
retrieve with the access token together
and use that in the background to get a
new access token
and that will give give you access as
long as you want because that refresh
token
can even give you access tomorrow or
next week
the refresh token i didn't touch it yet
because i need to make some decisions
for before of the time but the refresh
token is valid for 90 days
and if you use the refresh token to get
a new access token you also get another
refresh token valid for another 90 days
so as long as you stay in those 90 days
you will be fine
except
for those azure tenants
where they have configured that a user
needs to be interactively locked in
every
two weeks for example
in that case
because that is a configuration that can
be done and some
people do that
then the refresh token is not going to
work because the refresh token is trying
to log in a user without interactive
login
and then as you say sorry this user has
not not logged in for two weeks so i'm
not going to do it for you
well good luck with
working with an access and a refresh
token in the background in a background
process that you retrieve from a user
and that user is going on vacation for
three weeks
after two weeks the background process
is not going to work anymore
i've seen those situations
so it's a lot more than just a refresh
token
you need really to know how azure is
configured
i mean uh
my difficulties i mean i'm facing this
in a practical uh life
day-to-day life
because
i'm not really sure that whether we
should save it in a table field or
something for up as a buffer i mean we
don't use the refreshing refresh token
we just use the 60 minutes tokens yeah
so
just want to see if there's any i mean
if there's any other way that we can
secure it place because it's not secured
like if you save it in a setup table
buffer or something like that definitely
other ways as well definitely yeah
okay
so i see people leaving thank you for
being here and watching this i hope it
was useful
and
[Applause]
ah there are some t-shirts
that
you asked just shall i throw them
okay i don't know
oh there's another one
sorry for you guys in the back
[Music]
my
