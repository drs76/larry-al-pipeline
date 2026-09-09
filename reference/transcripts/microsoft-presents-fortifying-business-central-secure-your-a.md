# Microsoft Presents: Fortifying Business Central - Secure Your AL Code Against Real-World Threats

- **Source:** https://www.youtube.com/watch?v=EetJcsI4iWw
- **Video ID:** EetJcsI4iWw
- **Channel:** mibuso.com
- **Published:** 2025-10-02
- **Duration:** 43m48s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

And ladies and gentlemen, please welcome
Derek. He's going to talk about
fortifying Business Central. Secure your
AL code against real world threats.
All right, welcome everyone. Let's start
with who I am and why am I talking about
this to you. I've been with Business
Central for about seven years. I'm an AI
and security champ in the AI solutions
teams. Some of you might just know it as
the application teams from old days.
I have
security certifications specifically
more in network and application uh
penetration testing.
And my first question to all of you is
what does security really mean to all of
you? Is it application security,
information security,
operation security or even network
security,
um disaster recovery and business
continuity? If it's any of them, great.
If it's more than that, also great. As
long as you're thinking about security.
Now, we want to focus on cyber security.
So it is the practice of
mitigating and preventing cyber attacks.
And on the agenda for today, I really
only have two things. One is the
security development life cycle and some
coding best practices for you.
And within this development security
development life cycle, I'll talk about
what it is and then I'll talk about
threat modeling and a stride framework.
If you've never heard of them, that's
okay. I'll go into detail.
So, the security development life cycle
is really just a security assurance
approach such that infuses security into
all stages of software and your service
life cycle. It's there to help you make
your uh software less vulnerable and
more resilient to attacks. It's not
there to guarantee that you will not be
attacked. It's there to help you and
help you ensure that you know what you
can do if you were to be attacked.
So there are seven stages to this
security development life cycle. Um you
can find this on our Microsoft learn
page. So it starts with training,
requirements, design, implementation,
verification, release, and response.
There's a lot to cover in all of them,
but I won't bother with any of that.
Because what I really want you to take
away with doing secure development is
threat modeling
especially for your AL code.
So what is threat modeling? Threat
modeling is really a proactive and
systematic approach to help you
identify, analyze, and then mitigate the
potential risks.
You don't want them to become real
threats and then scramble to figure
something out. That is a little too
late.
So there are five steps to this. The
first one is really you want to define
and what do you want to define your
security objectives and the scope. So
what are the security objectives for
threat modeling. So take for example
that you want to ensure your customer
data remains confidential
or it could be preventing unauthorized
access to an admin feature.
Regarding scope, you want to determine
what is in scope for this uh threat
model and what is not in scope when
you're performing the review. So what
can be in scope for example be maybe you
are accessing an external service or
your feature internally is doing
something to another part of the system.
Those are the things that could be in
scope for your review. And what could be
out of scope things that are say an
external service you may own that as
well but that should have its own threat
model and security review.
Now the next step is to diagram. You
want to diagram your system architecture
into using a data flow diagram so that
you know how your processes are moving
data and also what are they really
doing.
Moving on from there you want to then
identify their threats. You can use the
stride framework which I will go through
and use that to help you identify what
could potential threats be against your
system.
Once you've identified those threats,
you can then start to mitigate to figure
out how you're actually going to
mitigate these threats. Not all threats
must be mitigated.
You could say there is this risk and I'm
willing to take this risk, but at least
you know about it already.
And then you validate your mitigations.
Are they good enough? And do they
actually work? And it's a cycle. The
moment you change something, you should
do your threat model, update it, and
then go through the cycle again.
So here's an example of a threat
modeling data flow diagram. I will come
back to this after I go through the
stripe framework. So that we will run
through as an example what this really
is and how you can apply this right u
framework to your own diagrams and doing
this diagram you don't have to use our
tool so I use the Microsoft threat
modeling tool you can do this on a
napkin you can do this on a notebook a
whiteboard it doesn't really matter the
medium it's main thing is that you
actually do it so you can know how your
system is actually working
so the stripe framework is a threat
modeling framework to help you identify
and then categorize potential security
threats. There are six steps to it. The
spoofing, tempering, non-repudiation,
information disclosure, denial of
service, and escalation of privilege.
Now, I'll go through each one of those
and give an example.
Spoofing is when someone impersonates
another user or system to gain
unauthorized access.
So an example of this would be invoking
an unauthenticated
uh Azure function and somehow you're
actually able to spoof who you are
authenticating as or in this case just
the user identification right because
there's no authentication.
So let's take a very simple URI that I
have of an Azure function. In this case,
I know it's a get method, but this can
also be a post method. So it takes in
both a tenant ID and a user ID. And the
user ID here, I have 1502, and that's
the one I'm actually supplying. What if
a user is actually able to control that?
They could now say I'm 82 or 8424
and this other user instead.
So what that can look like in BC. So I
have a very simple function. This just
calls out to my external service. But
the one thing I want you to take a note
is that why am I passing in the tenant
ID and user ID. There is no reason that
I should need to pass it into this
function. From this function itself, I
should be able to just get that from our
AL code. Tenant ID and user ID. You
don't need to pass this. You're opening
up a hole such that someone else can put
in some malicious ID. They could be
getting a tenant ID for someone else.
So something to think about.
Um tempering unauthorized modification
of data or system components.
Take for example an attacker has
tempered with the data right before it's
actually used and then that leads to
potentially incorrect or even malicious
outcomes.
So very simple example here I'm just
posting some document
but
right before I actually do the posting I
have an event on before post sales
document
and within this event I'm not just
passing the information to whoever wants
to subscribe to this but I'm actually
letting them modify this and is there
any reason I should let someone modify
this before the document is posted I've
called this function very specifically
to post it.
Non-repudiation
performing actions that cannot be traced
back to the perpetrator and that
undermines your accountability.
So take for example if you're building
an extension now a user deletes a
critical financial record from that
extension
and they don't they say that no it
wasn't me without some sort of audit
trail say change log monitor sensitive
fields telemetry how are you going to
prove that user A did or did not do that
action
now I want to note that if the more you
use change log and monitor sensitive
fuse I mean there is performance there's
also a say space where it grows
but I do want to mention that one should
always put priority on security because
if you don't have those logs you will
never be able to prove or disprove
something happened because of this user
information disclosure
now this is the unauthorized exposure of
confidential information.
So take for example a page containing
some sort of sensitive information but
then lacks access controls such that all
users can see it. Another simple example
also would be say you had a public
procedure that allows a user to access
sensitive information.
But going to the page example
hopefully you can see it well. Yep. And
so I have inherent entitlements,
inherent permissions. I forgot I left it
there because I was testing and then I
shipped it to my customer.
But you know, maybe not so bad. Maybe
they should have access to this.
Then next I look at it. Okay, I actually
have a username on this page. Not maybe
still not so bad, right? No password
yet. And then I see oh password is there
too. It is just text. There is no
extended data type. It's not masked.
Anyone who goes to this page can now see
the username and password.
And if we go further down, it's like
it's non-debugable. That's at least
good, right?
At least someone using code cannot
access these variables.
But then if they will have access to BC
itself, why would they care about the
code? They can just view it in the page.
Now I've cleaned it up a little bit. I
remove those inherent uh ex entitlements
and permissions and then I've at least
added the extended data type.
So one thing here with information
disclosure is to always practice the
principle of lease privilege. Only give
the necessary amount of permissions to a
user that they need to do their job.
Denial service
disrupting service availability to
legitimate users.
An example would be you're pulling an
external service and eventually it
triggers rate limits
and then some other user is trying to
work with that service in the same
environment perhaps or even from a
different environment entirely separate
tenant and they can't work either.
It could also be potentially from
deadlocks caused by tables. You can do
this to yourself. It's not necessarily
that someone else is actually causing a
denial service to you.
So very kind of simple example. I know
you might be looking at this and saying,
"Wow, true. No one writes this kind of
code." And that's fine. But if you
replace it with a repeat and repeat
until now if you have a large enough uh
fine set that you have done just before
that it's almost no different when
you're locking the table.
And the last one from the stride model
is that the escalation of elevation of
privilege.
Now being able to gain an unauthorized
access to some sort of higher level
permissions.
The example here would be a privilege
procedure. Now you might put say
inherent permissions on this procedure
and then that is mistakenly exposed as a
public action right on a page. And one
once again I mean this could be because
you were testing makes it easy. It's a
page action.
This allows anyone to then escalate the
permissions uh by doing that action
depending on what it does of course.
So just a short recap on the six parts
of the strike framework. Spoofing,
impersonating another user or system to
gain unauthorized access. Tempering,
unauthorized modification of data or
system components.
Non-repudiation,
performing actions that cannot be traced
back.
Information disclosure, unauthorized
exposure of confidential information.
denial of service, disrupting service
availability to legitimate users and
escal elevation of privilege, gaining
unauthorized access to higher level
permissions.
So just before I go back to the threat
model I have shown you, let's just set
the scenario. Let me just describe what
that really shows. So it's an extension
that I've built. It's the Contoso
company. Now it can do X Y and Z and
additionally it can load some sort of
tenant license from this extend um
external service
and then this yeah so the tenant license
service actually come from this external
service.
So sounds simple enough right? I'm
really going to focus on that tenant
license part of it.
Now we need to set we need to define our
security objectives and our scope. So
one of it is we want to ensure
confidentially of the tenant license
information. We don't want someone to
someone else to have access to only
yours.
We want to ensure the integrity of the
license data.
We don't want that the data that is
pulled is suddenly tempered with and
then they're able to say escalate
themsel or even get something that they
should not be getting.
um you want to have some sort of
authentication authorization such that
it's only valid tenants and extensions
being able to load that data and even
store that data.
And lastly, we want to also ensure the
availability of licensing service that
we are not the ones causing a DOS attack
against that service because it may
cause us to break.
Now what's in our scope? what's in scope
for this. So take for example handling
of the licensing data communications
with this external API
authentication mechanisms. How are we
authenticating username password or off
tokens API keys certificates?
How are we storing and also caching the
license information within business
central?
Now what is out of scope? What do we not
care about when we do this review? And
this will change depending on what focus
you want. So in this case we're saying
the external service yes we own it but
we are not going to be doing that review
in this one
business level business central platform
level security that should be handled by
Microsoft
and other unrelated extensions. I may
have 10 other extensions but they're not
related at least they're out of scope
this time around.
So now coming back to the threat model
itself.
So I've kind of placed right at the top
saying all right this is what the
extension can do and the last one being
it can connect to the tenant like 10
service tenant license service to get
the information
and I have just a small description of
that service and also how we are
authenticating to it. In this case,
basic authentication.
I want to just point out these kind of
dash lines, this boundary box, and it
says Azure up there. And what this one
really is is saying that everything
within this boundary box we trust. So
within the Azure boundary box, Azure
trusts all of this.
Business central we have business
central we have the PTE
and then externally we have our my
constosal external service that is
separate on its own.
So now we start I need to put in my
credentials so that eventually the
tenant can load up the tenant
information for this uh environment. So
let's add username, password, credential
to the system. Say maybe it's on a page
and now it goes through our PTE and then
it eventually gets saved into the
database.
Great. Now that's saved. Now I'm
actually using the page. So I go to my
say the Y page. Now this Y page needs to
first validate. Hey, do I have access to
this? Have I loaded in my license? I
have not. So I need to go do that. So
first things we do is actually load in
the credentials that we have and then we
make the call out to the service. We
authenticate with those credentials and
we get that.
Now that's being returned to us and we
save that into our database once again.
I'm sure this is not too unfamiliar to
all of you u building some sort of
service or feature.
Now let's go through stride on this
exact threat model I have. So the first
one I want to go through is spoofing
right. So impersonating another user or
system to gain unauthorized access.
So the first one I would want to look at
is it possible for me to when I'm making
the call out, what if I had no
credentials?
Is it possible for me to actually have
access to that?
Something to think about.
What about tempering?
Is it possible for me to have changed
the information before it's sent to the
licensing service? Take for example,
hey, I want to grab the information for
tenant um tenant B instead of my tenant
tenant A. Is it possible? And then when
the license information comes back, is
it possible for me to actually temple
with that? And this comes to say let me
take the example of business central
licenses, right? We have essentials, we
have premium. Now when I pull this in,
is it possible for me to actually go
modify the information such that I bring
myself up that will kind of be related
to the elevation of privilege but the
thought is there
non-repudiation.
So when someone does an action and you
cannot trace it back to who actually did
it.
So we're storing the information in the
database. Now I can potentially go and
delete that if I had enough permissions.
Do you have any way of tracing back that
that user deleted it or not?
And now this is of course credentials
maybe it's not so bad but if it was the
financial records it becomes more
serious.
Another one the license information
maybe it's similar. I could potentially
delete change. Can you actually figure
that out?
Information disclosure. Unauthorized
exposure of confidential information.
The username and password saving in the
database. Is it on a page? The page
example I had shown you. Is it possible
that a user goes into the system the URL
base URL slash question mark table
equals table ID? Can they do that and
load up the username password and just
view it in plain text
denial service?
Can you disrupt the service availability
to legitimate users?
In this case, could a user in your
tenant cause a DOS attack to the
external service such that other users
cannot use the service from and this is
all coming from the P my PCE here
basically
elevation of privilege
changing the it kind of also goes back
to like spoofing where can I change who
I am um uh for authenticating to this
service. Can I change the license
information from say essentials to
premium?
Now I've updated my threat model.
So let's go through this one. First
thing I've changed, instead of using
username and password, I now at least
use off to authentication.
Could use certificates, could use API
key.
Really doesn't matter. as long as maybe
it's something more secure.
Now I do the same thing. However,
instead of storing in the database, I
store in isolated storage.
That's already one level up.
And I go back and I do the same action.
I open page Y.
I get those uh client ID, client secret.
I do my authentication with the service.
Now it gives me back my access token
that I'll use to communicate with it
and then I communicate with it. I get
back my licensing information and from
there I save it again not into the
database but into the isolated storage.
So threat modeling is a proactive and
systematic approach to identify, analyze
and mitigate potential security threats.
So kind of covered going to the define
the diagramming identifying and coming
off a little bit of the mitigation. We
haven't done any validation but it's
circle that you should think about and
do.
Now let's go over some coding best
practices.
The first one being the secrets keys and
certificates.
And we'll use secret text isolated
storage Azure key vault as the main ones
talk about.
I hope none of you do this that you
don't hardcode anything as literal
string labels or resources.
Why? Because you might do that for your
testing. But if you have some sort of
say source uh a source repository git
for example now there's a history that
is going to be there until you purge it.
Will you remember? Very unlikely. And
why do I say this? Within Microsoft
itself, within business central, we have
had our own red team engagements and we
have found credentials that were valid
for many years.
And that has made us improve our
security to stop that kind of stuff to
improve our static analysis such that
even if we wanted to put in fake
credentials, we're not allowed. it flags
and it prevents us from even checking
in.
So secret text
recommendation is to employ secret text
to handle any sensitive information API
keys, passwords, tokens can be more than
that.
This just at least ensures that the data
remains hidden during debugging
sessions.
So use it if you're moving any
credentials from say the storage
isolated storage perhaps or even key
volt when you're to say when you're
using some sort of API
and this API could be HTTP client and
the JSON object crypto
or off to control addins.
So I have on the left side there is just
the authorization using a secret text
value for the barrow token
with JSONs. It was recently added where
you can actually write out the JSON
object into a secret text and in
basically injecting your secret text
into the JSON object as well
and control addins now also accept
secret text. However, do be mindful if
you do use secret text with control
addins that JavaScript still runs on the
end user's machine
in their browser. They can still debug
that they will see that value. We cannot
stop you but that can happen.
So isolate storage use it to store the
sensitive information.
One thing I want to bring up for is
storage is the data scope. I hope all of
you actually do use and set the data
scope explicitly.
Implicitly the default is module. So
irregardless of what you do only that
module can access that secret.
You can make it more granular but that
is basically the widest it'll be. You
cannot go from extension B and try to ac
access extension A's uh isolate storage
unless extension A has opened up its
isolate storage to you. And what do I
mean by that? Basically, they have a
public function that calls isolate
storage.
Now there are few levels for the data
scope. There's the module the default.
Then there's company. So only if you are
in that specific company can you access
that value.
Or another one is if I've saved this
value only I can actually retrieve this
value not any other user within that
environment
and it's still always within that
extension.
And lastly is if it's within that
extension also that company and that
specific user.
So this is the that's the most fine
grain it can get to.
So always use the appropriate data scope
depending on the data's accessibility.
Be be explicit about what data scope you
use.
Even if it's just module which is the
default set module one look at it and
you know that is the scope
set encrypted use it if you need to um
encrypt the data however there is a
limitation which is 215 characters I
know it's small and I agree I don't know
of plans to uph update that
when you If you use isolated storage,
use it in procedures that are internal
or at least local. This is to prevent
any unauthorized access to the isolated
storage for that extension.
Mark sensitive procedures with
non-debug. So this one is more generic.
This is not specifically just isolated
storage, but anywhere that you have
sensitive information, it's good
practice to set non-debugable.
Secret text helps tremendously,
but non-debugable can help you just in
case you forget and then you just end up
using text because it was easier in the
first place potentially.
Azure key
use it to sec use it to store and access
your secrets within your app source
extensions.
key is not available for extensions so
your PTE but only available for app
source.
So you want to store your app specific
secrets there. I would not recommend
storing secrets for your single
environment or a specific tenant but the
app specific secrets
you can use it to manage your secrets
life cycle more easily than isolated
storage. isolated storage you do need to
go back into that tenant
environment and then update it while
with key vault you can set expiration
dates for your secrets. It's good
practice because then they'll force you
to actually rotate them.
You can do automatic rotation for your
certificates or keys with key fault.
You should, as I mentioned, regularly
review and rotate those secrets that you
have. Setting the expir expiration date
definitely helps.
And how do you access the key vault?
There's the app key vault secret
provider. And using that can get you
access to your key vault that you have
specified in the app JSON and set up uh
all the stuff that you need.
Permissions
Practice the principle of lease
privilege. Give users only what they
need to do their job, not more than
that. I certainly hope you don't give
super to everyone just because it's
easy. You don't have to think about it.
Some other questions is are you giving
inherent entitlements and permissions to
all your objects?
makes it very easy to develop and I
agree but that's also very bad. It's
very easy to forget that you did that.
Are you implementing any entitlement
files?
If you don't, do you know the
consequences of that?
Are you implementing permission sets?
If you're not, please talk to me because
I would like to know how you're working
in production.
So entitlements
so entitlements define the maximum
possible access a user can have
and ina in case I didn't say it
entitlements is basically license right
so
essentials premium they have license
entitlements same same thing
so extensions that do not specify any
entitlement object give full access to
that extension objects implicitly. What
do I mean by that? If you had code unit,
page and a table, the code unit and page
have direct execute permissions in the
entitlements. And for the table, it has
direct read, insert, modify, delete, and
execute permissions.
That is the default. it's maximum when
you do not specify a single entitlement.
But if you do specify a single
entitlement, now if you say only specify
it for
uh essentials
and you don't specify for premium,
premium has nothing.
So do take note of that.
Yes. And there's the entitlement file if
you've never seen one before.
permissions.
Grant users only the minimum they need.
Use security groups to help you manage
your permissions centrally to ensure
consistent access
permission set if not seen one which I
hope all of you have.
what entitlements are like let's say
it's the circle what permissions are and
for any user to access any object they
need what is in the middle
they need the intersection if they only
have the entitlements
they do not have access to that object
they only have permissions they do not
have access to that either
some things about inherent permissions
and entitlements
You can use them for foundational
objects or pro procedures
that must be available to all your users
irregardless. So let's take it for
example the co-pilot capability code
unit. It's a very specific thing that we
did where we said all right this is
something everyone irregardless of who
in the uh in the business central
environment they should have access to
this.
Don't do this just because it's easy to
test and develop
grant. You can grant temporary elevated
permissions to procedures at runtime by
allowing specific actions beyond the
calling users permissions.
But on that part I mean so how it looks
like is with this get default work date
and then it grants uh indirect read to g
entry. I will not get into the reason
why that needs it. But on but on the
next point is that you need you should
apply inherent permissions to the
highest level of the call sting. And
what do I mean by that? The highest
level is where you're actually at right
now. You're only going to use that
permission there. You're not calling
five more levels
of procedures.
So only apply inherent permissions where
you're actually going to use it because
as you call other functions where you've
applied the inherent permissions, those
functions get that permission as well.
It will become a nightmare for you to
figure out where did this permission
actually come from? Why do they have
access to this?
So inherent permissions are very
flexible, but they will scatter your
permission logic all over. Now, that's
going to make it very difficult to do
any audits and for maintainability.
I'm going to end off with this.
It's going to be a non-exhaustive list.
It's just some things I've come up with
for all of you.
So starting with for example when you're
doing your thread modeling with stride
and
developing your extensions if you have
external connections or data handling so
are you calling an external service if
you are then you should start thinking
all right what kind of authentication am
I using is it secure and what kind of
credential storage am I using like am I
putting it in say a resource file am I
typing it and saving it into the
database.
Isolate storage.
What kind of data are you sending? Are
there any sensitive information?
And when you're using um when you're
handling uh sensitive information, are
you using the secret text data type?
There may be reasons why you don't want
to use it, and that's fine. But do
consider
can you should you
access control
are you practicing the principle of
lease privilege
logging. Do you have telemetry to help
you figure out if something has gone
wrong?
It can be telemetry. It can be logs in
the database. Can be any of them.
Yeah, having sufficient detail to trace
back to the initing users action.
And just before I get to questions,
I have a survey that has basically three
questions to those who would like to
give us some feedback. What security
task do you guys usually do?
What security information do you guys
find that is hard to collect from
Business Central?
And what improvements
can we provide in Business Central?
And that's for my presentation. I'll
open up the floor. I have about eight
minutes.
[Applause]
Everyone is an expert.
In the event if you have questions later
on, you can still write in the Hoova app
under my session. I will reply today,
tomorrow, but otherwise you can also
contact me on LinkedIn and then I'll
reply messages there.
Yep.
Uh the there are now several e documents
uh connectors I call it. Yes. uh first
party connectors. Yes. And some of them
use uh cross company or not company
bound uh setup. Is this good security or
it's convenient? It's convenient. How
would you consider this? So I can't give
specific information about that not
because I don't want to but because I
don't have the knowledge about that. I
didn't do the security review on that
one. So
anything cross company you should
inspect it closely. Do you really need
it? Can you do it in another way a more
secure way?
But besides that I really don't have a
good answer to that at this time. Yeah.
Sorry.
Hi, I have I I have a question about um
the business central partner. I I work
usually for customers directly and some
of them have the zero trust uh
procedures.
Okay. Um, can I block my partner from
accessing the production environment
uh from the partner channel
because the users accessing through the
partner channel are always created with
a super user permission.
Wait, what do you mean by they're always
created with super permission? Like if
they're not the first, you always lose.
If a if a an employee from a partner
Yes. has access through the partner
channel. Yes. Basically like to my
environment
or to my uh through the admin center and
my environment. It creates a user with
super permissions and I don't want them
to access the production environment.
Can I? So one way you can do it if there
is a page called configuration license
configuration if I remember correctly
and the kind of the GDAP and your
partner
uh users all get very specific licenses
that is one way that you can control and
give them very specific okay uh
permissions. Yeah. The moment they kind
of log in.
Uh I'm a big fan of managed identity and
I noticed that there is not much uh
features where I can actually do
business central and use manage identity
to connect to SQL database or for
example if I'm calling rest API calls it
would be much much easier to set up
manage identity directly if it's against
the same database rather than using or
two. So had there any plans for manage
identity or not? Totally agreed. I have
spoken with my colleagues. I think you
were at their session. I didn't. No. But
someone else asked a very similar
question and as of right now we don't
have a way to provide it so that you can
actually use manage identity from within
business central to call say some Azure
u service but we have plans to have a
discussion to see how and if we can
actually ensure that that is provided to
you guys because I totally agree it is
more secure to use manage identity
whether Uh there is a code code cop or
llinter which helps to identify such
problems in the code.
Not that I know of. Okay. Yeah.
Are there any other questions?
No. Otherwise, thank you all for
attending my session.
