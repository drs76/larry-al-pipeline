# NAV TechDays 2017: Easier and DevOps-friendly NAV environments using Docker / Windows Containers

- **Source:** https://www.youtube.com/watch?v=9c5Yl51yXb8
- **Video ID:** 9c5Yl51yXb8
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 89m17s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

okay first I am curious to hear by the
race of hand how many people you know
what darker is wow that was a lot I
prepared a joke right I'll tell you the
joke anyway because I thought that a lot
of people would not know what talker is
and I would tell I had never seen so
many people in a room going to a session
where they don't know what the topic is
but I can't say that because like over
half actually raised their hand - maybe
we need to skip all the slides about
what doctor anyway so the journey with
darker started beginning of March or
maybe July but in March in not much
August or July in August we actually
started getting getting people into a
private talker repository with Nav and
talker and since then since end of
October just three weeks ago we have had
nav and talker in the public docker hub
since then there's been a lot of tweets
a lot of blocks a lot of different
things on nav on Tucker and everything
very positive everything very very
everybody very happy about that and we
are going to talk about today what all
of this is because it started much
earlier than that on this slide it says
have in the corner that there was 4200
pools that was when we created this
slide a few days ago it's actually 5600
pulls today
meaning that 5600 times somebody has
said darker pool and have image since
three weeks ago I think that's amazing
but first for the presentation my name
is Freddy Christensen I'm a Technical
Evangelist in the Microsoft Dynamics NAV
team out of Copenhagen I've been working
on this from the Microsoft side and I've
been working together with these two
gentlemen who will present themselves
did one year and something
so experimenting with a navy and during
the last six or seven months we have
been running all new instances just on
docker yes my name is severe center I'm
from a German ISV called excels in FOMA
I think together with yaqoob I kind of
kicked it off last year like almost
exactly a year ago where we try to get a
Navy running inside the docker container
where Microsoft didn't didn't tried it
or at least it and let us know that they
tried it and together with yaqoob I
managed to get that to work and to run
and then we got kind of some interest by
Freddy and together we work to implement
that what we want to show you is give
you a brief introduction of what docker
is then get into more details about how
nav works on docker and what from our
point of view are there main benefits of
running a docker container for nav and
in the end we'll talk about what
Microsoft actually is shipping there and
if we have time then we'll go into some
advanced topics but that depends on how
well we go through all the other stuff
and how many questions you have so an
introduction to docker in Windows
containers um we'll talk about docker on
Windows Server because there are some
slight differences it's mainly basically
the same on Windows 10 but there are
some slight differences that you might
run into but today we focus on Windows
Server because it's a bit more stable
it's a bit more mature and you're able
to run that on a Windows server a bit
easier so what is docker
basically it's the leading
cross-platform software container
provider core software container
environment there are a lot more with
also a lot more of history in Linux but
darker kind of kicked it off for the so
to speak mainstream and on Windows
there's only docker for containers what
is a docker container what is a docker
image and docker image is kind of a
template of what you need to run an
application or to run a service so it's
the minimum OS that you need the minimum
binaries libraries and the applique
in itself which allows you to do
something like a very very small image
that only exactly contains what you need
to run your service to run your
application for nav it's a rather large
one because nav depends on net and a lot
of different additional things but the
idea is to bring everything together
that you need and include nothing that
you don't need to have as close as
possible to the minimum image and then
what's a container it's an instance of
that image so you basically tell darker
this is the image that I want to use and
now create me an instance because I now
want to run exactly that it has an
immutable immutable base which is the
basic image and then you put your
changes on top of that so you change
configuration you add locks your data
and that's that obviously changes but
the base image just is always the same
and what also is important is that while
there are many things where you compare
them a container container really is not
a VM it's not a VM light it's just isn't
it's something different especially you
don't have a graphical user interface
you connect to it through remote
administration tools or PowerShell or
command line but you can't RDP into that
so at least for me when I started off I
went looking for okay now there starts
it works how can i connect to it how do
I get my RDP connection and just to save
you time there there is no RDP
connection so what is the docker host to
bring this to an end the docker host is
the environment where your containers
are running so that's where where you
wear your containers really live to give
you more a bit of a comparison or to
better understand why containers are or
help you to solve some of the problems
that virtual machines have if you think
about virtual machines you have that big
ship so to speak which makes sense
because we're talking about containers
but let's just think about your your
virtual machine house as a big ship then
you're kind of putting small ships which
is your you VM images your base VMs
including your operating system onto
that ship
and then you're at their workload that
you want to actually run being it nav or
sequel server or is or something
completely different with containers
what we do is we remove that because we
don't actually need it at least not for
the purpose that that container serve
and that means that you can put a lot
more of the actual application payload
on to your hosts it means you get a lot
tighter packet packing of your
applications and the services that you
want to run so when we're talking about
image storage um how do the two compare
there if you think about a VM um you
have the first VM that brings the guest
operating system Windows Server then it
brings the binaries and libraries like
dotnet or something else and it brings
for example nav 2016 now if you want to
bring nav 2017 or a difference EU for
that matter and you bring the whole
stack again it's basically exactly the
same for a lot of intents and purposes
but it is just stored again so if you
have two VM bear images or hyper-v
images or whatever you have double the
amount of space that you need to store
that on your on your disk and then if
you bring something completely different
then it's the same again for darker when
you download the first one you also get
all that you need it actually is a bit
smaller or actually a lot smaller
because we're using Windows server core
so it's not your full Windows Server um
but again I have to download download
all of that but it gets interesting as
soon as I'm downloading the second image
the second docker image because now I
don't need to download the Windows
server core the base image again I'm
just downloading differences there's a
mechanism in docker that's called
layering and if I have the base layer
then I don't need to download that again
they store a md5 hash of those of those
layers and they just compare is it using
something that I already have then I
don't need to download that and it gets
even more interesting if I'm using nav
because it's using the base binaries
it's using the base libraries and again
I'm only going to download the
difference and you can imagine that that
it's even
more true if you're downloading a CU or
something so I'm really using my
displays better than that in that regard
and during runtime again if you're
thinking about VMs they are just
bringing the whole operating system the
binary is the service the actually
actual application all of that is
running but for docker we down bring the
the base of writing system we just reuse
the base of writing system that's
already there so that means that if
you're running multiple containers
you're just running one Windows Server
and that's the one that's running on
your host all the containers that are
running are not bringing their own
Windows Server they're just reusing
what's already there and that also
allows for tighter packaging of your
payload and if you're talking about
instance and so the different containers
that are running then it gets even more
interesting because if you think about
having for example three and every 2016
VMs running and there's the first one
and then you change a configuration file
in the second one and you change some
binaries in the third one then you still
have the full images running because of
what I told you in the beginning that
there's that immutable base and only the
changes are stored in darker it's
different because again the first one is
using all the storage that you have but
the second one where only the change is
in there users only really the part that
is changed and if it have something
bigger that changed and it's obviously
going to be bigger and over time while
the containers are running the
differences are going to go bigger and
bigger so you're losing kind of that
that a bit of that advantage but the
theory or the concept behind that really
helps to get to better use your
resources again so how does the resource
sharing work in the beginning if you
don't change anything if you just run
your container as we will see in a
minute how that works the containers are
able to reuse the resources as they are
on the host machine so in that example
you imagine a host machine with four
cores and eight gigabytes of RAM and you
have two containers and they're just
able to reuse all that so the first one
could use
as much as it gets and a second one can
use that as well but you can also
restrict that and help that container a
is only able to use part of that
resources and container B again is only
able to use part of that resource so you
can make sure that while they are
already using less resources than other
environments you are also able to
restrict how much they are going to use
on a maximum level that doesn't mean
that container a starts with two cores
and four gigabytes of RAM and they are
blocked but it means that it's allowed
to use nothing more than what you
restrict them to do for networking
because that is something that I at
least have struggled a bit when I
started with docker to give you an idea
of how that works um you have your host
machine in that example connected to a
192 168 Network and then you have your
container and in that example I used an
is container on port 80 so that gets its
own container Network and it's
completely different than the one you
have for your host machine that's what
called what's called a nut network in
talker and that means that if you have a
browser directly on your host machine
you can't connect to that container
using that IP address depending of your
setup name resolution might not work but
yeah IP definitely will work you can
connect there and you can use port 80 so
that works but if you're leaving your
host machine then it's a different story
because if you have another machine your
laptop or another another virtual
machine or whatever and it tries to
connect there it can't in that current
set up because it can't see the network
of the container so there's no way to
connect it to the one seven two network
and also there's nothing running on the
host machine and that would allow it to
connect with a 192 Network but we can
solve that for a number of different
solutions one is something that's called
port mapping and that means that you map
the port inside of the container to a
port on the host machine for demo
purposes I changed it to make it clearer
but it could also just map port 80 in
the container to mop port 80 on the on
the host but now I'm connecting port 80
on the container
to 81 on the host so that means that
from externally I can now connect to it
using the IP address of the host machine
and the port that I map to it so
bringing it to 192 and port 81 works
while the internal network still is not
available so with that if you're
wondering how to connect then why can't
I reach that and why can't I read why
can't I reach that that's the solution
for that and the other solution for that
is that you can allow the container to
reuse the network connecting connection
of the host and then depending of your
network setup that might get a not its
own IP through DHCP or you can set up
setting networking depending on what you
need but that would mean that the
container gets a IP address in the same
network and you can just use the ports
as they are so I would then be able to
just connect to port 80 on that IP
address and again on the host machine
now there's nothing running nothing
listening on 80 or 81 so I can't make a
connection there and the last aspect of
resources in in docker is the file
system as I said in the beginning each
of those containers lives kind of in its
own file system if you're coming from a
Linux background this is something like
a chain Trude so your mapping part of
your file system something that's deep
down somewhere in programdata docker to
the base file system in your container
so see temp in your container is
somewhere in your host again in a temp
folder and if you look closely for it
and if you search search your file
system then you can actually find it you
can see the files that are there but you
shouldn't directly use that because that
might not work in the future but what
you can do is something that's a volume
um I think that will also shown in the
in the keynote and what that basically
does it tells the docker environment
that I have that folder on my host and I
want to reuse it as that folder in my
container so in my example I'm using
cdata container temp and that should be
mapped to see temp in my container what
that means that if I'm doing something
in the container in C temp then that
will automatically also show up in the
host and I can work with my data there
that's typically used for configuration
changes or I want to use something
inside the container from my host or I
want to share something between
different containers then I can use that
for my volumes so that should give you a
basic idea of how darker works I hope I
didn't lose all those that already know
about docker and give those who didn't
know yet a basic idea of how what this
does and I'll hand it over to Jakob to
show you a quick demo we can see so the
first example is just to show you how
easy is run any view on docker so we
have a very simple example here I will
start it and I will describe what what
every parameter means so we have a we
are using docker run command to create a
new instance new container and to start
it in the same step then the last
parameter here is the name of the
container we want to run and you can see
we have two more parameters here the
first one is mandatory you need to
accept in the user License Agreement in
other case if you don't do not do that
so you're gonna receive this error so
you need to accept end user License
Agreement the second parameter is about
the memory restrictions and it's
necessary to specify this parameter on
especially on Windows 10 so if we go to
terminal you can see we have connection
already prepared and we can take this
URL we can go to browser you can
and we should be able to access the
container okay we can see the error
because we are using self signed
certificate one of the output here is
the user name and user password because
we haven't specified any authentication
methods so the container itself creates
for us one user with random password so
we need to take those credentials and
copy them into the opt indication screen
and we should be able to access nav we
wait for it to load that's the first
scenario that I talked about we didn't
specify anything on the networking side
so it just uses an internal IP as you've
seen here and we connect from from the
host itself to the machine that one now
isn't available outside of the host just
inside cool so that was the first very
simple run of an image and talker and
that was one of the scenarios that we
wanted to achieve with having Navin
darker that you should be able to run
that with the simplest commands of them
all and of course accepting the EULA
damn so how is the nav on darker image
actually created to be has talked about
the layering the Navin darker container
image this is based on Windows server
core it's actually based on a.net image
on top of Windows server core and on top
of that we install the prerequisites for
for nav sequel Express and IRS and then
we add some scripts this part of the
image is what we call the generic image
that's the same image that works from
Navi 16 RTM and until the Developer
Preview today and nav 2018 as well and
and that's the same base that's used for
so when Tobias downloaded a version of
2017 and 2016 all of this is the same
and that's the mature
of the package when you when you
download these images then the next
thing that happens is we add the parts
of the DVD only parts of it we don't add
the entire DVD and then we run the
install scripts so the install scripts
were added in the generic layer and then
after that we actually remove the DVD
again so you won't find the DVD in the
darker image you'll only find a running
NAB in that container this is what we
call the specific image this is a
version of NAB and you will all be
you'll be able to download that by
saying darker poll Microsoft Dynamics
NAV what version you want and a - and
then the release you want the release
would be the cumulative update or the
RTM or dev preview or whatever on top of
that of course the localization the
country database the specific image
would be W one without the conjugate
abase and then twenty more images would
be the localizations and there you would
have a naming strategy called saying
Dynamics NAV version release and then -
and then the country code on top of that
you could imagine that partners could
create their own images but we will talk
a lot about why it shouldn't be
necessary the problem with creating
images on top of our images would be
that you very quickly become like your
your image becomes stale right because
our images are updated every month with
the community update and I'll even talk
about an even more frequent way of
getting images from from an AV layer so
this is the format of our images and
actually you can you can omit the the
tak totally so if you say doc Apple
Microsoft Dynamics NAV and nothing you
just get the latest version of nav and
w-1 today that is 2017 see you twelve in
a few weeks from now that will be 2018
w1
that preview is actually out there as
well so if you want to run the developer
preview it is also under public docker
hub when you start a specific image you
saw some of this when when Tobias ran
the image and a moment ago it printed
out starting sequel server starting all
of these things so the the what happens
there is a number of things and and
please pay attention to the if necessary
here because it will only start the
sequel server if necessary the secret
service is installed and it's included
on the docker image but you can of
course use a sequel server that is not
that is that you can use as a sequel you
can use the sequel server on another
docker images you can use the sequel
server on the host and and if you're
using a different sequel server then of
course we're not going to start the
sequel so I mean it's not going to use
any memory or any any any CPU power on
the actual image when you're running
that same with the IRS you should
specify that you want to run the web
client on a different machine or you
want to not use the word plan at all
then we're not going to start the is
we're not going to create the
certificate if you have specified one
yourself we are going to reconfigure the
service here and start the service here
because that's kind of the entire
intention of the nav container setting
up web client file shares and setting
abusers is also optional and only P ran
if if actually necessary gives a picture
like this where you actually can run a
number of different images on the host
some of them only running nav some of
them running sequel server and nav and
end to web client and everything so one
of the the most frequent questions I get
is can I use my own database can I use
all of these things and yes you can
basically do everything and of course
there are a million ways to set up NAB
the million is probably even too too
small there are so many settings in that
and we have not just added all these
settings as parameters to talk a run
because then you're darker run statement
would
belike kilometers long instead of that
we've created a way of of extending
on-the-fly your container and I'm gonna
talk about that now some of the
scenarios we talked about and this is
where Jakob and Tobias was was very
helpful in the beginning of this project
was what are you using this for right
well how are using that and how how how
are you developing an app using
containers where you what you have now
and and to get kind of requirements in
on on all the different scenarios where
they use nav and and the last line was
kind of just stopped and said there's so
many different ways it's impossible for
me to to create configuration keys or
whatever for all of these things so what
we did was to create a extensible
foundation if we look at starting a
container everything happens in a in a
powershell script in the container
called nav start nav start will like
sequence a number of things like set up
variables set up database set up
configurations set up web client set up
web configuration all of these things
will be sequenced so it's calling a
number of scripts these scripts are
placed in the same folder as nav start
but before actually running that script
it looks whether there is a override of
that function in a my folder underneath
the run folder and if there is it's
going to invoke that script instead of
the original script in some situations
you want to invoke the default behavior
setup configuration is a good one you
want to involve the default behavior the
only thing you actually want is to
change a few settings maybe maximum
download size or whatever from your
service tier which we don't have a a
configuration key for so you can either
invoke the default behavior before or
after after after your custom code right
and there are a number of different
things that you could
you could override this example will
will set some some settings like yeah
this little buffer inside if you're
running that in a in the developer
environment right so this is just a part
of the setup configuration not a number
of these scripts are actually empty like
the additional setup is a script that is
called at the very very end when every
thing is set up it calls this function
and the function that is in run it's
just empty and will do nothing and that
is for you to override so that you can
do stuff like import users or oh yeah
register dll's that you've copied to the
the image or whatever all of this means
that you on the fly can add your scripts
and actually run them when you just
launch the container using the the
mapping that to be as talked about a
second ago you'll place your scripts in
a folder and share that to the container
in the my folder and then the container
when it runs will have your scripts
there and you'll be able to extend or
customize the container and everywhere
you want a number of the different
[Music]
extension points set up database add-ins
license variables web client and all
these things certificate is another one
and right now you actually cannot
specify your own certificate without
overriding it with a certificate script
maybe some of the things would be added
as parameters to the tag around maybe
not it depends on how many people using
these things and what the what the
requests are so next demo extending the
container
I don't think you're on can we get the
mic on so I can just talk is number
three on hello hello okay so the second
demo will be about the extending of all
the standard functionality you can see
that I have a sub folder here called my
in the docker run command I'm mapping
this con this folder in this line I'm
saying OK in docker take my my subfolder
and map the subfolder in to see run my
inside the container so at this moment
dr. Texas my folder copy the folder into
inside the container and we'll apply my
script I have in this subfolder so you
can see I have additional setup ps1 file
here and you can see I'm still coding
the basic the default behavior it's not
necessary in exactly in this case
because the original file is practically
empty but I'm doing it for best
practices and I'm calling here a
function called export client folder
this function is being implemented here
in this extension this is the second one
I'm extending helper functionality and
again on the beginning
I'm calling the standard behavior from
the standard image and I'm extending I'm
adding my custom functions and this is
the the function I'm being being called
for
additional asset over here so this
function specifically export my role
Tyler Windows client folder and copy it
into my host machine and additionally it
will in well create some a new excel
file that will allow me run
CSI directly from from this folder so we
have already started the container to
speed up the demo you can see I'm
already on I'm going to the folder you
can see that this folder has been
already created and you can see a new
file here fin fin sql1 docker dot excel
and actually this is PS script inside
wrap it as a EXIF file and has all
parameters necessary to point directly
to to the database so you can see i've
been able to enter directly to my
container which is called enough xed so
this was one of the possibilities how to
extend your or how to extend the
standard functionality you can for
example create you can for example use
the extensibility for creating or adding
your users from the domain to to the nav
or you can use practically anything else
that's it just maybe to add one thing
there as you saw Jakub was using the
standard behavior as well calling the
standard scripts but it also is
something that is optional i personally
haven't seen a use for where I just
completely removed the standard behavior
but extension mechanism works in a way
that if you know what you're doing and
you just want to do everything yourself
you could remove the
standard behavior as well by just not
calling the standard actually calling
setup certificate you don't want to call
the standard behavior yeah that's right
okay um building and reusing your own
images the next part now will be about
how you can use that for your intents
and purposes where it will help you with
problems that you might have today I
hope you have got an understanding of
what doctor does and how the knock on
door images work and now I'm gonna talk
a little bit a little bit about what we
solve with enough on docker and why we
probably looked at that in a very
beginning so the first one is building
and reusing your own images the problem
there is that you extended the standard
nav docker image maybe because you add
your own dll's you change a setting you
change a configuration you do whatever
you want to do and now you want to make
sure that that change is persisted and
it's doing the same across all
environments the reason for that might
be for us as a partner we want to make
sure that the changes that we make to
standard nav not inside of the four
files or the the CIL objects but the
changes that we make to the binaries to
the configurations the things we add
that that can be reliably deliver to
deliver to our customers and I guess the
same is true if you're running that for
yourself or if you're a holster and you
also might make changes to standard nav
or you might make changes to whatever a
partner provides to you and you want to
make sure that this is really persisted
and works the same all the time and
there then there is the so called
doesn't work here problem when you have
something that works on the developer
machine it works in your test
environment it works in your quality
assurance environment but for whatever
reason it breaks in your production
environment or it doesn't work at the
customer but it works in all of your
internal environments and that just
sucks the reason for for that is
oftentimes that is one simple
configuration that is different or they
using a different base Windows image or
for whatever reason a dotnet fix was
implemented on that framework fix was
implemented and update is there and it
just breaks or your developers are using
visual studios
they have some libraries that are just
not available in your running test
environment and all that can be solved
using the docker images because you are
absolutely sure that the docker image is
always the same if you push it to a
central registry you are absolutely sure
that the configuration is the same that
the binaries is the same the libraries
are the same and you don't have any
differences between them and that works
by just creating and reusing your own
images and there are a number of
different ways we just showed you how
you can extend this the standard images
to make the changes that you need and
then you do something that's called a
docker commit which means that you save
those changes for that you on windows
need to stop the container then you can
commit it and give it a tag so the the
versioning that freddie talked about and
you can add whatever is meaningful to
you a date stamp or a version or
whatever and that means that you now
have your own image and that image can
be referenced by the attack and if you
do a darker pull again to to load that
maybe to a different system then you're
able to reference it by the attack by
that label and get all the changes that
you need a mechanism to get this done on
different systems is a docker registry
there is a public talk registry where
you can get the the public images which
is called docker happened I think we're
going to talk about that a bit later but
you also have the opportunity to set up
your own private registry which means
that you are able to have your own
images stored in a central system in
your environment and on the different
different environments and Ivy
environments that you have like tests in
QA and production you just pull those
from your own registry and make sure
that you have your own images so it's a
two-step process you make the changes
you commit them you push them to the
registry on on the other on the other
environments you just pull and run them
sorry you might also be able to just
create your own docker file we have a
very good extend extensibility mechanism
inside of nav but if you're looking at
other other darker files or other darker
images then you might be forced to use
their their docker files and that
actually also
is kind of a good practice because you
you changed the recipe and then you're
also assured that the the template and
the image in the end looks the same
another problem that we can solve was
that of resource governance
I guess that a lot of you are in the
same boat as we are where because of
some problem in development being at
your own development or whatever you
have instances that just go crazy or
maybe a customer just called a bad
report with no filters at all and it
just blows up it uses all the CPU would
use uses all the memory and you get all
the problems that come from there maybe
your development your developers can't
work anymore your other customers that
are on the same host are impacted and
yeah you get a resource problem a
performance problem and all the
environments the so to speak brute force
solution for that would be to have
exactly one instance per virtual machine
but that also doesn't make too much
sense but it's a lot easier with
containers as we've seen before
you can have resource limits on those so
you can have any number of instances
that just work on your host machine and
you can tell every one of those that
they have to stay inside of their
resource limits that you can provide to
them so you make sure that you add those
resource limits is then running those
like I showed in the beginning only
two-horse only four gigabytes of memory
and they're not going to go over that
threshold but that you can make sure
that um not one of those instances is
impacting the whole host but they're
just staying inside of there inside of
the area and set inside of their limits
and if the main process which in our
case would be the nav server instance
it's an out of memory exception then it
also is automatically in started the
same as for the for the Windows service
itself in our case if the service if the
instance stops then the whole container
stops but docker also makes sure that it
restarts that again obviously the users
will lose their session but that's just
the way that nav works and but in the
end you afterwards have a instance
running and they can connect to that as
well and then there's something that's
called swarm mode where you're able to
do scale
were you able to do high-availability
that would mean that you can actually
run the same container on different
hosts for a number of instances and when
one of those containers fails because it
hit the memory limit or whatever then
all the others are there to just serve
you for your requests and the user
probably a lot of the users will not
even notice that there was a problem and
the third big one that was important for
us is running multi Cu environments the
problem there is probably also a lot of
you know or have hit that problem that
you can't run multiple accumulative
updates on the same release very well in
one machine there are solutions with
scripting and naming conventions that
make that work but it's not really a
good in clean solution we do have the
difference use that just reuse the same
files the same links so I can't very
well put them in the in the same place
and we don't have a solution for that
currently without docker we do have the
monthly C use as Freddy also mentioned
so that makes it a permanent problem if
you want to look at all the C use may be
on different release levels then you
have to put up a lot of different
virtual machines to really get that up
and running cleanly and you can again
automate a lot of that through
PowerShell but it's still a bit of a of
a hassle there from a customer or
hosting perspective you get enhancements
you get a solution for something that
that bothers you and then you see you
now you need to update your testing
machines your staging machine to your
production environments with the new C
use and it would be nice to just have
them run side by side so you can try
whatever you need and if you want to go
back you just switch off the new
container switch back on the old
container and you're up and running on
the old see you again and then there's
the case where I have parallel business
testing with C you testing like you
deliver a new solution to a customer
tell them to test and you also deliver
and you see you to them then you
probably don't want to mix those two up
because if something breaks and you get
a problem you don't know is it your new
implementation or is it then you see you
and with that solution you just have the
old solute see you with your new
solution and you have
then you see you with the old solution
and you can test both in the end you
will obviously test both together but
you also have an option to to separate
those from a partner perspective at
least for us we don't have all of our
customers on the same see you some of
them are using auto si use because they
didn't get to two updating them yet and
you have the problems you need to
reproduce those problems on the xxm see
you sometimes because it's only
happening exactly there and then you
have the case where you get a solution
for a fix and you need to test those as
well make sure that nothing's broken in
them um you also might have additional
problems it leases are in our case where
you deliver your own custom DLL maybe
more often than you deliver the see use
but then you'll also have different
environments with the same dll's or
different environments with difference
here less and you can also separate that
very well and cleanly using docker
images and in the end you have the
problem that sometimes the Cu
compatibility breaks so you can't
deliver a solution using an us-eu to an
environment with an older see you so you
really need to make sure that you're
delivering fixes and all the sea use and
deliver those to the customer on the
right see you and again you have a need
to have multi Cu environments what's the
solution for that again containers
because you can have them running
side-by-side as I said in the beginning
a container instance has its own
separate file system so you don't get
any conflicts with the nav server and
with the web client because that's all
running server-side we can have click
once clients for the Windows Server as
well as for the development environment
or can you can use the technique that
Jakob just showed by sharing that
environment to your host machine if
you're running in a distributed
environment and that doesn't really work
but if you're just talking about F
environments that also works very well
so with that you're able to develop
against those solutions you're able to
run against those solutions or that Cu
that you really need updating that again
is only a simple darker pool so you have
your your test environment you have your
Quality Assurance
you just do a rocker pool there of the
new CEO of the new version you have the
new one you run it you test it if you're
fine you keep it if not you just throw
it away and go back to the last one so
that really helps in running running
those multi Cu environments and those
were the three main topics I wanted to
talk about there's really a lot more
talking about darker especially around
continuous integration continuous
deployment a lot of those things also
work very well inside darker and have a
lot in in connection with the new
development environment as well but I
wanted to keep it at that level and will
now see how running those multi Cu
environments actually works facing the
problems with running many customers
with different see you so for me this
example is one of the the best one we
have in this example we are running two
different CEOs of 2017 we are running c6
and c7 so we have already started two
containers the containers are already on
we are using click once to publish the
package into the host machine so we have
already to speed em again we have
already downloaded this image this
packets and I can show you that here I'm
going through an AV I will be able to
see that I have two different instances
each one with the different built number
this is 16 996 and the second one is 16
five eight five so you can practically
run to different three different
different versions and for each version
on the same host you can run unlimited
number of different Co so from this
perspective docker I think it's really
terrific tool and platform cool so what
you've seen in until now is the number
of ways to run like docker run you can
in and that's what I call the raw making
mechanism of running docker images you
need to go to a command prompt you need
to run these things you can do it from
powershell yes but of course there are
it's possible to automate some of these
things it's possible to do things easier
and for that we've created some some
powershell scripts that makes life
easier when run working with nav
containers not surprisingly it's called
the nav container helper and it's an
open source project and github so go to
github.com slash Microsoft nav container
helper and you'll find a partial library
that that you can download and start
using these high-level commands which
makes it way easier to run with nav
containers so I'm going to demo some of
these here and actually you don't have
to download the PowerShell script you
can also take it from the powershift
gallery so just go in and and say
install install module and I've
contained a helper and then you'll get
the nav container some of the
Commandant's in that one new nav
container guess what it does create a
new nav container and then there are
high-level commands like convert
modified objects to Al that's a nice one
I'll show you that in a second let's go
to on this machine actually to
powershell here and have a look at how
this module looks so
really installed the module here it
really it's really Jun just by this
single line install module nav contain a
helper force that downloads it from the
powershell gallery and here are all the
functions that are available in the nav
container help us so there's number
functions on that can give you
information about the container that's
running or or the container images yes
container handling functions that's
object handling functions which are
specifically nice if you're working with
with with v1 extensions and want to
convert them to v2 app handling
functions for publishing and
unpublishing and installing and
uninstalling apps v2 extensions or
actually b1 and then a Asha VM specific
function for when when you're running
this inside the Asha p.m. when you're
running the nav Developer Preview it
actually starts up an Asha BM downloads
this module and runs the nav container
helper new nav container in that one and
creates the container using that
functionality and that's where if you
have a an Asha and you are you have
maybe polluted the database inside of
the container
you just want replaced nav so have a
container and it creates a new container
for you and you are up running as if the
machine was brand new let's have a look
at some of these things so I will first
of all run this section and talk about
it afterwards so it is going to ask me
for a password and that's the get
credential so it gets my credentials and
toss them in a safe way in memory and
actually the new nav container will
transfer these credentials in a safe way
to the container and remove the key file
that it can it used to transfer the
credential to the container so nobody
can can grab your domain password out of
the container afterwards and that is a
little hard to do if you are not using
PowerShell because you need to create a
key and you need to
your password with that key and
copy that to the container and remove
the key again so that all happened
automatically in the new nav container
when you're running a new knife
container talks about it tells you what
what version it is and what what generic
tag there isn't that version and then it
tells you that it shouldn't take more
than a few minutes to complete that one
yeah thanks
we've seen a lot of feedback around
those on github repository but Freddy
will also show later and it also
definitely makes a lot of sense if you
just show exactly what you're doing
there so show the output show the
commands that you were running then it's
a lot easier to help but some people
have posted issues this and that is not
running without giving any feedback and
if you just post that output tell us
what version you you you were using and
how you ran those scripts then it's a
lot easier to help yeah so that output
is not this that is the output I'm gonna
show here so now we're running one
container
it's called test one and I can get the
locks from this one by saying toggle
locks
test one and it's going to show all the
output that actually was shown when you
coop did the docker run a moment ago so
this is one of the important outputs
that we want if there are
troubleshooting issues the other
important one would be the darker
inspect of the container which talks
about again you are your network up
settings your labels here what what was
used in order to start this one and your
environment variables here I can have a
look at top PS see what images I have
running here I have one running that's
the test one I can go darker images and
see what images I have on this machine
and as you can see I have a lot but they
are only taking up very limited amount
of space on my hard drive even though
they seem to all be 15 gigabytes then
most of the things that are in these
images are actually shared as Tobias
talked about earlier
so it started my test one container here
and I should be able to start the
development environment and actually
then one of the things that the new nav
container does is it see if I can get to
my desktop I'll have to it creates some
shortcuts on your desktop so you will
actually have a test one seaside here I
can double click that one and get right
into my seaside and I'm now connected to
the sequel server inside of my container
and as you can see if I go all here
modify the objects of seven yes nothing
has changed in this one I will run a
PowerShell command that's called import
objects to nav container guess what it
does it imports objects to my nav
container now it's done so I'll go in
here and refresh and let's see view
refresh and now I have two objects that
have changed so I just imported to that
that from a text file and I'll modify
some more let's go in here and go to the
beginning find my customer table and add
a field and 50,100 test so now I've done
a modification to the databases well
saved it and I have three objects two
that are added and one that have changed
let me then try to go back here and have
a look at what does export modified
objects as Delta's - that's kind of hard
to guess right here get a I actually
asked it to open the folder with the
open folder switch and it opens the
folder with two text files and a delta
file and that is your tells us it is
still in the old syntax because I didn't
specify that I wanted to have it as new
syntax I can do that by simply
specifying
- use new syntax and then I'll get it in
new syntax should I try that you should
never change the demos while running on
stage but let's try I'm pretty sure
it'll work now this is a new syntax and
actually there's no much difference
there but I will be able to see the
difference if I go into these things and
see the date and time I - leave now in
the new format more interesting is it
probably to be able to convert that then
to al so convert modified objects - al
that's exactly what the name says
converts all the modified objects in
that container to Al and puts it in the
folder for you and you can take that
folder and move to Visual Studio code
and start developing they're all you can
find if there are a lot of errors in the
conversion process or errors in Al and
then go back and modify them in v1
before you actually do the
transformation - al it's a one step
process to take everything you have in
that container and make al out of that
of course behind the scenes it uses the
text - al that s been showed and the
very first day of this you studio code
and and so there's nothing here except
for grabbing all the functionality that
isn't the platform and making it easier
to call so it creates the deltas and do
all of these things to make it easier to
run
you can stop containers you can start
containers and all of these things and
you can start up multiple containers one
of the things I wanted to show here is
this thing with in the good old days
where you whenever there's new see you
you would have to download the sea you
have to put it in a repository somewhere
you had to install it on some machine
the ease of which to run different
containers is the difference is just a
string right if you want to run 2016 you
write 2016 if you want to want 2017 see
you 8dk that's what you write and
everything is is included in that spring
you will get that image you get you'll
be running that in a container
I can start all of these if I want to
but I don't think there's any reason for
that I want you to bring your attention
to this one so this one says docker pool
net insider
- Asiya IO Dynamics NAV daily now the
insider program I'm going to touch upon
that a little later
is when you are an app developer and you
are registered for the insider program
you would actually be able to have daily
builds of nav right there on darker and
then some of the things that I that that
you'll be able to do with that is to
make sure that your application is not
broken right you will get a built in a
month or two months from now and you're
gonna merge you're gonna try your
application you'll see that oh something
was changed and my application is now
broken in the next session is in this
room is John claims and Eunice they're
going to show you the github
integration where you will do source
code control of your application and
actually do automated daily daily builds
of your solution so whenever somebody
check something in it's going to move to
a machine that builds this and it can
actually just automatically download
from darker the latest built and you'll
be sure that you didn't break anything
and Microsoft didn't break anything
right so you will know every day whether
there's something that is broken not in
half a year from now where everybody
forgot what the heck we did have a year
ago so I think that's a very nice thing
I'm not going to start a lot of these
containers I think we will continue here
and talking about
oh that's not what I wanted
sorry about that I just keep it here
let's go to the next one so I was Adam
often half container however now
container helper is an open-source
project so I urge you to have a look try
it out if you have something that you
think oh this should be done in a
different way or whatever feel free to
submit a pull request and we'll have a
look at that it's really a tool which is
intended to help you guys it's not
intended to yeah it's it's really
intended for people working with
containers to have it as easy as
possible so please help us make it
easier for you guys
so what are we shipping and so right now
every cumulative update of NAV 2016 and
2017 on-prem are also on darker so they
are also on MSDN you can download the
DVDs but there are darker images out
there that is 25 cumulative updates 26
actually of 2070 2016 and 13 of 2017 RTM
to see you twelve that is a total of
approximately 800 images that are there
because we have twenty localizations for
each image and they're just they're
ready to download the reason for this is
of course as a coupon to be as I talked
about if you need a specific see you
because that's what your customers
running then it's just easy to get and
you can just say docker run that one
it's also for our CSS guys so whenever
somebody reports an error in 2016 cu5
they would spend a day of actually
downloading that one and setting up a
machine and installing everything to be
able to to to to do a retro of that park
today
it's a minute or two and they are
running with that community update and
connectedly start referring the bug soon
of course 2018 and Prem will also be on
the docker
important to realize it is at this time
support for tests and development it is
not intended for production purposes at
some point in time I think we will
support production environments as well
but that is not supportive that's not
intended for that and support for that
purpose now so the images that we have
on Asha we have a Asha demo environments
we have financial sandbox environments
and then to Developer Preview actually
developer preview is there now okay yeah
so the Developer Preview and the
workshop VMs are on darker now and they
are only on darker you won't be able to
get the Developer Preview on DVDs and
you won't in the future either soon we
will take the demo environments and the
financial sandbox and move that to
darker as well and remove the images
that we have on inertia the image that
spins up when you create the development
environment or the Developer Preview or
the workshops this is not an image we've
created we're just spinning up a
standard and have Windows 2016 with
containers that's an image from Asha and
then we are install we are we are
running a docker container on that one
so take some minutes but but it makes it
much easier for us because we don't have
to maintain images with a lot of
different stuff on it and we assure that
you always get the latest version of
everything if you spin it up anyway
workshop VMs
that's what Freddy uses Microsoft uses
for their workshops at directions for
example or here
but you can also use them for your
internal purposes because they are now
openly available for example we have a
couple of customers over every time we
release a new version a new major
version and have them test and that also
used to be quite a pain to set up those
environments and with those scripts and
and the template that you have there you
can very easily spin up multiple even up
to a couple of hundred VMs on Azure
which with exactly that see you that you
need that version that you need fully
automated and then you
ready to do the workshop the testing or
whatever you need yep going forward we
will be going into a like three ring
release cycle here so stable like yeah
if you've seen Visual Studio code you
know that you can go to visual studio
code and run the insider pill so you can
run the stable bills one is what shipped
and one is what what is kind of their
daily builds we're not going to put
daily bills out there for everyone we're
gonna put daily bills out there for our
partners who have a relationship with us
in what our developer programs the
stable ring is also on tarkir its
releases its cumulative updates is the
current SAS pills and stuff like that
you'll be able to find the current
hospitals of course on yeah online and
you'll be able to run the releases or
download the release and the cumulative
updates from from MSDN or run them from
darker whenever we are talking about
insider builds meaning like daily builds
or bi-weekly builds or monthly bills
will have two rings there will have one
ring which we call the the SAS preview
that is the version that we're going to
publish to our SAS service the next time
so our partners can actually get the
built that will be published in within
the next month through our service and
and make sure that they they have
everything there and partners will also
be able to run of download and use daily
builds of course with the caveat that
things can be broken and stuff like that
but yeah that is something that we would
like to hear also if things will be
broken of course that's the
communication on new builds and stuff
like that will be on the team block
collaboration and get up the nav doctor
in a repository on github is where the
sources for the generic image and that's
where you issues are reported and issues
are resolved
documentation will be on MSDN and and
unblocks i have posted a number of
blocks on trying to document all of
these things and my next topic to
document this then I have container
helper and I'll be going through a lot
of that over the next few weeks or so so
I think the next thing here would be
questions unless you guys have any more
to know
where do we have the t-shirts
okay so I have a question what about all
the nav builds is it even possible to
run them on docker
and maybe have some recommendations how
to do that mm yeah mm 30 2013 2 for
example yeah so 2013 r2 and 2015 we did
not include those in the docker images
because they are significantly different
from 2016 to install we are definitely
not going to do 2013 are too because
that's out of support in in very short
time we might be looking at 2015 if the
if if the request is big enough what I
support when I started off I tried to
install 2013 r2 and there are a couple
of things there where you would need to
do really ugly stuff that you actually
don't want to do and definitely would
want to do in production but I think you
should be able to get your own images
nas build on this but really your own
images for development and testing
purpose that should be possible when I
started we had a github repository which
was different than what Microsoft data
and you could check there how we
implemented things back then
use the installer we did a couple of
tricks to get it up and running and you
should be able to use that if you go to
your coops github repository which was
also on the slide you should CDC that as
well if you want to use it in develop an
environment and also for automated
testing as the server core is headless
have you run in any issues because if we
want to also test against third-party
solutions or our own develop stuff so
what we that we can run the installer
fully automated through PowerShell are
there any issues that you run into or
that you had some software installed us
where yeah which could not be automated
like this yeah there are a couple of
things that just are not possible if you
don't have a GUI I haven't seen anything
that should work on a server side but if
you're talking automated testing you
might want to do some of the things that
are actually on a client side inside of
the container and that might be
problematic so you could look into
having the client side still as a
traditional client and just spin up the
containers to e-stat but if you'll it's
more that we need some windows services
which where we don't talk to through web
service ok so if you talk into something
completely different and you need to
look into if windows server core
supports that and I personally haven't
seen anything that's not supported or
that that doesn't work yet the issues
only are if you really need a client and
a GUI for a client then you have a
problem but if it's running on the
server side if it's a service then it
they're good chances that it works not
everything works but a lot of it can I
choose can I choose my own SQL server or
when installing docker for multiple
docker images can I use my own SQL
server instead of using SQL Express yes
yeah it's just a parameter when you when
you start a docker container you tell it
that you want to use that server you
want to use that instance you want to
use that database and then the container
just connects to that you have to think
about how authentication works so how do
you authenticate the container the nav
server instance inside the container to
the sequel server are you going to use
Windows accounts then that's
but more that you need to do or are you
using database equal database accounts
then it's actually quite easy to do when
you used like doc or a daily update in
that case it will automatically update
that SQL Server also like image say it
again please
okay when you when you use a doc refresh
like image refresh like that time if
suppose Microsoft added few more tables
are objects to the image then it will
automatically update to your restless or
a result no if you were installing an
app service G and connecting to the
database there's no magic there it's the
same same scenario right what it brings
it brings the new the new database
inside the container so if you're using
the one inside you don't have the
problem but if you're using your
separate then for for intent of the of
the sequel server the nav server
instance inside of docker is just the
same as any other nav server instance
that's running outside of a docker image
is it possible to use existing sequel
server installation with docker
container that wasn't that the same
question okay another one sorry is it
possible to use is it possible that
helps the phone station when multiple
docker containers use the say use the
same database again that's exactly the
same as if you're using any V instances
outside of talker it's just an five
instances running inside or outside of
docker connected to the same database so
you see the same issues does it see
outside and it's perfectly possible yes
what about resources for example
printers and all of that should be
handled client-side because again you
don't have a GUI to connect to so I at
least I personally wouldn't know how to
set up a printer in Windows server core
if you want to do service are printing
then you should probably look into
having a PDF and sending that out but
you you can't connect to
yeah I can click darkly yes you should
you should really see this as an as a
nav service tier running isolated that
is what it is right and and then we have
added the sequel server and stuff like
that in order to make it easier to spin
up something so we've included
everything there but but in this in the
essence it is just an isolated service
so exactly the same scenario if you were
able to to install five different
services on the same box side-by-side
and they were not touching each other
that's what happens okay thank you you
told that it's still not useful for
production is that still far away for
production or is it something what is in
nearest future
I cannot say when or if or how we're
going to support for production I can
say that we're looking at it but that
we've shipped this three weeks ago and
and I think we want to make sure that we
have tested it thoroughly before we put
customers on on running this but you
will sure that it will come I think I
said that I'm not sure that that it will
come but we are definitely working in
that direction and if the demand is
there and and we find that we don't have
any issues and I can't see any reason
why not it is basically supporting
Windows server core is the basic
operating system we need to support and
and now we are able to test it so now
we're able to true to do the testing if
we do then my assumption would be that
will be around tenerife timeframe but I
don't know
hello cannot tell few words about
multi-tenancy yeah so right now the
Dockery mr. Singh lieutenant but
basically it is just changing a setting
inside the container and that is one of
the topic that is on my list of things
to add multi-tenancy so if actually if
you have a database that's outside the
container it is just changing the
multi-tenancy flag and then you are
running multi-tenancy as well the thing
that that requires a little live is if
you want to run the entire demo
environment inside the container with
the inside sequel server in
multi-tenancy let me try some scripting
and I'm not sure I don't know if it's
worth doing or not it's kind of up in
the air extensions coming up into the
2017 or 2018 can I include the
extensions into my docker image and then
probably ship it over to some other test
environment alongside with the
extensions so that I don't have to use
the extensions or rebuild extensions
again yes you can yeah okay using this
currently for is for the development of
our own first extension and this is
built completely on container so I've
never run our extension in a traditional
nav server instance and it works
absolutely fine okay thanks
Thanks
what about performance is the enough on
a docker hosted on docker is working
same as the nav on a rough machine
absolutely I haven't seen any
differences at all I didn't run any
performance testing on it but
conceptionally it's just the the process
is using the the host environment
actually if you if your are on the
docker host and look into the running
tasks then you can see the Microsoft
Dynamics NAV dot server dot access so it
really is using the CPU and the the
memory and the file system the same so I
didn't see anything and I wouldn't know
why it should be any different than
installing it natively ok cool exist I
might be ok because you're using yeah
yes because we used the s4 Express right
yes the solution to that is of course
yeah I think the Microsoft sequel
Express inside the container will only
be used for demo purposes and all if
you're developing v2 extensions where
you really just need a container in
order to be able to publish your
extension and run it so there you just
need this container for for for having a
testbed of your solution and you're
using Visual Studio code maybe on your
laptop and then publishing to your local
container and you can do that in the
plane on the way home from wherever you
are and and still be able to develop
your v2 extension and never get a
minutes of sleep anymore yes thank you
very much
sequel server in the container that's
used more widely there are more people
who already are using sequel server and
there are a number of blocks and people
out there who are talking about sequel
server performance in a container and
these at least as far as I've seen they
come to the same conclusion that sequel
server behaves just the same you need to
think about why your sequel server is
not performing if it's not but it
doesn't matter if you're running it
natively or if you're running it in a
container
I have a question down here as well I
have two questions actually one is is
the test toolkit and test libraries
available in the standard docker images
itself without the need to download the
DVDs and another question is how does
the monitoring of the docker work do we
have something like even viewer in dark
you know so the first question I can
take that that's something we're looking
at I got that feedback from a few other
guys you have the MVPs actually asked me
for that so we'll be looking at
including those as part of the build so
that the tests are there on the
monitoring I don't know what you have
yeah experience you can one that's how
you can use the standard mechanisms that
you have in in Windows Server like the
performance counters they should be
possible in the near future they're not
there yet but you can in the future and
then also there's interesting stuff that
you can do around monitoring your darker
environment and that is basically two
things you can look at how much
resources being at CPU memory or i/o is
the container using and you can also
look into the container to use that
performance counters and there are tools
like Prometheus or Graf Amma to give you
a nice dashboard of what actually is
running so it's interesting as soon as
you're looking into the darker world
then the same problems that we have
around nav and sequel or the same things
that we want to solve you now see in a
really wide world where people are doing
a lot of stuff with docker and they have
the same problems and you can just reuse
their solutions so what I'm currently
working on and hope to be able to
publish on my blog in the next few days
is to do exactly that how do you monitor
a container environment containerized
nav environment with something that's
regular in the open source outside of
Microsoft world so it's gonna show you
how you can use those tools Prometheus
and Cortana to get a nice dashboard
around that performance and my point
basically there is if you go into the
darker world then a whole new world of
tools that are already there a very
strong open source world opens up and
you can use that to manage and handle
your nav
sequel installation hey you mentioned
that house platform of choice is a
Windows server and that's something
about Windows 10 as a platform okay you
tell me can I use Windows 10 as a host
platform for docker and so it works with
Windows 10 as well but when there's 10
always run with the hypervisor so you
have to isolation mechanisms for
container 1 is process isolation which
is what Windows server does it allows
you to share all the resources of the of
the hosts that you're so here in Windows
10 it will pre allocate some memory and
actually run up like a small VM a very
lightweight PM but it will pre allocate
the 4 gigabyte that you gave it so
you'll only be able to run three
machines on a 16 gigabyte machine right
we're on a Windows Server I could easily
start up eight containers without any
problem because they'll be using the
exact amount of memory that the service
T is using and nothing more
okay so it's only resource limit yeah
Windows Server is just better at but the
version of of tarkir that is included in
Windows Server is the Enterprise Edition
and what you can get for free for
Windows 10 is the Community Edition and
that's the big difference thank you I've
seen more funny stuff in a Windows 10
environment where you have to dig deeper
and find problems that are kind of
uncommon that might be because then
those tend tends to be the laptop
someone uses and they mess up things in
Windows Server it's maybe more central
and more more controlled and also it
might be because docker is just not
working as well on Windows 10 I'm not
sure leading into the first direction
but I'm not sure so just from my
experience it's very very stable on a
Windows Server I haven't seen almost any
funny things there on in Windows 10
there are some head scratchers where you
need to invest a couple of times a
couple of hours to get to the bottom of
that and then it works again it's just a
bit more effort so it's just like yeah
it's a lot easier if you if you run it
on Windows server but it perfectly will
run and will work on Windows 10 as well
in volute n I think the primary usage
there would be for the developer using
business to geocode and actually just
want to run your code your tests your
your your app to what say running
serviced here and there it's perfect
because you only have one and then you
replace that with a new one whenever you
get a new version of so you can have
many containers on your machine and you
can go stopping and starting them so
it's another option is it possible to
run on a notebook virtual machine with
the server and then docker on it
ooh too complicated it actually does
work we do a lot of that in exactly that
scenario it's just you need to have
something that's called nested
virtualization and then it works
completely fine so it might be an
additional setup that you have to make
on your laptop but it absolutely will
work so we have a question down here you
just charge your question and we'll
repeat it if when I'm running into
issues as docker is no Microsoft product
and for example my containers do not
start up it's always crashing with some
arrows do I create github issues in this
case on on your side of Microsoft or is
there any community or do I need to use
the the docker community for it for the
questions or how do I proceed with
issues issues it depends on who's to
blame no I
No so you can always try it at the the
Microsoft or Casa max left nav docker
I've created blog post called
troubleshooting nav and darker which is
a 15 item list and that those 15 items
every single issue we've had that were
related to to nav on docker is explained
there how to solve them and if we hear
more we'll add 2 to that troubleshooting
this is probably kind of gonna be on on
talks as well or something like that so
for now please put them on github issues
NAB darker or and I have container
helper if it's if you're using the NAP
container helper and then we'll look
into that and help you ok Microsoft
support channels for a problem we had
with the container and the first
feedback I would guess by 1st level
support was not so encouraging because
that guy definitely haven't heard of
containers before but after I got over
that hurdle and that went very very
quickly then I think there's a lot of
interest in in Microsoft as well by
second third level support or even the
development teams who want to look into
that and want to understand how people
are using that and what problems are
there so the first impression might not
be that good but if you get over that
hurdle then there's definitely a lot of
good feedback and an interest in helping
you to solve through the official
Microsoft support channels as well and
then there's the you talker community
they just tend to be like 90% on Linux
because it's a lot older there and then
you have the 10% of Windows guys who are
also in my experience very open and very
fast to help
do you need to install windows updates
on a container so yeah the windows
server core is updated every month as
well and when you're running the nav
container you'll actually get a warning
or an error if you're running and I've
container that is more than 90 days old
you can start the container with the -
accept outdated and and you will accept
that you're running an outdated
container but we'll update we will
encourage you to run the latest and that
will include the updates of course and
then you wouldn't be in that situation
but yes you can you can download and
install updates on a running container
if you want to typically if you're
running Windows Server the the layer the
Windows server call a used there is
actually the majority of that it's just
yeah interfacing to your host operating
system it's really not using that that
layer so it's not necessary to to have
as many updates to that you're updating
your host and that will be updating the
majority of the vulnerabilities that are
there but yes there are takes to Windows
Server Co as well and they immensely
like they are with Windows so what we
encourage you to do is always to use the
latest image from from us and that will
be updated and then you'll be safe ok
thank you you can have the latest image
but there's an old see you
so you're on for example see you five
but your monthly updating see you five
and then you get a monthly fixes we're
actually not gonna monthly update all
see use oh okay
so I take that back sry no running
running an update of old old cumulative
updates or something we are yeah we
don't know if we're gonna do that but
I'm not gonna promise it here okay
any more questions we have one there
hello
are you're in extension examples
available to download
I like the dev environment is that
available to download from your website
or from today's demonstration I got to
save time rather than reworking what
you've already done
yeah I would very much encourage you to
go to Jakob sceeto everything Satori
that you see there
um it's having a lot of examples there
that make make a lot of sense and we'll
have you saved a lot of time there
because he's doing in my opinion the the
most common examples that you would need
to do and if you have further questions
don't just drop us a note might look
into that as well and I could offer it
on my blog or a coupon on the on the
repository okay thank you
yeah so everything you've seen on stage
today is available either on yeah blocks
and the nav container hello of course
okay think that was it thanks for
joining
