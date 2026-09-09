# NAV TechDays 2019 - Make the most out of Business Central on Docker

- **Source:** https://www.youtube.com/watch?v=Dr6bFoRELnY
- **Video ID:** Dr6bFoRELnY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 89m53s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
thanks a lot about docker and how we can
use it to make more out of our business
central containers and those
environments to just give you a brief
introduction after being introduced so
well my name is Tobias Fenster I'm the
CTO of the cosmo console group and the
dual microsoft MVP for business
applications and for Escher if you want
to follow what I'm doing this URL to my
blog and also a couple of ways to get in
contact with me
so if you have anything to discuss
mainly around the concepts of docker but
also everything else around business
central or I sure feel free to contact
me so what are we going to do today
first of all I'm assuming that you know
roughly what occurs that won't be an
introductory session I'm going to use a
couple of things that are a bit more
advanced and I'll try to introduce those
but the basics of docker are just assume
you know what it is so in case you
haven't used any doctor before that
might be a bit hard to follow the
scenario that I want to take her today
is caused by by the following base
principles or the base ideas that docker
containers are allowing you to run
multiple versions now if you've worked
with docker you know that you can have
something like NAB 2018 cu5 and cu7 and
Cu 11 running next to each other and
then there's maybe business central 13
and then there's business central 15 or
whatever and you can all put them into
one into one and the same VM without
having to worry about those interacting
with each other so that's a good way to
have something up and running on your on
your VM or even on your laptop and also
we have the fact that docker containers
have a much lower resource overhead
because VMs all bring their own guest
operating-system containers don't do
that they just reuse the operating
system of the host machine so that means
that we have a much lower resource
overhead when we are running containers
and also creating a new container
deleting a container starting and
stopping containers the whole
interaction is a lot quicker than with
VMs so you probably really want to have
a lot of containers running inside of
your VM or on your laptop and not a lot
of a lot of VMs running for your
different environments so that means
that we need a place where we
can put our containers we want them up
and running we want probably a lot of
those up and running in our VM or
whatever we want to use for that one so
that we can save resources and scale a
bit better but then the question becomes
how can we connect to those if you if
you stalker on your laptop that's very
easy especially with the enough
container helper and the the update host
flag where you can just use the name of
the container and connect to it that
that's very easy but as soon as you want
someone else to connect to your
containers or you want to have a
centralized environment where you want
your development or your test machines
to connect to that that's gonna be a bit
more difficult and that's what we're
gonna tackle today in the first three
steps so I'll introduce three ways to to
get that done the first two are just
built using darker itself the third one
will use an additional container
additional tool and then in the end we
will talk about two more ways to get
that even more efficient even more
scaling and even more flexible and
dynamic so to start we will look at a
way how we can get the networking
problem to work by worrying about all of
the ports individually so we're gonna
make sure that everyone is able to
connect to our containers but we will
handle every every port individually and
that can be done with something that's
called port mapping the basic idea here
is that we have our docker host that's
the blue thing here and then we have one
container running in that host now that
container is listening on a couple of
fours and just as an example I'm using
the NST port 70 45 to 70 49 and but what
we can do with port mapping is we map
those ports of the container to ports on
the host as I tried to show here so that
would mean if someone wants to connect
to the development port 70 49 on that
container they would just use 70 49 the
host name and port 70 49 on their laptop
to connect to that container and because
of the port mapping the host would know
that it needs to redirect that port to
port 70 49 on our container now that
seems very easy but the question is what
do I do if the second one comes up
because now I can no longer map 70 45 to
7 to 14
to the same ports on the host because
they are already in use by my first
container I can't do that I would get an
error message if I try to so what I can
do is I can use different ports for the
mapping in that case I'm not using 70 45
to 70 49 on the host but instead I use
71 45 to 70 149 that means that I need
to tell my users now if you want to
connect from your laptop to that
container you need to use port 71 49 so
it's a bit more of an overhead I need to
tell them what to use when in which
occasions but apart from that it just
works they will get the connection to 70
49 of the container and they can work
with that and then if we imagine a third
container you probably can imagine how
that one works I'm just mapping to a
different port range again and let the
users connect in that example to 72 49
and they were able to connect to the
development part of my third container
so how does that actually look like
oh that's gonna be interesting let's see
if I can see that as well
okay that's better no I'm seeing it as
well so I have created a hose on on
Azure and created hyper-v VMs on that on
that host as well the reason for that
will be shown in the second demo but for
now let's look at the first one about
port mapping so what I'm gonna do is I'm
gonna run going to run a container as
you can see here I'm just using regular
docker run commands and I'm mapping a
couple of ports I kick those off so that
have some time to start and then I'll
explain in more detail so what you can
see here is just a regular docker run
command that you might have seen before
so we're just running we are accepting
the end-user License and this abling
sorry and this abling SSL Certificates
as it's lots of a bit quicker there and
then I'm mapping ports in that example
I'm mapping the web client port 480 to
port 8080 on the host so you can see
here - P is the parameter that allows me
to do the mapping and the first part of
that is the port on the host that I want
to use 8080 and the second part is the
port on the container that I want to
connect to in that case 80 and I'm also
connecting the development part in that
case I'm using the same port 70 49 I'm
mapping - 70 49 again and for the first
one I'm using a German image so we can
see the difference in a minute now I
also want to show you how you can do
that using a second container and in
that case I'm doing the exact same only
I can reuse the same ports as I
mentioned because that would be a
conflict instead I'm using port 81 84
the weft line over here and I'm using
470 149 instead for the development port
so why we let those start I'll switch
back to my presentation and see if I can
get that one to work okay
so um what's the good and what's the bad
about those ones it's very easy to
connect as you will see in a minute but
you need to know the port if you know
the port and it's very easy you always
need to find out which ports are free
because of the problem that I can't
reuse the same ports so if I start a new
container I need to make sure I
understand which ports are already in
use which are blocked and then use
something else in the in the demo you
already saw that there are additional
ports to consider so it's not only 70 45
to 70 1449 but it's also the redline
HTTP or HTTPS it might even be sequel
server and it could also be the download
the download page that is listening on
port 8080 so it actually is not 5/4 that
we need to worry about so but it instead
might be nine ports that we need to
worry about for every container
depending on your firewall setup you
might also have to open up the ports on
the firewall in my case I don't need to
do that because I've reconfigured that
but you might need to open all those
ports because they are falls on the host
if the host is secured by a firewall you
might have to open the ports there as
well and if you're running on a juror
that means you have two firewalls to
consider because there's a narrow
firewall in front as well so let's see
if the containers have finished loading
you can see that okay I'll try it that
way so no I actually can't see my mouth
sorry
okay so here we are um the containers
have finished loading you need to scroll
up a bit to see the password that was
used and now I can get over here to a
second machine which is acting as a
client and I'm connecting to the host on
port 8080 and I'm also connecting to the
host on port 80 180 to get the second
one and the first one login and try to
type the password correctly let's see
and looks good and then I'll try the
second login
so as I said you can see now that I've
connected to the host on port 80 180 and
I've connected to the host on port 8080
and I expect to see two different
environments I've already put in two
different passwords so that probably has
worked but we should see in a second
that this one will give us the German
that lined while that one should give us
the English web client so let's see yes
you can see the beautiful German word of
coughs all talks for bytom is the name
of the roll center and then we have in
English here the sails whatever say it's
order processor right so you see we've
connected to the two different
containers we could of course repeat the
same for a third for fourth how many I
can just fit into that virtual machine
let me just quickly clean up those two
containers and we will continue okay so
to get back to the presentation here we
are so we've seen that it actually is
easy just inputting the port but across
the problem is that it is a bit
complicated and error-prone if you can't
get the ports right if you're maybe
conflicting if your users get confused
which force to use when that might be
that you end up in a situation where you
have a lot of things configured
something is pointing to somewhere and
you're not 100% sure anymore
what is happening where so the second
option for that would be to bundle all
of those ports together as they are and
just worry about every container
individually that would mean that we
keep the ports but we worry about each
container and that can be done using
something that's called transparent
networking the idea here is that every
container gets its own IP address and
depending on your network setup I might
even be able to reach it by name so I'm
running a container on my host that
container has a name in that example DCA
and that would be reachable on its own
IP address and that's an IP address that
I can actually get from the from the
laptop so I
would only need to enter the name and I
would be able to connect to my container
I would just reuse the same standard
force that are already there so nothing
else I need to document or configure
because it's just the standard faults
that are in use anyways and the second
one that is happening or that is started
gets its own IP address again I can
connect to it using its name and of
course the third one just works the same
I get its own IP address I get a name
and I can can connect with it using that
exact name so again how does that work I
go back to my host the first thing we
need to do to use transparent networking
is create a transparent network so let's
do that and then we need to run our
containers this is the first one and
this is the second one and they should
be starting so what we've done here is
as I said we created a network that can
be done using the command talker Network
create we are using a specific type of
network which is a transparent network
so we need to set that parameter and we
just need to give it a name so we can
reference it later the docker run
command again has the acceptance of the
end-user License Agreement the
disablement of the SSL certificate now
we give it a name the German one and we
also give it a host name that is
necessary because we wanted to be
reachable on that name and what happens
when the container starts is that it
will reach out to DHCP and DNS service
that you have in your environment or in
that case that are happening on Asha so
it will request to get BCDE as a name
and connected to its own IP address to
show you the IP addresses that are in
use we have the host and that has 192
168 or 100 to actually we have our
client which gets 192 168 oh three and
now let's look at our container
they are not fully started for BC but
they should already have IP addresses
and we can see that here so I'll inspect
that one scroll down to the very bottom
and there we should see no IP address so
as I said it gets its own IP address um
try that one again on the command line
so just run ipconfig on the container
okay now you can see it got 192 168 0 10
so it's on the same network as the
client and the host and we can reach
that one and let's look at the W 1
container as well and that one got 11 so
again I can connect to that container by
now they might have finished starting
yes they have closed that one again so I
again use my client machine now I'm not
connecting to the host instead I'm using
the the names of the containers and I'm
connecting here and try the second one
as well let's see what the username and
password are here
and those should log in as well no I
mistyped there try again and the other
one is already logging in no what am I
missing
that's a de 1
do I have
okay I'm actually not sure why but the
main point is I can connect to that one
and as you seen I've connected at least
to the login screen so it seems to work
and let's see if at least the English
one will come up yeah here we are
so this is the English one the german
probably missing something oh let me try
that again yeah okay reading and writing
not my strong suit um so here we go
while we wait for that one to load and
continue here so what are the benefits
and the the disadvantages on that one as
you've seen it's very easy to connect
again I can just use the name as if it
was a virtual machine or a service
running somewhere so you only need to
let your users know what the name is
they need to connect to and then
everything else just works creating a
new container is easy as well because
all I need to do is specify that I want
to use that transparent network and
nothing else the problem there is that
this needs to be allowed on your network
depending on your network security
policy it might not possible that just
something pops up and gets an IP address
and gets a DNS information there as well
and also it needs a specific setting on
your on your hypervisor so that's MAC
address spoofing or from miscues mode on
VMware and that is something that might
or might not be possible in your
environment and something that the the
hyper-v admins would need to tell you
technically as possible but what it
basically allows is that a network
interface gets the traffic for another
network interface because we still are
going through the network interface of
the VM of the host but we also need to
address the traffic that is going to the
container and that has a different MAC
address so that is something that is a
security issue in some environments and
it definitely is a security issue on
Azure so we won't be able to use that in
Asscher externally facing now I had
created a VM and created VMs in VMs and
we can do that but I wouldn't be able to
connect from the outside to that one
so while it's a good solution for
on-prem it works very well there if you
have everything set up it is just not
possible on Azure if you want to connect
from outside of the VM and just to show
you I'll switch back once more and we
should hopefully see yes we have
off soft rocks for our item again
for the German one okay um that would be
the part about transparent networking so
we have bundled all of our ports
together we'd no longer need to worry
about each part individually we only
need to worry about every container of
course that might be a lot of containers
but still it's kind of convenient if you
can use that one but what if we had only
one place where we could go all our
network traffic through and we only need
to worry about one entry point there so
how does that work the idea here is to
use a reverse proxy the reverse proxy
means that we have our containers
running behind that proxy and all
connections just go through the proxy
and the proxy knows what to do with that
traffic so if someone comes in and says
I want the connection to my host slash a
def then there is a rule inside of the
reverse proxy that lets it know if
someone comes in with a def I need to
redirect to the container called ECA and
because it's the DEF endpoint I'm going
to use for 1749 so I have my container
running there and it will just get the
traffic and connect there so if someone
else now comes in and wants PDF I know
there's another rule that's called be
des maps to be CB 470 49 and I couldn't
connect to my second container and you
can probably imagine the third one CDF
and again I have a rule that maps see
def to BCC 470 49 and I can again
connect to my container if I want to
have connection to the web client as
well or to soboro data whatever I need I
just need to have a rule that lets the
reverse a proxy know if a request comes
in that looks like this you need to
redirect to that port and that sub URL
on the container
so again and let's look at how that
works for that I'll switch to a
different machine
and I'll just create a new container and
again explain to you in a second how
that actually works you need to give it
a username and a password and then we
create another one and as you can see
I'm using half container however in that
case I could have done the first one
with naff container helpful as well and
I could do that one without enough
container helper just to show you both
ways are possible here so some more
explanation of what is happening here
this is done using a reverse proxy
that's called traffic there are others
like Engine X or H a proxy but traffic
has the advantage that it's really
really is a cloud native contain a
native solution so it really is very
well integrated into the docker world I
could just can run it as a container and
it knows very well how to handle
everything in a in a container based
world it's very easy to set up and run
because it just comes as its own
container I run the container and give
it a bit of configuration as we'll see
in a minute and then it's up and running
it has a couple of convenience features
as well so it grabs the let's encrypt
supports so I don't need to worry about
SSL Certificates it can use your own
certificates if you have those in place
but if not you don't need to worry and
it can pick up new containers by
checking their labels that means that I
don't need to change any configuration
do any additional setup but all I need
to do need to do is start the container
in the right way and traffic will
automatically pick that up and be able
to do the routing and the connection the
actual mapping is done reg reg X based
so if for example I get a request like
you can see here that is connecting to
be ca rest then it will understand that
there's something behind that part and
it will map it internally to bc a port
70-48 bc OData because that's where my
or data service might be listening and
then it's just adding the stuff that
came in after the beginning of the URL
and also of course the same for example
for the web client and in that case it's
just mapping
- the same on the container you need to
do some additional configuration for the
business central container mainly
because the business central container
needs to know how it is reached from the
outside what the urls from the outside
are so that it can generate correct urls
into the redirecting correctly so there
are a couple of settings for OData for
so for the web client and the public dns
name so that again business central
knows what it's called from the outside
and we need to set those up and starting
the containers we also need to give the
web server instance a different name
because otherwise the redirection will
always insist on redirecting to NAV or
PC depending on the version that you're
running that unfortunately won't work so
we need to just give it a different name
but it is supported by the business
central image images since a couple of
months actually only is an easy an easy
setup step there as well and then we
have the problem or the challenge that
traffic only picks up healthy containers
no no if you know that but the docker
containers for business central have a
health check that checks if the service
and the web client are already there up
and running so it does that of course in
our scenario as well but the problem is
the traffic only picks it up when it
becomes healthy but the health check
will try to use that public DNS name so
it basically goes to the outside and
tries to reconnect through traffic again
back to our container but traffic will
never do the routing because it never
becomes healthy so we have a problem
here the solution for that again kind of
easy we just check for inside of the
container we avoid leaving the container
and going through the outside route and
then it works again and then traffic
also needs a set up file but that is
also very easy to set up it's very well
integrated into the azure arm templates
provided by Microsoft so if you go to
aks
aka MS get PC or get nav or what those
URLs are like then you will get a toggle
called add traffic you just said that
one - yes and then traffic will
automatically be set up when the VM
starts enough container helper supports
it as well so if you start the the
container as as you maybe have seen or
look at in this in a second you just
have to specify use traffic and it will
know that you're running behind traffic
if you're doing this on your own VM so
you're not using the pre provided VMs
but doing this on your own VM then
there's also a set up command let that
you need to call and it will bring up
everything like traffic needs it will
bring up the the configuration and the
traffic container and you should be
ready to go for your own VM as well so
let's see if we are there yet so now I'm
back on my which on my own laptop and
I'll try to connect to our container so
as you can see I already have a
connection and
yay as I said reading and writing and
that seemed okay I'm fearing that this
was said to English
exactly this was set to English and I
have a special character in there very
well so what we're going to do is there
is a container already in place when the
VM starts and we will just use that one
that also goes through traffic so it
should basically be the same and I hope
that I now know the password yay
okay and that's the password manager you
know why so that one is up and running
just to get back to the to the new BC
container commandlets what we are doing
here is everything as you've seen before
it rather it's a it's a rather easy
statement or actually the most basic
statement that you can do when creating
a new container the only thing that
we're adding is the used traffic over
here because this will create the
container in the right way and to show
you what that means if we look at one of
those containers we will see a lot of
labels over here smaller here so what
you can see is first of all we need to
let traffic know that we wanted to
handle that container that is done by
setting a label that is called traffic
and able equals true and then we need to
set up our our routing rules and for
example you can see that one here so if
something comes in using slash third
that will only be redirected to the
Container on port 80 so what we've used
before where we said slash nav server
that only will be redirected to the to
the nav server container on port 80 a
slightly more complex rule you can see
here in that case when something comes
in using third GL for the download page
it will just remove that part that's why
it's called path
Fix prefix trip because it will remove
it and it will redirect to port 8080 on
the container and then the most
complicated that we have here which is
actually not that complicated at all is
that when something's come something
comes in for example using the prefix
third rest then it will know that it
needs to do some some reg X replacement
so it will take everything behind the
third rest and put it behind slash BC so
you can see here this is the first match
this is my my search pattern and it will
just transfer that one to the to the
other URL and redirect in that case to
port 70 48 so with that I have
everything set set up I can connect the
web line to the download page and to my
development rest and self services and I
should be up and running the traffic
terminal file as I said is a very easy
configuration file we need to let it
know what the domain is that we are
going to reach from the outside so that
it can request the right let's encrypt
certificate we need to let it know that
it should watch the docker endpoint and
where it can reach that docker endpoint
so it gets the information when a new
container comes up and can look at the
labels to find out if it needs to handle
that container or not we need to define
the entry points so we are listening on
port 80 and we're listening on port 443
but if everything comes up to comes in
to port 80 we just redirect to to https
- 443 to make sure there's a secure
connection and this is the setup for
let's encrypt for the certificates they
want an email address they can use to
let you know when your certificates
expire traffic also has an automatic
renewal in that case but you will still
get the email address or the email
information and it also again needs to
know what the thing is called from the
outside and the rule here below is only
in order to make the to make the landing
page work so if we go to the landing
page of that virtual machine sorry
go to my browser then you can see this
is the standard landing page that
Microsoft provides for their VMs and you
can see here that it knows where the
containers are running so this is the
one that we just used and that's the
second and the third which are set up so
to show you that the connection also
works I'm going to create a new al demo
project and just use the defaults here
it's my own server and I need to let it
know which server to use now on the
landing page conveniently there is
already a pre pre prepared stuff for the
launch settings so I can just copy that
one and paste it here so two things to
notice I of course have put in my my
server URL but then as a server instance
I'm using the path where traffic is
listening so in that case that would be
nav server Def and I need to set the
port to 443 because remember we want to
tunnel everything so through the same
port so traffic is listening on 443 and
we need to do every connection to 443 as
well
so if we now try to download symbols and
some suspense again seems like I didn't
miss type this time yeah we can see the
package is downloading it's only missing
the base app and the base up is here as
well so our errors here have resolved
now let's try to set a breakpoint and
deploy that one
it has been published it should start
you can again see that it's using slash
snaps over here because the development
endpoint will let it know that it needs
to connect through enough server that
again only works because we're setting
the public web base URL correctly and
our breakpoint that's it and you can see
here I just get the usual stuff in the
in the debugger so that just works I'll
continue and with that I see my my hello
world again okay let me check did I want
to show you anything else
oh yeah the health check so does that
look like as I said we can't connect to
the outside as is the default instead we
are just using localhost for that one so
we're just connecting to the localhost
getting the connection there and with
that because we it returns healthy
traffic we'll know that it needs to pick
up that container and we're fine
in the in the original standard it's not
localhost here but it said it's using
the public dns name everything else is
basically unchanged okay that's what I
think I wanted to show you there maybe
so that you have seen the file structure
here as well sorry to do that on the
server the configuration files are
stored in C program data and I've
container helper traffic for BC and then
there's the config area and there is the
traffic tamil file that I've just shown
you a template where it is generated
from and the ake me JSON file contains
the certificate that it got from from
let's encrypt so if you ever need to
tinker with those files they are in the
standard and F container helper folders
okay so let's get back to the
presentation
so what you see now is how that setup
works and I think that's a very good
setup as well because it's very easy to
connect to from the client you only need
to know the path that is something that
you can probably communicate easier
creating a new container is easy as
you've seen you just need to use the use
traffic switch and then you're up and
running and you only need to have one
entry point for reverse proxy so if you
have which is usually the case only one
reverse proxy up and running then you
only need to worry about that port and
so you could have additional ones but
really it probably should be as easy as
having one entry point that you need to
worry about it of course it is one more
component to set up and maintain again
if you're using the arm template setup
it's very very easy so that there
shouldn't be too much of an issue but if
you want to handle that on yourself you
need to basically start understanding
how traffic works we would need to do
more work for the non HTTP traffic so
everything that that F environment does
so breast and the back line and that
stuff is all HTTP based and that just
works but for example the connection to
the sequel server using seaside or using
the sequel management studio or the old
windows client that would be tcp-based
and that doesn't work out of the box
with traffic 100 traffic 2o which came
out a couple of weeks ago should support
that
um but I have to admit that I haven't
tested that yet so it should be possible
and I'll probably try that in the next
couple of weeks and blog about it but
I'm not sure 100% yet and the URLs that
are returned from the soap and the rest
endpoint are not correct but I'll show
you in our in my last demo how you can
easily fix those as well so I guess
that's a good solution for both worlds
either on from or on Azure because you
can do that quite easily and if you have
the option to go for the azure VMs and
use the automated setup it should
actually work very very seamlessly and
just out of the box okay so with that we
will go for the real deal the more
advanced topics and that for today would
be water profiles or about bottle
rockets
so as you can see here that is what you
can do with a soda bottle a bit of water
and then some pressure and it doesn't
want to start here we go
I find that absolutely amazing I might
be a bit biased because it's one of my
kids but I just love that when I saw
that the first time the way they go up
and how far they go that's amazing but
of course that's not the topic for today
um we've seen a couple of approaches how
we can handle the networking problem but
there are a couple of issues with that
because we have only one host where we
can run our containers so while that's
fine until a couple of containers are up
and running we will run into problems
when we have 10 15 20 25 or whatever
containers then just one host isn't
enough so if we run out of resources we
need to find another way and the easy
answer for that one is well let's just
use the second VM in a third VM and a
fourth um and so on but then the problem
becomes how do I figure out what to put
where why am I using the first host for
that container and the second host for
that container how do I let my users
know what is running where because now
they need to have different machines
they connect to how do I let know how do
I let them know how to reach everything
so that can become more problematic and
scaling up and down is more problematic
as well
I mean scaling down is switching off the
VM so that's that's kind of fine um but
if I want to have the container still to
be able to connect to that one if I want
to move containers between VMs that will
become more difficult and scaling up
means creating a new VM setting
everything up bringing docker up so
that's a bit more effort on that side
and the second limitation that is there
that we're still running one sequel
server per container as I said in the
beginning the containers are good at a
resource consumption because they are
not using their own virtual machine host
system but they're just using the the
Windows server that is running on the
host so we are very efficient there but
then we are running one sequel server
per container so if you're running 20
sequel service that's 20 let's say
Kronos databases and we're having 20
sequel servers that's of course not
where sequel
server is best it's perfectly capable of
course of running trendy databases so
that doesn't make too much sense there
as well we have the same scaling limits
for sequel server even if we use a
different one on a different virtual
machine than we might run into scaling
issues and if you're using the sequel
server that is running inside of the
container you will hit some size
limitations as sequel server Express is
running inside of the container so you
can't do databases that are bigger than
10 gigabytes and you would need to worry
about that one if you're using that so
in order to solve that I'm going to
introduce two concepts or two new tools
that we're using and that by no means is
the only solution for that but just one
of the possible solutions that I want to
show you and the first one that we're
going to use this docker swarm as you
can see by that image the base idea is
to have our containers handled not only
by one of those queue wall layers but
actually we want to have multiple of
those and are still carrying all of my
containers together so what's the base
ID here um darker swarm is the built-in
container Orchestrator from docker so it
really is the answer when you're asking
the question how am I going to
orchestrate a lot of containers how am i
bringing them together making sure they
are working together then the standard
answer from docker is docker swarm the
idea here is to bring the resources of
multiple container hosts together so I
don't have only one container host where
I'm running my my my my containers but
I'm actually using a lot of them and I
have a way to centrally manage and
control them I don't need to worry about
each of them individually but I have a
central interface where I can do the
management and the configuration now if
you imagine you have multiple container
hosts you might need to have some
configurations some secrets access keys
whatever that you need to spread across
all those hosts and dr. swarm has a
concept there as well it's called
configurations and secrets and it
automatically takes care of spreading
that across the whole swarm so whatever
whatever virtual machine has joined with
that swarm will be able to have access
to those configurations and secrets it
has a declarative service model as we
see in a minute that means I only need
to describe what I want to have but how
it is actually done is up to swarm and
at
need to worry about that it has a couple
of automatic self-healing concepts that
means that one of if one of the
containers fails it will automatically
restart that one and get a replacement
for that one and it has a couple of
advanced networking networking concepts
that help me with our resiliency as well
so if you've looked into the darker
world recently or the last couple of
month and of course docker swarm is
something that that has lost some
traction actually the container
Orchestrator that is used most is
kubernetes from google i'm not using
that here because of two reasons the
first is that kubernetes is really very
very good at micro services stateless
micro services and while the the Navon
business central container is an amazing
piece of technology it definitely is not
a stateless micro service actually it's
kind of the opposite if something like
that exists so a lot of the benefits
that you're getting from kubernetes and
the features that are there you won't be
able to use anyways and it has a rather
steep learning curve so while docker is
very very easy docker swarm is very easy
to set up and use kubernetes has a bit
more overhead there so it's easier to
just adopt swarm and use it because it
has all the features in my opinion that
we need for business central anyways and
the other thing that you might have seen
is that a couple of days ago Miranda's
bought docker especially the docker
Enterprise Edition I need to say and
they had an announcement that said that
docker swarm would be out of support in
two years but what they actually are
saying is that for the Enterprise
Edition that probably none of you you
are using anyways docker swarm support
will be there for two more years but the
Community Edition the open source part
that is still there and it's still
living on a stalker and as darker ink
the company that will continue to exist
and we should have talked a swarm
support there as well and also there
something that I want to mention about
kubernetes that the second point is that
there is currently no way to run a
Windows only kubernetes cluster you'll
always will need to have at least two
so-called pods that are running on Linux
so depending on your skill level that
might not be a problem or it actually
might be an issue so
those are the two reasons why I instead
decided to go with swarm here so to
introduce you to some of the basic
concepts in the swarm world the thing
that you will run on a docker swarm is a
service and in order to create a service
you will need to let it know what image
you want to use how many containers or
tasks you want to run and the
configurations that you want to run so
my environment parameters the
connections to sequel whatever I need to
let the container know in the BC world I
would need to set that as configuration
parameters those could those tasks can
be replicated or clover replicate it
means that I just let it know I want
three of those and then I will have
three of those in my swarm or I can have
it global global means that every one of
the machines or nodes that are joined
will have one of those containers up and
running nodes are the container hosts or
the docker
engines that are joined to the swarm and
there are two different kinds of nodes
the first one would be a manager node
that is the one that has the control
which I connect to to to get my services
running to remove them to find out what
is happening and then there are worker
nodes which are the ones that are just
doing the workload if I now want to run
something I'm declaring that service so
I let it know use that image that
configuration that number of tasks
I submit that to a manager node and it
will make sure that the things that are
actually needed to be done so letting
all the workers know that I want to run
something pulling images starting
everything keeping up with it still
healthy that will be automatically done
by swarm and it will keep the desired
state so if I say like I want to have
three of those and one goes away it will
make sure that it's recreating a
container again so the base idea here if
you think still in the old world where
you have three docker hosts what would
you need to do if you want to one if you
want to run five containers you would
connect to the first one through RDP or
a remote PowerShell session or whatever
and let it know I want one container I
want two containers then you would
connect to the second docker host you
would
they didn't know I want a third
container I want the fourth container
and then you would connect to the third
talker host and again let it know I want
to have my first container so the task
of running five containers on three
hosts is rather cumbersome I need to do
a lot of connecting and starting and
setting up now if I run this on a swarm
I just talked to the swarm as a whole as
a concept so I just let it know I want
five containers wherever running on my
swarm so with that I would do nothing
but let it know I want five and it will
spin up five of course behind the scenes
there's still the workers and the
managers that are running the containers
are still running on the VMS but I don't
need to worry about that one I just let
the swarm know I want five and it will
handle all the rest now for the
networking stuff the containers are or I
can use a feature that is called ingress
networking and it works that way that
wherever I connect to to one of the
nodes on a specific port it knows which
service is serving that port and it will
be able to connect to that one so for
example I connect to that worker and try
to access a port where I know a task is
listening then it might give me that one
but if I connect to a different one for
example the manager here it might still
give me the container that is running on
the worker and even if I connect to a
note that is not running any of the
tasks that is providing my service it
will still let still know that there's
some service somewhere and will connect
me to that again that's called ingress
networking and the base idea here is I
don't need to worry about finding out
which container is running on which
hosts but I just connect to any one of
them use the right port and I get the
connection that I need unfortunately as
I said the BC container is really not
stateless and being stateless is a
requirement for something like this so
we are not able to use that one so I'll
show you using a different image in a
minute the second feature that I wanted
to show you it's very much usable in the
business central world and that's the
ability of a swarm to find to let a
service find other services no matter
again where they are running that's
called an overlay Network so if we get a
connection into our
first container and that container
depends on another container or on
another service it's able to find it
whether it's running on the manager or
maybe it's running on a different worker
it will just automatically find that one
again I don't need to worry inside of my
service inside of my container where
something else is running I just let it
know I want to connect to a service with
that name and no matter if it's running
on the same host or its if it's running
on another host it will automatically
get that connection so as a demo
scenario I will show you a service that
consists of two containers or two tasks
and that one will just return a starting
page and will also show you the ID of
the container so we can see that it's
actually connecting two different
containers then I'll show you how
scaling-up works and I'll show you how
the resiliency works by just removing a
task for that I will connect to my swarm
and create my hello service and say
hello service so that should be the
right one still there oh thanks a lot
okay so I just connected get up there I
just connected to my swarm and called
the service doctor service create that
is creating a new service I'm giving it
a name in that case say hello I let it
know that we that I want to replicas and
I let it know that I want to connect to
I wanted to connect to port 8080 on the
host so that looks kind of similar to
the port mapping that we've seen before
I can also do things like this where I
let it know that I don't want to run
this on a manager node so the constraint
here is that the role of the node where
those services or those tasks are
running should not be a manager and I'm
provided with the image and that would
be just the sample image that I just
talked about so if I now connect to port
8080 on my swarm I should hopefully see
a starting page page exactly and this is
the the ID of the container that is
running and if I now reload again I'm
just using the same URL if I now reload
yeah I'm getting the same container over
and over again so let's check what is
happening so I have my say hello service
here that by the way is port aina and a
GUI interface for working with docker um
and I actually do have two tasks running
from my say hello as you can see here
one is running on workers worker one and
one is running on worker zero so that
should work
let's try again no that's trying a
different browser okay you see I got
that one here and using the same URL I
now got that one so I indeed have been
redirected to a different container to a
different task and actually those are
running on different virtual machines if
we look at for trainer again it has a
feature that allows me to look at the
swarm
so I can see here that I have one
manager note and I have three worker
notes those are just different virtual
machines and it even has a visualizer so
I can look at that one as well I have a
manager note that one is running porteño
which we were just now using it also has
traffic but we're not not using traffic
at the moment it has those page base
agents they are necessary for porteño to
work in a swarm and you can see here
this is worker zero it has a say hello
service say hello Tosk
and here we have worker one that one has
a say hello task as well so those are
the containers and as you've seen I just
told the swarm I want two of those and
it automatically spread them across
across my swarm so if we go back to the
service definition and now for example
we want to have more of those we can
just hit scale here let's say I want
five and then I need to quickly switch
back okay now you can see it has created
three more and if we give it a second
now they are up and running you see
that's a rather small image business
central go take a second more so those
are up and running and now I'm able to
connect to those five or use those files
they are again spread across the cluster
so to check the visualizer again we now
have two running on work or two we have
two running on work of one and we only
have still one on worker zero and so on
will automatically do that so what
happens if I just remove one of those I
can still look at the individual
containers and I'll just remove that one
to delete and then switch back and now
you can see here that it understands it
currently has four up and running
because I removed one it needs to have
five up and running and because I wasn't
quick enough it has already scheduled
the fifth one so it already has
recognized one is missing I need to
create another one and if we refresh now
we get five up and running again and of
course I can also scale it down so let's
say I don't want five I actually only
need three and if we give it a second
then it should automatically delete the
others shutting down and now we are left
with only three containers running again
this needs a stateless architecture so
we can't directly use that on on docker
on business central but depending on
your use case that might be might be
something that could be interesting for
you as well okay what else did I want to
show you I wanted to show you how the
setup works to show you that it's really
not that difficult I'm running this in
an arm template as well so it looks a
bit more difficult than it actually is
but what you basically need to do is you
need to allow a couple of network ports
that is necessary for a swamp to work so
I need those two TCP ports and it and I
need those two UDP ports and then swarm
is running and then I just need to call
docker swarm in it that is initializing
the swarm on my manager node and then
I'm using some some scripting to get
that information to the 2d worker nodes
because the worker nodes need a
so-called token basically a secret that
allows them to connect and what the
notes are doing to join is doing the
same networking stuff here again and
then it's only calling the join command
that I've provided here so on the
manager you do a docker swarm image and
on the on the workers you do a docker
swarm join and with that you have it up
and running without any any further
problems okay that is what I wanted to
show you one last thing initially I'm
using docker compose to set everything
up so you can use docker compose as well
with a swarm and in that case I'm
letting it know that I want to have one
traffic image
running on my on my swarm I want to have
the agents running on my swarm as well
sorry as I said there's the difference
between the global deployment and the
the replicated deployment so in that
case that would be a global deployment
to make sure that that every node gets
one of those agents and for my port Lina
I'm letting it know that I want this to
run on a manager and then I'm also
publishing or that actually was traffic
um I'm also publishing port Ainur I want
to run that one on the on the manager
node as well so you can see here that I
can also use that I can also use docker
compost to define the containers that
are I've been running let's worm now
this is the compost file I want that to
happen and it will automatically bring
up the containers as well okay so that
was the first part of trying to tackle
the issues that we've seen with the
individual containers the second part
that I'm going to use here is a sequel
and after elastic pools so if you
haven't worked with every sequel that's
a platform as a service offering that
means that Microsoft is running the
sequel server it's maintaining the
sequel server it's updating it it keeps
it secure whatever you need to do there
it scale it can scale up and down
dynamically so I can let it know I have
a database that database now should use
two cores and whatever amount of memory
and I can scale that one up and down
like if it hits 90% resource usage for
more than an hour I'm scaling it up and
if it's running below 10% for more than
an hour I'm scaling it back down again
it has almost no resource limits so as
you know Asha has a lot of resources and
we can use a lot of that using Azure
sequel and the additional thing that I
want to use is an elastic pool because
that allows me to reuse that resources
between databases as I said I can
allocate resources to one database but
then that database might hit a peak
where it's not
enough and for most of the time it will
maybe idle at 5% or whatever so it
doesn't make too much sense in that
scenario to to allocate the resources
just to one database instead I'm using a
pool that means if one database needs me
more resources it can get those
resources from other containers that are
idling at the moment and that way I'm
able to scale even more flexibly in
there
so overall the benefits are of course I
don't have any server maintenance I
don't need to worry about updates
security fixes whatever I have almost no
scaling limits but of course I have cost
I need to pay for that so if you recall
those were the limited limitations that
are introduced after showing you the
first three parts we had the problem
that we were bound to one host and we
needed to find a way to use multiple
hosts the answer for that is the docker
swarm and we also had the limitation
that we had one sequel server inside of
a container and maybe even limits if you
ran that one on another server so the
answer for that one would be every
sequel and an elastic pool again that's
not the only answer of course it's just
an answer that I want to show you which
in my opinion works very well so to
bring it all together what we're doing
is we will create we will use the same
arm template to create a docker swarm
that will contain one manager VM and in
that case three worker VMs these note
that you wouldn't want to do that in a
production environment because if the
manager goes down the swamp goes down so
you would have would want to have three
or five managers or something like that
to make sure that you don't run into any
trouble if one of the one of the
managers failed I'm going to use a as a
sequel server with an elastic pool and
I'm going to use the script that I just
walked through where one is initializing
the swarm that the workers are joining
it sets up traffic and what we will also
do we will prepare the excess
credentials to access the database
because um even if we're using Azure
sequel we still need to get the database
in place for that container and the way
that I'm using here is I have a template
database or a master database in my case
is just Acronis but that could be
something else that you are using for
your products or your use solutions and
then the container will need to know
that it needs to
create a copy of that template if it
doesn't have its own container so while
the container starts it will check if
the database that it wants to use is
already in place if yes it just uses it
if not it will create a copy from that
template database and that way we are
sure that we always have the database
that we need so what we're gonna do is
we're gonna start a PC swarm of PC swarm
service and connect it to the database
that will be created on demand so for
that I connect to my business central
swarm and create a service and that one
has been created so as you can see I'm
using a business central on-prem image I
let it know that the original or
template database is having that name I
give it a name so the service has that
name and I'm reusing that name as a user
name and I let it know that I want to
have enough password that will be set as
password for that user so let's see how
our service is doing and it's called
check days so that way we can check the
state the desired state is running as
you can see here but the current state
is starting so that means it has
recognized that it already has created a
container for us but the container is
not yet healthy it's still in the status
of starting and to look at that using
port aina
so we now have it connects yeah
we now have an additional service that
it just called tech days and also
pre-created a fallback if everything
fails but this is the one that we just
created called tech days and you can see
here that it is starting in that case
it's running on work of one and I can
look at the log file and hopefully see
that it is starting it's actually a bit
slow and see you can do the same here
that doesn't exactly look good so it's
good that I created a fallback service
let's see here so what happens when it
starts I switch Auto refresh off and get
back up here so that is not the full
lock sorry
not getting the full lock why not let's
see if that one
works yeah okay
and we use that one um so what happens
on startup is over here so it's
downloading my scripts and I'll show you
in a minute and first of all it's
importing azure modules because we want
to interact with Azure in that case it
locks into my to my account and then it
checks if the target database already
exists so it looks if there is a
database in a place where it expects it
and the answer is that it doesn't as you
can see here resource was not found'
so it just creates the copy
automatically and when that copying has
happened that took one minute in that
case then the container starts just as
usually it initializes starts everything
it doesn't say starting local sequel
server because we are connecting to as a
sequel but it will know that we're
connecting there and it sets up
everything else so if we try to connect
to that one where did I that's here to
the web client
copy that and try it here the username
would be
Tech days and my fancy password No
and we are locked in into the database
that is running in the swarm the
container is running in the swarm and
the database is running in Azure sequel
so to show you a bit more how that setup
works we are first creating those
configurations and secrets those are
necessary to give give the access so I
do this once by logging into the swarm
because I need to login using my
credentials and of course don't want to
put my credentials in in a script here
but then I'm creating something that's
called an azure service principle and I
only give it access to a very limited
part of my subscription of my of my Asha
resources so I only let it connect to a
sequel service that is the original one
I give it read access to my whole
subscription so that it can login and I
give it again write access to the
original sequel database server where
the template database is stored so it
knows where the template database is
stored and has the connection there to
that sequel server and it knows where it
wants to create the new database and has
access to that one as well and then I'm
sharing that as secrets the application
ID which is basically the username the
secret which is the password and the
encryption key for that and the password
that we want to use for using sequel
authentication because business central
doesn't know about those as ready
principles and it just needs to use
sequel passwords there and then I have a
number of configurations as well as well
which lets it know which as a
subscription I want to use with resource
group which server name and so on so
that way we are limiting the swarm to
one sequel server where the the
templates are stored and one as a sequel
server where the target will be
happening but in my opinion that's not
too much of a limitation because if we
want to use different sequel servers
then we can also use a difference form
because the initial sequel server can
scale almost without limits so that
shouldn't be too much of a problem but
you might want to consider a swarm for
development the swarm for testing a
swarm for external access or something
like that and then you have the
databases separated as well okay then
you've seen I've just used the script to
create the service and the reason for
that is
that I need to provide quite some
parameters there they are actually not
that complicated but they are a lot you
can see the traffic stuff here as well
we've seen that one before and then I
need to give it access to my secret and
to my configurations so the way that
works in swarm is that if a container
wants to access a secret or wants to
access a configuration I explicitly need
to give it access using that startup
parameter so I need to provide all my
configurations and all my secrets in
order to allow it to connect there and
as you can see here I can also do things
like memory limits so I can make sure
that not one of the containers is
blocking my whole swarm or my whole my
whole container host instead I let it
know that it can use a maximum of 12
gigabytes of memory in that case okay so
we have locked in we've seen the web
client we can also use our beautiful new
modern client so let's connect to that
one need to give it the URL and we can't
connect
oh yeah I ran into a slight problem
preparing my interfere my demo
environment so that's what's happening
here now I can login and I should have
my web client up and running
the same is true for the mobile client
so if the connection is still there I
can show you the mobile client so to log
in here again it's using fallback and
put in my credentials no and hopefully I
should see a login screen if you try
that with the current state of the of
the traffic implementation that probably
didn't work that's because there was a
slight problem with HTTP and HTTP I
fixed that for the for the presentation
today and we'll share that hopefully in
the next couple of days so then you
should be able to do the same with your
traffic with your traffic hosted
environments as well okay um and then
the last thing that I want to show you
is the following as I said the OData and
rest interfaces or the the OData and
rest endpoints return not 100% correct
URLs so let's connect to the rest
environment and just do a rest call and
one should return it's unauthorized cuz
that's the wrong username for the
fallback environment so let's try that
one again
and it needs a bit to warm up but then
hopefully it returns it does and now if
I want to connect so those are the sales
orders as a rest endpoint now if I want
to connect to or get the data for one of
those I have an ID here and I can copy
that one if I paste it in here you will
see that it's the returns PCO data so
basically the internal thing that the
container thinks although we set the
public o data endpoints but it's for
whatever reason it's not respecting
those so I replace that with tag days
the rest and sent the request again and
here I have my sales order so you need
to know that you can't directly use
those behind traffic but with that
slight change you can actually still use
them okay for the sake of time I won't
do the demo that the Deaf environment
still works I guess you can believe me
trust me it works but we've seen that
before as well
okay so with that I am at the end of my
presentation would open this one up for
questions with just one slide addition
there are three things that I really
really like on the BCIT side in addition
to the bcal health hashtag so the first
one would be that we are using docker a
lot and I guess a lot of you are using
docker a lot for a test and development
environment lensed but there is no
production support yet and I want to
share or raise as many awareness of that
so if you go to that URL or scan the QR
code please vote for production support
for containers because that is something
that I would really love to have and
while you are there you can also vote
for the second one probably not an issue
for to many of you but the developer
licenses are limited to 120 kilobytes
that seems like created in the 80s or I
don't know but actually that is
something that I think should be fixed
as well and as you've probably seen in a
lot of the sessions already there is a
new hashtag on on Twitter bcal help so
use that one if you have any questions
I'm trying to follow that one and listen
to that one as well
so
you run into anything just tweet there
use that hashtag and I guess the
community will be able to help as well
so with that that's the end I'm opening
up for questions if you have any so just
to clarify doctor and doctor swarm is
for development and testing only not to
use in production environments fourth
correct for business central absolutely
because we don't have official
production support so I guess if you run
into an issue with docker and business
central and you would want to get
support for that one you might run into
problems with Microsoft support but
outside of the business central world
dr. and dr. swarm are very much used in
production environments for example
there is support for running sequel
server in a container by Microsoft the
whole Linux world if you're basically
googling you will hit a production
container because Google is using loads
and loads of containers so the
technology in itself is very much
production already we just don't have
support for the business central
continues ok it's the same for on
premise absolutely no yeah alright yes I
absolutely for the questions yes thank
you you've been demonstrating how you
can connect a docker server instance to
and as you asked well yes
would it also be possible to connect a
darker server instance to my own SQL
Server for an environment or yes as
possible yeah absolutely
actually what I was using is I'm just
putting in the parameter server name
server instance username and password
and from then on it's it's the same if
you're using on-prem or if you're using
Azure sequel the hardware just happens
to be an azure but it would work exactly
the same you just let it know what the
what the serving in the instance the
password and the username isn't a Newton
just can go ahead okay thank you sure
I'll try to throw it hi hi
I would love to the users swarm for
development purposes for a development
team is there a way to scale the workers
up and down so I can spin up the MS out
depending
on how many containers I actually have
yeah that bed actually is the next thing
I want to look into a colleague of mine
has used what are they called the way to
scale the MS in a in a scale set exactly
so the way forward would be to just
check the scale set see what load
happens and then start a new one on on
demand you only would need to share the
secret for the swarm and then on sort up
you just run a docker swarm join give it
the secret and then it would all
automatically connect so that is if when
I've done publishing all that the next
step would be to use a scale set because
of course that is exactly what you want
to do scale it down when there's no load
and scale it up again when when you get
load cool that will be awesome yeah sure
if you want to join me later I can get
you that one okay yeah how does taka
swarm decide which gets how many tasks
this is just the count you can do more
so currently it's it's doing a count but
you can do more by for example look into
the resource consumption of the of the
workers but that is a more complex
additional setup it automatically will
just do a round robin so the first one
gets the first second third and then it
will start with the first one as well
but you can do additional things like
looking at the load and using the one
that has the least load and something
like that okay thank you sure additional
questions one over there yeah yeah yeah
that's that's shorter yeah I knew that
one
this seems to be the possibility of a
death spiral andhaka swarm of fail fail
and it keeps bringing up new instances
the control mechanism to protect that to
not make it know when you failed one of
the tasks failed then it was starting
over and it would start another a
limiter a limiter on death exactly you
can basically set a retry limit so
something like try five times and if you
fail then don't try again you can
configure that one as
just to avoid a death spiral yeah
absolutely and we have one over there
for security reasons I hand this over
thank you amazing presentation Thanks
yep the workers have to have the images
yeah there's no way to share them
between workers in terms of size okay
okay um first of all yeah what I didn't
show you the arm template allows you to
set a parameter which images it wants to
pre pull so if you set up it has
basically a list of images that it wants
to use now of course over time that will
get stale so you need to do something
there as well and what you would need to
do is make sure that every container
every worker is pulling the images if it
doesn't have an image it will
automatically pull that but of course
for the business central images that
takes a while so you probably would want
to set up something like a script that
pulls all the necessary images every
night and try to find out if there are
new images for the resource consumption
you probably would need to do something
where you would monitor the the disk
usage and then decide that you maybe
need to clean up your images or
something like that but I have to admit
I haven't thought about that one yet I
[Music]
have to admit I don't know if the
manager cares about the disk usage of
the workers or if you even can get that
information so the way it might be that
it can I just don't know it the way I
would go is with just a a scheduled task
on the on the workers that check and
then maybe get rid of images or get new
images and would you recommend using it
you can also do that on from that's just
for convenience I can spin up those and
and spin them down I don't have any
dependencies on anything so for the demo
I did this on a sure but you perfectly
fine to do that on
thank you further questions yeah how do
you scale or what was your thought and
scaling on for the hardware that is
involved in basically hosting the docker
swarm or hosting the docker images what
you look into is it more CPU heavy Maram
heavy or how do you basically adjust do
you make a template for yourself which
you below by trial-and-error learned
would be the optimal resource i actually
all the trial and error i have because
we're not using a talker swarm in
production yet is that when you run too
many containers on a vm then it gets
slow so that's the that's the error that
we found no to be honest i don't have a
good idea there but for for scaling
issues i always say that it doesn't
matter if it's running in a container or
not so if you want to think about
scaling then think about how many n STS
would you put into your VM and that's
the amount of containers that you should
put into that same VM if you're not
running sequel server of course sequel
server would add an overhead but if
you're just using the NS T in a
container then scale it exactly the same
as if there were no containers and you
were just running multiple and as T's
there all right so basically you're
saying of course it's not yet in
production there's no fixed plan for
that but you already have like an idea
on how to set that yeah absolutely and
and what I know and we're not running
that in production but actually the
question for that is not what we would
do with the swarm but the question is
how many resources does the NS T in a
container use and the answer for that is
it uses the exact amount the same amount
of resources that it would use outside
of a container so thinking about scaling
in the talker environment to me is
exactly the same as think thinking
outside of of containers because the
resource consumption is just the same
there's no word thank you very much
sure any more questions doesn't look
like it so ah the one more year sure go
ahead
maybe we have tried to add the support
for Active Directory users inside
container what area active directory
directory support for users inside an
app container so we can use Windows
authentication or yeah windows users a
lot that that works you probably you
have to two possibilities if you're
using that one on your on your own
laptop then you just can reuse your
windows username and password if you do
a more stable environment you need to
use something that's called a group
managed service account so you basically
create account an account for every
container that you start you assign that
account to the container and that way
you do something similar to a domain
join so that way the the container is
able to connect to your ad and talk with
that I've setup that we in my previous
company we're using that a lot so
unfriendly I definitely know that that
works very very reliably I've also set
up a sample for doing that using Azure
ad but I don't have more experiences
with that one I just know that the
initial setup has worked I could connect
I could use it I could use Windows
authentication that was fine but I can't
say I've run that one for more than two
or three days okay yeah you copied it
from a template yeah so I guess it would
be also possible to copy a customer
database absolutely do you have any idea
how it's an efficient way to get to the
cloud as far as I know you can use
backpacks and then you can use backpacks
and bags and backpacks are amazingly
slow so I unfortunately don't have a
better answer for that one
what I'm doing is I'm creating a premium
tier environment to do the upload it's a
bit quicker than and then then just
scale it down to basic or standard or
whatever I need but really I mean you've
seen it takes about a minute one and a
half minutes and that's actually a four
hundred megabyte ADA base so you can do
the maths how that would work with
500 gigabyte of this really that's
that's one of the open questions I still
have with Ezra sequel how on earth are
we gonna do resource efficiently if it's
up and running then it it's case very
well and in my opinion but getting a
backup to work that's that's a struggle
no it's a free download and it's part of
C II so to speak yeah as it's part of
the open source side okay one more
Thanks
hi amazing presentation thank you what
you prefer as a SQL server directly in
Azure or what you put the SQL Server on
the container host for performance wise
because I'm creating a development
environment for our developers and yeah
okay um performance wise I would prefer
the azure sequel as we just talked about
the backup and restore is slow but after
that you can get amazing performance out
of every sequel so if if runtime
performance issue is an issue then I
would go with Ezra sequel if restore
performance like you have to set up new
database all the time then as far as I
know there's no really good way to do
that with a sequel there's there's a lot
of waiting involved there so that might
be a reason why you would go with your
container host but then you're just
limiting yourself to the to the
resources of the container host if that
is fine if you can scale scale those
hosts weld and then there's no reason to
not go with the sequel server on the
container host but if you might run into
scaling issues on your container host
then every sequel is a nice alternative
and of course it will cost you money
that is just another question
transparent network directly on a JVM
because I created one and it's very
difficult to to DBMS that they get the
IP address from the DHCP yeah
what would you deploy in hyper-v server
directly to the azure host and create
their attacker hose or what would you do
I would traffic oh yeah I actually
wouldn't go with with transparent
networking on Azure
I don't think there's a very good way to
get that up and running reliably okay so
I use traffic to yeah okay yeah I would
I would look into I mean if you still
need to use like probably a lot of
seaside and the old Windows client then
you would need to look into using
traffic to Oh or maybe give it a couple
of weeks then I
we'll probably look into that one as
well but apart from that I think it
works very well for all the rest already
okay thank you sure one more try I know
it's either question or lunch so no more
questions that was the key okay so
thanks a lot for joining and
[Applause]
