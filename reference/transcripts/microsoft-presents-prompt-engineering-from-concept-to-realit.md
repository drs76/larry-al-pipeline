# Microsoft Presents: Prompt Engineering: From Concept to Reality – Challenges and Insights

- **Source:** https://www.youtube.com/watch?v=xSHsa0Xu0FM
- **Video ID:** xSHsa0Xu0FM
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 92m14s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, please welcome
Kasim and Derek for the Microsoft
presents prompt engineering from concept
to reality, challenges and insights.
Hi everyone.
Uh welcome to our session.
Uh we have a packed agenda, so I hope
that
we'll be able to cover everything.
So, we have actually split this into two
parts. The first part being concept to
reality, and the second part being the
advanced prompt engineering and our
challenges that we've faced.
But one quick thing I want to let you
all know, I'm sure you guys will have a
lot of questions. So, if you guys have
questions, you can easily just go on to
the mobile app and then go to our
session and add your questions there.
It'll make it a lot easier for us when
we get to the Q&A at the end.
So, let's get started.
So, in part one, I mean, we're going to
tell you all about what a prompt is,
how you can actually go about
engineering your prompt, how you can
actually build safety directly into your
prompt, and I'll go a little under the
hood of what we have done to build our
own Microsoft capabilities.
So, I want to start off for prompts with
what are roles. So, there are three
different roles. There's the system
role, user role, and the assistant role.
So, what is the system role? So, take an
example like this. You are a helpful AI
assistant, respond concisely and
politely. So, some of you may have heard
of system prompt, meta prompt. They are
the same. They are interchangeable.
They're basically the prompt that you
use to control the large language model
to do what you'd like it to do.
Then you have the user role. Now, the
user role is, let's say, Kasim. He's
using the Copilot. And now he's asking
question, "How Explain how Transformers
work in deep learning?" Now, that's the
question it's being asked to me, say the
Copilot.
And when I respond, it comes out as the
assistant role.
Now, that will
be something like this. And how you
actually show this within Business
Central in AL code is a little like
this. I know it's actually very small,
but it's add system message, add user
message. And when the Copilot actually
responds, automatically it adds the
system message. So, you actually don't
have to do it yourself.
So, we're going to start off with a
concept. So, our concept is that we have
a company called Contoso.
We receive hundreds of purchase requests
through email every day.
Now, that's a lot of emails for us to go
through.
And but one thing we've noticed is that
all our emails that we receive typically
only has one intent. And what do I mean
by that?
An intent is basically they want to
purchase something from us. They want to
ask, "Hey, how's my order? Like, when am
I going to get the delivery?" And other
questions similar like this.
So, a lot of times it is a manual
process for us to kind of identify what
the intent is, then after that process
the email, and actually reply.
Now, I'll hand it over to Kasim to talk
about how we are actually going to build
from this concept.
Yeah. Thanks, Derek.
So, now we know the concept of the
Copilot that we will be building as part
of this presentation.
So, I would like to go
go through from scratch how you
basically write a prompt for such an
application.
Before we even go to any of the AL, you
need to validate that your use case can
be solved through LLM. So, that's the
number one thing that you need to do
before you do any of the AL part. So,
that's what we will start focusing
to start with and then we will go to
some of the more advanced prompting
techniques later on in the session.
The tool that I will be using is the
Azure AI Foundry. It's a very uh
a lot of there are a lot of features
within this
Azure AI Foundry that can help you to
write prompts and evaluate and all those
things. Uh but what I will be using is
the uh chat playground to write a prompt
for such an application.
So, let's start. So, I'm going to start
with a very basic two instructions
uh because we are just getting started
to build this co-pilot. So, what I'm
saying is like you are an AI system
which intercepts or interprets an
incoming email which could be in natural
language
and try to get the intent from from the
user
and try to extract uh the
uh
useful information from that input.
And the two actions that we want to
support is the creation of a sales code
and or basically getting the status of
an existing
sales order.
So, within my Azure AI Foundry, I paste
my system prompt inside this
window and then now we have a user
prompt which says, "I need to buy
uh two red bicycles, two helmets for two
year old in blue color." So, this is a
normal uh
request from the user
that we receive.
Now, when this particular prompt is uh
executed, the response from the LLM is
the action which is in natural language
but is like the right one which is the
intent was to create a new sales code.
We have a bunch of other information
that was extracted from the user along
with a lot of extra information that was
also extracted or outputted from the
model. This is not something we can work
against in AL because we need a bit more
structure
response.
The action is also something which is in
natural language. So you cannot
basically do some action on this
particular natural language. So you need
to be a bit more specific what the LLM
needs to respond. So let's try to
iterate our system instruction. So I
will try to add two more instructions
within our system prompt. The number
The first one is basically the first
intent. So I'm basically
telling
uh
if the user inquire about purchasing an
item, you need to
call the action create sales code and
extract the customer name and all the
other relevant information.
The second intent is basically if the
user ask about an existing order, the
intent needs to be get order status and
you need to extract the order number out
of it.
And very quickly to add in like what is
this create sales quote, get order
status? You can think of them like AL
functions that we want to call.
So now let's try to run the same example
again and now the action name is a bit
more predictable.
The same keyword so now you can
basically do some action based on this
particular keyword when you get a
response. But still there's a lot of
this extra information inside the
response that you actually get. And we
need
to remove all the all of those
information and try to get the entire
response in a more structured way.
So now what will add another set of
instructions where I'm saying like the
response needs to be in a JSON format
for both the intent and all the
information that will be extracted.
So running the same example again, now
we have a nice JSON formatted response.
So this is something we could work
inside AL and make uh
decision based on this response.
And one thing that you can see
uh
the problem over here is like it was
able to extract the features for the
helmet,
uh but not for the red bicycle. So, it
was not able to basically split the name
and the feature
out of the user request. So, basically
our AL logic could be like we want to
treat the name of the item differently
than the features. So, we need a better
instructions to make sure the model is
basically splitting these in the in the
right format.
So, what we can do, we could basically
give another sub instruction for the
first intent
to split the name and the features, and
then we also try to give a very simple
instructions. Any information such as
the specification or the detail of the
item should be categorized as the uh
features of the item, and then the name
of the item needs to be splitted with
the feature.
Running the same prompt again, we can
see the the name and the feature were
correctly splitted, but now still we
have another issue now, which is
the feature is not an array, it's a
key-value pair. Again, something which
is not predictable. We need to make sure
that everything comes in a exact same
format, so that we could work against
that.
So, let's see how what we can do over
here.
So, now what I'm doing is basically
adding another section inside my system
prompt, which is called the example
response format, and I'm being very
specific for intent create sales code,
you need to return the intent,
the items, and the feature needs to be
an array.
Uh So, now the model will make sure the
response is basically in the same
format. So, now I know all the features
will be in a in an array.
So, if we uh similarly for the get order
status, I'm saying I need to extract the
intent and the order number. I'm not uh
expecting anything else out from the
user prompt for the this use case.
Running the same example again, now we
see the feature is basically an array
uh for both bicycles and the helmet. So,
everything looks good.
Let's try to uh we have we have just
tested our prompt with just one example.
So, let's try to do another example. And
now I'm basically asking about four
wooden chairs and one office desk.
So, it was able to split the chairs and
the features correctly.
And but not for the office table. You
can see uh while working with the
prompt, you might be working with a
limited set of inputs. It might work for
that, but when you go out into the world
and people try to enter a lot of
different things. So, it might work and
it it might not work. So, this is the
issue I see right now. The splitting of
the name and the keyword uh or uh the
name and the feature is not working as
expected. Although, we already added a a
specific instruction how to split the uh
name and the feature. How we can put
even more emphasis to this particular uh
part of the instructions.
So, we already had this instruction. We
were already asking to split the name
and the feature. Now, we are even giving
an example. So, this
basically tells the model how exactly
you need to basically split the name and
the table. We you can give more examples
as well based on how
uh the model is reacting to a lot of
different uh requests. But, this shows
you how important it is to test your
prompt against a wide range of inputs.
So, now running the same example again,
the you can see the chair and the office
uh
What's the example? The table and the
office are basically splitted in the
right format.
Similarly, for the order status,
uh, it works it's a simpler uh,
scenario. The intent and the order
number was extracted correctly from the
user input.
So, looks good so far.
Before we go further, few tips up till
now all right while we were writing this
prompt. You can always ask Copilot to
basically enhance your prompt and you
should use the capabilities of this
model to basically suggest how the
instructions needs to be formulated and
uh, basically refine.
And you should always be concise and
specific inside your instructions. We
have seen uh, moving uh, between models
and
uh, different models.
Uh, if you are not concise, if you are a
bit vague, it might work for your
current model, but as soon as you move
to a newer model or different model, it
might not not work.
And you should always start simple. The
example that I showed, I only added the
instructions to split it the name and
the feature only when I needed it. We
get a lot of capabilities from the model
out of the box. If the model is working
as expected, you might not even need to
add uh, these instructions. And that's
also the case when you are moving to a
newer model, you might need to refine
your prompt and exclude uh, a lot of
things that you previously added in
inside your prompt and it might work as
it is. So, you can even optimize your
prompt when you're moving to a newer
model.
And adding practical examples basically
help a lot. So,
no matter how you formulate your
instructions, sometimes the model do not
react as uh, intended. So, adding
examples basically helps a lot goes a
long way uh, to make sure your uh,
Copilot work as expected.
So,
a quick recap regarding our system
prompt. We have this big uh,
uh, meta instruction which is telling
what our AI system is all about. We have
set of instructions starting with the
first intent which was the create sales
code. Then we have the instructions
which is the about the get order status.
And in the end we have the instructions
about how the response needs to be in
JSON.
And lastly, we also have a section where
we are giving the example for format in
JSON. You can see in this instructions
and also the example, we are putting a
lot of emphasis what needs to be the
response.
How exactly the response needs to be,
what are the exact keywords that needs
to be extracted. This does complicate
our system prompt a lot.
So this is where I want to introduce
another concept which is the function
calling.
Function calling out of the box
basically enables you to have a
structured communication with the model.
And
you just by setting the
functions, you let the model know these
are the capabilities that my co-pilot
supports and what are the arguments for
this particular capability.
Response are formatted in JSON by
default so you do not have to basically
specify anything inside the system
prompt.
And it's very ideal for the the
type of co-pilot that we are just
building and a lot of use cases. I think
it's a default that you should always
use function call.
So this was our system prompt without
function calling.
Just by introducing function calling,
our system prompt is just reduced to
this set of instructions. You can see
now I have only two set of instructions
where in the first one I'm saying when
the intent is to purchase an item, you
need to call create sales code. I still
have this extra instruction to split the
name and the feature to make sure it
work as expected. Secondly, uh for the
second intent, I'm seeing uh if the
intent is to get uh the status of an
existing order, uh you need to call get
order status. You can see and uh I'm not
now specifying anywhere what exactly the
parameters that needs to be extracted
from the user input. That is where the
function definition itself comes.
So, now we have the system prompt.
And let's look at our first function,
which is the get order status. How you
define a function? It's basically you
define a function in a JSON format. So,
you have the name and some description
about the uh function.
And then you also have the parameters.
Whenever this function will be called,
uh the order number will be uh extracted
from the user input.
Similarly, for the create uh uh sales
code, we have the name. The description
is optional. Uh but the now the model
knows we have this capability for the
create sales code. And then we have
bunch of uh parameters that we need to
extract from the user input, which
includes the customer name, uh company
name. And we are also specifying that we
need an items in an array. Again, the
features are also in an array, quantity
and all those things. So, we can
basically define the entire response
format uh within this function
definition.
Lastly, we can also put some emphasis
where while defining this function, what
are the fields that are mandatory. So,
whenever this function will be called,
the model will make sure there's at
least some customer information and the
item name. So, that uh that's the bare
minimum so that we could basically
create a sales code uh for this uh
particular request.
So, now let's look for the same example
that we did the previous demo against is
the the bicycle and the helmet.
Now, the response from the
uh model is basically a tools calls of
type function.
Uh
the model was smart enough based on this
request to identify the
uh the intent was create sales code and
then there's an argument object that
basically uh have all the parameters
that we have defined in the function
definition. So, we have the customer
name, we have the customer email, items
in the the format that we have defined
uh the features in the right format and
everything. So, now we have made our
system more robust. So, we know exactly
whenever this particular intent will be
called, this is the structure that we
will be responded back and then we could
basically process this inside AL.
So, these are the three different
components that we have just discussed
now. We have the system prompt, we have
the function prompt, and then we have
the user prompt.
Uh a quick look how it looks like in the
AL is pretty simple. Uh you specify
tools.
Uh over here I'm giving three tools, the
uh create sales code, uh the order
status, and the magic function tool. I
will come to the magic function shortly.
And then we are giving the system prompt
and the user prompt. So, it's like very
simple inside AL.
Uh so, the Azure AI Foundry doesn't work
uh that well with functions. So, the
tool that we usually use internally is
Insomnia. I will just give you a very
quick demo.
How it looks like inside Insomnia.
So, you can see on the top we have I
have a deployment of my model. And on
the left is the input uh JSON and on the
right is the output. So, right now I do
not have any system prompt. Uh
so, my system prompt is basically empty.
And then I I defined a function which is
the get weather status. So, the model
was smart enough just by definition of
the function itself, what are the
capabilities that my co-pilot supports.
And the parameters that I want to
extract is basically the location.
So, now when the user input is like,
"What is the weather in Antwerp?" and I
press send,
the response will always be a tool calls
with an a function type, and the name is
uh get current weather, and the location
is Antwerp. You can see how simplified
our prompt looks like with using
functions.
Uh
just by defining the function itself, it
gives a lot of information to the model
how the communication looks like with
the model. And it basically uh you get a
lot of things out of the box.
Let's go back to the slides.
There's also one more thing that I just
want to introduce a feature within Azure
AI Foundry, which is the generate
prompt. So, right now what we did so far
was to write the
prompt from scratch.
But, there's also something that you can
use that is a bit more uh
you can basically have a very quick
start to experiment your use case. So,
what I did is using this generate
prompt. The first two instructions that
we actually wrote, the very first thing
that we did, I actually just gave those
instructions to this generate prompt and
tried to generate a prompt for my
co-pilot.
And what it did, it basically created a
detailed instructions.
It had all the key actions that needed
to be taken.
It have all the steps defined,
including what the output format needs
to be, and it also added some examples.
So, you can see just by giving two set
of sentences, I was able to generate a
complete end-to-end prompt out of it.
So, it's a very quick way if you want to
validate your use case if that thing is
could be solved
uh using
any of the models that you are intending
to use.
So, now
I didn't did anything the same prompt
that was generated. I copy-pasted a
slightly complex email.
We do not have to go through the entire
email, but the the gist of the
email is like the customer is saying I
bought multiple items from you which
were good. Now, I need to buy a few
other items.
The model was smart enough to
differentiate between the items that the
user was only discussing that he
previously bought and the items that he
wants to buy now. And if you look at the
response of it, the the response only
considered the items that were basically
the user basically needs to buy now and
it identify the right intent. So, you
you can see without writing any just two
sentences I was able to basically
generate the entire prompt and it works
pretty
fine even for a slightly more complex
input.
So, now back to Derek to talk a bit
about safety, how we make sure safety
inside our co-pilots.
Thanks Qasim for showing us how you go
from a start concept to actually having
a whole prompt. And now we want to talk
a little bit about safety.
So,
the cost of failure is the lack of
trust. So, whenever you build a co-pilot
capability
and the co-pilot now responds with
something that maybe it's harmful, for
example.
That is not a good sign on your company
or if you're a partner building a
co-pilot for another company, it's not
good for them either. So, it's going to
affect the technology, the brand, the
solution, and ultimately you.
I'm sure you have all seen some of these
headlines. They are a little old, but
they do hit the mark of
it's not good when these things happen.
And that's why I want to emphasize that
takes safety very seriously.
Um it's what also Peter at the keynote
had mentioned. We do accuracy testing.
We do harms testing to ensure we meet a
certain bar before we ever put things
out.
Um
yeah, exactly that.
And now I'll hand it back to custom to
show you how we integrate safety into
our prompts.
So yeah, within Microsoft we have a lot
of things that we do to make sure that
our co-pilot is safe.
One of the things that we use is through
uh definition inside uh some
instructions inside the prompt itself.
So this was a uh system prompt that we
previously had. So now what I have done,
I have basically added another section,
these safety instructions. What it says,
like if the user input includes any
harmful content such as threat or any
illegal activities, you need to call
magic function.
So now we have introduced another
function and
a- as you most of you might already
know, the nature of the model is to
always respond. So if I would have said
something like if there's some harmful
content, do not respond, the chances are
the model would respond with something.
So it's better to always redirect
anything that is harmful to a particular
uh intent or our function in this case,
uh we use magic function so that you
could properly handle that inside AL. So
something you can say, okay, this is
something not supported uh and then you
can throw some error based on this. So
this is how we make sure uh this is a
very simple instruction that we are
showing. We have a lot more complex
instructions that we give, but the uh
the important point over here is
for all of these things, we are
redirecting the model to call the magic
function in that case.
And I also add another instructions like
magic function could also be used for
the things that you are not supported by
your co-pilot. Not only just the harmful
content, but the things that our
co-pilot does not support. You can again
call the magic function and properly
handle that and throw an error for the
end user.
So,
let's look at the definition of the
magic functions. Like all the other
functions, we have the name magic
function and some description. So, if
the user request is about not about the
purchasing an item or
uh checking an order status, we call the
magic function. And then the parameter
that we are extracting is the intent.
So, that this could be used for
telemetry, so that you know what are the
different ways unsupported ways the user
are basically using your system.
So, let's look at a few examples. So,
let's for the first example is like not
harmful. I want to create a warehouse
shipment, something our co-pilot do not
support. The magic function is called
with
warehouse shipment as the intent.
Similarly, the second request is is
there an item I can use to harm someone.
So, this is a supported intent. We are
in a business of selling items, but
since it was categorized as harmful
because we do not want to suggest
anything which is harmful, the model was
smart enough to redirect this request to
magic function as well, and the intent
was harmful content.
So, magic function is very powerful tool
that we use across a lot of co-pilot and
agent features that we build
to basically control the unexpected
behaviors. It also sets some boundaries
to whatever your co-pilot feature is
supported, and you can basically handle
all the things which are not supported
in a more uh
natural way.
And it does mitigate any risk and ensure
safety. So, the only thing you need to
provide, okay, these are the two things
that I support. Anything else is
categorized and need to be redirected to
magic function, and you don't have to
care about how the end user might try to
exploit your system.
So now, let's try to look a bit under
the hood how we use these concepts in
some of the co-pilot that we have built
in-house.
Yeah. So, the first example I'm going to
go through, I'm sure most, if not all of
you, have actually tried marketing text,
but maybe you wonder how does it
actually run under the hood.
So, as you guys know, you can take in
some style and effects, basically the
attributes.
And now, we actually take that in, we
merge it with our prompts, and we give
that to the LLM. Simple enough, right? I
mean, that should be all.
But, that's actually not all we do.
We need to keep it safe. So, our prompts
do incorporate safety, however, that is
not enough.
Now, we have a function, basically a
validate answer function. It's kind of
what we do to kind of ground the LLM's
answer to what is actually in your
system.
Now, let's take for example, we have a
table, and it has the height, the
weight, and oh, length, and width. And
let's say the length is 100 cm.
Now, we will actually take that value
and see, hey, in the generation, were
there any other numbers?
Is there a match for this number, say
100?
If there isn't, we check or against all
the other facts that we have, and if
that doesn't match, we know this is a
hallucination. That is hallucinated some
number out of somewhere that we don't
know.
And that is one way that we do kind of
the grounding for marketing text.
And from there, we we try to do it five
times, try to generate an answer for
you, but we really can't,
we call magic function and say, "Sorry,
we just cannot give you an answer." So,
we'll then respond back if we have
something, otherwise, it's either we
have validated and tried five times, we
can't, return, say, "Sorry." Or we had
actually called magic function from the
first call.
Now, another one I want to go through is
the sales line suggestions.
So, it's slightly different. Now, you
have your input.
And this input can be just text that you
wanted to, hey, I need some lines for
something from, say, a document or some
items.
So, we give it to the LLM to extract
these keywords, this intent of what the
user actually wants.
And from that intent that we have
extracted, we decide, all right, hey,
what does the user really want to do?
Item search, document search, or it's
something that's unrelated, and we call
magic function and say, "Hey, this is
not a supported intent, we cannot do
this."
And once we have that uh document item
search done, we pass it on to go and do
a little more item entity search before
we come back with some kind of response.
Because through this, we are still
incorporating safety. And how do we do
that? Because we're actually validating
what you wanted actually exists within
the database.
Because if it doesn't exist in the
database, we should not be responding
with you something that the LLM has
hallucinated.
Now, another way you can use the sales
line suggestions, if you have played
with it, is through attachments.
So, through a CSV, we will extract out
all the columns,
and using those columns, we'll then ask
the LLM, "Hey, which is the columns with
the data that is relevant for this
co-pilot.
And from there, it extracts the product
and information
and takes that information to then
forward it to the same uh
bottom section that we can see that we
extract the actual intent that wants to
run before giving you an actual answer.
So, some key takeaways with writing
prompt engineering.
Always be precise, concise, and precise
in your instructions.
The start simple before you add
complexity.
Like what Custom had mentioned, using
Azure AI Foundry is a good start, but
you will always want to refine it to
make it as concise as possible. Adding
more instructions doesn't mean the model
is going to adhere better to those
instructions. Sometimes it makes it
worse. That is where testing really
comes
uh into play.
And functions can really simplify your
prompts and make your systems better.
And safety, it can help reduce the
unintended consequences. So, if you have
intents that are not uh
something that it's handled by your
system,
use a the magic function, for example,
to help you handle that and push it
away. Because then you can give back
that generic answer. And also, you if
you were to say log like in telemetry,
say the intent that the person wanted,
you can always use that to refine your
co-pilot going forward.
And now we actually move on to part two
and how you can configure your AI models
used for optimal output. Um I'll put
some more definitions and a few more
techniques for prompt engineering. And
we'll also cover the common challenges
um in enterprise use. Things that we
have faced building our co-pilots and
also the agents and some things that
we've heard from you before.
So, let's get started on that.
I'll move over I'll move over here.
Um
So, these are
the topics that I'll cover.
But, let's ignore what's on this slide
and just go straight into it.
So, with model configuration
well, the model configuration really
transforms what a general purpose LLM. I
mean, there are many LLMs out there,
right? I mean, you have the ones from
OpenAI, you have the ones from Google,
so on and so forth.
So, they're all like general purpose.
But, then you can transform them using
your prompts to unlock the precision
that you need and creativity
and the efficiency for your co-pilot
capability.
So, the first one, the first parameter I
want to talk about is the temperature.
It allows you to control the randomness
of a model's output. And
now you might wonder, what do I mean by
randomness?
So, here I have an image. I think it's a
pretty nice image from zero to one.
Actually, I'm sorry. It's not one.
It's actually zero to two.
One is the default value for temperature
and that varies from model to model.
Now, on the left side
the zero side. So, the outputs are more
deterministic.
Um we
when it's set at zero, it's never
exactly deterministic. If you put in A
and you expect A back out it may not
always give you A. It might give you A
now, it might give you B later. So, it's
not always deterministic.
So, some things that we actually use it
for. So, take it for example,
comparison.
Um the features like bank
reconciliation, for example.
Now, we've taken the data, the lines,
and we've taken
the other side and we want to compare
these two and this is when we really use
temperature zero because we know, hey,
don't we don't want it to hallucinate.
We want it to ground it in the data that
we provided.
Another example is using for data
extraction. So, for example of
extracting out the intents,
we wanted to extract the intents, but we
don't want it to just hallucinate some
random intents that the user had
not actually keyed into say the email.
And more on the other side of the higher
temperature
is when outputs become a little more
creative.
Now, one of the examples is creative
writing, which marketing text does. It
has a higher temperature.
If I remember correctly, the temperature
we actually use is .7. So, it's nowhere
close to two
or even at one,
but that
I would say playing with .7 is a good
start. If you get all the way to two,
things that it generates may not be
coherent at all times.
So, it's something that you really need
to play around.
You can also use it to say generate
ideas because now it's a little more
random. It's going to select things that
it doesn't always select.
So, very simple of how you actually use
this in AL is that in the chat
completions parameters, you would just
set the temperature.
The default, if I remember correctly, is
one in the system. Um, but you can
always play around with that.
The next one is max tokens.
So, max tokens actually define the upper
bound of the number of tokens that the
system can actually generate.
So, what does that look like?
Um, so, I wanted to throw in another
term real quick, which is the context
window.
I'm sure many of you might have heard of
the context window before. For example,
with GPT-4o, the context window is about
128,000.
Now, this is the both Oh, this is both
the input and output tokens.
And when I talk about max tokens, this
is specifically about the output tokens
only.
Most models nowadays have a maximum
output limit of 32,000.
And this includes GPT-4. Like, if we go
back to say GPT-4, I think we've had
16,000 and then it grew up to like
32,000.
So, it really depends on the model.
Yeah. Um
and then when you set a lower limit, I'm
going to take a very simple example
here. If I ask the model, "Hey, tell me
what are the primary colors?"
It's probably going to tell me red,
green, and yellow.
Oh, red, green, and blue. Sorry.
The
when I limit it, I say, "I only want one
token to be output." Now, it's going to
say maybe just red, and it's not going
to generate anything else
from then on.
So, outputs can get truncated.
And if you were to use a reasoning
model, say O3 mini or 1 mini,
now those reasoning tokens that it
actually generates as it's thinking,
it is also counted against the maximum
number of tokens that's generated.
So, that's a key thing to keep in mind.
And how you would actually just put this
in AL is setting the max tokens in the
parameters.
This one I don't exactly remember what
the default is.
Frequency penalty.
So, there is also the frequency penalty
that you can play around with, and it
really helps you control the repetition
and help you improve like clarity or
even encourage more natural and diverse
responses.
And what do I mean by that is really it
the more it uses a certain word, it will
stop.
Sorry, not stop, but gradually stop
using that word.
So, if you have a whole prompt of maybe
even say 10,000 words,
a word that you may have used very
frequently in there, it's not going to
probably not going to use it at when
it's trying to output any tokens at all.
There's another very similar one,
presence penalty.
So, I'm not even going to talk about
this
text here, but
what it really does is the moment it
sees the word,
the future generation has a has a hard
penalty, and it will not use that word
going on forward. So, the first use
initial initial initializes basically a
harsh penalty on what's and future
generations will not include or very
unlikely to include that word.
So, just to split them up to see the
differences, right? So, on the left side
is the
frequency, and on the right side is the
presence.
So, for frequency, it is triggered based
on how often a word is used, while
presence is based on whether a word is
used, basically the first use.
So, the penalty increases with each
additional use of a word for frequency,
and for presence, as I have mentioned,
upon usage of the word.
So, that's what frequency really does is
that it reduces an overuse,
while presence just encourages new use
of new words immediately.
So, short message here.
You use them to encourage diversity,
reduce repetition, for example, like
creative writing, summaries, or
brainstorming.
However, I would recommend you to just
leave them at zero if you especially if
you have temperature zero.
Why? Because
sometimes when you have temperature
zero, you want a very concrete answer
that may be coming from the initial
text. And if you use these, it may stop
generating some of those words that
actually appeared in your grounding.
And that is why I would recommend using
a zero if you have temperature zero, but
if you are doing something more
creative, you can play around with this.
Very similarly of how you would put them
in AL is same in the chat completion
parameters to just set the frequency and
the penalty. The defaults for these are
at zero by default, and they go from
zero to two.
So, just a short recap of all of them.
Temperature controls the randomness. Max
token limits how much can be generated.
Frequency gradually reduces the chance
of a word being reused. And presence
reduces the chance of a word being
reused.
So, next I want to cover some prompting
techniques.
So, better prompts will result in
smarter results. And mastering how to do
prompting will help you unlock the full
potential of language models.
One one that we have actually already
covered, but we never put a formal name
to it. So, it's kind of the zero-one or
even few-shot prompting technique. And
this helps you unlock the adaptability
of LLMs such that you can tackle new
task, task that you may want to solve.
And you don't need to train you don't
need to fine-tune a model. Just use the
generic model and use this technique.
And what is this?
So, we had already seen it earlier where
Kasem gave it the example of hey, I want
to split this uh item name and the
features, right? So, this is one is what
we call zero-shot prompting. We've not
given it any example on how to do this.
We're just relying on the model's
pre-training to determine
what it should do with this information.
With one-shot,
very similar to what Custom had already
shown, is that we gave it an example of
I need two kids bicycles, and then split
the kid and bicycle up.
Few shot, simple enough, just more
examples, not complicated.
But why is this
uh like important to know?
So, here's a chart from a table
actually, um from one of the tables by
Google
about the Gemini models and comparing it
against GPT-4.
And here they actually do the tests with
different prompting strategies, for
example, using five shot, which means
just means five examples,
to chain of thought at eight, and chain
of thought at eight really just means
they're using the chain of thought
part of the model with eight examples
given to it.
And we can actually see GPT-4
the results that it got, that's it
doesn't really change too much.
Now, I don't know what the test really
is,
but
it does make a difference depending on
the model, depending on the task that
you're actually performing on.
As we can see with Gemini Pro, it got an
8% bump.
Now, depending on your task, whether
it's complex or simple, it can
help tremendously
if you had more examples, if it was a
more complex task.
Cuz the more examples it can see,
the more likely it's it
more likely for it to understand what
you really want as the answer.
And for the ultra, it also went up.
So, a short table here to help you is
that
depending on your task complexity and
how much time you actually want to spend
to kind of come up with these examples
is what what you would go with.
I would say you can always try with zero
examples first.
See if you get the results that you
want. Test to see if you get the
accuracy you're looking for.
If you don't,
give it that example.
If it's still not good enough, give it a
few examples to then determine.
The next one I want to talk about is
reason and act. So, we have actually
seen this already when I spoke a little
bit under the hood about the sales line
suggestions,
uh, as that one, yeah.
So, this really allows
a model,
uh, large language model to not only
think through the prompt,
but also to act.
And because it can act using external
tools, calling functions, now it can
able to kind of in a way reason over and
be more accurate in what the final
output is going to be for your Copilot.
I'll take come back to this example of
the sales line suggestions because I
think it's a good one where
at the top, as I had previously shown,
it you give it a attachment, and from
there it takes that
the columns and then extracts that
information out, um, to determine, hey,
what is in this
table on this attachment that you've
given it.
And from there you pass it on to the
next LLM to then determine, ah, okay,
now I got this information.
What is
what can be done here?
And
it's
so, it's taking the first part to reason
over it, and then it's acting,
and then reasoning over it again, and
then acting to determine, all right,
this is what they want,
whether I can do it or I cannot do it.
So, some things to think about for when
you want to kind of do this.
You use this to answer questions that
require possibly multi-step reasoning.
So, you need to call multiple functions,
maybe get multiple results from various
places before you can combine it all
into one.
Um yeah, get it and then if you need to
verify some results, possibly from
another tool that
uh returned something.
You can also use it to make more
data-driven choices because now you can
actually use the tools
to get that information and
make decisions upon that. Not just to
give it one time to answer the question.
So, you can then use your tools, which
is like web web searches, calculations,
or even accessing PC database in real
time.
And lastly is that with that new
information that you can pull in, that
real-time information, now it can adapt
what it's actually doing.
Without that, it always has old stale
data.
Next one, we've actually talked about
this as well, structured output. But now
you kind of know the
name and what it can really do. Um so,
it really ensures that the LLM delivers
consistent, machine-readable
uh results,
enhancing reliability and streamlining
integration into the systems.
So, structured output, the
um
magic function that Custom had talked
about earlier
is func- function calling is a subset of
structured output.
It's basically getting an output that is
in a certain format and it's guaranteed
to be in that format.
So, one
Yeah.
So, structured output ensures the
predictable format, in this case JSON,
and it's typically always JSON. That is
what the LLMs have been trained with,
and it's really good in working with
JSONs.
It enables easy parsing and consumption,
especially downstream APIs, whether it
is a BC
function or if you were calling out any
anywhere else.
It can also enforce structure and help
you prevent errors, for example,
malformed function calls or invalid data
views. So, we had seen this example by
Custom earlier, where one of the very
first times he was trying to tell the
model what to do. This is before using
function calling.
We tell it, "Hey, we want you to run
certain action based on certain intent."
But this output is now going to possibly
change every time we call
the model.
And that's not what you want.
Yeah.
Okay.
So, how do you use structured output
with a BC? You had kind of seen the add
tool, the second one already. But the
first one is also an option, the set
JSON mode.
So, what you really need to do for that
one is one is to set JSON mode to true,
but within your prompt,
you just need to use the word JSON as
well.
If it doesn't use the word JSON, it will
actually throw an error. And not because
we want to throw an error, but because
the model
um the platform will throw an error.
Just to let you know.
So, something that maybe you guys have
seen before, I mean, I've mentioned
about the reasoning tokens, is chain of
thought.
So, chain of thought can help a LLM
transform from guessing to reasoning, so
helping you increase your accuracy,
transparency, and even trust in the
model.
I I a diagram here.
So, given say some prompt,
we have we start at the bottom now the
blue dot.
So, given that prompt, we the model
starts thinking.
It starts thinking, okay, first what
does this person what is the prompt
asking for?
What do they want from here? And then it
starts reasoning over, all right, I know
they want this.
This is probably the result. And then
let me just double check my work before
I give back a final result.
And that's really what chain of thought
is doing because it is a So, models are
also regressive model they're auto
regressive basically means
they take everything they've
given and generated before before they
generate the next token.
So, as it generates things, it's also
using that to think
uh going forward.
Um
So, how can you actually incorporate
chain of thought?
So, there are two ways. I mean that
whether you're using a non-reasoning
model or you're actually using a
reasoning model doesn't really matter.
With non-reasoning models, you can
actually provoke it to
reason just by adding thing
step-by-step.
So, one example I want to show that
maybe you guys don't know
and even for us it was quite a bit of
trial and error
is you can use chain of thought
in a function.
So,
this is not the best example.
I'll loop through that.
But, take for example here where I have
something called detail reason.
I want it to give me a thorough
step-by-step reasoning
of why this user request is for example,
irrelevant. Why should it not
um be why should this magic function be
run and not the other function?
So, this will actually run through and
give a step-by-step reason in there
before it actually generates the intent.
So, it's possible that it reasons over
what it thought it should do and then
determines that, "Hey, this is actually
not correct. This is actually a valid
intent that the customer wants it." And
it actually fulfills um or actually the
other function can't fulfill what the
user has wanted.
And then this intent reason will
actually change.
So, this is actually something we use
for our agents.
Uh
yes. So, chain-of-thought helps guide
the model through problems uh with
structured logical steps.
It can help you increase transparency
because you can see the reasoning um
behind it before it actually gives you
the output. Now, this doesn't work for
the OpenAI models because they just do
not generate or they just do not give
you back the They do generate the
tokens, but they do not give you those
reasoning tokens.
If you play around with say DeepSeek or
Gemini, you would have be able to see
what these reasoning tokens look like.
This enables models to reason over their
own steps and possibly even fix errors
along the way.
Uh
and
uh yes. So, just a short recap on all of
this. So, few-shot
it's uh prompting basically adapts new
task with no additional training.
React uh reason and act allows it to
think and act, use tools, fetch data,
and then get you better results.
Chain-of-thought goes from guessing to
reasoning, so allows for clearer and
even smarter results.
And then structured output makes it
consistent, reliable, and
integration-ready uh responses.
Now, I'll hand it over to Kasim to talk
about challenge we have faced
and you may have or may face in the
future.
Thanks, Derek. Uh, so yeah, we'll
probably start with some of the
challenges that we face when we were
building our co-pilots and agents. And
then we will probably open up the floor
for Q&A so that you could guys could
also share some of the challenges you
faced and we could have a discussion on
that.
To start with, grounding the model in
your ERP world. So, as we all know,
these models are trained by the entirety
of the internet. It knows about ERP and
it knows about Business Central in
general, but it does not know about how
your environment is set up.
So, you have to make sure that the model
is basically grounded
with your configuration or your
environment.
One of the examples that we see a lot is
like we use a lot of these opaque IDs
within our items, for example. We have
item called like item 2023 FG EU. So,
this doesn't help the model to know what
this item is all about. You need to give
this extra context about what's the
friendly name or the description and all
the other information about this
particular what this particular item
basically means.
Similarly, in retail, everyone knows
what SKU is. It's a common term that is
used quite
uh,
in all the ERP world.
Which is basically to uniquely identify
specific variation of an item.
But we, within Business Central, use it
slightly differently.
For us, it's not just the unique item
or
unique item, which is the item number or
the variant code, but it's also the
location that particular item is. So, we
have this extra location code, which is
very specific to Business Central. So,
if you do not provide this extra
information and you are building your
co-pilot, so the
the co-pilot the model will be confused
or might not respond as expected because
the knowledge that it has is only based
that the SKU is basically used to
uniquely identify an item, not with the
location.
Similarly, we use when you are providing
a lot of data to the models,
you should avoid using coded field like,
for example, document type three.
We all know what document type three is,
but we cannot assume that the model
knows about it as well. So, we need to
spell it out for the model that the
document type three is basically a
credit memo. So, you need to give some
kind of a mapping for all the coding
data that are you sharing with the model
to react on.
And one other thing, for all the fields
that you are sharing, you it always
helps to give all the captions
along with the fields to better
to let the model better understand what
these captions are all about and the
units and all the business rules that
you have.
Few examples that I want to share with
you, like we recently rename jobs to
project, and we still use these two
terms interchangeably.
So, if you are building a co-pilot on
top of jobs or project, you need to
specify or let the model know these
means the same inside Business Central
context.
Inside Business Central, we use the
vendor vendor term, but we do not have
anything which is called supplier. But
someone who is coming from the outside
or from the other ERP system might try
to communicate with your co-pilot using
the keyword supplier. So, when you are
building or some information inside your
prompt regarding vendor, you need to
also specify what this vendor actually
means so that the model can make more
educated guess if someone is reference
referencing supplier in in place of
vendors.
Let's see or let's look at the real
world example. Let's say you are
building a co-pilot which is built on
top of customer data and all the
transaction that are made inside the
system.
Uh normal user query will be to
summarize
uh last quarter top five customer.
But, when you are providing this data to
the model, if you exclude all the
transaction
were made in this particular local
currency or which currency
the transaction was made on,
the chances are the model will basically
respond incorrectly because it do not
have this extra context of all the uh
transaction that were made in which
currency that uh they were made.
So, if we look how we can uh emphasize
that inside the prompt itself, so I I
have this simple prompt for
uh demonstrating this particular
example. So, you can see I'm passing the
customer data uh later on in my prompt,
but I'm specifying the sales are the
sales amount, and then I'm also uh
providing another field which is the
currency. So, telling that the sales
amount is basically in this particular
currency. So, now when I'm showing
multiple transactions or sales that have
been made, I'm giving the currency as
well, and I'm also giving the sales
amount. So, now the model will be a bit
more uh in well position to basically
respond to you top five customer
considering the currency that those
transaction were made in.
But, what about the exchange rate? We
haven't provided any exchange rate. So,
what will the model do if we haven't
provided that? So, it will most likely
consider the exchange rate that the
models were trained in, which are
factually incorrect. Uh and the response
will be most likely not the actual uh
response that you expect or something
that you can rely on.
This also brings us to the next
challenge that I want you talk to you is
about the hallucination and factual
accuracy.
So, as soon as you have some gaps in
your prompt,
the model will try to fill those up. So,
in the example that I just shared, since
we didn't provided any either the
authenticated source or the exchange
rate, the model will come up with some
kind of exchange rate and give you some
response. So, that is a very risky thing
in ERP because uh finance is a
finance-heavy ERP system is like we
depend on our life or our business on
those numbers. So, we need to make sure
there are no gaps
uh within our uh system so that the
model is not inventing stuff.
You need to add some kind of one-time
validation. So, whatever the model
responds, you need to validate that
response within Business Central before
you are basically suggesting to the
customer.
An example could be to cite the document
ID or
some kind of reference you ask the model
to respond when it whenever it's
responding. And then within AL, you do
the sanity check if uh there are any
transaction, for example, for this
particular customer or not or if any of
the numbers are looks suspicious, it
doesn't add up uh uh
when you do uh some validation inside
AL.
And one more thing that you can do is to
force citation or magic function. So,
like again, something like if the model
is uncertain about, rather than
responding with something, you need to
redirect to the magic function by
saying, "Okay, if you're uncertain of
the or if the information is not
available to you, call magic function."
So, you need to do these kind of check
to make sure that you are avoiding any
hallucination or if the model is coming
or making stuff up.
So, yeah, you could trust models for a
lot of different things, but you need to
verify whatever the response that you
get from the models.
Let's look another example. So, now our
Copilot is built on top of some vendor
information and all the transaction that
we have with the vendors.
A question that you can ask or the user
can ask is like, "What's the time it
take for a particular vendor for
delivery?" In this case,
vendor 03.
Even though we have not provided any
purchase history, the model would be
naive enough to respond saying 27 days.
So, again, something if we have some
kind of AL validation and we try to add
up like there is no purchase order for
this customer, how come we ended up
having 27 days? So, you could raise some
flags and not to respond back to the
customer when they try to when you run
to this kind of situation.
But, let's see how you can do basically
inside the prompt itself as well.
Similar concept that we have been
sharing all along this presentation is
like,
you should only consider the information
that is provided to you.
And if you are unsure, you should always
call magic function. So, if there if the
model feels any of the information does
not exist, it will call the magic
function. So, if you look at the table
below,
there's a list of transaction, but it's
only for
the other vendors, which is vendor four
and vendor five, but not the vendor
three. So, just by introducing these two
simple instructions, the model will
basically trigger magic function rather
than responding you with some random
number.
The next challenge that we all have is
the token token limit which they briefly
mentioned. And we have a lot of large
business data that we want to share to
the models to make any decision. So this
is a very big challenge that we have and
we all know
that GPT-4 model that is the the one
that we are most of our features
currently build on has this 128
thousand token limit which roughly
translate to 90,000 words.
But this doesn't mean that you can use
efficiently this amount of tokens.
The more tokens that you use, the
quality will go down, the latency will
go
high and the cost will also balloon.
A rule of thumb is like for every extra
1,000 token that you use, there will be
1 cent for the prompt for every request
that you make and 3 cents for the
completion. So you can see like although
we have this large context,
you cannot basically use the entirety.
So you need to be a bit more efficient
when using the token.
To put a bit more emphasis to this point
like there are some a lot of benchmark
done on different models. So I just want
to share the benchmarking some of the
benchmarking that was done for the GPT-4
model. You can see when you are using
from 8K to 32K tokens, the accuracy is
quite high. But as soon as you are
ending up using more tokens, the
accuracy you see a noticeable dip inside
the accuracy. So that's not something
that you can rely on your system like if
you're using a lot of tokens,
uh
if latency and cost is not a question
for you, but still if the accuracy is
not there,
uh then you cannot basically rely on
such system. So I just want to put a lot
of emphasis on this like you need to use
your token efficiently.
So, that's why all the things that we
discussed like you need to start simple
with your prompt. If something can be
done in less tokens, uh why use more?
Let's look a real-world example like
uh a lot of uh
co-pilot that we have built internally
and a lot of feedback that we got from
partners like they were building some
co-pilot on top of items.
And you know like if we want the models
to know the context about all our items,
we not only need to provide the item
table itself, we need to provide the
variance, attribute, translation,
categories, and bunch of other related
tables to item to make sure the model
have the entire context. But, you can
see as soon as we have these different
tables and we need to provide all the
information, the we will ended up ending
up using a lot more tokens. So, this is
not a practical solution especially if
you all have a lot more items. If you
have very few items, then it might work.
But, if you have a lot items, uh
even uh smaller amount of items with
this
uh combination of all the tables, the
you will end it up using a lot more
tokens.
So, let's look a similar example related
to this.
Uh so, you have a co-pilot built on
these items uh where you need to respond
with the best possible matching item.
So, the the So, the user query is I need
five red kids BMX bike.
So, if you would have to dump the entire
item table, the cost will go high, the
latency will go high, the
quality will go down. So, what's the
mitigation over here? So, one of the
mitigation that we use in these kind of
scenarios where the data is very large
and we still need to get some value out
of the uh LLM. So, what we do is
first thing is rather than sending the
entire data, we try to extract the
intent and the key keywords that we
want. So, in this particular use case,
we are getting the name of the item and
the feature along with the synonyms as
well. So, the user is saying bikes, but
we could use the LLM to get the synonyms
of bike as bicycle as well. Maybe the
item is called bicycle inside our
system, not bike. So, not only we are
extracting the keywords, we are you can
extract the synonyms, you can also
extract the alternate terms
uh
or you can be even more smarter about if
you are your system is any particular
language, what are the different uh
ways of uh
items that you have named within the
system. So, you can try to extract all
those keywords from LLM first.
Then you pre-filter all the items based
on the keywords that were extracted.
Maybe you could only filter on the item
description with the name of the bi- uh
name of the item. You might you may
ignore all the features to do this
pre-filtering.
And then you only send this subset of
items back to the LLM so that it could
now you are sending a a lot less amount
of data for LLM to basically get the
best results out of it. So, this is a
technique that we use internally for a
lot of different scenarios where we have
to send
a lot of con- uh content to the LLM to
basically get the the entire context.
So, we try to first ask the model what
what are the key things the user asked,
try to do some filtering within AL, and
then only pass the filtered data back.
So, how it looks like in prompt is quite
similar. So, this is just for
demonstration like this prompt like uh
So, it's too small over here, but yeah.
So, we need to convert the product
information in the JSON.
And
and you can see I'm trying to extract
the name and the features and for this
particular example I'm getting the name
with the synonyms as well. You can be a
bit more advanced, ask about alternate
items and all those things, singular and
plurals and you can do a lot of
different variation when you are
extracting these keywords from LLM and
then you could try to see which are the
key fields inside my
table that I could filter based on which
field.
So now when we when the user says I need
five red kids BMX bicycle
the response is the name which is bike
or bicycle. So we do an or. So now when
we are
searching applying filters in AL, we use
an or. So in case even the item is named
bicycle, we will probably get it. And
then we are also extracting features.
Even for the features you can ask for
synonyms as well. So now the are you see
how small our prompt is like we are
just trying to get the
the key the key information from the
user input.
One more challenge that I want to the
last challenge that I want to talk about
is the maintainability and the
testing of the prompt.
There were a lot of
information that was shared in the
keynote as well regarding the testing.
But before going to the testing part of
it
you have to do a lot regarding the
maintainability of the prompt. You know,
every other month we are getting newer
model. So it's pretty hard to cope up if
you do not have any kind of test or any
kind of mechanism to maintain your
prompts or corporate features.
So the few things that we do internally
is like we consider these prompt as
executable specs.
So every model temperature tweaks, any
change within this
BC schema, we consider that that could
basically flip the output.
So, every times anything change in the
LLM world all the model, any
configuration that we have that model,
or even something change within Business
Central, we try to make sure we run our
tests again.
And the model drift is real. I'm not
talking about moving from 4.0 to 4.1.
Even within 4.0 like recently we
experienced when we got
the response that we were getting out of
this model were like 20 times more in
length uh
for let's say for a marketing text or
these kind of uh features that we had.
So, if you are depending on those kind
of things, so
uh you need to verify even if you are
staying within a single model, but using
a newer iteration of that.
So, we treat prompts as code. We keep
them in source control, and we always
spin
this is the prompt that works for this
particular model with this particular
configuration. And every time anything
changes, we try to make sure we run the
entirety of our test, and then try to
pin again, okay, now this version of the
prompt works against this model with
this configuration and this version of
BC.
Lastly, uh
you get a lot of things out of the newer
model. So, a lot of things
that you might be facing challenges
challenges when you are writing prompt
for a previous model might be already
fixed in the newer model. So, it's
always a good practice to always use the
latest greatest model.
But that doesn't mean your existing
prompt will work
with the same accuracy or better
accuracy with the newer model. You need
to change your prompt. So, one example
that was also shared in the keynote like
moving between 4.0 and 4.1, 4.1 is very
good in understanding the instructions.
So, it took each and every word
literally. So, it basically
dropped our performance. For example,
the performance that was mentioned in
the payable agent that we faced is
because of like how the good the newer
model was how we
compared to the previous one. So, you
always need to do some kind of
adjustment whenever you are changing
models.
And always try to aim for the latest
greatest model.
And we like I mentioned, we have all
these guardrails in in form of test. We
have telemetry. Anytime anything
changes, we have these automated
pipelines. So, we run it daily, weekly.
So,
so we are making all the changes in the
business central. So, at any point if
there's any change in the accuracy, we
are notified and we try to rectify that.
So, let's look few example how the how
things could impact your accuracy of
your co-pilot.
One is not related to the model itself.
You are on the same model with the same
configuration. But like like I mentioned
recently, we renamed jobs to project for
all the user facing. So, now if your
co-pilot was basically built on top of
that, it might not perform as expected.
Although nothing changed in the LLM you
are using still using the same model and
same configuration. So, the point that I
want to make here like something that
changed in the product could also impact
your co-pilot feature.
And again,
if you're working with a model and you
are only using at the newer version of
the same model,
it might add extra information. So,
previously you might be extracting a
the response in a CSV format uh which
were previously responding only three or
four columns. Now the model suddenly
decided to put another column, which
basically is to show how confident it is
uh for the result that is being shown.
So again, if you have some AL logic on
top of this particular response, it
would uh it will break.
So,
there's a lot of things that we do to
make maintain, uh but the number one
thing that uh the thing that I want you
guys to take away is using having a lot
of test. And for that, we have this
Business Central test tool
uh
for Copilot uh that was also mentioned a
lot in the keynote as well. So, I could
not put any much emphasis like whatever
you build, you need to have a lot of
test using this tool. And this tool
basically helps you a lot uh to use to
maintain your Copilot feature, and it it
basically uh
uh you will save a lot of time if you
use this.
I will not go uh very deep into what
this tool is all about, but
uh just to give a very higher level
overview is like you have one test, and
you have hundreds of input as uh as test
cases. So, uh each of these test cases
have the expected output as well. So,
you run all of your 100 use cases
against your single uh Copilot feature,
and based on whatever the response is,
uh you validate that. So, in case of
features like marketing text, you need
some extra evaluation because the
response is uh free text. So, you cannot
have an uh AL logic on top of that. But
if you are basically extracting
keywords, let's say if the user say I
need two red kid bicycle, and the output
always needs to be this particular
keywords, you could have basically uh AL
logic on top of that. So,
yes, please try to
uh, test your feature. Have a lot of uh,
test cases. Even like internally,
whenever there's a bug, we convert that
to a test case. So, we make sure if we
have fixed it now. So, any future change
that we make to the prompt do not affect
any of the test cases.
There's uh, another session tomorrow uh,
talking a lot more about this testing
and also how you can basically generate
this a large uh, data set that you can
test your feature against. So, you can
only come up with few test cases on your
own. But, uh, to make sure that it works
across a lot big uh, data set, uh,
please free uh, join this session and
you will know how you can basically
generate a lot of data set uh,
uh, using the power of LLM.
To conclude uh, the challenges part,
grounding is
The every environment that we have is
like different. So, you need to give
this extra context about what your uh,
Business Central is, how it's performing
by decoding the codes, uh, the caption
and the rules that your environment
basically
uh, follows.
To avoid hallucination, you need to use
concepts like magic function. You need
to make sure there are no gaps inside
your prompt. So, nothing is left
completely on the model to assume. So,
you need to do all of these things and
you always need to validate the answer.
And yeah, testing is a big factor that
you can
uh, use over here.
Token limit, like I mentioned, we have a
very big token limit. But, you need to
use this
uh, efficiently to make sure your
co-pilot feature is basically working
performantly.
And lastly, try to use the latest
greatest uh models and always try to
have a lot more automated uh testing to
make sure that you have the best
possible uh
model to work against. And so, something
that you will get a lot of things from
the newer model already.
Uh
that's all from our end, but now we
would like to open the stage for Q&A.
Yes, so we'll open it up for Q&A. Uh if
anyone has questions or if anyone has
actually written in here, um I'll
quickly look.
Um okay, we do have one question
actually. Um just to also note,
we have t-shirts. So, if you have
questions, we'll give them to you.
Um
so, one of the questions is, I can see
you use a lot of markdown for the
prompts. Is this the best way the LLM
will understand the prompts or is there
another specific reason?
Do you want to take this?
I think in our experience, uh we need to
give the instructions in some uh
structured way to the model itself as
well. So, the markdown is the simplest
format that we feel giving to the model
by using the least amount of tokens.
Even if you are using JSON as an input
of your prompt, then you might end end
up using for the same text, you might
end up using a lot more tokens. So, for
from our internal experience, I think
the markdown syntax is the most simplest
one that we could give instructions and
it's it's very capable of understanding
the syntax as well.
So, I can't see who wrote this, but I
think it's a good question. So, later,
please.
Oh. All right, I'll just pass it to you
now. Woah.
Oops, sorry about that.
Um all right.
pass this to
Yeah. Why don't we Why don't you go for
the next question first?
Yeah, just speak into it. Oh. oh, the
top dropped off.
Um so, basically, what what what what do
you expect or what do you think how
resilient is this to
letting it loose on partners and having
them extend like tables logic and etc.
It's like Is that part of your focus
there as well? Because I saw that you
all your problems and you had fixed
parameters.
So, at that point, it is basically
non-extendable, is it?
So, that part is not really extendable.
Uh I mean, theoretically, it is because
you could have it such that
uh
when the LM responds, it tells you call
this function with and it will give you
a JSON object, basically. And it's up to
you what you want in the JSON object.
You could have Let's it put in, say,
free text. And if within that free text,
it could be another JSON.
It could be anything that you want it.
So, you don't have to hardcode it to
tell it that, "Hey, I want these views
only." You could let it kind of make up
the rest of the things in there. And
then, in your application, is where you
kind of read what is actually in there
and then perform
what is actually given to you.
But, we're still reliant on that initial
connection that the agent and the prompt
did to the call function, basically.
I'm sorry, can you say that one more
time?
Like like um searching item
Okay.
has fixed inputs and outputs. And so, we
can't extend those.
No, that that wouldn't work. Yeah.
That's what I was going for. Okay.
Thank you.
Uh I get Oh.
Okay. Why don't you pass it to him? I'll
just take the other question I saw here.
Is double um
hex a reserved word in prompts? No, it
is not a reserved word. It's basically
just markdown. It's a markdown for if
you have one hex, it's like the title,
two hexes like title two.
So on and so forth.
Uh you please go ahead.
Yeah. The hallucination in the prompting
is real problem. Like once you also give
the context to the AI and then you do a
subsequent prompting,
it's again start hallucinating.
Because you have one prompt, you have
given all the context, you have all the
given all the resources and then you get
a response and the next you again write
a subsequent prompt, it start
hallucinating again because it loses the
context sometime. And that's a real
problem.
How do you how do we make can make sure
like if you want to build a something
which is a sequencing prompting
and we can get a consistent answer.
Otherwise, we have to rebuild this
context again and again with each and
every prompt which will be like too
much.
My suggestion will be to split uh
what you want to get out of the LLM. So
for example, when we talked about the
example of splitting the items like uh
we wanted to rank uh get the best
possible items out of all the items.
So we have like a different version of
prompt which is we are extracting
keywords, only sending the subset of it.
So we might not need the context from
the first part for the other part. But
yeah, if you want to pass context, you
will
reach
uh the limit of tokens or even you ended
up using a lot of more tokens which will
basically hallucinate as well. So you
need to come up with more uh
creative ideas how you can split the
multiple calls to make sure that you
only provide what is needed for this
particular call.
Uh but yeah, s- depending on the
scenario, you will need to come up with
these kind of innovative ways to avoid
using a lot
a large context window.
So basically you are saying we should
use the functions all the time. Like
when we actually want to build a
sequencing, we should you build lot and
lot and lot functions.
Yes.
Then we actually start sequencing
calling these functions.
So, it it could be one way, like for
every call, you only send the functions
which are relevant for that particular
call. You should not have a very big
list for all calls.
To add on to that,
the models don't work well when you give
a lot of functions. Like I would say
about eight should be about your limit.
More than that,
it's not going to be able to choose
well, unless you have really
well-defined functions that separate
from each other.
Oh.
It's going to be behind you.
Thank you for letting me know about it.
No, of course.
All right. So, on your
maintenance and testing slide, I think
you talked about the model drift, right?
Yes.
So,
if we write something that's working
pretty well, it's been thoroughly
tested, and then you talked about how
with the May patch,
you know, things have changed. At what
frequency should we be testing our code
or testing things that are going to be
using a certain model? With when I
typically write something in AL, the
goal at least is once it's been tested
for about 6 months, I can usually rest
assured that my code's probably not
going to break.
At what frequency should we be testing
something that has been written using a
certain model? Are these patches
impacting
existing code that's working? Do I have
to opt into taking, say, the May 2025
patch if I'm using the GPT-4 model?
Because that seems like a constantly
shifting or moving target, and the cost
to test, forget the cost token-wise, the
human cost to test and keep up with this
could be fairly significant.
Yeah. Uh so, internally, we uh run this
quite often.
Uh some of the examples that I showed is
not just about transitioning of the
model. Anything that changes within the
product could also impact the output of
your co-pilot. So, every time you see
something major changes within the
product, we try to run all of these
tests, and we also even run these tests
even more regularly, even if you are on
the same model to make sure that we are
on the higher accuracy. But, yeah. Uh,
six Yeah. So, every time you do what?
Model switch duration, definitely you
want to run the test again. But, now,
uh, if you are doing it after 6 months,
and something in the product could have
impacted, then it will be very hard to
go back what changes were made in this
long period.
So, Kasim, if I can ask a follow-up
there.
Yes.
You talked about model switch. In this
case, it seems like the GPT May 2025
GPT-4o May 2025 patch, is that a model
switch? As in, do I have to opt into it?
Or does it automatically affect anything
that I'm
building using GPT-4o? I mean, that's my
concern. It seemed to me, maybe I'm
misunderstanding it. It seemed to me
that since it's a patch, it's
automatically going to apply to
something that I've built. In which
case, it seems like I have to wait for
something to break, somebody to tell me
it's not working, or maybe it's not
working accurately, which has lowered
trust and credibility for my users, and
then I have to fix it. What can I do to
stay ahead of the curve? What can I do
to kind of
proactively do it?
So,
make sense?
Yeah. So, if you're using, say, directly
from Azure Open AI, they do have a
configuration that basically asks you,
"What do you want to happen when they
have a new version?"
Yeah. So, for example, if they have a
new version coming up, you you could
say, "I want to always be up on the
latest and greatest." It will
automatically switch you. You don't do
anything.
You could also say, "I only want to be
switched at the very end." That's also
an option. Or you don't want to ever be
switched, and you basically be broken at
that stage.
Uh there's one in the back.
Uh yes.
Yeah. So, uh outside of running these
tests, are there any way to keep track
of how the models are doing? Um I mean,
can we in the telemetry set up
something,
uh cuz as a partner, we develop a
solution for a customer, and unless they
talk to us,
we'll just let it run, right?
Yeah.
Uh so, one way is like if suddenly
started to uh
raise a lot of magic function, for
example, things that were working. So,
you can have that kind of telemetry, uh
like if the magic function is being
called, or uh you can log that, okay,
something is not working as expected,
and you can see the intent out of it. Uh
internally, we do not uh log any of the
usage, exact usage, how the end user is
basically using it, due to privacy.
Uh but yeah, uh you could log all the
As a partner, I I guess you can log some
kind of telemetry of which functions
were called. Based on that, you can make
some educated guess, okay, if something
went wrong or not.
Okay.
I think we are out of Are we out of
time?
We have 2 minutes.
Okay, we have 2 minutes.
Okay, there's no questions in the
audience. I mean, there's still more
questions on the app. Um the first one
being,
what does "Please send me quote for one
sex bomb model" meet safety test? I
mean, it's one test, and
it will be part of like the harms test
that was mentioned by Peter.
It's the I think it will be covered
under safety
sexual
and harmful
test.
So, yes, that would meet the bar.
But, it is something that when you're
building your test, you need to have a
large wider wider sweep
of
prompts that you're testing against.
Meanwhile, I just want to mention this
like if later on you're working on your
co-pilot and you have some challenges
that you want to reach out, feel free to
reach us on LinkedIn. I think that's the
best way to reach us
after this conference, of course.
Yeah, I will also be at the booth.
Okay.
Yes.
Just one question. How is the
multi-language support for the prompt?
So, a prompt is uh
written in English will work with
data and uh
with
in every language or are there some
consideration to be made?
Yeah.
So, the prompt itself uh how we do it
internally is are are always in English.
But, the responses we specify to be in a
particular language. For example, in
marketing text, if you're in a German or
a Danish environment, we will respond
the marketing text in those particular
languages. So, there are a lot of stats
for each model how it well performs for
each particular languages and it's
getting a lot more better. So, English
is still the best
the models work against. Our prompts are
always in English even if you are
working in any country version, but the
responses are also getting a lot better
in all of these uh country specific
versions. That's why we have a lot of
features GA in all of these uh country
and the accuracy is quite close to
English in most of our
uh places that we have uh released.
All right, and we are basically out of
time. I want to thank everyone for
coming for our session.
Thank you.
