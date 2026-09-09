# BC TechDays 2023 - Azure Functions Deep Dive for Dynamics 365 Business Central developers: present..

- **Source:** https://www.youtube.com/watch?v=4WwgwsAJlS4
- **Video ID:** 4WwgwsAJlS4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 97m13s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you everyone for attending this
session we are
presenting okay perfect
this session is about Azure functions so
uh the goal of this session is
presenting you how is why Azure
functions are important what are the use
function where Azure functions are going
in the future and uh
a lot of
especially a lot of best practices in uh
in order to use efficiently Azure
functions in in real world projects
uh this light just just to say that if
you have follow-up questions after the
question and answer the session that I
know able to respond directly you can
feel free to write me on my socials and
I will respond for sure
I know an agenda for today but I have
some session goals that I want to uh I
hope to be able to transmit to you
especially my goals are to uh
understand
transmit the idea why Azure functions
are important in the business Central
projects uh
where this Azure function platform is
going so the future of azure structure
platform and what changes
uh understand what you can do more than
publishing as simple Asylum code in the
cloud because Azure function is not like
that only like that and and
understanding best practices and some
tricks in order to efficiently use Azure
function in the cloud because as I said
always if something is working it
probably is not always the uh
maybe working efficiently so especially
in the cloud you need to take care of
that
uh
a a an alert for this session because uh
uh this session is focused on their own
functions so we will not see a lot of Il
code some IL code but very few other
code we will see mainly uh
uh other type of codes like for example
C sharp because actual function cannot
be written directly in il code and we
see a lot of actual stuff so don't
expect to see a lot of real code here
uh
why Azure functions why we use Azure
functions in Business Center why we are
talking about in a place here where we
are
business Central developers because
actually functions especially in
businesses online uh
rnes in uh today and normally when I
talk about Azure functions I think that
the main point where we use Azure
functions in Business Center projects
are uh
uh what I listened in these slides so
the first need the partner rev is
executing.net code in a SAS environment
you cannot use internet variables so
it's one of the need that where you need
to do something else and Azure function
is that the most effective way to do
that in the cloud
reusing existing libraries is another
problem that Partners have
uh probably you comes from NIV a long
history you have a custom libraries that
you use in nav and you would like to use
that Library maybe also third-party
libraries in your business center
projects SAS project and function is the
way to do that
Azure facial extreme importance for
interactive with other Azure Services
Business Center should not be a closed
box in a cloud World should be
integrated with and often is integrated
with Azure services and uh one of the
effective ways to integrate Business
Center with Azure services so generally
speaking not only Azure services but
also integration with third-party
applications Azure function is one of
the ways to do that
Azure function is also important for
creating serverless workflows uh when I
talk about WordPress normally we talk
about
power automate uh Power ultimate is I
always said that it's great but it's not
important to create workflows for
Integrations workflow Source scalability
there are other Technologies like logic
apps or Azure functions for doing that
in
and timer-based triggers and then
sometimes Azure functions are also
important to create as a layer between
business Central apis and other
applications often I don't want that an
external application directly talk with
business Central by calling the rest of
the apis for many reasons and Azure
functions is a great way to do a middle
layer between apis and Business Center
and the coupled applications
so when we when we talk about Azure
function a common definition that every
knows is something like a serverless
compute service that permits Mew to run
to the event trigger record in the cloud
without
provisioning uh or managing
infrastructure so I simply deploy the
code in the cloud all is managed by
some other parties and I don't believe
on what's then under the wood and what
normally uh partner knows about the
functions that is something like I from
Business Center I can send uh
a request to a black box
and I send an HTTP request to a black
box and the Black Box responds me with
the response I want executing some code
deploying in that black box
but
this is one of the models of the Azure
function as a structure has not only the
possibility to
be called and we are calling via HTTP
and receiving a response but Azure
function is more than that uh
function is normally a a fully
serverless way to run your own business
Central code in the cloud
you create your code you deploy that
code in the cloud and
the infrastructure scalability and so on
it's all managed by you by the Azure
platform but Azure functions are not
only
a code deployed in the cloud that you
can call and you see the response Azure
functions are as as triggers triggers
means who starts a function uh triggers
can be
HTTP goals but also can be events that
occurs on other resources on Azure you
cannot third party triggers that calls
Azure functions and you can also have
time relevance
initial function that starts every five
minutes and executes some codes
I should factorize a full integration
with your the Azure staffs one of that
important and we'll see later is the
Azure monitor stuff so you can integrate
Azure function with Azure application in
size in order to receive Telemetry and
monitor the performances and you can
also automate the ICD inside Azure
functions in order to have an efficient
problem process
very quickly what
compose an Azure function when you
create initial function you normally
start from an Azure functional app the
Azure function app is what is deployed
on azure and in Azure function app is a
collection of one or more Azure
functions uh
inside the function app you can create
different functions and a function app
exposes these different functions to
your
endpoints uh
another important part of the Azure
function is during time the runtime is
responsible for running your code
and this the part of the the Azure core
services that includes the logic on how
to trigger the code and how to execute
our code efficiently Azure functions as
also another important part that is the
scale controller the scale control is
responsible for manager for you the
scalability of the function so
if you call it one the financial once in
a year or one millions of times in a
minute
the scale controller is responsible of
scaling the functions and granting you
the the performance you want according
to the plan that you have selected uh
Azure functional have settings where you
can specify some configuration
parameters or your functions and as you
essential as triggers triggers are
extremely important because R who starts
your function triggers a cell before are
not only HTTP calls but can be events on
every resources like a message in the
queue like a file saving suitable
storage or a timer executed every means
for example
uh
then that's the function code the
function code is obviously decode that
it must be executed and the function
code I said before is not a yell
language is one of the supported
language of uh Azure functions today we
I will show some C sharp code but uh
remember that Azure fashion can be
created
with other types of languages also with
Powershell for example you can create
such a functions
Azure functions should be and we I
repeat that later should be lightweight
and short-lived you cannot if you think
on or if you create an Azure function
that does tons of code tons of process
inside the same measure function that's
something wrong
Azure functions as bindings bindings I
will talk in depth about bindings
because are one of the most important
part of your functions if you want to
orchestrate
processes not only a code that gives me
a response but something more complex
and bindings are important for that and
but you know spend now time because I
will talk later about bindings
uh when you create a natural functions
you need the first thing that you need
to create is selecting a plan
and Azure function normally have three
types of planes the consumption the
premium and the up service plan
uh every plan has a different type of
characteristics the consumption plan is
what normally I suggest to start because
you pay for the number of execution of
your functions and not not exactly the
number of execution but is the number of
execution
plus the memory you use and the CPU you
use so that's why later in the session
we see some tricks in order to optimize
that
uh
Premium plan sometimes is okay sometimes
it's not okay sorry consumption plan
sometimes could be okay sometimes could
be not okay and maybe you in some
projects you need to scale to for
example the Premium plan the Premium
plan gives you more power and and also
more features like in one of the main
features is the integration with the
virtual Network or uh that sometimes is
required or important and there's also
another important feature of the Premium
plan that I will explain later
uh the tour plan is the dedicated or up
or what is called the app service plan
and the uh service plan means that
simply speaking simply speaking is
something like you are acquire a set of
resources
CPU RAM and so on and inside that you
execute all the functions you want you
are responsible to scale and you pay not
for execution but you pay for the
resources you acquire so you can execute
every function you want in
without carry obviously uh if you
acquire not enough resources you need to
stay by or by by yourself
uh clicker okay
uh now
one of the big changes in Azure function
is the execution modes Azure functions
as historically uh
only one execution mode that what is
called the in-process mode in process
mode mean that that you deploy a code
this and you create a cloud this code is
deployed on azure and
display this code is deployed in
inside the Azure runtime the Azure
fashion runtime and the code you deploy
must support the same Azure function
runtime so for example if Azure
Financial runs on dot net core free
your code should support The Deco free
if you want to use a dll or library or
something like that that's no support
not Network free
uh you cannot you cannot do that and uh
it's executed in process so means
directly also in the uh the Azure
function runtime now measure function
supports also another
uh execution Mode called the isolated
process or how to process normally
isolated in the common mode that the
couple
your functions code from the function
runtime and this is a great Improvement
because permits you to
create a function app for example in I
don't know.net6
is the actual time arriving on Azure and
you can use on that
functions every Library what also if
this Library does not support on the 7.
because you the couple
your function code from the function
runtime
so the isolated model removes all the
limitations of the in-process model
you have full control over you create
and configure your code full control on
the host and ability to use features
that are not so directly supported by
the host that runs your functions
uh remember that the isolated model is
the future
so I should function now
supports
both
execution modes we are here in this
moment
so uh
Azure function supports the isolated
anti-process mode but the future is
going
for the isolated
so you should start
working on the isolated model and
take confidence with the Israeli model
that has some differences compared to
the old
very quickly showing
I will try to switch between slides and
very quickly showing how to create an
Azure function in both modes uh
existential can be created in different
tools I will use visual studio today
with a studio or with a studio code but
as said before you can use Powershell or
something like that uh
uh I honestly prefer Visual Studio but
because it is more powerful uh
uh but if you want to use Visual Studio
core because it's a standard either in
for a business center developers
remember that you need to install uh the
Azure function extensions
otherwise
you have no support for that and you
have also need to install the extension
that gives you the language support so
for example I use the c-sharp and so I
need to install the C sharp extension
when all that is set up simply
require that you can go in the common
palette and select the Azure function
create
and we just call gives you a set of
questions the first question is where
you want to place the file the most
stupid question that you can ask and
I place this file in
this folder for example previously
created
okay now it's asking me what language I
want support
and the runtime here is the model that
you will need to select uh
uh you can select
the isolated model or the uh not
isolated so the in-process model and now
I create a function in the hallway so
with the in-process model so I select
this
and then you can select the type of
function that you want to create and
here you have a set of triggers and or
function template
as you can see the most common is the
HTTP trigger
I call you with a request use response B
with a response but there are a lot of
other triggers
that
starts from evidence in azure
or for timer
a function that I want to execute every
X now I select the HTTP only because I
want not to create the function deploy
the function but I want to show you the
skeleton so I create this I leave it a
name
here you can select your namespace class
name
and then the authentications the
authentication you can change also later
we see later about talking about later
about authentication now I select
function
that means I need to call the function
with the key
uh opening quarter window it's okay
and you just do a code deploys
the skeleton of my function
and this is an in-process function so an
in process function as you can simply
see that I have only one file
called as my function name
uh this file defines the function with
the name I can change it as I want this
is the this is the function app
and this is
the name of the function that I want to
expose
the skeleton is an HTTP trigger so it's
saying is exposing the authorization
I can change it also later
uh
the standard schedule supports getting
post but if I don't want to support for
example get I can remove and
in this way
my function only supports post
uh
a parameter name from the query string
or from the body of the responsive I
support post
and gives me okay alone hello name or
something like that but I don't want to
spend time on that I want only to show
that explain that
the Azure function in process has only
one file
this code that you place here every
complex code you want or you can add
third-party libraries and so on runs in
the same process as
Azure so you cannot use if I select the
dotnet6
because the Azure function runtime has
not like six I cannot add now a library
that is not compatible with dotnet6
the other
possibility now uh
yeah I open another window is to do the
same thing so again create a function
uh always the same I say temporary
folder
okay
and is always sharp and now I select
the isolated model so for example the S7
is related
I always select the HTTP trigger just to
show the differences
and I open this
now the project is created
and
this is an isolated function and as you
can see the main difference here is that
uh
now the firm before the file was one
now I have two files
a program five program CS5 that if
someone of you is familiar with console
application seems like a console
application
and uh
uh the real function
type that contains me my HC trigger and
the code that I want to place inside my
HTTP trigger some parameters are changed
before we have I should be a response
now we have HTTP response data and
actually the request data so it sounds a
bit a change but logic is absolutely the
same but what's important important to
note at the moment is that
uh in this case we have a program file
that uh
gives you the access uh to the startup
or your function so uh
uh you are responsible here as you can
see
in this
piece of code you are responsible for
creating a starting your own instance
most instance so this means that
the function code is the couple from the
host instance here you can add your
libraries you can add your services that
you want and uh
the host is Austin on the financial
runtime and your code is executed in a
separate process this letter which is an
example this will give you you open you
a lot of power because you can host this
in every platform supports the Azure
fashion runtime so you can also support
executing Azure fashion locally on your
own network without going on azure
and
later I will show I'll show some example
of that so this is the main difference
how we create the function called
is exactly like before so here you can
add your custom Library you can create
your function code replace this and pass
put your function code as you want
okay
saying that
if life goes okay uh
we have deployed our first fashion later
we show more advanced encode uh when we
have a function on Azure uh now in uh I
think you know that in with the central
now we have an Azure function system
module that permits you to uh
avoid by using the HTTP client and
creating manually across to an Azure
function but this module gives you
Authentication
a method to call the Azure function
without bypassing parameters without a
few lines or code without doing that
yourself and these Azure module supports
function or or through Authentication
and the uh
something different if you want to
support Azure function keys or
oath Authentication
how to use that I quickly
show
with the sample because
probably you know
these
so
uh
ER I previously created a
an Azure function
that creates Square code
uh it's nothing if nothing difficult
essentially with trigger function
that receive an URL
and from this URL generates a QR code
you can create a barcode or something
like that
what I've done that is that I know I've
used this
this is a third-party package so
this is a library
this Library
that I installed from nuget
and so it's a dll your custom dll my
custom dll in this case is a third-party
LL I don't have the source code of that
but it's just for showing that I can
embed a dll
and I can deploy the function in the
cloud and these dlls are automatically
deployed in the cloud and they can use
everything you want I want from
uh business Central or uh or something
like that now when this function is
deployed in the cloud function can be
deployed in the cloud directly from
Visual Studio or much better
from
cicd and later I will show how to do
that
but when the function is deployed inside
the azure
I have
let me close something because otherwise
it's difficult with I close the
previously created samples
I'll save this okay
I can start using and from using
this function is just to show is a
simple function that when deployed on
Azure response to this URL
here
so it's a bunch of that called I call
quiz Square generator I use the function
key as authorization and I'm passing a
Json with the URL and if I test this
function
the code is executed and the function
gives me
in this case is a QR code
and uh I I want to use that from
Business Center so what I I want to do
here is I want to place in the customer
card for example
a button
or
calling my code
so you are simply create a function
called uni sorry where with the method
where I pass it the idiom page on the
customer card and decrease the code
if I go
to check this code
this code uses the uh Azure functions
modules of the system app so
uh I have Echo units for authentication
that
resource and interface for the
authorization
and must be used in this way
like the method to use is create code
out if you want to use code
authentication so functions key and
later I will show an example with ALT
key
in this case I need to post a Json to
the function so I create a body that is
a Json that I can use Json object here
is simple so I can directly create the
screen the the string of the Json and
I'm sending the poster request by
passing the the Authentication
or the function
and my body
if the call is okay when reading the
response and you have the Azure function
Response Code unit
as methods
to read the response from a measure
function as text as stream depends of
the Azure function what answers in my
case is a stream because it's giving me
the bytes of the PDF file and I reading
that and downloading
the function for stream so what happens
is simply is that if I open my business
Central here I have a customer card
where I have this button and if I call
this button
a barcode is generated and then is
downloaded to my
to my download folder in this case but
you can do everything what you want and
if it's automatically generated so my
code calls as a standard function that
does the processing and gives me the
output for me
can also be used not only with normally
people use Azure function with function
authentication but if you have more
security more Enterprise feature station
areas you can also use Azure Z directory
authentication and to do that
uh you need to remember that
yeah I have a function here
the most effective way to do that is
start deploying the function in
Anonymous authentication and then
activate the uh authentication from here
from authentication you can add an
authentication provider
and Azure Financial supports different
authentication providers not only Azure
directory but also you can sign in with
apple with Google with GitHub or
something like that
uh if you if you set Microsoft
uh it what what happens is that it
creates
an app registration as you I think you
know if you are yet used in the past
apis it creates enough registration and
in this app registration you have the
client ID
you have your payment ID you need to
create a secret as use one
and you ask this
ID URI app ID theory that is the
operator URL that you need to pass to
the Azure function if you want to use
Azure directory so
if I want to call that previous function
with Azure ID directory I need to
remember that I need to call the method
to call is not uh
the
function key but create all two method
by passing the endpoint
URL of my function
the authentication code
that is the authentication code that I
have in the app ID the client's ID that
I have in the app configuration and
uh Italian secret and then there are
some parameters that I think they have
some uh name is not not friendly one is
what Microsoft calls old Authority URL
that should be
this
you'll attach the token and then the
redirect rule that must be uh this
in this format
uh in this case you are able to
log in with the
O2
when you call the function
authentication is in process is done you
have a token and then you can call the
function and reading the response so
both authentication are actually
supported by Microsoft what to use
totally up to you but sometimes Azure is
directory
uh is one of the most secure and
Enterprise ready features to
to do that
uh slides please okay
uh
another important thing to remember is
that Azure function should be stateless
because you have no control when when
and where a function is executed so this
is one of the errors of sometimes I see
one part that you are using Azure
functions uh
if you want Azure fashion that preserves
States uh
uh during a process I think that you
need to have two solutions One is using
as I show later cues between
the process of the function or you need
to use another type of framework called
durable framework that is a framework
for creating Azure functions stateless
so stay flow sorry
what does that mean that you should not
do something like this so for example in
this case imagine that this is what I
see yes some months ago in a partner uh
what this call is doing this partner
wants to uh control the number of calls
to the function and make some logic but
if you do something like this so request
number Global and every time someone
calls I increment the request number but
this is not
correct because uh
you have the scale controller so when
someone calls the function if I have
only one goals it's okay but if I have a
lot of parallel goals the scale
controller starts and I have different
parallel functions execution so these
counts
will not be correct so
you don't need to do things like this
in an Azure function because
uh scale controller stacks
and another important and extremely I
think less no features of the Azure
function and cause of problems and costs
is the usage of HTTP client in Azure
function
what does that mean and normally
often quite often an Azure function is
used because I want to pass some data
from Business Center and from the Azure
function I want to call someone else
uh
normally what I 90 percent I see in
Partners is that they have a method
inside that method they call the HTTP
client
but this is not absolutely not the best
way to do that because
in the body of a function we create a
new instance of the HTTP client every
time
and
this can create uh
problems promise that starts from Big
memory usage so costs
and or more dangerous problems like what
is called sockets exemption so you have
a natural function that will stop
responding
uh
the recommended weight today to use hcv
client in Azure function is using an
object called HTTP client Factory
and I think that with the code is much
better to explain so
let me I previously closed the example
uh sorry I need to find
this
folder
come on
so in this example uh I will show you
three possible way from the worst to the
best of
doing HTTP calls from an Azure function
if it's a studio starts
okay
so what normally
I see
is that
this is the same Azure function calling
simple functions with rigor
calling
an external app
in this in this case this is a stupid
endpoint that gives me some poke data so
what not the
the common error that I see is that if
you when someone wants to call a natural
function creates a so when we want to
create an Azure function calling an
external application do something like
that so creates an instance or the h3d
client object
and then calls
the other
in point this is inside
the method
and calling inside the method
uh
creates an instance of the HB client
every calls without releasing resources
and this is prone to what is called
socket exemption so if you have a lot of
goals
this
your sockets will be exhausted and
sometimes the Azure function can stop
responding and you have also a big
memory usage
uh uh so obviously initial value calls a
few times these FS could not happen but
imagine you have an Enterprise scenario
where you have millions of calls to your
Azure functions this we can create a lot
of problems
so
the
a possible
best way
muscular or better way
to do that is do something like that
so in this case
I'm creating
a global instance
of my HTTP client object not inside the
code
but I simply use this Global instance
or mine
method so this is my function here I'm
not created as before
the HTTP client object might I only
reusing what is called as what I create
is global
and this is much better because I am
reusing connection
the only problem with that is that
it came
create problem with DNS changes because
if you change the DNS rules or something
like that in the external service this
is not reflecting the DNS changes
but is much better than before so this
is the memo requirement
that I suggest if you want to use HTTP
client inside Azure function
and not having problems
the best way and the recommend the
Microsoft way to do that
in
dot net 6 and before
and after sorry
is
do something like that more complex I
agree but it's come on
but it's
the best way in terms of performances
cost and so on
that is the using what is called the
HTTP HTTP client Factory object so in
this case I I need to add the
uh
a reference to the Azure function
extensions
and you get package
and uh
what does this code I'm creating here
a
HPD client Factory object
and this is maintained on the iPhone the
Azure function run time between
the course
and each time you call the function
the designer creates a new instance and
dispose the new instance when the the
the calls is is finished so uh
when I have this created uh
and uh in my function startup
here I need to
add
the HTTP client object
and I can also create more than one for
example if I have one service
also what is called name service so a
new HTTP client with the name and
inside my function class
I is create an instance in the
Constructor of the function class I
create an instance of the HTTP client
Factory object
by passing my hdb client objects they
want to include in that
Factory object
and then in
my functions called I simply call
DHC client
instance one of these HTTP client instas
that I creating inside the factory so
now these are for example if I uncomment
you can also create the HP client with
names
and this is the recommended way to do
that so what you need to do to repeat is
create create an extension of the
startup function where you configure the
uh what is called the Jos Builder you
add your instance of the hdb client and
then
uh you create a Constructor like this
with the HD design Factory where you put
inside that the definition of your HD
client objects and then you can use that
this is automatically disposed
efficiently by you and you will have a
great impact on performances and on
course if you use this Dash class
because
memory is not used efficiently used and
so on
okay
then another problem
that normally I see on Azure functions
is related to timeouts Azure function
have some timeouts that you need to
respect and remember consumption plan
has a default of five minutes and
maximum multi or 10 minutes
the Premium plan
is much more so
sometimes if you have a function running
for a lot of time you need to change
plan accordingly
uh
remember that's because this is a common
error that
regardless of the function time out up a
plan that you have uh if you are using
HTTP calls you have a timeout that is
maximum
this number of second uh no sorry sorry
this number of seconds
not five minutes or 30 minutes like in
the top of the slide because this is the
default timeout of the Azure load
balancer that handles the hdb client so
you cannot go above of that
and uh
another big problem of actual function
is what is called the cold start
consumption plan is the recommended way
to start but in a consumption plan Azure
functions can be placed to sleeping from
the Azure function runtime when not in
use and the next time you call a
sleeping action function it takes a bit
of time to react to go your function up
before responding
uh
this is sometimes a problem especially
for example if you use Azure fascial as
a book client for business center
because web books you need to uh
create a subscription to the webbook and
a response in a particular timing and
sometimes if you have a a natural
fashion sleeping uh
uh the Yen Shake is fails because the
other part is not responding in the
timer in the time in the business center
requires so you can solve that in two
ways one is going to the Premium plan
where you don't have a sleeping instas
never
you have always an Azure function up
running or the second possibility is to
Ping
if you want to still remain in the
consumption plan you can create a timer
trigger faster the pings your endpoint
or using things like application inside
this as a ping methods to being anywhere
else is totally free and this permits
you to having always an Azure function
running
remember that because it's a problem
sometimes another
tricks that I suggest to you to remember
is if you are using timer trigger a
function if you create a timer trigger
functions uh normally
you can specify
the timing of your functional execution
for example in this case is is a chrome
expression that means five minutes
every five minutes
uh
this is the default as Visual Studio
Visual Studio are doing is doing but
this is not a best practice having a
these are coded
because if I want to change these I need
to go again into the Azure function code
or I can change that redeploy and so on
so it's not recommended to that
normally the best way to do is making
that Dynamic and to make that Dynamic
you can use a syntax like this
uh
put your valuable names
inside that and uh
in this way you can retrieve the timing
from local variable uh
if you have a local variable because
your Azure function can be also locally
executing locally the bug and so on so
local variable can be placed in the
local settings file in this way and here
I'm placing the my string and
when I'm doing debugging this will read
that
and totally dynamic
when deploying on azure you need to go
into the configuration tab and you can
add here
your variable with your timing
and this will be totally Dynamic so
never please leave these inside Azure
function because otherwise you need to
change it's not dynamic
and then now one of the most important
myopic part of the Azure function
Frameworks and is the bindings the
binders is the possibility to
declaratively uh connect other resources
to your Azure function
uh and let Azure function take care of
the rest so you simply connect Azure
resource it to the your endpoint and
nothing more than that and these are one
of the main building block if you want
to create workflows in the cloud
because if I have one single function
that I call in the response I don't need
my Linux but if I have
something like this
the example that I will show
now in this example I have a solution
where in a standard application needs to
place an order
so called my point that receives an
order
uh my employee needs to check if the
order is valid and then giving
immediately a response to the customer
then it needs to save an order into a
database then needs to create an invoice
for that order and place this invoice in
the blob storage then need to send me to
the customer and also I want that daily
weekly I don't know a process that takes
all this creative order and generates a
daily report of the the order so it's a
being process complex
that I want to handle with Azure
functions
and yeah I have mainly two problems the
first problem is that
uh it's absolutely not recommended to
create a
a monolithic code that does step once
they choose the three step four because
it could go outside the timeout
and it's not reliable something fails
transaction is failed so I would like to
have a transaction of this process
reliable
and so this means that between the steps
I need to place something where my data
is safely stored IQs for example
and uh
uh I don't want to handle
the insertion of data into the queue
directly so I don't want to create a
some separate functions with the
Q trigger timer Trigger or something
like that in order to handle that I
can't do I can do that but I can okay
also use bindings and
to show that
I have
sometimes the mouse is not well
responding
uh you have these let me close something
I have this project
okay this project is a project
first I start and then I'll explain
I'm executing my function
and then
if I remember where I place the folder
uh
no
sorry because I don't remember the
folder name where I placed the uh
okay
this folder
because I'm searching okay I'm searching
for this file
that is the file where I have my sample
calls okay
uh uh the first thing that you you can
see when I I deploy I run this Azure
function locally is that here I have one
endpoint
that is waiting for calls so
this is the endpoint that is waiting for
my course
called receive order
and the other are not in point that
wait for calls but are in point that
react to events
attached to other resources like for
example we have acute rig I have a timer
trigger and I have a blob trigger
because in my example I someone calls
this tassimir in order when I have an
order I put that order into the a
temporary queue called
received order
when the order is placed like that this
is the
function that
uh creates the the order is will be
stored in a database in my case it's a
table storage on Azure but can be
Business Center for example
uh
then there's a function that when the
order is it is safely stored create an
invoice
uh and put the the fines The Blob
storage then I have the functional
starts from a Blog trigger and sends an
email to Mike to the customer say that
this is your invoice for uh for this
order and then I have a timer trigger
that creates the periodic generator
so if I
uh
yeah
if I
execute a call so this is a stupid order
that means oh if I am able to
that
I'm sending an order
so the order arrives to my Azure
function as a Json this is the Json
design pass it to the order and then
again it's placed into the queue
and then when it is on the Queue later
we explain the code but I'm creating a
object that times is
Json that I'm passing to my table
storage in this case of er you can call
business sensor for example if you want
to store business center and then
everything the process goes so if I what
happens is that if
my process now is finished correctly
uh what happens if I check the log here
you can see that a lot of tasks are done
so uh
here
the report generator function is started
it's the time of trigger that it started
then I
the sales report generator uh
this is where the function that received
the order is started the function that
they generate the order is started after
that
uh
so it's giving this amount like
generating voice for order blah blah
blah uh then the send mail to customer
process is started and it's giving me
some details like placing the log like
what is the file
the order processes and so on and uh the
report generator we started so all my
steps or the workflow are starting if
something fails I can
the transaction is not broken I'm not
losing orders
because I'm using a temporary storage
between the steps of my workflows to do
what happens under the wood
in my azure
uh
I use this storage account
and in this storage account I have some
containers
blob storage
one is equals invoice and one is called
reports where I should have the final
invoices
these uh if I can download
or
let me click here
download and this is a65
in my case I'm going to containing the
come on
okay containing the the invoice for that
order
and uh
there's also
the reports where I created the reports
for the order
and uh
where is
here I have the first queue called or
the received queue where the
when I receive an order I temporary
place the order in that queue that now
should be empty and okay it's empty
because the order is taken here and
processed immediately by the other steps
of the function if something fails
the order is still in the queue so I
next iteration I will take that order so
I never try to lose a transaction and
that's important if you have
complex workflows in the cloud and then
I placed uh the the orders in a database
in my case for Simplicity I use a table
storage so if I use the storage Explorer
here I should update and should be an
order placed on that
how to handle that in code
I have used bindings for doing that so
but what our mind is bindings are
possibility to in your this trigger
definition
declare
water resources are attached to the
trigger so in my case sorry for in my
case this is this is the standard HTT
HTTP trigger called
order receiver
but I I added something more to that
I added a q trigger so a key binding so
saying that when you receive an order
you need to place that into this storage
this queue
and
I have also other another binding
with a table storage
called order stable
behind this means that I don't need to
uh
do connections do authentication so
something like that all is handled by
that process and in my
my steps of these steps of the process
so they are receiving part of the order
simply with bindings I'm reading the
order and I'm placing the order in the
queue and then I place in the order the
Json or the Json of the order in the
table stops yeah I don't have connection
with the queue authentication storage
connection string and stuff like that
all is handled by the bindings
uh
then
let me stop this otherwise I have the
other steps so
the first is the order receiver then I
have the uh generating voice
the generating voice is
a q trigger so starts from when data is
inserted into the order receive a queue
and
generates the invoice
in my case by file into the blob storage
and
when a file is invited into the block
storage I have the sales report you know
sorry the same mail to customer
function
that as before
now this function has an input binding
with it or the stable
so parallely when the first function
saves the data into the table storage
these stars parallely and sends the
email to the customer by reading the
data from the table storage and placing
the data into my so this this order row
of this is the row of the stable storage
that I've inserted
and sends him a to there to the customer
using the output binding for same grid
so angry is a tool in Azure for sending
messages SMS or something like that
and then I have the sales report
generator that is
a function that
uh
periodically
so with the trigger that they want
reads the tables the orders table and
creates a report for my user with the
today are all these order was passed
from the external application so
bindings are important in order to
create concatenation between steps
without writing
uh
Uh custom code or uh or something like
that
another important part a new part of the
Azure function isolating in this case
only isolated mode is Middle worse
Midwest is a
possibility to create something like a
pipeline between uh Azure functional
execution
uh when you create a natural function
initializing mode this function has a
you send the request what is the clicker
yeah yeah you send the request here and
normally this is the functional response
and gives you a response but Azure
function also has a in the isolated
model as something like in the middle
that you can handle you can create in
the middle and different instances of
what is called a middleware that can
interact with the data before the
functional execution or after the
functional execution and this is
important for mentioning areas for
example authentications logging or
manipulations of the incoming or
outgoing requests or something like that
very quick demo of the middleware what
are the meters very easy to use
uh close this
and I also close this
otherwise I have too much window open
don't save this
okay
Okay so
yeah yeah very stupid so I call it a
standard Azure function called the same
message
HTTP trigger and function that I receive
normally receive a name and give a
response hello name
in this case
I'm uppercase in the name so someone
path name and
I want to retrieve the name uppercase
very stupid but just to show how
immediately works so
uh
when I uh
in this function 200 milliliters
you need to uh I said before only
isolated model so
this is a function in this relative mode
as a program in the program if you want
to handle middleware you need to do
something like that so add this
line of code that say that I want to use
middle words so I want to handle some
codes inside of the pipeline and like
what middlewares the convert message
meter is a my custom class
this
that needs to inaries
from a classical I function worker
middleware and in this I can
handle this method
where I can retrieve
the before uh this will be executed
before the execution of the function so
here what I'm doing I'm retrieving
uh the context of retrieving what I'm
passing to me uh
I'm passing the Json if the Json
contains the the name parameters
I'm simply uppercasing it
and I'm returning
uh to the Middle where by passing
updated this
context parameter of the middle there
are all documented that says that to the
Azure function that someone has modified
the body of the request the incoming
request
the Azure function does that so
if it's using middle words
I'm retrieving if I have updated body so
if I have someone as updated my body
before the execution
and then uh
if so it receives the updated body and
then in this case I'm saying hello uh
to my my endpoint so
inside the Middle where you can place
authentication custom authentication for
example logging or something like that
so if I call these uh
yet previously created no
the I need to send the guys today
because they died on there but as you
can see here uh first is the Middle
where we started not the function
this is the middle one that is reading
if I pass the function now I don't pass
I not pass the name so it goes on error
but it's reading the information
and now gives me a mirror because it's
not in the format that I want I not
passed the execution but just to show
that the function is not yet started it
started before the middleware and then
uh the function so
if you you do a post call or guest call
with the name parameter this works and
converts it to uppercase
okay uh now another important part of
the Azure function that I want to show
you is the
this
uh possibility to automatically deploy
Azure function so lots of time Azure
functions are deployed directly
uh from Visual Studio code to the cloud
works
but it's not always the best way to do
that and Azure function has the
possibility to uh
you can create a pipeline in Azure
devops or GitHub or something like that
uh
so that's one of the possibilities
recommend one of the recommended
possibilities or you can also uh create
what is called the contiguous deployment
to an Azure function to continue to
deployment means that you can when you
have the function app running you can go
into the deployment Center menu here
and you can connect
your repository where you have your
function code
the tab Azure devops or many others
when connected
you can select your repository you can
select the branch
that
will draw this deployment
Master Branch or other branch that you
have and when you have that
uh every time someone Updates this
branch
the code in the
in the Azure cloud is updated
and as you can see here
normally
you should not do that in the production
Azure functions as slots production and
you can create more than one simply by
uh going
sorry slides
uh
do that simply I go over here deployment
slots and create my one more than one
slot so not only production but you can
look also play the prey deployment
testing or something like that you
deploy automatically here your customer
can test with a different point when all
is okay you can simply click
this button
and
your test becomes production
automatically and so on with all the
settings
reverted and this is a good way
to deploy Azure function in the cloud
another
part that I think is quite important for
Azure function is I love eye level
it's quite common that when we have
business center for example to customers
in this case what I would like to do is
deploy my extension to that customer the
same extension
and if my Essential goals energy
function because maybe I have an apple
on upsource or something like that I
would like that
if the customer is in Western Europe
okay if the customer is in Western
Europe
I would like to call an Azure function
in Western Europe
and if the customer is in uh
Ops
with the clicker uh
if the customer is in the U.S I want to
call an instance of the function us that
these two functions as different urls
so I cannot do something like
testing the the the the the country of
the language of the the environment and
doing a big case if customer is U.S then
this is the end point if custom is uh
Italy disappointed this customer is uh
Belgium this other endpoint but I would
like to have in my app one single
endpoint
and the forwarding of the calls should
be handled automatically and uh one of
the service
uh that I
recommend the use for that
is the what is called the Azure traffic
manager the traffic manager is a service
that permits you to to have a single
endpoint
that redirects traffic to another
endpoint in this case the Azure
functions
according to the rules you want
rules can be priority rules
in point IBC and I can give a priority
and redirects can be normally what I
prefer to to employ two rules one is the
performance rules so your goals is
redirected to the functions that gives
you the best performance in temporal
latency
and the other that of quite sometimes I
use is a geographic routing geography
routine is that
the same as before so for example if I
yeah us and Europe customers I want that
your customer because the European point
and the other course the U.S endpoint
the performance routing is also useful
for scenario IDs so if I set performance
routing and I call my function
in the case I don't call my function but
I go directly the traffic manager and
points or single endpoint this is
intelligent to know okay you are calling
me from uh
this client that is uh
a client from a particular
location of the world I said this is a
performance so it Checks In This Moment
from this endpoint
what is the provided the best
performance
normally is this
but in this moment this is down
so I I stopped the function or something
like that
uh
it automatically see that this is down
and redirects my function to this second
point
so not all it's also able to react to
when the function goes down
and it's a
H it's important I think
also for so what does that mean is that
so simply yeah Business Center in
Western Europe I
in my app I don't have a case switching
but I I only call this a point that
redirects to the function accordingly to
the routing and very quickly configuring
traffic manager is absolutely easy
because just go
on the Azure portal
and
uh
select the traffic manager profile here
you can create an instance
and when you create an instance
give a name it's like the subscription
and so on and it asks you okay
what is the rule that you want to Route
traffic performance weight priority
Geographic and so on performance stop
simply you you select the your different
Azure function instance and then nothing
more to do here I creating for example
one based on
routing
geographic region so you select endpoint
when you have the literacy manager
instance you have a single URL that you
place in your app
but that you that you you need to create
the under the wood the under the use is
uh you select the endpoint so I click on
ADD I select uh Azure endpoint
I here I select I give give a name
uh here I select app service and then
you can select your functions
the function that you want so for this
endpoint can be these endpoints or this
function for example can be called by
uh in this case I'm using the geographic
so I need to specify the area that calls
this function okay this function can be
called from
all Europe or I can also go
uh this country this country this
country goes to that always to that
function the other goal always goes to
the function I'll end in my app
I only use
uh
come on
in my app I only use the URL of this
endpoint
this
and not the Azure function URL because
it takes it under the wood automatically
okay the other another important aspect
yeah
is
monitoring for different reasons
uh
Azure function as built-in iteration
industrial monitor so you can monitor
everywhere and normally when you use it
with business Central
uh if the Azure function is alone you
can connect the actual function to an
application inside instance by yourself
but if you are using the Azure function
together will be the central because
it's part of your business center
processes is recommended to use
redirect the data uh to the same
application inside instead of where you
have the the telemetric data or Business
Center because in this case if you want
to analyze a business process that
includes also external calls you can do
that
uh
monitoring is also important not only
for Telemetry in my opinion function but
also for testing because one of the
problem that I saw a lot of time in
Azure function is that you create an
Azure function that works perfectly
but
if a day your users moves from 10 users
to 100 users or you move this
differential from 100 of calls a day to
one meter or course per hour
immediately something explodes so
what I
normally do
if I able to switch
is protesting so I I want to when I when
I I know that I have an Azure function
that has a can have a big usage or a
variable user I would like to test how
my usual function goes if I have 10
calls a minute or one millions of calls
a minute
and you can test that
with for example a tool called Azure
load testing
uh Works quite good but sometimes it's
not easy to to test if you have if you
want to pass for example parameters
functions or custom authentication so uh
a tool that I personally recommend
because
I like it it's an open source tool
called
I can open a terminal yeah
sorry first I open initial function like
where I connected a Telemetry like for
example in this function
it's a
sorry not this actually because this is
an initial function
in this Azure function I connect to the
Telemetry so I have application insights
connected to that function
and I can click on view application size
data
to to check what happens is the usual
function and one of the nice features of
the Azure function to test
how it works uh is for example going to
the live Matrix
and in the right Matrix you can live
live testing your uh
your function so now my financial is
doing nothing because I'm not calling it
but with a tool like goload I can do
something like that gold is a tool that
you can
download from this URL
uh also git or from nuget and uh
individually you have the source code
that you can modify the source code
is a simple tool there you need you
select the name and you can be okay I
want to set test then the request to
this endpoint my usual function for uh
entire request in 50 seconds in this
case or 1 millions in uh three seconds
and if I execute these
uh Mouse come on okay if I open my
common prompt
not this common problem but the other
because this okay I play pass my test
and I execute my test goload start
sending
and you can see that
here my Azure function starts reacting
so I can see
our memory moves
I can see that the full set trace of the
calls so why is quite important because
I can see that I can check if uh with
the 100 of course a minute in CPU and in
memory
is okay
maybe if in one Millions fails or in one
Millions it goes the CPU goes up and I
start spending because remember that
spending cost is also linked to the CPU
usage
and memory usage
so uh you can monitor that
and when you have a
test and monitor imagine that this is a
live Azure function you can also go on
uh as usual I think that you are expert
on that
you can go on logs
what is logs here and you can
as in business Central monitor
everything like traces like uh requests
and something like that
and so on so you can monitor the traces
see uh
what happens in the camera request is
the parameter properties you might you
can also for Azure function you can also
monitor more than traces like incoming
requests failures and so on so
uh Azure function gives us access to
other of these metrics fields for
example is important because you can see
the sex trace of the code and see why
this function is fade maybe you have a
code to fix or something like that
last part
that I think is quite nice important and
quite new
is the possibility
uh to run Azure function on Docker Azure
functions
in the isolated model as said before
uh
are the touch
to the function runtime so this means
that
every platform that supports executing
the function runtime .net core or
something like that
can execute your Azure function so
imagine that you have a scenario where
you have invested a lot of energy and
money and so on on developing Azure
functions
for your Solutions
and you have a customer
I don't know like
the banking like NASA something like
that where security is extremely
important
and they don't absolutely don't want the
cloud
uh
if you have this problem you or you move
the code that you have placed into Azure
function in something like that works on
premise
or there's a problem
with that you function in the isolated
model you can solve that by embedding
the Azure function inside Docker for
example so doing that is quite easy just
do three comments that I listed in the
slides so the first is
this this command creates a function
with this name
with this runtime dot threat isolated
and
specify that I want the docker support
you launch it from the command line
or from before we use visual studio
right click the Azure functions Docker
support uh
here here I'm creating a new Azure
function tool HD with rigor and what
happens here is that I have a
project like we have done at the
beginning of the session that is an
https function
with the eye Docker file and this is the
docker file automatically generated for
you that you don't touch it simply
this Docker file
starts from my an image
that contains the Azure function runtime
uh
what you have to do
when you have you create your function
code obviously inside this one these uh
this file as as said before you use dlls
or something like that what you want
uh
then when you are ready you launch this
command Docker build you select the
platform
and uh
uh you can also place a tag to the
the image in order to build the image
and create a Docker image for you
this runs a bit no not too much but
downloads the Microsoft image builds
your function inside the Microsoft image
and then
simply when you have the image Docker
run the ports that you want your ideal
differential and you have the functional
upper running
locally fully
when you have that you can also push
this on for example dockerab with Docker
push comment
and when you have the function on lock
it up you can also embed the function in
something like Azure container instance
or other type of platform and just to
show this uh yeah I have previously done
before because live it takes time and we
are quite around out of time uh but as
you can see here in my machine I have
here
a image
or is corresponding to this part and
this in this image I'm simply running
Azure function so if
uh if I'm going to this URL
open okay we don't want to type
just to show first if I now I'm going to
this URL
open a browser
first I remove the function
so just to show that simply go in this
you can see that what the answer me is
defined the Azure function runtime so
you say me that okay it's not a custom
application this is the Azure
application saying me that okay you are
calling an Azure function local running
but is wrong the URL because I'm not
calling the Azure function in this case
but if I'm call
the right URL
that is
name of the oyster slash API slash name
of my function by passing parameters and
so on
the Azure function is responding and
this is the natural function Totally
Running locally so
in scenarios where you have
tons of your function
for your business and you have a
customer that don't want that this is a
possible
uh a possible solution
so this ends what I want to show about
that what I recommend in Fourier World
projects
uh
I open two questions if we have about
four minutes four questions
so if sorry if I don't see
after the third line but there's
is like in the stadium there's a light I
saw a
uh
I launched this
no I don't know if I don't want to
Center someone
hello
I don't see you sorry if you
the park
Azure functions in um
yes yes it's possible to debug in
production absolutely you need to uh
attach uh
uh the function to a process uh uh there
are a set of steps so uh
quick answer is absolutely possible if
you want to throw the steps I have some
uh slides to show for the steps not not
planned for uh for the session but I can
show that the steps needed you need to
see simply speaking you need to attach
Visual Studio Visual Studio code to uh
the Azure function process called UPC
dot X and we're not attached to that you
need to place the function in the back
end more temporary in debugging mode and
then you need to attach it to a process
from Visual Studio Visual Studio code uh
and then you can debug
I cannot explain uh now these steps
because you shouldn't see that if you
want I can I can show how to do that and
another question sometimes logs appears
not directly after a call of azure
function but in some time maybe in two
minutes three minutes logs yes but
that's this is a pro this is a standard
of uh application inside so logs uh
uh comes after a delay are not are
collected immediately but in application
size if you go on traces or something
like that you have a delay also in
Business Center is like this is not uh
automatically live so imagine function
you have you can go into the live
session as I showed before and you see
live what happens
but if you go on traces on requests and
so on there's a
there's a delay between uh
or it's not possible
to have in that real time yes
real time no because it's uh as is by by
the Azure platform so it's there's a
delay between when the the
the the front end shows you the logs
okay thank you I have
if you go yep if you have another
question I have three shorts to for sure
I don't remember
thank you
um in your serverless or order manager
this is basically you made it as fire
and forget
right PC it's the request we get 200 PC
gets a 200 back for PC it's done and you
implemented the retention policies all
the stuff but what if for example if you
have a data errors consistency errors so
a new example you also send the email if
the email is is wrong how do you then
make the process safe that PC gets aware
that it needs to be
if you want to have a reliable workflow
in with Azure functions uh normally uh
you should have steps between the
workflow so as in the example for
example with the bindings I'm not
directly doing the steps call and
receive but I'm do I'm using uh
middle words between the steps so for
example cues or something like that
there are
storage that costs nothing and permits
you to have a reliable transactions so
for example if I need to send an order
and during the order processing some
business center needs to take this order
and create a sales ordering Business
Center for example and something fails
during that
the order is still in the queue
so next time you re-execute the function
the order is taken to the queue again
and the process fail is it continues
very obviously you have logs you can you
can inspect widely function phase and
you can fix but the order is still in
the queue so you don't lose transaction
if you don't do that so if you have a
workflows that simply call a function
give me a response and someone from the
external task an order and the function
phase the order is lost so uh you don't
have notifications if you want to do
that uh
accomplish workflow in the cloud should
be reliable reliable means that you need
to handle uh
queues multiple steps or something like
that in order to have a reliable
workflows otherwise uh
otherwise it's not possible a long
granny workflows Azure fashion normally
are born to be
weak quick short-lived and so on if you
want to have a complex workflow you need
to do like in the example of bindings
and that you have in the slides that
uses steps and uses a middle word
between steps this is the only possible
way to do to be reliable the other
possible way not to explain this session
uh is using another framework called
durable framework that is an extension
of durable of azure function quite more
complex but the Azure durable functions
does exactly the same so out of the box
when you have a step they automatically
store this step into a queue
or automatically without you
you'll be aware of that every step is
stored in the queue and then execute the
next step the next step if a step fails
you have the transaction saved and then
you can repeat and so on so it's the
only possible way to to have a reliable
transaction is using that
otherwise calling and receiving a
yes it's the transaction phase
you you can log obviously but you need
to end by yourself
I don't have other other gadgets
if someone has other questions or if I
don't see like over
sorry
I'm sure that someone
you go to the office some considerations
directly calling business Central apis
and you prefer to put a
is it only because of the coupling or
because of some other limitations that
you faced with the business center apis
to call them directly
no uh sometimes I don't prefer call
directly Business Center API honestly it
depends on the scenario in many scenario
uh you know that business center API has
some operational limits by Design
uh if you have a application that calls
frequently Business Center apis or maybe
cannot use the LD same authentication of
uh business Central you don't want to
expose directly with the central apis
like personally I do we mention areas uh
you can create a sample size layer
between Business Center and your
external application by using an Azure
function so the external application
calls your Azure function
in the way you want with the parameters
you want the the format you want and so
on and then you in the back end inside
your Azure function call you College
Business Center so you know uh
uh yeah sure T director authentication
how to do that the other don't don't
care about that you know how to call the
apis
uh this is an effective way because you
can avoid the operational limit
because if I have an external
application imagine that I have a
need to interact with the production
machine
that sends me see like iot scenarios
that can sell me tons of millions of
seniors every minute
I cannot do and I want to do something
in Business Center I cannot interact
that to Business Center because uh there
are limits so
Azure functions are good for that
because you can create an Azure function
uh function can receive
have no operational limits on that so
you can receive all the requests you
want in the rate you want in the format
you want
and then you can call Business Center as
you want so for example typical scenario
I can place these millions of requisite
perminos in uh
a queue or something like that and then
I can process that and I can call the
Azure function with the rate I want the
business center apis with the rate they
want so this is a quite common scenarios
to have Azure function
the coupling Business Center from uh the
external application
uh
honestly I I recommend dimensional to do
that if if the scenario is simple
sometimes
and the the app is maybe handled by you
or something like that that you know how
the Json should be created how the calls
should be created and so on okay but
there is also quite common that the
external application don't want to
create a Json like a business center
requires down table is not able to
handle Azure the directory
Authentication
or
okay
so it's quite common
we have to I think
if the question is quick I have the time
for another question or not no so uh
if you can wait I only
or you can jump
