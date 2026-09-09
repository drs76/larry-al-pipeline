# NAV TechDays 2017: Azure Functions Deep Dive

- **Source:** https://www.youtube.com/watch?v=f10lFZtUWGE
- **Video ID:** f10lFZtUWGE
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 97m54s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Hello.
And welcome to Azure Functions deep dive
session.
This is the first session after lunch,
the best time to actually fall asleep a
little bit.
So, get relaxed.
Uh they're not serving popcorn here, so
I will I will try to make it as boring
as possible for you so that you can
really take a good nap.
My name is Vjekoslav Babic or uh simply
Vjeko. I've been an MVP for Microsoft
Dynamics NAV for uh 7 years. I've been
blogging for 10 years. I've been busy
with NAV for more.
And I'm I've usually been the the crazy
guy here at TechDays presenting crazy
stuff and and tips and tricks that
Microsoft hates. They're actually
nodding at me from the first row. Yeah,
yeah, that's what we do. So, this year
for a change, I'm not doing a black belt
session. I'm not doing anything crazy.
I'm actually just doing something
interesting and easy. So, what is this
session going to be about?
Uh well, obviously Azure Functions.
That's what the title says. So, what
about Azure Functions? We'll talk about
what they are.
Uh we'll talk about how to use them, and
we'll talk about why we would want to do
that. And this session will have some
theory, of course. It will also have
some practice,
of course.
So, uh what are Azure Functions?
Well, um
if you ask Microsoft,
uh they might not tell you exactly the
first thing that comes to mind. Azure
Functions are
FaaS or FaaS. This is a yet another uh
buzzword from the as a service
uh collection. As it stands for actually
function as a service. So, if you've
never heard of what function as a
service is, then maybe you've heard of
this.
Serverless architecture. That's what
Microsoft would tell you that
uh Azure Functions are. And then you can
ask like, how can it be serverless
architecture? What kind of sense does
that make?
Well, um also you could think like
serverless architecture, it's something
like uh look ma, no hands. I don't need
a server." Of course, you need a server.
So, what is serverless architecture?
It is a concept in which you do not need
to worry about server or about
provisioning any specific hardware at
all. It is, of course, cloud-based.
Uh it is fully event-driven. It is
stateless.
It is short-lived and it requires
theoretically zero administration.
So,
um
what does this all mean? Uh it means
that uh I mean, in in what way is this
actually different from other things
that we know from this as a service
stack? Like, what why is this different
than software as a service or platform
as a service? First, this is not
platform. Uh platform as a service gives
you facilities that you need to uh to
utilize to actually make something work.
Azure itself is platform as a service.
Software as a service typically requires
you to configure virtual machines, to
configure big fat applications or
things. Here, with functions as a
service or serverless architectures, as
you will see,
you actually have very light, thin
layer. Everything is running in
containers. Nothing is running in
virtual machines. Everything is really
provisioned on demand. So, resources are
provisioned on demand. They are assigned
on demand. It is very lightweight,
fairly fast, as we will see. So,
um this is a little bit about what
serverless architecture is.
Let's now talk a little bit about Azure
Functions and let's see what they are
and what they allow us to do. So, first
thing that we could say about Azure
Functions is that they allow you to
choose any language you want to write
them in. So, actually not any language,
but uh
a lot of languages are out there for our
disposal. You can use C#, you can use F#
if you for whatever reason want to. Or
you can use Python, or you can use
JavaScript or TypeScript or PowerShell.
I know that Waldo would like to do that
in PowerShell. So, there is really a
number of languages that you can choose.
It doesn't care. Funny thing is, you can
provision one application for function
services and then have one function
running in JavaScript, one in
TypeScript, one in C#, and one in
Python. It's also completely legal
because they are all completely
detached. We will see how that works.
Also,
um I would like to address this um
financial thing up front. Uh it is
actually very cheap to run. It's almost
next to free. Um you have 1 million
invocations per month, and then after
that you pay something very little. So,
uh essentially for testing and for most
typical uh use cases that we in NAV
world may come up with,
you will just perceive them as free.
So, they have this very affordable
affordable model. We can discuss it in
detail if you want during
uh Q&A part. Then, um
we can also use dependencies. It means
that when writing those functions, we do
not necessarily need to contain all of
our code in the same place. What we can
do, for example, if we are in
JavaScript, uh it's actually running on
Node.js, so we can use NPM to pull any
dependency we want. Or if we are in C#,
we can use NuGet to pull any dependency
we want. We can even build our own
dependencies, which is the nicest thing
of all, especially for us in the NAV
world, also something that we will see a
little bit later.
Uh it comes uh with integrated security,
which means that you can secure access
to those functions. That's also
something that we will address in a
little bit more detail. So, it supports
uh all authentication uh with a number
of providers, and it also allows you to
uh secure it
uh uses uh using access tokens.
Also, we have flexible deployment.
Uh
sorry, flexible development. Uh we will
see that we can use a number of options
to write functions. We can actually do
them in browser, or we can use a
full-blown uh development environment
such as Visual Studio, for example. And
finally, we have um
this open source platform that function
Azure Functions are, which means that
they are completely open for anybody
else to to use, for you to use, for you
to contribute if you want. So, here is
the GitHub uh repository where uh
Microsoft is actually maintaining the
entire platform. So,
uh it's currently in development, it's
constantly in development, it is being
changed uh as we speak. Uh one demo
broke for me. Uh I hope it will work
later on, and I can only blame it on
things being changed in Azure Functions
platform. So, let's see when we get to
that point. I will give you an advanced
warning about this demo. So, uh
yeah, I have to
do some uh
some lame uh excuse before a failing
demo. Anyway, uh
this is a little bit about what Azure
Functions are and how they actually
work. How do we
invoke Azure Functions? We have a number
of ways, and they are actually not just
intended for us to replace our NAV
stuff. Uh we have a number of Azure
triggers that we can attach them to. So,
when something happens in Azure, your
function can execute. Or uh we can use
web hooks, like uh GitHub hooks or
generic hooks. If there is an
application that publishes a web hook,
you could attach uh Azure Functions to
to that hook to execute your own logic
when some event somewhere happens. And
also, you have those other triggers, uh
which are timer, and the most important
one of all is HTTP request trigger. This
is the one that we will spend actually
the entire session today talking about.
So, plenty of different ways how we can
invoke those functions and how we can
make them run.
Um talking about their architecture, it
is nothing complicated. We have uh
applications. So, all of the functions
are hosted in in applications, but those
applications are not
projects or source code applications the
way that you
are familiar with when you develop
stuff. They are simply containers that
combine some settings and security and
authentication options. They simply
contain your functions, but they do not
applications themselves and themselves
do not have any code. So,
they are simply
containers or placeholders where you
will store your functions that simply
simplify administration of all functions
by applying specific settings that apply
to multiple functions at once.
And then once you have an Azure function
application, you can define multiple
functions as many as you want within a
single function application.
So, each function comes with its source
code. It can has have its own language.
It has its own access keys.
It can specify its own triggers and has
it can have its own bindings, etc. So,
you can monitor it individually. Every
single function is individual. You
completely manage it as an individual
entity. So,
this is a little bit about Azure
functions in theory. So, let's take a
look at the first demo. Let me stop
talking and let me actually show you how
those functions work.
So, I will go in my Azure virtual
machine
where I will be writing some code. And I
will start by simply creating an Azure
function application. I have a few, but
I want to show it from the start so that
you can see how easy it is to actually
get started. So, we'll just click new.
And then in the list of
things that I can create, I will select
serverless function app.
And here I will give it a name. I will
say Tech Days
2017.
Oops, taken. What do you know?
So, NNV Tech Days 2017. This is not
taken.
Then I will choose location. I will put
it to West Europe. This is closest I
think to us.
And then I will select
an existing
storage
group.
This one is fine.
And I will create this application. So,
once you click create, it will validate
if everything is fine and then within
couple of seconds, half a minute, you
will have your application uh in there
you will be able to use its resources.
Let's wait for
those couple of seconds.
I will click on function apps here.
And maybe it's already there.
Let's take a look. Not yet.
I'll give it a little more time.
Okay, it says deployment succeeded. Go
to resource.
And here I will be now in my um Azure
function. So, it's complaining about I
have take this it's saying something
whatever.
So,
let me see if it's Yeah, it's listed
here. That's fine.
Good.
Once I am in my
Azure function application, I will click
this functions and then this plus right
next to it.
So, it will ask me what kind of function
do I want to create? There are a couple
of options. It selects this web hook
plus API, which is in fact an HTTP
trigger function. So, I will select
that. This will allow me to invoke it as
if it was a web service. This is a
primary thing that we would want to do
from NAV anyway. And then it asked me
for for the language. I will go with C#.
And I will just create this function.
So,
at this moment it creates the function
and shows the source code to me.
So,
it will be a piece of C# code
that I will be able to to start invoking
immediately. So, um
there it is. So, this is my very simple
C sharp function. It receives uh a
parameter either through uh
query string or or through uh request
body.
And I can pass either of those. If you
want to invoke it, you can click this
get function URL. Then you simply copy
this URL. I will try it immediately in
my browser. I'll put the function here,
and then I will add name is TechDays.
Enter. And it tells me, "Hello
TechDays." Okay, it returns some
um XML in a string. I don't know. I
think it's just um my um I think it's
simply
Chrome that shows it that way. If I open
it in Explorer, I'm pretty sure I will
not see this XML. I don't know. Why is
that?
No.
I cannot even do that.
Let me see.
Ah, okay, it wants to open it. Yeah, it
receives some JSON from there. Never
mind. It works. So, I've seen it here.
Good. So, that's how easy it is to
actually uh create a function and invoke
a function from the browser. But we are
not invoking them from browser. We're
invoking them from uh NAV. So, let's
actually go into
our AL development environment, and then
let's invoke this function.
So, I will start by creating a new code
unit.
So, it will be
code unit 50,102.
My demo.al. Inside of here, I will do
this code unit. I will
invoke demo function.
And then here I will paste my URL. So,
let's take the URL.
Copy.
I'll paste it here and add name is
Yekko.
Okay.
I save that.
So, this is
50,102 my Azure function demo. I have
prepared
a page extension for my order processor
role center. I will simply invoke this
code unit from here.
My Azure function demo.
Let's make sure everything is in place.
On run will invoke this. It will show
the result in the message. So, yeah.
I feel confident it will work. So,
let's take a look.
So, I'm deploying this.
Signing in.
And then I have this invoke Azure click.
Hello Yekko. What do you know?
It's that easy, in fact. So, good. Job
done.
Questions and answers.
No, no, no, no, no, no, no,
uh I have two more slides to to show.
Okay. Um
So,
that was
how easy it is to actually get started.
It takes all 15 seconds plus plus some
popcorn time until it actually deploys
all the resources. So, how do we develop
those functions? Obviously, we can use
web browser,
go into Internet Explorer or Chrome and
then just write some code in there and
you
probably do not like that. Me neither.
So, you would not use web browser to
actually write functions.
Uh Visual Studio Code is amazingly
popular platform and actually very very
nice platform. It also has support for
uh Azure functions, but it's very weak.
So, I would also give it uh one big fat
uh no mark over it because uh you cannot
just do everything from Visual Studio
Code. You can do some things, but not
all.
Not yet, at least. I'm pretty sure it
will be possible.
There are other environments uh that you
can use to to work with Azure functions.
I don't know if you develop for Python,
you could use some environment other
than Visual Studio Code or if you
develop for Java or if you develop for F
sharp, you probably use Visual Studio,
but what do I know? So, uh there are
those other development environments
that certainly will work, but what I
will actually spend most time today is
Visual Studio. So, we will do some
Visual Studio development where we will
see how nicely Visual Studio integrates
with Azure. Not not just Azure, but
actually specifically Azure platforms.
Visual Studio Code comes with Azure
development workloads. It allows you to
easily create Azure projects of
different kinds, and we will see how
nicely in the latest release of 2017, it
actually allows you to develop and
manage Azure functions. So, how does
this Visual Studio development workflow
look?
You start by creating a function app
project. So, that's the holder of your
functions.
Uh there is a template for that. You
don't need to install anything
specifically. When you install Visual
Studio 2017, if you tick off this uh
Azure uh during setup, everything will
be configured for you. So, um you create
this Azure function app project from a
template. Then in that project, you
create a function,
which is an object, which is in fact
just um a file uh of extension CS. I'm
not sure if you can actually do
JavaScript or F sharp or other types
from Visual Studio. I never tried, so I
cannot say no, but I cannot say yes
either. So, C sharp is supported
natively. I don't know about others.
Then, when you do that, you typically
test locally before you deploy. You can
simulate Azure environment on your
machine, and then when you do, you can
easily connect to that. You can you can
see if everything works. And then when
you are ready, you publish that to
to some
application that is available in Azure.
So, let's take a look at how we develop
Azure functions using Visual Studio
Visual Studio, sorry. Visual Studio,
real Visual Studio.
So, I will go here in my Visual Studio
and I will start with a new project.
So, the project type I've selected this
Visual C# and Cloud then Azure
functions.
And then I will just call this
simple demo.
I will click okay.
And I will wait a little bit until
everything sets up.
So, it seems that everything is now set
up.
And I will right-click my project name
and then click add and then click new
item then Azure function is
automatically selected so I'll keep it
as is and I will just call this function
hello
there, not hello world. I hate hello
world. So.
Add. Now, it asks me a couple of
options. What kind of function is this?
What kind of trigger it should be? So,
I'll select HTTP trigger.
Access rights, I will just say
anonymous. We'll talk about security
later and then I will click okay.
So, this pretty much looks like what
you've seen in in the web browser except
that you have full intelligence support,
access to all the libraries and
everything
from here so it's much better to
actually do it in inside Visual Studio.
Good. So,
that much for actually writing it. I
will now run. I will press F5.
And when I press F5
this will build and
oops.
Oh, I didn't see this coming. This is a
fresh machine that I never It was a
clean machine so
apologies for this. This will take
a little while. So,
while it takes a little while,
let me actually see
what's going to happen. Yeah, it it's
working fine.
Good.
So, this is my local Azure simulator.
This Azure simulator will
bring up all the necessary
infrastructure to simulate Azure as if
you're invoking Azure. And here it tells
me for all of my functions that I've
exposed, it gives me this URL. So, I
will select this URL.
I will copy it to clipboard, and then I
will simply change the URL in my Visual
Studio Code.
So, I will exchange this
with this.
Good.
So, I will
actually uh
Let me do something else. Let me stop
this.
And then let me do just minor changes
here to make it obvious that I'm
actually working off my local machine,
not from from that application that
we've seen. So, hello.
I will just put hi, and I will press F5.
So, it will now redeploy locally.
My NAV is already deployed, and it's
waiting. So, when my function is up and
running, which is now,
I can actually click this, and I will
see
Good.
So, that didn't work. Let's take a look
at
Yeah.
So, you all like this error, right?
Let's Let's try to see what is happening
with this. I will go back to my
AL,
and I will copy this.
Function is running, and I will just try
to invoke it from here to see if
everything is fine.
No.
No, it
Uh there is question mark.
It's there.
So, it's not about question mark.
It
No. Look, uh
well,
one more demo down.
So, trust me it would work.
But this wouldn't be that exciting
anyway. Like, this is just to show that
you can do that locally. This is a
virtual machine and I will I'll blame it
on that. Uh
it does work. It is easy to actually do
it this way, but you would eventually
want to put it into Azure. So, uh
when you put it into Azure, when you
actually uh deploy it, sorry, uh
you will be able to
invoke it directly from this Azure
infrastructure. So, let's actually do
that. Let me stop this local simulator,
which refuses to work for whatever
reason.
So, there are no compiler errors, it
would not run. So, I will simply just go
and deploy that. So, to deploy that to
Azure, you right click the project
again, then you click publish,
and then it asks you if you want to
create a new publish a new application,
or you want to select an existing
application. I will use the same
application that I have um used uh
previously, so we'll just click publish
on existing application. It will connect
to my Azure um
subscription,
and then it will ask me
Come on.
Okay. Uh then we'll load all of my
function apps, and it will ask uh it
will ask me which function app actually
all of my resource groups, and then in
each resource group, it will allow me to
select
an application. So, I'm deploying it to
the same application that I've created
earlier. This is to show that you can
use the same Azure function application
to deploy both from Visual Studio Code
and to create uh new functions from web.
It will not conflict out. If each
function is individual. And the fact
that you have this project for Azure
functions in in Visual Studio does not
mean that it has to be blank fresh uh
Azure application out there in Azure.
So, let me just select this and click
okay.
It will now create create my publishing
profile. Uh sometimes it takes a little
while. So, uh what does this publishing
profile do? It connects to to the Azure
application. It reads its settings. And
it prepares um everything on my machine
so that when I need to publish, it can
just invoke couple of services in Azure
and push my source code there. There is
going to be a difference between my
function that I created in the browser
um and again, my function that I created
in and Visual Studio. Because when
Visual Studio publishes the function, it
doesn't publish the source code. It
publishes binaries. So, source code is
available only on your machine, not in
the Azure.
So, uh if you want to maintain and
manage source code, um
you really have to to do that inside of
um of your
web browser environment. So, that's the
only way where where you can see the
source code of Azure uh function in the
browser. So, let me actually demonstrate
that. Let me click publish. So, when I
publish this, it will not take too much
time.
And my my function will appear
inside of the list of my functions
for this function application. So, when
I click my function application
and then functions,
okay, it still didn't
refresh, so I will try to refresh.
And if I click functions, I can see that
I have hello there.
And when I click hello there, I actually
just see this JSON configuration, which
uh allows me to configure the the
endpoints, but it doesn't actually show
me the source code. As I said, the
source code is not available in here.
You can actually see all the files for
for this function if you click here and
then
uh you browse. However, you cannot see
you can see that there is just this JSON
file, so you cannot access anything but
that. If you go to storage directly into
the storage account where this function
is stored, you would be able to find the
bin folder and and everything that Azure
infrastructure is actually storing, but
you you cannot access the source code.
So, uh I will copy the URL from here.
Let's take a look if it's demo gods or
it's my Yeah, now it works again. Whoop.
Yeah, I didn't pass
anything, so I'll just do name equals
TechDays.
And it returns hi TechDays. So, I will
just
use that URL, put it back into my
Visual Studio Code, save, compile,
and
with a little luck,
it loads.
Sign in.
Click Invoke Azure,
and hi vehicle with all the differences
that I've done in this specific uh
project. So, that's how easy it is in
fact to uh
develop functions using Visual Studio.
So, you do everything locally. When
you're happy with the results, when you
complete testing, you simply publish.
Publishing will take like half a minute,
and then you have your function up there
in the Azure ready to serve your
requests.
Good.
Can we debug that?
Well, if it's running locally in this
local
similar environment, of course you can
debug.
That's why you have it.
But, can you debug it remotely? Yes, you
can debug it remotely and you can debug
both the version that you have written
in the browser and you can debug the
version that you have built using those
binaries. So, all of these options are
possible. I will not demonstrate local
debugging,
but I will talk about how to actually do
remote debugging. So, when I say what
this demo is not going to be debugging
my local Azure demo environment, it will
actually be debugging Azure locally from
from my machine.
So, in fact, no. I will not be able to
demonstrate this because my local
machine does not want to load. Anyway, I
will skip this part and let me talk
about remote debugging. So, imagine that
my
demo Azure worked on my virtual machine,
which for some reason it does not want
to do. So, I would be able to hit the
breakpoint and then run from NAV, it
would stop there. But, I will show that
from remote. How do we configure remote
debugging?
There are two settings that you need to
be careful about. The first setting is
when you publish your function, you need
to specify this debug. So, if
if you want to start debugging, it's not
enough to just use the debug
configuration of your project, you
actually have to specify that the
publishing configuration is also debug.
If you don't do that, you may not be
able to debug.
The second thing that you have to do is
you have to switch off this enable just
my code setting in the debugger of
Visual Studio. So, if you don't do that,
again, you will not be able to debug.
Depending on your configuration of
Visual Studio, Visual Studio may
complain and not tell you exactly
nothing about why it's failing. It gives
you some obscure error messages or it
may give you an exact error message
which tells you both of these things.
Like switch this debug
configuration on and switch off this
setting. But again, it depends on how
your Azure tools are configured.
Uh this works in 2015 and 2017. And uh
in 2017, it's at least polite and it
tells you what is wrong when something
is wrong. So, I have uh configured this
uh debugger option already. Let's take a
look about
how I uh how I can publish this for
debugging. So, here I can see that my
configuration is release. So, I'll just
click settings and I will change this to
debug.
I will save that and then I will publish
my
function again.
So, once my uh function is published
and it's in debug mode,
I can use Server Explorer
to expand this Azure node and then App
Service node and then
when it refreshes,
I will see the list of all of my App
Services
where I will have to find
the application that I've created, which
is NavTechDays2017.
So, I select that and then
this is actually resource and No, this
is App Service. This is the application.
So, I right-click the application and
simply say attach debugger.
And that's all. So, this may fail and I
hope it fails so I can show you how to
fix when it fails.
So, let's take a look.
I- If it doesn't If it doesn't fail, let
me just explain what you can do if it
fails. This fails if your application is
uh already set in debug configuration on
uh Azure
Azure portal.
And sometimes, for whatever reason, and
again, this is probably because this is
still being developed, um it just
doesn't catch this debug setting from
there. It tells you that debug setting
must be switched and it is switched. So,
what you need to do is simply go into
that portal.
You go into the application.
So, you select the application.
Then you select
function app settings.
Um I'm sorry. I apologize. You select
Just a second.
Overview, application settings.
And then here you select remote
debugging on. You don't need to specify
version of Visual Studio. It will be
automatically specified by Visual
Studio. So, here I can see that my
um Visual Studio is running. So, it is
successfully attached to the process.
Sometimes it would complain. It would
tell you that it needs to be in debug
mode. And it is in debug mode. So, if
that happens to you, you simply go here,
switch debug to off, save configuration,
go back to Visual Studio and reattach.
And then Visual Studio will reconfigure
everything and it will work. It didn't
fail now, so I can just start debugging.
So, how do I debug? I simply set a
breakpoint. So, I will set a breakpoint
in here.
And then I will invoke
again this function from NAV. I will
click invoke Azure and you see that my
Visual Studio is blinking. So, obviously
um I'm now debugging my Azure instance.
I can step over. I can see that I have
received this name from query string.
It's Vieko. You cannot change that.
Remote debugger for Azure doesn't allow
you to change the values uh in the watch
window. So, I'll just press F5. There is
nothing going wrong in here. It tells me
hi Vieko. So, that's how easy it is to
debug
source code. Uh actually, how to debug
functions uh when they are published to
uh to Azure. And this is Why is this
working? Well, you have published your
binary. Your binary contains your debug
information, and when you attach a
debugger, it will match that debug
information. It will know that this is
the solution that you're debugging. It
will know where exactly to stop. But
what about the solution or the function
that you actually wrote in the browser?
So, if you remember,
I was in the browser,
and I created this function called HTTP
trigger C# 1,
which allows me to see all of this C#
code. Can I debug that? Yes, you can
debug that as well. So, let's take a
look at how we can debug that specific,
uh, function. So, I will just now detach
my debugger,
and then I will expand
my, uh,
function application, and then I will
look at files.
So, when files refresh, I will see them
grouped by function. I will expand my
HTTP trigger C# 1, and here I will see
this run.csx.
That's my source. So, I will double
click that.
Answer no when it asks you if you want
to fix those line breaks. You do not
want to fix those lines line breaks. If
you do that, the
debugger will not be able to attach
because it will notice the difference
between the source and debugged file.
So, just click no, accept it as is. And
then you can set debugger breakpoint in
here.
And again,
I will attach
my debugger.
And then I will just
copy this URL again,
so that I can paste it
in my
URL parameter in here. And let me go
without this vehicle.
Okay?
So, I now do not have the necessary
content inside of my AL code. So, I will
invoke it intentionally with a problem.
Good.
It runs.
I will click uh, invoke Azure
and it stops.
So, I'm now debugging this web created
plain text code. So, I will step over.
String name will be blank, so it's null.
It also doesn't read anything from my
content request content. It's also null.
So, here it will check if name is null,
it will return this response which is
bad request. Please pass the name on
this query string, etc. So, I can just
go on and receive an error in here. So,
it tells me please pass the name,
whatever, blah blah.
So, that's how you debug Azure
functions. Again, very simple. It's easy
to configure, easy to start using. So,
good.
What else shall we talk about?
Okay, yeah, yeah. I've just demonstrated
that. Thank you.
Why do we need Azure functions? So,
that's um
an important question. So, um serverless
architectures
and function as a service as a as a
concept and Azure functions themselves
are a very nice way to actually
integrate different service workflows
where things are happening distributed
on multiple applications, on multiple
platforms. You can easily connect them
and have certain things happen,
especially when you use webhooks or
Azure events.
This is something that, of course, we
may want to do.
We may want to attach them to common
data model or we may want to attach
them, I don't know, to to anything that
you can think of.
But, um
the the more obvious example is to
provide web APIs. If you think
of how we developed software 15 years
ago. If you were a vendor who was
building some API, you would typically
ship it as either
an automation API or later as .NET API.
These days you would not probably ship
it as .NET or anything. You would just
ship it as a service API. So, you would
just
make a service application that is
invocable that has provide some rest
endpoints that your customers can
consume. So, this is number one reason
why you would want to also use Azure
functions. So, they are very easy as you
have seen to to expose, to create some
functionality in there, to make it
possible to to invoke your API, whatever
that is. We will see a couple of
examples of what that API can be just in
a few minutes. So,
this is probably the the the number one
reason why people would
start using Azure functions today.
We in AL world in in .NET Sorry, in NAV
world, we have
a more burning reason why we would want
to start using something like Azure
functions. And this is this, replacing
.NET interoperability.
So, let me just now try to wake you up a
little bit. Let me see, who has ever
written a .NET interop library to be
used with NAV?
Okay. Yeah.
Yeah, quite some of you.
So,
now all of you who put your hands up,
put it back up if you are happy with
managing the deployment of those
assemblies.
Okay, I have I see three hands actually.
The
four hands.
Microsoft doesn't count. So, we will
talk about that. I want to know why you
are happy. So, there are a number of
problems with
with those assemblies that you build
yourself when you want to make them
available. So, for example,
the most obvious one is that if you
change anything, it's a very breaking
change for all of your CIL code. So,
when you change your
uh
your assembly, a good practice is to
version up. And when you version up,
then you break all of your CL. You have
to recompile that. Actually, you have to
re-reference everything. So, if you're
lucky, if it's easy, you will export
your objects as text, then do a search
replace all with the new version, then
import, then compile. And again, if
you're lucky, it will work, and it will
be just 5 minutes exercise. If you're
not lucky, if you're versioning up
multiple things at the same time, it
will be a longer process. So, it's not
that easy. But, that's just the first
part. First part is easy. You fix that
versioning up. Now, if you want to make
it available to uh
your users, you need to deploy it on the
server.
If you're using direct deployment on
server in the add-ins folder, you will
first have to stop the service tier,
then put your assembly there, then start
the service tier.
Also, uh you may want to use database
deployment, which
is kind of a simpler way. It doesn't
require you to actually have physical
access to the server. But, then you have
another problem. You have problem with
dependencies. If your assembly is using
external dependencies, and those
dependencies are used across multiple
assemblies that you use, you will have a
lot of problems. It is possible to
solve, but not not easy. And once you
solve that problem, there is a big, huge
wall that you just cannot come over.
It's called Dynamics 365.
Okay, we don't have extensions V1
anymore in in Dynamics 365. But, let's
talk extensions in general. If you want
to have your extension
use your .NET assemblies, you just
cannot make it work if you have
dependencies across assemblies. It just
doesn't work.
You can have one dependency that is used
from one assembly, but if you have the
same dependency used from two or more
assemblies, it just doesn't work.
It will not allow you It will allow you
to build your extension, but it will not
allow you to publish. And Microsoft's
statement is won't fix.
And I understand they do not want to
fix. Why? Because uh .NET interop is
going away.
Uh Uh, in extensions V2, there is no
more .NET interrupt. If we talk AL
language, there is no more .NET
interrupt. So, uh, not only it is a very
painful process to maintain our .NET
assemblies.
Uh, we now have a very burning reason
why we would not want to use them
anymore. That's just because AL language
doesn't support them yet. And
when I learned about this for the first
time a year ago that Microsoft is going
to kill support for .NET in, uh, AL
language,
uh, for me it was like the end of the
world, literally. If if you know me from
earlier, you know that I've been talking
about .NET in this way or another at
TechDays since the very first TechDays.
So, I I think I had like six sessions
about .NET here and two workshops or
three. And, uh, for me it was,
"What?
No .NET? What?" And then Freddy told me,
"Look, you don't need .NET.
Uh, you actually need a solution for
your problem.
So, .NET was a solution. Let's talk
about another solution. Let's see why
you need .NET and then let's solve the
root cause." So, uh,
why do we need need .NET? The question
is, "What is .NET good for? Why do we
actually use that?" We use that to
do classes of things. Number one is to
invoke web services. So, if you want to,
uh, invoke a web service, we need .NET.
Then we do some string manipulations,
then we do maybe, uh, some collections,
whatever. There's a number of categories
of tasks that we do with .NET that
Microsoft has started replacing on AL
language level with functionality that
we can invoke directly without .NET,
which actual actually is not just a
replacement for dot .NET. It's actually
implemented in a correct way. If you
are, uh, a .NET guru or ninja, you know
that .NET interrupt actually uses uses
reflection all over the place. And
reflection is hundreds of times slower
than direct access to to same
functionality.
So, uh when you're using .NET Interop,
your .NET will not run as fast as it
would run uh without at least
uh if you are invoking individual
functions on .NET variable. If you embed
everything in one single function in
.NET, it will be good enough. But, if
you're invoking multiple things in a
sequence, for example, you have a
dictionary and then you feed thousand
elements into that dictionary, it will
be much slower than if you do it from
C#. Just because it's using reflection.
Uh
what Microsoft did is they provided a
number of wrappers for us that we can
just start calling now from AL. Things
like HTTP client that I've used here in
this uh example today. Or JSON, or XML,
or many other things. So, uh all of
these wrappers are non-
reflection-based. They are real things.
So, they are fast. So, we have now
received from Microsoft very good
replacement for a lot of .NET, but not
for everything.
And for those other things that we still
cannot solve with AL language, well, we
have Azure functions. And that's why
they are interesting to us. Because we
can now start replacing um our C# code
inside of our assemblies with C# code
in other kinds of assemblies. So, it's
going to be a very easy task, as you
will see.
Uh
So, we have many many benefits, I would
dare say. Uh not only that uh
we have a faster solution, native
solution that works on AL language
level. We also have a possibility to
decouple our code. So, it's not tightly
bound, intermingled, all together,
assemblies with versions and everything.
When you have an Azure function, you've
seen that I've changed the same Azure
function couple of times. I didn't need
to restart anything. I didn't need to
stop. I didn't need to deploy anything
new. I just changed URL. And sometimes,
depending on how you write your
application, you may not even need to do
that. So, it's all up to you. So, Azure
functions are really a very good
replacement for that part of .NET stack
which is not yet replaced by Microsoft.
Mind you, Microsoft also wants to
introduce more and more functionality in
in this
AL language .NET replacement stack, but
still Azure functions are going to be
number one way to replace those things
which are not natively
supported by AL language. So, how do we
replace .NET? If we have uh
some code that uses .NET. We have two
possible situations. The first possible
situation is that we have some code
which uses what I like to call CAL.NET.
It uses a bunch of .NET variables of
this and that type, and then we
write everything in AL. We don't have
any external dependencies. Everything
that we use is from .NET framework
stack, native .NET framework stack,
which means we can run it on on any
server without deploying anything to
add-ins. If we use that,
then we will have a little problem. So,
we will first have to do something with
it. This is more complicated situation,
at least for migrating to Azure
functions.
The simpler situation is if we have
everything already written in C#, and
then we have an assembly which we are
simply consuming from AL. So, in AL we
have one or maybe two or three variables
which are of .NET type which reference
that assembly, and then we are invoking
it from there. So, that will be a much
simpler thing to replace. And let's see
how we actually approach these two
situations.
The first situation is if we have CAL or
CAL.NET.
If you want to replace it with Azure
functions, this is what we would have to
do. First, we would have to start by
translating this to C#.
Because
eventually your function will be C#, and
then when you have it in C#, uh
you can start running it. But if you
have it in
sorry in
CAL.net,
it is worthless. So, you will not be
able to use all of those variable types
anyway. So, first step is create a new
solution,
put your CL C# code in there, translate
your CAL into C#, then build it, then
deploy that,
and then refactor your CAL to actually
use the Azure function that you have
created. Or actually sorry, not Azure
function. The first step is to actually
refactor to use your assembly. So, you
need to get from CAL.net to real.net so
that you just replace individual calls
with one .net call.
Good.
Let's take a look at how we would
approach that problem. So, let's replace
.net
which is completely written in CAL with
some Azure functions. So, the first step
is not going to involve Azure functions
at all. The first step will involve
exclusively CAL and C#. So, let's take a
look at what I have here. I will go to
items,
and then I will open this
touring bicycle.
And then I have a function
called upload image. So, this upload
image is this code unit written in CAL,
which has quite a lot of .net.
So, this is completely written in
CAL.net, if you want. It has no external
dependencies. I can just take this FOB,
deploy it anywhere, it will run.
So, if you take a look at what kind of
variable it's using, I if I go here, you
will see that it has quite a number of
things that it uses from .net stack.
So, when I
click this upload image, it will invoke
that code unit. It will ask me to select
an image. I will select an image. This
is a bicycle image, which is fairly big,
and I do not do not want to have big
images. I will first resize it and then
I will crop it to 300 by 300 pixels. So
that's what my function does. So there
it is, my touring bicycle.
I can actually verify that it is resized
and cropped by pasting this image in
here. I can see that it's actually
300 by 300. So
this AL code or CL code has done its
job.
But this is not good because
I cannot really turn that into Azure
function that easily. My first step is
to turn that into C#.
And then try to have exactly the same
functionality from CL by invoking that
C# that I have to deploy.
So of course I will not do it step by
step because there's a lot of code. I
have prepared that project. So I'll just
go to my Visual Studio
and I will open
Just a second. I will Oops, I have to
stop my
or detach my debugger first. So I'll
open this Tech Days 2017 solution.
And here I have exactly the same. I have
two classes, the helper class which just
handles the stream part of everything,
which is if you take a look at this,
it's
in essence the streaming part.
And then I have this
image manipulator which does this resize
and scale and and crop and whatever
needs to be done. So this is my AL just
translated to C#. Then I have deployed
that C#.
I have changed my CL code so it now
looks like this.
So everything I have from .NET is this.
I have these three types.
Uh
I have to retain at least some .NET in
here because otherwise I wouldn't be
able to perform everything, but that's
not going to be an obstacle because I
will handle it easily from my Azure
function. So let's take a look at what
happens if I invoke this other function.
So it's exactly the same code. It's just
my .NET now is executing my C#. So, when
I click this
import image C#. Okay, actually let me
get rid of it first.
So, I will upload image from C#. The
same image. It will be exactly the same
result because it's the same code
executing this time from C# not from
CAL. So, that's the first step. You need
to get your stuff completely in C#.
And then, what do you do then? What do
you do when you have it in C#?
Well, now this the easy part comes.
So, once you have your functionality in
C#,
you create you actually take this same
solution that that uses that that you
have just used from from CAL. You simply
add another project to that solution,
which is of Azure function type.
And then, inside of that project you
reference your original C# assembly.
And then you publish it.
So, that's all.
And since you're using this dependency
that you've just written for yourself,
and since this is all C#, and since this
is all just supported by .NET natively,
and since Azure functions do support
.NET natively, it only takes those few
steps. So, let's actually do that now.
So, let me actually demonstrate how to
now use this new solution that I have
created to
move it all to the cloud and enable me
to use this functionality that that I
have completely had in CAL,
how I can do that from uh
from AL language in uh extensions V2.
So, I will close this, and I will
simply
right click my solution, click add
new project. I will select Azure
functions.
I I simply call it
Azure
manipulator
and click okay.
There I have it.
When it completely builds
so I will know that when this
dependency's warning sign goes off. So
now it's completely built. I will right
click dependencies. I will click add
reference
and I will simply select this project
and then image manipulator. This is my
C# project, the one that I've just used
from CLI.
So I reference it from here.
Then
I right click my image manipulator
sorry, Azure manipulator and click add
new item and select new function.
I will call it
scale and crop exactly as it was called
earlier.
I will specify that it's an HTTP
trigger. I will specify that it has
anonymous access rights and I will click
okay.
So
there it is, a function that does this
hello world. So instead of this hello
world, of course, I have to now put this
streaming part of
logic, which is simple. I have copied it
in here.
And
I will just replace this body with
code that I've prepared earlier. So
there is no magic in here, there's just
some streaming happening where I receive
the stream from the request.
Then I interpret or actually load that
stream in an image, do couple of image
manipulation operations, and then save
the stream back into the output stream.
It complains a little bit because of
course it doesn't see all the
references. So I will have to fix that.
I have to reference system.io.
So I reference that first. Then this
image manipulator is also not
recognized, so I'll just use TechTaste
2017. And this image format is
complaining, so we'll just reference
using image Sorry,
system.drawing.imaging.
And that's it. So, my function is ready.
And I can now go and deploy that
function. So, I can try building just to
see if everything works fine.
If my Azure simulator worked, I could
test it immediately from my machine, but
since it's not not working, I will not
lose any time on that. So, it builds it
builds nicely. I have no errors. I will
just right-click this image manipulator
and click publish.
Then I will select existing application.
I will click publish. I will again
create a publishing profile.
So, let's just wait for a second until
it refreshes.
I will put it in my Nav TechTaste
2017.
And then I will select this application.
I will click okay.
It is preparing the profile.
And when the profile is prepared, I will
be able to click publish. When I click
publish, my function will appear inside
of my function application in Azure. And
just by creating some AL code, I will be
able to replace it. So, let's actually
do that AL code while the publishing
profile is being prepared for me.
So, here I have another page extension,
which is item card extension.
Everything is ready, so I will just
remove those comments.
So, what do I have here? I have an
action which invokes this code unit
image management. It invokes this
uh upload image function. So, image
management is my
AL code unit. In fact, this is nothing
but AL translation of this CAL code
unit. So, it has those two elements. The
first one is which handles this input
dialog, and the second part is instead
of this blob Sorry, um stream handling,
which is now part of my Azure function.
It actually just handles invocation of
Azure. And this is the Azure invocation
part. I simply convert my
uh, stream containing, um, the image
into, uh, a request. I actually stream
it as application octet stream, which
is, uh, just the way to serialize your
byte array when sending it to web
service. Then I invoke my web service. I
will simply
replace this URL with what whatever you
correct URL I will get from, uh, Azure.
And it sends the request. My Azure
response does image manipulation and,
um, gives it back to me.
So, let's take a look if this is ready.
Yeah, I can click publish.
And in a short while
there will be a new uh, function
available in my application that I will
be able to invoke. Okay.
I can go to my application.
I can refresh the application.
And I can see that I have this scale and
crop.
I just take the URL.
Copy the URL.
And paste it in here.
I don't need to add any parameters
because this is being sent through the
body rather than, uh, sorry, through the
headers, uh,
and content rather than through, uh,
through the, uh, query string. So, I
will save this. I will run this.
And it will add a new action to my image
card.
So, uh, I'm going into items.
I will select this
touring bicycle.
Let me first remove this picture.
And then, uh,
here I have this invoke Azure action,
which has just appeared. So, I will
invoke it from here. I will select
choose, select the same image, click
open, and now it's Azure handling it.
And there we go. It's the same image. I
can actually verify that if I copy the
image address
that it is really an image of 300 by 300
pixels in size. Just to show you that
this is not smoke and mirrors, I'll go
into pictures and open this one. This is
fairly big, you know, it's certainly not
300 by 300. It's actually 2,600 by
1,607.
So, this is uh
now my Azure function responding. It
took me all 6 minutes to get it from CAL
into an Azure invocation and having it
actually do something um fairly complex.
So,
um
what else can we do?
So far we have seen how easy it is to
create functions. We have seen how easy
it is to deploy functions. We have seen
how easy it is to debug them. We have
seen how easy it is to invoke them from
from AL language,
uh how easy it is to actually turn
previous CAL into new AL and having your
Azure function up there in Azure. So,
what else can we do? Is there anything
else we can automate? Oh, yes. So, one
thing that we can automate, which is
absolutely worth your uh attention, and
this is that demo that failed for me. I
just couldn't make it work today.
Uh but I will try something because I
have some theories why it couldn't work.
So, I will just test one theory here in
front of you. You will humor me those 2
minutes that I attempt to do that. So,
uh
how What is this development about?
We have a possibility, once you have
your function developed in C# inside
Visual Studio, that you simply take this
solution from Visual Studio, put it into
a repository, something like Git for
example, or something like TFS or
whatever,
and
forget about Azure functions completely
because
everything is going to be completely
managed for you
by the Azure stack. So, let's take a
look at uh different providers which
allow us to store
the source code of our Azure function.
So, we can use Bitbucket, Dropbox, Git
installed locally on your machine. You
can use GitHub, you can use Visual
Studio Team Services, or you can use
OneDrive. So, all of these are options
which allow you to store your source
code and then connect your Azure
application to that repository and then
keep your application up to date. It
will automatically detect when there are
any changes and it will automatically
refresh your application. So, without me
talking too much about that, let's take
a look at
how we can actually automate our
deployment
using Git. If you're not using Git yet,
I hope you will start using it today
because Git absolutely rocks.
So, um
what I will do here is I will start with
a new
solution. So, I will just start file new
project.
And here I will create a new Azure
Function project and I will call it Git
Deploy.
And I will just click okay.
Inside of this Git Deploy, I will simply
add a new function
which is called
test me.
And it will be HTTP trigger and it will
be anonymous and I will click okay.
So,
that's all I need.
I will not publish it to my Azure. I
will instead connect it to my Git. So, I
will right click
and I will click
Sorry. Solution right click
add solution to source control.
Okay.
Here I will click publish to GitHub.
I will use micro, sorry, publish.
Ah, what did I do?
No.
I apologize.
Let me just This will be quicker, trust
me. So, we'll just create it again. So,
function app called
get deploy to
and a function in that app which is
called
test me
and this is HTTP anonymous, okay.
And then I'm going to add this to to
source control.
And then publish to GitHub.
So, I will just click publish on this.
Okay, so I will not mess up again.
So, now we'll go to get
it will be there will be a new
repository for me on my GitHub. I simply
need to commit all the changes. So, I
will just call initial.
Just a second. Let me take a look at
Everything is actually already there. It
is
Let me just go to home and let me click
to
sync.
Sync.
Let's take a look at GitHub. So, inside
of my GitHub
If I go to my repositories,
I will see this Git Deploy 2.
It has my solution. It has my code.
And then I will go to Azure
and I will click on this application.
And then I will go to overview
and then application settings. Uh sorry,
I apologize. I will go to
platform features and then deployment
options.
From here,
I will click set up
and then I will click choose source.
I will choose GitHub. If you have not
configured GitHub with your Azure
subscription at this stage, GitHub would
like you to authenticate. Since I did
that already, it doesn't ask me to do
that. So, I can simply choose which
project to use. This is this Git Deploy
2.
That other one doesn't work for whatever
reason.
And everything else is fine, so I'll
just click okay.
So,
uh if I'm lucky
and I don't know why it didn't work
earlier, what will happen now is my
Azure function application will connect
to Git. It will fetch the changes from
there.
And then it will build my application
uh inside of my Azure application on the
server. And when that happens, I will
actually have uh my
Sorry.
Let me take a look at what's going on in
here.
Yeah. So, it's adding project files now.
It's actually It says that it's
building. So, it will take a little
while. So, maybe um
2 minutes
uh until it builds. What is the idea of
this uh continuous deployment?
The idea is that you can actually start
working in your development environment
the way that you would normally work
with some kind of source control in the
background.
And of course, you would uh not be
working in your master branch
uh as I'm working in it right now. You
will probably select one specific branch
that you want to to build from. If you
remember when I was configuring this
application to connect to GitHub, it
asked me which branch I want to use.
I've just selected master because I have
master. But you can easily say I have
Azure deploy branch. And then when you
have this Azure deploy branch, it would
always pull stuff that is present in
that branch when that branch is
committed or actually synced with with
GitHub. So, once you have all that
configured,
GitHub will notify
Azure that there is a change in this
repository. And then when there is a
change, Azure will simply fetch all the
changes. It will locally rebuild your
application. And when your application
rebuilds, if there are no errors in that
application, it simply exposes all of
the Azure functions which are present in
that application
inside of your Azure function app. And
you can see it online and you can then
access that from
Visual Studio Code or from any of you or
from anywhere else. So, this is the
idea. Then as you're developing, you
don't need to publish, you don't need to
do anything. You are simply working as
you would normally work. And then once
you're happy, you simply merge your
changes into the target branch. You push
your changes to GitHub and GitHub and
Azure do everything else for you. So,
it is still building as I can see. But
in a short while it will be completed.
And when it's completed, I'm pretty sure
I will be able to see it uh
in here. So, to to not just stand in
front of you and chit-chat
meaninglessly, let me actually just
continue with everything else. And then
I will immediately come back to that at
the next demo point.
Let's first talk a little bit about
performance of Azure functions and then
we'll go back to this Git.
How well do those functions actually
perform? So, that's a question you may
reasonably ask. Well,
what you think is happening is probably
what is happening. They are not the
fastest thing in the world.
And why are they not the fastest thing
in the world? Because
they are some Azure service sitting
out there
possibly far away from where your server
is, where NST is, from where you're
invoking them. And then there will be
some network latency. And then, of
course, every time you invoke an Azure
function, it needs to provision your
container, it needs to start it up.
Sometimes it is fast, sometimes it may
take a while. But it's not that bad, you
know. I've now explained a lot of things
that happen, but it certainly takes
Azure far less time to do all that than
it takes me to explain what happens. So,
we'll quickly see exactly how fast or
how slow that is. So, let me just
demonstrate the performance of Azure
functions. So, let's see if it's
actually slow or fast.
It's still building this, so let it
build and I will come back to this demo
a little bit later.
Let's take a look at
my functions. I will just open another
instance of
Azure portal.
Um I will click my function apps.
And then I will click
this function app that I have prepared
earlier.
And when that function app refreshes, it
will show me all the functions inside of
there and then I will be able to see
couple of them to see how fast they
perform. So, here I have some
performance test C sharp.
What does it do? It simply adds 5
million entries into a list.
Good.
I will run that.
And then I will let it uh let it
execute. So, for five 5 million
requests, um okay, it's now processed
the request. It says that it needed
seven 7 seconds, 7,400 milliseconds. I
will run it again because it had had to
spin up the first time. So, let's see
what happens when I invoke it second
time.
It will tell me that it took 6.2
seconds. So, that's not that bad for 5
million operations. Okay, but this
doesn't really tell us anything. Let's
see what it means to invoke an Azure
function, which sits somewhere out
there. And let's see how well it
performs then. It's easy for me here to
see that it took 6.2 seconds to run a
function from the environment where it
is actually hosted. Let's see what
happens when I invoke it from my NAV
machine, which is who knows where, as
compared to my Azure
uh service uh where it's physically
stored. So, I have prepared some demos
in here in AL. So, I have this Azure
functions
code unit, where I have this invoke
demo, which I've used earlier, and I
have this measure performance. So, what
does this measure performance do?
It simply invokes a number of functions,
which are exactly the same copy of
exactly the same thing, just hosted in
six different locations. Let's take a
look at what those locations are. So, I
have these functions called sorry, a
function apps called
uh Tech Days uh test Tech Days AU, this
is Australia. I will expand that one.
Then I have it in Ireland and in
Netherlands. And then I have it in
Netherlands, but in the same resource
group and on the same storage account as
my virtual machine is. So, let's see if
that has any effect on the actual
performance.
Then I have one in Singapore and one in
Central US.
And what does the function do? The
function is actually my very simple
Hello World. So, it's that function that
is created
uh by Azure itself as a demo. So, So
function is actually fairly lightweight.
so it doesn't Whatever time we measure
will be actually the latency between my
server my my NAV server and Azure
function endpoint. And it will be the
time it needs to actually spin up this
container in which Azure function runs.
So,
let's take a look what happens if I
rebuild this
and invoke measure performance.
I will do two runs.
Uh both of these
two runs will be uh
actually not. Let me just show what
exactly I do inside of this.
I actually invoke it 10 times. Each of
them is invoked 10 times, not just once.
Because one invocation would not give
you exact number. It's just uh there are
a a lot of influencing factors. So 10
times
will give you number that you can divide
by 10 and then get some nice
approximation of what is going on. So I
will invoke this same function 10 times
and it it's going just to be invoked on
six different places in the world. So I
will run this. It will take roughly half
a minute to execute, after which I will
see the results. I will see how much
time it took for me to execute all that
and
what?
Uh
let me
close
these
that I don't need anymore.
And let's just make sure that
everything is fine.
Okay. Um
if you would allow me just to go a
little step back and take a look at this
one. GitHub says that it has deployed my
function to Azure. So I will just go to
Azure apps
and click okay here. And then I will
take a look at my NAV
Tech Days 2017.
And I will take a look at functions in
there.
It's refreshing and I can see that I
have this test me function.
So, this test me function is now uh
going to execute this code that we have
seen in here. So, it will say hello,
whatever.
Okay, I will do another change and then
let GitHub do some more stuff while I'm
demonstrating performance. So, this is
going to be adding actually changing
this hello. I will just put uh hi there
and then
how are you?
Just so that we can see that there is
some difference. So, I will not publish
that.
I will simply go to my changes.
I will commit this as update
into my master branch
and then I will sync.
And then I will sync.
So, it's now going to
uh be pushed to to GitHub.
When it's pushed to GitHub, I can check
my
Azure function. I can check my
Just a second until it refreshes. I can
click this deployment options and then
from here I will see that it detects
that GitHub is updated.
So, it's updated. It's now refreshing
and in a short while it will actually
uh put everything back. At the same time
while GitHub is busy with deploying this
function, I'm going to check what's
wrong with uh with this piece of code.
So, let me actually verify that all of
these URLs are actually working because
I have I suspect that I managed to break
one of those earlier today.
So,
let me try to see. This one should work
fine.
And this one is what I suspect could be
broken because I was playing with that
and I shouldn't have. So,
Oh, yeah. This one will not work because
the um
Let Let
just select this NAV Tech Days 20 Sorry,
uh this one.
I think this URL is not correct.
So, I will just inside of this
test Tech Days
uh application open this
function and recopy the URL and repaste
it into NAV because I think it's not the
same. It's the app key that has changed.
So, I will just
Well, it seems to work. I don't know
why. So, I'll just replace this just in
case. So.
Let's take a look. I will rebuild this
again and then I will actually set a
breakpoint in here to see if there is
something wrong.
So.
I'll press F9
and then I will just run it in a
debugger to see if something is uh not
being invoked as it should.
So, I click invoke Azure.
It seems that it's not invoking my
So, I will stop it
because something else is happening. Let
me just
check my
order processor extension. Ah, yeah,
this is the problem. I'm not even
invoking my code unit. So, code unit is
called Azure
functions.
So, I will redeploy
and this should now work.
So, when I click Azure functions, okay,
I did not run it with a debugger,
but my functions are now happily
executing and I will let it run. I will
just stay for a little just to see that
that error doesn't pop up.
It seems to not pop up. Let me take a
look at what's going on with my Azure
deployment from Git.
So, I will select this application
again.
Is Git still busy?
So, it says that it has completed this
update.
So,
I will not do anything right now because
I have a demo running. So, I will just
let this execute.
Before it completes, I will just let you
know this.
There was going to be increasing latency
between those endpoints. So, Amsterdam,
which is right next door, is going to be
very fast. It will be just couple of
seconds of total invocation time, which
would roughly put execution time for per
function invocation at 300 milliseconds.
So, one function to execute actually
will take roughly 300 milliseconds. And
it is mostly because Oops, what is this?
This is now uh
internet issues.
Well,
I hope internet comes back.
And yeah, it's back.
And results are back. So, if you cannot
see that, uh it actually says that
Netherlands is 3 seconds
and 832 milliseconds. Netherlands same
storage is 3 seconds and 323
milliseconds. So, I didn't gain much by
putting everything in the same storage
account. So, currently my virtual
machine and my Azure function
application with everything are stored
in the same storage account. It has only
gained me roughly half a second or sorry
uh
yeah, roughly half a second per uh 10
invocations. Then Ireland is 9 seconds,
nearly 10 seconds, Central US 14
seconds, Singapore 21, Australia 15.
So, this is latency. And this is to tell
you that when you're using Azure
functions, you actually have to put them
as close as possible.
Latency is going to be your biggest
enemy.
Uh performance is good. It's just that
latency is bad and uh you have to
somehow handle that. So, it's certainly
not a a good thing that you have to wait
for roughly 2 seconds when you're
invoking it in uh
in Singapore, for example. So, uh what
did I do? I managed to
break everything with this magnifier, so
we'll just get it out. And
I will move on. So, uh
actually, I would like to show other
demos and then in the end we can go go
back to this uh GitHub deploy, but trust
me, it will show that message. So, let's
take a look at this thing. Which
language should you actually use?
Uh when it comes to languages,
developers really love crusading. Like,
my language is better. C# is better than
JavaScript. F# is better than C#. Python
is better than all of you and stuff. So,
which language is actually the best
language to write Azure functions in?
The choice should be yours. There is no
rule. All features are supported in all
of these languages and Microsoft is
adding more and more language support to
Azure functions. You can combine them.
You can have applications which combine
multiple languages. But do they really
perform the same? So, um I'm kind of a
JavaScript guy. I absolutely love
JavaScript. And people tell me
JavaScript is not a real language. It is
interpreted. It is slow. You should not
be using it, you should use TypeScript,
whatever. That's just
nonsense. TypeScript is JavaScript. And
it's not going to run faster than
JavaScript. And what people say like C#
is going to be much better than
JavaScript, I will just prove you wrong,
or actually prove anybody wrong who says
that C# is a better choice for Azure
Functions or for anything for
for that matter.
Um actually, let me compare the
performance of the same stuff happening
under different languages. So, I will
just go into my Azure platform and I
will take a look at my function apps.
And then I will expand this app which
has the same function
running under three different languages.
I will compare C# to JavaScript to
Python.
So, here I have
Sorry. Um
C#.
Should I have F#, but I don't care. Um
C# is
doing this. So, it's inserting 5 million
entries in a list and we have seen it
already. So, I will click it and then it
will show me that it performs those 5
million operations in
What was it? 6 seconds or something like
that?
So,
well, 11 seconds. But that's because it
had to spin up the the container. So,
we'll run it again.
And it will be less. So,
Okay, 7 seconds. I will click
JavaScript.
Let's take a look at how well does
Node.js compare to common language
runtimes. So, I'll click run.
It does exactly the same thing. So, it
creates an array and then pushes 5
million times
uh
the string we actually the number
converted to string. So, it's exactly
the same operations, just written
differently. So, here I have it in First
time it is 10 seconds and then second
time
and third time it will be less. So,
first time it had to spin up everything.
So, it's done in 2.8 seconds.
Twice as fast as C sharp second time.
Again,
and it's going to be again roughly
twice as fast. Okay, while it's
executing, I can actually click Python.
So,
okay, well,
if you click it enough often enough, it
will be it will be consistently faster.
So, C sharp cannot hope to get to those
uh whatever uh and 1/2 seconds. And
Python, let's take a look at Python. It
will be actually slower than C sharp. I
don't know why. I actually don't know
much about Python at all. I I know that
people love it, but it doesn't really if
you're comparing performance, it's not
such a performance beast, obviously
obviously. So,
um the point of this exercise here is
not to tell you like you should all
write JavaScript for Node.js. JavaScript
is compiled and it runs pretty fast.
It's very solid language. It's to say
that
you should choose language that you're
comfortable with. You will not have any
problems using any of the languages
available. All of them have the same
features. It Probably the language
choice will be about dependencies that
you can use. Okay, so Python did this in
20 No.
2.6 seconds. Was it Is it possible?
Whatever.
It is. Yeah.
So, it's uh
Okay, it will it will show some number.
We can come back to to that later.
How do we secure Azure functions?
Uh there are a number of ways to secure
them. So far, I've been invoking all of
them nearly anonymously. So, all of the
functions I created were anonymous
functions, so uh anybody who has the URL
could access them. So, how do you secure
them? There are two ways. First, you can
secure them using access tokens.
And those access tokens are uh in fact
just that cryptic string that you put
either in the query string
or in a header in authentication header.
And then whoever passes the correct
string,
that string will be evaluated and
accepted or rejected by the application.
Um we call this um security by
obscurity, you know, because it's
how difficult it is for anybody to
obtain that um that access key.
So, when you talk to security experts
and you ask them um does security by
obscurity really work?
These are roughly the answers that you
can expect.
Uh what is probably the better way to
implement authentication is to use all
authentication protocol. However, there
is a big problem with OAuth.
Uh OAuth is user-level protocol. So, if
you want to implement OAuth, you
actually need users to authenticate, not
the application to authenticate. And
then when we come back to this nonsense
of security by obscurity, it is actually
fairly good as long as you are
having service-to-service communication.
Your service is not exposed. It is using
HTTPS. So, it's going to be as secure as
HTTPS. And if only your service knows
this secret
and you don't share it, it will not be
such a big problem. So, the point is you
should actually not spend too much time
configuring uh some more complicated
security than simply adding those
authentication tokens. So, I will simply
show you how to secure access using
authentication tokens. I will not be
showing how to do full OAuth because I
honestly don't know how well it would
perform in a service-to-service
communication scenario. Here we have CAL
invoking Azure function somewhere out
there. Why would you want to
authenticate a user for that kind of
authentication? This is just a service
thing happening, not a user function
happening. So, here I'm in my Azure
function. If I click this URL, I can see
that it doesn't have any authentication
because it is anonymously authenticated.
If I click on manage
I will be able to specify
a new
Sorry, is it here or
Just a second.
Here. Sorry, integrate not in
authentication. I will choose
authentication level and I will specify
is it admin or function or anonymous. It
has been anonymous. If I click function,
it will allow me to save and then it
will allow me to add keys. So,
I can just take a look at
Why is it so slow? I'm running of time.
Yeah, something is bad with this today
and I don't have a clue. Anyway, let me
Let me just skip over that. You would
have to create a key. That key would
appear in your query string and you'll
be able to pass it. That's it. I'm
sorry, time is running up and Azure is
really slow and I cannot make it faster.
That's all. So, that's all I had to
present. Now it's time for questions. We
have 3 minutes and 28 seconds and uh
you know the drill. It's shirts for
questions, but questions have to be
smart.
So, um
question over there.
You're next.
Yeah. Hi.
Um so, in general you have shown that
Visual Studio is the preferred uh
environment to develop.
But But I didn't catch that.
But Visual Studio is uh the environment,
but
which edition you use?
2017. Uh this was community.
So, I used community edition here. So,
don't need to have anything higher than
community.
And is it working with a lower version
also with Express for example because
sometimes you're not allowed to use
community for
I don't honestly know. I know that it
works with 2015
uh just you need to install Azure tools,
which you need to download separately.
And for Visual Studio 2017, you don't
need to download them separately.
They're embedded in the install process.
I don't know about Express.
Because community has some limitations
in the Express.
2015 at least. Yeah.
Okay.
Okay?
Uh
Second, yeah.
Um
As you said, you we use internet uh .NET
interoperability in order to
access web services and such things and
so on, but sometimes we use it also to
connect to some
other applications or other other
databases that are not in the cloud.
They're They're locally. How we can do
this in
Well, uh you would have to use probably
service bus or something different to
access your local resources. This is
possible, but just be more complicated.
But we have to publish this to to have
Well, uh if you have that situation that
Azure cannot possibly talk to your local
resource, then you would have to host
everything locally. So, you would just
have to develop a service application
locally which exposes HTTP endpoints
that you invoke from AL.
It's It would be just like developing
any service application. It can be WCF,
for example.
And that's it. Yeah.
There was a question over there.
Uh regarding uh
service-to-server communication, is it
also possible to
uh do white listing on Azure functions,
so to say only those IP uh
uh originating calls are allowed
from a certain IP address?
Um well, that's something that goes to
uh infrastructure of Azure. I'm not an
expert in infrastructure on Azure, so I
cannot tell you exactly that this is
impossible or not possible. I assume it
is possible because you can normally
configure Azure fire firewalls.
And uh I'm pretty sure you can configure
it for for this thing, too.
It's just that
I cannot tell you today this is how to
do that.
So, I'm pretty sure you can. I just
don't know how exactly. So.
Would you consider it to be another way
to improve security?
Uh sorry, I didn't catch that.
Uh can be used to improve security by
Uh how can be used what to improve
security?
To prevent illegal access to your
services.
To your functions.
Mhm, I'm not sure I understand the
question. I apologize.
Okay.
It's okay.
Can you try to rephrase?
If you whitelist uh who is allowed to
use the Azure functions.
Yes.
You can use that as a means of
preventing illegal access or
unauthorized access or unwanted access.
Well, um
I I don't know answer to that. I'm
sorry. Yeah.
Yeah, t-shirts. I forgot t-shirts. Yeah.
Uh there were three questions.
Uh you asked the question.
You asked the question.
I asked the questions.
Yeah.
Um
There is a question over there. Yeah.
Please try to
I I cannot catch half of what you guys
are saying. So, I just have to assume
what the question is about. So, try to
Uh do you think that Microsoft could be
publishing some of the Azure functions
for for NAV community to use?
Um I can I don't know, but I assume yes.
So.
Do you think how how likely is it?
Maybe we should ask them. So, uh
Okay.
I I I don't know. So, I would love to
see that, but I cannot tell you how
likely that is.
Yeah, what I would like to see, for
example, is NAV exposing some hooks for
Azure functions to hook into. That would
be amazing, but I don't know.
That's a They say that's a possibility,
but yeah. Let's Let's keep fingers
crossed. That would be lovely. Yeah.
Yeah, okay. So, you have you have shown
it always with your Azure account
with your small Azure machine, but in
real life
it's uh
coding for for a customer of you or for
a hand of customers. And if you're
deploying your Azure functions,
you should Usually, I guess, deploy them
to the customer's Azure account, right?
Uh not necessarily. So, this is an API,
which is public API. It can be your API.
It can be part of your service offering.
Okay.
talking Dynamics 365, it can be part of
your service stack. You do not need to
have a customer's account to host them.
Okay.
So, everybody who is your customer will
be able to invoke your stack.
That's the point.
So, I should just make a contract with
my customer and they pay for use my API.
You don't need to do that because
they are using your service. So, you're
paying for Azure, it's your Azure, and
your customer is your your customer's
database is calling that instance.
I don't know why you would have to have
any kind of contract. Why customers
would even have to know about that?
I don't think that it's even necessary.
So, it's just a part of their
application.
Yeah.
in Germany and Azure in Germany, they
are
cloud.
Tell them that their bank account is in
the cloud and their money is in the
cloud. So.
Any other questions? Okay, let me try to
not kill you when I throw this over
there.
Oops.
Is everybody alive over there?
Yeah, yeah, yeah.
Okay.
Uh
just a short question. Can we use Can we
call this
Azure functions from CL?
Uh yes, you can. So, you would just have
to use .NET interop, the guy you are
trying to replace.
Mhm.
So, uh you will just have to use exactly
the same classes. So, you have this HTTP
client class, which I use every single
time. This HTTP client is
system.net.http.httpclient.
All of those types, HTTP client, HTTP
request message, HTTP response message,
blah blah. They all come from this
system.net.http.
So, you simply take your AL code,
convert it to CIL by changing the
references of actually the declarations
of those variables. What was HTTP client
becomes .NET of subtype
system.net.http.httpclient,
and there you go. So.
Okay, thanks.
Easy.
Sorry? Oh, yeah, you can use the
the code unit, which is built by
Microsoft for that purpose, for invoking
web services, yeah.
I have a really important question. Can
I get such a cool T-shirt?
I'm out of shirts, honestly, so
there's none left.
Then then I will take this with me.
Thank you.
I don't care.
I care.
It's not mine.
Any other question?
Okay, over there, first row. So.
Oh, let me try to kill somebody from
Microsoft.
Hello.
The example the other guy there
mentioned before where you deploy your
API for the your function for the
customer,
Mhm.
and the customer maybe move away to
another partner.
Do you have any views or access to to
check if the customer still uses your
function?
Well, you have. So, you can always go to
the function, and if my Azure is alive,
and I hope it is at this point, yeah,
you can click this monitor.
And here in this monitor, you will be
able to see
it's You will be able to see that
switch?
Ah, yeah. Anyway,
you click the function and then click
monitor. There is monitor node
underneath the function name. When you
click that, it shows you all of the
invocations and you can see if they are
being invoked.
So,
that. Yeah.
So, you can see all of the invocations.
You can see what was sent and
And from where?
Well, I'm pretty sure you can do that
not from here. You have also one thing
called Kudu. So, you would click the
application itself and then I don't know
how much time we can actually stay here.
I will click on application, sorry,
platform features and then I will click
on
where is it? Here. Advanced tools Kudu.
This is Kudu tool that Microsoft has
made a part of the uh
Azure function stack and from here you
would go to tools and then web job
dashboard.
And then from web job dashboard you will
see nothing, but then you would click
functions when it wakes up. Azure is
mighty slow on here. I don't know why.
It's uh it should be a decent VM and
everything and I don't know why it takes
so much time. So, click functions and
then in here you would see all of
invocations and here you can see a lot
of information about
that invocation. So, um
yeah, I cannot see from here
here where from
the call comes, but I'm pretty sure that
that is logged somewhere and this has
API to invoke, so you could probably use
that API to reach that.
Yeah.
customers to use your functions?
Yeah, there is I mean there is a way
because you control the keys. You You
controls control those access keys. And
when you have access keys, you can
assign them per customer. Every function
can have a number of access keys active
at the same time and then you can switch
them on and off.
Okay.
So, you can easily say like, okay, this
access key is not valid anymore, so
nobody can use it.
Okay.
So, that's uh
one way. Yeah.
I think we need to wrap up.
Okay. Thank you very much for attending
and see you
