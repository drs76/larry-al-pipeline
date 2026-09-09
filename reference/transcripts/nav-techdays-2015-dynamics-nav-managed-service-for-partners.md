# NAV TechDays 2015: Dynamics NAV managed service for partners

- **Source:** https://www.youtube.com/watch?v=K_eaQguYUxE
- **Video ID:** K_eaQguYUxE
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 84m28s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

hello everyone welcome to our session
first thing first let me introduce
myself my name is Ida I am actually
enough partner like many of you here I'm
a solution architect for a very famous
fashion company called fabrica and I
think many of you know that amazing
company my team recently has been
working on to build a repeatable
solution for fashion companies of
solution is multi-tenant and we are
planning to sell it in volume as a SAS
offering I was in direction in October
and first time naf 2016 but announced
with the announcement of naphtha 2016
nav managed service it was also lunch it
was presented as platform as a service
offering for partners with such
solutions it was exactly like my
solution of course I was very interested
I went to the workshop and I really
liked what I see but you know I didn't
get a chance to have a deep drive so I
meet this guy Christian he is actually
from Microsoft and from the team that
has busy service and then he promised me
that he can have a session with me and
make me to understand the functionality
of manage save is much better and also
to understand what how it has been built
in the back end so let me let me walk
you through my experience
fantastic so a Christian I'm going to
actually go to the experience and then
please help me if I miss any Esther of
course so I am logged in to naff
management portal this is a self-service
portal for managing the service and also
for deploying my solution in the club to
deploy my solution in the cloth you
might think I need few components the
first thing I need is a platform so let
me go to the platform section I can see
there is a list of platform here that
microsoft released every month as
cumulative updates and they make it
available in the portal for me to pick
up and use it for deploying my solution
so what would be the next step the next
step I need to kind of define my
application for the service and also
upload it to the club so let me go to
the application section as i told you i
have to flavor of my fashion solution
fabric and fashion accessories and
fabric and fashion upper i have already
defined this above the application in
the service and give it some basic
settings so let me go to one of those to
see what are those settings I have given
get a name fabric and fashion upper a
short description I have also defined my
branding elements so I have given it a
display nning this display name is what
my customers see when they log into my
solution i have also uploaded the images
with my logo then it can be used for
plug-in imagine for a splash screen
images therefore you know I can kind of
present my solution with my brand
I have also defined the links to the
legal content and the privacy content
that i have i have also give some links
to the feedback page and the community
page and login page so my customers can
stay in touch with me when they're
interacting with my solution some more
things of course I need to upload my
license here that I have done also I
would like to run my solution with
office 365 authentication therefore I I
could actually go and simply click on
register for office 365 authentication
here and my solution was registered for
office 365 fantastic so you can see I
have all the basic elements here to
define my application so let's see what
was the next step now I need to upload
my application to the clock for that I
need to add an application version so
let's go and see what does that really
mean so now i am creating an application
version i need to give it a small name
some name i use some of the coatings
that normally are useful versioning my
application i can define some
description but here actually it comes
all the way all the components that is
my application so i need to upload my
business logic that is my fashion
solution that i want to sell it as a SAS
offering i need to also upload my tenant
data this is a template that contains
the initial data for my customer to get
you started and if I have some custom
health content I need to upload that
advertise with so actually let's think
about this all I need is the soft that
is the components that is my
intellectual property and I upload them
right here so if I want to upload them
now
oh let me see I was just thinking all
these components actually there's
nothing new about this how these are the
components that I'm pram I was also knew
how to beat them and I was creating them
and making my solution V but there was a
slight difference if i remember
correctly so let me demonstrate for you
so when I want to upload these
components the service actually works
with them in a little bit different way
it treats if it works with them as a
backpack format the bedrock format is a
standard as your equal format that is
actually also supported with other
sequel tools on premise ville and it was
really really easy to create basically
all I needed to do is to go to my sequel
management data and management alpha do
and then upload my database as a
backpack formats basically two clicks
that was the only difference but i'm not
going to upload them now because it will
take a while so i have already uploaded
my application version let's go and look
at them and you can see here every time
actually i'm going to you know extend my
application with some new features and
with some hot fixes then i can create a
version and upload it to the portal so
basically i am actually using as portal
for managing the whole life cycle of my
application i can just piss me a stuff
uploaded to the portal and then i can
choose when I want to pick them up and
add some what point of time I want to
push it to my customers so christian i
have uploaded everything now to the
cloth and basically I have my components
up there but you know where we say
upload is soft
into the cloud what does that really
mean yes let me explain you but first
let me say you did everything exactly
right but i would like to show what
actually happens on the back end when
you did the things you did so you are on
this page and you selected two of your
most important assets you are
application database in an in a backpack
format and attendant template database
also in a backpack format and then you
click upload but what was it uploaded to
well in the company i work for which is
microsoft we use asia for our services
and any remaining service for partners
also lives in asia and when i say listen
as your eyes I mean it is entirely in
Asia so to have a place for your files
we create a storage account just for you
and so when you click the upload we
simply transferred the files to that
storage account and store them there as
flops so you can think of this as a file
share basically that we maintain for
your files in the cloud you can access
it but you can use it via the portal
when they've been uploaded you can also
download them again in case you ever
want to bring them back to your
developer machine for anything I hope
this make sense yeah absolutely so let
me wrap up Microsoft have the platform
uploaded the platform I uploaded my
application version which was my tenant
database and my tenant template and
basically now I have all the components
required for me to deploy my solution to
the club right so to do that I need to
create an application service so let me
go to the application services list and
spin up and your application service
here I need to choose which which
application I want actually to deploy to
the club I want to choose fashion
apparel for now one of my flavors and
now I am presented with the versions
that i have uploaded
so I'm going to choose their initial
version and then I end up in the
application service page basically here
I have all the elements for configuring
my service but if you notice around here
you can see that everything is
predefined basically I just need to
define a name for my application service
let me try it to try to give it a
specific name because that is the way
that we have the naming convention in my
company great so I give it as a specific
name absurd with one and then actually I
am now ready to provision a chance as
simple as that everything ready but i
want to discuss before that some of the
more options that i have here for this
service i can select from to type
production and sandbox for i use
production services if i want to run my
production tenants and i use my sandbox
if i am using my service for
troubleshooting and for testing I can
also choose from which as your location
I want to deploy my solution to actually
I have a list of other locations
available for me to choose from of
course now we are in Belgium so I'm
going to choose rescue that probably
makes sense and then I can also define
different type of authentication I can
choose between user name and password
authentication or office 365
authentication in the next tab I can be
fine how I want to scale my service do I
want to have a large scale service or a
smaller scale series I can also define
my custom domain then I can have a
good-looking tenant URLs for my
customer with my domain in it I also
need that I also can you know upload my
own certificate and that is what is
really recommended by Microsoft when we
are deploying the production tenant then
it is completely secure the connection
that I have between my customers talent
and nav but of course I can leave this
checkbox here if I want to if I want to
have like production or test services
then the service will generate a
certificate for me and the last not
least I can also choose if I want to
enable web services on this service just
by simply clicking enable web services
so now that I have configured my
application service all I need to do is
kick off the provision and of course it
asked me we want to provision a service
yes and you can see instantly Maya
status is changing to provision and I
believe Christian this is going to take
a while but i can't wait for it actually
because at the moment this is running
i'm going to login into it well almost
because what you have created is a
service you will end up with a full nav
installation but you don't have any
tenants or users yet so you won't be
able to login yet when you saw me what I
have right now I'm a big part of it
absolutely so I will return to my slides
and show you what we have so you were on
this page and specified all the details
for your service for example the name
the data center you want to deploy to
and everything else and then you click
provision so what happens on the back
end well the first thing we do is we
create a database server and SS sequel
database server since you chose West
Europe that's where we will create the
database server this takes only a few
seconds
and after that we can start to create
databases so we will immediately create
two databases the first one will contain
your application database that contains
your tables and code unions and all that
and we will create it based on the
backpack file that you upload it before
the second database we will create
immediately is the tenant template
database and we will also create that
based on the backpack file you uploaded
before so now we have two databases but
nav is more than databases we also need
to install a Navy somewhere so we will
create an SUV em in the this works in
the same region namely West Europe once
we have created the BM we will install
all the well-known nav component so we
will install the nst and can configure
it to talk to the application database
we will install the web client we will
install a website that hosts click once
so your end customers can easily run the
windows client as well and finally we
will install the help server with either
either our default help content or the
help content that you can upload the
last thing we do is open some firewall
ports so your end users can actually
connect to these services so as you can
see with this we have a full nav
installation but we don't have any
tenants our users yet okay let me try to
do that switch thank you you can see I
have a beautiful application service
here running in production ready for me
to add tenants so I simply go to the
Actions menu and add a tenant of course
I should give a name to this tenant to
honor of great event I should specify a
country where my custom is okay to that
also just to make sense and basically
that is it my tenant is ready to be
provisioned as simple as that
of course you mentioned that i need to
add users so let me start to add myself
as a personal user
and of course i will add my email
great and my I make myself a partner
user oh but actually I am in the
unbolting field I really want to unboard
somebody from their audience as my first
customer let me look around to find
someone this guy I know him a little bit
I wonder how are you do want to be the
first custom on boarded on managed
service especially in the navteq days of
course you know we have many customers
already on board as Microsoft has told
us in direction okay can I have your
email let me see maybe I have your email
actually I have your card from of MVP
dinner last night I can try so you have
known objection can i add you everybody
can see your email fine good guys this
is valid okay username of course mando
will give it also a real name and a
contacting me great now I am really
really ready to provision it's an ever
you want to change the name of the
tenant you are right you know one who
puts himself here up there maybe we
should honor him no offense was
ok let's provision valdo stations and
see how it will go yes of course I want
to provision and of course now it is
taking a while to kick off the
provisioning we hope for the best it
really depends on the network great so
the status change from draft to
provision this will take not so much
actually a minute or two but then let me
go to another talent that i have and it
is already running and explain to you
some of more advanced options that i
have on the tennis coach so you can see
except from what you saw I can actually
I have this talent configured on a
application service with a custom Bama
so here I have the opportunity to define
a subdomain prefix to a specified the
you my you are lieutenant URL and as you
can see because this is already
provisioned it has picked up this
subdomain prefix and it looks quite nice
so it has my domain in it and it has the
specific name of the shop of my customer
I also have some more advanced option if
I check mark and if I enable a lower
application database rights that means I
can let my tenant to actually be able to
go and modify the application database
that can be quite useful if I want to
change the permission sets or configured
web services or something like that but
of course you can imagine that this is
not something that we advise you do if
you have a customer chance that is like
it can be a nightmare it is very good if
you have
personal talents for maintenance so you
can configure things or if there is a
permission set that you need to go and
change or do a a small bug fix then you
can enable that option there is also a
table connection name here basically if
I register if I just add a string give
it a name then I kind of register this
connection and you know what happens
these tenants will be acting as a master
tenant and other servants can connect to
it and read the data from it this is
actually leveraging one of the very
powerful features of naf 2016 external
sequel tables and I already here that we
have some of the of great partners
having some session about how to
leverage that features if you want to
know about it more just please refer to
msdn it is quite powerful so now that's
it let's come back to off tenant list
and see what happened to waldos fashion
let me refresh
I can see when those fashion is already
probably it is a steel provisioning so
we need to wait maybe few seconds more
but let me actually want this is
provisioning the network is a little
because so here until this is
provisioning I explained to you
something so what what will really
happen when I when the tenant gets
provision when it gets provision because
I select that great option that Center
welcome mail then my customers that
would be also your customers will
receive a welcome meal with the username
and password to login to the tenant and
that is the way that you are going to
onboard the partners well great so I can
see the Vandals fashion is active and I
suspect because I was a personal you
know a partner a user here i have
received a maid and wonder what about
you it did you gotta mean you gotta mail
can you log into your talent
rata de fantastic I also got a mail see
Wow can I see again before I explain is
that yeah you are also using our
beautiful tablet client action on
surface so you can see that your
customer will receive such an email then
I also have access they also can have
access to the Aviles client actually by
clicking through they click once here so
let me try this should we try sup to you
the earth we already see the you know
the tenants on guess I need to try it it
will take a wife so in a set of me login
to the tenant
so actually a Christian how long it took
it took me less than an hour to
provision my solution in the club and it
took me less than 23 minutes to
provision a tenant so while I am logging
in can you explain to me how all this
magic happened of course so yeah I have
shown what modest what we had before so
we had a BM with any be installed on it
and we had the two databases and then
I'd I specified the details for her new
tenant world of fashion and click
provision so what happens at that point
well a tenant needs a separate database
so the first thing we do is create a
copy of the tenant template database for
this new tenant this is a pure database
operation that doesn't involve a navy at
all but once we have the database we can
simply mount it on neff so now the
application database has a record of
this database and at this point the
tenant is actually fully functional the
only thing we need to do is create the
users that either requested so we do
that as well these users become regular
nav users you can also create them in
the application like you're used to and
if you do that we will synchronize them
back into the management portal because
we want to always give you a full an
accurate list of the users in the
management portal and when you're in the
management bowl you can also make
changes for example reset a password or
disable a user and it's interesting you
mentioned the external table connection
before because that's a feature we use
to enable this since we want to show the
data that lives in another database
namely the chain and database small
location inside our portal we create a
direct connection to that database and
read the user's out
then time and then show them in this
list so it's quite a powerful feature
that we have used several times and
maybe you have ideas for how to use it
too anyway what the users created you
have a fully functional tenant and users
can login fantastic actually I have I
have few concerns because so far what i
have seen was really great and i have
few questions let me start with the
first one that come into my mind and i
think many of you see the great demo on
extensions that Tomas saw in the keynote
and i have already actually use
extensions on pram so i hope in future
you are going to support extension in
the service because it is very
specifically built for the multi-tenant
solution yes but we actually already
supported in this service and you can
try for yourself just go to a tenant and
manage your extensions from there okay
let me actually try it
let me to let me go to one of my talents
I think this one was that I uploaded my
database I had some extension so yes
that's right I have a manage extensions
teacher let me see wow that is very easy
basically I easily can install an
extension on my tenants great you know I
have few other concepts to be honest and
one of my concerns is you know it's all
this stuff is running on the cloud right
so what about my data is my data really
safe your data is very safe and we have
an automatic backup system that takes
care of all of this and actually you can
even go back in time let's say you want
the data as it was when the conference
started this morning you can do that
just go to your tenant and click the
point in time restore button I can't
believe you well it's true it's almost
like a time machine this course is
really like a time machine okay let me
try let me go to where should I go
actually I should go to point in time
restore here great and let me see if I
can figure this out wow I have a fully
fledged calendar here so I can just get
back in time they can I get back to last
year left techniques well it's not
really a time machine right so you can
only go back to when your channel was
created and you can't go back more than
14 days okay but if they you know it's
quite impressive so actually this French
fashion shop it's my French customers
and they called me yesterday and they
told me that they have been running
their daily jobs
and one of those jobs is cool day data
and they were asking me to undo it you
know I don't have that many option here
everything is in your guy's hand so
maybe I can use this feature folder
maybe when did they run the jobs they
run their jobs I think at noon every day
at 12 that is a daily schedule so why
don't you roll your database back to
1150 okay let me try so now we are in no
wonder so I go to yesterday and I tried
11-50 even with 1130 I'm going to be
happy and then now what should I do just
play press ok here yes ok yes I would
like to get back point in time because
they are not functional anything let me
see what happens here ok the status
changed from active to provisioning so
it is provisioning based on the data
from that's right as long live in 50
yesterday but I can explain you how it
works on the back end ok let's go ahead
so it is actually a sequel that is
making this possible for us so you
wanted the data as it was at eleven
fifty yesterday for your tenant database
in this case apparels your fall so how
can SOC will give that to you but to
answer that question we need to take a
closer look at as a sequence automatic
backup system so SS equal actually takes
frequent backups of your databases so it
keeps them storage that you can see but
it keeps that storage for your database
backups so it takes different kinds of
backups it takes a full backup every
week it takes incremental backups two
times every day and then it takes
backups of all your transaction logs so
you can see with this information SS
equal actually has all the information
required
to recreate your data at any point in
time so you wanted the data as it was at
eleven fifty yesterday so what s a
sequel would do in that case is find the
most recent full backup before that time
find the most recent incremental backup
before the time and apply that on top
and then find all the transactions from
that time until 11 50 and then replay
those transactions and the end result is
you have an exact copy of your database
as it was at that time I think that's a
pretty amazing feature and you know what
the best part is SS equal dust it for
you automatically you don't even have to
enable it and it's free so how do we use
this cool as your feet as a sequel
feature in the nav menu service what we
basically just add a little bit of user
friendliness on top of it so we created
this little page you specified a time we
tell s a sequel please create a database
for me from that time which it does
based on the backups then I dismount the
old database and mount the new one and
now you have it you have a tenant that
is running on that old data great but
actually something grabbed my attention
you said you specified the time i was
lucky with my French person because they
are running these jobs every day add to
it but what if they didn't know they'd
mean that something is screwed up
yesterday but they didn't know exactly
at what point of time right in that case
you may have noticed that next to the
point in time restore button there was a
point in time copy button and the
difference is that the point in time
copy creates a database just like we do
illustrated but it doesn't delete the
old database instead it creates a new
tenant with that new database so you
actually end up with two tenants and
then you can log in through your second
tenant and explore whether the data is
okay okay that sounds right so I can get
back to
different point halftime create these
copies of my databases and then try to
see if the job is started at that time
and based on that is specified what was
the time and then do a full point in
time restore to that time and get my
tenants back online roger that makes
sense but you know I still have some
concerns because I really love about all
these agile sequel outages it kind of
freaks me out what about that what
should I do about that like how we can
address that concern yes so there are
different types of outages it can be a
single database server that goes down I
can be an entire service in this case as
a sequel that goes down or it can be a
whole data center that goes down right
but don't worry in all these cases we
have you covered and let me explain how
we do that so as before we have SS
sequel server and a database and we have
the backups that are stored in storage
so what we didn't talk about was that
this is placed in West Europe which is
in Amsterdam and let's imagine the worst
case scenario now a natural disaster
wipes out amsterdam and the data center
and there's no way we will get our data
back from there so what acer has is the
concept of mirror regions so west europe
has a mirror region which is north
Europe and vice versa so these two data
centers help each other create
robustness against any regional outage
so what license equal does is they it
takes those backups that you created
that we talked about and it copies them
to the other region it does this
continuously so typically covers them or
it has covered them within 10 minutes of
a change right so now you can see how it
works basically we're taking backups of
your back rubs in a different region and
since this is doing that on the on the
fire it's not instant it can take up to
one hour or load is typically really
fast you can take up to one hour
up before it has copied it and then you
know it also if the worst case scenario
happens you risk losing up to one hour
of data which i think is a fair
guarantee because it is an extreme
situation and as with the other side all
of this is completely automatic by SS
equal and it's free okay this is
actually pretty much amazing stuff that
we are talking about but you know what I
don't call myself a dinosaur like one of
our great MVPs calls himself I'm sorry
mark but you know I really like to run
my business on the cloud but I'm a
little bits all the school Christian
like you know my data my customer data
on the cloud I really want to get hold
of them to be able to control them we
have an option for you as well as a
dinosaur but it's not a feature for
dinosaurs only it's actually quite a
useful feature it allows you to download
your data at any time you like but you
can try it out go through your tenant
and click the tenant data files I really
would like to do that oh good because i
had a network issue that i couldn't
connect to the service great i think we
can connect now it's very slow that was
also prevented me to be able to log into
my tenant but then i used one of the
very great features of management portal
which i show you and then we can go
through that experience as well I think
we have a drop in connection so it's a
little bit slow I'm looking forward to
see your dinosaur option
you couldn't even open a search engine
before interesting you know Christian
that's why I like to have hold of my
data okay let me try to reason and I
give it another try I log into the pores
on with a beautiful office 365 single
sign-on future it is actually good
compelling what we experience this
morning we thought we can't run the
whole person who the whole session so
hopefully we can log in and Presley
I wanted to demonstrate to you but maybe
I'm not sure maybe I can show that until
we are logging into the portal so
basically I had a problem connecting to
their tenants and then I was trying to
copy the password that is produced for
me and probably it was not right so I
went to my penance card and reset my
password one of the nice features that
it's also very good to have and then
define the user friendly passport not a
generated password it seems that we are
logged in but let me go through this
experience so my user may and you can
see that i'm in the value of fashion
tenant that I just provision and my
password let me type it just to be sure
and you can see actually there splash
screen then I uploaded is showing off
and also the title of web clients is
showing my gran D fabric am fashion
apparel name and then this is my talent
you know running on the cloud provisions
in two minutes just we should ignore the
network connections in navteq page ok
let me get back to the portal closes
trying to connect again
so what should I do now maybe maybe we
can proceed with some of the other
concept in the poor that until network
is back online
you can use none of us are ya should we
run it from mine yeah why not let's try
from you you have a bit better adaptive
optic good so we were talking about the
manual bag of the ability to check your
data with you at in time and you had
that option on the tenant page and we
call it sin and data files let's back up
at least Waldo there is the value
segment ok i go to my tenants car
and what should I do now I can see I
have it I have an option here 10 and
beta fives and then I can go here and
sing simply click on the back up yes I
want to make a backup of the system
let's see what is happened so my backups
are getting created great so if this
will take a while right Roger let me get
back to another tenant that there is
already some backups to see how the end
results will look like
right I have some backups here so you
can see that the backups have been
created at different points in time and
then after the backup is created then I
have a download option so i can download
my backup on pram and fetch my data that
is quite cool by the way can i upload
this data files by clicking yes you can
and you can also check once you have
uploaded it you can restore your chin
and based on the data you upload it okay
let me try so can I get back to two days
from now maybe to the 17 and select this
and just say real soon and let me see
what is happening it well my talents
were running and it is already changed
to provisioning so actually this is my
version of time machine well it's much
more reliable because I am actually
provisioning dis cyan't get a data file
that I take the back of off from two
days ago I think that we should give up
on the connection on my side
great
alright what's next alright so we talked
about we demonstrated how you can
download the data file and you can also
upload ready again and then start
running on that and that is actually
quite useful in many scenarios for
example imagine you have a customer
already on primp and you want to break
them into the cloud well you can take
the data and and bring it into the cloud
like this another scenario is you want
to download your data and do some
advanced troubleshooting rounded for
exam will fix some data corruption and
then upload it again once it's fixed and
finally in case you don't like our
service after a while this allows you to
easily take your data with you and find
somebody else to operate it so it's
quite a useful feature okay we took a
pass because of the you know the network
problems we had but I want to say too hi
again Christian hello Ida I can't
believe it's already been a month it's
good to see you again I had a very
exciting one month i have actually on
board with hundreds of customers and
everything was going very very fine
until yesterday they start calling me
and telling me that the service is
really really a slow and you know I
first kind of helpless what can I do in
this case well you can actually go to
the service and see for yourself how
it's doing if you go to this service let
me go to the end to the service and see
we call it service utilization great let
me go to my service and look at service
utilization
it probably did take away that's at
least as far as it is responsive we are
happy very interesting information is
communicated to you now it will take
longer than usual we got it already so
what I'm going to see its various
utilization by the way now that like I'm
just waiting for it so we collect
performance data from all our VMs all
the time and that allows us to show
graphs that you will be able to see so
with those waves you can see how your
service is doing right now whether it's
running hard or not and you can see how
it's been doing over time for example
what is the rhythm in your load when do
you have peak loads do you need to to
add more capacity it has never take
longer than this usual amazing you think
we are disconnected totally or there's
some hope you
so actually let's proceed at least you
can address my problem Oh fantastic
finally great so let me see what I have
so actually my customers were not magic
oh I can see here they said the problem
is started yesterday right so let me get
back to into for others and actually
they were right my service was quite
loaded by that time great these are
great options at that i have and i can
see that I can you know get back in one
over the groove 24 hours up to seven
days and I can see the CPU and memory
and all that great information is nice
because now I know my customers are not
nagging and there is a real problem but
what can I do about it well it looks
like you need to add some more capacity
to your service you can do that on the
service car okay let me do that so right
now how many escaped units I'm running
on I'm running on to a scheduling
probably I need to add one more right so
I can go to the escape action and set
the target to 33 it is pretty fine it's
always add 10 by the way I can see
something here also a scale what is all
that about well let me get back to the
auto scaling feature in a little bit but
I would like to first explain what
scaling actually means do you want to
start it let me start
yes I really want to a scale up they are
really calling me and then I can see
that they're scaling estate has been
changed to a scaling to treat right so
let me explain on this will take a while
yes all right let me explain what
happens on the back end now so here's
the picture from before we have an SUV
em with any be installed on it but now
we have a hundred ten and databases and
this is too much for this VM so we need
to add more capacity and now I need to
explain extend the picture a little bit
because the SUV em lives inside and
Azure cloud service and when your users
connect to the service they actually hit
a load balancer that comes as part of
the clouds and the load balancer
forwards the request to the vm and with
this information you can probably guess
how we scale yeah so actually this is a
quite amazing feature because i don't
want they call me and inform me that
something is going wrong you know or the
services s low I don't want also to sit
down there and always look at my that
nice graphs they are nice but I have you
know much more urgent business to taking
care of so sure I think that's quite
interesting soon your service will have
three in this case I have Illustrated to
two VMs and the load balancer in front
distributes the load between these two
and we can add as many as as we want and
what an interesting observation here is
actually that the VMS are one hundred
percent identical and this is essential
because it allows us to add BMS and
remove VMs pretty easily and then back
to your question about also killing how
does actually work so the auto scaling
does this force if you enable it so it
detects that we need to add more beams
and does it and when we need to remove
the end and if you recall the
performance data we gather for the BMS
that we use to show the nice graphs
is what is used by the autoscaler as
well so basically there's an algorithm
that says if the CPU or memory is above
a certain limit then add a vm and vice
versa if it drops below a certain value
then remove a vm and the end result is
you will always have the right capacity
you will not be called by your customers
because there's too little capacity and
you will not pay for capacity that you
don't need great so let's get back to
management person because I have some
other things as well so during the last
month I receive a lot of feedback I
extend my solution I add some hot fixes
and the features i have added is there a
little bit tricky so I don't want to
actually roll out these features to all
my customers I would not just send it to
selected few for example I love while
due to provide feedback see normally has
a lot of constructive feedback he should
promise me to don't blog about them just
yet so for that maybe we go to the
management also just working no it's not
working it's extremely ok what I have
already done let's go to the list of
application services what I have already
done I have provision in new service I
have a hug at first I have created a new
version of my application upload it as a
version as you see and then I have
provision in new series the feedback
service based on this new application
and you can see that my original
application the version number was C 1
and this is now see you too so what I
want to do I want to go to my original
the list of tenants of my original
application service let me go to the
list of tenants
and then make a copy I need to make a
copy because I don't want to disrupt
anything I want to make a copy of one of
my tenants and I will do that so i have
already make a copy and i use this great
copy feature ok and I'm to select the
active talent and then click on copy
when I'm doing that I create a copy of
vandals tenant yes I would like to copy
this if you take a while until it kicks
it up and then the copy will be created
and all I want to do here is I want to
move this copy yes we hit this again
fine I want to move this copy to the
feedback series and actually I have this
feature I have the move feature here in
the management portal that I can move it
from one service my tenants from one
service to other and i have used it
quite a while but i was just thinking
when I'm moving your stuff they also
perform upgrade yes you do do you want
me to explain yes you better explain
because we are not going anywhere with
this network so what we didn't get to
but was this page where you can take a
tenant and move it from one service to
another and the other service is
typically running a newer version of
your application maybe it has bug fixes
maybe has other features so to
illustrate what happens on the back end
I've shown this so we have one
application service I've abstracted it a
little bit away but you know it contains
Williams and it is running application
one your old application and that one
has the Waldo fashion tenant attached so
what you have to do is then create a
second epic
service running your new application and
this application can have your upgrade
logic as well when you then move a
tenant from one service to another we do
the following first we dismount the
tenant from the old service then we
create a copy of the database and then
we mount it on the new service now we
need to do a few things we need to run
schema sync your upgrade logic and
company initialization which we then do
and once we've done that your service is
your tenant is fully functioning again
on the new service and they're your
users will probably not even have
noticed this little downtime because it
takes a couple of minutes maybe two
minutes and the URLs they have to
connect to the web line stay unchanged
great but you were mentioning about
moving you know I think me and all the
people in this room we have a lot of
experience with upgrade and we don't
like it as much so what if something
goes wrong during the upgrade process
yes so you saw we started by creating a
copy of the database and we do that
exactly so we will always be able to
return to the original so if anything
goes wrong for example a code unit that
feels we will simply restore we will
simply go back to the old database and
mount it on the old service and then
it's like nothing ever changed so
basically in the beginning you are
actually moving a copy and if it is
going fine then it is going fine if it
is not then you want back the origin
database that's quite a smart I feel
very safe about that great let's get
back to the service and see if we have
any chance to show some of these
beautiful features to the audience no no
chance maybe we can insert a new session
we were actually using a phone hottest
spot it was not very good experience
this morning but it was definitely
better than this
shall we try the hot as possible
honestly we were fine with it so a
message to look if you want clutter
stuff to be demonstrative we really need
a nice network just a normal nice new
fully fledged
want proof to you we can run miles
reported from the hottest but that's
good keyless right now yes this is the
power of that's great not read I was too
fast excited sorry
maybe we jump to web services can you
guys help us we can jump to the hip with
exactly so that's fine so we've shown
you a lot of things and everything you
can do in a mansion pole when it works
you can actually also do via web service
and this allows you to automate all of
the things and I would like to
demonstrate how it works so I have
prepared a little script in PowerShell
but as you know any language can connect
to web services i'm just using
powershell here because it's nice and
simple and i'm connecting to my mansion
porn first i'll create a set of
credentials so i can actually get into
the mansion board then i will create the
web service proxies for some of the tent
if for some of the web services so you
can see that the domain name here it is
pointing to the real Mensch important
and we we would like to connect to the
application service web services
application tenant application data file
so let me create those three proxies
so when we have created the proxies the
proxies are simply some helper objects
that live in PowerShell now that makes
it really easy to talk to okay it's also
not working the connection is nothing do
you want to try this
give me time on time
good so now I've created these helper
objects pointing to the web services of
the management portal so let's see if we
can see how many'd services we have with
this these few lines so we have these
services which you might recognize from
the fall and I won't push my log on the
tenants but let's get our favorite
tenant which was called Waldo fashion
and so I'm creating a little filter here
and say I want all this all the tenants
that have that name which is only one
yep it found it let's look at what data
files we have for this tenant so you see
we have one database file which was
created like 20 minutes ago and still
being created let's create a new one and
it returns an operation that I can then
use to query for the status of the
operation whether it's finished or not
but let's list what Channel Five's we
now have and you see we have now too so
basically you get the idea you can also
made all of the things that you can do
in the portal with web services and we
use that in my at Microsoft for things
like automated tests but I'm sure there
are many other usages of that yeah I am
just thinking about the first script I'm
going to write it would be I'm going to
create a script that creates and
downloads all the tenant data files
great so there's also some other
capabilities of my service can be tried
one more time push our luck and if you
don't then we now I learn to don't get
excited
let's get that part you talk about it
yeah we can talk about this because I
was also wondering you know what would
be my troubleshooting experience in the
club how much because you get away a lot
of abstractive a lot of a stuff from us
yes so you can actually troubleshoot
much in the same way as you normally do
for example you can connect a debugger
to a tenant and actually that was a very
simple experience I simply go to my
tenant card you can imagine now and I
have a debug button and then it has also
some great options for example i can
download my customer user configuration
of my windows client that locally
installed on my machine on the flight so
like my meal in client is connecting to
the right channel and then i can see the
list of sessions and as a result i log
into the debugger and then i can debug
exactly the same way i used to do yes
and somehow some of the other things you
can do is run object so you can run in
table and see all the fields and make
simple fixes to your data and you can
look at how much load you have on your
databases basically get a nice graph of
the load over time of your database and
I have tried that experience as well
it's also very simple you just click on
access to the objects and then you go
through the same experience and
basically you have you need actually to
specify your tenant ID and your type of
object that you are referring to and
then you will get into it so some other
stuff so actually let me recap what has
been my experience so I develop my
solution on plan and then i upload my
components my IP my business logic my
tenant data and my custom hell
into the club and basically their use
those component tube is my service and
on board my customers so if you look at
it this is a runtime environments on the
club and actually I was thinking about
something else maybe because it is far
more than that we need to also have this
in mind that this service is hosted and
managed by Microsoft there is a fully
fledged ops team that managing the
service 24 hours and we have 24 7 up
time for the services that right that is
what I have it but I have some other
questions as well about this because I
know you guys have on boards many many
customers now there is close two hundred
customers are running live on this
service and they never experience what
we experienced today so and this should
cost something as well right and then
what about licenses so you are asking
business questions and I'm just an
engineer a technical guy at this
technical conference so I'm not the
right person to answer that but
fortunately we have a guy in the
audience which knows all about that and
it's good which you already know poverty
so but what we did cover today was two
things first of all we talked about what
the nav many service for partners can
actually do and second we talked about
how we implemented it and I'd like to
say that I de and I and the nav service
team in Copenhagen have been on an
extraordinary journey over the last year
to produce this service we are proud of
it we hope you like it too and no matter
if you think it's relevant for you or
not we hope you like this session and
maybe learn a thing or two as well thank
you
so we have a little bit of time for
questions and there are also some
t-shirts for two good questions yeah go
ahead I have some of them here so but if
all you can have up to two hundred and
fifty gigabytes inside the database so
that should be plenty for most of you I
guess sorry the question the question
was whether there is a maximum size for
the databases and the maximum size is
two hundred and fifty gigabytes that is
a limit set by HS equal let's take some
you Oh
you showed us how to upscale that speed
can also down scale it back then yeah
absolutely you can actually scale down
you can scale up and down all the time
and if you have the auto scaling feature
then that will happen food I am
wondering how you are maintaining the
URLs to the client when you switch to
where you knew you and a new version of
the application where the application is
that we should go into a new version of
the application yes we still keep the
same URLs yeah absolutely so after done
the first first thing we did was upload
our backpack files they are stored in a
central place and then I start in West
Europe or North you of anywhere because
it's just a file see I know Sims but
when we need to use them when you want
to use them in a service you say West
Europe then we cover them and create a
database in West Europe based on them
how do you add add-ons to their talents
so add-ons so we allow you to upload an
application database and a new feature
well it's not really new well it was
extended a little bit in nav 2016 is
that you can put your add-ons into the
application database so it's a simple as
that you have to package it in a zip
file put it into application database
and it comes up to the service with the
application and when they are needed
they would be unpacked on either to
serve all declined yeah okay hi that
picture creating it as a multi-tenant
environment in a third-party cloud on a
third-party data center is it basically
basically possible that you connect with
the management portal if this data
center runs the azure stack so if so
Asia has some data centers that mall is
have the same capabilities you know it's
a sequel and
computer and all that but microsoft also
releases an Asia stack that allows you
as anybody to check that code with you
and stand up your own data center and
the interfaces are the same but we don't
allow you to use those in this portal
okay because you would we have
configured it to talk to the public
cloud okay let's just hope we can you
pass this up question about the support
of the yet ends like Yahveh scripted and
also Clinton's ordeal else which are
running on the server which ones are
supported here so which one sensible so
we operate platform as a service here so
we take we have we own the vm the nav
platform and other components like that
so if there's any problem with that it's
our problem right if you upload your al
code or any atoms and there's a problem
with those it's your problem so I'm not
sure if you are probably thinking about
what is if there's any if you can rely
on there being some things on the vm
whether there can be mismatches or
anything like that yeah they are
supported you just upload them with your
application database so the javascript
Eddings let me repeat the javascript at
in controls you upload them in your
application database and they will be
streamed out to to the pipeline or the
windows line and this feature was
introduced actually 2013 and 2013 r2 and
partially in 2016 as you mentioned the
customer job that screwed up data and
stuff I wanted to know if there is
anything about gnats and configuration
of it in this portal so we simply enable
the nest for you and we run code unit
lively 450 isn't it that runs the job
queue so it's it's that's a decision
we've made and then you can you can use
the job queue as it is or you can take
over if you want but it's running
yeah so there was a load-balancing
component in the stack where I was just
wondering whether it be possible to use
that without the managed services like
you have your own idled implementation
stuff and you want to just use the load
balancer in addition to the deployment
so the load balancer is a part of the
SEO cloud service if you've ever used
them as a management pole you know you
have to create in points which are
visible from the outside right so when
you're in customers connect they hit the
endpoints which they in which they are
called but then on the endpoint you can
say that this is actually forwarding the
requests to the multiple other places
for example two different bm's so it's
part of the acer cloud service anymore
quiz
but what about the custom developed
dotnet daddy's these are separate DLLs
yes and you can sip them together and
put them into your application database
so they will be moved to the cloud
together with the rest of the database
ok and then thanks on demand of the
backpacks I like to know that you upload
it's not a question hi rip my question
is you you manage the performance of the
nav tier but how do we manage the sequel
performance problematics so we don't
give you access to the sequel database I
should probably guessed right so you are
somewhat restricted in what you can do
but to compensate for that we pop we
will show you a lot of the things inside
the mansion bottle so you can see which
we didn't get to unfortunately graphs of
the load on your system you can see how
much transaction io IP is being used how
the memory has been used and a lot of
other things there are also other
features for example missing indexes
that it will suggest to you that you add
some new indexes which we know can have
a dramatic impact on your performance
and also your sequel query statistics so
actually you can see that which one of
them are using the system the more and
then you can see there's some adjustment
that you need to do you can also
actually get access to the event log of
the database server that is running the
tenants and supervise that as we what is
your question down here
can you upload upload any database or
does it have to be certified for ms for
them in business question technically
it's any database but I don't know if we
have any requirements about
certification anymore cuz there's one
over direction you can come and ask her
afterwards with you before I could you
talk some more about the method for
setting up tenant users and
authentication options yes so those are
two different things right so because
the authentication type impacts how we
install in AV it may means you have to
set certain configuration values on the
nst and on the web plan and in case you
use office 365 education we have to
create a ad objects as well and link
them together so that's how the this
decision of authentication has an impact
when it comes to users so creation of
you I mean I can you everything where
you create a thing about how we actually
create the users or how we set choose
whether they should use one of the other
authentication toggle anything so so we
when you when in the poll you can create
the users and based on the knowledge of
you know we know whether this tenant is
created on an application service that
uses one or the other authentication
type so when you create the users we
guide you a little bit by hiding the
password field and the authentication
email field depending on what
authentication type but after that point
when we created the users what we do
technically is we do remote power shell
into one of the Williams and run the
command lets for creating new users
which you have probably used to
no but you can use any aad account you
like but we are running in the cloud and
if you have an active directory already
it's quite see easy to federal rate that
or synchronize that with an act as your
Active Directory and you should have the
possibility to select the self signed
certificate but what if we want can we
also use our own root certificate or our
own certificates and do we then need to
share our private key with you so you we
recommend as either explained that you
upload your own ssl certificate if you
are going into production with this
right otherwise your customers will see
a warning dialog whenever they connect
which is not nice and in order for us to
be able to install those certificates we
do need your private key which we can
talk about how we store that and we
encrypt it and we use a keyboard that's
a long story too but we're following
pretty strict guidelines on how and we
also have the key rotation on natural
keyboard so it's it's very hard to be
compromised I should automatically
rotation every time we are a swimming
above a new service and then you
deployed all right if there is no more
question or just one more and it's lunch
time so I can understand if you want to
get out of here you already mentioned
the add-ons that can be deployed to the
tenants but what about the extensions
yes so I think I think we also covered
it briefly so if your application
contains extensions then on the tenant
and the individual channel you can
choose to have them installed or not
right so you go to the tenant you click
manage extensions and then you see the
list of the extensions that are in the
application together with a check mark
whether you have installed them on your
chin in already and then you can change
it and press the button and we'll do the
installer on us all so it's quite simple
all right times up thank you very much
for coming enjoy the rest of the
conference
