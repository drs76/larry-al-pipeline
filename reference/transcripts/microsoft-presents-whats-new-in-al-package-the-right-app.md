# Microsoft Presents: What's new in AL - Package the right app

- **Source:** https://www.youtube.com/watch?v=TsKozdmZxqc
- **Video ID:** TsKozdmZxqc
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 44m35s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

All right. Uh ladies and gentlemen, for
the next 90 minutes, we will have uh two
sessions with multiple speakers. Uh for
the second session, it will be what's
new in IL language enhancing your
development experience. But right now,
get your hands together for our first
speakers uh with what's new in AL
package the right app.
[Music]
Okay. Okay. Everyone welcome. Welcome.
As was said, this is going to be a long
session. It's going to be two sessions.
So, we're going to talk about the
package first, the app package and the
language a little bit later. But first,
let me introduce uh my colleagues here.
We have Blanca, we have Balash, we have
Peter, and hiding over there somewhere
is Espen who's going to join us a little
bit later. Uh so, for this first part,
we're going to talk about the app
package. And for the app package, we
want to talk about the things that are
maybe not just the AL code, the other
things about the app package. This can
be source control information,
resources, and some instructions for the
platform. And then we're going to let
Peter talk about troubleshooting about
how to troubleshoot your app package.
Yeah, let's go. Blanca, stage is yours.
Sure.
All right. So for this uh first
scenario, I'm going to show you how you
can leverage some of the latest
capabilities uh such as source control
information um and resource files in
your app package. So for this case, you
can imagine that I have a marketing text
uh generation app using AI. And what I
want to do is leverage the new uh
feature for resources so I can move my
prompts into resource files. And this
will allow me to pro protect them better
and also make my um my extension more
robust.
So uh to do that the first thing that I
need is access to my source code. Um and
actually now I can do it uh since two
releases ago now I can do that from
directly from the web client. So, I'm
going to go ahead um and go to extension
management page
and I'm going to look for my extension
which is this one over here and you can
see that uh I cannot download the source
code directly from here because it is
protected by the resource policy. Um but
if I open the car details then I can see
that it has some s source control
details. So I know that this app is on
GitHub. So I can see here the repository
URL where it's hosted and I can also see
the commit ID um that corresponds to the
version that is installed currently.
Um and you can so this is actually quite
useful the commit ID if for example you
encounter a bug then it's quite easy to
pinpoint uh from which commit ID uh this
was introduced.
Um and you can add this information on
your app manifest or if you are using
algo go for GitHub then this information
is uh stamped automatically when you
create a release of your app. Um but
it's also recommended that you add this
as part of your process if you are using
your own release pipelines.
Um and thanks to making uh adding this
information in my package now I can very
easily access my source code directly
from the client with this new action
open source from git.
So once I click that as many other
opening VS code functionalities this
will uh go to VS code. Um and since it's
the first time I can either clone or
open it. So I will clone it in this case
in this folder. Um, and as you know, you
can only do this if you have access to
the repo. So, if you don't have access,
this will throw an error.
Um, yeah. So, you can see I already have
my uh repo cloned. Um, and I'm going to
create a new branch from main and I'm
going to call it changes.
And um, yeah, that's my my app and this
is my source code. Um, another thing
that you will notice is that I'm missing
some references. So, for that I need to
download the symbols, but I don't have a
launch configuration for this project.
So, once again, I'm going to go back to
my client
and then help and support and then I
will find this new action over here
generate launch configurations.
And when I I click on that that will
generate the configurations directly in
my project matching my environment. So I
don't have to do that manually. And now
I can easily download the symbols.
So I did that just with one click. Um
and while that is going on I want to
also make a remark. If you look at my
code you can see that I'm using the um
BC AI resources. So the these were
mentioned earlier in the keynote. So
these are the Microsoft manage resources
that you can use to access LLMs. Um and
I'm not going to go into detail with
this right now. But if you want to get
started also um with your own AI
project, then you can very easily use a
template that we have introduced in VS
Code. Um and you will have a project
just like this set up and uh you can get
started with your own uh project and
test it out. And now that my references
have been resolved, then it's time for
Balash to to continue with the resources
part. Thank you, Blanca.
So, um, continuing in the context of
this marketing text copilot capability,
let's consider the scenario where we
want to move the system prompt out of
our AR source code. This could be
beneficial for multiple reasons. Maybe
uh we want to access it uh from other
code units as well or maybe it contains
some uh important and sensitive
information uh like intellectual
property that we do not want to keep in
the source code. Well, Business Central
now allows you to package arbitrary
files with your AL extension that can be
accessed at runtime. Uh these resources
can only be accessed by the extension
they are packaged with and not by other
extensions. So to move the system prompt
into its own resource file, we first
have to create a new folder that will
contain all of my resources. Um, and
then I have to add it to the app.json
resource folders property. In our case,
I have created the resources folder with
the prompts subfolder and added my
system prompt.ext file which contains
the prompt that I wanted to move out.
Then I went ahead and added
the resource folders property uh and I
added the dot resources folder to that.
After this um accessing the resource
from al is super simple
and it can be done by invoking the
nav.get resources text in our case and
then specifying the full file path
relative to the resource root folder. Um
if we want to do some further validation
we can also list the resources and check
and verify that the system prompt.ext
file is actually available.
We can use the nav app list resources
and then we can pass the prompts text
literal as a filter and it will provide
the full list of the resources that are
available in the prompts subfolder. I
can check if my prompts/systemprompt.ext
text file is available in this list and
if it is not I can manually handle that
case in any way I want.
So if uh packaging the system prompt
isn't ideal at all then an alternative
could be to move the prompt into your
own Azure key and read it from there.
First you have to specify the key volt
to read from by adding the keyword URL
to your app.json. JSON then reading the
secret from the keyword can be done by
first initializing the app keyword
secret provider and then invoking the
get secret method of the secret provider
and passing the name of the secret that
we want to read. To prevent accidentally
exposing any sensitive information, we
strongly suggest you use a secret text
variable type instead of a plain text so
that the system prompt will not be
exposed during your debugging sessions.
And that's been it from me. Now back to
Blanca to look at the packages from
another perspective.
Yes. Um so
yes another important aspect of packing
your app is to know how to mod
modularize it in such a way that you can
maintain the extensibility scalability
and um maintainability of your apps
going forward. But as you know, time
goes by and the apps start to mature and
they start to grow grow grow and then
it's time for you to split those app
into smaller parts so you can maint um
keep those uh principles.
Um so
yes that's actually my my case right now
because I have an app that it's h it
used to contain just a sales uh uh
functionality but now it also contains
the inventory functionality. So for this
case I would like to split up my app
into two different applications one for
sales and one for inventory inventory
functionality. And as part of this
process that means that I also need to
move t um objects from one one
application to another application. So
for example with the pages I can do that
through the usual obsolution process but
with tables it becomes trickier because
I need to handle not only the move of
the table itself but also of the data
inside the table. Um and up up until now
the only way to do this was through um
migration. So you would have to write
your own uh upgrade logic to transfer
the data from one extension to another
extension.
Um but since last release or actually
since last year you might have already
seen that we introduced a new feature
for moving tables and moving fields
through some properties that we set in
AL that acted as platform instructions
for the platform to handle that move. Um
and last year that was released only for
the base app but since last release we
also made this available for your apps
app source apps. So now you can also use
it for your regular apps in apps source.
So as I said uh this is done through
some properties that you set in and then
uh the uh platform uh takes these
properties and handles the upgrade for
you uh the transfer for you. Um so there
are usually three iterations where how
you would do this. So in the first h
first iteration you want on this on your
source extension you want to prepare for
the move. So that means on your table
you just need to set the obsolid state
property to pending move and you have to
speci specify the app id where you want
to move your table and then you have to
deal with any of the breaking changes
that could happen during that uh stage.
The second iteration it's also on your
source application. You just need to
allow the move and you do that but h by
setting the obsolate to move.
And the third step is on your
destination table application you have
to uh reintroduce the table and then you
have to set the property move from
uh to your uh source app ID and it's
very important that you have set h in
step two the table to moved because
otherwise the upgrade uh the uptake um
the move will take will fail during the
the upgrade phase.
Yes. So, skip that too fast. Um,
so that was it for the theory.
Now, let's look at the how that's done
in in practice. So, in my VS code, I can
actually set up my app source scopes.
So, I can kind of stage how I'm going to
do this before actually doing to app
source. Uh, so I did this right now and
I have my my sales application. You can
see I have my inventory module and my
sales module. And I want to move all
these objects to my new application. So
as I mentioned earlier, I need to in my
first saturation, I just need to enable
these properties over here. And you can
see I already get some errors over here
about the table that is missing. So I
also want to move this subject. So I'm
also going to mark those as obsolete uh
pending.
And now I can increase the version of my
application
and I could go ahead and and publish
that. So that would be my first stage.
Um for my second stage I have to go
ahead and mark this as moved.
And you can already see that all the
references to the table are no longer
valid. But since I'm moving these ones,
then I can go ahead and delete uh the
subjects that I'm going to move to my
new app.
And that's it. And now I can go ahead
and increase the version and publish
that one. And then for my third step, I
just need to update the move. So for
that, I already have my new app over
here, inventory.
And you can see I have reintroduced the
table. It's very important that the
table is exactly the same as the old
one. You cannot remove any fields. You
cannot remove any uh methods
public methods. Although you can add
fields and you can add methods. And then
the only difference is that I have to
set the move from property to the old
application.
Um and you can see I also reintroduce
the page and the permission set objects.
And that would be my third iteration.
As you can see, I'm also missing some
references over here. Um, so I also need
to deal with that. But I will go that
back into a bit later. Uh, but that was
as you can see that was very very simple
way of of doing it. Um,
yes.
So for uh moving fields, it's also a
very similar process. Let's see. Let's
take this case for where I want to move
a field from the sales table and I move
it I want to move it to its own table
extension or another extension um and I
could do that uh using the the same
process basically. So again I can go to
my sales
table over here
and I have to set my properties. Oops,
I'm zooming out by mistake.
There we go. It's different keyboard.
Okay. Yeah. So, I need to set up my my
properties. Uh then that's the first
iteration. Second iteration. And then on
my new uh extension, I just need to
reintroduce
the field. So, I actually have already
done that here. So, I can show you. And
that's my field table extension with my
new field with a mood from property. So
again, a very similar process.
And then let's go back to the case that
I showed you before that I had to deal
with and it's a more of a complex uh
process because as you can see I both
applications depend on the code unit and
an enum object. So when I moved the
objects from one extension to another
extension then that broke that
dependency.
So to handle that then I need to move my
objects uh in this case the code unit
and the enum to an app of itself and
then I can make that app a dependency of
my two other applications
and that should uh solve my problems.
And then if you want to be an even
better uh developer, you can also make
use of interfaces and that that was that
will make your whole extension more
maintainable in the future. So you can
have an interface and then have code
units implementing a different
functionality of that interface.
Um and that was it for for moving tables
and fields. Uh this was just a case
scenario. So make sure to check
documentation and other uh the launch
event video if you want the full
information with other cases and other
considerations. Um and just before that
as a bonus uh case I want to show you
that as you can see if we had an
application uh that depended on my sales
app that's only one dependency but now I
have potentially four dependencies and
instead of manually having to go to my
uh app.j JSON
uh file and update all the dependencies.
Then I can easily
go once again to my environment.
I can go to extension management page.
Then I can select my dependencies,
my extensions.
And now I can find this new action over
here, get selected as dependencies. And
then I can show and copy. And that will
format my extensions as dependencies
without having to manually fill in the
information. And I can copy paste that
and put it in my app.json or I can also
go ahead and download those directly in
VS code. So so this will update my
app.json with my dependencies and it
will also download the symbols as it is
doing right now. So um that was it for
for this scenario and now Peter will
show you more about the troubleshooting.
Thank you. Let's give Balash and Blanca
a hand.
Yeah. So I think uh Stefan oversold it
maybe a little bit because he said
troubleshooting and we have lots of
troubleshooting tools in the product. Uh
actually you can go to aka.ms/bc
troubleshooting. We have a whole landing
page on the troubleshooting tools. I'm
going to talk uh about performance and
when you make an app uh right imagine
that you deployed it and the customer
calls and say they have bad performance
you got these more lights right you have
a hands as well so how many of you are
you know solving performance issues as
part of your everyday work
yeah not that many maybe but uh that
that's good to hear so what we have for
helping you with performance issues use
is of course telemetry. You can use
telemetry to get insights into what
actually happened and try to mine that
and find patterns. But we also have some
more interactive tools uh in that you
can actually uh profile code. So how
many are aware of the profiling support
that we have?
Yeah, not a lot. So about five years
ago, we introduced the ability to from
within Visual Studio Code uh create
these snapshots, basically offline
debugging from production environments.
How many in the audience have tried
using the snapshots feature from Visual
Studio Code? Well, that's great. That's
actually a lot. And so one of the
features that you could do when you
created that snapshot was that you could
include a performance profile that could
actually give you insight into um the
calls and the time spent within the
methods uh and within sort of a branch.
And that's the view I have uh behind me
here. You can see basically follow along
see uh the the execution and you can
actually jump into the source code as
well if you have that available uh in VS
Code. We have a hyperlinks that lets you
go in there. And so that's that's
something we had uh in Visual Studio
Code. And then um in 2022 I think it was
we introduced the incline performance
profiler which uh was or is a way for
you to uh interactively investigate
performance issues within the web
client. Basically uh you can run through
the scenario and get the same kind of
information. How many of you have tried
the inclient performance profiler?
Still a lot. So uh that is something
that is useful for developers which I
guess most of you are uh but also for
functional consultants for support for
example trying to investigate and
pinpoint where in source could be could
there be a bottleneck when the customer
is is talking about a performance issue.
And so uh the way it works is that you
can open that from help and support or
you can search uh for the performance
profiler and it will basically open up a
window that you should place on the site
uh where you can start and stop the
profiling. You then start the profiling.
You perform the user scenario. You stop
the profiling. That's why we call it
interactive. You basically do the
scenario while you are recording. And
then after the um profile has been
captured, you can get an overview of
where time is spent. So which extensions
spend the time? That's a good indicator
of uh should you blame Microsoft, should
you blame an app source app, should you
blame a pretendant extension for a
specific customer. For example, you can
actually also enable some further
details. So you can see uh the call
stack and you can see which objects took
part of the flow and where is the uh
time spent. So that's basically the
scenario uh for this.
Now uh some of the challenges with the
uh inclient uh performance profiler is
that it's exactly interactive. So that
means that somebody needs to do the
repro steps. So if the customer is
calling uh you know they need to help
through the maybe they can't use this
tool themselves. So somebody in support
might need to help them h go through a
pingpong and that can take time uh and
and and impacts the time to mitigate
because it's inefficient.
Also if you have any kind of performance
issues that are transient that doesn't
always happen it under certain
circumstances right the customer is
complaining about performance but you
don't see any performance issues that
can be a challenge as well and then the
inclined performance profile only
supports uh interactive flow so the user
clicking in the UI so those are some of
the the challenges
they don't support web service calls for
example they don't support background
sessions like job cues so uh about um
half a year ago uh we introduced
schedule profiles. How many heard about
the schedule profiles?
So that's not a lot. So uh schedule
profiles is basically a way where you
can uh capture these performance
profiles more in an automatic
non-interactive way in the background.
So uh you define a set of rules for when
the profile should kick in and then the
platform will handle uh triggering the
the profiling and that reduces the
manual collaboration with the customer.
It also reduces the time to mitigate and
another nice thing is that it does not
only support the interactive flows with
the user but also web services and
background tasks. Right? So if you have
a performance issues in a web service,
you could actually go in and monitor
that via a scheduled uh profile.
And so again, you can go to help and
support or search uh for now um analyze
performance with the schedule profile or
you can search for profiler schedules.
And that basically opens up uh a list
view where you can define the rules for
when to trigger a profile. And of
course, we're going to do new. And when
you then create a new profile, you need
to uh add some capabilities or some
rules to that. The first one in the
general uh section is that you can of
course decide whether you want to
activate this or not. You can still have
it linker there. Maybe you reuse some
profiles and you want to check after the
uh you fixed it or something like that
and rerun uh the this uh this profile,
but normally you would have it enabled
during the um the investigation. And you
can then set the time window in which
you want to profile in which it's
active.
Um you can also set some filtering
criteria. So you can say that you're
only interested in profiling a certain
user
uh or a certain activity type like
clicking in the UI or a web service uh
call. And then you have some advanced
settings where if you worked with the
profile in VS code or you work with the
incline profiler you might know the
difference between instrumentation and
sampling. So basically instrumentation
is that we monitor everything happening
even the smallest things that's
available when you profile from Visual
Studio Code. So if that's your need, you
need to use the visual studio code um
snapshots. Uh the um interactive
performance profiler and this uh
schedule profiles they use sampling. So
basically at any given interval fixed
interval every 50 milliseconds or
something like that it will look what is
happening now what is happening now what
is happening now and it would summarize
that afterwards. So that means that you
won't necessarily be able to see
everything that goes on, right? Because
if something happens at 40 milliseconds
and take two milliseconds, it's not
going to show up, but it will show the
longer uh longer transactions or the
longer AL code execution.
But you can you can influence that and
you can actually also influence uh
filtering out of the real small ones uh
small durations if you just want to
focus on the big things.
Um, so now we have a rule in the list
and it's active. Uh, and time passes. I
don't know how many recognize this. I
always see this Spongebob, you know, one
moment later, but I'm super old. So, I
played Maniac Mansion, uh, you know, uh,
that you remember the days of the
tentacle maybe. And this comes you
jumped in time basically. And later that
day, it said in that game. And so later
that day, somebody goes in and looks at
what was captured for that profile. So,
back in the rule and you open up uh the
the the the capture profiles and then
you can actually see what happened. What
did the user do? They clicked around in
the UI and it took some time and you can
see that right and if you find something
interesting each of these entries are
basically a whole profile, right? So,
you find something where oh it you know
it looks like opening customer list is
normally fast but in certain
circumstances it's super slow. This is a
slow case. I can then open that profile
specifically and you can open that uh
either in the sort of normal inclined um
profiler tool that I showed before.
Again, you can see which extension is
taking the most time. You can also open
it in Visual Studio Code if you want as
we saw in the beginning. And so that way
you can drill down and figure out where
is time being spent again. But the nice
thing here is you don't have to talk to
the customer and you can mine some of
these uh transient issues and you can
cover web services and background
sessions. Now uh right now we don't uh
have a way to go from this view into
source code. Maybe you want to
investigate source code right uh we
probably will add that sometime you know
blank has showed these open in VS code
from the client. This is an obvious
place to just have a hyperlink. you
click on the place in the call stack and
it will go to VS code and if you have
source access it will show you that but
another thing you can do which is
actually new in VS code uh for for this
season is that where you can search in
symbols so within Visual Studio Code you
can use CtrlT and then you can search
for say a customer page or the vendor
list or something like that and find
that and you might ask you know what's
great about that well of course you can
that that's nice that you can search but
um you can actually use it also for
context for GitHub copilot. How many are
using GitHub copilot in Visual Studio
Code?
Yeah. So, one of the nice things with
Visual Studio Code uh now is that with
GitHub Copilot, you actually have agent
support in there that can help you
refactor code etc. And you can provide
context. So you can actually uh link
with control t you can link in objects
like take this customer um er you know
table and create maybe a customer page
from this and instruct uh AI to do that
with these fields or something like
that. So it's a way to bring in context
which was hard before. So it's super
nice feature both for finding and for uh
for AI or co-pilot use. And again the uh
access here depends on the IP protection
just like blank talked about with open
VS code before. We'll talk about that in
a moment. But first I want to say for
all of you um it is a common pattern
with performance issues in customer
cases. We don't see as much adoption of
these tools as we would like when we get
performance issues into our support
organization. So please use the normal
profiling during development uh and
troubleshooting. use source of the new
schedule profiler uh to find uh the
issues. As I said, we have ak.msbt
bc troubleshooting. It'll if there's one
thing you remember from right now,
that's the link because it contains 20
tools that you can use across your daily
work on troubleshooting whether it's
debugging, snapshots, these tools or
others.
So, I mentioned uh ALS source and IP
protection. How many of you have heard
the term IP protection policy?
Not a lot. Okay. So, um
we're basically mainly talking about
apps source apps. Uh and as a publisher,
you normally want to protect your IP so
that others are not stealing uh your
effort. Um and so let's talk a little
bit through that sort of concept. So we
have you know we have normal
applications an extension here um and um
it could be an app source app or PTE or
dev. It's not really a PTE right in in
the IP protection but just in general we
have an app and you can deploy that to
the cloud one of the Microsoft cloud
instances that could be a production or
it could be a sandbox. You could of
course also uh take that app and deploy
on premise or to containers or local
installations if you're a developer
right
from these two environments. Uh
sometimes you need to use what we call
symbols. I guess you're all familiar
with symbols. Um it's basically a
reduced representation of the app that
you can use to code against. uh the
symbols can either come just with the
metadata or they can actually also
contain source code and so I alluded in
here that for the normal app we have al
source but it's offiscated but it it
does contain al source and it contains
resources that uh we heard Balash talk
about in raw format the symbols they
either contain the offiscated source or
no source and then also either resources
or or no resources if metadata only. And
then we have something called uh the um
runtime packages which are sort of like
a pre-ompiled thing where you can um
what it what it helps you is that you
can deploy something on an NST without
compiling it on the NST. It's a little
bit like a file for those of you that
know the old days. Uh and that contains
again the offiscated AL code. does have
source code and the resources and it
also contains C sharp which is generated
right for that specific version of the
NST that it was generated on which is
supposed to match the same version of
the NST that you deployed on. That's the
whole idea.
Um, now comes the important part. Well,
there's actually one more step. You can
of course also hand these out. Maybe you
don't deploy them yourself. You just
give somebody an app file. You can give
the symbols. You can give the runtime
packages. maybe as part of a partner
calling to get some CSC pipeline support
for them to test your functionality, you
can give them something.
But the important part is that when it
comes to protecting that IP, the only
place that we can protect that is
actually in cloud. When it comes to uh
local installations,
we cannot do anything from Microsoft on
that. Yes, the source code is obiscated
uh but that could be broken.
Furthermore, once it's installed, it's
on the NST in, you know, SQL tables on
SAS, you can't access that. But if
you're on a container or on premise or
something like that, you actually do
have access to the metal, right? So,
there are ways to get to that. We can
only help make it harder, but we cannot
guarantee it. And that goes also for
handing it out manually.
And so, let's talk a little bit about
what you can do in SAS uh to protect
this. We have a a property in the
app.json JSON of the file itself that we
call resource exposure policy and in
that one you can control whether anyone
uh you know whether the app can be used
in debugging whether it's possible to
download source or whether the source is
included in the symbol files when you
pull down symbols from the environment
from for instance visual studio code uh
normally we have set the defaults for
these are false to not expose anything
but actually they'll go uh project
template in visual studio your code will
typically have these enabled uh because
then you know it's a little harder to
start out with them having been
completely locked down.
Then uh another feature that we have is
that ISVS can actually you know what
what if you lock it down but you
actually need to collaborate with
partners or you need yourself to have
access to be able to troubleshoot on an
environment
and you locked everything down. What can
you do then? Well, then we have
something that we call uh sort of
dynamically granting access. How many
have heard of this dynamically granting
access?
Very very few. Uh how many here are
actually involved in making apps source
apps? Because maybe I'm talking to an
audience which is not doing a lot of not
a lot actually. Maybe that can explain a
little bit but but uh regardless um you
can dynamically do this. So we heard
about the key volt that you could set
up. We saw before how you can set it up.
If you have a key wall for your app, you
can put in a secret called BC resource
exposure policy overrides in that app.
And then you can actually specify or
grant partner access, specific partners
access to be able to debug or download
or get the code from symbols. Typically
partners don't want to grant uh
downloading source because it's a bulk
download. It's easy to get IP. It's a
little harder to in in in debug, but in
theory you could brute force uh fetch
during debug as well. But it is still
something where partners are in control
or publishers are in control on this.
And then you can take that grant away
after a period of time as well.
Um this is something that is not
supported on snapshots and profiling.
It's only debug on uh normal sandboxes.
And then very recently we applied this
to dev extensions as well. So if you
have an app source app and you want to
deploy that uh to an envir you locked it
down but you have your own environments
where you want to troubleshoot something
uh you can actually uh allow access to
that in the environment because normally
dev extensions are made so that you can
download source code because you're
supposed to debug and work with them. So
if you just dump a dev extension on a
customer's box, in theory they could,
you know, get access to the the source
code. And so you can apply the resource
protection policy to dev extensions as
well.
And just like with the dynamic granting,
you can do the exact same thing for dev
extensions. So you can grant yourself uh
that's typically the normal scenario.
You lock it down and you grant yourself,
but you could also grant uh you know
customer or uh partners you work with
their environments uh as well. uh when
we talk about dev it's more the tenant
that you grant access when we talk
normal resource policy it's more the
user that you grant access and in the
user case it needs to be a delegated
admin
so just to summarize the recommendation
for appsource apps is that you lock it
down I know that can create problems
with partners not being able to to debug
so it is a balance but for those that
you then know you could grant them
access temporary or forever basically
and you use the key vault uh to override
that uh and then really only share app
files externally with uh someone you
trust. When it comes to PTE uh I'm
urging you to from a sort of IP point of
view make sure that you know we see more
and more cases about disputes about who
owns the IP customer might not know you
know they want to move partner etc. I
understand parts of the lockin effect on
that but please make sure that um it's
very clear from the beginning who owns
the IP if the customer is leaving for
PTE cases and ensure that you have
source control also for PTE
preferably shared with the customer.
Yeah. So uh we just covered a fraction
of what is uh changed in the language.
We have a ton of information on the
launch event videos. How many are
watching launch event videos?
not a lot really a lot of content that
you can watch when you sit in the bus or
on a train or somewhere else. So, I
highly recommend that. Uh we talked
about the troubleshooting links uh you
know GitHub co-pilot and the law yeah
the launch events for the two videos we
have um
seven minutes for Q&A I think.
Awesome. And we have t-shirts. We have
t-shirts. Yeah. Thank you. Thank you,
Peter. That was very nice.
So,
we have t-shirts. Anyone want to ask a
question?
Oh, lots of people. I'm going to go very
far for the first one
just so you don't have to sit on the
first row to get a question. Here we go.
Let's see.
Catch. And then you get this one
afterwards. Um, you showed us that we
can move fields between pages or
extension. uh not between pages, between
extensions. Is this also possible to
merge table extensions into one
extension? Because we have the problem
that someone decided to create another
extension with if with we basically have
to move with us
and we want to move it into the main
extension. Is there a way to do this now
or is it still not supported? Yeah,
Blanket, do you want to answer that one?
There's an extra mic there if you have.
Meanwhile, you can get this one.
Does it work? I don't know. Hello. Yeah.
Okay, it works. Uh, yeah. So, you cannot
I I lost was the question. Try it. Yeah.
So, you can move a field from the base
table to the table extension and from a
table extension to another table
extension, but not from the table
extension to the base table because
that's not supported for this feature.
erh in a moment. So for your answer, I
guess that's a no. You could move all
the fields to the same table extension,
but then you will have the table and a
table extension.
Yeah. Thank you. Anybody else?
We have one here at the front row. Was
that
question? So you get a reward for
sitting at the front row. Here you go.
Yeah. I have I have a question regarding
this new app file properties with where
you can also link to your repository
what we saw on GitHub. Yeah. Is there
only GitHub supported or any GitHub uh
based repository?
Yes. So um the property itself is just a
string right? So that you can put
whatever you like in that property. Same
goes with the commit ID. You can put
whatever you like there. However, for
the opening VS code, maybe you want to
take that one,
the value of the GitHub repo property.
It's because I lost the question. Okay,
sorry. So, the question was whether the
the property for source control is only
for GitHub or there are other So, it's
actually for any git repo. So, it
doesn't have to be GitHub. It can be
GitLab or Asure DevOps. So, so that
works with any Git repository. Yeah.
Good.
Somebody want to ask a question without
getting a t-shirt.
There we go. Let's go over here.
Who was it over here? There we go. Yeah,
I'll get to you next.
There we go. concerning the data and the
the splitting of the tables into the new
app. Um when and how takes the data
update uh the data movement of the of
the existing tables place in the in the
um in the system where you update your
app. Is it is this done by um some job
queue or is it just by changing the name
of the table in in in in the background?
How is this done? Good question. Yeah,
it's a sync engine. Exactly. So upgrade.
So when you upgrade to the so in the
last step when you have a destination
table that up takes the new table and
it's actually the same table. It's the
same name SM ID. It has to be the same
but it's up taken from the new um
application. When that application is
upgraded to that version or installed if
it's the first time that's when it takes
a place that movement of data. Yeah. So
in the sync as part of the deployment
and
excuse me if you said so blanket but we
also sometimes hear about or get
questions about performance of this move
and the majority of the scenarios are
actually renames uh or very fast
operations on the SQL so not moving
data. Yeah for the field I think there's
something equivalent of the data
what's called data transfer. Yeah. But
normally, I mean, if you move a table
from one extension to another, it's
instant basically because it's just
renaming down in the SQL database, not
moving any data. Cool. Last one here.
Uh, I actually have a fairly
non-standard question about the language
server protocol implementation for AL.
Um,
yeah. So, uh, I'm I have a side project
trying to bring AL to other editors. Uh,
and I noticed that the deb debugger
adapter protocol and the LSP as well is
a sort of non-standard implementation.
Uh, any plans on making it one more
standard in the future? Short answer is
not right now and it's not in our scope
as it looks right now, but if you have
ideas, reach out and we'll we'll have a
talk about it. Absolutely. Might be some
improvements we can do there. Okay. So,
you have about 60 seconds to run out
before I'll start over with the next
session. But please stay. I mean, yeah,
exactly. Please stay. Yes. Let's go on
to the next one then.
