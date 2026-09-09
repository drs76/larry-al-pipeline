# Microsoft Presents: Authorization techniques you might have never heard about

- **Source:** https://www.youtube.com/watch?v=9c-4p0zlLCk
- **Video ID:** 9c-4p0zlLCk
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 48m12s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome thank you so much for taking the
time to come and picking our session
from all the wonderful sessions that you
could choose from and we're pretty sure
that you've you've learned a lot and
enjoyed from Roman session and we've
we're going to continue some of the
concepts and uh dive really deeper now
into some not so conventional
authorization techniques that you might
not have heard about so I'm REO and this
is Christian and we are both part of the
platform team at business Central
and we handle a whole bunch of areas but
we're also kind of the authorization
experts so let's let's dig into
this yeah so before we start let's let's
take a recap right like let's figure out
how does a user normally sign into
business Central and what this usually
encompasses is you have you know some
business Central user they get
authenticated in entry ID which means
you know you verify who you are like
this is my username this is my password
my tofa that's great and then we have
two layers of authorization that's
standard in our business Central um Au
flow right and the first one is you are
authorized two features in business
Central and that can mostly be done with
a subscription or a license so you have
the business Central premium
subscription we know this the second
layer of authorization is through
permission sets where you you know
restrict it to the specific
um operation within business Central
right from all the things that you are
entitled to and then you get access to
the client so just to summarize what I
just said imagine you are you you have a
HR
employee and you authorize them with the
premium subscription to you know both
View and edit HR data but then if you
want them to only view the HR data and
not change salaries for example then you
would want to restrict them to only the
HR viewer permission set
so we know this right and this is this
is the normal flow and everyone knows
this but this is not exactly what we're
going to talk about you also could be
authorized in a different way where you
have like the administrator role and you
know Roman explained some of those in
the previous session and uh this is also
pretty common for a lot of partner
scenarios right and if you notice the
pictures are exactly similar and it
changes in this one part there's a few
other
ways so now let's talk about some of the
non-conventional ways that you can
actually be authorized in business
Central and the first concept we are
going to dig into is called security
groups and let's understand what these
are so security groups is not a business
Central concept per se it's something
that has been sitting in Azure and entry
ID for a while it allows you to manage a
group of
users and a lot of your customers are
most likely already using this to manage
access to you know SharePoint to Outlook
Azure other Azure apps so they already
know about this right and obviously
business Central would also like to
leverage this and uh if you attended W
those OG session then some of you guys
also know that this is pretty similar in
concept to user groups or you know the
security groups for Windows groups that
we have on Prem and obviously you can
leverage these in SAS and we're going to
show you three scenarios which will make
this pretty effective for you to design
and uh support your your really like you
know big customers so the first one is
managing access to
environments and uh what business
Central allows you to do is you can now
specify a security group on the business
Central admin Center page that you are
familiar with and if you hadn't then
Roman also showed it earlier and only
the direct and indirect members of this
group can then access the environment
once you link it uh of course these
restrictions don't apply to admins they
you can freely sign in regardless of
when you set this Security Group and you
link it but we'll talk a little more
about the
SL so how exactly does this work and uh
this is the admin Center and we've
opened this to the environments page if
you haven't defined a security group for
environment access yet this is how you
do it you can click here and then you
can select from your available entra ID
groups so you need to go back to Azure
and either create one if you haven't
already or you could use one that
already exists once you've selected it
you can also then come here and modify
it if you need to do that for some
reason and let's say like another
colleague has you know somehow deleted
or renamed or something like that the
security group then if you come and you
know users complain that you can't sign
in you can always come here and check
and it'll give you a little warning
saying hey you've linked a group but we
can't really find it anymore and you can
you know set the correct one or
something like that so that was
environment access the second way you
can use security groups is to assign
permission
sets and the way this works is you can
you can link the security group that you
have in Azure in business Central and
then assign your permission sets to that
security group and all the members of
this group in
Azure who are licensed to business
Central will also get these permission
sets automatically so just for example I
have the users page over here and you
can see there's a user I've not yet
assigned any permission SI of the
security group so this is empty but then
if I go to the security groups page I
can say new it'll then allow me to
select my security groups from entro ID
I select the one that I have set up for
example uh like let's say HR viewers or
something and then I can go in and
assign a permission set to that security
group so I can filter and pick exactly
the ones I want and now when I go to the
users page right and I can see that hey
there's this I already have the security
group set up in Azure so there's a user
in there and it will also indicate to
you that you know this person is getting
a permission set this is the per the
security group that they actually got
this permission set from so it becomes
very easy for you to validate that you
know what you set up actually works like
out of the
box and then finally and this is not a
business Central feature per se again
but you are able to assign licenses in
bulk in enter ID and this is great
especially if you've got large customers
and you need to assign you know 50 or
100 or hundreds of licenses and you
don't want to you know assign them to
each one so you set up a security group
and you can assign the licenses to the
entire
group
um exactly and then all the direct
members of the group will get this
license and since we are in the real of
license in some aspects like location is
very important so make sure that you
have a usage location for these users
set and I'll just show you how this
works this is a snapshot from entra ID
that I've created um a security group
called BC licensed users and this is the
one that I want to assign my license to
and then I can go ahead and um add some
members to these groups so in this case
I have this one guy Jason I've added him
to the group and then I can add assign
the license to this group now let's say
you've set this up and maybe the usage
location or something was incorrect so
you want to verify that you know
whatever you've setup actually works how
do you do that you can go to the
licensed user section also an entry ID
and verify all the members right like
who all have licenses and azra does this
pretty cool thing that'll show you that
hey you have a license and the access
path is actually indirect and will tell
you which Security Group it gets the
license from
so how does this look in business
Central well it's completely abstracted
away so the user that we see now in the
user page in business Central it shows
you just in the way that you're familiar
with that they have the business Central
for information worker license so
there's nothing special in business
Central it's just a user who has been
assigned a license but the cool thing is
that this license comes from a security
group and now you may be asking okay
what do I do with all this information
right so let's let's try and think of a
hypothetical situation where you're now
going to try and support a customer that
is a really big clothing retailer and
they've got operations in Sweden and
Denmark and logically let's say their
company is structured like this where
they have some Danish Erp uh you know
employees and they have some Swedish
ones and they have like a sales function
and an HR function in each of them so
there's many ways us partners could set
this up but let's talk about one of the
ways that you could
try so again we have the close company
they have the Danish employees the sales
HR and also the Swedish now let's see
how we would set this up one way we
could set this up in Android ID so first
things that we talked about is you want
to manage the access to the environment
and you also want to assign BC licenses
so let's start with our first Security
Group let's call it Erp employees for DK
and you'll assign it U of you know 100
business Central premium licenses for
example you can do the same for the
Swedish one and now you've got the
security groups for environment access
and for licensing setup the next thing
that you want to do is you want to
control the second layer of
authorization which is a permission set
so let's set up those security groups so
I can create one for the Danish sales
employees and likewise for all of the
others and in this way you can set up
for example entro ID and the security
groups there now how would this work in
the business Central environment so
let's take the Danish production
environment right you can link the
security group for Access cuz maybe the
customer tells you like hey I don't
really want my Danish sales people
messing around with Swedish sales items
right so I want to keep those separate
so you'll link the DK Erp employees in
admin Center so only they can access the
production environment in business
Central now the next thing that you want
to do is you want to assign the sales
permission sets to the sales employees
and the HR permission sets to the HR
employees and you can do that as well
right so your Danish environment is
fully set up and very simply you can do
this for the Swedish one as well so far
so good but you may say Hey you know
this is like quite a bit of work right
like I need to do this but what is the
true benefit of this now when you are
dealing with a customer this big
obviously there's going to be lots of
changes let's say for very simple
there's a new sales employee joining the
Danish organization now imagine if you
didn't set this up like this you would
need to assign them license you'd need
to make sure somehow that they don't get
access to the Swedish environments you
need to assign them the sales permission
sets but it's super easy if you set it
up like this all you had to do is add
them to two security groups one is the
DK Erp one where they directly inherit
the license that they need for business
Central they would also get only into
the environment production for Denmark
so that's done straight away and the
moment you add them to the sales uh
Security Group they will inherit the
permissions set automatically and that's
the only setup you have to do and you
can imagine this this also scales with
other operations that you do for example
somebody moves to a different uh
function etc etc so you only have to
manipulate the security groups and this
way you can also uh leverage the
customer admins to do this themselves
right so it's pretty pretty
powerful this was one of the concepts
that we wanted to talk about and I'm
going to hand it over to Christian to
tell you about the next
one y thank you Raina service to service
or S2s as we call it is a way to authen
to web services which is really designed
for system integration so you have one
system that needs to call another for
example if you have a web shop and needs
to call business Central apis then S2s
is designed for that scenario and the
thing that sets S2s apart from normal
authentication is that it works without
user intervention like how do users
normally log in they get some UI popped
up and you need to enter your email
address and your password and maybe you
have two Factor authentication enabled
that works fine you also know that the
next day you come in maybe you don't
even have to enter your password again
because it remembered you but then the
third day you come in and now all of a
sudden it wants you to reauthenticate
that's the nature of of that kind of
authentication so if you use this
technique in your webshop system let's
say to authenticate to business Central
via the web shop what it's going to do
is going to work just fine until one day
it needs also to reauthenticate and then
there's no user around right so this is
why S2s is really the way to go for
service to service since system to
system service to service application to
application there's no user involved
here at all this is actually not a new
uh feature in business Central that we
support this this was added in version
17 and then further expand it on in the
following release let me show you how SU
set it up Roman touched a little bit
upon it I'll just do a small repeat so
the way you set it up in inra first is
you go in there and you find app
registration click new you get this page
you give it a name and you leave the
default values as they are because
that's typically what you need and you
click register now you have an
application an inra application and then
you need to do two more things to make
it work for our
scenario the first one is you need to
assign a client Secret Roman also
mentioned this that can be a certificate
it can be a secret and it can be some
other things in this scenario I've used
secrets so I go and say new client
secret and I give it a name and I give
it an expiration and when I press okay I
get that string that Roman also showed
which is kind of the password for my
application for my int application that
was step number one step number two you
need to Grant it permission to call to
authenticate to business Central apis so
under API permissions you say add
permission select business Central I
have you cannot see that here but you
can see in the upper right corner that
I'm in the context of business Central
apis at this point and there are two
types of apis there's delegated and
application and delegated is for the
user flow so here you are granting
permissions to the application such that
when a user loged in the application
the user delegates to the application so
the application can authenticate to
business Central on behalf of the user
that's not what we want here we want
application permissions because we are
doing S2s so I've selected application
permissions here and you can see there
are a number of different permissions
you can say api. readwrite all that
gives you access to all the apis in
business Central you can also say
automation that Rite all that gives you
access to a set of apis namely those
that you use to set up an environment
for first time use like install
extensions import configuration packages
and other setup tasks and right above
you also see admin Center the read
write. all which is the one that Roman
used
before finally don't forget to Grant
admin content right so give it a
name add a client
secret Click put a check mark in this a
information that's all it takes now
we're done on the entra side on the
business enter side we also need to
register it because we need to give it
permissions inside of business Central
so here you go to the Microsoft entro
applications list page click new you see
this page so you take the client
ID from intra you uh give it a
description and enable it and then you
can assign permission sets to it as any
other user because ultimately uh it is
kind of a user in business
Central and that's it that's all it
takes few minutes I would say to do this
now it's ready to be used I also have a
small example this is in C with four
lines of code and you can see all the
placeholders here you have the client ID
of the application the secret and then
the tenant domain or tenant
ID then that's all you need and if you
you do this you can request an exess
token and this point this the thing
right it will not open any dialogues
here guaranteed right it's going to run
in the background and can reauthenticate
as many times as it wants so here you
get an access token and if you ever seen
an access token you know it's a very
very long string that kind of encodes
who you are so when you send this to
business Central
apis it will know who you are and will
let you in or
not so the way you send it it's usual
way put it as a header of your HTP
requests so if you if you if you
actually go ahead and call business
Central
apis uh no
sorry let me explain entitlement so
Raina explained in a very first slide
how some of these entitlements usually
work like for a user how do they they
get entitlements how do they get the
right to use business Central the normal
way is you buy a license and assign it
to a user
that can be a premium license when we
see that you have a premium license we
give you a set of entitlements that give
you right to use parts of business
Central if we see you have an essential
license we give you the right to use
give you some entitlements that give you
a right to use a little bit less of
business Central that's the normal way
or you have you maybe your user is an
administrator of some kind when we see
you an administrator we give you a
different set of entitlements so you can
do different set of things inside a
business Central for applications the
way you give entitlements to an
application is by putting these crosses
in those check boxes in
intra automation rri all or API Rite all
so don't you don't need to buy a license
for your application or you don't need
to make it in administrator all you need
to do is is put the check boxes uh in
inro
that was uh S2s another concept guest
users or invited users as we also
sometimes call them so guest users are
relevant when you have two organizations
working together for example you have a
customer and you have um an accountant
organization and they need to work
together because you want the accountant
to look after your business Central
environment this is an example where you
want your accountants maybe to have
access to your business
Central and the way you can make this
work is in the following
way inside the customer's intra you can
see all the users that the intra that
the customer has you can also invite
external users so if I click this invite
external users invite external user I
will get a page like this where I can
put in the email address of my
accountant user let's say I can also ask
inra to send the invite for me by
putting the checkbox there and have a
little greeting and when it sends the
email the accountant will receive that
and they will see You' have been invited
into the customers uh tenant
organization and if they accept they
will be shown this dialogue where they
are where inra is kind of telling their
accountant by accepting this the
customer organization will be able to
see things about you profile and they
will also be able to see when you log in
and what you do in the context of the
customer
organization so if the accountant
accepts this they now become users in
the customer organization so now they
appear here but with a special type
guest and you can also see how they got
there they got there via an
invitation also if you look at the user
principle name it looks a little bit
weird
user principal name is an ID of a user
it's not necessarily an email address
even though it typically is the same
value but it doesn't have to be the same
value this is an an an identification of
the user so the invited user the guest
user here has a weird user principle
name it has the same domain in this case
CDX something um and in front of the add
sign you can see not just the normal
Alias but the is plus the organization
that that user natively lives in so in
this
case I can see that in my organization I
have the three users plus one guest user
and the guest user is actually Raina who
lives natively in the
microsoft.com organization so whenever
you see something like this you know
immediately this is a guest user and you
can see who it really really is so when
they log in when Raina if Raina were to
log in here he would not use this at all
this uh user name he would log in using
his
microsoft.com username email address and
password and all of that but this is how
it looks in the in the the other
organization so if Raina were to log
in uh sorry before that um you can now
assign licenses to this user just like
any other user so here we can see you
maybe remember Raina showed this where
there were only three users now there's
a fourth user and we can also assign
the business Central for information
workers license to that user so with
this Raina will be able to log in to the
customer's business
Central and if he does that we can see
it inside of business Central so he will
become a user in business Central and
you can see once again here we call it
authentication
email little misnomer perhaps but this
is really the user principal name again
once again so you can see this is a
guest user right there but everything
else works the same way as for regular
users that was guest users then we have
granular delegated admin
privileges or
gab what ddab does is allow me as a
customer to delegate some permission
some admin privileges to you so that you
can manage my environments which
probably you have done used already
perhaps some of you very very
convenient there used to be be another
system called dep delegated admin
privileges that is dead don't use it
it's going away DDF is much better and U
this is the only thing that will
continue to exist and the way the thing
that makes D better is it's much more
granular that's why it has that g in it
and how is it more
granular in a number of ways
it is a you can limited period like I as
a customer can give you access for let's
say 90 days only with da I would give
you access and if I didn't remember it
to remove you you will have access
forever so it's Li it's granular in the
duration it's also granular in the roles
so I can give you the roles that I think
you need like for example this new role
that Roman mentioned also that gives you
access to manage my business Central
environments I could also give you
access to This Cloud app administrator
that was that was asked about for the
previous in the previous session that
would allow them to
authenticate um or to authorize
the uh application in
intro that was the second one the third
one is it's actually kind of for you as
a partner also for the customer when I
when I set when when we set up a
relationship I'm the customer you're the
partner I trust you as an
organization I don't know your employees
I don't in principle don't care how you
do your work it's up to you but on your
side you maybe have an interest in not
over granting permissions to all your
employees so with gab you are able to
say for my for this customer for me only
two of your employees should be able to
manage that you weren't able to do to do
that before so now you're able to sort
of limit these employees manage these
customers those employees manage some
other
customers let me show you how it works
so even though it's it's me as a
customer who need to approve this in the
end which makes sense the process starts
with you you request an admin uh
relationship with me as an organization
so you say you gave it a name you go
into partner Center and you say find my
find find me as a customer and say I
would like like to create and admin
relationship request and you give it a
name give it a duration you say what
roles you need to to to have to do what
you want to do and uh you can also make
it auto extend and then you say uh
save what I will get is an email with
these
details um you can see that it has the
duration and other things but the key
thing here is the link so you see the
link here takes me to my M365 admin set
C so if I go to that link I will see all
the details about this admin
relationship
request I will see that you want these
roles for this for this long and so on
if I say that makes sense you need those
I will accept
it and then the admin relationship is
active so now it's there it's like a
contract between our two
organizations you can see it's active
you can see it will expire after a
certain amount of time it will not Auto
extend we're not done yet because on
your side as I mentioned you need to
select who can use this right which of
your employees should be able to use
this and to do this you open this admin
relationship and you select at the
bottom what security groups what groups
of users employees on your side should
have access to manage my environment so
once you've done that added some users
to that then your employees can access
my business Central
environment and if you if they log in to
my business Central environment I can
see that too just like I could for the
S2s applications and for the guest user
because they become users in business
Central as
well but they look like this so they are
totally anonymized I guess this is for
privacy Reasons I'm not sure I guess so
I don't need to know which of your
employees actually log in I can just see
that that that that they logged in what
I can also see is that they got the the
license for for delegated
admins so gdf gives you a lot more
granularity than we had in the past but
there's one dimension of granularity
that it doesn't give us which is one
thing that we have uh received requests
from customers to support and that is
illustrated by this
example so let's say continuing Roma
raina's example we have two environments
one in Sweden one in Denmark and let's
say for the Swedish environment I have a
Swedish
partner that should manage it and for
the Danish environment I have a Danish
partner how do I give them access to the
right environments I can't do that with
gab because for gab I give I would give
the Danish partner and the Swedish
partner both the business Central
administrator role which would enable
them to log into business Central and
see all the
environments so what we really need here
is a way to say this environment is for
this partner and for this environment
this is managed by that partner and this
is actually one thing that we are
working on so this will come and now it
is even more granular than it was with
GF and then I'll hand it over to Raina
again who will talk about device
users thank you
chrisan cool um let's talk about device
users has are you how many of you are
aware of this concept of device
users okay that's Prett cool like a few
quite a few of you so let's explain a
little bit for those who don't know what
exactly is this so device users allows
basically simultaneous or concurrent
access to business Central and uh the
main scenario you could think about is
you have some customer that has a
warehouse with scanners or you know POS
systems Point of Sales Systems things
like that right and just to illustrate
the example let's say you have a
customer that has a warehouse with 100
scanners but they know that at any given
point there's only going to be at most
33 scanners in use because the employees
who use them are shift workers right so
let's imagine over an entire day that
only onethird of the the use the
employees are going to come in and use
those scanners so now it doesn't make
sense to buy 100 licenses right you you
want to keep the cost low for your
customers you also want to make sure
that they actually get uh the most out
of the setup so you don't want 100 so
you buy 33 device licenses and the whole
the whole point of this was to allow
these to sign in
simultaneously and um give you
concurrent access so you don't need to
you know assign a license each time to
each user um every time the shift
changes you just have buy 33 of them and
whenever 33 sign in they get access so
this has actually been around for quite
a while we released this back in version
15 but very recently we also added
support for running schedule tasks as
device
users and uh how exactly do you set this
up again this goes back to the setup in
entry ID and it's also security groups
but this time it's a very special
Security Group because it's a very
special name so you have to create a
group with a specific name and all the
users in this group will be considered
device users you do not have to assign
the licenses to these users because as
you went back to the example the whole
point was like only 33 out of 100 sign
in at any given point so we want to make
that easy right and now let's look at
how the concurrent access would work so
for example okay if you haven't seen the
license this is how it
looks and let's assume you bought three
of those device licenses right and now
your
first shift worker comes in they sign in
all good you've got you know two spots
left the second one comes in also fine
third one comes in no problem now the
fourth person comes in and they have to
wait until the first uh shift worker is
done because they only have we only
allow three uh concurrent uh users to
sign in with these licenses and when the
first shift worker shift is over they go
away and now the slot frees up and this
person can now sign in
again so the main takeaways of why we
had added this or why we added this
capability it was you want to use a pool
of device licenses you you don't want to
continuously assign and remove licenses
from users and we see about 8% of our
paid customers already leveraging this
and we just wanted to put a reminder out
that this exists and this is there so if
you have scenarios which you could
unblock with this then please leverage
it um and finally remember it's a very
specific group the name so and you do
not have to assign the licenses to these
users so we've uh if you run into issues
with concurrent access and uh just a
reminder again Roman showed you the
admin Center and in that you can also
see active sessions so if for example
you know you get a call from one of our
customer saying that hey I can't sign in
you can always go and close any session
that's still open even though the shift
worker has gone
away so we showed you quite a few
techniques on like that's not really
super conventional on how you could
authorize but what if you have issues
because a lot of these are pretty
complicated right there setups in entra
there setups in BC and uh how do you how
do you troubleshoot this stuff so
hopefully our error messages are helpful
to you know pinpoint exactly what's
wrong and uh in most cases we try our
best sometimes you know let us know
we'll improve things but a lot of this
setup can really be hard and outside of
domains that we can spot right for
example like I mentioned the usage
location when you're assigning licenses
like it's very hard to know when when
that doesn't work for example so then
you have option two If the message is
not clear enough over here remember that
you also have a session ID and we've
talked a lot about app insights we love
it it is super cool and you can go and
put in exactly that session ID and
figure out what was wrong what went
wrong you know I was missing some
permission or I was missing a group or
some other role was not there etc etc
you can figure that out exactly if you
can't then again the information on this
error message is super super useful to
us at Microsoft when we want to debug
issues that you have it makes it very
easy for us to spot and follow up what
went wrong so please send us that
information when you reach out to us
and uh yes let's let's do a little
summary of what we've done today and
what we've talked about so we said in
the beginning how users usually get
authorized in business Central right we
talked about the two layers of
authorization where first you're
entitled to different features in
business Central and the second where
you restrict access through permission
sets and now we've seen a lot of
additional um techniques that are purely
based out of entra which make this very
very Cloud native and
it's it's a stepping stone to really
unblocking a lot of you know scale and
you know managing bigger customers and
larger customers with different
different locations
Etc we've seen how you configure and use
some of these
techniques and we also talked about how
you could troubleshoot them so chrishan
and I did something interesting we just
looked at a day's worth of art Telemetry
to see you know what kind of login
errors are people seeing and we we you
know took a entire snapshot and we will
actually uh we I we hope that we pick
the right themes for this topic today
and hopefully you know a lot more about
uh you know roles and security groups
and you can go and look at app insights
and figure out what went wrong and fix
these issues for customers and
uh yes and we hope you continue to
leverage these techniques and manage
your users at
scale that's all we have for now but let
us know if have
[Applause]
questions the other one
got um my question is related with the
service to service
authentication say again service to
service yeah and uh that uh in relation
with the operational limits for API
calls uh to the environment because uh
now the operational limits will be per
user and one of the Microsoft
recommendations
is because all op calls are from one
user because this is the service to
service authentication to create more
than one and to rotate them that means
that I have to register more than one
Microsoft entra applications and as and
because they are not limited by the
license is there some limitation how
many I can create no uh good question so
yeah so the question is about S2s and
the limits that we have on them as you
mentioned we have now switched over to
use per user limits as to how many web
service calls you can make in a certain
amount of time and how many we will Pro
process simultaneously so for human
users entro application users any other
user there's a limit per user so if you
have two applications they will have
twice the throughput capability if you
have five you can have five the
throughput if you have 100 because we
don't have a limit you can make as many
as you like and have as much really
throughput as you
like basally there's there's no limit no
you're right and if you s if you want to
learn more about that we actually both
of us have a session tomorrow on uh
scale in business Central where we're
going to talk about that so I think
you'll find that interesting and now the
guy behind you that you stole it from me
than you when the is isolation per
partner is coming is it a half year one
year uh um probably Roman what do you
say in a half year
maybe end of the year end of the year
okay thank
you yeah just
take hi um I'm I'm just wondering uh
regarding the device users from let's
say from the scanners um the customers
sometimes would like to know who's using
the scanner at that moment let let's say
they are booking shipment or put away or
pck list or what
whatever they need to know who is that
person at that moment Y is there a way
to trace yeah instead of using the
device log in so if they are if they if
they are licensed via the device user
mechanism that Raina explain at the end
of the day they will be logging in as
themselves we will have application
insights Telemetry that shows there was
a user who logged in and you can also
have the user ID the Telemetry user ID
if you're familiar with that that will
be part of the uh application insights
event so you can see when whenever and
whoever logged in at any time okay but
you can't see the user himself on
Business Center way to see it on
business centrer but just to add another
layer to what Christian said like if you
remember the original picture right
there's there's two layers of
authorization so the device license is
just the first layer that's what like
gives them the entitlement to get in but
it's there it's the actual user that
ends up as an entry in the users page in
business Central
so then when you look at app insights
and you look at your logs you will still
see the same user Telemetry ID in there
so you can always get them it can be
traced under the Teter okay yeah thank
you cool was some over here
yeah thank you so question about device
users um I know in business Central you
need to have for for for device us you
need to enter the device in the device
users
uh list and they need to Security Group
yeah no no in in business Central itself
there's there's a page called device
users ah so this is this is uh this is
the one step further yeah this is on
Prem so in in Prem yeah yeah in the
cloud you don't you don't need to do
that it's purely through this license
and the security group the question is
gone yes
yeah but maybe we could we could take
we'll take some notes and maybe improve
our documentation or something because
that's that's good feedback as well for
thank you thank you um when will uh
security groups become available for on
premise environments H you already have
them you should already be able to use
them okay last information I had that it
does not work for on premise because we
cannot connect to enter okay uh drop me
a mail I'll follow that up okay great
and the second one um please don't mix
uh um gdap uh privileged accounts with
guest users if you do that it uh breaks
the system exactly um but go away from
dap completely that would be yeah so the
DAP and the DAP another problem with the
old model is that if you were both a
guest user and a delegate admin we
didn't recognize you as a as a guest
user I think gdap doesn't have that
problem either yeah we we didn't add it
because it we thought it might be
confusing but you could technically
invite a gap user into the you know
environment assign them a license and it
would all be exactly the same but thanks
for bringing that up any more questions
Y is it planned to actually uh allow
Partners to install custom extensions uh
using service to service authorization
because now it prevents to use the P
plans and releases effectively and uh
requires user um interaction I believe
you can do it today the automation API
should no we we use devops and on
primary Solutions you just run the on
pull request and it installs the
extensions but in Cloud Solutions it's
it's kind of not possible because it
requires the user to go in to device
login website uh put the the little code
which you get from the business Central
then you get authorization token and
only then it installs the
extension let's also follow up on that
offline to my knowledge you can actually
install extensions by so as service yeah
so as Christian showed the two API
access um Scopes right there was the API
Miss Central all and there was also
automation both of these actually should
allow you to do that but uh drop us a
mail and let's let's follow up all right
all right thank you cool thank you
thanks for that
question yeah just uh touching base on
the anonymity of the delegated admins is
there a way as a member of the partner
org to figure out like what what those
users are what a ENT ID um users those
map too because I mean a lot of times
it's like oh this user did X Y or Z and
it's like oh I'd like to talk to them to
find out why that is an excellent
question I don't know I'm sure there's a
way so the this the string that we see
there I think I so I look a lot at the
access tokens when we build our
authorization Stacks but I I all send me
a mail because what I want to do is just
confirm that this is publicly documented
or not before I just share that hey I
noticed this but yes drop me a mail I'll
get back to you yeah
thanks do you have any more
questions
yes thank
you uh just a question when you've got
uh when using
the the group for license
management uh when you have a user on
the let's say the two groups is it
consuming two
license I don't think so no but then
again like again this is just my
observations I don't think it's publicly
documented but it also needs to be
direct access so I don't I couldn't get
it work with you know nested groups for
example but um yeah there's no clear
document ation on this but maybe it's
it'll come soon so I it should not but
you can always verify because uh when
you go to the license and you check
license users like the screenshot that I
had shown earlier it it just shows you
like one entry for the user so I don't
so the end result is that the user gets
a license um and they I don't think a
user can have to with the same type of
license and also just to illustrate how
it really works is so say you have a a
security group with 100 people in it and
then you buy uh you assign 50 licenses
to that group what do you expect to
happen right that's a that's a loophole
of course if we if it work like you
would think no then only 50 of the users
will get it right so you will actually
be able to see which 50 got it and 50 50
others won't get it right so at the end
of the day the user gets a
license like any other way you you would
give it a
license any last questions you have one
is it possible to use nested groups when
working with security groups so for
environment access yes so the one that
you would Link in the tenant admin
Center you can I believe it should also
work for permission sets the only one
that I'm absolutely not sure of is the
license assignment so that one I don't
know if Nessa groups will work or not so
I I I'll need to clarify I double check
that
pass I've got one small question
regarding security security groups and
user groups currently we still have
customers who have only set up user
groups and for example they have two
companies and their current pattern
often is they sign users User Group per
company and do I understand it correctly
if they want to Transformers two
security groups they would have to
create two security groups where they
assigned the exact same permissions one
for company one one for company two to
be able to
assign uh the permissions correctly in
the future or yeah if if the groups
contain different sets of users you
would need to have two security groups
in entra and then set them up per
company okay
any last
questions if not then thank you all for
coming hope you learn something and have
a great conference thank you so much
