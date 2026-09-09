# Microsoft Presents: Prompt engineering and functional calling in AL

- **Source:** https://www.youtube.com/watch?v=2OSvZNhzFnA
- **Video ID:** 2OSvZNhzFnA
- **Channel:** mibuso.com
- **Published:** 2024-06-16
- **Duration:** 46m27s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome everyone to our session on
prompt engineering and function calling
I'm Derek and with me cim all right
let's get started so for the agenda of
today we'll go through a demo that we
built for this session uh what we call
the order co-pilot then we'll talk about
function calling Custom will talk about
the prompt engineering side of it and
then we'll get into some
Q&A all right so let's show the
demo all right so four cases we're going
to show
here and now we're going to run the
order copilot the first case we're going
to get the status of an order so we
selected from The Prompt guide putting
in a order
number and now generating that now we've
gotten an order now we'll open it to
actually just double check hey that's
actually what we wanted and it is and
it's also released so now let's close
that and look at another case
and this is from the same co-pilot so
now I'm removing that and then I'm going
to ask it to create a sales quote I want
two bicycles four tires and for the
customer the Canon
group so let's let it finish right
thing yep and then let's generate
that and now we can see it creates a
sales quote so let's open it and double
check all right it's for the Canon group
and it has two bicycles and four tires
just as we
expected now let's look at another case
say we've received an email from a
customer we don't want to par it
ourselves so we just dump it in and
generate let's see how the L model will
work and now if we open the
quote we'll see that it got us similar
except it's for the office desk and
office chair will show you the email
and go into details afterwards and for
the last case we're going to show you
what happens when we perform an
unsupported case so in this case I'm
trying to create a warehouse shipment
which we have not built support
for and you can see we've just thrown an
error stating that hey what you're
trying to do is unsupported so these are
things that you can do with function
calling all right let's get back to the
deck and yeah so function calling so
I'll kind of go into the what is this
why you should use it I'll go through
some very basic example use cases and
then how you can build it with an
Al so what is function calling so it
allows developers to augment the
capabilities of flash language models by
en enabling it to call functions or apis
and just based on the users input and I
got that from
co-pilot so what this also means is that
with the model you can it can be
enhanced to interact with the system
business Central an external system it
can access upto-date information by
retrieving it from external sources or
perform actions Beyond just generating
text so why would you want to use this
so you can enhance the interactivity
where your users can now interact with
your system in natural language the the
model will then be able to call the
appropriate functions as we had seen in
the demo earlier and this makes the
system a little more user
friendly it can also give adaptive
responses so for example as I had
mentioned it can provide up toate
information by retrieving it from the
system or externally and also get the
relevant information and all this is
based on the user's query
so some example use cases you could use
it for all right in the wrong order um
data retrieval so for example your user
wants some specific type of documents
and from the last couple of days so they
could kind of just say hey I want the
last um five sales orders from two days
ago and function calling can then be
used to determine hey what are the
required filters I should put in and
then you can use that to retrieve the
appropriate data that they actually
want and what if you had a customer
support co-pilot for example so the
customer needs assistance with getting
say order the status um they want to
initiate some returns or have some
inquiries you can build one C to do all
of that what so function calling will
allow you to then U be used to fetch the
all the status it can be also be used to
initiate returns and then answer those
queries in generative text
so I'm going to give a very basic
example if you've played with the edge
open AI or open AI U function calling
before you would have seen this example
uh back then so I have two functions the
first one get weather it takes in a
location parameter and this location
parameter is just string text and then I
have a magic function and my magic
function basically is a encapsulation of
it's going to my catch all of everything
I don't support custom talk into great
detail about that
later and what you see on the right side
uh is the function prompt and for this
one is the get weather
function so now I'm going to go through
two examples here so for example tell me
the weather of anope my expectation is
that it's going to tell me to call to
get weather function and it's going to
tell me that the parameter it should
have is
n and secondly I'm going to ask it hey
tell me about the solar system there
isn't really any weather that it should
be telling me to call so my expectation
is that it's going to tell me to call
the magic function and then I can handle
that in whichever way I prefer because I
know what the user has intended is not
supported by my
co-pilot so now all the following code
and stuff I'll be showing is from the
demo that project will also be shared
with all of you um through our GitHub uh
which I'll get into details at the end
of the
presentation so now I have this function
it's called the get order status
function and when you want to implement
your function calling there's an
interface the aoi function and it needs
three um three functions that you need
to implement there's the get name get
prompt and execute so I'll go into
detail for all three of them for this
function so with a get name you want to
return the name
that you have determined within your
function
prompt so what it looks like is here so
there's the function prompt and the name
that you have put in there is the exact
name that you want to return
here next up for the get prompt so this
is prompt that we had just seen that you
want to written and you can see that I'm
getting it from isolated storage we
always recommend you to keep this secure
as your prompts whether it's your system
prompt your your function prompts all
this are your IP so as such in this case
I'm getting it from isolated storage as
it's just an extension if you have an
appsource app you can use key Vault but
the main thing is that you want to keep
your prompts
cure so I'm getting
it oh yes that's the same thing um I'm
just checking that hey I actually have
my prompt start otherwise I'm just going
to read it in and I'm going to return
this object such that when the um the
large l which model is called it knows
hey I have this
function now one of the most important
ones is the execute function the execute
function will automatically be called
and this is the meat of your
function so the arguments parameter
basically will contain all the
arguments I'm sorry it's not all the
arguments it's the ones that you've
defined that are required and
potentially the optional
ones so in this case I know that I I
have not meant dated the order number so
I'm now checking hey does the order
number actually exist in my
arguments if it doesn't I'm going to
throw an error so I'm going to uh
validate that take it out next is that I
want to check that maybe the large
language mod screwed up in some way and
it's given me an empty string for order
number and clearly I know I cannot have
an order number with no uh that is empty
so I'm also going to going to handle
that so always validate the input you're
getting from the
model and then I'm going to validate
that after to see if that that order
actually exists within uh the
system and I'm then I'm going to have my
return um to
the the call and in this case you can
return anything as it's a variant you
can return a record you can return tax
you can return a code unit the options
are unlimited it's up to you how you
want to use
this so now let's we've defined that
function and assuming we also Define our
other functions how do we put this
together to actually make the call to
Ure open
ey so there's always the setup you've
set your capability you set the
authorization and then here's the meat
of it where you want to add your tools
so I've added the three tools create Sal
quote
uh get order function and my magic
function and one of the things that you
want to look at is the last line which
is set two choice so there are two parts
to this as you can see I've set it to
Auto and that is also the default if you
don't set it ever it will be Auto and on
the other side is you can set a specific
uh function so when you set a spe when
you set a specific function it will the
model will always call that function
irregardless of what the user query is
so for example if I requested the order
status for 100 it will call it correctly
it will tell me hey go check for the
order status order number 100 however
now if I ask it to tell me hey tell me
about the weather in Anor it may end up
putting Anor as the parameter but that
is also not what I want so and as as
such that's so why we have multip
functions for example with the magic
function to handle things that are not
developed and with also there it will be
able to call any of the functions
provided however the key thing that you
need to remember is that not only will
it call any of the functions it can also
generate free text and at that point you
want to validate that you're actually
doing a function call if that is what
you expect or if you also expect
potentially generative text
then you handle it in the manner that
you need
to and yeah so then I set my system
message I add my user query and then I
call
generate and from there I can check
firstly it's like okay was my call to
edure opening I successful I am missing
a line here where you can check if it is
a function
call and then you retrieve the um the
function uh response and from there you
can check if the function response was
actually um successful so the reason we
can do this is that when the model calls
it will then automatically call your
function that it was defined and was uh
returned by the LM so that's why the
execute function was important is
because that fun that execute function
will automatically be called for you and
you can just retrieve your result uh
from the get
results and additionally sometimes you
might want add context to your functions
so here's a very simple example so I've
added a variable called all the type uh
a global variable to that function uh to
that Cod unit sorry um and then I have a
Setter for
that yeah so I have set and where I'm
using it is in the check order
exis so then the get that's where I'm
Now setting that to ensure like hey for
this specific type this one exists and
where would I call this
setor so in the start order the co-pilot
function where I've added my functions
and as long as just before your
generation you add or you set the type
that you want or set any context that
you want and when the execute function
is called the same instance will have
that information
yeah all right so let's take a overview
from here so in this case now I'm asking
hey what's the order status of this now
it sends to the uh compile to Kit you do
all your
setup and that has the function
included and from there
you we'll call the Azure openi
service and now that will return what
function it should be calling and the
parameter
arguments yeah so that's returned and
then within the tokit you will find the
few functions or it will find a few
functions that you've defined and it
could call and it will choose the
correct one that was
defined and in this case is to get all
the states and it will call the execute
function yep and from there it will then
uh return back up so that the toet
already knows what the response is and
then you can or the return is and then
you can take the response out and then
see that hey the result is actually this
is supposed to be a sales orderer and
this is
the uh the order
number and then from there you can show
it to the user or call the Ed when I
service again some of you might remember
this slide from Dimitri's uh present
presentation yesterday and I hope you
guys were there because it was really
great all right I will hand it over to
kasim to talk a lot more about prompt
engineering thank you Derek so I will be
talking about prompt Engineering in the
context of the co-pilot that was
presented
earlier I will try to go through like
how you write the prompt for such a
copilot application what are the
different components that come together
and of course we will be talking about
about functions since our copilot is
heavily dependent on functions as
well so before I go further I want to
quickly recap uh what we have shown in
the demo so our co-pilot could do either
it can create the
sales uh yeah either it could create the
sales code or it could get this order
status or it could do any every anything
else everything else is basically to
capture what is not supported and this
is also a capability uh itself and I
will go uh a bit more into details uh
what this function is all about I think
there's a mismatch with these slides
over here and over here now I
guess um they are
same so now let's look into the prompt
component what are different components
that come together to build such a
copilot the very first first thing that
we have is the system prompt which
basically gives the context to the
co-pilot what this AI system is all
about and then you can give bunch of
instructions to it the second part is
the function which
basically tells the model what are the
capabilities that your AI system
supports and what is the communication
structure with the llm model what are
the exact response and what are the
exact arguments that you expect as a
response and lastly we have the user
prompt which is basically what the user
inputs so now let's look what the system
prompt looks like the first thing that
we need to Define is the context which
basically is to give the AI
system uh some context what this AI
system is all about and in this
particular demo we are saying this AI
system is this design to inter
interpretate emails or natural language
as input and extract information to call
an appropriate
function then the second part we have
inside our system prompt is called
safety instructions as part of
responsible Microsoft responsible AI we
put a lot of effort to make sure
whatever the content that is generated
from the AI is safe and we are not
presenting anything which is harmful so
you do that there are a lot of things
that you can do one of the things that
we do inside the prompt is adding safety
instructions for this particular demo we
have this particular instructions that
if the user prompt have something
harmful content such as threat or
illegal activities you must call Magic
function and this magic function is
basically which captures everything else
I will be going a bit more into it uh
later on as
well the third uh section of the system
prompt is the task instruction which
basically uh in which a section you can
explain what this uh copilot is
basically all about what are the
capabilities and at how you want to call
uh each cap capability on what kind of
user input for the very first one if the
user asks for an item that they want to
purchase we call create sales code
function try to uh we within the same uh
instruction I'm also putting some
emphasis to make sure the name and the
features are splitted for example if you
are searching for Blue
Bicycle uh you want the blue to be a
feature and bicycle as the name of the
item so that you can apply filters or
search differently based on different
things and I will show some example
later on as
well our second uh instruction is about
get order status so if the user input is
about uh getting the status of the order
uh we call this particular function and
lastly if anything which is not
supported or anything which is
categorize as harmful we call Magic
function so this is the entire system
prompt that we have for our co-pilot the
important thing over here to notice like
there is no instructions about what
would be the
response uh what would be the exact
response from the copar what would be
the uh structure and what exactly uh the
information that needs to be extracted
from the user prompt that is where the
functions come into the play before I
show you uh the function prompt few tips
about writing system
prompt Pro uh you should provide very
clear and simple instruction wide
complexity the longer your prompt is the
more tokens you will use and it will be
more costly for each llm call that is
made since uh to is our currency when we
are talking to
llm try to use State forward language to
guide the model through the
process you can always ask the copilot
to improve on your prompt like once you
have a similar system prompt you can
always ask copilot to refine it to make
it in simple language or you can ask
guidance uh for from co-pilot to improve
your prompt as
well and lastly
no oops yeah yes uh lastly to put some
emphasis on a particular uh instruction
you can always provide practical
examples for example in our very first
uh uh instruction about create sales
code we are talking about splitting the
name and the uh features and this is a
problem when I was writing the uh prompt
I like the splitting was not done as
expected with the model so I put some
emphasis by giving an example saying if
the user input is I need two red bicycle
you should call uh create sales code
function with bicycle as the name and
red as the
feature and you can always bold uh any
part of the prompt as well or put uh
Stars around it to make put a bit more
emphasis on anything that you feel that
the copilot is not not reacting as as
expected so now uh let's look into how
the prompts are basically
defined the very first prompt that D
already showed was the get order status
the few things that we need to Define is
the name and the description description
is optional uh but you can uh Define
over here and to add some more clarity
for the model but what we have
experienced as soon as you have more
complex uh instructions uh it better
Works to put those instructions in the
system prompt rather than the
description I mean I know so you've
noticed that it's undocumented yeah but
in the description that is a maximum
length that you can have which we have
found out it's about
1,024 exactly and as soon as we have
like multiple functions and complex
instructions the description our
experience with adding instructions in
description doesn't work that well
that's why you have seen that I've added
instruction when to call which functions
inside the system
prompt and the next thing which is very
important is to define the parameters
that needs to be returned as part of
this
function these properties will be used
as an argument when the model decides to
call this particular function for
example when get order status is called
the model will make sure to extract
order number from the user input and try
to pass that as an
argument to this function and then you
can react inside the execute function
that was shown earlier in the AL side uh
you can uh use this uh order number to
do your for the
processing let's look into the second
function which is the create sales code
similarly uh we have the name and the
description over here I'm not giving any
description like I mentioned I've
already specified when to call this
function inside the system prompt
and then I'm giving bunch of
parameters uh Properties or you can call
uh I have the customer name company name
and if I go further I also have the list
of all the items uh array that needs to
be extracted uh whatever the user has
defined I'm using an array over here and
each particular item the information
that I'm interested in is the name
quantity and bunch of other thing
including features for example and you
can always give the the type for each
properties and also give some
description uh to each uh property but
again it's optional uh it's up to you
what works best for
you and lastly what is very important
over here is you can also Define what is
required for you when this particular
function is called for example when
create sales called function is called
uh we the information that we absolutely
need is the company name and some item
because to create a sales code we need
to Define some uh customer and we need
to at least add one line so what I'm
doing over here is making sure okay I
need the company name I need the item
array and within the item array at least
I need the item name if the quantity is
not there I could always default to one
but the item name is something I'm
making sure to let the model know that
uh you need to extract from the user
prompt so now let's look at one of the
examples that was also part of the demo
uh categorized as user prom so imagine
you receive an email uh from a
customer let's try to go through this
email in the very first section the
customer is telling about few items that
he has previously
purchased uh in this case black office
chair and conference table and now he's
asking for few other items that he want
to purchase which is the office test
office chair and you can see the office
chair that he is now willing to buy is
actually blue but previously he bought a
black office chair llm will be smart
enough to identify which were the items
that the user is willing to buy and
which are the items that the user is
only referring
to lastly you can see uh the customer
and the company informations is either
in the email or in the footer llm again
is smart enough to extract all the
information from this particular
email so now let's say you receive this
email you can copy paste inside this uh
prompt dialogue uh since this is a demo
so we use like copy pasting of the email
inside this uh prompt dialogue but you
can always build an extension to read
the email directly from your uh inbox as
well so once you copy paste the email
inside the prompt and press generate
without giving any other information
information the llm will be smart enough
to identify First uh I need to call the
functions and then it will uh correctly
identify like I need to call create
sales code function just by giving this
uh protocal email as a user input the
only thing that we have previously given
uh llm to the uh the system prompt and
the list of
functions and when the llm will call
this function it will try to extract all
the arguments as well now if I go to the
next slide to see all the list of
the all the list of the arguments uh you
can see I have the customer name I have
the company name and the customer email
that was extracted from different places
from the email and then I also have the
item array for all the
uh uh items that the user was willing to
buy you can also see like the office
that was extracted was actually blue and
all the other features that uh that was
explained in the natural language uh
that were also extracted from this uh so
this was the the reason that I add the
instruction inside the system prompt
because I wanted to treat the item names
separately than the features because the
features let let's say comfortable you
have an office chair but nothing in your
system says comfortable so I need to
make sure okay uh which features are
optional which terms are optional and
which are mandatory so that's why I I
added that instructions in the system
prompt to do the
splitting so now let's look at the very
third function that we talked about
which is called the magic
function similarly uh regarding like the
other functions we have the name and the
description similar like uh call this
when the user Cy is not about items or
status and then we we also have a
property called intent which is string
which will basically give uh try to
extract the intent of the user uh when
this particular function is
called let's look into few
examples so when the user say I want to
create a warehouse shipment the the
magic function will be called and we are
throwing this particular
error what if the user enter something
which could be categorized as harmful
is there an item I can use to harm
someone the model will be smart enough
since we have the instruction the system
prompt it will call uh the magic
function and we will throw the same
error if you look at the responses from
the Aur open AI for both of these cases
uh for the very first when I want to
create a uh Warehouse shipment the magic
function was called with the intent
Warehouse shipment for the second one
for the harmful content the magic
function again was called with the
intent harmful content but right now for
both of these different scenarios uh we
are basically showing the same error how
can we categorize the unsupported with
the harmful content how can you extend
your magic function to make sure that
you are showing maybe a different error
or M uh doing something different based
on what kind of uh uh intent was there
so how you can do that you can extend
your magic function the intent part of
the property and add an enum with all
the possible categories that you can
think of right now I'm giving two
categories which is either it is
categorized as harmful content or not
supported uh
content now when you do the same input
uh within our uh as a user input I want
to create a warehouse shipment it is
categorized as not supported intent and
now you can show an error which
basically says okay this uh is not
supported in case of harmful you can ask
to rephrase or do some other uh nice
messaging uh to the
user few key key points about magic
function using the magic function you
can control the unexpected because since
the input is free text so you are never
in control control what the user can
enter using the magic function you can
basically control okay you are
redirecting everything which is not
supported to a particular function and
uh basically handling it that and you
are also basically setting a boundaries
to your AI features basically what is
supported and what is not supported and
lastly you are mitigating risk and
ensuring safety by redirecting
everything to a magic function one thing
that we have experienced
uh very well using magic functions
regarding safety is like the model works
best if you redirect any harmful content
to a particular function or uh the
alternative would be to say okay if
there's something harmful don't respond
the llm most most in cases responds uh
with something so to mitigate risk and
safety and if you're using functions it
works perfectly like uh when we do our
red teaming redirect everything to Magic
function functions and it works pretty
well so something for inspiration like
uh the future of function calling what's
uh down the uh pipeline for function
calling uh so this is something already
part of azure openi and it will be part
of our SDK in the future as well it is
called parallel function calling I will
try to explain this through an example
for example you have two functions
defined in your prompt one is the get
weather uh crun weather function the
other is search FAL you you have to find
these two uh functions inside your
prompt and now when the user input is
what's the weather like in San Francisco
and New York also suggest hotel in these
cities the llm will call the get weather
function twice for both of these
cities and it will also call the search
hortal for both of these cities now with
just one llm call there were four calls
made uh for getting the weather two for
the weather and two for the search uh
hotel and yeah in the future that will
also be part of the SDK and then you can
uh uh make some uh use of this as well
so yeah uh that was all about the prompt
engineering section um let's just do a
very quick re cap of uh kind of what
we've just talked about so for function
calling main points to kind of take away
is that it augments the capabilities of
an
llm the functions are triggered
automatically for you so you can just
get the result
immediately and you can add additional
contexts to the functions um whether
you're using it for one co-pilot or
another you can generalize some of them
regarding the prompt engineering like I
mentioned be concise and specific in
your instruction start simple and see if
it already works and if not then try to
add more complexity to your system
prompt and function does simplify your
system prompt because now we are not
adding any extra instruction in the
system a prompt regarding the response
and the communication is also always
structured so you do not have to uh
handle any of the structure like the
response should be Json or these are the
arguments in this particular format if
you define a function the model will
make sure uh it works as
expected and everything is on GitHub so
the AI module is part of the system
application and can be found at the BC
apps repository and for the demo that we
had showed you all this code the prompts
and whatnot we will be putting it up on
BCT Tech we have not unfortunately but
either later in the afternoon or Monday
we will have it there for you and let's
get to some Q&A if anyone okay de
question yeah so uh regarding the magic
function and kind of those unexpected
inputs obviously that user input as eron
and uh Augustine point out that's their
data but from an extension developers
perspective it might be interesting to
know like okay what's going on that's
leading into this path so is it clear
like what could we log to Telemetry
probably not the user input but what
about the intent of what the user is
putting in can we log any of that to
find out what users are trying to do
with our
co-pilots um what we can store inside
the I guess uh do you have answer to
that I was say I was going to think that
the enum would be fine I mean not the
query of course but the
enum
[Laughter]
eron yeah okay there you go um so this
has been a very big question for us like
obviously we want to know with all of
our AI features what kind of questions
are you asking what kind of responses
are you getting but the thing that the
user types in and the response that they
get back is obviously all customer data
right because you could write in there
like write a sales invoice to my
customer with all of these things and
you know that's your business
information you could even type your own
name in there and at that point that's
also personal data so at the moment we
actually don't collect any of this
information it's very hard for us to see
how the product is being used because
there's all of these privacy
implications to us collecting all of
this data and so I mean the Telemetry
you log as your own problem right like
we make sure that we are following all
of our internal compliance guidelines
that we don't log all these things to
Telemetry and um but as far as I
understand it all the partner Telemetry
is stored in your own like partner
subscription and so then you know you
have your own guidelines as to how you
handle that data right um we're working
on Solutions internally for us to be
able to uh store all of this information
and so that we can actually gain these
insights but it's going to involve users
consent into providing this data and
obviously you'll be able to opt out
we're only going to collect it if if you
actually like give us permission to
collect this to improve the service the
if of any of this data would be customer
content oh yeah anything that they type
into the product and anything that comes
back from co-pilot it's all customer
content yeah at least from our
perspective just to add to that like at
least you can record element like which
function was called I guess that's
already part of the S as well or you can
tell okay either the magic function is
called or the create sales order
function is called yeah so we do
actually start to track things like that
right so we will classify the requests
like for example for co-pilot chat like
a looking for information or you're
looking for data but we don't know what
information you're looking for or what
data you're looking for right yeah I
guess question that was a question
here so actually the first question I
wanted to ask the same about the
Telemetry because it's really
interesting to understand what's going
on there and why you receive any any
response from the chat but yeah that's
clear so another question is uh is it
possible to find some ver some bench of
examples uh of the prompts written by
the Microsoft like to handle the
standard already written functions by
Microsoft so as I had mentioned earlier
prompts and system prompts function
prompts basic prompts in general are
considered IP so we have ours and you
have yours and as such that's why we
don't for example with sales line
suggestions marketing text none of those
prompts are available um however for
what we have built for this demo is
specifically to be given out to you guys
for the same things we have done for
hours but just for this co-pilot so this
is I think this might be the only
example that we have okay thank
you there over there
yeah hi um I want to ask how we can can
grant uh good performance if you have a
customers with
150,000 items
Etc um so you can definitely not pass
those as part of the prompt so once you
extract that information uh you uh I
guess what was earlier shown in one of
the demitry session was either you can
use embedding and use those thing or you
can use your own searching to find those
uh items uh uh but yeah uh currently if
you cannot basically pass that kind of
information to llm so you have to rely
on some searching based on the keywords
that you extract from
that yes hello um everything that we
have seen so far as regards to the
system prompts and the the function
descriptions they're all in English but
most of our users would be writing input
in different languages any comments on
that thoughts on what to add or is the
model at least our experience that even
if the user's input is in another
language it still works fine okay you do
have to kind of tell the model that for
example with marketing text is that hey
reply in the users language if you're
looking for generative text of yes um if
it's calling a function then it doesn't
really matter
for the most case what language it
returns because it's going to bejon and
some parameters that you're going to
parse yeah Okay add to that you can
write your prompt in any other language
as well and if like uh direct mention
for marketing text our prompt is in
English but our uh user input could be
in any language and the uh LM will
respond in that language in fact it also
worked with Emojis if you uh enter and
all the different things that you can
input uh you will be amazed how the LM
would be able to respond in either of
the languages that you may input okay
thank
you this one
there I'll come to you
after
yeah uh so when using Asia open AI am I
using the vanilla CH GPT or am I using a
custom version that has more business
Central context or so there is the the
models are not fine tuned and it's just
what you have deployed so whether it's
GPT 35 turbo GPT 40 gbd4 turbo it's your
deployment that youve deploy within the
AI studio um where you've gotten it yeah
okay thank you
y uh so youve also shown on one of your
slides that you have already defined
what content is not allowed usually open
ey already has a pretty strong filter on
it um my question is I have imagine a
scenario that for example we have a
customer who is in the chemical industry
and maybe we write a function for him
where he can query how he can for
example make a weed killer what does he
have and what um kind of material he
needs to do with this normally this
would already be not allowed by op I
standards is is the implementation for
business Central less restricted than
the normal open AI or is it equally or
more restricted so if you use it with
our system prom it would be more
restrictive yes so the reason why we
have a default system promp for you is
in case you don't provide any safety on
your own that we provide you a layer of
safety already and but that can be maybe
too restrictive depending on industry
and what you're querying for so
sometimes you might want to have your
own safety in that
sense so um didn't like um um so if I
don't make any like prompt for um what
is the IL legal content it would then
just go would it then go with the
standard from open I or would it just
say no filters at all
but there are some filters that aure
openi automatically provides so even if
you have no instructions about the risk
uh for some of the industries uh chances
are the model will not respond okay but
it will be less likely if you like for
chemical industry we have to experiment
but when we did our testing even without
any instruction some things are stopped
by Azure openi by default as well so the
chances are it will be stopped depending
on the
content yeah it's something you just
have to play around and figure that
out there you go thank you that's the
last question thank you uh hello um the
presentation was very good very
interesting so compliments to both of
you thank you um I wanted to ask is it
possible for um a tech saavy uh user to
kind of like bypass the system prompt by
brainwash ing the model uh like
basically telling it to ignore the
system prompt or does the model
prioritize the system prompt and then
the user prompt so you're talking about
jailbreaks yeah the prompts yes um So
within our default prompt or any of our
features especially we do have to with
the responsible Ai and red teaming we do
have to do tests on that and there is a
certain level that we have to hit um to
prevent that and so there may still be
ways that it comes through we can't stop
everything or we do
try so
it's dependent I would say but it can
happen okay thank
you all right I guess thank you uh if
you guys have more questions you can
always uh reach out afterwards as well
thank you everyone
