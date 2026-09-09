# "When a dream comes true" aka NuGetized Business Central

- **Source:** https://www.youtube.com/watch?v=JpmPqDM-hzU
- **Video ID:** JpmPqDM-hzU
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 90m29s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

I'm camil saek I'm product development
manager in natica company in from buno
Czech Republic and I am MVP for 19 years
already my name is Freddy Christensen
I'm a technical evangelist working at
Microsoft in in lungu uh not an MVP so
EnV at Camille but I've been lucky
enough to work on a lot of cool stuff
over the the last many years and uh Nate
is is one of the things I've been
working on so take it away okay what we
will talk about today that's uh the
agenda for today uh yep sorry r2d to
play it with my slides there is a
translation for you uh we will talk
about the dream we will talk about what
this new new get uh how it works uh and
about some Basics we need to incorporate
into the produ uh into our process is to
support usage of the new get in our our
development work and cic CDs and
everything we will mention even the
problem of the runtime packages and what
is runtime package and why we use are
using them and what is the special
things on on them uh in in uh connection
with newat and of course we will show
you how you can uh work with new get uh
for example through BC container Helper
and Al go for GitHub and we will give
some uh advice for you when you came
back uh and you will speak about new get
with your uh managers or someone uh why
you should uh use them okay first about
the
dream the dream just try to
imagine business Central
Development without using
Al download
symbol yeah because what you are doing
now you you want to develop something
and you you create the app and now you
need to download the symbols to download
the symbols you need environment first
yeah but you have you need to have
environment of correct version of course
you need environment with all the
dependencies you want to use in your app
and you need maybe some some
applications or at least symbols from
third parties if you are building on top
of work of some other partner for
example and this is this is a problem
because uh it delays the start of the
development I can't just for example if
I need to fix one line in my code or a
code of someone else and compile it and
and push to the to the G repository and
fire the pipelines I can't without
downloading the symbols it means I need
first the environment
why and of course it's possible to to do
like to work like that and it's possible
thanks to the uh nuget tool and we will
talk about that
now and short demo how it looks when you
are not not using the download
symbols I will show you the example I
will go to the vs code oh sorry again
R2D2 sometimes plays with my vs code I
will need to clean up he like the clippy
and and cats and everything that's okay
close
that I have a clean application there is
no
uh there is no dependent
yet uh I have only some name and and
platform version and application version
and of course the hello word and I want
to start to to
develop I do the magic without
downloading the symbols having any
environment somewhere running to
download them and you see that when the
magic uh stops I have in my Al packages
folder the symbols I need to
work it was fast and if I decided okay I
don't want to work with 23.2 but 23.1
for example I can change that random
magic and in while I have symbols for
23.1 no problem and we are happy we can
develop we can compile and everything of
course if I want to publish and test it
I will needs the the environment but
that's another
story that that looked pretty cool I
mean why are we having a session it
looks like you're done already
yeah it is working it is working even
because you already spent some time on
that to be able to do that but of course
we are not there yet so Camille reached
out or Yeah we actually had a lot of
discussions going on on nouet over some
time
uh but we actually did
investigate other options
like in both as devops and in uh in
GitHub you have a lot of different
packaging mechanisms like jams Maven
cond Gradle and so on and so forth and
they are all for for different like npm
for JavaScript and I can't even remember
what they all are but nouet is for net
packages um and we've very quickly came
to the conclusion that either univers IV
packages are n get are the ones that we
would use for this purpose Universal
packages doesn't really provide anything
it is just like binary files in a in a
storage and then Universal packages
cannot be anonymous so that one is out
and that leaves nougat nougat isn't
perfect but it actually solves the
problems and and and by doing some magic
around stuff which is what we're going
to talk about for the next 83 minutes
and 31 seconds
um is like what is nugat how many people
here know like in details what nougat is
mean quite a few that's good it is so I
actually when I I I still say net it's
nuget but it it's pronounced nuget they
say uh you pronounce it correctly I
don't um it is a package manager really
designed to for for net to to distribute
packages um yeah centrally or or on your
own file system uh in in what is it
under the hood it is just a zip file
with an extension called M
kg and when you unzip that there's a
manifest inside of that one and the
files that you want other people to use
and then the the magic comes from like
when people get your package like vs
code uses Ned Visual Studio uses new get
um and why not also business Central so
if we put some logic into the newat
packages then we can use the
distribution model uh either from from
newat servers or you could download
stuff and put them on your your local
file shares and stuff like
that
um yeah short demo how it can looks
like uh AB
it's very easy to create uh new get
package uh what you need you you need
only some new speec file which is XML
file and it's very easy to generate that
for your
application because you need only the ID
of the package the version you are
creating title description outs and
other things there are some optional
things you can include your license URL
or or anything what is supported and you
will put some dependencies metadata it
means on which other apps your app is
depending and which versions and you
will somehow uh reference your up file
which should be part of the of the
package I just prepared uh three
versions of my app here or or new new
spec files for for this all is uh same
uh application just different versions
and I will create uh the package I will
show you
the uh command file which I will use I
am using standard new get tool which is
uh free for for usage and I will need
first to go to the correct directory
sorry um
and do
the magic again create P now it's
creating
the net packages for me you see this
these three files here uh of course they
are binary because they are zip files
but part of the process what I did was
even uh push these these uh packages to
some storage in this case the storage is
just just local file system you can see
that it's just just folder uh on on my
disk that could be still source for your
packages and I will show you how how
this storage looks
like uh that's the storage there is a ID
of the of the package and subfolders are
versions of the
packages and you have metadata and other
information other files from the package
aail available and the package itself
with the app inside yeah that's that's
uh one possibility how you can
distribute your your packages but of
course it's not what we will use uh for
BC mostly but it's really really easy to
generate the the
net how it should work when you are
consuming the package you want to use it
someone created it put it somewhere to
some sources we will talk about the
possible sources later uh and you want
to consume it what we need for that
first we need the upjs because inside
there there are the data we need to
create everything to ask for the correct
uh nouet package and uh consume that
that package
later put the ab Json to the mixer we
will add some list of sources from where
we will download this this packages we
will mix it oh sorry yeah Mr y just uh
remembered me that we forgot to put some
spice into that mix mixture we need some
rules we use during that that process we
put the rules inside mix it and we will
receive some n get packages we will use
for development when we look into these
packages of course there are the app
files and we will use app file files as
a symbols or or uh applications we will
publish to our environments yeah the
process is easy but it is about
transforming data and to be able to
transform something we need the
transformation rules it means uh if I
have up Json and there is some
dependency I need to be able to generate
the correct package
ID which I will
download I need some sources of the new
new get packages of course we will talk
about that and we need to somehow be
sure that we download the correct
versions of the uh packages because not
every time I want the latest or or
lowest version or something like that
yeah and of course uh we need somehow uh
download them uh the
result uh as I mentioned some times I
need highest version sometimes I need
lowest version uh if you will use some
tool check that this tool is supporting
something like that because uh it will
helps you to have a
correct uh result for your your
development and as I mentioned earlier
we did have quite a few discussions U
about naming right it's always like that
if you need a name for something uh
people have opinions and we had a lot of
people with different opinions uh in the
beginning I thought that why don't we
just use the app ID I mean that it's
like um it's the only thing that is
unique for the app why don't we just use
that um but but rightfully so people
told me that we need to be able to
actually look at the ID and see what uh
what it is and and not having to
like take the app ID and put in into a
search machine to figure out what what
what is this app so we ended up with the
naming being publisher. name. app ID
that is a long name because the ab ID
itself takes a lot of characters and
there's a tag in between that tag can be
a runtime it can be a localization tag
it can be symbols like if you're
downloading a package that only contains
symbols then that
says do symbols. ab ID and this this ID
must be unique yeah it can't be reused
by something else even when it will be
on different Source because everything
is maybe cached locally and if you wants
download the uh the package with some ID
and version from One Source it can't be
different content if you download it
from another source it can't be yeah it
must be still same content if it have
same ID on version which immediately
makes somebody think that's why they put
the tag there because the base app
exists in a number of different
localization and it has the same app ID
so uh we kind of had to do that one we
dislike it but uh yeah we have to do it
um the content again disagreement I
thought it would be a good idea to be
able to have like a number of apps in a
package so that if you download a
package you could like find all the apps
that uh an app would like have a
dependency on uh if if that was the only
one but uh I got convinced other people
told me nope one app per package and one
app per package is our
recommendation the dependencies we need
a full list of dependencies on again
same naming algorithm publisher name tag
and ab ID and obviously the version
number comes as a dimension to that in
um
net and for search and
resolution I in container hel and in go
for GitHub only use the app ID which is
what appsource does right appsource only
searches for the app ID and then it
finds the right version of that for
nuget and packet apps that camil is
using he's using the full package ID and
version for for that it have some
downside that if some partner rename the
application or change the
publisher uh the package resolution
could fail because that but for me uh
it's not a problem because mostly we
want to know about such as changes we
need to to change our up Json to have
correct publisher and correct
application name and everything will
will work again uh that's
okay that's accept uh for me it's it's
uh something I can accept uh and when
using standard tools yeah they will
still work I need just uh think about
these
possible breaking changes from from
other
partners and for runtime packages we're
going to cover runtime packages later in
the in the session uh we found out that
the only reason uh the only way to make
this work is to have an empty n get
package and then really put the app file
in a referenced dependency to that new
get package but much more about that
later
um yeah some rules Max one app file per
package uh something about the ID a
maximum of 100
characters uh the the naming the the the
the way that we calculate the name is by
if if the publisher and the ab ID and
the the the name of the app is longer
than 100 characters we will cut from the
app name so we'll keep the publisher and
we'll keep the app ID because we all use
the app ID for for uh finding the right
package and we we're going to normalize
the publisher and the app name so we're
going to remove everything that is not a
toz and A to Z capitalized 0 to9 or it's
not an underscore or a minus so it's not
quite net namespace because we include
the
minus uh but else it's the same as it's
it's more readable I think how long is
the the GD 42 characters 42 characters
if if you remove that from the 100 and
you you can imagine for example
publisher having 60 characters in some
cases or more I already noticed
something like that somewhere uh there
is maybe few characters for the up
name uh don't don't don't uh please use
too long Publishers and too long
application names because there you will
have a problem with that and not only
for the 100 limit here but we will see
the other
limitations in just a while we do
support full 4 digit uh version numbers
like major minor uh build and revision
and we also support uh like pre-release
suffixes like Alpha Beta preview
whatever uh so that you when you you are
searching for preview packages you can
get that as
well uh we suggest taking authors and uh
title description and everything from
App Json using that and dependency must
be included on the
dependencies um
we include all the dependencies
including the dependencies that are from
the uh from the dependencies in app Json
but also the application dependency and
the platform dependency from
appj the application dependency is only
like uh one line in app Json application
colon and version number what we
translate that to in dependencies for
new get is microsoft.
application. localization if that's the
case and then the version number of
course yeah if you are using W1 of
course there will be no tag yeah in in
in the Microsoft dot application that's
the good good side that's you don't need
to care about that if you are working on
top of
W1 and we don't include the app ID on
the application package nor on the
platform
package um a very small demo let me see
if my machine
actually works here we
are camil showed you how to create a
package with the new get
command um obviously uh container hel
will have some functions or has some
functions for this um like the new BC uh
the new BC nouet
package and let me just run that and the
next lines here really copy the package
to a zip file and unzips it and shows
what it contains so if I just run this
section uh it will display the the
Manifest in my window here and
show the zip file just contains my app
and the Manifest that Camille just
showed you and if we have a look at the
Manifest file here it is really just
taking the various properties that I
found in app Json adding those to the
Manifest including the dependencies and
then we have this um I don't use the new
get command or the packet command
anything like that because the one of
the things that is special with
container hel is it it doesn't have
dependen anything so I don't have a
dependency on having new get installed
or packet installed so I'm just using
the standard sipping the package if you
want to do it differently you can always
unip it and use n get pack to siip it or
you can like create the new spec
yourself and just pack it it's really
really easy there's really no reason
for for getting stopped by
that
here let me
see so this is just a redisplay of the
new get package and really important
Fields is the ID the version obviously
the dependency to the application so
this one was built on uh with the
dependency to microsoft. application
21.5 meaning that I can install this app
on any ver any any business Central
higher than
21.5 business Central doesn't have these
concept of saying maximum version so it
just assumes that this app can be
installed on on anything higher than
that the file section is really optional
in uh net you don't have to provide that
uh my command do that but you don't have
to uh provide that I don't know we are
we are not doing that in one special
case but we will talk about that
later
um yeah Please be aware that Windows has
like long file name problems so even
though we write
2024 we still only have 64k no we we
only have 255 characters for for file
names yes we can uh put like a a setting
in our in our registry to like have long
filing names but then uh the the file
names become a UNC path and and stuff
like fail from each other and and
doesn't work anymore so keep name
short uh use a short temp path name in
order for for the the full cach path to
to work this is not a problem if you're
using the container hel stuff
because I'm actually not caching
anything there um but that'll Al means
that that's a bit slower than the new
good and the package stuff you you can
have even problem for example if you are
working with uh uh application workspace
in your windows profile document folder
or something because that will be really
really uh deep uh folders uh name and uh
you will you
will have much longer path than allowed
very quickly even when the package will
have short short name uh I needed for
example change our uh temp files on our
build agents to just ctmp or something
like that because the the nuget uh tools
are working with temporary folder it
means I I force them to use this short
folder and under that folder there is a
new get package ID sub folder and inside
of is the app file with the long name it
means
and if the ID could be 100 characters
plus
extension you can see that you will very
quickly go over that two 255
characters and for runtime packages
again uh we'll cover that later um but
yeah the real problem with runtime
packages is that they have to be for a
specific version of of business Central
so you really have multiple versions of
the same app when they're built for
various different different uh versions
of that so let's cover that
later sources okay that's uh about how
we can distribute the the business C
Business Central nuget packages we have
multiple possibilities of course
everything is what new is
supporting and uh the most used sources
are Azure defs artifact feeds you can
use public feeds and and uh private
feeds uh if you use public feed anyone
will have access to to your new get
package uh and you can distribute it
very easily uh then but uh of course
Sometimes some Partners want to have uh
some control over who is downloading uh
uh their apps and so on
this Source can be used as a Upstream
source and I will show you upstreams and
how it works in short while uh private
feeds could be used too but of course
you need somehow uh give the access to
to the partner to to that uh feed and
these feeds are not supported as a
Upstream feeds in Azure defs uh
server or cloud cloud
service that's something which um I
don't like but I can't do anything with
that there are many different requests
already
existing to this area uh where where
other developers are uh requesting new
features how for the upstreaming and so
on but uh there is no change uh in in
the Azure defs for that you can use the
GitHub page registry again you can set
them as Anonymous it means public or you
can have access token uh authorization
or authentication for for these sources
and it's mostly working that you invite
someone uh to your repository or or to
to the uh registry and he will generate
the access token he will use to access
the packages in in that Source uh it's
not supported for the upstreaming in
Azure def phobes it means I can I can't
easily connect my Azure defs feed with
some some package registry on GitHub uh
but of course you can you can use
different way how to connect to that
that Source because it's still nougat
Source you can use directly uh that that
Source in in your scripts or tools or
whatever you will use for uh working
with nougat because because I expect
that in next years there will be many
new tools created by really good
developers and people who who like to
support the community uh to work with
these new gets and and uh I expect that
it will be much much easier than
today of course there is public service
like net.org
uh those can be used to to distribute
Nets too but please don't trust these
sources because you don't know who
published something
there and if you download the
app and you will not check what's
inside uh you can very
quickly find out that maybe the app is
not what you expect it and something
will happen maybe to customers data if
you push that that application to the
customer
uh of course Publishers can reserve
prefixes on on uh these sources like
nuget.org like I expect that Microsoft
have
registered his uh prefix it means
anything starting with Microsoft will be
from Microsoft because someone else
can't publish anything like that there
but please be aware of this problem and
don't trust these sources and of course
you can use even other sources I I was
uh telling you that you can use a local
file system it means you can use the
shared file system on some server you
can use uh for example blob storage or
or anything and and if it have the the
support from the tool you will use for
downloading the package it's not a
problem but please try to use something
which is commonly uh supported because
uh if you are publishing the package for
others uh this these other partners
needs to somehow easily consume the
package from that
Source okay um of course the even when
you decide which service or which form
of uh Distributing your net package you
will use you can have multiple feeds or
multiple sources created for your your
your packages because for example you
can have a feed for released versions
and pre-released
versions because you can have even the
the suffixes like beta and and prayer
release or something like that for the
new get package but you can even put
these packages which are in Pre
pre-release uh state or something uh
just puts them to different Source than
the the versions which are already
released uh both ways are Leed uh you
can use both uh consumer then can decide
if wants to download the pre-release or
release version of of the application
and it's easy to to set up you can have
some daily builds cumulative updates
feeds or or hot fix feeds uh it's on you
on and on your your needs uh how you
will configure uh the sources you will
offer to others
and if you are consumer you need to be
prepared that you will need to decide
which source you will use in which case
yeah that's a that's a additional level
of we need to take into account when
deciding which source will be
used in the test phase we are right now
in in that test phase uh Microsoft will
provide three public feeds we already
have two examples how it will looks like
there will be one feed for Microsoft
applications it means Microsoft do
application and everything under
that
uh also the first party application like
yeah everything that's basically on the
DVD or in everything starting Microsoft
yeah yeah exactly will be there there
will be separate feed with the same
nearly the same content but the apps
inside these packages will be only
symbols it means the packages will be
smaller for downloading but will include
only the symbols it means you can't you
can't publish them to the environment
but you can use them to compile your
application in vs code for example and
it will be smaller for download but you
can use even the full packages if you
want uh in vs code and SE Source will be
the
upsource
applications but only
symbols yeah it means if you want to
build on top of some App upsource
application you will be uh able to
quickly compile your app with these
symbols because you you will be able to
download these symbols directly from the
feed you will compile your
app but you can't publish it to some
envir M uh you will need to of course be
in contact with with the publisher of
the application and ask for full package
or something if you are deploying for
example to some uh on Prem container or
or anything uh outside the standard uh
online sandbox because in online sandbox
of course you mostly you are able to
install the application directly from
upsource at least in some trial or
something like that
yeah but it will allows us at at least
very quickly prepare the app compile it
check what is inside if we can extend it
easily or not and so on because even now
you have access to the symbols if you
create the some some environment online
environment you can install the the app
there and then you can download the
symbols now that's why Microsoft can
publish the symbol because they are
already public publicly available but it
will be much easier for us because we
don't need to go through the environment
and installation and so on we just
download the symbols
directly and short
demo how these sources will looks
like I will take my glasses because it's
really small for me uh
this is the source of uh the Microsoft
applications you can see that uh there
are
really many applications
already and you maybe you will find out
that there are even applications you
never know that they are existing like
exclude anonymize data sharing yeah
application and address and you see that
uh every application have many versions
already uh yeah it's long long list
since version 17 oh if we have all the
hot fixes here yeah it's growing fastly
um there is one thing in Azure def's uh
feed you are limited in in number of
versions you can have in in in the that
feed it's I think 5,000 5,000
versions uh it's big number but if you
count the number of hot fixes which are
released by Microsoft if Microsoft will
release every hot fix uh I think that
you counted it for one year or something
that you will you will it's probably
going to run out I mean uh quickly so
we'll find ways to make sure that uh
yeah how we handle handle that situation
yeah it means yet we have this this feed
now please don't look at the URL because
it will be definitely changed it will
not be like that um it will be similar
but it is not final final place or name
how it will be be used of course if we
look at the this lists and I will try to
find for example microsoft.
application oh sorry
you can see even that there are multiple
packages with the different TXS yeah
Austria and so on you see all the the Lo
localized
applications and if we look at the
versions again we see how many there are
for every package like that it means yep
it's growing very
fast that's the source of full package
there will be done similar with symbol
packages and we can use them uh in in
our environment and for that if you are
on Azure devops it's easy to consume
because this is my feed in my compa in
my account and I can set up
Upstream Upstream sources and Upstream
sources is something which will be
contacted when the when someone is
searching for or something which is not
in my feed if it is not in my feed it
will look into the Upstream feed if it f
finds what what is needed the package
will be downloaded and copied to my
feed and will be used uh
then be aware of that copy copy action
here yeah that's if you search something
in upstream and it will be found it will
be copied to your feed your feet will
grow and depends how fast the versions
will be changing and and how you will
work with with the versions it depends
on that
uh the the the grow of your feet could
be uh maybe more than you expect uh you
expect but still the price for gigabyte
of of the feet is not so high it's just
few cents I think per month per
gigabyte if I want to add new Upstream I
have a multiple choices here I can use
public Source but in public Source I can
use only the net Gallery it means
net.org which we were talking about
please don't trust it others are for
other types of of
packages another possibility is feed in
my organization
but it's just it means my feeds maybe in
another or uh in another project or I
can add Azure artifacts feed in another
organization but it means Azure defs
organization not tenant it's still about
the same entra
tenant and it's written
there but there is a big but and that's
why I was able to use Freddy's
feet even when it is not in my
tenant because if I select this choice I
need to create the feed locator if I
create the feed
locator from Freddy's
organization project and feat
name I will connect because his feed is
anonymous it's public and there is no no
authentication and it should work yeah
it
means yeah should because it
worked trust me it
worked one hour before the session it
stopped for work but luckily because I
already had downloaded the packages in
my feed everything what I will show you
will
work because it's using the local copy
and I hope that someone one will fix
that and it will work later again yeah I
will just enter the locator check that
it's nouet and put some name add it save
it please don't don't uh forget to save
because uh many times I did that forgot
to save and say why it's not working
yeah I forgot to save uh we are not use
it used to that from business Central
yeah I have now two feeds here and if I
go back back uh to my feed I can search
Upstream sources for new get package for
example Microsoft do application again
search and I will found all the versions
available in that Fe Upstream feed and
you see that uh name of the Upstream
because if there are multiple you can
receive multiple answers from different
streams and if you want manually you can
manually save that version into your
feed uh and save it for for your work
preventing downloading it again or or
later that's the Upstream uh
Source uh in Azure defs there are
additional functionalities you can use
because for example Azure deob feeds are
supporting
views and every package version you put
to the Azure uh def feed you can assign
to some some uh uh
view one view is default one and you see
that default are pre-release and release
it means I can promote the package to
pre-release if it is pre-release version
and if for example later I decide it is
release version quality I can uh promote
that version to the release and then
when I consuming the new get
in the URL I have the filter for the
views and I will receive only the the
versions for specific view it means that
if I want only the released version I
will have ADD release and the result
will be only the released versions in my
result that's the the fastest way how to
work with uh released pre-released but
if you want to to use uh the the
suffixes beta pre-release release and so
on you can it fits your your pro uh
processes okay that's about the feeds
and
sources I'm sure that Freddy later will
show you the source on on the
GitHub I will go back
to the
presentation another part of the work
with the nouet packages
is version
limitation because we need need to
somehow limit which version the process
will return to us when we ask for
example for dependency which is
compatible with specific BC
version it means and if you if you
imagine that the the the dependency
three could be a complex things complex
graph there must be some algorithm which
will go through the graph and will
resolve which version of each dependency
will be
downloaded it could be time consuming
mainly if there are many many many many
many hot fixes in in the feed and then
you you need some caching to to be as
fast as possible and of course many
tools already solve that for us because
many developers have the same problem uh
like in C and so
on this is the example on the left side
uh you see the isv product which is this
distributed as a new get
packages uh the the major version of the
application is same like ma major
version of business Central for which
the app is compatible to to just easily
show you uh how it works on the right
side we have some crystal ball cleaner
application for some specific customer
which just uh make the crystal ball
forecasting isv solution much better for
that Customer because the the crystal
bow will be cleaner and we have a
version 23 of our app it means we are
working on 23 because maybe that
customer is not so lucky and is uh
running on
Prem and he found out that their server
is still 2019 server which is not
compatible or supported for
bc24 yeah and they can't upgrade yet
because they need to wait for the new
version of servers and they are not in
budget for this
year when we create new version and we
have already 24 version of the
application on isv site if we try to use
the latest we will fail the uh the
application will be not compiled of
course because that it means we have we
need some some tool how to limit which
net package we want to consume it means
as uh yeah the isv is depending on 24.1
we are depending on 23 and we need to do
something with that to have uh the
situation corrected because we need to
consume that version in this case it is
not latest but it is the latest for us
compatible with our our conditions and I
will show you some small demo
because I I will show you how the tool
Works in my
case I will go to different branch of my
example uh it will be one with
dependencies I will force everything
out and clean up and you see that I have
app with one one dependency on the super
cool extension maps pte from some
publisher with name Freddy Christiansen
yeah thanks for that extension uh I
don't know is using it some
someone no
sorry uh and we go and do the
magic you see that's I have the symbols
from previous demo here still
23.1 oh
nothing more and we are now downloading
and yep I have Freddy Christiansen being
my pte uh application here downloaded uh
for me and because it is compatible with
version
23 if I go and switch to version 21 and
if I look into the
feed of Freddy's
uh versions and we see which one is
oldest supported
21.5 I will switch to 21.2 I will do the
magic oh
sorry do the magic and I expect it will
fail yep we have
error and if I look into that I am using
the bucket client you see that there is
a conflict detected and it didn't found
the correct Freddy Christianson being my
pte blah blah blah compatible package
for me and it uh it can't download it
that's okay we expected that because we
can't correctly resolve that if I put
21.5 and do the
magic everything will be okay and the
the the application will be downloaded
again
correctly yeah it is here and we can
work how it works if I look at the
packet. dependency file which is the
file used by the packet client which
supports to the to uh uh the work with
the nougat packages and not only nouet
packages but others I have some source
of the uh the packages that's the my
feed uh this this feed have uh some
authorization some password which is in
in in variabl somewhere stored and
authentication basic and I want new new
get package with that name but I added
even my dependencies on standard
Microsoft
application and this means I want
anything which is
21.5 something any build any patch but
it must be
21.5 Microsoft
application it means it cannot be
21.6 yeah or higher
and you need a package of my package
that has a dependency on Microsoft T
application that is higher than that
yeah it means I'm limiting the selection
the the the dependency graph
resolution and I want only that that uh
result not every tool have that uh but
uh it's very easy in in pcket and just
by adding these lines I'm I am Limited
in the search correctly and I will get
the correct result uh for for what I I
need yeah and that's that's the strong
strong uh tool of the
nuget because you have all the
dependencies all the metadata about the
versions and so on you can resolve
correctly which version will be
downloaded to be compatible with your
platform with that we go to talk about
runtime
packages so what is a runtime package
it's a it's much like uh fob files in
the bad old days um where we had a
compiled image of of your app um it can
be installed on premises without having
a license where you can insert into the
extension something whatever can't
remember what camil told me but but it
is a a construct where you can like
share your app with
customers
um pre-compiled for their version it
doesn't contain the AL source code but
it actually does contain the compiled C
source code so it doesn't really like it
it doesn't hide away your source code
totally you will be able to get given
that you have a runtime package to be
able to actually see the compiled image
of what code people have written you you
have mentioned that something like fob
file I think that's many people here
don't know what's that who knows what's
this for file file yeah okay sorry too
much people know that
still that reminds me of the first
session I had about Docker where I asked
how many people know what Docker is
everybody raised their hand and I said
well was a surprise um that was a
surprise as well okay
anyway it is only guaranteed to work on
the same minor version and the same
localization of business Central as it
was created
for which makes you have to create a
whole lot of these runtime packages you
want to be absolutely sure that it
works cannot be uploaded to appsource so
runtime package doesn't work
there uh can't be installed as a
pertinent extension it can be used for
devops purposes or for on premises
installation it
is an obfuscation of your IP it is not a
protection of your IP
so I think but that's clear if you still
want to use runtime package then
then like obviously if if we look at
what we talked about earlier with uh
with normal net packages we have like we
have a number of packages in net and
there's another dimension to that we
have the version of these packages so
it's two-dimensional we have a list of
packages clicking versions versions
now adding runtime package to that
mix makes it
three-dimensional we add the BC version
to that any any version of your
app like if you my my app version one
now needs to be available as a package
for or 21.0 Czech localization 21.0
Danish localization 21.1 and I could
actually how many localization we have
many um so it kind of makes makes this
three-dimensional and and how do we
solve that uh we had quite a few
discussions on that and we want
three-dimensional nouar packages or I
don't know if that's a thing um but the
essence is that one one version of the
app is available for many different
versions and if we one of the
suggestions was to add all the versions
into the same package so that if you
find my app version one you will
actually have both one version and the
other version so we have two runtime
package in the same app uh the problem
with that is that then we ship 24 of
business
Central and uh it is not possible to
update an existing runtime pack or an
existing nouet package so I had to find
a different way and the solution we
found is to use something called
something we call indirect packages
because it's really not something we
could find anywhere else than this
suggestion and indirect packages if
trying to explain how that works is that
that you have an a package on net called
your the the publisher. name. runtime.
abide ID so the resolution the
dependencies will be going to that app
ID and they'll be like they they'll find
this package right that package
um does not really contain anything it's
an empty package uh
but the indirect package the empty
package which we call the indirect
package has a dependency on another
package which is in this case we have .
app. runtime do and the version number
of your app meaning
that uh that now we have like a
relationship basically a table
relationship to that version of your app
and now we can have multiple packages or
multiple versions of that package in
that new feed
so it does mean that the version of my
app from the indirect package is now
part of the ID of the package for that
version specific and yeah the actual
package where the runtime package is
inside will never be found by any of our
because there is no app ID yeah the the
app ID is not included in that one so
they'll like go under the radar and
we'll only find them as dependencies to
uh the indirect
package and the runtime package the
package containing the runtime app then
has a dependency on Microsoft ad
application and then square bracket
version number comma version number
parenthesis that is net for saying
larger than or equal 23.2 and less than
23.3 meaning that if you go back to the
uh the the the the the resolution that
camil just talked about where I'm
looking for something that satisfies the
the the apps that I have
we will know that if we want to find
this app for our version of business
Central 23. do do3 the first one will
not satisfy that um dependency the
second one will uh so this one says no
files in that one and the runtime
package is in the other
one and that one can only be used with
app
23.3 U so the dependencies really will
point out that the first one can only be
used for 23 or two and if we go
to this one when we then ship another
version of of uh business
Central you don't have to create a new
version of your app and create runtime
packages for everything in order to
create a new package but you can just
create another package and add that to
the second feed of the version number of
your app so you can actually have
multiple apps that will work in this
way but what about
localizations are we really talking
about
four-dimensional like n get packages so
we quickly decided that this thing
having the localizations as uh as part
of the package if we look at runtime
packages I think so theoretically a
runtime package can break if it's
compiled for one
localization and running on a different
localization if it's on the same version
number uh when I say theoretically it's
like if if the change has to be like a
parameter to a function with a different
different type if I change a type uh in
the in the US localization to string and
it's a number in in the Danish
localization or change the parameters
for a function that's called then the
compiled image will
actually uh fail because it's compiled
towards a different
type how many times does that happen
that a localization has a different
parameter set or different type actually
uh than the other one I I don't think
it's a common thing um but if you want
to be absolutely sure you need to
compile it for every single localization
and then we decided if we want to do
that we are not going to create like
another layer of indirections in nuget
we say that people put the runtime
packages into a the localizations into a
folder in
the second package the package
containing the runtime package you
create one runtime package that are like
in the root and then a subfolder for
each localization that has a special uh
version of that so if you ever find out
that this localization needs a special
version of my runtime package then that
is the solution to get around that every
time it's on you how you will choose the
the the
the scale or or the ratio between the
cost and the outcome of using the run
time and generating all the combinations
and have gigabytes of gigabytes uh of of
the runtime
apps which will work or you will have
less versions
which will work mostly in 95% or
something like that and if you find some
which doesn't work maybe you will fix
only that one 95 is a very low I'd say
99.99 something like that I think it's
very yeah it it it is you will probably
never run into that but
anyway uh I totally
agree so when a new business Central
version uh ships you'll just create a
new package of the uh new get package
that actually contains the runtime
package for
that
[Music]
um this is the indirect package that has
a dependency on the other package which
is in the same feed and you'll have a
number of versions in that one so let's
go
to look at the actual news spec of the
indirect package where you'll have the
ID and the version and then you have a
dependency on Freddy Christianson Bing
Maps pte runtime
51230 version
1.0 um you have application 21.5 you
have platform these are from App Json
that's the minimum version and then in
the actual news spec for the runtime
package you'll have the file section
with the runtime package and you'll have
an application dependency pointing
to the application dip that this one
supports it's really long name of for
the up file yeah you will have a problem
with that file
name I mean there
targetting PT 5123 Point run time 23 21
yep too
much
no so
you've seen a few uh examples on how
these things works on as one slide
before the demo uh using the net client
and the packet client uh obviously some
of this stuff is also added to container
Helper and uh supported in algo as well
or we are working on supporting that in
algo but uh the functions are existing
right now in container Hela and the
functions that we added for that are
these guys like you can create a new
package you can push the package to to
nouet the same as nouet ad really if you
had a the new get client there you can
find a package you can get and download
the package then you can there's these
two Uber functions like download BC new
get package to folder will download a
package and all dependencies to that
folder and you'll have publish BC n get
package to container which will download
all pack packages this package and all
its dependencies and publish them to the
container in order of dependencies if
they are not already installed in the
container uh so as you can imagine these
functions are used when you run devops
and you kind of need to install your
dependencies
um camil's methods using new get and
packet are here I right probably I think
that is a that is in order to satisfy
myself for not saying they are faster
but but I I cannot there might be
situations where where I'm faster than
you but I think in 99% of the cases new
get and packet will be faster than the
implementation in container hel because
container hel doesn't cash anything it
actually goes to the server and finds
the packages and like looks at the
dependencies and in some cases it can be
a really really really long search
before it finds the right package and uh
we might make that better or somebody
might might find a a better solution
than than what I cooked up um but but
let's look at that one let's have a look
at the functions
in container
helper if we
can uh that's not here
so uh I'm not going to show all the
functions I'm just going to show a few
of them like the get BC new get package
uh the way that it's implemented now
Camille talked about Upstream uh and
stuff like that that doesn't exist on
GitHub and what we use in container
helper can use both as a devop feeds uh
GitHub feeds and
N so the way that you do do it is you
you set up a number of trusted feeds in
this case I have one trusted feed that
is my own on GitHub business Central
apps index to Json and then the token is
my authentication
token uh that is added to my my settings
and I can say the patterns for this one
is I'll take all packages that are on
that feed I could here put like
Microsoft dostar if I trusted that and
the reason for that is obviously you can
trust n. and Microsoft dostar you can
also specify a a code signing um thumb
print if you only want to accept
packages that have been signed by that
author so having a look at how this
works if I run these three
lines there'll be a lot of output here
uh but it downloads the package and I'll
have like a file name uh down here where
the package has been have been
downloaded to if
we have a look here what it found 12
version the first version were 22.0.1
2016 the last version was this so the
earliest version is that and I
act asked for select earliest so I got
that one um I could have of course taken
the other one if we scroll down to the
download basally new get package uh to
folder I'll Trust a feed as well that's
the same feed and I will download a
package plus all its dependencies and
the download dependency says all bir
application meaning that when it when it
traverses the uh the dependencies it
will stop when it reaches
Microsoft uh application I can there's
also a tag called all but Microsoft
meaning that it knows that all the
Microsoft apps are in the artif effects
for that one but in this case it found
four apps and what I was asking for the
the the app ID that I was asking for
here
bc5 is the Danish version of my app my
Danish version has a dependency to W1
and W1 has a dependency to Common and
Licensing um and by asking for the
Danish version of of of my app I then
got all four apps downloaded to this
folder
and can use them to publish to whatever
I want I can also use the publish BC net
package to container and I've created
two containers already uh the first one
here or actually that's this one will
take exactly what I just downloaded to
this folder and publish to a container
so I'll run
that to a bc24
container and we'll see exactly the the
same it's going to go through this one
and and and find the packages find the
dependencies and one once it's done that
it will start publishing them and
probably either common or licensing
comes first uh because they don't have a
dependency on anything so starts
publishing common and then it
publishes licensing and then the W1 and
then the Danish
version
so the other example here actually uses
runtime packages
and looking at that it's the same thing
I'll just say I want to publish this app
165 something that is probably my Bing
maps pte that nobody uses uh to a
container here and I'll select the
latest matching version now my container
here is a 23.2 I think so what it's
going to do is it's going to find the
runtime package for that version and it
it goes through and finds oh there's a
23.4 that's not good enough there's a
23.3 that's also not good enough then it
finds the 23.2 and then it downloads
that and publishes that to my
container obviously if you
had a thousand versions out there and I
would like enumerate back from all of
those that uh will probably take more
than a few seconds and something that
I I don't want want to demo here for
sure um so that's a little about the
functions that are in container
helper let's look
at the next one which is Al go for
GitHub and what that does uh for nit the
it's work in progress what we have in
Alo for GitHub
today um by the way that's my dog
so but it's an AI photo of that so um
you have two things you can create a
secret called GitHub packages context
you do that ALG goo starts uh
publishing automatically uh all packages
built to GitHub packages and it uses
that GitHub packages feed for package
resolving meaning that immediately by
creating that secret as an
organizational secret all repositories
in your organization will have access to
all packages built by any repository in
your organization
uh for automatic dependency resolution
so that's a nice one to add if you have
multiple repositories and they depend on
each
other if you create a secret called a
setting called trusted nouet feeds then
algo for GitHub will automatically
search these net feeds for dependency
resolution when looking for dependencies
during buildt and it will find whether
it finds symbols full packages or or
runtime packages uh everything will be
taken but of course full apps will be
preferred and then
um symbol of run I I actually don't know
it I'll have to check that up whether
one is preferred over the other if it
finds
two um the last one if you create a
secret called nouet context it will also
start
publishing your apps to that net feed
Again full apps um
it says runtime packs here
yep that that doesn't work today today
it publishes full apps there um and and
the runtime pack uh functionality is
something we we're looking into adding
functionality for for for doing there so
that's a that's an error on the slide
sorry about that let's have a small demo
of how Al goo for GitHub does these
things
this one this is not ELO for
GitHub so let's have a look first at
just a my simple GHP like GitHub
packages uh my Danish version I have
created GitHub packages context as an
organizational secret and I created a
net context as an organizational secret
as well if we have a look at the buildt
in the deliver section you'll see
deliver to get a packages and deliver to
net the deliver to nouet Will will
deliver this package to the feed that
says here Dev as.com
Freddy DK apps something I think that is
what actually the feed that you yeah
there is something earlier I can't read
it it's
something I try to zoom it
up
um yeah so so that that's one that's one
and then it delivers to GitHub packages
as well going to deliver here and
finding the same URL or that's new get
package GitHub business Central apps now
looking at these feeds looking at the my
apps feed on aure devops we'll see that
this is actually the the common one that
it found this is the Danish one that it
that that was built but the common one
here exists both in a Freddy K version
doesn't exist other version and then in
several versions here and it's going to
find the right version when we go for
the
that packages here uh yeah the versions
of that if we have a look inside the
build
for when it uh resolves the dependencies
when it builds like the Danish version
it will be looking for it says I have
missing app dependencies to these two um
app IDs and it's going to look for those
in Nate and every time it downloads a
package finds out that there's a new
dependency so I'll have to download that
one as well but the down download uh BC
n get packages to folder we'll solve all
of that for Alo and and and download
everything
there um means everything is Plug and
Play yes as everything else what we try
to do in Alo for GitHub is plug and play
with ability to configure and can I
somehow configure the process that if I
want for example publish two two sources
and and from some reason can I somehow
have impact to that process if you want
to publish the two different
things not by a set then you'd have to
create a small poell script and add that
to
so with that I think back to you yep we
are going
to final things why to use the net at
all trying to summarize that for you uh
if you are on the publisher side
it's for you the easier if you share the
the the
packages for other partners to easily
consume them and they will find out that
uh the application is good and they can
easily download the application and work
on it they will definitely sell this app
to their uh customers it means it will
be for
you much bigger sales because uh yeah
why I should sell something which is
hard for me to use as a partner for for
my customers yeah that's that's uh the
biggest reason because uh right now if
me as a v i want to consume multiple
application from different Publishers I
need to go to multiple portals emails uh
some storages and so on manually
download the packages or apps and and do
everything manually if it will be
unified and automatized it's much easier
and I will support that definitely as as
a far if you are on the consumer side
for you it means that uh the cost of the
de development of something on top of uh
solution of someone else will be much
much uh cheaper it will be faster
because I don't need to create first the
environment to download the symbols and
start the development I will just run
the development because I will easily
download the symbols for for the vs
codee and if there there are some other
apps and I need runtime packages for
example for specific version I will
easily download them and use them and of
course if I will have symbols for with
correct version for my development in vs
code the it the output will be better
quality because how you are working now
you have up Json up Json dependency on
3.2 but your only environment is
23.5 yeah download the symbols it will
work uh I will I will do everything then
you will compile the app you will
publish it to for example uh environment
3.2 and you find out that you used some
feature which is not there because it
will not compile it you will not publish
it there because it will fail that's
problem of the quality and everything
you will have a correct
versions in in your process and for
every
developer it will be much faster to
start the
development the it will be less
complications when using these these
apps and and these processes uh shter
lead from beginning to start the
development I just need the app run the
magic uh through some for example in vs
code extension will be there in maybe
one year or or it depends on others who
will ex uh who will develop that and you
will be done and ready for for
development that's uh the dream we are
not there still because we need few more
uh things from Microsoft side a few
maybe tools for the usability for for
all the developers and yeah that's
that's the dream
which is becoming reality act now if you
can uh start to publish the nougat
packages at least internally consume the
nouet packages internally in your cic
CDs we are doing that in our company
already long time we just slightly
changed the naming convention we were
using to be in line with with these
rules and we don't have a problem to
just for example Upstream Source in our
feeds and we are consuming already these
temporary feeds from from
Freddy they are not up to date uh yet
but uh if we are missing something we
just uh create fake package in our feet
and we can continue with with working
with these these n get packages yeah it
means yep try to to act Now consume that
PR prepare your cic CDs for that and uh
you will be ready for uh the
future now time for the
questions I think we had up here I will
let it to on
you is there is a plan to replace
current behavior with download symbols
uh with no jet no new get packages or
they will work
together if if it's a plan to be able to
download symbols without n get packages
I mean uh if someday um Microsoft
decided to change current download
symbols uh with using only uh new get
packages or replace the the the the
download symbols with something which
will work with new get packages ah so so
adding something inside of V vs code
that can do that uh yeah I mean I don't
it's not on our plans right now anybody
could actually do that right you guys
could add a a a small uh Gadget to AVS
code extension and and add that but
maybe Microsoft will do that as well
obviously we haven't worked on that
since we don't have our own Feats yet
so
okay I think you next
here um my question was basically pretty
much the same but um an additional
question was from your perspective does
it make sense to do some kind of real
package Management in a backwards um in
a backwards search for example um let's
say I have a reference to a dependency
of a third party app in my app I have
using version
24.0 the Publishers releasing 24.1 I do
not recognize this
but some kind of package management like
new get would do in in V uh in Visual
Studio would update the new get packages
with a command something like this this
would just make sense for you
or uh are we talking about package
management basically in invs code for Al
extension yeah yeah it's a of course
everything have meaning if there is
consumer for that if you as a
developer need that and you will be
using something like that why not yeah
that's some we will develop that but for
me I need just run some function which
will do the resolution for me and
download the packages like the script I
I I I was using I don't need anything
more because if I want to add some
dependency or something I mostly uh know
that that that info from from somewhere
yeah of course I can imagine that there
will be some catalog of uh packages and
so on but uh yeah I don't see that as
something which is broadly needed or
Partners will want to support I don't
know because something like that it's if
mostly the upsource is source of this
informations yeah it
means I will look there F find but maybe
we will find out in in one or two years
that something like that will be nice
and someone will came with that I don't
know right now I can't imagine I think
there's one big difference thinking
about it uh between like if you create a
vs Vis Studio project and anything like
that in this world business Central you
are not deciding whether the customers
upgraded to the latest version of that
other app right that happens and and and
you guys just need to be prepared for
that so as camil said like he's running
workflows with the earliest version and
the latest version and we're doing the
same so so your next major workflow will
will like be taking the latest version
of all these packages out there and
report to you if there is a a break or
anything like that and and uh yeah the
current version workflow will probably
do the same um package management I
don't I don't
think that something that we would
invest in I think was the next one so
yeah are there any scenarios where I
should use runtime packages as a package
consumer are there any scenarios we have
to no no scenario where you have
to scenarios where you where you only
can get a run package like if you were
depending on a uh like um an appsource
app from some partner that don't want to
give you the full app okay then the only
thing you might be able to get is the
runtime package if you can get that okay
Mo mostly mostly it's problem of the
license and for example we hit one one
uh uh problem when we were deploying our
app to customer site with his license we
get uh license error that we can't
create table
extension but right now it it was a few
weeks ago we had no time to go deeper
into that if it's problem of
configuration of our granule because it
was our upsource app published to the on
Prem system or it this problem of the
customer
license on Microsoft side or something
but the we solved it by publishing the
the runtime package because runtime
package could create the the object
regardless the license yeah it means uh
there are some licensing uh sites why
you are using a runtime package to to to
publish the
app uh hello thank you um I have a
question about
um so a rainy summer day in Denmark we
decided to also use things like
propagate dependencies in our apps is
that going to work also here with new
get
packaging uh so there's this property
that you can have in your app it's
property but it's it's just about how
the code is compiled it's not about the
dependencies because you are still
depending on the app on top of your tree
yeah and you see all the functions uh
under it but the apps still have the
dependencies on these these these apps
the one that propagates yes and yeah and
it's still an app file yeah so the
microsoft. application is actually an
empty app file with propagate dependency
and we do nothing we do nothing special
for that in building all of that so yes
that will work yeah the propagate
dependencies is just about what you see
if you are depending on that app it have
nothing with the structure under it's
treated as a normal app basically yes
with the dependency that have you got
last
one well maybe I missed something or
didn't understand everything but um can
you use the runtime package as a symbol
S yes okay
thanks okay have we still some shirts or
we already we don't have anymore we
already don't have the shirts sorry we
have 43 seconds to get an
answer does uh run Al pipeline supports
uh in stalling apps from the feed new
get feed I get need that one more um run
Al pipeline from BC container helper
yeah does it supports uh installing apps
from the Feed N N get feed yes it does
but it does that
by oh you have to specifi there's a
override function there that that's
called install missing
dependencies uh Al go for GitHub will
provide that override when it calls run
Al package so you can have a look inside
go for GitHub what it does but basically
that install missing dependencies is
called that you provide and then you
basically just call download BC new get
packages to folder as a response to that
uh that
c okay thanks for your questions thanks
for being here
and I hope that it it's it's spe time
sorry enjoy rest of the conference sorry
yep
