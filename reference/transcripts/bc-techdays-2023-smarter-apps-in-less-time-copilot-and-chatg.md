# BC TechDays 2023 - Smarter Apps in Less Time: Copilot and ChatGPT Integration for BC Developers

- **Source:** https://www.youtube.com/watch?v=tKFWO9sT-Cc
- **Video ID:** tKFWO9sT-Cc
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 93m03s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you everyone hello everyone
Welcome to our very handcrafted session
no AI generated
almost
so my name is Dmitry
my name is this white
oh yeah
my name is Stefano
yeah so today we will guide you into the
world of AI
into the judge Deputy how we can connect
together
jgbt open AI all these magical words
with the business Central
and today you will probably learn
about vs code copilot X
then we will move to jgpt and Azure open
EI and into the world of prompt
engineering you saw some slides and
demos during the keynote and also
and you're in the co-pilot session today
we will do a more deeper technical dive
into how you can do all this stuff
foreign
then we will do some introduction how
you can embed a chart in business
Central
then guide you into the world magical
word means embeddings
what does it mean and then Stefano will
also show you another part of the story
so how you can use external tools like a
dotnet and semantic kernel to chat with
your data
um
but to start
I was thinking how to start that and
what demos to prepare and we as a
developers and as a users we all we
almost we all want some free time and
focus on what really matters
and but in a business Central and in
this code there are still some
areas that are very difficult
that we need to learn how to how the
things works
and sometimes we use them rarely so we
always go to Google and search how the
things works one time to time Stefano do
you have such areas in a business
Central
yes sometimes I've uh I need to uh
search in Google for example for
handling sales and lots for me it's a
it's not a comfortable way and speaking
about the developer's perspective for me
is always sometimes difficult to
remember for example the date formula uh
something that sometimes I need to check
the Google documentation in order to
create complex form or something like
that
for me especially I found myself that
for me it's very difficult to
um
schedule job cues because there are so
many things to remember like object IDs
the records the app is difficult then
there is date formal as well that is too
complicated and I thought and you know I
got some idea how we can
make things much easier
and you and I wouldn't do you know where
a good inspiration yes I think it's good
because it's scheduled queue sometimes
is tricky so if there are some tools
that can help I think it's could be
interesting for everyone yeah so I
actually agree so I actually got the
inspiration from my wife because my wife
she's super good as a task scheduling
she can just tell me hey go to get our
kids from school and on the way to
school go to the grocery and take some
fruits and that works you know
and I actually asked judge PT
um
I was interested
what other like General wife do task
scheduling for General husband
and uh he told
that darling tomorrow morning could you
drop
dry cleaning
hey honey
I have a doctor appointment do some
stuff
I love the last one hey superman
tomorrow is our anniversary
could you plan surprise date night
and actually if you think about that
jdpt was trained on the public data from
the internet so it means that there is
some secret place in the internet where
wife our wife has access where they
learn how to do how to schedule tasks
for the
for us
and that's I thought maybe we can do
something in the business Central
so I thought so I just built some
prototype and today we will
go through the process of building the
chart inside of business Central
and uh with a just natural
not voice today but natural language
typing we will ask
business Central to schedule job gives
for us
yes that's nice and I always want my
users to be able to use a tool like this
in order to be smart and schedule task
and interact with data quickly and can
we combine both
yeah sure so let's start with a copilot
X GitHub copilot X because
so we want our users to be happy with
the business Central but we want like a
developers to be happy in a vs code so
hmm
the copilot X let me see I have
let me go here first so the copilot X is
actually an extension which is called
copilot nightly in a vs code
that you should sign up and then
uh
it will give you so it will you will
send upheep here and it will give you
some nice features inside of vs code
so
Zoom that a little bit
so the first feature is this chart you
saw that in
you know today
so what we can do
or I will just
copy some
code
so what we can do
we can ask to generate table
with the end point and the secret key
for example
you see now it generating something not
very ale related okay
so but we you can give him
point for example you are
L developer
not really well
that's right
okay a a l
come on obviously
come on okay maybe try not
you're written
in
L language
nada
foreign
yeah okay let's do another way
I love that
so we created an ill
be a cracked charging Beauty
oh
[Laughter]
[Applause]
okay
um
so we will just paste it here
we do some cleaning we don't need that
and I think this should be
text
so you saw this during the keynote what
you actually didn't see during the
keynote is another feature
copy that as well
so we are now inside of the object let's
say
and there is a magic
combination of buttons which is in on
Mark is a common I
and in a Windows it's alt I which
actually means a i
so we'll add two procedures to return
endpoints in the key
and
forget that
that's simple
right so uh we will create in a page in
a
very natural way
okay so I will now have a table
and the page
um
and let me
so what we also prepared
let me return to the slides
so with a GitHub copilot X once again
you need to sign up
it will give you
the features like embedded chat and one
more feature that I will show in a
minute
um
and then
we created a control add-in actually we
created it without DPT
so this is the control adding that we
prepared it consists of actually two uh
fields
the one field to input
and then
the message from the user and then the
history and then re the response from
the AI so very HTML
built inside
and
you can do better than us for sure
because we have enough Force boost on
the CSS or something like that
yeah so
now we have this setup table and control
it in what we need to do is we need to
add the Azure open AI integration for
that
yes uh Azure open Ai and you mean champt
but there's a difference between Azure
open Ai and uh
open AI
yeah that's a very good question
um
you probably hear like a chat DPT open
AI Azure open AI what's the difference
between of them and
actually I want to a little bit talk
about where we now in AI field
so the artificial intelligence I
actually use this slide in two years or
more
here on the BC check days
and we actually were
here
so the there is artificial intelligence
like a general area of in investigations
about what machine can do what machines
can can it do as a with the same
communicable capabilities then there is
a machine learning so it's techniques to
train the machines on the data then
there is a deep learning it's a kind of
algorithms inside of machine learning
area so it's special algorithms how to
train your data that were the state for
three years ago and now we actually have
this generative networks and this
generated networks is a one step further
but is inside of deep learning so it's a
type of
deep learning algorithms and inside of
generative networks there is a GPT so
the GPT is only one model
that is became very popular but still
there are a huge amount of other models
that we can utilize and that are very
open source
and
so it's not only GPT
okay so are there any other models
and like Azure open AI so the open AI is
actually a company that built jdptpt the
Azure open EI is a service inside of the
Microsoft azure
the Microsoft partnered with the open AI
so the Microsoft
store the model provide the API requests
and so on
there are also some differences between
openai and Azure open AI
so
the common things is that the models
itself are the same because
the Microsoft actually provides the apis
to the model that were developed by the
open AI company
however on top of that Microsoft had its
infrastructure
security capabilities and also content
filtering
that's the main differences between the
apis from the open Ai and the API from
the Azure open AI
how to get access
also there is a difference between
openai and Azure openai with the open AI
you can get access immediately just you
need to sign up on their web page Azure
open AI you need to go to the wait list
and there are actually two wait lists
the first one is to get access to the
Azure open AI itself and then to get if
you want to get access to the gpt4 which
is the latest model you should also sign
up for another wait list
so you are saying that I can deploy my
own charge gbt mod inside my Azure
account yeah sure you can just try
oh let me try
to do that you can simply go into the
original portal obviously as Dimitri
said you need to have the Azure of an AI
service enabled and inside the Azure
open AI when you have the Azure API
service you can
create an Azure open AI instance
it's very easy just click create an
instance and here you can see the first
big difference compared to Azure
compared to the standard open AI
features
it's Azure in this guy in this in this
way you can specify the region
you can specify a resource Group so
group resources Azure and you can
specify a price in TL pricing tier is
actually is only one
but in the future you will have more
than one present here the main
difference is that you can specify the
region so as you can see in my portal
you can have more than one instance of
ai's European AI service deployed on
different regions for example later I
will explain why
any sign and Azure open AI instance I
previously created this
you can specif deploy deploy manage your
deployments your models
and by clicking on uh model deployments
you are redirected to what is called the
Azure open AI Studio
and inside Azure organized Studio you
can create and deploy your model
instances you can have different model
listers also for the same model
should open AI Studio starts
uh from ER
you can deploy the model you can test
your model you can play with your models
writing some prompts see how your model
response and then see the deploying the
model is very easy just click create
deployment and you can select one of the
available models inside your
subscription so it depends on what model
some models are available at the moment
only on us other no are available in
everyone like in this case I deploy the
instance on West Europe
uh you simply select the model for
example the I don't know the GPT
turbo and you can specify the deployment
name if
uh in your subscription you have
um yet deploying this model or bypass
them or the the quota that you have
available on the subscription and
message appears saying that you need to
request more quotas on the subscription
uh when you have the deployed your
models you can have as said any
different instances of your model and
you can see here that you're a different
models have different capacity and later
we explain and we show how you can
handle that
okay so you deploy the model
I have the table and the controller Gene
now we can write our code to call the
Azure open AI
uh yes we can do that but uh
you know you how you can do you can do
that to
in India language do you do you have a
uh
you do you know what what community
there is there in Business Center or
I saw in the today uh session that um uh
we we have a co-pilot already in
business Central so it means that there
should be a good unit yes uh uh but uh
if I I don't remember the name of disco
unit so I think that we can use to do
that a tool that someone developed uh
this Tool uh can help us because we can
for example ask something like uh what
type of code unit we we can have for
example uh is there a code unit
or Azure open AI
in business Central something like that
we open this is in code Focus mode so
Central queue
uh she would give us some answers about
the code I probably know someone who
developed that yes probably and uh oh
yes the the unit is called Azure AI
usage and that's this ID so I think
probably you you
you can work on this
yeah so and we can
even click here
and go directly to the system app
uh okay so what we're going to do you
know
I think we can achieve that because
the access is internal
but yeah the thing is that
Microsoft show today that there is a
copy of that available on another report
so but they didn't notify me about that
so I will just follow my demo
so uh what we're going to do we can just
copy some parts from that I guess
so we will do
here
okay
so there is a code unit and I think we
need
so I think we need
probably this function
and we need a sent completion request
and Ascend request
so just copy that
and let's do some cleaning
just
delete some parts here and we have
actually our own settings that we
created
with just
do it very simple
we don't need that
you don't need that
and we created these guys
go get endpoint
and
it was also a get secret key okay that
we created before
delete that
we don't need that so actually when
Microsoft prepared for the session
yesterday
I mean for the keynote I think they did
more or less the same
at night
yeah we can just
move that
just to be there delete that
we don't need many things here
payload payload
oh yeah good
okay so more or less fine so uh what
what I want to show you here it's
another feature in uh
copilot X
so what do we actually did now
I am just on the stage of the visit like
this cloned the code
and that was the code that I didn't
wrote so
I can just go through code and
understand how it works but what we can
do actually
here we have
explain things
so on the right side we have a code
and here we have Alex explain this code
thing
and everything here we can just read
that and uh
yeah it seems
we even have some
improvements recommendations here
uh
you know what I also doesn't don't yes I
don't understand why there's this lash n
yes why is this needed I don't
understand that as well so maybe we can
uh ask so what we can do we can just
copy uh not copy select that
and then copile it explain this
oh so with some kind of
when we got back some response from the
open AI it do some cleaning of that
response
okay good
also
you know what
um
so
this is the playground that you showed
uh but we also have this show code
and so very actually two uh endpoints
with the uh
GPT calling thing the first one is the
completions here so the completions is
what you saw during the keynote and the
completions is the model the endpoint
that uses with a BC Copilot
but we want to do a chart
and the chart is it uses another uh
endpoint well the endpoint is the same
but them parameters that you paste into
the call different instead of the prompt
we should paste messages here
okay and here you see we paste a prompt
so what we can do we can just change
that
messages messages
and then we can do something like that
get
messages
it also should be a
user input we should provide that in the
beginning
and what we actually can do we can ask
copy that
alt a once again
so play it please create a Json array in
the next format
and it creates actually a
procedure so we just need to
get messages
right so now we have a
we can do some cleaning here but we now
have a Json array
that we put into the
messages
the other thing if you switch to the
messages
you should also
replace
the output because the output from the
the response from the open AI is a bit
different if you use the messages so
actually you just need to go here and
just
replace with a choice messages content
so and you are good to go but I have two
questions on this uh first what is a
prompt
uh not totally understood and the second
if you get if you get a response from uh
open AI uh how do we we create a job
queue task from that
it's a very good questions my friend
so now we're diving into
another part of our session about the
prompt engineering
so the prompt is actually a text used to
generate a response from the language
model
so think about the prompt as a some kind
of instructions that you give to to
intern
that you have
with you
so in turn will do the work
for you
based on your instructions
and there are some techniques that
will make your prompt
as good as possible
the first
you should set a model into some role
so usually now it's industry standard
you start your prompt with the Ur So you
are a teacher you are a psychologist you
are Al developer you are an API or so on
then
do some instructions at the beginning
continue with some additional context
I will show you how to do that
then provide some examples
about the input and about the outcome
and
you know there are always difficult to
try to find a balance between a short
instructions and Loan instructions
because you cannot put as long
instructions as you would want
there is also the documentation from
Microsoft
uh you can follow this link there are
many examples of how you can structure
your prompts
so and for our task
our good prompt structure will look like
this so we're good in the beginning some
instructions
we put into the context that you are
Dynamics 365 business Central job queue
scheduling API
you must only return information from
the context that we will provide
then we will provide some
instructions about the input and the
output
we will provide the output format
provide the context text examples
and once again
we say that answer in this format the
thing is that
always try to one more time
say about the you know
output format at the end
because
lunch language models
if you put much information into the
prompt
and you will tell about your output at
the beginning
they can just forget about that when
they read down to your text
so let's go here
so this is actually the open AI
playground
I will
copy paste some things here
so here we can play as a user who use
our app in a business Central
they probably want to schedule a job
queue in a natural language way like
this
update analysis views every morning
uh before working hours on a working
days
however before
however we are not given to the AI any
prompt how to do that so AI response so
as a Al English model I'm kind of
schedule tasks
so we need to provide some system prompt
for that
let's try from a simple one
you are a business Central job queue
schedule an API
so
now we like put the model into the
context of business Central
so it tried to respond
in a way how to schedule the job use so
it's more like um
helper for the user but we don't want
helper who actually wants to uh
schedule the job use automatically so
actually put the temperature to zero
uh just not to be very creative in that
and they increase the maximum length of
the output
what we can do we can uh
add
more
things to our
prompt
so uh here I describe that you will
provide it a request an initial language
about how to schedule a job here so I
telling him about what should we would
be the inputs
and here I tell that you must always
return results in a predefined Json
format do you know why I'm doing that I
think because we need the structural
Json response in order to be able to
call the apis
not exactly to call the apis so the
thing is uh when you like
receive a response from the open AI
model
you you as a developer expects to
receive a response in some structured
Json format that you can just just pass
this Json format and do some action in a
business Central that we're actually
going to do
so if we do like this
so now we we see that well
our response have some Json but also we
have some comments in the beginning so
still still not very structured
so we can
continue improve like this
don't include any comments
how it doesn't include any comments
so um
now we have like a Json response that we
can at least somehow
parse in a l but
if you look into
the contents of that actually it's not
something that
we can use in a business Central to
schedule the job queues so we need to
actually teach the open AI how the job
scheduling works in a business Central
and how we can do that
yeah so actually there's one more thing
that I forgot to show so this uh the
output is not very structured Json so we
can do like this and specify which Json
format we expect from the model to have
so now we have like a structured output
but uh
you need you see this like a next round
date formal is today and it's not
something that business Central can
understand also like around on Thursdays
comes together with next round date
formula
that will not work in a business Central
so we need to add more context to that
and what I did I actually searched with
a central queue and it gave me some
links to the blocks
about how job scheduling works so
actually two blocks
this describing the job scheduling
scheduling and also another blog
described in the edit formula
so what I actually did
um
let me
go to the
tick this one
so what I did here
the same beginning
then
the context part
then I just paste here the information
from the blog
and then I just paste here the
information from the second block
okay
and I saved some placeholder for for the
examples
and we will add examples
in the couple of minutes
and let's see if that
getting better
so now we have like a better result
let's see with another
request
how it works
run the code unit three two five on the
last Friday of current months at
16.
and I would use the correct
things run date for more
um
and maybe
try another one
so
what I see here which will not work with
the business Central
it used the next date formula together
with a run on Fridays in a job Q
scheduling we can't use that together
so I will add
some limitations
into the prompt
I'll just copy that
so I add this like limitations so once
again this is like instructions to the
model
first don't generate object type object
number if you don't know
then generate a comment politely say I
don't know
it's not allowed to set next run date
formally and other fields together
like other things
also I asked him describe your steps to
get the result into the AI command field
I will use this field to Res to show
into the chat window into the business
Central
let's see how that works
so we see now we have like AI command
first filled in a Json respond
describing how he got into the
result and also it splitted this request
into the two job queues instead of one
because we had the limitations we can't
use that together
okay
um
the other thing which is also
useful to add is these examples so I
will
copy that
once again
the examples are good
because that will give you more reality
reliability on the
output of the model
so it's the same problem but I added
these examples
request and response so for example if
the user asks run every Tuesday AI
command sorry I can't schedule you
didn't provide object type object number
then like another request
and the response that I'm
assuming should be
and the one more
so if I will do I think this is the same
one
so yeah you see that I created two
separate job queue entries
that's
good boy
or girl
so if we go to the
business Central now
so we oh yeah I forgot to show you
uh code
that
yeah
so
we
I prepared this
code
to parse the
to create a job queues actually what I
do so I call
here
so I sent
uh these two the user request to the
Azure implementation code unit that we
created
this code unit actually will send the
prompt that we created into the uh
playground actually what I'm
using I store this prompt into the blob
storage so I take the prompt send this
prompt to the Azure open AI
then I get the AI comment and then I
create a job queues so and to create a
job queue actually that's a normal
parsing of a Json that I expect
because I instructed the model about the
Json format that I expect to get and
here I get this part of this
Json
see that that's all the fields that we
instructed and here I just insert the
job queue
so here is my business Central with this
copilot chart
and let's see if I
if it works
run consolidation
report every Friday in the evening and
at the end of the month and 8 pm
yeah and we have our job queue scheduled
so here we have
this AI command
that we actually expected
and here we have a
two job cues
run on Fridays
at six
pm
and this at the end of the month
so that works yes
if I understood correctly you tell me
that if I can for example take all the
business Central documentation into the
chat you can directly do uh ask I can
ask anything
oh you know the magic has some
limitations
because if I will go here
into our
examples and let's say I will just copy
paste that
and provide more examples
and I will
submit it once again
you see
the model maximum contact length is four
thousand
tokens
so we can't actually add more
contents there
so we have this prompt limits
depending on the
model we use they're different but still
they exist we use here the GPT 3.5 which
has four thousand tokens limit
recently open AI announced a new 3.5
model with a 16
000 tokens
that's 16 000 tokens it's about 90 PDF
Pages file
so it's a lot but still how limitations
the gpt4 has 8
000 tokens and also 32 000 tokens but
depending on the you know token size
that you pay more also the latency will
be
worse or better
and you should remember that this
tokens limitations not only for the
input they are together for the input
and the output
so you should take that in mind as well
but what is a token actually
and the token is a small unit of text
that is used to represent a word or part
of the world so
Owen has a large language models were
trained on on the internet data
they actually split it a sentence into
the words words into the parts of the
words so in this part of the word tokens
so approximately one token is about four
characters
and um so and how we can like add more
knowledge to that
um the thing is uh the answer is
embeddings
and two
show you
what's embeddings are actually I
prepared a little bit another demo
so let's close it
so
this is a little bit of python code
what it does actually it I created them
a chart
that answers equations about the BC Tech
days
so if we run this
chart
so okay great to be here
I think
let's just copy that
so is there any session about judgpt
I'm sorry I don't know
so
um
this chart uses
embedding Vector database to store the
knowledge about the BC Tech days
now the storage is empty so it doesn't
know anything about BC Tech days
and
the storage actually is a cloud
Vector database
and
I will just
document about what is a vectors
so let's just want to show you that this
is a superbass.com
service this is a cloud Vector storage
database it's empty now
so
actually the
we we before we lived in a world of
keyword search the keyword search means
that
um
when you search something in Google it
indexed the website before and it
searched for the same word and give you
a result semantic search works a bit
other way so it when you search for the
king it also the word Keen is very
related to the word man
like the queen is aware related to the
word woman
um
yeah so London is related to England and
it builds this map of a relationship
between uh words
how we do that
so actually it converts words into the
vectors of numbers
and
Technically when you ask for the judge
GPT something it first converts your
input to the numbers then search for the
similar
Vector with the similar numbers in this
mapping Global mapping and then
[Music]
provide you a response
so it's and also the vector databases
actually they have
at least
of these vectors with the different
dimensions
and
the number of dimensions for the open AI
models is one thousand five hundred
32 I guess
uh
and that's actually the columns
and the rows
are the individual chunks of text
converted to the vectors
so
to show you that
um
what we're going to do now
we will take
we will actually take the BC Tech Days
event
website
we will load that into the chunk of text
and we will split this chunk of text and
save it into the our Vector database
so we will just run that
will take some time
so if we will look into the
take this website it's actually very
complicated to get some speakers we have
information about sessions
we have information about Antwerp how to
get here
many diff
icult stuff here
let's see
so we took like 15 seconds to
to get that describe the website and
store the convert everything to vectors
and store into our database so if we go
here
and
update we will see that we will have
how many of them I think about
oh yeah 200 11
vectors
so we have here the chunk of text
and we have here the embeddings
so the idea behind that is when the user
will ask for something
it will go to this Vector database
search for the by the semantic search
the knowledge that actually
answers the user question then take this
chunk of text put that into the prompt
and the large language model can answer
both of this information so we don't
need to put all the information to the
prompt how we did before when we can
just take the part of the knowledge that
relates to the question of the user
and um
so if we
let's say go here
ask once again
yeah there is our session here
let's
do other
type of questions
how to get to the conference
so it took it now go to our Vector
database find information related to the
question and put that into the prompt
and large one language model compatible
to answer on that question
um
okay like that
how to get to the conference for free
I didn't know that for every five full
conference tickets there is one more
free ticket
good
um
what beer is the best here
I don't know you don't know
ah the point is that's good not good not
good yeah the point is there's there is
no such information there on the website
about that so I thought maybe you can
help
to add
more knowledge to this database
so can you just scan this uh nice
QR code generated by
AI
and write your response
yeah so there is a simple form you can
just feel
providing some life hack
can you scan that
no
yeah someone yes someone yeah some
sometimes with
actually I have a
foreign
with the normal
okay oh I think it's enough
otherwise
someone scanned
just to receive some answers
yeah okay let's see I have this
home we have 44 responses
thank you
okay we can just take this so we can
just what we're going to do
um
we will open that in a Excel
where is my
so this is the
Excel I will just
grab it here
I'm going to rename it a little bit
so it will be not without without spaces
and what we're going to do next
we'll use this Excel to train to add to
convert that into the vector database
so we will just run this
and of course that doesn't work here
5x Okay so
name
should be
like this
no
document is empty
why it's empty
this right file please
come on it should work
we tested that before
okay sorry I think
Excel again it should work
I'm not sure why
we cannot see it
yeah okay sorry I think we can miss that
but yeah you got the idea that we can
just convert that uh to the interactors
into the vector database and ask some
questions
okay I think
this maybe while you're preparing
continue our session I should share this
is right ah yeah
sorry okay I will not do that no no okay
so uh in this first part we saw uh all
the main things about about related
about Ai and especially using not AI in
a simple way but using AI in a more
complex way uh how we should use AI in
Enterprise perspective and uh I'm
absolutely not a guru of machine
learning I don't come from this world
and when I embrace the AI word uh
sorry but this why is that
okay
I learned something embracing AI this
the first lesson that I learned is that
AI could be expensive and unpredictable
if not well used
so you should learn how to use AI
correctly
the first things that I learned is that
AI is not only hrgbt but it's much more
than just GPT AI can use can be used
with your own data not generally
speaking asking questions and receiving
general answers what I would like to
have with AI is using my own data and
chatting with my own data and receiving
my own response
I also learned that AI is not only
python when we talk about AI to when we
search things about AI we see tons of
pythons but I'm personally not coming
from the python world and what I would
like to do is using AI
without using python because I'm not a
python expert
and uh
the other things that normally I learned
is that to replace Developers
customer needs to describe what they
want as Dimitri said before if you don't
describe correctly what you want
AI gives responses that are not the
right response that you want
so
probably devs will have a long future
again because it's difficult to does
that
foreign
I also learn another thing that the most
common pattern
that we have in AI is this
so if we are you have out
because uh AI needs to work you need to
give a good prompt and if you want to
give a good response without a good
prompt and without a good data you don't
have a good response so that's the part
that you need to remember and the
quality of data reflects the quality of
the auto response that you have so if
you have good data and you want to chat
with data
you have a good response
so
what I would like to show now is that uh
other tools that permits you to do more
complex Fields with AI the first tool
that I want to present is the Azure open
AI on your data features its features
released two days ago
uh uh it's actually in public review and
permits you to chat with your data in
just sorry in just few clicks if Dimitri
can please switch okay to do that is
very easy
previously we saw that
uh we I I have created a deployed the
model so
my mouse doesn't work okay something
like that I have deployed different
models uh
uh in particular mode I create this
model using GPT 3 3.5
and uh
if you you create this model at your
Europa you deploy the model and then you
open the playground
now
you have uh the possibility to add your
data
from two days ago or not probably not on
every subscription now it's deployed by
step by step but you can add your data
yes in a preview and this is quite a
powerful feature because it permits you
to add a data source
and a data source can be on different
types of data source mainly
in our ah
speaking about business center uh
I think that is important is that you
have the iso blob storage
data source
and uh when you select the answerable
storage you can specify
an Azure blob storage instance where you
have your data like this and you need to
specify and activate an Azure cognitive
service instance simply just click on
the button and create the Azure
commission services this is needed in
order to automatically index the data
that you're giving input to your model
so I'm selecting my instance and I
select a container where I have placed
that the data the CSV data and I can
create an index
now I give a random layer like something
like that this is the index that the
engine will crawl my data creates the
index the vector database and then okay
start chatting when I have deployed that
I can simply click OK and deploy it's
works on my data
I don't do that because it takes some
time but when you have deployed that
you can also deploy this
you can chat with your data from here
but the interesting part is that you can
deploy this as a web application and
when you have deployed this as a web
application you have something like that
it's a web app running on azure
where you can also give user permissions
and something like that and in a
in in here you can accordingly to the
data that you have given in output in my
sample here I've given sales data so I
exported from Business Center
periodically the sales data says lines
say settings and so on and uh
with this app automatically created by
Azure I've done nothing
in code now I can write things like I
don't know can you
uh books at least they sales revenue for
uh
customer grouped
by
month
I don't know something like that
and uh
the users can chat with the data it
works this is I I repeat that this is a
public review actually not available for
everyone
it's not extremely stable so give that
the time to work uh as you can see
performances are not are not extremely
uh
our food especially if you have a lot of
data but it permits you to
chat with your data directly without
doing nothing
there are limitations there on that at
the moment you can only use from this
web app I hope that it will respond now
okay it is give me some data
normally it's much more performant but
it's giving some data so I I'm I'm not
to work on the data this is these are
coming from Business Center
I do nothing and done nothing and I can
type every type of query what is the I
don't know
the top sold item in the last month
something like that and
queries you can I can chat in this way
without doing uh
uh if it is not able to recognize
because you and you don't have uh
uh data is responding wrongly so it's a
first approach
without doing nothing to chat with your
own data
uh
but what I would like to do is something
more so this tool is quite absolutely
useful new
uh
I'm obviously not use that in real world
projects at the moment because it says
a starting point you can test with your
customer but it's not production already
in my opinion uh I would like something
to have something production already
and to answer the production radio in my
uh what
when I start embracing AI I have two
goals yeah in my mind the first is this
I want to suffer for my users from
Business Center to chat with their
business data
and the first goal was to give Mayo user
the possibility to for example embed
external documents or something like
that that they have in inside the
corporate and permitting them to chat
with these documents without searching
for files or something like that
so what I would like to do is
uh
something like this
uh we showed before that we have created
totally created controlled in inside
Business Center
uh and in this control thing that you
can place everywhere I placed it into
the so it says manager or Center for
example uh
I can go here I do the same question as
before so for example what is
uh the top
sold item
uh in the last month
I don't see
what they've right because there are
uh and the requisite sent to Azure open
AI
and I should receive
the response so I'm essays manager to to
do that I need to uh I don't know I
execute some reports or I need to go
into the say statistics uh uh I don't
know in this way it's quicker I'm
chatting and it's responding that the
top soldiers is a conference bundle and
so on that is one of my items that I had
in this uh business Central environment
but I can also do something more complex
like uh I don't know for example can you
create a table with the uh I don't know
the sales revenue
for customer
and requisite again is sent to Business
Center
and
uh if the prompt is good always
obviously
you should buy something that says a
sense
uh is giving the response in the table
format so I have it here a table
or customer for sales
uh
and it's much much more than executing
so I've never executed in a report to do
that in Business Center in a standard
way you need to do say statistic or
something like that here and chatting
with data so
what's their end of the use of that
uh previously and also this morning we
saw that in Business Center the article
unit
for using with Azure open AI this could
use this actually internal but we
probably open to everyone in the next
future
uh
I'm not used digital unit because there
are lots of limits later I will talk
about that so what I used immediately if
you can please go into the slides
quickly
what I've used is something external uh
later I will explain the reasons so uh
that one of the tool available that you
have today is the Azure open aisdk4.net
it's a library currently in beta that
term is used to have a raptor inside the
Azure open AI all the other Azure open
AI
you can connect to Azure open AI but
also to the standard open AI libraries
remember the display release so you need
to in order to see reacting from tools
like Visual Studio or Visual Studio code
you need to add the Prelude check
otherwise we don't see that
with this tool you can create some some
something more powerful so in my case
uh again sorry for the switch
in my case I creating a self-service
and Azure function
if someone don't know what the function
are throws back yeah throws yeah
tomorrow that's the session but okay I
create an Azure function in this Azure
fashion I use in the Azure open AI SDK
so I'm starting as a library and yeah
I've done exactly the same thing as
explained as before from Dimitri so what
this is done is simply reading my
question
and I also passing in this case the
index of data that I want to read
from my database Vector database and I'm
calling a prompt
so given the following data reading from
The Blob storage
from the vector database I'm calling my
Azure open AI SDK
uh
so I'm creating a completion
let us in mind the name of my model
and some parameters required by the
model
summer was previously explained uh
important is the temperature parameter
the temperature is normally a parameter
between zero and two and I have
temperature means that the model will
take more risk to give you the answer
so it depends if you want the model to
do random things
if you want to the model to strictly see
the data that you want take the
temperature lower
uh why I use this the Azure function and
not the business central unit because uh
sorry again I can do that okay uh
because uh there are some problems one
of the problem is this the Azure open AI
service quota limits
and the first problem that I when I put
this into Productions
the first problem that I am is what I've
written involved in the bottom of the
slides
the rate limit is totally different if
you create a request to have a
description for an item
probably if you have I don't know 100 of
users in your business Central
uh
in the worst case
you can have one handle of requests that
are maybe sold during the same time
because uh imagining that every user
creates a one Android User in the same
old items in the same times you have
that number of regular Mass if you start
using a chart with data so if you
integrate a chart inside your business
center and every user can chat with the
data requests are a lot could be a lot
and the first problem is that with the
with the code unit you cannot scale
the the standard unit you simply can
specify the model
and sending prompt and you can scale
what uh sorry I I'm not able to use that
what I
do in production
is something like that and what happens
in with external tools like the Azure
open AI SDK and the actual function is
that I can scale
I can create more instances of the Azure
open AI instance I can have a single
endpoint
where accordingly to the number of
requests okay redirect
the request to my Azure function and
this permits me to avoid the token limit
because
uh if I have 1000 Euro users I can
redirect this request to every
the other tool that uh sorry before this
other Tool uh if the meter came against
which
uh I want to quickly show this
uh another this is a web app using the
same tool as before
but in this case
uh but first I we can show the web app
this is the web app in this case I'm
also indexing PDF files
and this permits me to embed AI also in
the entire documentation that a company
have so so I can for example I I leave
the web app easy in order to understand
I can create an index in my Vector
database called Tech days
like
days
create an index
the index is created into my Vector
database and then I can uh here I can
chat with my data
and if I select this index so if I work
on the text there is this index that I
ask for example uh how many
oh sorry oh Manny license types
business Central
have
sent Eric with AE said no no because I
create an index on my Vector database
but the index is empty
if I do something like that
so I select my index take days
and I select a file like the business
center licenses guide
uh this tool is scrolling is uploading
the business center licenses guide
then it's extracting the contact of the
business center licenses guide
obviously the PDF should be well done
and then the PDF files is completed and
this is the the standard Microsoft
licenses guys so not my
so just to show is the standard with the
center licenses guide that you can
download from the banner site now like
if I
uh I go again with the chat and I
reselect my index and I do the same
question what no how many
license type license types
business Central Ave
now I should have response
it saved me that business center has
this type of licenses and it's also
providing me uh
a link
you can also do other that's that's only
a question that AI cannot response and
in this case what team members can do
also AI doesn't know what three members
can do but if I search for example what
uh
I don't know what types of permissions
or can the team member license
license for example yes
member license
it should give me an answer so uh
uh team member is not able but if I if I
uh if I write something the problem is
in the PDF Microsoft PDF has a table
with dots inside the
permissions and dots when you crawl the
PDF are not well done so much some
answers in the PDF files are retrieved
so this is just to say that we can also
embed
files
so well you was talking I just figured
out what was the problem with Excel file
there was some
extra lines so I just
um
took your responses also embed them
and now we have
the most
important question here what the beer is
the best here
we have an answer
okay okay conclusion yeah so
to conclude this uh some actions you
take to make your apps AI powered
so register on the Azure open AI or open
AI
then learn how prompts work experiment
with prompts in the playgrounds and
think what scenarios you can embed in
your extensions
and maybe one day will come from this
maybe through this
into something like this
so thank you very much
we have a type of questions I think yeah
we have questions
first microphone
hi hi uh I just want a simple thing to
use the co-pilot to allow me to program
faster
is it free can I try it out you know uh
copilot requires
a a a a license with the with a GitHub
account so you need to uh to have a
Guitar Pro account
uh copilot chat is actually in preview
so uh
uh you need The Insider version preview
version of Visual Studio code otherwise
it's not installable it's installable
instead on on the standard version of
visual studio uh uh the standard version
of visual studio so not Mr code here you
can install uh
copilot chart on the on the business
reports Pro uh account
up
uh I have a question could you give some
well maybe pointers what to add to the
copilot prompt for it to better
understand Al El language
so for the AL language
so in my experience I started with a
copilot a year ago
for their languages was bad
but
and then since more developed Al
developers started using that
at least me and AJ so we figure out that
uh it becomes better so
the my recommendation will be just start
using that just you know activate that
so you can it will learn from what
you're typing and uh if you
are in a uh inside of Al file it will
learn better how according from the code
that you already have and also a little
secret that it also use it use uh to
prediction not only the active file that
you open but also two or three files
that are open uh
in another tabs and also two or three
files that you opened before so
you have this context of the thing
you're working on right now and it will
give you better recommendations
okay
um when you say that your using this in
production
for chatting with your data uh are you
able to upload the data incrementally
to the to these files and what are the
limitations because if you try to ask
something for like a sales analysis and
so on it could be a lot of data there
and you have to refresh it from time to
time
so are you able to upload it
incrementally
yeah so it's up to you how you are going
to increment the data from for example
for the central queue service that I
built I index all the data once per day
so and add
more data there so but I have like a
separate script for that so that is
running let's take the data and put it
in the vector database so
is there any limit
like
one gigabyte like the amount of data
that you can use for your own
now if you if you use a vector database
I don't know the such limits you don't
have a limitation on the data that you
can index normally for example the the
business center data scenario I use the
blog storage as a uh as a index to take
the file and then store the file into a
vector database in develop storage uh I
don't know if you know that there's an
extension that the MBC to a DLS
extension determines you to export data
from business Central to uh storage via
features uh this creates Delta files for
uh
four files that you want to for example
you have modified every
modify from last day and you can crawl
that file into your vectors
and uh
it
uh permits you to create your indexes
incrementally and then you can
database
it's difficult to uh to have a large
amount of data to chat with a large
amount of data
that's why uh
the IL language enough only solely uh
at the moment I know your Italian guy
you can speak speaks
but we are asked to finish but thank you
very much for coming here and if you
have any questions
uh like you can ask us in you know
locally
