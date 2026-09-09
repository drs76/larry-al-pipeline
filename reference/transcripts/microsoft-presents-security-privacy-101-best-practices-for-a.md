# Microsoft Presents: Security & Privacy 101: best practices for an AI and data-centered world

- **Source:** https://www.youtube.com/watch?v=YUNWXxb2HrI
- **Video ID:** YUNWXxb2HrI
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 39m13s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

AR and I we're going to talk about
security and privacy today we're going
to talk a little bit about how do we do
how do we approach this topic in
microsof and try to give you some
examples of operational you know advice
that we use and some things that can
help you also increase your posture in
there um so who am I and why am I
talking about this thing uh so my name
is Austen um I recently rejoined
business Central and I'm leading uh one
of the AI Solutions forly know as
application uh teams but
I let's see yeah actually I've been 11
years at Microsoft I was back in fno for
three years another five years in
business Central before and then I
started like a Little Rock tour around
the US uh so I was working with the Bob
team for another three years and I used
to be a security lead and responder of
incidents and I was also working on the
Privacy side of things I did the
implementation for gdpr for the internal
data for business
Central so let's just start with what
actually security mean right um it's the
practice aim at you know defending
against cyber attacks but most people
stop thinking about security there but
there is a very important piece which is
actually mitigating their impact once
you get something when someone attacks
you and you get inside you you have to
minimize the pain and that is one of the
pieces that is more important um
actually if you look at the picture in
the right hand side that is the Cyber
defense Operation Center of Microsoft
and it's one of those fancy rooms with
like screens all over the place and the
news and all of that stuff and the big
piece of that room is that protect
detect and respond so protect is what
most people think when they think about
cyber security but you know figuring out
that something is wrong and you have
someone inside is at least as important
and kicking them off afterwards is is
also massively important so actually
this is what people used to think when
they think about cyber security we put a
massive wall around the stuff that we
want to protect and we hope that no one
gets in the problem with that is that if
you know there is a small Hall somewhere
in the wall or someone finds a whale
tunnel under your wall and you're
screwed your the Keys of the Kingdom are
gone so what we tend to do instead is
what we call assume Bridge assume that
someone is already inside and then
figure out how you're going to figure it
out that they inside and figure it out
how you're GNA kick them out
basically yeah yeah so uh now we've
heard from Augustine and why he's here
and what he's going to talk about but
perhaps you're wondering who am I and
why am I qualified to talk about any of
this right so unlike Augustine I never
left business Central and in fact some
of you might remember me from previous
years talks about Power Platform but now
I have a new role where I'm working on
uh co-pilot experiences and co-pilot
chat but in my uh spare work time I'm
the Privacy for the client teams so if
anybody on like with my colleagues have
questions about privacy issues then I'm
the person that they would go to to find
out the answers right so let's talk
about what privacy means uh security is
all about protecting your data from Bad
actors but privacy is all about how your
data is handled by the people that you
trust
and privacy and security problems often
shared the same solution it's all just a
matter of perspective so there's going
to be a lot of overlap of what we're
talking about today from different
angles and so just a quick refresher
what do we mean by your data right when
I say your data you're probably thinking
about uh data that is about you right so
that would be your name your address
your contact information obviously
that's very personal to you but it's
also data that is created by you so that
would be like sensitive business
information or credential or even the
things that you type in as search
queries that's all uh you know
information that was provided by you
that is is your personal private
information it also covers data which
identifies you so when you use the
product we're going to assign you a
unique identifier so that we can track
things like error messages and you know
usage behavior in the product and it's
also all of the data that is linked to
that identifier and finally data that is
shared by you with Microsoft so if you
provide us feedback or you have
conversations with our support engineers
then all of that information is also
your own personal data and contains
sensitive information about you so how
does Microsoft actually govern data
privacy how do we make sure that we
follow the regulations what are our
internal policies that's some of what
we're going to talk about today so I'm
just going to go through each of these
one by one the first thing is obviously
when you purchase a product from
Microsoft then you enter into a service
agreement with Microsoft and as you can
see the first thing in that service
agreement is your privacy right and we
detail the terms of the Privacy
agreement all of the things that we're
doing to protect your data and it's the
first thing in the list because we know
that your data is important to you and
it's also very important to us we want
you to be able to trust us and so we
have all these policies right so there's
also laws that we need to comply with so
the general data protection regulation
or gdpr is an EU law which grants you
certain rights regarding your data so
you have the right to be informed about
and consent to what is collected why
it's being used and who is collecting
that data in this case us and you also
have the right to view edit delete and
Export your data as well so you have
total control over what data we hold on
your behalf and so we need to comply
with this law um and so the way that we
usually do that is that you can view and
edit your data and and get a copy of it
all just through the product right this
is something that's a natural part of
using the system if you want to update
your sales invoices or you know export
your data from the database you can do
all of that through Tech or through the
UI and when you sign up to use business
Central you have agreed to the terms of
service and to the service agreement
which we laid out before so we know that
we've obtained your consent before you
even log in so most of these rights are
taken care of just by the nature of the
product itself but there are some
special conditions to this so for
example if you've provisioned business
Central in a European environment and
you have a like a tenant that's based in
Denmark but your Power Platform
environment is provisioned somewhere
else it's a perfectly valid setup but in
this case we need to inform you that
your data is going to be sent out of
geographic boundaries there might be
other different compliance um
certifications that are required by some
software and not others and so when you
use one of these features you use one of
these Integrations we need to get your
informed consent so we will show you a
privacy notice and you can't continue to
use the feature until you've accepted
this and we keep a record of the fact
that you've accepted that to cover
ourselves and make sure that we are
doing things in a compliant way
So speaking of gdpr uh in 2020 there was
a little bit of a change to how you
would traditionally handled data with
gdpr right so uh there's a guy called
Max shm who often goes to the European
Court to fight on your behalf as users
for your data privacy rights and in 2020
there was a court ruling that the
existing agreements where you would be
able to transfer data from the EU to the
US were actually a violation of gdpr
because the US intelligence Services
have access to your personal data when
it's based in the US
and so in order to combat that Microsoft
implemented the EU data boundary and
this is a Microsoft policy right it's
not something that you'll find anywhere
else this is something that we have
implemented to make your lives easier
right so if you provision all of your
services so if you get business Central
and Power Platform and all of the other
services that you've linked together in
the European data boundary which is uh
I've drawn it out on the screen right
this is a map of all of the countries
that are in the EB obviously there are
some countries that are in Europe that
are not in this list right so so this is
the the areas that are covered by this
and uh as a partner when you provision
all your services inside the eud you can
trust Microsoft to keep that data
compliant with gdpr so you only need to
worry about your own
solution uh and finally I want to talk
about compliance certifications right so
all of the products in the business
Central ecosystem all of the the
business applications that we provide
and even Azure itself are required to
obtain privacy and security
certifications and so there the ISO 2701
that's about Security Management Systems
2771 is about privacy Management systems
and then stock two is all about how you
actually you know secure the data and
protect people's privacy and so it
covers broad areas for example
encryption obviously we want to protect
your data from Bad Actors Access Control
so making sure that the right people do
have access to your data data redundancy
so let's say that our data Cent's got
down or some of your data is corrupted
then we need to be able to secure your
data and ensure that we have a backup
copy uh service availability so if the
service goes down we still need to
guarantee your gdpr rights we still need
to make sure that your business can
continue to operate so we need to make
sure that the up time is to a certain
level and then we need continuous
monitoring right because as great as we
are things will break and the service
will go down data Sensers will get
corrupted and so we need to make sure
that we're aware of that and that we
have an incident response plan so that
we can you know secure data as fast as
possible and so these certifications are
awarded by Third parties right we do all
of the work and we provide the evidence
but somebody external to Microsoft needs
to certify that we have satisfied all of
these requirements and so you can be
sure that when you use business Central
you're using an industry standard
product and we have all of the um you
know protections that you would expect
in
place cool cool cool so we talk a little
bit about what security is and what
privacy is now we're going to talk a
little bit about some of the operational
things we do in order to comply with
those certifications or some of the
internal um processes that we follow and
I I talked with one of the bbp cvps
corporate vice presidents from the
response Center that we talked earlier
about and he had this very cool quote
that maybe it's not extremely quite
specific but I think it's a good way to
think about this topic um he maintained
that 50% of the fight of improving your
security posture um was about inventory
and maintaining your assets we dig down
into that the other 30 40% is about
other security fundamentals like
authentication uh encryption all of
these things and the last 10 around 10
20% is about just thinking about
customer perspective be empathetic with
your customer and also on the other side
of the coin think as an attacker how can
I get in into my own systems if I was
trying to break in how would I do that
so we'll take a look into that a little
bit more
see yeah it's working cool one thing if
you get one thing out of this and we
will go back into it inventory your
stuff you cannot protect what you don't
know it
exists and actually we were doing an
exercise a few years back we were trying
to do that attacker mindset I was saying
before and the patient zero that we
managed to actually breaking into some
of our systems was a test machine that
no one knew it existed for like four
years and we just kind of found it
somewhere and it happened to have some
credentials and that was the starting
pivoting into the rest of the system so
really really really take a look at
everything you own in the company
everything you're using assets software
licenses whatever the heck it is and
write it down in a paper in one note it
doesn't have to be anything too fancy
just think about what you have because
everything else comes based on this
right so this is a very massive
Improvement once you have that list and
you know what you have be very critical
about what is in that list do I really
need this thing can I actually you know
kill half of the VMS that are sitting
down somewhere that no one is really
using um as much as you can reduce
attack surface it's going to be much
more difficult to get in that that we
should have killed that machine you know
years back right and it was definitely a
very big risk so Marie condo your
if you can
go through it reduce simplify uh
eliminate let's
see and once you that have that you know
what you have the minimum amount of
machines keep them all up to date pick
up all of those annoying messages about
updating your software click yes
automated if you can there are some very
cool tools like Wing getting Windows or
Mac updator in in Mac keep them up to
date because I don't know if you know
but this is a few years does any of you
have seen this message before I cannot
see much the hands maybe we can do like
a
small Okay cool so if you click no into
that one in that particular one I don't
know if you see but in between the fix
your mouse wheel there is something that
says fix CI hacking notepad++ issue that
was a publicly available vulnerability
released by Wick so if you didn't press
yes suddenly your machine was probably
compromised or potentially
compromise and not only that but uh
let's
see this is a few years back but there
was a very nice article about uh the NSA
talking about the vulnerabilities that
the state agents were using to get
inside machines some of them were like
many years back right this was 2020 this
is one vulnerability in 2015 and was in
the top 20 of vulnerabilities that were
used to get into people's you know
remote execution which is a very very
bad one
cool that's that's the 50% thing so
let's get that out of the way and then
let's jump into um other fundamentals
right think about your story about
access control think about who you know
who has access to things who are you
giving access to your internal machines
your internal privilege actions um
another one of this ones who in here can
actually push code into production just
with your username and
password too many people in here can
access production resources in their
regular machine like the one they take
home every day and they install WhatsApp
on cool so the think about these things
because there is a bunch of like think
about the different factors of
authentication when we're talking about
passwords is something that you know but
now we are starting to be more and more
um familiar with things like like Okay
can authenticate with my phone or I have
a a juie key or something to plug or
maybe I'm authenticating with my
fingerprint or something like this it's
always great I think you heard this a
lot but multiactor for the wing right at
least two Factor authentication
everywhere if you want to go crazy go
three Factor authentication that also
works but two Factor will be great um if
you can like you know a fedo token like
ju key or an authenticator app like the
Microsoft for the Google app whatever
just it's going to increase your your
security at on um if you can avoid it
avoid the SMS phone authentication it's
less it's still way more secure than not
having it but it's probably the worst of
this all and lastly there is also like
if you don't know this website have been
pound it's by Troy hunt which a very
very cool security researcher and it
publishes all of the leaks of like
passwords and breaches and everything
like this and you can set up some
monitoring if you want and see if any of
your passwords have been licked into the
internet uh yeah so what I was saying
now right use an identity provider try
to go passwordless try to set up a
password manager if you are writing code
that you are like put your secrets in a
dedicated Secret store don't put them in
code don't put them in a notepad file
just put them somewhere and have a think
about what are you going to do if you
have to rotate this Secrets if you get
leak how are you going to change them
especially in your production
systems but everyone can mess up on this
that's what I'm saying as many many
things that you have is better because
does anyone want to guess what the pass
were for the Most Wanted cyber one of
the most Wanted cyber criminals for the
FBI
was you're not far off it was not far
away is his cut name one to three
actually so his machine got taken by the
FBI he managed to lock it on time but it
didn't take that much to actually get
the password so try to go to AA try to
do all of this extra stuff because it's
not everyone can mess up so try to put
the things in to avoid it very worthy
slide but just basically pipelines just
use tools for this right there is static
analysis there is dynamic analysis use
things like code ql or use cred scan uh
use a ton of like there's a very cool
open- Source Community for tools um that
check for vulnerabilities like those
ones that we saw before the very
aggressive managing Secrets right um do
not put secrets in Code Credit scan is
great block people from putting
credentials in code and removing them
from your code doesn't work because it's
in your Source control history so that
was one of the first things we were
doing we're trying to you know break
into our own systems look for commits
that says oh I'm removing a password and
then you go and test that password like
nine out of 10 times it still works
shouldn't happen rotate the
password uh um
yeah lastly I'm going to talk a little
bit about encryption as well you know
encrypt everything that you can think
about what you have around you have any
domains that you have to um use
something like L encrypt we the data
that we have microsofts at least you
know always encrypted at rest and most
of if you are provisioning some cloud
services some blobs be sure that you set
up the configuration if it's already
there but don't change it to be
encrypted at rest all the time be sure
that we have anything to ensure that the
Communications are decrypted in in
transit and then if you have very
specific cases like some medical domain
things like this there is even the
possibility to go into incr it at use so
it's incr it in your in the ram even on
the machine there is things like always
incr for SQL that does this type of
things for very specific uh domains and
just for one extra thing you can
actually even in some cases bring your
own key and encrypt stuff with the key
that you only
know yeah so speaking of encryption it's
not only relevant to security it's also
relevant to privacy and so as partners
you may be working with customers that
are in domains with like extremely
sensitive protected information like
healthcare or with government
organizations and so in this case we
allow you to protect your data with your
own key with the customer's own key and
so I'm just going to quickly explain how
that works and then why that is
important and why that's something that
you might want to onboard to and so the
way that it works usually is all of your
data is in your a Azure storage account
sorry and uh your customer manage key is
in the customer key vaa so the key VA
administrator grants access to an
account that is shared between Microsoft
and the customer and when the Azure
storage account needs the key then it
can request it using the managed
identity and so the customer manag key
is used to encrypt the storage key that
is kept alongside the data and if we
want to access the data then we need to
get access to the custom manage key to
decrypt the storage key right so it's
like a layered encryption method and so
the reason this is relevant to privacy
is that Microsoft itself cannot decrypt
your data without access to the customer
manag key and you can revoke access or
revoke uh rotate sorry the key at any
time and so with a customer managed key
you control who has access to the data
and this is a legal requirement in many
Industries and so now business Central
is offering this and if you're in one of
those Industries then you can on board
to this system uh Microsoft also runs on
a policy of least privileged access and
so oin was asking before like how many
of you in the audience can access
production resources and customer data
from your own personal laptop well
Microsoft we don't do that right we need
to take your uh privacy and security
more seriously and so we're only allowed
to access customer data and production
resources from restricted devices that
are locked down in terms of the uh
websites they can access network
requests they can make software that can
be installed and we need to have special
accounts that are only used to access
these resources so that we can keep an
audit Trail and ensure that we Grant the
right access
uh when a Microsoft employee requests
access to customer data they need to
provide a justification and there's a
select group of approvers within
Microsoft who are able to grant that
request and those permissions expire
after a short period of time so as
somebody who is you know working to
resolve your support cases on the
engineering side I only have access to
the things that I need for the least
amount of time that I would need them uh
and so obviously you can see that we've
made a lot of effort to protect customer
data and to protect their data rights
but it is kind of Microsoft granting
itself permissions right obviously you
can trust those but again in some of
these sensitive Industries you might
need a little bit more control over this
and so now we are offering lockbox uh
lockbox is essentially putting you the
customer in the approval chain right so
when a Microsoft employee requests
access to data protected by lockbox then
the customer is notified about the
request and then the customer can either
approve or deny the request uh so if the
customer is on board it's lock box then
they have the control over their data
and you can assure them that we are
taken their privacy
seriously so how do we actually ensure
compliance with this right we can't
expect everybody particularly everybody
in this room but everybody in Microsoft
to be a privacy and security expert and
Microsoft itself has over 200,000
employees and some of those people are
project managers who often have
fantastic ideas but they often C
conflict with the privacy and security
right so we have an internal review
process within Microsoft of several
States stages so uh when work begins you
need to do a preliminary risk assessment
which identifies risk with the planned
feature and this revie process is the
same for both privacy and security when
the feature is completed we need to do a
thorough review of the actual
implementation because what you actually
build is often different from what you
intended to build in the first place now
that we have the AI Revolution there's a
lot of specific AI requirements that
need to be fulfilled as well and then
once a year we'll do a detailed review
of the whole service and every component
that is involved so that we can provide
evidence to external Auditors who are
going to audit us for for example to
Grant compliance certifications or in
response to security incidents and so I
just want to talk about these three
steps today because these are steps that
are relevant to you when you're also
doing engineering work these are things
that you can apply at your own uh
companies so the preliminary assessment
it should just be a quick meeting to
identify risk with the feature right so
as the Privacy usually the engineer
working on the feature would come to me
and present what they're going to do
and you know explain to me how the
feature works and then I will ask how is
your personal data being handled right
are you sending personal data to uh
other services this sort of thing what
types of data are you handling and also
a security view you ask what are the
potential threats with this feature
right you know are you making
authenticated requests with the user
password or tokens this sort of thing
and so the outcome of this meeting is
one of three things either great you're
good to go it looks like this feature is
going to respect uh privacy and security
guidelines
or maybe wait this feature needs a
little bit more consideration right just
make some small changes here and there
maybe we'll cut this part or stop this
feature is a in complete violation of
security and privacy guidelines and this
doesn't necessarily mean that the
feature is a bad idea right Augustine is
going to talk about this a little bit
later on but often when you're dealing
with privacy in security you need to
make a trade-off between usability of
your feature and convenience for the
engineer and the customer versus privacy
and security and you should always lean
on the side of privacy and security but
obviously that means some ideas that we
have we need to turn them down because
we respect your rights and so the next
step is the feature review for security
so I'll hand it back to Augustine to
walk through how this works yeah so as
eron was saying this is kind of very
similar between both sides so normally
what we try to do is we try to do a
thorough review of the initial design uh
um of the Implement first we discuss and
then as the code is created start to be
created we we asked for people is to
okay bring a threat model which is just
basically a fancy way of like putting
those threats in a way that it's easy to
identify um risks and then we sit down
together we identify which ones are
higher priority higher risk we make a
list of a mitigation plan it's like you
cannot there's no way we can ship with
these things so let's go and mitigate
them and finally when the code is ready
we will go and verify that everything is
is fine at at this stage right this is
kind of what it looks like like a thread
model doesn't have to be this fancy um
but you can see here's things in here
like H Storage and keyboards and SQL
data warehouses so this is the way that
we will look at because I have no idea
what this feature may be because I'm not
working directly on it the domain expert
is the one that is coding this they will
create this View and then we will see
together and kind of like okay what is
happening in here and we will end up
with something like this which is a list
of you know potential risks right and
you can see that some of them are high
severity it could be elevation of
privilege it could be a medium severity
like repudiation uh risks or even denial
of service and we will pick up this list
and say okay let's let's mitigate this
this way mitigate this one this way and
uh keep them in mind before we move
forward yes so we also have the review
for privacy so I'll talk about it from
my perspective so generally what I will
ask for is for somebody to produce a
data flow diagram right so now that
they've implemented the system they
should capture all of the services and
the data that is Flowing between them
just to visualize to me and serve as an
explanation for me as to what they're
doing and how it works right um they
also need to create a data inventory
documenting every data element and how
it is handled I'll come to that in a
minute and finally using this evidence I
will verify whether they have met
Microsoft's compliance
guidelines and so if the review
identifies an issue that doesn't mean
you need to cut the feature or stop or
that you've wasted your time right
usually it just creates some action
items for example don't send this piece
of data maybe you need to redirect this
request to a service that's in the EU
this sort of thing right and so here is
an example data flow diagram this is one
that somebody drew and presented to me
with the sensitive parts removed and so
uh you can see that I've mapped out all
the services and the boundaries of those
services so whether that's Geographic
boundaries or boundaries between
products um and captured all the data
that's flow in between and you can
capture the the actual specific data or
just the types like customer data uh
user identifiable information this sort
of thing and then we will produce the
data inventory so Microsoft needs to
have evidence for all these external
Auditors to gain these compliance
certifications and so we very thoroughly
document all of the data that is handled
and exactly how it is handled so first
we will list out all of the types of
data that are handled like your address
ID name Etc and then we'll capture a
sample of that because it's not always
obvious from the name what is involved
right if it's like a user object does it
contain their name or just a ID this
sort of thing and then based on that we
can classify the data elements so we can
say you know customer address that's
obviously personal data the correlation
ID that we use to uh correlate elemetry
between Services that's just Microsoft's
own system data and then we'll capture
all of the compliance related
information so which services are
storing this which Services handle it
are those services in the EU lots of
other things about third parties and
finally we will determine for each data
element is it handled in a compliant way
and so we're not actually suggesting
that you go that deep into it right this
is obviously a very intense timec
consuming process we need to do this
because we deal with a lot of external
organizations that have no understanding
of how business Central works but they
need to audit us and grant us
certifications but for you guys the aim
is just to think about privacy and
security right so here is a data flow
diagram that I drew yesterday for an
example where you just communicating
with an API right so you can see that
you authorize with the Au token and you
pass the object's idea of the thing that
you want to retrieve and then it returns
back data that is owned by the customer
right and this is enough and I came back
and just wrote down a couple of things
like think about the key Bol and hey
what happens with uh with these external
Services how do they authorize right
it's it's not necessary to go into this
big massive processes the act of
thinking about these things already is a
massive win yeah the intention is to
stimulate a discussion about this right
and often the feedback that you would
get on something like this is is well
you know like let's say that your
service is in the EU but the API is in
the US well the Au tokens often contain
personal data right it's just bics
encoded uh personal data like your name
and your email address and things like
that and so actually you shouldn't
really be sending those you should be
doing like service to service off on
behalf of the user and so my suggestion
would be can you switch to service to
service can we use managed identities
for this can you not send that piece of
data
please and then finally we have the AI
feature review right so Microsoft has uh
come up with what we call the
responsible AI guidelines responsible AI
principles and so I'm just going to walk
through quickly each of them so there's
accountability so this is putting the
user in control of the decisions made by
the AI right we don't want the AI to go
Rogue and start creating new sales
invoices and billing your customers we
want to make sure that you know what
co-pilot is doing and uh we need to make
sure that you're the final you know gate
of approval before the AI takes some
kind of action then transparency so
often the AI will come back the response
and maybe you're thinking well how did
it come up with this answer well it
needs to be explainable and we even need
to disclose that AI was used to generate
this answer in the first place right uh
then there's reliability and safety so
making sure that the feature serves a
genuine purpose not just using AI
because it's fun we're using it because
we want to make people's lives easier
but also making sure that the output of
the feature is consistent so if you give
the same request multiple times it
should come up with a predictable output
and monitoring and uh taking feedback on
to make sure that we address issues that
arise then there's fairness we want to
make sure that it's not biased we're not
uh you know making the AI based on uh
like
stereotypes inclusiveness so now that
we've built all of these fantastic AI
features it'd be a real shame if only a
certain portion of the population could
use them right so we need to make sure
that they're accessible that everybody
is able to take advantage of these
features and finally we come full circle
to privacy and security because now
we're you know passing your data to the
model we're using your data to uh you
know generate insights with co-pilot
right so we need to make sure that we
take your privacy and security extremely
seriously uh so here is an example of
some of the UI from a co-pilot feature
that we just released and um you can see
that like we've shown you all of the
information about how this response was
generated you have the option to edit
this information and then you have final
approval and if you don't like what
you're seeing you can always give us
feedback and this is baked into every
feature that we've built so here are
some example responses from co-pilot
chat where we've applied these same
principles and it's not only in the UI
it's also when you're doing the prompt
engineering and you're architect and
your service on the back end and in the
next talk in the same room we're going
to talk more about that about prompt
engineering right so there's going to be
a lot of co-pilot talks throughout the
day we're going to go into detail about
the chat in a session this afternoon as
well and so if you want to learn more
about responsible AI then uh stick
around attend the co-pilot sessions and
and we'll tell you all about how to
apply this in your own uh in your own
product yeah awesome so we talk about
inventory we talk about sec the
fundamental some of them there's many
more uh but some of the ones that we can
look into um after this talk the last
thing is actually thinking about the
customers perspective and how what they
may know about security or not know
about security but also think about the
attackers how do they actually get in
right so some examples of that it may be
secure by default this is something that
has been you know talked quite a bit in
the last period and it's about trying to
make always and this is a definition
from the cyber security center from the
UK try to make everything always as
secure as it can be all the time without
knowing it don't make people pay for the
stuff make people go into settings to
set it up more secure just make it
secure
first it doesn't always happen if you
have an iPhone in your pocket and you
slide from the top right corner you can
open the command center and go into
airplane mode without a pen so if
someone takes your phone you can just
set it up so it cannot talk to the
internet it cannot be located it cannot
be anything because it will go into
airplane mode unless you go and change
the settings so that is not secure by
default so if you have to choose between
security and usability what do you think
what do we go
for yeah security with with a small
asterisk right so obviously don't fix
something that is extremely low priority
and and crash the usability of your
application right it has to work it has
to be used
but consider that trade-off
always um one more thing that uh just I
will walk very quickly when we're
thinking about like fishing think about
fishing as well um in a slightly
different way that we used to we used to
we are trying to look at those weird
emails with like long wrong text maybe
wrong URLs and weird names that still
happen but it's not the only thing right
especially now with AI expect that those
emails will become much more realistic
all the time trust your gut think about
what you're getting and there is I don't
know if you heard about spear fishing uh
but that's where you know now with the
all the data that we have in the
internet with AI someone can go and
figure out that maybe you took a
vacation in the Hilton Hotel because you
put it in Instagram and the next thing
you get is an email that says hey I'm
from the hotel and you forgot your
laptop and your iPad please click this
link to recover it do you think number
one is a ficient attempt can you this if
you think
so what about number two is number two
fishing
attempt yeah it is as well this is a
fake link right it's just an URL mask
right it's exactly the same URL on the
top that says Anonymous fo but just with
like um a URL beautification on Top This
is a spoof email which is not very
difficult to get an email spoof so if
you have a good email provider it will
probably tell you something like this
but just exercise caution always it's
not that easy just try not to click into
things it can happen to people it
happened to even security researchers um
but it's um is definitely a tricky one
try to ensure that you have the right
culture to avoid that lastly offensive
security we have a red team in Microsoft
which are basically hackers that work
for us and they think as real attackers
right so they come and try to break into
things so we can go and fix them but try
to do the same yourself you don't have
to be you know top Elite hacker just to
increase the security of everything you
build like tenfold just by thinking how
you will get inside get things like a
scanning websites scan your open ports
if you're living open ports all over the
place be sure that you know about that
and if you have money or you have power
decision or you can influence your
bosses pay for a pen test if you can
that's that's a cool very good way to
also get humbled very
quickly um cool so that's uh all of
those things that we discussed before so
just to wrap up I guess yeah so uh we
thrown a lot of information at you today
and I just want to focus on the things
we expect you to take away from this
conversation right and mostly we just
want you to start thinking about privacy
and Security in your own organizations
and so Augustine's favorite point is
create and keep an upto-date inventory
of your assets because you can't protect
the things that you don't know that you
have and once you've done this then you
should think about appointing subject
matter experts right so you will have
people in your organization who are
passionate about privacy and security
and put those people in charge have
those people create internal guidance
and training materials for the rest of
the organization and then for every
feature that you have conduct a privacy
review right just have a quick
conversation about the feature what it
is how it works what the potential
threats are and then when it's done come
back and draw a data flow diag and think
about what you're actually implemented
right think about the data that is being
handled and the threats that are
possible and how you've mitigated those
risks and finally once you've had that
conversation actually act on the outcome
right it's one thing to sit down and
have this conversation but then you need
to go and do the work so finally I was
going to say that we needed at least one
AI generated picture in the presentation
that was the previous one so they have
to guess which one it
is um so the last thing is to use AI
responsibly right so I know that a lot
of you are going to be starting to work
on AI features you're going to want to
use the co-pilot toolkit to build your
own AI integration as business Central
so please go and read the responsible AI
guidance and make sure that you're
handling people's data with AI with
respect attend today's sessions about
how to uh how we built business Central
co-pilot where we're going to show you
how to apply these principles in
practice and then go back to your job
and apply the principles
yourselves so that was everything that
we have to talk about uh I think we have
five minutes for questions so there is
also a ton of like extra uh material on
the deck so if you pick it up there is a
ADV of other of those security
fundamentals you can look into and we'll
also be around so if you find us in the
in the Microsoft area just come and ask
questions as well we have time for one
question or two so if anyone wants to
ask something and if you ask a question
then uh you get a free t-shirt so oh
yeah anyone no yes just stick your hand
up really high if you want because the
it's kind of bright up there
no cool maybe we confused everyone a
little bit too a lot to take in awesome
then uh yeah it was a pleasure just uh
find us around if you have any questions
and yeah thank you yeah thanks
