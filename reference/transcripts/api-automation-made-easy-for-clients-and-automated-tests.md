# API automation made easy for clients and automated tests

- **Source:** https://www.youtube.com/watch?v=0j_A-haYC9U
- **Video ID:** 0j_A-haYC9U
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 94m59s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

well ladies and gentlemen welcome back here in
room number eight our next presentation is uh API
automation made easy for clients and automated
tests so please welcome Tobias Fster and Simon
Fisher [Music] for joining our session uh we're
really happy to see such a crowd we weren't 100%
convinced and we're talking about a similar topic
at another conference where basically the audience
was maybe 10% of this so I hope we we found a tech
topic that's that's interesting for all of you um
of course we're going to talk about API automation
how you can generate clients automatically but
also how you can mock your backends so that you
can um easily do development automated testing etc
to first introduce myself my name is Tobias Fster
i'm a managing director at 4PS um by Hilty company
in Germany we create an ISV uh a BC ISV solution
for the construction industry so on the off chance
that you're working for a construction company we
also would be very happy to talk on the probably
slightly bigger chance that you're a technical
person that looks for a new challenge we're also
very open um I'm also a chief engineer at Hilty
because 4PS is part of the Hilty group and on
the community side I'm a regional director and an
MVP for Azure and for Business Central as well as
a Docker captain and if you find interesting
what you're seeing here please um go to my
blog tobsfer.io there you can find links to the
social networks um indeed my blog my podcast etc
with that I'm going to hand it over to Simon
who I'm very happy to uh join have me join today
on stage please Simon take it away thank you
Tobias yeah uh my name is Simon Fcher um I'm a
software developer at 4PS in Germany um working
together with TBS uh I initially started with
that development quite a while ago already back
when uh it it wasn't called AL but CL and that
I extended my focus soon after that um to CL um
and I love sharing what I'm working on at least
if it's worth sharing that's one of the reason
I'm here today um I worked with the community
in Microsoft before on different topics uh for
Business Central for Azure for PowerShell and
um I think you can't overestimate how excited
I am and also a little bit nervous to be on
the stage here today um if you want to reach out
afterwards feel free to contact me via the socials
or in the hallway during the walking dinner or
whenever you see me all right with that being said
uh today I will start with um showing how to
automate uh the generation of REST API clients
what it is why we need it and of course a demo
uh after that Tobias will show you how to mock
APIs during automated testing and hopefully we
will have some time for Q&A afterwards so let's
dive right in what is the problem um I don't know
about you but in my day-to-day developer life I
need to integrate more and more external systems
often these are uh REST APIs and uh working with
REST APIs in AL is a bit annoying at least in my
opinion uh it got better with a rest client module
thanks to AJ and Waldo but fully implementing an
API still means lots of repetitive work and code
um I don't know how what's your approach when you
start um uh when you get a JSON response from an
API and you want to handle that in code uh by the
way you have all these little uh lights who of
you is working with REST APIs in your day-to-day
developer life okay I see quite some lights here
that's so right audience that's good um so you
probably also created some custom uh data type
conversion to handle the JSON you got from the
API or add some fancy messages to uh debug what
you what your code is doing um and you probably
also manually crafted the message bodies you sent
to an API or the HTTP headers uh authentication
authenticating stuff that doesn't feel very modern
uh currently in AL and it's very cumbersome so
you probably know the pain of doing the same
or similar things all over and over again whenever
you need to integrate a new API in your system and
um in other languages we they already have tooling
to uh help with this to not do it all manually
and so we are not the first to struggle with this
in AL of course not um other languages are a bit
farther with that and you probably know a company
called Swagger they quite a while ago they created
um a specification to define REST APIs uh so all
the entities the operations and um uh relations
in it um this became so popular that it was uh
transferred to the open API foundation it became
the open AI specification open API specification
not open AI and having this specification made
automation possible um uh the specification
has been adopted by a large number of companies
microsoft is using it Google IBM PayPal and very
also a lot of smaller companies because of the
tooling that is available and part of this tooling
is uh or one of these tools is called Kyota um
what is Kyota for used for you basically feed it
uh an specification and will generate the client
for you um Coyota supports uh .NET languages
dot go java typescript and yeah I know this
is BC tech days not net tech days or so so um now
there's initial support for AL and Kyoto so uh I
added that a little while ago and it's that's what
I'm going to show you today um coming with that I
will come to my first demo and just so you know I
will switch a bit back and forth uh through demo
and slides to give you a better overview and we
will start with generating the first client and I
uh oh no sorry first show you this this is the uh
demo specification that we are going to work with
today um Swagger provided uh this pet store uh
specification it contains some entities like pet
uh store and user and some operations you
would expect like put post get typical
um just very typical API um what all everything
that you see here is basically just the UI or the
uh for the specification file here it's this
JSON and in this JSON all the entities or the
operations and possible paths are defined so when
you've worked with an API before you probably know
these kinds of uh files so um with Kyota let me
just launch it here really quick um what are we
doing we call uh to generate a new project with
an open API specification the one that I just
showed you uh say which language we want to use
and then in which directory we want to put it and
the name so basically the important part is just
the file and the language in our case it's already
done um it's generated here based on time stamp
you see was just generated let me quickly copy
um the symbol file so that when I open it in VS
code I have no compiler errors right away um but
before I dive into the code let me just show you
one more slide um what what did we just generate
here uh you will see an API client that basically
provides some basic functionality and high level
entity access to all the entities you saw uh
request client classes and request builder classes
to talk with the API or execute the functions and
the model classes for each entity like pet or user
that are um wrappers for easier access with the
data what you will also see in a bit is that this
um extension has a dependency inn net uh Microsoft
has a package called Microsoft Kyota bundle
um that provides some library functionality
for request handling authorization handling
so I'm doing something similar with
an extension called Kyota abstractions
uh that contains similar uh helper functions and
interfaces so I will walk through this now um
let me first show you the result i added a small
test page so everything you see here above is
generated and this one here was just copied by
me let me just execute this uh or publish this
um extension so that you can have a look
that we can have a look how it works
so test page is very simple we have a um we
just provide an ID and we can call get here
so when we call get it will query the API
and we have a response there's a name test
we have status is available the response was
success we could try I don't know any other ID
uh and see I don't know if it's also available
no this pet does not exist but I don't know
whatever we use we can just um okay also doesn't
exist but we basically can verify it via the
um test here let's have a look 999 execute and we
will see it's test and available that's basically
the same we just got but we didn't have to write a
thing um to make it happen um so how did we do it
the behind this action basically let's ignore the
variable uh resetting basically the interesting
part is are these two lines so we have an API
client um where and we want to call something on
the entity pet there's an indexer function which
uh receives as a parameter the ID that we want to
look up and then we call the operation in this in
this case it's a get it could also be a delete or
uh I think a post so but let's keep it at get
if it was successful we uh the we can check the
success response on the client we just access
the from the return value pet from the return
pet we just access the property name so we can
access any property we have categories that is
uh yeah ID name photo urls it's a list
of text so things that you would also
uh so that you can easily access everything um
but yeah the actually interesting part is then
in the API client right so let's have a look the
API client um let's ignore the warning for a bit
we all know AL likes its variables sorted by type
and Kyota likes it sorted out alpha numerically
so that's just Kyota's style of ordering variables
um we have some configuration methods in here some
um and besides the configuration we have
methods for each entity pet store and user
um each each entity uh method returns a request
builder class basically so and in the and for each
level of this we just pass down the configuration
of the current client that we that we're working
in so when we look at the pet request bidder in
our example because that's what we worked with
um we have all the operations that you also see
in the specification if we go back we can see we
have put post get under get we have find by status
find by text uh this index functions here and an
upload image that's the same that we see here we
have find by status find by text post put and for
uh the index functions uh or the index operations
we have uh this method called item idx so it's a
generic function whenever you have uh yeah access
something by an index this will be generated and
we will pass down the information there as well
and oops on this one we will have um again the
operations delete get post but for the specific
item of the entity all these requests are built uh
similarly we pass down u a config object basically
to a generic request handler code unit and specify
the HTTP method we want to use and then call
actually handle the request so for delete we
don't have a response type but for example for
get and post there are two more lines if it was
successful we will pass down the response into
the actual entity object so each uh each operation
function is very small and generic the um part
that's interesting is then in the or the technical
part is handed in the request handler so that's
let's have a quick look at the um Ky abstractions
sorry um that's the library helper app that
I mentioned earlier so in here we have this
um reco center sender code unit um it you can set
configuration in here set a body if we want to
post messages and in the end we have uh this handy
request function and it's also very simple build
we craft the request message with a restclient
module code units um set whatever we need write
the body and then send the message and the little
magic is in here because the config packages
contains a reference to our API client um here
we just you see it's a it returns an interface
of Kyota API API client and we set the response
on this object and this is done um here so as you
can see we passed down the reference to this code
unit so you configure set all the configuration on
this code unit and pass on the actual object so
in here we then have the option to read out the
response that was set in the client uh in the in
the uh recus handler function uh so this wouldn't
have been possible early in earlier versions or in
like this was introduced I think in the last major
version so um uh this approach is only possible
very recently um yeah that's basically the AL
part know um but I guess you are also interested
in how this actually works and if you don't like
the design how you can modify this design right
um so let's have a look at the uh implementation
very quick let's go back to the slides that was
now client in that oh I forgot something sorry
let's go one let's go back here to let's one
look at the you saw the request beta classes
let's look at one of the model classes all
of the entities like pet user store and some
um others have corresponding code units that
uh so that you can easily access all the
uh properties of it there's a set body function
with a debug switch that so that you can test
the reading and writing of all properties but
you don't need that always but besides that
you have getter and setter functions for each
property um so now the the pet is a small pro
um entity with not too many properties but if
you have um entities with like 200 properties it
gets a bit larger and this way for each property
you can just pass down an object of of it with
a value and it will create will be set um also
each model code unit has uh so-called two JSON
functions or serializer functions the two JSON
without parameters will just return the currently
uh read um JSON body basically which we got from
the API and if you need to manually craft a new
object there's also always a function which uh
receives all the properties as parameters so that
you can manually build the object yourself but
without manually crafting the JSON your yourself
uh this JSON helper is also part of this
abstractions package so that we don't have
too many redundant code in each um extension
and yeah I guess that covers the AL part um
how does this work in in Kyota so Kyoto takes the
uh specification file uh it then walks down the
uh all the operations the resources the
relations between them and it creates a
generic code model or document object
model that is the same for each target
language so this model contains classes
methods properties everything that is
um the same for just it it builds the
specification in code basically after that
some language specific refinement happens i will
show you that part later on and then this generic
model is translated to the target language in our
case AL but you could also translate it to C Java
TypeScript or whatever you like and is supported
so let's have a look at the Kyota changes
um let's start at the refer um the refiner the
language specific refiner you see there are
refiners for C for dart for go for example um in
AL we don't have async await and kyota by default
adds cancellation tokens so that you can cancel
longunning um operations but al doesn't support
cancellation tokens so we can just uh remove these
from the um from the from the uh generic model so
rem remove parameters here cancellation tokens
and also the request configuration in this case
because we take another route at uh in AL but it
basically with this crawl tree we just walk down
all the elements from the top of the specification
to the last operation and um check if any element
is there containing this what we want to modify
there are also um some functions for example move
properties to methods in C you probably know
there is you can just add a get and set to
add a to create a new property on a variable
um in AL we don't have these this property
identifiers or access modifiers so we just um add
this getter and setter functions so um everything
that happens in here is so that we have a working
AL model later on and with this generated code we
then for for each element the the specific variet
is called later on um let's look at the one for
code units that's called a code class declaration
writer and we come in here with a code class a
class declaration element and basically we first
check if we have any name spaces um or any using
we write that first and when this is done we
will write the actual code unit identifier get
an object ID get the name and start basically the
object with uh properties like access internal or
other properties that we might define as defaults
and then uh if there are any global variables so
we have basically now the header of the code unit
and after that we can go to the methods because
code unit consists of methods and variables and we
already handled the variables part so let's have a
look at the method writer this is a bit more um
uh there are more different cases here first we
write basically the signature of the method um
if it has an access identifier like internal uh
and then the the method name the parameters and a
return type after that we just start with a begin
handle the actual code in the method and after
the end let's look at one of these methods we have
different cases here for example a serializer or a
request executor the serializer in our case is the
are these two JSON methods so we want to serialize
the values that we have on the object back to JSON
and we have two different kinds of uh methods
one without parameters and one with parameters
so the one without is easy we just return the
current um global variable that is defined in the
um on on the as global and if we have a to JSON
method with parameters we create all these um all
the lines of code that you basically saw in here
so add to object if not empty and the target one
so if it's a collection type variable we iterate
iterate it um and if not we just add it there's a
different case for enums if we want return it
we might return it as integer but yeah that's
basically how we write everything we you see there
are quite some messages or some methods in here
that we need to handle and um right now it's not
perfect yet uh because we needed my I need to do
a little work around um you will see some helper
functions in in here like this is local variable
because my goal was to not modify Kyota standard
code except for the parts where the enum like add
language support for AL was necessary but I only
added new objects and didn't modify existing ones
uh to make it easier later on to merge it back to
the Microsoft repo so we have um I have introduced
so-called custom properties the custom properties
is a small workaround where um each Kyota element
or code element has a generic documentation
property and basically I just append to uh
to the documentation property I just append some
key value pairs with these properties and later on
read them out so here for example it's written to
the description template it will be stripped away
before actual documentation is written but that's
a workaround right now to avoid modifying the
standard Kyota code so if you stumble upon these
custom properties um just know it's it's currently
a workaround not sure if it will be in the final
version i also explained some of these things to
make it easier for you if you want to work with me
on this fork um edit a read me to make it easier
to uh get an idea of this repo um because Kyota
has quite a massive code base um and yeah the
this very generic approach took a while to really
wrap my head around around um yeah I think that's
for Kyod right now um current state of this
change uh I initially created a pull request
in the Kyota repo um but I was unaware that there
is a community approach uh that they used before
to add uh new language support so right now
I'm uh in contact with one of the maintainers
um so that we bring the code in the community
repo first and then after it's uh basically tested
there we will merge it back into the main repo um
the this companion app the Kyota abstractions that
I showed you earlier is currently in my personal
GitHub um of course public but my goal would be
to make it part of the system app or Microsoft app
so that it can be shipped default by default with
um uh with business central so similar to the I
don't know Azure blob storage module um and right
now please be aware there might still be bugs um
uh we still need to test it it's um an early draft
but it would be great if some of you uh clone
this repo um try it out test it against your
own APIs or the ones that you are work working
with and uh give feedback and let's try to make
it um production ready code if you want check out
the uh repo uh of course I will afterwards also
publish a blog post with containing I don't know
20 different links to um answer all questions uh
which resources you might need um so don't worry
uh there will be a summary post afterwards and
with that I will give to toss thanks a lot Simon
um yeah give a round of applause Simon did that
I hope this gave you an idea and I can only echo
what Sean said please help us out here um take
a look at it improve it give us feedback what you
want to do differently mostly Sean feedback um and
then I hope we can create something that will
help all of you with the with the work on API
clients with that I want to move into the second
um topic and that is kind of on a related problem
um because the the basic starting point is the
same we need to integrate more and more systems
uh via APIs that's what Sean explained and I think
by by show of your lights you showed that you also
have that problem um but that's not the end of it
we on the one hand side have the the topic that
we need to integrate into BC when we also have
the topic that BC needs to integrate into other
thirdparty systems so it's not only about the APIs
that we have in business central but it's also
APIs of third parties simon showed you how you can
generate a client for that and I want to show you
how you can tackle a different problem which is
that we during development and um test development
we often face some challenges I guess it's kind of
similar for you where it might not be that easy to
have the systems available for example if you're
integrating with a third party that third party
might actually be kind of a competitor so you
might not even have access to it or they limit it
to a very highly priced model or um they are just
techn technology why is not aware that there might
be something like a deaf environment and they are
not stable enough so you might get flaky results
by talking to that um test or deaf environment or
something like this then we have the topic of data
so what you specifically want to do with a
third party or even what you want to do in
BC you often times for those API integrations
and test automation you need a specific set of
data and that of course can also be a challenge to
generate that data to have it in place and uh make
sure it's there when you do your development or
run your automated tests and then the last part
of it could be scaling depending on what exactly
you are doing maybe it is a challenge that um
three different people are doing development or
three different pipelines are accessing the same
backend system you might get into each other's
way that might again be business central or third
party solution where you have that issue and the
question of course is how do we solve that um an
approach to that can be mocking where the idea is
that instead of having the real business central
or a real third party system you have a mock
instead and what that means is that it accepts
the same requests as long as they are relevant for
you as the real system and they respond with the
same responses that the real system has so that
means that instead of talking to the real system
you talk to a mock that stands in between behaves
acts like the system that you want to integrate
with and so you strip away the dependency on the
actual system you only depend on your mock which
you have very much under control that's basically
the main idea I want to talk to you today about
how can we mock business central so if you create
additional clients like an additional front end
an app a portal or or a thirdparty system or if
you want to mock a third-party system that you
want to integrate with how can we do that easily
so that during development and automated testing
you don't have the dependency on those systems but
you have everything under your control what I want
to use here and and introduce to you is wire mock
you can see the description um that they provide
on their homepage an open source tool for API
mocking and um yeah the the last part I think
is very interesting it's about isolating yourself
from flaky third parties that's a less friendly
way of saying maybe there's someone else who isn't
in full control of their environment and of their
technology you don't want to depend on on those
um kind of offerings instead you want to have it
under your control it does allow you to mock
those APIs um through JSON files and through
code and we will see both approaches today we can
not only do that by hand we can also record those
API calls so we basically make the API calls get
a recording and use that to create our mocks and
we can also implement stateful behavior i'll show
you in a second what that means of course we're
at a developer conference so the first thing
we're going to do is a hello world and let's
dive into that one and what we want to do in this
hello world is we want to create that mapping we
want to load the mapping and we want to make the
request to the system so that you can actually
see the hello world how does that work we will
create a hello world.json file and I hope this
is big enough for you to read also in the upper
area looks like it okay so um what you see here
in this JSON file the first part is the request
um where we have the get so we're basically saying
when a request comes in it's a get request and
it has the URL of some SL thing then we want to
react how do we want to react we want to create a
response with a status code of 200 we want to send
a body hello world from BC tech days and we want
to send a header with it if we now um ask wireok
whether it knows about that there is an admin
API that you can see here so underscore_admin
gives access to wireok itself so to speak and we
if we ask it about the mappings then we get an
empty response because we have just now created
that JSON file so what we need to do is we need
to reload those mappings we've done that if we
now ask it again about the mappings then you can
see here this is the list of mappings so you can
also query via mock and ask it which mappings do
you know if you get weird responses or something
you don't understand that gives you an insight
with that we have it in place so let's show the
actual hello world we're just going to call the
wire server on s thing and it responds with hello
world from bc tactis so this is basically um the
the very minimum way how you can use wireok you
start an instance you put the JSON file somewhere
you might have to reload the mappings and then
you get the responses that you defined according
to the requests that you defined so what have we
seen we created the mapping we loaded the mapping
and we made the request and saw the response
so I would say hello world is accomplished
what is the real scenario I want to tackle the
first one I want to tackle is mocking business
central so basically you can assume that
you have a client application or some other
uh service system that makes an API call towards
business central but instead of calling it
directly we want to call wireok so we use it to
do the recording in this setup and then we can
basically strip away business central completely
because wireok now behaves exactly the same as
business central would behave so I no longer
have that dependency on wireok sorry on business
central but I only need my wire server and as
an example we're going to get companies because
we always need companies when talking to the REST
API and then we're going to do um reading creating
updating and deleting of customers so um the the
CRU actions um on customers so what we need to do
is we need to mock the responses for get companies
for get customers based on the company for getting
a specific customer based on the company and all
of that we're going to do in standard wire in Java
so wire mock um originally comes from a Java back
end i'll also show you the .NET implication in
a later part but first for the first one we're
going to use the Java implementation and record
and optimize those JSON files as a client and
that's actually the less interesting part because
I basically care about the mocking and less the
client so I only created a tiny C# application
for development and testing that is done in dev
containers so we have one container for the client
application one container for wire so we always
have access to that one and if we have time in the
end I will also show you how that setup works kind
of the advanced topic that I also want to show you
here is stateful behavior and we need that because
we want to create a customer read update delete
the customer so basically our scenario is that we
want to create a new customer and only then can
the customer be retrieved before it's created we
expect to get an an error message when we call for
it um we also need different responses before and
after the update has happened because we changed
it so the response should be different and then
after it was deleted we again expect to get an
error when querying for for the customer so this
basically is the setup of the stateful behavior
depending on previous calls that were made to
the mock the mock needs to react differently
it we can't just define everything statically
but we need to have some kind of a dependency
and that is done via scenarios we have a name we
have a required scenario state that means where
does the scenario need to be so that a specific
call is happening and then we have a new scenario
state if we want to move ahead in the state that
also means that we now need to mock additional
um endpoints so we now when we query for the for
the customer need to have different responses
whether it has been just created whether it
has been updated whether it has been deleted
we also need to implement the post and the patch
for creating and updating the customer and then
in the end the delete call to make sure we
can also remove it how does this work let's
jump back into our demo and as a first step
I want to show you how we can record that you
remember the hello world JSON we just created
but that would be a lot of work to create all
those requests and responses so instead we can
tell wire mock to start recording then we make
the calls that you want that we want to mock
we stop the recording and then as a result we
get the files that cont contain those requests
so the first thing we need to do is we need to
let viog know that we want to start recording
there again you can see a call to the admin API
um to slashrecording start we let it know in
line 15 what the target base URL is so that's
basically the instance of business central I'm
targeting we let it know that we want to extract
the body what that means you will see in a second
and also we want to capture one specific header i
could also capture all headers but probably not
necessary um but if you worked with the Business
Central APIs before you know that there is this if
match e tech header that is important to make sure
um you can only patch something or make changes
to something when you have the latest state so we
also want to simulate that in our mock to make
sure in our client we also respect it properly
if we call that we just get a 200 which means
recording has started so now we can go in and
make the calls that we want to make in this
example I have set up basic authentication
note that in line seven I'm now not talking to
the business central instance but to wire because
wireok is acting now as a proxy between me and the
the business central server so that it can record
the settings first one that we're doing is a get
for the companies and if we make that call it now
takes um a bit almost two seconds because we have
targeted business central so there is um a bit of
a response time then we um store the first company
ID in a variable and then get all the customers
now we get a list of all the customers we remember
the first customer ID and get a response for that
one as well now we want to create a new customer
so this is basically the post request we give it
a a display name of Falcons which is the baseball
team of my son so I want to show this to him that
I actually used it here um and there we get the
response you can see here the display name is
Falcons as expected we need to again remember the
ID of that um created customer and try to retrieve
it so if we get that one that works and now I
need to do a little trick by copying the E tag
because I couldn't figure out how to properly read
that from the response but with that we should be
able to call the update now the display name is
tsklling which is the basketball team of my other
son so everyone in the family hopefully will be
happy um and we can get the created customer get
the modified customer again so now the response in
the display name should again be different because
now we basically made a change business central
of course is aware of that but when we mock this
we need to keep this in mind last thing now is to
delete the customer which is just a delete call
we get a 204 response and if we try to get deleted
deleted customer we get a 404 because the customer
is no longer in place so this is basically the
scenario that we want to mock we get a customer
we create a customer we update it we delete
it and we have the different get requests in
between to make sure we have everything in place
now I stop the recording so from now on um wireok
is no longer proxying towards business central
but instead when it now talk to wireok it's only
based on those mappings that we have um generated
so if I now would do a call towards a I don't know
sales order or something like this would no longer
forward it wouldn't have a mapping about the sales
order so it it no longer would be able to respond
um what have we seen we started the recording we
made the calls and we stopped the recording and
what that means is that we now have a bunch of
files so you can now see here in the folder that
we have for example the body of the um call to
get companies and here we have the mappings um
that also are are generated but they have those
cryptic names based on the URLs and the ids that
are in there so we want to do something about that
um if you just use them as it is if if this works
already out of the box if you don't have state
etc then it probably is fine if you just keep
them if you keep working on those APIs then it
makes sense to rename them to something that's
a bit more meaningful so we need to also make
some improvements I want to show you um how we can
make things a bit more dynamic which is why I have
renamed the files so it's a bit easier to navigate
and I would encourage you if you work with VM to
do the same to give them a bit more meaningful
names than just the generated ids so if we move
forward um this would now be the example of the
call to get companies as we've seen before it's
just the name is now companies to make it a bit
more easy to read we have something very similar
to the hello world in this case it's a get request
to slash companies and here we have the response
um in this case 200 the content type is set and
the value of the uh company is also included now
this is basically a very small file i can just I
can still overlook it so here we could have the
body still embedded in the in the mapping file uh
what you also see is that we have a fixed ID here
and of course in business central that makes
sense because we're going to reuse that ID for
later calls and the ID needs to be the correct one
but you also might have different scenarios where
you want to randomize such an ID or if you work I
don't know with items or um something else where
the the ids are not fixed you could use something
as you can see here where you just generate a
random value so if we now reload the mappings and
make the call then you can see on the right here
in line 10 it's now an ID that starts with 80 if
we make the same call again it's a it's an ID that
starts with 81 so you can see the randomization
works of course in Business Central that's not
too helpful so let's switch it back to the to the
fixed value but just to give you an idea you can
randomize um stuff in here another example would
be a date field like the system modified ad that
we can see here that one would now be fixed to
a date somewhere in February but maybe as you
progress you keep using your demo data you want to
make sure that those date fields don't get too old
so we can also do something like this where we say
this is now min - 7 days so this is basically now
um created dynamically instead of using the
fixed value that we've seen in before so if
we reload the mappings again and make the call
now you can see in line 18 that it now says
um last modified date was on the 5th of June
which is a week ago so basically this is a bit
of the dynamicity that that I can bring in here
easily another part of the uh request is when we
get customers for example we have the um get
request here this one um points at a specific
customer the response you can see here where we
have a lot of headers we have the status and we
have specifically here a body file name that is
what I mentioned in the recording that I want
to extract the bodies into a separate file which
has happened here so now I don't have the mapping
and the body mixed in one file but I have two
files that I can handle separately and this is
just what the what the body file would look like
i just have the JSON payload um and I can easily
handle that and manage it another example um is
the request to create something new so here in
line six you can see that I'm reacting on a post
request and I'm now matching the full body in line
so I'm basically saying the body has to be exactly
the display name the the type etc and then I want
to react on it the reaction now has a different
status code of 2011 and um I'm again extracting
the body into the into a separate file to make
it a bit easier to manage and handle the next
example or to show you how that works would be the
fetch call to update a customer so very similar to
the thing that we've seen before we have the if
match header here so this one makes sure that the
e tech if match logic in business central also is
mocked in our wire mock so that um whatever client
you generate whatever client you um you develop
also is sure to handle that properly otherwise
um you might run into issues when you talk to the
real system the response very similar extracted
to a body um and a status of 200 last one I want
to show you is the delete call that one is again
a bit easier because we have um the method and the
URL of course but the response now doesn't have a
body at all but instead we just set the status to
four in line what's this nine um so basically that
the delete call um doesn't return anything just
the status and and that's it so that makes the
mocking a bit easier so that's what I wanted to
show you um how you can structure those files make
sure you have proper naming in place my suggestion
would be to um remove the bodies into separate
files so it's a bit easier to handle and uh you've
seen how we can use those pre-recorded files but
still have a bit of dynamic behavior by using
uh the randomizers um or by using the the date
changes that you have seen we also have the state
topic and unfortunately that doesn't exactly look
like it like I wanted it to but let me show you
um this is basically the state graph that we want
to implement so on the left we have the fact that
the customer is not yet created this one should
respond to a call to the customer um with a 404
once we created it it goes into the state created
now if we try to get it the response should be
the created customer then we have two options
when it is created we can modify it and then the
response is um the modified customer or we can
delete it we can also delete it after it has been
modified and in a deleted state it now must return
um the error message again because the customer
is no longer there how how do we do that um we
have two two or three depending on the the file
additional elements in here and you can see in
the create that we are starting what is called a
scenario so the scenario basically is a collection
of those states we call it crowd customer and
after the create we can see that the new scenario
state after that call has happened is now crowd
customer created so we basically have our scenario
and we move it into the first state then if we try
to get the created customer you can see here that
it only reacts via the required scenario state if
we are in the created state so only if the create
call has happened we move into that state and then
this one matches so the response is um that we've
seen same for the update call in the update we
expect to be in the created state because we
can't update it if it's not there and once it this
call has happened we move into the updated state
and I actually also wanted to show you
the delete but I guess you can imagine
the delete can only happen based on the modify
and the updated um and then it would move into
the deleted state if we now take a look
at the scenarios you can see we have the
created state we have the deleted state we
have the updated state and then also shows
all the mappings so that you understand
what um contributes to your scenario so
you can keep an overview if something acts
weirdly or or doesn't work as you expected
so what we can now do um that we have all of
this in place is that we still talk to wire
moach but because we're no longer recording we're
no longer proxying this is actually using the JSON
mocks that we have provided so if we do a get
we still get the expected response if we do um
a get for the customers we get the right response
because we have mocked if we query for a specific
customer we get the right response we can create
a new customer with a name um you see in line 42
and we get the right response in line 22 we uh
try to get this customer again this is sending
us the right response then we try to update it
and I forgot to change the e tag so now you can
basically also see what happens if we don't have
a match it lets us know that um it actually works
so we see the closest stop um the scenario is
the right one but we don't have the right E tech
so let's try to Oh oh no that's the wrong one
no
doesn't want to let me copy
the right thing let's try again
call the modify and now we have the modify the
name is changed to what you see in line 20 then
we can also get the modified customer because we
have now moved the scenario one state ahead it
also is returning that one we can do the delete
that one accepts just responds with a 204 and
if we now again query for it we get the our error
404 and just to remind you this is now all talking
to wireok behaves exactly the same as Business
Central would behave but we don't need a Business
Central system in the background we only need our
Viomox server with the um configured JSON files
so what you've now seen is how we can implement um
that stateful behavior by setting those scenario
state required scenario name required scenario
state and new scenario state by moving things
ahead in our state graph um so what we now want
to do and that's actually the most boring part I
think of the demo is that we want to use the mock
um to show you that we have everything mocked and
how we can use it in development and testing and
as I mentioned for that I have created a small
C# client what that client does is that it just
gets the companies iterates over the companies and
um shows the responses and also gets all the
customers per company and shows all of them
then we go in and retrieve a single customer
where we know the ID and show it we create a
new customer again we make sure that we have
the right body because otherwise wire would not
um react appropriately and then we read
it again we have the update call where
we change the display name and make sure
that the change actually happens so we
get the right response and then we delete
it and expect um the delete to fail in C#
that means that an exception would be thrown
that we can handle so if we just run that one
you can see that it it's sending
the requests and from the speed
that it has gone through all those
scenarios you see that this is now
actually talking to wireok and not
to a um to an actual BC back end
so this would be the client application but we
can not only use it for clients but maybe more
interestingly even we can use it for automated
testing what would that look like in in C i'm
setting up a number of constants here and then we
would have for example um in a call that retrieves
a specific company uh make sure that there are
actually companies checks the first company make
sure that is the right name and has the right ID
and also the modified date that we um added the
dynamics on is not is is newer than 8 days ago
a similar one would be that we get a specific
customer so again we use a client to get the
customer we make sure that it has the right the
expected display name um has an email address in
this scenario and also has a valid modified date
um I'm also trying to um get a specific customer
here there I'm again checking the display name and
the customer number i have the create call where
we um set up a new customer and then retrieve that
new customer so we make sure that the post also
works by checking um the responses here again and
we have the update where we basically first create
the customer we update it we make sure that we get
the right value when we query for the update and
in the end we again have the scenario where we
delete a customer and make sure that the customer
actually no longer exists so this is just standard
test code and it would look exactly the same if
you would query a BC system so that's kind of the
main point I want to make here the the test code
doesn't change you write your regular test code
the additional benefit is that you no longer rely
on Business Central on a Business Central instance
to be available but instead you just spin up your
Wii instance so if you look into the tests and run
them once compilation has finished that one should
be quite fast yeah it has been 418 milliseconds so
basically the whole scenario didn't even take half
a second which again is an an additional benefit
of doing things with a mocked back end because
you're a lot faster if now the back end changes
or my client code changes um I as a developer can
figure out very quickly um that things are maybe
broken and in my uh pipelines this only adds
a very small amount of time to make sure my
integration still works so this is what I wanted
to show you for using the mock um basically now
we have the full life cycle we have seen how we
can create the mock for business central and how
we can use it in development and test development
that basically concludes the first demo so you've
seen the recording you've seen how we can record
the steps that we wanted to do how we can optimize
them you've seen a bit of the renaming the
dynamic values and the header handling the
the e tech handling that's specific for Business
Central you've seen how we can handle stateful
scenarios and also how we can use the back end
for um development and test development that's
basically the first demo the case when we want to
mock business central but also we have the other
way around now in this case we're in business
central and we have a third party that we want to
talk to similar to what um Simon showed us as an
example when you have a REST API and you want to
integrate it into business central again we take
the same approach instead of talking to the to the
third party application that we maybe not don't
have control over where we don't have proper deaf
and and test setup instead we put wire mock in
between and when we have set it up we don't need
the backend system anymore we only rely on stuff
that we have on our full control and I want to use
also the exact same example that Simon has shown
you the pet store application where we want to do
um create read update and delete again and I will
also um use a client that has been created through
Simon's Kyota um edition so this is basically
the the uh generated code in action again what
we need to mock is the get call so we want to get
a specific pet and we want to also get random pets
as you see in a second we want to create a pet so
we have to mock the post call we want to modify
it which is the put call and we want to delete
it which of course is the delete call um this
time I'm using wireok.net the reason for that and
not using standard wire is that my Java days are a
bit past so I'm more uh okay with using net and um
that's why I switched to vmok.net so we can use it
for recording and also then when we generate code
I'm a bit more familiar with that but the basic
concepts are the same you have the mappings
you can do dynamics um you can do scenarios
etc the client now is in business central
as we've seen um in Simon's demo already
and I want to show you how we can use it during
development and testing so how does this look like
let's go in here again what we want to do is again
as in the last example I don't want to craft all
of this by hand but instead I want to do the
recording make the calls stop the recording and
then I want to show you an additional tool called
wireog inspector that we can use to generate the
code so this time um we're innet and you can
see here that we set vomog up so this is just
the standard um configuration we wanted to listen
on port 9059 and we don't care about this message
um we start the admin interface this was the
underscore admin calls that you've seen before
if we want to have that we need to enable it and
we have a logger that just writes some output
and then if we are in proxy mode we have two
additional settings which is the proxy URL and we
want to make sure that the mappings are saved so
this is basically the setup how we tell viok.net
net that it should start um in code um that it
should start in proxy mode how do we do that
we have two arguments to our little application
proxy and then the URL so you can see if we start
it like this then we are proxying towards the pet
store um application that that you've seen with
seam one what then happens next is that that we
have two different outputs if it's not running in
proxy mode we say so and if it's running in proxy
mode it tells us um which URL it's proxying to and
then it basically waits until it is canceled by
someone so I can just hit control C or kill the
process or whatever and then um the application
stops now if we run that one you can see here
below the parameter so we do a net run proxy
pet store swagger IO so we expect it to run in
uh proxy mode and you also can see the output
down here it says running in proxy mode and
proxying requests so basically now when we make
the calls as you can see here talking to localhost
9995 where now wiremark is running and do a call
to the API for pet 999 as Simon has shown you it
will make the call to the real back end and
return the response still the same 999 with a
name of test and a status available so this is
basically what we expect but now viok is again
recording it to take a look at it I want to show
you vmok inspector which is a tool to interact
with viok.net you can find it at this URL and
install it simply using a net tool install and
then connect it to the relevant instance in
our case the local host port 1995 and if I do
the connection here I can now see yes indeed
it has gotten a request the pat 999 request i
can take a look at for example the path which
was API v3 pet 999 etc uh no query parameters
no headers no cookies um we can also take a look
at the mappings because we told it to save the
mappings basically we're in in recording mode
it also has that one which shows us okay what
is the definition the request the response etc it
has a tab for scenarios which we will take a look
at later at the moment we don't have any and a
nifty thing here is also that it shows all the
settings for example we see here that is running
and that is having the safe mappings and it has a
um a proxy URL set so this is very useful to make
sure you started this with the right settings and
because the documentation is um a bit lacking
in some places it's also a nice way to see which
settings are actually available that you might
be able and interested to use and as I mentioned
we want to use this to generate the code so I can
take a look at this request and then for example
say I'm interested in the method i'm interested
in the path i'm not interested in the request
headers or the cookies request body and the status
code is relevant the response headers I also don't
care about but the response body so now I have
basically um the code that I can just use and put
it in my C# application which is what we want to
do next um but we also want to make sure that we
have a bit of dynamic behavior in this one so what
I want to show you is again how we can randomize
the responses similar to what you've seen in the
JSON files but I also want to show you how you
can use parts of the request in the response and
how we can even add custom logic and custom code
into that one so let's put um the right code into
our little application that we have just created
so if we are not running in proxy mode then
we want to add um a mapping so this one will
react on the get call to the 999 request and it
will respond with a status code of 200 i'm also
adding in line 54 a specific header so we can also
immediately see that this is something that wire
has generated and then we have the actual body
in lines 65 to 62 where uh 56 to 62 where you
can see the the pet that we have retrieved so if
we now go ahead and run this why didn't this run
let me see by the way this is an amazing extension
called demo time that very often works perfectly
so um this is now basically starting our server
again you can see it's running in non-proxy mode
so this is now basically only working on the on
the calls that we have defined and if we then make
our get request you can see that it responds with
the 999 as expected so we're getting the mapping
that we have just defined in our code um you can
see here that the path currently is fixed but
maybe we want to make this a bit more flexible so
that we as Simon has shown you can just change the
ids but still get a valid response so what we can
instead do is that we don't use the hard-coded
path but we instead use a wildcard matcher so
that whenever something calls in that is a match
and you can see here that we basically accept
everything then we um will respond to it but
we have in our response also still hard-coded um
the ID and the name which obviously doesn't make
sense if we um make the the request dynamic then
also the response should become dynamic so here
we can do um an access to the request path and um
access the different segments so the first segment
would be API um v3 the second would be pet and the
third no first is API second is v3 um third is pet
and the fourth one which is addressed as three
of course um is the id so this is the way how we
can access parts of the request and use it in the
response so whatever we have requested now should
also be part of the response and to make that
work we also need to add this with transformer
call to make sure that those transformations
actually happen so if we um generate our
application again and let it run and make the call
to the back end and change the ID so for example
now we are requesting 429 we get a response and
there you can see in line 9 indeed the ID is 429
and the name is now pad 429 basically now we're
reacting in the response on the request to again
make it a bit more dynamic the next thing that is
statically defined is the status so we only have
status available whatever we call we will always
get available which is probably also not what you
want what I first thought and that was a bit of a
learning that I wanted to share with you is that
I could do something like this where I create a
function here get random status that just has the
the available um status available pending and sold
and then return a random one and then we use this
um function and reference it here in the status
so we just have a get random status let's run this
and then show you what happens because if I
now do the get request I get available and
if I do it again and again and again and again
and again I'm always getting available and the
reason for that is that wire goes through the
code initially and only calls the get random
status basically on initialization so if I run the
server again I might not get available but maybe
um sold or pending but it will for all
requests be the same and that most likely
isn't what we want to do so instead of having
a call here that is only executed once we also
um can use one of those um handlebar templates
those are called the dynamic handlers in um in
wireok.net where you can see that now we want to
randomize based on a string list where we have
those available values and if we now go ahead and
um create it again and do our get call once again
you can see now pending now available now sold
available pending sold etc so this is basic that
was always the same order no now it's different
it's getting a bit uh worried but um yeah it's
actually really random but for three it can
have some patterns of course um so this is the
right way if you want to randomize something like
this now we have two additional areas the photo
urls and the text and those are also statically in
this case mapped on empty arrays and wire doesn't
bring something that's suitable to um have random
results for that one so what I want to show you
is how you can bring in your custom code and then
properly reference it instead of doing the thing
that I did with the get random status um how to
how to do this properly for that we first need to
register a helper and give it a name so you can
see here the name of our new helper is a random
string array and then we have a piece of C# code
that um just gets random words with a minimum and
a maximum length and then splits them so that we
get an array of words basically the second example
is our URL helper so we also want to get URLs that
one is the random URL area helper um it also has a
minimum and a maximum length and it goes through
the URLs and generates the URLs you can see here
how that works i just have a list of domains of
image extensions and it generate a random name
put them together and that creates my random URL
you can see here I also didn't do a lot of work
in creating the data set but still this might
be enough to just generate random URLs what I
now need to do is that I need to um register them
so in startup I say that I have um a callback and
that callback registers those URL handler that
URL handler and that string array helper that
we've seen before how do we reference that now we
gave it a name random URL array and random string
array so we can just put them in and we had the
minimum and the maximum length as parameters so
that is that you can what you can also see here
so we have between zero and three photo URLs and
we have between zero and five tags that are
added now if you run our application again
and make our get call again
we should see random photo URLs
and random tags oh go back one step
and now you can see that's a different one
calling it again a different one calling
it again a different one so now we've basically
um randomized the responses again that's what I
wanted to show you for the dynamicity so you've
seen how we can use the request in the response
you have seen how we can do a bit of randomization
and you've also seen how you can bring in your own
code if the randomization the dynamic stuff that
is in wireok doesn't um fit your needs then you
can also provide your own code again we also
need stateful behavior for the pet store that
is very similar to um what we've seen in business
central with the customers so um it needs to be
created while it's not created we want to have
an error when it's created it can be modified it
can be deleted and the responses need to be the
right ones so that's that's basically the same
um state graph as before but how does it now
look like when we go into code mode here you
can see that we have the initial get and I use
the ID 1000 um for our special pet that we want
to create and while it's not there we will just
respond with a 404 because the pet doesn't exist
yet second step of course then is to create a new
pet um to make it a bit easier I have also created
uh record classes here so the pet has an ID a name
photo urls tags and a status as you've seen before
and then we can use this to just define our pet
so whenever um we get a new pet we call it fluffy
um and then we will mark it as tag because
of course there's some AI that figures out
that fluffy is very very cute but how does the
actual request look like now we accept a post
we again have a wild card mure on the um on the
pet URL and all we care about in the body is that
the name is fluffy so you can also see here
in line 101 the JSON partial matcher compared
to the full body that you've seen in the JSON
example this would be an example where you say I
don't care what anyone is sending all I care about
there is an element name and that has to be fluffy
so you also don't have to react on the full body
but you can only uh can also react on parts and
if that is the case then we will also move our
scenario ahead that is basically similar to what
you've seen before in this case we have a pet
crut scenario and will the sets will set the
state to fluffy created so we're moving our state
graph ahead and we will respond with fluffy now if
we want to get it afterwards you can see the get
request to pet 1000 and this one um only reacts
if fluffy has already been created and it stays in
the fluffy has been created state and it responds
with fluffy of course because that has what we
just generated then we add the update so in this
case um we are changing fluffy to sold because
someone bought fluffy uh the method now is put and
as a respon as a matcher we again only care about
the ID and the status so whenever someone sends
something in with the ID 1000 and the status sold
then we change that if someone would also send in
the name in this case we would ignore it so this
really depends on your um scenario and your case
again we are only reacting if fluffy has already
been created and we move ahead the state to fluffy
was sold and we return the slow sold fluffy next
step would then be to also respond to a get after
fluffy has been sold so again you see this is
only responding when fluffy has sold and stays
in that state and it returns the sold fluffy
last one is that we want to delete fluffy again
um this is happening both in the created and in
the sold state so we're doing a bit of a for each
here we accept the delete call we um take it
in the petrut scenario if it's either created
or sold and then we set the state to deleted um
and we only return the status code 200 which is
how the pet store works and the message of pet
deleted so basically this is um again moving our
our little pet through that state um through it
states graph if we now run this application again
and it has started then we can use um all those
those calls but what I first want to show you
is that via has that scenario inspector that I
mentioned before so if I now reload because we now
have defined scenarios in our code it recognizes
that there is a pet crut scenario and it basically
creates um the state graph so I can also see
when I create something in code it generates a
graphical representation for me so that I can
understand what happens and I can see which
um transitions are supported and uh through
which definitions where they are triggered
etc so this gives me a better idea after
creating the code whether I have actually
created the stateful scenario that I wanted to
create now let's give it a try um first try to
get a pet of course we haven't created
it yet so it responds with a not found
then create the pet fluffy it responds as
we expected we try to get it again now it
works because we have created it our state
graph has moved ahead we can update it again
the rest of the body basically doesn't matter
we only care about the ID and the status and now
the status has moved to sold if we take a look
into the wire inspector again it has the nifty
feature that it also shows us in which states
it already um has through and where we are now
so I can see it moved through created into sold
and I know um which transitions have happened
to show you I can also get the do the
get now I see the get with the status
sold i can delete it it responds
properly and if we now do the same
get call I had not found because we
have of course deleted it so again
um we have now a wire mock instance in place that
completely replaces that pet store and I'm not
no longer relying on it instead I can do that
state graph i can do the dynamic handling and
everything without without relying on pet store
so I can do my client development independently
so what have we seen we have seen how the
setup for recording works how we can record
the required steps and generate the code we've
seen some of the dynamics using the requests
and the custom handlers seen the partial body
matcher wire inspector is a nice tool and how
we can handle stateful scenarios in this setup now
I also want to show you how we can use that from
Business Central and now we're going to basically
use the Kyoto um generated client that Simon has
shown you and um I have extended the demo page a
bit for this because we are changing the status to
sold i also wanted to show that and I added some
actions to create update and delete because Simon
so far only had the get so what did I do that's
kind of standard AL code um I just added a status
enum i added the pet create action which does
a post call so as you can see this is now using
um the client pet post in line um 107 this
is yeah the nice handling that we get through
generating the client um via Kyota and then we
make sure that the um response is successful
set the status and show the output modification
works like this again we're using in line 131
um the client that has been generated we
use the indexer to access the right ID and
um get it so this one should basically show give
us the right the right pet and then in line 135 we
have the put call so we do now the modification
um after we change the status the delete action
also very simple we get the right pet using the
indexer and just call delete um and then show the
response but basically the API interaction
thanks to Kyod is just the one line in 157
um and I've promoted promoted all the actions so
that they are visible so now let's deploy this yay
what happened here
let me try to reload
there we go
trying to build
okay try to publish
let's see if that works of course I need to log in
okay so this is now basically our sample page
where we now have the pet status as well i
can request 999 i can request one two three and
you can see we get the the right responses with
the randomly generated URLs and the the randomly
generated text but I can also create something new
so if you remember I only was checking
for the name so if I just create fluffy
create I need to reset the scenarios because we
had moved through them let's try to create now
I get a new um a new fluffy with the status of
available of course I can again reset it and say
for 1,00 I want to change the status to sold so
this also works if I now do a get for that one it
has the status sold we can also delete it and once
we have deleted it the get should also return an
error that the pet has not been found so what I
mainly want to show you with that one is that once
we have the mock in place the code of the client
doesn't change it's basically the same as if you
would talk directly to the pet store which is the
whole point right so we have a mock we don't need
the real back end anymore but the coding the
whole experience is basically the same only
it's a lot faster and it's it's perfectly stable
let me see what did I want to show you of course
um automated testing so I not only want to show
you how you can use it during development but also
during test automation and maybe I can take it
from here so what I want to do is basically take a
test code unit um just the the basics and add some
test code for example we have the random get here
so in line 70 I'm just getting a random number
accessing it in line 18 and then I make sure
that I get a successful response and I also get um
the right ID that I that I requested so um this is
the randomization and this is the assertions in
the end if I now go ahead and publish that one
I'm in the test runner and I can run my random
get test and that one takes only 87 milliseconds
and it has validated the things that we that
we expected um then we also of course need to
test our CRUD application or our CRUD scenario so
let's take a look at how that would work and again
this is not particularly um special or specific
AL code just to show you again you would do the
exact same thing for wire mark it makes sense
to first reset the scenarios so that you don't
see the error that you've seen for me before but
in your automated test you always basically start
on a clean slate then we first try to get ID
1000 it's of course not there yet so it should
um be false then we create it with a new name
of fluffy and make sure that we have created
exactly that one we want to retrieve it afterwards
because now that we have created it it should get
the right response again we expect a successful
state the name the status and the ID should be
right then we can modify it by first changing
the status to sold and then doing the modify
call again we expect a successful um return
and make sure that the status has changed
we want to delete it again a very similar
call a very simple call that can only check
for success and if we afterwards check
it check it again we should see that
um it doesn't return a successful response
so let's try to run that one as well
and if I run that test you can also see 80
milliseconds um so again a very fast test
this is exactly how we want it we no longer rely
on the pet store but instead we have our mock in
place and have very reliable and fast responses
again the code in Business Central is exactly
the same as it would be if you talk to a different
system which is again kind of the point of all of
this so with that um you have seen how the test
automation part works um but only the basics of
it so we basically now use the mock pet store from
business central you have seen how we implemented
those action on the test page again exactly as if
we would have talked to the real system and how we
have implemented the automated testing for those
um CRUD actions how would you deploy this now so
if you think about trying this at home how would
you run this um during development it's easy you
can just run via mock natively on your laptop on
your VM or whatever or in a container and the code
would be my recommendation to store it alongside
your application so that whenever your client
changes or the mock mocked back end changes you
have those things in um in sync and the versioning
is consistent during automated testing if you use
Cosmo Alpaka this is very easy there is a concept
of a companion um container so you have your
development container and a companion container
and that companion can just be um can just be via
mock so to just briefly show you you would define
the companion here and say this is the image that
I want to use this is the URL that I want to use
and then um whenever you create a new development
environment you automatically would also get a new
Vomok environment that you can use also wireok has
a paid offering that you can use for that or if
you prefer to use whatever container back end you
might have for example an Azure container instance
Kubernetes service that also would be easy this
one liner spread across multiple lines um would be
the one to create an an Azure container instance
container so this is really something that you
can easily put into your pipelines if needed a
few closing remarks um Simon talked about the
open API specification and of course um that was
something that would totally make sense to just
use the open API specification throw it at Vomok
and get a fully um generated mock i looked at it
for viok and there it's included in the paid
offering so I didn't want to show this today
um but not in the free offering basically
yesterday afternoon I realized that viog.net
actually can do this in the free version so
that's certainly something I will investigate and
um probably share on my blog as well something
I didn't show you for the sake of time and as
we only have five minutes left it was good that
I didn't try is that you can also induce faults
and delays so you can also say something like
on a randomization scale every third request um
should return an error or I want this particular
request to take um something between 1 second and
10 seconds so you have a more realistic response
time if you do something like load testing or
something like that and then of course this is not
the only way how to mock um probably you're aware
that there's a new feature in AL and I think
there's even a session um that covers it that
you can use to mock your backends and I would say
that is extremely helpful and makes a ton of sense
if you're mostly working in AL if you also have
other frontends if you also other systems that
you want to mock where you're not only living
in AL then I think Vimok is something that's
absolutely worth looking at um and can solve a
lot of your headaches that you might have around
third party integrations that's it with that we
would be very open for questions thanks a lot
questions i guess the light indicates a question
uh I want to ask about Kiota um does
it also when it generates the client
uh does it also handle the negative responses
like I don't know under 500 whatever you you
just generate the client to talk with the
API the API will uh you mean like handling
I mean the client the client itself when it gets
like 500 does it throw error or just ignores or
should you handle it by itself um right now the
the error handling is not very extensive i only
check if it's a success status code and return
the response uh if it was successful if not
um right now that uh right now we need to add
some additional handling for that so that you
it won't throw an error so it won't be a runtime
error but you won't get a response if there's
an error right now that's why you had those get
successful state or what is called so after the
call you need to make sure that it actually was
successful right okay and does it also work if I
would have body as XML or it's not supported
i mean in the XML instead of JSON yeah yeah
uh as long as it's in Open API specification
yeah it would also work so because OKI also
supports XML and does this AL part support
i mean this uh right now the one you showed
uh right right now it only supports uh the the you
mean the access in the model code units right it
supports only JSON right now okay because it's the
more common selection the open AI specification
can be in XML or JSON so if you have an open AI
open API specification in XML that would work but
if the actual payload is XML that won't work no
actually open API supports payload and XML Yeah
but not not yet in the AI client right yeah
that's great thank you you're welcome oh that
means other questions one shirt for you anyone
interested in topics or shirts maybe over there
yeah sorry didn't catch it because well first
timer here um my question here is how easy is
it to share the wire mark like for instance if we
have like the wire mark for the business central
and we have a third party client that's trying
to integrate itself into the business central
would be to share some sort of environ with them
if well I guess they do know how to use it yeah I
think you basically have two options the first
would be that you share the code so either the
JSON files or the C# code in my example and give
it to them and show them how they can set it up
for themselves second option would be that you
generate a container image using your wire and
then they could just spin up a container with
that um with that image and it would have wire
as you have defined it and the third option
would be that you just spin up a server on your
site and let them know here's how you can reach
the server so depending on what level of access
you might want to give them I think those those
would be the three options i see i see thank you
same problem that I had any other
questions over there that's too far
thanks um uh can you mock also the authentication
issues with uh yes there is an integration for or
off 2 if I remember correctly i stayed away for it
from for it for the for the demo and also because
in implementations I could so far always exclude
it but yes I think it can mock O2 if I remember
correctly thank you other oh and um basic
authentication would just be a header and you
react on the right one that's trivial but we don't
do basic anymore right um yeah further questions
on the left on the left on the left
ah here thank you is there a way to use the
Kyoto client um if I don't have an open API
specification so um I was handling a lot of APIs
that uh yeah don't have a swagger light site where
I could yeah have the comfort of seeing all the
functions i I think I saw some tooling that can
help you generate the open API specification but
you can Kyodia only accepts this it can be in YAML
or JSON so it doesn't need to be JSON but it needs
to be in the uh API okay so I would first generate
the specification myself if it's not provided uh
by the provider and then I think for some default
patterns you there are like converters but I
didn't I didn't test them myself okay thank
you oh sorry other questions and I think we don't
have shirts anymore no no more shirts so only if
you're really interested in the question but
no shirts well that was too far thanks a lot
yeah um hi um you have shown a clean uh flow of
create and retrieve and delete a pet but in a real
um case um does the does the automation support
mocking those relationships um as well or would
that still require manual uh setup in one mock
or test code units how do you mean relations
um you have uh the pet in that case was uh dog
uh how do you can um com um how how can can you
uh relation a pet with a new customer or when
when you make a a call with a get and you Yeah
I I I think I I got it now so that again would
be um a scenario where basically you create the
customer you create the pet and then you assign
the pet to the customer that would just be an
API call and Viomok would know would have to
know about that and then the state would move
into something like pet connected to customer
and then you can could ask um which pets are
assigned to the customer and it would return
that one so it's not wire in a sense doesn't
have any idea of entities or something like this
it's just URLs and how it reacts so I think you
should be able to model something like this yeah
oh okay okay nice yeah thank you further questions
doesn't look like it and we are also at the
end um and the only thing between you and
the lunch break is us so thanks a lot uh thanks
for coming please give us feedback thanks please
