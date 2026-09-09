# Microsoft Presents: A brief introduction to the history of AI - from Deep Blue to Copilot

- **Source:** https://www.youtube.com/watch?v=CjTm5mqsQ8o
- **Video ID:** CjTm5mqsQ8o
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 42m23s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Hey, good afternoon. Um, so I realize
this is the session that stands between
you and some beer and some dinner. So I
try to make it as uh entertaining and uh
and interesting as possible. Uh so this
session um by the way about you know
getting secure in the cloud uh versus
onrem. Uh there's only one answer to
that. Uh you need to get to the cloud.
Uh if you're on prem you're going to get
hacked. It's just a question of time. Uh
I'm I'm I'm serious. This is getting,
you know, the pressure on security
getting increasingly high and it's
getting harder and harder for an
organization to get secure by themsel in
an on setting and you should really
leave that to uh you know the people who
know about it and you know as Ed and and
Omar showed you before there's so much
thing invested in the cloud for security
there's no way that you can you know
even expect to reach that level of
security. So get to the cloud. Um uh so
okay um in this session let's get back
to uh to AI now. Uh so this session I
just you know just a fair warning is
going it's going to be uh not tech
non-technical sessions. Um it's there's
not a lot of uh of coding in it and not
at all actually. But I think yeah okay
it's okay to leave.
Um um so so I I thought I wanted to talk
a little bit about AI in a broader
perspective. Uh I'm not even going to
talk very much about BC in that session.
I'll talk a little uh a little bit about
how we made agents. If you haven't
attended the session uh about origins by
Christian and Omar sorry and Christian
um
and and Erica you if you have seen that
session that's going to be kind of you
know very short repeat of that and if
you haven't that will give you a little
bit of insight in how we build agents uh
but I wanted to basically take a a step
back and and uh and and clarify a few
things around AI because everybody's is
talking about is going really really
fast. There's a lot of um you know
terminology out there. Uh and talking
about terminology I will start with
that. So I showed that slide uh already
I think last year at tech day. So you
raise your hand if you remember it had a
slide about technology.
That's fine. Nobody remembers it. That's
cool. Yeah you one people. So I I'll go
through it again because I think this is
important. So what is artificial
intelligence? Artificial intelligence is
a lot of things. you know we say AI
these days people are saying AI all the
time uh and using it in all sorts of you
know context and artificial intelligence
is actually an old science it's not new
and uh it started uh I think let me take
a look at my notes here uh I think the
uh if you look it up the the term AI was
first time coined by a guy called John
Makati at the domos conference in 1956
so that's how old the concept of
artificial intelligence is um in 1950
even before that before the term
artificial intelligence was used Alan
Turing we've considered the father of
computer science by many um imagine the
touring test you know he already back
then in 1950 he had this vision of
machines being you know uh as
intelligent as people and he devised you
probably heard of it the touring test
which is a test aiming at determining
whether you uh interacting with a
machine or a human. If you haven't seen
the movie, by the way, uh it's called
the imitation game. It's a pretty good
movie about the life of Alan Turing um
and specifically about his work on
cryptography during the war. Uh and then
in 1952 there was the first um machine
learning program a self-arning chess
program uh which was built by Arthur
Samuel
uh and in 1951 the first neural network
computer were um invented by or or you
know established by a couple of guys
called Marvin Minsky and in so um this
this is this is just to say artificial
intelligence is is not new. uh but then
it becomes really interesting uh in the
in the '9s because in the '9s uh there's
the first occurrence of what's called
machine learning. So what's machine
learning? uh the very first the very
first attempt of artificial intentation
there was mostly um rule based what we
call rulebased systems where you have
like basically a rule engine um and and
we're trying they were trying to with
this rule engine try to simulate what
what a human would be doing I don't
think there's much uh going on in that
area anymore but it's still considered
being part of artificial intelligence
and there was classic computer system
computer vision system uh already there
was people were trying to you know do
something with cameras and try to
recognize what's on pictures already
back then. Um but this was pretty much
everything was pretty much algorithmic
based. So somebody somewhere was read
writing algorithms pretty much like you
do today in traditional programming and
then uh in in the 90 in the 80s uh
machine learning appear. So the
difference with machine learning and um
and traditional algorithm algorithm u
based you actually don't write a program
in a traditional sense machine learning
is about you know as I'm sure you you've
heard having a lot of data um and you
have some data and trying to find
patterns and you know you know so you
typically you have a lot of data and you
know what the output should be uh so you
have a lot of input and you know what's
the right output it and you fit it to a
machine and let the machine determine
what the algorithm is. So you don't
write the algorithm but you train the
machine to figure out what the algorithm
is. And uh the magic in that is you know
if you have if you have a a not very
many data uh you know imagine a table
with certain number of columns if you
have two or three columns um then it's
pretty easy for a human to figure out
what the algorithm should be. You can
see kind of the pattern in it and with a
lot of if then else statement you can
kind of code this algorithm but as soon
as you have a large number you know
imagine you have very large number of
parameters also called features in
machine learning language like let's say
you have a hundreds of them and they all
vary and depending on this combination
of parameters you have a different
output then that becomes really really
hard for a human to actually
design the algorithm that would do that
and that's what machine learning does
that's the magic of machine learning,
right? So you train a model into
basically generating the algorithm and
then within machine learning there is
deep learning. So deep learning is even
more magical in that sense that with
machine learning traditional machine
learning which is not deep learning you
have kind of an idea of what the rules
are. Um and you kind of you know uh tell
the model this is this is how you should
build the algorithm. you don't tell the
what the algorithm but you you have some
rules right whereas in deep learning you
don't do any of that you have a neural
network you just tell the machine this
is the um this is the uh the output
that's expected and before I continue
with this terminology slide um I want to
do a a a kind of digression on this um
um if you haven't read that book um
there's a guy called Ray Solomon and he
was he was part of this company called
deep mind and he's wrote a book recently
called the next wave where he's talking
about AI and it's a really good book if
you if you um if you want to read if you
I really recommend you read it um and so
he's talking about he's talking about
his journey and and what they were doing
at deep mind uh they were they were
actually uh working a lot with neuronet
network and they were using games uh and
and and basically uh that was the era
after the the the chess game. So what
happened in history was the the chess
game was one of the first game that the
people who were researching artificial
intelligence used as a as a use case
because it was considered a pretty
complicated uh game right and there was
this you know this turning point where
um uh I don't remember the date but I
think I have it in my notes um in uh in
1997 Deep Blue which was a a a program
written by IBM actually beat one of the
world champion. Kasparov was the one of
the best player in the world at chess
and uh and it actually was not it was
not like a you know there was six games
and um and uh there was three draws and
two wins. So it was not like you know
it's just beat the the crap out of him.
So it was really a tight a tight race
between uh between the you know Kasparov
and um and uh and Deep Blue. Uh so when
when that was done uh when that was done
then the researchers they turned to they
turned to other problems because
actually at the same time computer and
computing power became you know more and
more available and cheaper and you could
have a lot of computing power and and
some of the ways that uh these chess al
machine learning chess games were
working they were using a lot of what
you could call brute force. They were
basically trying you know to calculate
all the possible combination and
determine what the best combination was.
And the thing with chess is that it
doesn't have uh that many combinations.
Chess has an estimated number of
combination of 10 to the potent of to
the exponent of
123. It's a pretty big number. You know
it's a one with 123 zeros but it's still
not very big you know compared to how
the computing power has evolved these
days. So using brute force be became you
know less and less uh interesting in
term of artificial intelligence and
that's why um that's why um researcher
turned to another game uh which is the
the game of go uh it's come from Asia
and this is the reason why it's
interesting is because the rules are
quite simple but the number of
combination is you know let me look at
my note is like way way bigger it's
estimated to be between 10 to the uh to
the power of 170 to 10 to the power 360.
So that's a difference of about 10 to
the power of 47. You know I know if you
can imagine this is really really big
numbers you start to be there where you
have a hard time to relate to that and
and clearly the brute force approach
doesn't work for these kind of games. So
what so getting back to deep mind and
what this company did they so they they
starting looking at these games and
starting looking at go but they didn't
start with go which is kind of
complicated they start with simpler game
like back in the 80s they looked at in
the '90s they look at video games like
breakout for example and um uh so if
you're not familiar with this game
that's a video game you have the you
know raet at the bottom and you have a
ball and uh you need you need to break
all the um all the bricks here by
sending the
uh and uh so so what Mustafa wrote in
his book is that there was two key
moments in his uh you know in his
journey working with AI and one was you
know when he was training
uh they were training that the model to
play that game and so he was it was
again he was you know deep learning so
the only thing they did the only thing
you do when you're deep learning like
this you say okay here here's the the
racket you can move it to the left or to
the
uh that's what you can do and your goal
is to maximize your score. That's all
that's all you tell the model and then
you let the model play. Uh and what
happens is that so the model will will
try moving randomly at the start and
score zero obviously because it will
miss the ball and then at probably at
some stage you know randomly it will hit
the ball and uh it will make a few
points you know uh then the model will
realize okay when I do that when I hit
the ball I make points. So what it's
going to do as next is going to try to
hit the ball more. Uh and of course it's
going to realize that okay I make more
points when I hit the ball and then you
you train it like this and u and and the
great thing about that kind of training
is that you can just let it run you it
doesn't require it's called unsupervised
training. You can just set it to run and
come back in a month and you know
eventually you'll have you'll have a
model right? So that's a you know that's
pretty practical way to do machine
learning and deep learning. But then
what happened uh was that what what they
figure out that this this model figured
out that actually if you keep hitting on
the on the side and create a corridor
here uh where you open all the bricks
here and send the ball behind then the
ball will go and hit all the bricks and
that was a really good strategy to make
a high score right so the model
consistently was trying to do that
because it figured out that was a good
strategy and the reason why you know
Mustafa Sulleman think that was a
turning point and a milestone in the
history of AI is because this strategy
if you asked a human who you know was an
advanced player of that game who has
played that game a lot they will tell
you oh yeah yeah we know about that
strategy we know about that that's
that's how you play the game that's how
you you try to get a high score you you
make a you make a hole in the side and
you send the ball behind so that what's
interesting about that is that in that
instance the model actually reach a
strategy which is the strategy that
human also had you know figured out,
right? So, which is pretty, you know,
significant when you think about it. And
another decisive moment was with Alph
Go. So, Alph Go was a again a model that
Deep Mind had the train to play this
game of Go and they went to I believe it
was Korea to compete against some of the
you know world champion in in Go. And
this is again these guys are really
really you know smart and and they train
a lot. this is like a sport and uh and
in Asia is really really big you know
there's like people commenting there's a
lot of you know audience and um and the
machine was so this model we're playing
against one of the world champion and
what happens there is so the the it's a
tournament so there's this old games and
the model won the first game um not so
surprising and then in the second game
there is the famous move 37 uh and and
you can look it up Everybody knows about
the uh the move 37. And what happened is
that in 37 moves of the game, um the
machine, the model made a move which
everybody thought was a stupid move. You
know, nobody understood why the model
did that and the the people, you know,
the commentators and the public, you
know, they all went, "Wow, that's it.
The model the model is just, you know,
made a mistake. It's going to lose." Uh
because it looks like really a a stupid
move. But then um the player who was one
of the you know world champion that
didn't think exactly that was such a
stupid move and he took a really long
time to play again to to respond to that
move and actually the story says he just
actually stood up and went and went out
and came back and it turned out you know
uh after 10 or something moves after
that turned out this move was really
really clever and the the model ended up
winning against that player. And the
reason why it's a interesting milestone,
too, is because in that instance, the
model actually figured out a strategy
that no human had thought about before.
That was kind of a new strategy. There's
a lot of strategy known in Go because
people are studying them. You know, it's
like in chess, people are starting these
strategies. And you know, for the first
time in history, a machine actually was,
you can say, clever, more clever than a
human.
Um so that was a you know that was a
discretion let's about this but I just
thought it was interesting to mention
this um the this this this thing which
historically had had some significance
in the world of AI. Um so let's get back
to the terminology. Uh so deep learning
uh deep learning you know getting you
know the model to the neural network to
again determine the algorithm just by uh
no based on data and just what expected
result and with no preset rule. Uh and
then within deep learning there's this
thing called generative AI. So that's
what everybody's talking about today.
And a lot of people today when they say
AI uh when we talk about AI they
actually mean generative AI. So
generative AI it's about just to be
clear as the name says it's about
producing new content for example images
text music. Uh so there are models you
know everybody you know is talking about
uh often about large language models
which are about generating text but
there's also as you know models to
generate images but there also models to
generate music text and music and all
sorts of things. Uh so this is
generative AI and and and again within
generative AI there's large language
model elements which is yet a subset of
um of generative AI.
uh so as you can see uh there's a lot of
things within AI and and even if today
large language have a you know a big
place on the scene uh the rest of the
eye is not is not dead like for example
you know uh uh when you talk about
self-driving cars you know we know that
there's a lot of AI in self-driving car
it's not generated AI you don't want you
don't want to generate new content right
you what gener you know self-driving
cars try to
like given a input like you know from a
camera or sensors try to determine what
to do with a brake uh you know the wheel
and the accelerator things like that but
you don't want it to be like creative
and generate some new things right so
this is not a generative AI problem but
it's still a very interesting and
relevant problem uh AI problem right
all right um so and and and yeah and I
need to say that uh then there's
Microsoft copilot uh just to confuse
everybody body. Uh there's this term uh
copilot that we use at Microsoft. Just
to be clear, uh copilot is a brand. It's
not a technology per se. So it's
basically an umbrella
u over a whole bunch of technologies
that we have at Microsoft, right? So we
have chat copilot, you know, we have
generative AI for pictures. It's all
comes under uh you know, agents. It all
comes under the the Microsoft Copilot
brand. But uh just to be clear, this is
not one particular technology as such.
It's just a brand name. So I hope that
clarifies uh a few things here.
All right. So let's talk about uh
language models uh now because this is
the obviously the talk of the town. This
is what everybody is talking about and
I'm going to talk about large language
models and small language models a
little bit here. Uh but first a few
examples of models and uh so I'm sure
you're familiar with some of these. So
there are models like um GPT4
uh it has 200 billion parameters. I'll
get back to what that means because you
might have heard about it. people talk
about excuse me about models in terms of
what size they have you know is that a
big model small model and what it means
is how many parameters they have and
I'll get back to what you know what what
that means uh so for mini is a reduced
version of um of uh of 40 it's only 8
billion parameters um and you have a
very very large model GPT45
it's one of the largest model available
today uh at least in the commercial
realm it has an estimated. So these
these numbers now you know past GPT40
they are more or less estimated because
uh OpenAI got a little bit secretive
about how many parameters they have in
their model. So so these these are not
quite public but there's a lot of people
you know estimating these things and and
you know it's just it just doesn't
matter whether it's five or 7 trillion
is just to have an idea of the magnitude
of these models. GBD45 is is a huge
model uh as you can see compared to the
other one and actually it's going I
think it's going to be retired by OpenAI
because it's just simply too expensive
uh to to run this model uh and and they
made so much progress with other type of
model um that um that they're not going
they're going to discontinue it GPD
GPT01 which is a reasoning model so it's
been specifically trained to be good at
reasoning
uh has 15 billion parameters. Uh and
then you have models like a 54 which is
a Microsoft model. It's a small model uh
with only 40 billion parameter. Uh and
something and then another model that
has been a lot in the news. I'm sure you
have heard is the coming from China is a
deepseek air1. It has 671 billion
parameters. Um so the the the the way uh
small small models are made uh no sorry
I need to point there. You can't see if
I pointed there. Uh so so the the trick
with making small models I I'll get back
to small models in in a in a minute but
the trick is you know so so I'm sure you
know one of the so what what's used to
train these models is the internet. So
you probably heard that that the
language model they trained on the old
internet. So first of all that's not
entirely true. Uh it's it's not like you
know you you take a model and and and
let it lose on the internet go and say
go and train right because there's a lot
of I mean simply because of the fact
that there's a lot of content on the
internet that you don't want your model
to train on you know and I don't need to
go into details but I'm sure if you go a
little bit on the internet you often
stumble across things that you don't
want to be you know you have part of
your training. So, so what what people
are doing when trend is model they take
basically a curated version of the
internet. So they remove something you
know uh things like you know uh that
could be you know uh hateful things that
with you know sexual content things you
know harmful things you know think with
racist content all these things are
curated and removed from from the
internet before these models are trained
luckily
uh and the idea with small language
model was that okay maybe we don't so
the idea was okay the internet contains
a lot of even if you curate it contains
also a lot of crap and a lot of you know
uh less quality content
So instead of instead of training on uh
everything, let's try to pick a subset
of uh of this training set which is a
good quality and train a model on that
and that's basically the principle
behind small language model. Uh so you
know the idea you know so the idea was
you take things like for textbooks,
Wikipedia, you know things with
relatively high uh quality content and
train this model on that and that allows
you to make models that are much smaller
and can run on uh smaller you know much
less hardware. I'll get back to that in
a second. Uh so what so I've been
talking about training and parameters
right and you've probably heard a lot
about this as well. Uh so what does that
mean? Um so let first of all let me say
it's very complicated. It's really a
science that um you know we should leave
to the the people who know what they're
doing right uh for for a small world you
know if you working with BC you know
there's enough you know work to do you
know don't don't go into training uh
that's way way too complicated uh but
but just to understand a little bit what
that means and and what these parameters
mean let's me make an analogy does
anybody know what that is
nobody okay that's a synthesizer from uh
I think from the ' 70s. Uh so you know
it's a before it was before the digital
era of synthesizer. So it's a it's an
musical instrument and and you have all
these buttons and it's all analog,
right? And you have all these button
which are supposed to be, you know,
you're supposed to be able to emulate
sounds from other instruments with that,
right? Uh horns and and violins and and
and and and
piano and stuff, right? Uh so and
imagine you want to produce you have
this idea of a sound in your head right
and you want to produce that particular
sound uh there's about 44
um you know button and uh and switches
on that uh on that synthesizer here
right and uh sorry and then um so you
will need to basically you will need to
tweak uh and adjust each of the button
to create until you reach the sound that
you want, right? If you have this idea
of a sound. So basically, and this is
pretty much the equivalent of having uh
40 parameter 44 parameters as an input
and you have a an output that is the one
you want to achieve. Right? So this is
training for this is one row of training
in your data. Right? And then you'll
have you know and then you'll repeat
that for another sound, right? another
outputs and you'll have to readjust all
the setting and this is what training is
and the analogy of the buttons are the
parameters. So when you talk about a a
model with 200 million parameters that
means there are 200 million buttons that
the training needs to adjust until you
get uh the expected output. So that's
basically what happening when it's it's
very very oversimplified but the the
principle of it is is remains uh remains
pretty much as I explain it here. So you
have these you know uh 200 billion or
something or 200 million parameters
right with that one output and you're
going to try all the combinations until
you get the output you want right and
then you repeat that for you know all
the rows you have in your in your data
right so this is what training does so
as you can imagine this is very computer
intensive and takes a long time right uh
just to give you a few example
uh
so Uh no I actually I get back to that
later. I have some examples of how long
time it takes to to to to train these
models. Um
this is about hard. So this this slide
is about hardware. uh because again as I
mentioned this this is very computer
intensive training these models and I'm
sure you have heard you know uh that
these uh these models they run on GPUs
uh which are originally graphical
processor unit but they there's not much
graphic going on in this so this is a
Nvidia H200 which is one I think one of
the most advanced GPU these days uh and
just to give you an idea on that this is
one GPU right uh it looks like this And
it has something like about 1,700 CUDA
cores. CUDA cores are you think about it
as these are processors which are meant
to run in a parallel architecture and
they are basically worker processor and
they are able to do a lot of operations
in parallel. Uh my laptop has 12 cores
just to you know for a comparison right
which is you know a good laptop. Uh and
there's 528 tensor cores. These are
other cores which are specialized for
training. So these are mostly activated
when you train models as I mentioned
before. Uh and then there's like 141 GB
memory. This is all in one chip, right?
Uh 141 GB memory on the chip as well.
There's something about latency between
the processor and the chip which are you
know relevant for how you know how how
you can do the training. It's kind of
you know very advanced. Um and then they
consume about 700 watt uh just one of
these right so this is one H200 right um
so models like GPT4
can requires 8 to 16 GPUs to of this of
these the one you know of the H200 to
run for a mini can actually run on one
on a single one it's actually possible
uh and so GPT4.5 as I mentioned is one
of the largest model that exists it
requires 24 to 48 uh GPUs to just to
run, right? Uh but small models like
GPT01 and 54, you can run them on one
GPU. And actually, if you have a decent
graphic card at home or you know,
Copilot Surface Plus uh with a a
built-in GPU, you can actually run this
model locally on your machine. They
don't run very fast compared to when you
use the cloud versions of them but they
do run and you can you know do simple
things like you know summarize this some
that you'll get you know you you'll get
an answer but uh it's not very it's not
very fast but it's possible
um okay so training cost um so how you
know how much does that cost to train a
model a large language model um so GPT
uh two which was the early model which
has 1.5 billion parameters uh costed
about $50,000 in training. So that's the
you know that's the GPU time you're
using you know the power and and and the
GPUs. Uh Megatron Touring which is
another model. Uh it's not an open my
model. It's a pretty large model. Uh it
has 530 billion parameters. The cost was
$11 million to train that model. and um
GPD from so from GPT 3.5 I think and
after that again openAI became a little
bit secretive about how much training
time they use and of the cost of it but
of course uh you know when things get
get out on the internet so there are
some estimates GP4 was trained for about
100 days so you know as I mentioned
before you go and let this model train
and that took about 100 days about 3
months to train this model and the
estimated hardware utiliz hardware
utilization cost was about $63 million.
Uh so it's just to say you know training
a model is is is a kind of a complicated
affair and it's also very expensive and
it requires some infrastructures that
most people don't have. Um so now uh
let's look a little bit at small
language models because I think they are
you know everybody's talking about large
language models LLMs but small language
models are also you know I think you
know really relevant and interesting for
us uh in in the context of business
central. So they're much cheaper
obviously, right? Uh they are much
faster. So if you if you use them for
simple tasks, they they will respond
much faster than large language models.
Uh they're great for many tasks. Of
course, if you have a very complicated
sorry complicated task that requires a
lot of uh reasoning, uh they might they
might fall short, but if it's just do
something like summarizing or something
like that, they they are really good at
that. Uh and so examples of again
example of small small models are 4.1
million uh 54 uh and they are much much
cheaper per token.
So uh let's talk a little bit about uh
tokens because you might have heard uh
the terms as well uh people talk about
tokens and how many tokens there is. So
so tokens are um you know basically
prompts are and replies are handled as
tokens. Um and uh you can almost say
that uh a word maps to a token. So one
word, one token almost. It's not quite
true, but uh as a rule of thumb, it's
it's it's you know pretty much uh uh
what it is. Some some words don't don't.
Some words requires more than one token.
Um and uh for models like uh Asia open
models you if you go directly to the
model uh I'm not talking about what we
announced this morning at the keynote uh
about agents we have a different pricing
model but if you just you know go to
Azure create a uh you know deploy model
an openi as open eye model you are going
to pay per uh token consumption
and there's a different in input tokens
and output tokens output tokens meaning
the reply I you get for LLM are much
more expensive than input tokens. Uh if
you want to know a little bit, so I have
a quick very quick demo here what uh
tokens look like. Uh there is this page
on um on uh OpenAI on the OpenAI website
uh which is a tokenizer. So you can
enter a you know a text here. This is
let me type this is a test and it will
it will show you know you can see here
in the underneath show you how does that
get tokenized
where's my laser here you go how it gets
tokenized here so there is uh five
tokens in this uh in this uh um in this
sentence right uh and uh actually these
tokens are
converted to ids to numbers and what
happened after that is a lot of you know
matrix calculation with this with this
token that generate actually the output.
Um so let me show you another
example. If I add a this is if I write
this is un predictable right you can see
here a couple of interesting things is
that this and this here are not the same
tokens uh for whatever reason don't ask
me why unpredictable for example has two
tokens here as you can see it's even
even though it's if it's one word uh and
there even sometime very long word they
tend to be broken down into three tokens
so if you want to see how many tokens
there is in your prompt
You can use this this tool. It will tell
you exactly how many tokens uh you are
going to pay for in your uh in your
prompt in your input prompt. And if you
take some sample answer that will tell
you also how many uh output prompt there
is output there is in your prompt. Let
me get back to my presentation here.
Yeah. All right. So um
uh so so the some example of pricing and
these prices are per million tokens. Um
so GPT40 you going to pay $250 for 1
million token inputs and $10 for output.
There's a factor four between uh the
replies you get the the output tokens
and input token. It's roughly you know
the same for all models. there's roughly
a factor four between uh input and
output. So if you you know if you think
about it um if you when you do your
prompt engineering actually you can have
a if you have a much um much bigger
input prompt and a and a smaller output
prompt it's actually a better a better
deal. So in some in some scenario it
might be interesting to have you know a
a larger prom as input and just have a
you know just answer true or false uh
and then you'll get a very small uh you
know output token very few output tokens
which is you know going to save you some
money. So there's some things to you
know comp you can compromise with here.
So for mini uh is a lot cheaper again
that's small language model I was
mentioning before they are much cheaper
only 15 cents and and 60 cent for output
tokens uh 01 so we're getting into the
more expensive model now 01 which is the
reasoning model cost $15 per tok per
input token $60 per output tokens and
whether 01 mini cost only $ 350 uh and
$13 as a as an output but you as you can
see GPT45 is really really expensive
cost $75
for uh for the 1 million input tokens
and $150 for um uh for output tokens. So
very expensive model. So you should only
use it if uh you need something very
very complex. Actually most of the tasks
today you know even if you have a quite
complex tasks model like 01 and the new
reasoning model which is relatively
cheaper are pretty good at solving a lot
of complex problem these days.
Uh okay, a few words about agents. Um
so, uh agents are the new thing. You
know, we we talked a lot about agents
this morning at the keynote. There was
this great session with Christian
Esteban and uh this afternoon if you
haven't seen it. Um maybe you can see
the recording. Uh so agents are you know
obviously con based and constructed and
developed on top of generative AI and
what's specific with them is that they
they are you know they can perform a
task autonomous autonomously
uh and they're different from AI
assistant and chatbot because they
really have a you know they have a
purpose they have a goal uh and they are
meant to do something very specific uh
and usually they can perform this task
through multi-steps
And they're also capable of autonomous
decision. They have agency, you know. Um
and and I have a few minutes left and I
want to use that to you give you a
little bit of insight. Uh if you haven't
seen the presentation I was referring to
on how we build uh our agent platform in
BC. Uh so basically what we're doing is
that we are the principle of it for the
sales auto agent for example that we are
we have 11 different prompts in in our
platform. Uh and you can see they have
we do a lot of things. We do we analyze
the message we summarize the steps uh we
execute the task we have a task action
prompt we gen reply and so forth right
there's a loop detection prompt which is
trying to detect whether the the agent
is running in a loop and doing the same
thing all the time but the the the heart
of the agent is a task execution
and what what what it is basically I
mean the rest is kind of you know the
mechanics of the agent it's important as
well but really the heart of it and the
the promp we spend the most time on I
would argue is a task execution prompt
and what does it do? Um uh yeah and
there's some uh review request and and
context validation and there's some
orchestration around this right so this
task execution uh the principle of it is
here is a page you know we show the
agent basically a a representation of
the page you are on it's a JSON
representation but it's just a
technicality could be HTML right and um
we show all the fields on the page all
the actions and um we we give the a
bunch of of functions that the the the
agent can call. It's basically a
function calling uh prompt and we say
okay you can navigate to that p to
another page you can click on these
actions you can fill data in these
fields these are basically the things
you can do uh there's a few more but
more this is more or less what we say
and we ask so we ask in that prompt then
we ask them okay given that page and
given the task which is for example
doing a sales order and given that you
have this possible action what action
should I take next so If you're on the
roll center, if you start on the roll
center, the agent will probably go,
okay, uh, what's on the roll center?
What is this action called sales order?
I probably want to go there. So, it's
going to say, okay, click on sales
order. And then, so we navigate to the
sales order page and then there's a list
of sales order. And again, we do the
same thing. We show the page, do all the
sales order and show it to uh to the
agent uh to the LM and and with all the
possible action and ask again, okay, now
that's the page. So, what do I do now?
And the agent will probably reply, okay,
I'm creating I want to create a new
sales quote or sales order. Just click
on the new button and so forth, right?
So, here's an example of, you know, a
little bit under the hood of that works.
Uh, so this is basically the page
description as you can see here. So,
it's it's not a complete one, but just
to give you an idea it looks like. So it
has I know it's a little bit you know
unclear but basically what it says you
know this is basically the role center.
Uh so you have some some actions here
you know it says for examples order
description view the existing sales
order sales quote these are the action
that the the agent sees and all the
fields and so forth. So that's what we
basically show to uh to the agent and we
we tell the agent here are the able
function the available function. So you
can end the task, you can draft a reply
if you know if you know it's time to
write a mail or you can um you know
request assistant, request review, set
field value and so on and so forth. So
these are the possible action that uh
the uh agent can take and then the LM
replies you know that's the very
beginning of the flow. Okay, navigate to
this node which is you know uh the name
contacts because I want to find that
person with that contact. So that's
basically you know the principle of it.
Uh so this is how agent work. Uh and uh
yeah and so that's that's that's how the
platform works but as you can see it's
very powerful because it's doing
everything through the UI. So I thought
I wanted to give you a little bit of
insight on how that works. I can see I'm
running out of time. So thank you very
much for attending the session. We won't
have time for Q&A but just know feel
free to uh you know catch me at the at
the booth or you know anywhere under
conference. I hope you enjoy the
session. Thank you very much for
attending.
