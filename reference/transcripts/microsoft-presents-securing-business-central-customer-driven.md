# Microsoft Presents: Securing Business Central | Customer-Driven Best Practices and Real-World Cases

- **Source:** https://www.youtube.com/watch?v=yFnIxV72U9I
- **Video ID:** yFnIxV72U9I
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 45m50s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Welcome uh ladies and gentlemen for our
final session of today. We will have uh
two sessions with multiple speakers. Uh
for our second session, it will be a
brief introduction to the history of AI
form DBlue to co-pilot by Vincent. And
then for our session right now, we have
uh Muhammad and at who will be
presenting security business central and
customer-driven best practices and real
world cases.
All right. Hi everyone. I am Ed that guy
over there Edmono. I've been working
with Business Central and specifically
Microsoft uh for the last nine years.
I'm a member of the control plane team.
Uh and for the last three years I'm
actually leading security initiatives uh
across business central. Yeah. And my
name is Umar and I've been working for
Microsoft for almost eight years now and
I'm part of the engineering systems team
and also security champ for them. And I
and Ed have been working on many
security initiatives. So we want to
share some thoughts and uh real world
cases with you guys.
Yeah. So Omar and I usually work behind
the scenes in Business Central keeping
our cloud customers secure and up to
date. But the with the growing number of
security related questions from partners
and customers um through Yammer
specifically but as well as through
support tickets um we decided to host a
session uh to ask the most frequent
questions and see how we can apply the
best practices from the Microsoft secure
future initiative that I'm going to
introduce right now uh to customer uh
scenarios.
So let's briefly talk about the
Microsoft secure future initiative. So
uh and let's step back into 2023 for a
second. It was the year when uh cyber
attacks got uh smarter and sneaker um AI
powered scams, supply chain hacks and uh
uh they were pushing companies to uh and
governments to step up their game in the
the security game. And the Microsoft
response was kicking off the cyber cyber
secure uh future initiative which is um
long-term plan to rethink uh the way um
our products are being built across the
whole Microsoft making security the top
priority of the company. So far,
Microsoft has invested in uh over 13
months the equivalent of 34,000
uh engineering working full-time not
obviously only across business center
but across the whole uh Microsoft
itself. The initiative itself
is built um with around three um
principles secure by design, secure by
default and secure operation. Secured by
design means uh security comes first
when designing every product and service
not only business central. Uh secure by
default it means that the default when
you're creating a new tenant or a new
environment or any other source in Azure
should be secure exactly by default
doesn't require any additional
configuration and then secure variation
which means that all the security
controls and uh monitoring has to
continuously be improved to catch all
the existing and future threats.
Uh the initiative is built around six
pillars. Um protect identities and
secret, protect tenants and isolate,
protect networks and engineering
systems. And these pillars contain
overall 28 uh objectives which most of
them are actually long-term and require
uh they span several years of work. Um
these objectives are supported by
standards which are codified
requirements and these code standards
are continuously improved into paved uh
paths which are actually blueprint for
the developers to implement.
So we don't really want to talk about
the secure future initiative overall.
You can actually read all of it in the
links there. You can you can find it on
the web but there is a clear explanation
of all the the reports and actually
every four months there is a detailed uh
report with all the progress in
percentage across the whole Microsoft of
everything. What we want to do is to
focus only on two of these objectives
and specifically to what we have done in
business central and how these changes
can be applied to customers and
partners. So first of all we're going to
focus on the protect identities in
secret and specifically in this specific
pill are only about one of the
objectives which is about protecting
application with system manage
credentials. What does it actually mean?
It means that um for all the Azure
resources that are building up business
center in production, we're talking
about 36,000 storage account u 1,700
service buses uh more than 200,000 SQL
databases and uh a few Cosmos DBs as
well um and as well the entid
applications. As part of this initiative
uh we completely removed every
credential, every you know storage
account keys, every SQL database
username and password and only using
entry ID authentication.
So uh that was obviously a kind of
significant amount of work that kept us
busy for uh several months but that got
us thinking like can we do something
about it? Can we apply this to some to
to some of the scenario that partners or
customers are using? So here's the first
scenario. Web service calls to business
central APIs. Now uh a few of you are
actually familiar with this are using uh
service uh to service authentication
with business central and if you have
been using it uh you probably have been
following the instructions that are
basically stating to create an antid
application. and gave it some specific
permissions and then in this little part
over there says create a new client
secret and then from your application
you will be using and leveraging that
client secret uh to authenticate. Now
similarly if you're doing a call to the
business central admin API the uh the
documentation at the moment states uh
exactly the same thing that you have to
create a secret is there anything we can
do about it? Yes, absolutely. Let me
switch my screen.
So,
before we talk about secret secret list
calls to business central, let's talk
about some of the pitfalls of client
secrets. Um, they are obviously can be
exposed and stolen leading to potential
breaches in your organization. They
require manual work from your side. Uh,
they need to be uh rotated periodically
and they need to be stored securely.
That will increase the operational
workhead on on your organization. Then
if you have multiple applications
running uh with multiple secrets you
need to manage all of them and this can
be a complex process and can be
errorprone as well. Um and then it could
lead to sometimes be hard-coded secrets
in code which will violate compliance
standards in your organization.
So what can we do instead of using
secrets? We use manage identities and
these take care of all those pitfalls
that I mentioned before. They remove the
need to manage secrets. Um they also in
turn provide uh access to role-based
access control in Azure. So you can give
very granular control to your
application through the manage
identities and then they integrate
seamlessly with all the Azure services.
Um I have this small diagram that shows
how they work in practice. So basically
when you enable manage identity in on an
Azure resource, it becomes available on
that resource for you to be able to
authenticate. And it creates a service
principle for you uh in entertain. And
you can use that service principle to
give those granular role-based access
controls that I was talking about
earlier uh to the application that you
want to access. And then from inside
this Azure resource, you will be able to
get an access token to the resource you
want to get to. Um
so most of you might already have an
intra application that you are using
with a client secret perhaps uh to call
the business central APIs and you can
actually keep using the same entry
application but instead of using uh the
credentials now we will use federated
credentials instead instead of instead
of the client secrets I mean and here
it's a very overview of how how this
works. Um so we will use manage
identities to set up a trust
relationship between our application
federated credential configuration and
and the manage identities and at the
time of the authentication um the the
Azure resource will get a federated
token request through manage identities
which will then be checked against the
federated credential configuration and
if everything checks out um entra ID
will give a access token to you that you
can then use to access the resources
that you want to. So my demo is exactly
how that really works. Uh we'll set up
an enter application with federated
credentials, then give appropriate API
permissions to the app, set up app on
customer environment and grant consent
and showcase secretless API calls to
central. So let's see how this works.
So this is simulating a partner tenant
and in my partner tenant I have created
a manage identity and one thing to
notice over here is the client ID that
we will be using later uh to request an
access token from the Azure VM resource
and then I have created an Android
application and if we see the API
permissions under this one
we have API read rewrite all access from
business central
over here and under certificates and the
secrets
uh we have this federated credentials
that have been set up and it's trusting
the manage identity that I just showed
you earlier. Uh we also have a client
secret over here that's just to showcase
the demo. I'll be removing this later uh
to show you that we can also call the
API without it.
And once you have this app set up um
you'll take the client ID and you'll
send it to your customer.
And then I have a customer environment
over here. Um they will need to go to
the entra. Oops
application section
and I have already set up uh this one
over here.
So they will need to add that client ID
over here grant the consent and then
over here we can also leverage the uh
permission sets inside business central
and you can just only give permission to
what you want the partner to be able to
access. So in this case for example
we've just only given read access to the
data in business central.
So that this setup is done and
then we have this Azure VM uh that I
created in the partner tenant uh where I
have that manage identity and
application and under identity of this
virtual machine user assigned I'm
trusting that manage identity and this
enablement uh makes this identity
available on this virtual machine uh
that we will use now.
So I I have logged into this VM right
here
and I'll just show you some code. Uh
this is standard uh way of getting an
access token using MSA library. Uh we
have the application ID in in our
partner tenant. This resource tenant ID
is the customer tenant ID.
And then this is the manage client ID
will which we'll use later. Uh but I'm
first using the client secret that I
showed you over there to get an access
token. And then under that environment
where we gave the consent, I'm just
requesting a list of all the companies
in that particular environment. So let's
just run this and see if this works.
So we see we get a list of companies
this environment has two right now.
So that that's how it was working
before. But now let's go and to our app
and let's delete that client secret. So
we make sure that it's not being used.
Now we only have the feric credential
over here that is assigned to that VM.
And I have some code over here that
shows how to get an access token from
there. I'll just
comment out this part
and
uncomment this one.
So as you can see there there's no
password or credential that is being
used over here. The only thing we need
is the ID of the manage identity uh that
we created before and we create a client
assertion using that manage identity
using this code over here
and then we pass that to our
confidential client
and then it can get an access token for
us without using any secrets.
And then let's run this and see if this
uh still works as we want it to.
So we were able to get the access token
and we are still able to call inside the
environment and we can get the list of
the companies from there as well.
So that's good. That's works as
expected.
So the takeaway from here is that
please start migrating to
manage credentials. As you saw the code
is actually quite straightforward and it
will bring you a lot of benefits.
Now the second thing I want to talk
about is auditing in Microsoft purview
and what that means for business
central. Um I hope you guys are familiar
with what Microsoft purview is. It is
the def facto solution for Microsoft for
auditing and it has a lot of benefits.
It tracks user and admin activity for
security compliance. It has risk
monitoring capabilities, detects
anomalies, unauthorized access, policy
violations in your organization. Then
you can set up different data life cycle
management policies and it also has a
portal where you can search uh for the
audit logs across the whole tenant uh
not only just uh for business central
and what it specifically means for
business central is that business
central automatically emits all the
auditable events to perview. Um we have
a full list of events in our learn site.
Maybe we should take a look at that
quickly.
So under here you can see we have some
events. So anything anytime you do
anything to administer the environment
configure extension administer the user
configure co-pilot an event will be
emitted to perview and under each
activity sorry these are the events and
under each event we have a list of
activities. So for administrative
environment event for example anytime an
environment is created renamed copied
scheduled and update for we will get
auditable logs inside Microsoft preview
so that's all great um
now let's see what we can build upon
Microsoft uh preview uh in our case so
we'll set up an entra app with again
with f federated credentials and give
the appropriate API permissions and
we'll build Azure functions to query and
receive audit results from Microsoft
preview and then we'll build a simple
logic app to query these results and do
something actionable based on that.
So what I've done over here is uh
let's try over here
I have an enter application um and if I
go to the API permissions
we have given permission to audit locks
query read all through Microsoft graph
and under certification secrets there's
no client secret over here it's only a
fitted credential that is trusting a
managed identity
and then I have built
two Azure functions.
Um, one of them is building a query and
sending to Microsoft preview and the
other one is receiving results uh and
returning those records.
And under this if we see
identity
and user assigned we have assigned the
manage identity to this function. uh so
we do not need any secret uh
client secret we to inside this function
it can just leverage the manage identity
inside so let's see what code is behind
these uh two functions that I showed
over here
so the first function is just using this
similar kind code that you've seen
before using manage identity to get an
access token to Microsoft graph and then
it's building a query to sent to
Microsoft preview. Um we're just doing
last 24 hours and we're getting all the
records of type business central
and we we're just sending off this
query. And in the second function
we are through the ID of the query that
we sent in the previous one. uh we're
getting the results and in this
particular case
we are looking for administered
environment
event and the renamed environment
activity.
So if you find any audit event in last
24 hours where somebody has renamed an
environment on your tenant we will
return those records.
And how am I using this in the end
is that I have a simple logic app that's
running on a recurrence every 24 hours.
It will submit the query, parse the
result, wait for a little bit for the
query to complete, get the results, then
parse it and then the condition is that
if there was any record returned, it
will send you an email. So I hope this
gives you guys some inspiration how you
can uh create these simple automations
uh that will let you know of any
suspicious activity that's happening on
your tenant.
So the takeaway
from this one is
that you should look at the exhaustive
list of events and activities business
central image to perview and familiarize
yourself with the perview audit search
portal. I will show you that how that
looks as well.
Uh this is the perview portal and you
can basically manually search for audit
events over here and if you're looking
for for example business central there's
a record type for business central that
you can select over here and it's the
same process you can you will create the
query it will run for a while get the
results and then you can see the results
and then you have some inspiration of
how to set up quick automate automations
that u will let you know of any
suspicious activity on on your tenant.
So from here back to you.
All right. So until now we focused on
the examples um on the identity layer.
So basically on who is accessing
resources rather than from where they
are accessing resources and to build a
defense in depth strategy you need to
combine more than one of these um
methodologies. So um let's talk then
briefly about uh the protect network
layers. So um one of the objective of
the protect network layer sorry pillar
especially objective two was to apply
network segmentation and micro uh sorry
network isolation and micro segmentation
to all Microsoft services not only
business central. So uh in order to do
that every service in business central
had to um have something that we call
service tags. Service tags are actually
um predefined set predefined and
reserved set of IP ranges that are
dedicated to specific services. I'm
going to explain uh what actually this
is about. But the main reason as you can
um you know uh deduct is actually to be
able then to create uh firewall rules
for upstream and downstream services to
only allow the traffic to services based
on their outgoing uh and incoming IP
addresses. Um
again based on this one uh what we have
recognized is that so first of all we we
have service we had service tags in
business central since 2023. So it's not
really something very new. Uh but we
realized that in order to adhere to the
um
secure future initiative uh
requirements, we had actually to to make
some additional changes to be able to
segment slightly more uh all our network
and uh actually with this as well we
introduced support for for IPv6. Um,
one important thing we actually realized
as part of this process is that um, our
documentation that we have published on
aka.ms.bc
security there is going to be there is a
link at the bottom of this presentation
at the end of this presentation. Uh, it
actually tells you
what can't be done not really what you
can do or how you you will be able to do
it. For example, I'm going to show you
an example on on um trying to use
service tags for storage account and
basically the documentation explains you
very well why you can't do it but it
doesn't tell you how you could achieve
that. Okay. So this is actually the
customer scenario that we are trying to
solve. So uh let's say you have an
environment on a cluster
and then you have um partner resources
or customer resources that are in a
subscription hosted by by the customer
either you know a customer web service
or a customer storage account and the
outgoing traffic is coming from business
central using a public IP address. Um
similarly resources could be behind a
customer firewall or some other sort of
programmable firewall. And then um so
you have calls originating from business
central either from a PTE or for an app
and you as a responsible of the services
the customer related services you only
want to allow traffic from business
central not from the whole internet.
Now uh as I said we're going to talk
briefly about service tags. As I said
service tags are group of dedicated IPv
ranges. So they are not really part of
this Azure cloud service tag. They are
kind of dedicated one reserved only for
business central. They are IPv6 and IPv4
ranges and we have within business
central other different services tags
that we are using internally and they
are not publicly uh available. Um the
list of these uh IP addresses uh is
updated not super frequently, not very
frequently, but it is updated and it's
published. Uh there are different ways
on how to obtain this list of IP
addresses. And I'm going to um show you
how to do it. Now the important thing
about these is that these IP addresses
are being reused. So they are part of
ranges and every time we create new
clusters or we remove clusters you know
we delete clusters and for upgrades or
uh
there are several other reasons why we
are creating and working on clusters but
basically it's reusing IP addresses from
the same address pool so it's not like
we are constantly updating this list
adding new addresses but there might be
reasons uh for example when we are on
boarding to an new Azure region or we
have reached the capacity of the number
of reserver IP IP range is that we will
be requesting for new IP ranges on an
existing region and then um the list
this list of IP addresses is going to
change. Uh the service tag which is
actually uh the theum cumulative list of
all these uh IP address ranges is
published together with a lot of other
service tag
tags published by Microsoft and uh it's
a list which contains all the IP
addresses for all the different regions.
It can be used in uh network security
groups to create ACI rules but as well
on primish firewalls um to which are
allowing you to block to block traffic
from specific ranges. So I'm going to
show uh a few demo. Now there is a
slight issue with this which is
mentioned here. So u a few weeks ago
this service tag here which is the
dynamics 365 business center which has
been active and uh uh you know publicly
available since 2023
um due to a change in Azure networking
has been switched from GA to uh
development mode. So the service tag is
still valid and available however is not
selectable via the portal. There is a
workaround to get around this problem
which is basically just directly
specifying the tag in the in PowerShell
when you're creating the rule or using
an AR template but in a couple of weeks
is going to be uh resolved because um
there is a change now that is being
pushed out now u
okay so
I'm going to show you the scenario that
I want to try to resolve okay so first
of all I'm gonna
demo service tags.
So
I have a network security group. As I
said the network security group is this
resource that can be associated to VNET
and um you know uh directly to
networking interfaces on VMs. In here I
have created a network security rule
which is allowing traffic on port 443
TCP for all the Dynamics 365 business
central service tags. So all IPv6 and
IPv4 addresses of business center will
be able uh traffic coming from these
addresses will be able to uh go through
this uh network security rule. Um just
to mention the issue that I was talking
about here uh in the when you're
creating the service tag you can select
service tag as a source and in the list
here you normally will be able to see
dynamics 365 business the central but
unfortunately as I mentioned for the
next couple of weeks it's not showing up
here um as a workaround you can just
basically do an ARM template and uh
write the name of the tag in there in
the ARM template. So it's kind of a
temporary workaround but the rule
actually works and there is uh no
problem in there. So uh this is actually
how you can create rules specifying the
service tag. But um
before talking about some of the kind of
problems with service tags themselves. I
want to show you what these ranges the
SIP ranges look like and a way to
actually obtain them. So for that I
created a workflow in a logic app that
is calling an Azure rest API which is
called service tags okay on could be any
subscription because this is actually
not uh getting IPs for the resources
that are related to the subscription.
This is basically listing the the whole
list of service tags available in
Microsoft. So um again sorry talking
about managed identities. All right. So
uh in here we are using the system
assigned managed identity of the
assigned to the logic app itself to be
able to to query the list of service
tag. Why? Because this endpoint actually
requires authentication. So uh I have
added read access to using arbback
permissions to the subscription itself
and with that just we will we are able
to get the list of service tax. If I
check the latest running history just to
show you um how the output looks like.
So this request by the way doesn't you
know has doesn't have any parameter that
needs to be passed or anything else. The
raw output
is uh a JSON message that contains the
list of all the service tags public
service tags published by Microsoft. So
action group is actually a service tag.
I don't know exactly which services this
about but uh as you can see here it it
obtains the list of all the IPv4
addresses and
long list and the IPvC addresses as
well. So if you create a firewall rule
with action group as a service tag you
you are kind of sure that the the tag is
always updated and will always um
without any user intervention be able to
get you know the latest versions. Now I
want to focus for a second here on this
uh change number. Change number is
actually the version number for these IP
prefixes. So every time there is a new
specific uh IP range that is being added
to this service tag, the number is
increased. Why is it important? Because
I'm going to show you an automation that
I have created to update um the firewall
rules on a key volt only when that
number increases.
So another way
to obtain the list of service tags is
actually the IPs is actually through
this um published publicly available URL
which is just directly the JSON file
itself. Same results that you're getting
through the other code. The only
difference is that in this case it
doesn't require any user authentication
but I just wanted to showcase a
different way to obtain the list of IP
addresses. So in there from the JSON
object I'm actually just filtering out
only for the Dynamics 365 business
central um service tag and in there
because some of the resources such as
for example key volt are only supporting
IPv4 ranges uh in the firewall rules
they're not supporting IPv6 so in here
I'm using a kind of a small trick to
identify which ones are IPv6 which ones
are IPv4 and construct two arrays with
the IP addresses
And I'm going to store here in a
variable the change number as well that
I did show um earlier. Now
based on that one I'm as well um sorry
not based on that one as well I'm
getting the list of uh key volt
settings. The reason why is um I want to
update the key volt the customer the
simulation for the customer created key
volt that I have in here. I only want to
update it obviously if there has been a
change in this version of IP addresses
this change number. So in order to do
that I have stored here in a tag on the
key volt itself the the change number of
the latest version that I have used to
update these ones and just to have a
look briefly the firewall rules that I
have at the moment on the key volt are
these two uh kind of random IP addresses
that I have just added there. So the
automation that I have written here is
just getting the list of you know the
tag from the key volt itself is uh is
doing is kind of doing an if condition
between the value of the tag and the
value of the service tag version that I
have obtained from business central
central then it's constructing a network
ACL object that is then used here to
call um the key volt itself and do a
patch on the firewall rules and update
them and then setting the tag and
sending me a message. So if we run this
automation now, let's see. Should be
quick.
Okay. So this actually by the way
obviously with the recurrence can be
scheduled to run um even every day there
is no issue. So I'm getting the list of
service tag in here. I'm constructing
these two arrays as I said of IPv6 and
IPv4 ranges. P4 and P6. Then I'm getting
the tag from the key volt. Here it was
15 and I'm initializing a variable. Uh
and in here I'm actually because 15 is
obviously lower than 16. I'm going to
update the uh the firewall rules here.
I'm constructing the actual object that
is needed for the rest API to update it.
Uh I'm updating the key volt here and
then I'm setting the tag to version 16.
And then hopefully I'm going to even
going to post a message here to my uh
workflow.
Where is it?
Here that states a change has been
detected in the public IP ranges and the
key volt firewall rules have been
updated from version 15 to 16. Now if we
just go back to the customer key volt.
Okay, refresh. Yeah, we can see that the
change version of the tag is 16. So the
next time this is going to run is not uh
going to update any firewall rule. And
in here it has populated uh all the all
the rules like all the firewall rules
with the all business central IP
addresses which um yeah.
All right. So uh
okay going back here.
So yeah
now one of the questions we are getting
quite often is can I use service tags on
a storage account? Uh this is one of the
most common questions we are actually
getting. uh the you might I might be
tempted to say yes uh but it is not
true. Okay, it's it doesn't work. So uh
first of all, you can't use service tags
on a storage account. Uh the storage
account itself in the network firewall
rule only supports IPv4 ranges. But I
mean you could use an automation such as
the one we have created to update these
firewall rules. Um however there is a
big uh question mark which is uh
unfortunately if the VNET of the calling
service is in the same or paired Azure
region as the storage account you can't
uh actually create the reason is uh you
can't actually use firewall rules the
reason is with a PV4 the the main reason
is there is a limitation in the Azure
networking and the IP addresses that is
seen by the um by the storage account
itself in the firewall rules, you can
actually check that if you're enabling
the diagnostics uh logs on the storage
account is an internal IP address. So
the calls are anyway rooted through the
internal network even if um
even if you know you haven't said that
explicitly. So short answer is no. You
can't really use it. You might try as a
workar around to create a storage
account in another region but you might
not want to that for I don't know
compliance or privacy region. Maybe you
have the storage accounts in North
Europe and you want to keep as well your
storage sorry you have the application
services in North Europe and you want to
keep the storage accounts as well in
North Europe. Now so then what can I
use? Can I use virtual network rules?
Another way is actually to specify
directly the uh ID of the subnet within
the VNET on where the business central
environment is actually created. So in
this example you can see you have
clusters our cluster internally I have a
VNET at the moment we are not exposing
it publicly but even if we were to
expose it will this be possible uh not
really because when we are upgrading or
moving environments from one cluster to
the other uh that will have a new VNET
so uh the communication um like that
will not be allow listed so you you
can't really use that so then is there a
solution for all this problem. So there
is a way to actually almost seamlessly
work with this which is creating an
Azure function. Um Azure functions
themselves support uh firewall rules
which are based on service tags. So as
you can see here you can create in the
uh Azure function itself in the
networking configuration you can select
to allow only specific IPs or uh you
know service tags to uh call into the
Azure function and then you can specify
to have a deny rule and only allow
Dynamics 365 business central service
tag as in the picture. So uh in that
case when the environment is moved over
to another you know cluster uh you will
be able to connect to it. Now the
storage account which is behind the
Azure function that's you know uh could
be uh completely off the internet and
you can use private links to to write to
that that's uh it's not a problem. The
main advantage of this approach
obviously you don't have to maintain any
automation or anything for uh the IP
ranges. So uh a few takeaways from uh
this session
where possible go secretless. Obviously
this demo works if you are in control of
the resources right if you have the
caller resource is actually in Azure and
you can assign a managed identity to it.
If it's not in Azure or for some
developer scenarios you can't really use
federated identity credentials. So but
if you can and you're moving your the
caller workloads to Azure uh then you
can go secretless using uh managed
identities where possible uh in some
cases you can't use the managed identity
directly as Omar did show you have to
use an entid application you have to
specify you have to allow the API
permission yeah to allow the API
permissions as well in that case you can
still use manage identities use the
federated identity credentials
um for Azure resources the the the
obviously um try to switch over to use
enter ID authentication. So disable one
one way to be sure and actually it's the
way that some of these secure initiative
uh KPIs are actually tracking success is
by disabling local authentication on the
resources. So SQL storage service bus um
and Cosmos DB as well they are all
having a setting which has been added by
the secure future initiative to
completely block any other type of
authentication that is not entid and
ultimately as I said this is the way we
are kind of measuring success uh to make
sure that we are only allowing entid uh
authentication. Uh one of the questions
may be uh okay but I need to you to
create SAS URLs. you can still create
sus urls as well for your storage
account. Uh the only using the one of
the identities obviously that uh had has
access. One of the um you know
constraints is that the maximum validity
for that SAS URL is 7 days uh was much
more before when it that was actually
created based on the storage account key
under the hood. Um now one other thing
actually is uh making sure you have
anonymous access disabled on the blob
storage. Obviously you don't want to do
all this work related to authentication
and have anonymous access blob access
enabled. And then uh as we mentioned as
part of the um networking effort um
where possible obviously um add a second
layer of protection adding um blocking
traffic to your resources using firewall
rules. And in the future um there is
network security parimeter which is a
feature now in preview which will
actually simplify um all of this
hopefully. Uh we think it's going to be
great. And uh
another thing we didn't have time to
talk about is about uh elevating
yourself to have access only when
needed. So avoid obviously avoid having
persistent elevated access. There is a
feature called uh pim in uh in Azure
that you can use to elevate your your
permissions only when needed and please
leverage that. Now the documentation uh
for a few of these features uh even the
ones that are telling you what not to do
are under ak.msbc security but we will
it will be refreshed soon. We are
planning to revamp all that
documentation include the samples from
today's session as well. And then uh one
last thing if you have vulnerabilities
in BC if you find a vulnerability please
report it using that link we have a
bounty program uh as part of all
dynamics and uh you will uh you will
even have the chance of getting some
rewards uh out of that. Now if you there
is another session that we are
recommending you to go to which is
tomorrow which is about securing your AL
code. So Derek is going to post that and
then uh uh we can open up to Q&A. You
can uh reach out to us directly or Yeah.
Look at the there's a question online.
Any question? Yep.
Hi. Um, in regards to the
uh manage permission, not permissions,
the not secret way, managed identity.
Managed identity. Thank you. Um, do they
also have an expiration date of two
years or are they permanently? They are
permanent. Perfect. Good. That's all I
needed. So, uh, the way it works is that
uh is basically getting the managed
entity is assigned to an Azure resource
and the Azure resource is to is getting
a token from an internal endpoint. The
token has a short validity but the
assignment of the identity is you know
depending depending on you. So yeah also
just want to clarify that there are two
kind of manage identities. The one I
showed is a user assigned manage
identity and then there is a system
assigned managed identity and that one
is refreshed when the resource is gone.
Then the system identity is also gone
but this user one stays and you can
assign it to multiple resources.
I give a t-shirt. Yes.
Any other question? This one.
You get the t-shirt. You give the
t-shirt.
Yes. So, I'm using a client secret um
authentication from within Business
Central. Is it possible to use
federation authentication from within
Business Central? Yes. Ed uh no
unfortunately that part of the flow
still is not is not changing there are
several reasons but we are in a sus
environment we don't have identities per
tenants and yeah it's a multi-tenant
environment so it's
not possible right now
yeah a t-shirt perhaps any other
questions
Is there any question on the app?
We cannot use manage identity and secret
is not secure. What would be the
recommended way
for integration with external uh
applications when we're coming in to BC?
You mean coming from outside in or yeah
from outside because if I give a secret
right someone who steals it can access
it I cannot limit on BC side that hey
that guy that comes but it's really that
guy who I give access to.
Yeah I mean manage identities work
inside Azure as we said before if it's
an external caller then I don't think we
have any other solution for it right
now. calls from business central to the
outside. No, from outside to business
central for example. From outside to
business central how can I ensure that
outside
is a person is the one I gave a I don't
know maybe the conditional access
policies on the tenant itself.
Yeah but what if it's expected? Yeah
it's yeah I don't know it's a yeah we'll
we'll go back to that.
There's one up there.
Hi. Uh, so I'm definitely new to this.
So what about uh securityurities on with
on prem clients
or is this just for
SAS?
Uh yeah, this one was for SAS.
I think we would have to get back to you
on that. Okay. Yeah, we can't use
managed identities in on prem. It's uh
you you don't have you can't assign an
identity to Yeah, you you need a
resource in Azure to be able to sign
when identity.
All right, so thanks a lot. Feel free to
reach out or we are going to be at the
booth uh later. Thank you.
