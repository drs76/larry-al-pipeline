# Copilot is just a fancy autocomplete…

- **Source:** https://www.youtube.com/watch?v=zTejuQzYAb8
- **Video ID:** zTejuQzYAb8
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 92m16s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, welcome to today's
morning session. Please welcome on stage
our next speaker, Tina Stichic.
Welcome. It's it's great to be here
again. I mean, I know I did a session
yesterday, but this this is the one this
is the one that I'm I'm I'm very excited
to to present to all of you. I knew
already back in November that I want to
talk about this topic. And I'll tell you
what's what happened in November. But I
was talking about this topic already
earlier in the year. But the tech days
kind of this audience this audience
pushes me to to go deeper to go further.
Uh so to all of you welcome to copilot
is just a fancy autocomplete or a
session where I try to convince you that
it's not just a fancy autocomplete
anymore.
Usually I would start my sessions by
explaining a little bit around why do I
care about this topic? How did it come
to be? And yes, my name is Tina Stage.
I'm an architect with uh with Companion.
I've been an MVP for about a year now.
But I wanted to start today's session
slightly differently.
I want to take you through like a
timeline of how this this whole story
started for me. And it all started in
October of 21 when GitHub Copilot was
initially released. Now, of course, this
was not when the story started for me.
In October of 21, that's when I I just
barely relocated to Lithuania from
Slovenia. But it was kind of cool to see
that we've had this tool for about four
years now already. The story for me
started slightly later in December of
22. That's when I saw in my mailbox that
I accepted my trial subscription back in
December of 22. This was just a fancy
autocomplete. It did only work for
mature languages like C or TypeScript or
Python. And the way it worked was that
you had to write some comment lines in
your code and then when you would move
to the next line, it would propose the
implementation of a procedure to you.
Now, everything changed again in April
of 23. That's when I put my money where
my mouth is and I spent the full $10 on
the GitHub copilot license because by
April of 23, it was still just a fancy
autocomplete, but it started working for
AL quite well. By that point, it allowed
me to be a bit more efficient with what
I do and it was already bringing me some
fun uh while while I was coding. So, I
thought I said it's fully worth the the
$10 price.
But then in December of 23, I stopped
paying for the copilot license and I
even got a refund from GitHub because
the the billing period was was shorter.
Why did I stop paying for it? By
December of 23, I was able to convince
our organization that this is no longer
just a tool for enthusiasts, but that
all AL developers can benefit from
GitHub Copilot and can be more efficient
with it. So, our organization started
paying for everyone's license, which
means I no longer had to pay for my own.
In December of 23, there was another
announcement.
GitHub Copilot Chat was announced and no
one cared, not even me, because Copilot
Chat was essentially just chat GPT, but
they brought it into VS Code. That was
not exactly groundbreaking.
What was groundbreaking is what they
announced later in November of 24,
co-pilot edits. Now, that's something I
really want to talk about today. But I
didn't get to know about co-pilot edits
from a blog post like this one. I got to
know about co-pilot edits at an event
called direction zia where I was
speaking to a speaker in in the hallway
a guy I think a lot of you will
recognize veo he was telling me that
he's using something called claude with
something called edits and that all you
have to do is shoot a prompt to it and
it starts generating code for you and
that it works and I knew that as soon as
I come home from Vienna I have to try
and play out with it and I did I first
tried it out with with like C and Python
and that was groundbreaking. You really
just you you type a sentence of what I
want and some of what you want and
something else generates the code for
you. And then I tried it with AL and it
worked for AL and that's how I knew in
November already that this this is the
topic I want to speak about at TAG days.
And that's what brings us to June of 25
to BC tag days. When you get accepted as
a speaker to BC Tech Days, Luke, the the
organizer, Luke, he sends an email with
all the tips, what you should do, what
you shouldn't do. One of the things
that's in that email is thinking about
life coding. Think again. Watching
someone debug in silence is less
thrilling than it sounds. Use copy paste
or pre-loaded files for smooth sailing.
Well, I'm sorry, Luke, but we're going
to do a lot of VIP uh not VIP well VIP
coding as well, but live coding today.
But I'm not going to be the one writing
most of that code.
I don't really have a like a structure
for today's talk. What I do have is a
bunch of examples of how I use GitHub
Copilot for AL work. But on top of all
of these examples, I also found quite a
couple of interesting pictures when I
was preparing. Um, here's one of them.
And this one also kind of captures what
I'm trying to pass on to you. I think
for too long we've been looking at AI as
something that takes in inputs then
something magical happens and then we
get some outputs. I want to explain to
you how the scope pilot actually work
because what I've noticed is when I talk
to developers when they see how things
work they're more eager to try the tools
out themselves. but also the more you
are going to realize how copilot works,
the better suggestions you're going to
get out of them in the end.
So if I just quickly do now explain the
the project background, I want to
explain what the codebase is going to be
about which we'll be looking into for
most of the session. What I've been
doing for the most part last year was
working with a non-b businessiness
central ISV, an ISV that has a an
inventory predictions backend service.
Uh but they don't they don't have any AL
developers. So they asked us to build a
library app for them so that when AL
developers want to integrate with their
backend service, they could do so in an
easier way. Now all of you, you actually
know what a library app is. Think of a
scenario where you want to integrate
with Asia blob storage. If we would like
to integrate with Asia blob storage, we
would usually create a code unit where
you create a procedure to get the access
token to list all blobs to put the file
to get the file to rename the file. But
if you think about it, this is not the
code you write when you integrate with
Asia blob storage.
this is you just use one code unit the
ABS blob client and you initialize that
code unit and then you get the the file
out of it right so that's the same
approach we tried to take with that uh
non-B businessiness central ISV so
instead of developers having to worry
about what's in the JSON payload what
kind of fields should be in there
instead all they have to do is populate
a certain temporary table and then you
pass that temporary table into a certain
code unit which does all of the rest
does the authentication with the backend
service does the uh the logging the
error handling
and with that let's go to VS code now
so this is essentially the project I was
talking about the backend service has a
lot of different APIs uh and for each of
those endpoints we have to create a
temporary table for it and then the the
code unit that handles all of
So you can imagine if the back end
introduces a new endpoint something like
brands that you can send the brands of
your items so it can use that to well
calculate the inventory fluctuations.
Well we need to create a new table for
brands and how I would usually start
with that is that I would create a new
file call it brand table
and I would use a snippet. I would give
it a number. I would give it a name.
And what you will notice is that as soon
as you have GitHub copilot, when you
move into the next line, it proposes
some code for you. Right? This is the
the fancy autocomplete. You click tab to
accept it all or my preferred way is to
control hold down control and with the
right arrow key, I can select part of it
parts of it and then maybe it's not text
250, it's text 300. And I can press tab
to accept all the rest.
Every time I do the fancy autocomplete
demo, it goes differently. That's
because GitHub Copilot gets updates like
every two weeks. And if I was doing this
session back in April, there would be
one big tip that I would like that I
would share with all of you, which is
change the model that's powering
completions.
The way you would do that is by going
here to this little arrow key next to
the uh copilot icon. You would go to
configure code completions and change
completions model. In April, there were
still two models here. GPT3.5
which was the default and then GPT40
which is which is the new better model
for it.
Right?
And in April, I was still saying go
switch to 40 because it is better. It is
better for AL. But uh now it become
became the new default. But I still
wanted to show you where do you switch
these completions model models and
because Microsoft I believe soon will
introduce another model based on the
GPT4.1
model. And again that model won't be the
default and we will first have to switch
it around switch around to it.
Okay. Anyway, let's remove all of these
useless parts here from the
uh snippet. Let me also remove the
fields over here.
Okay,
you can see here that copilot kind of
knows exactly what I would like to
complete. It knows that I would want a
brand ID, a code, a description. How
does it know what kind of suggestions I
would want to have here?
Well, it's because I have the category
table open over here and it sees ah so
for categories, this is how the table
structure looks like. Uh these are the
properties, these are the fields,
category ID, code, description, and
probably you want the same thing for
brands.
That is a very important point. Copilot
looks at up to four additional open tabs
for context which it sends to the
language model which produces the the
final completion that you see on the
screen. So
close down your tabs. Don't have more
than four additional open tabs open uh
besides what you're working on because
if you're working with like 30 tabs open
likely you don't know which ones are
relevant to the changes that you're
making. So how can copilot? So kind of
the first tip is get very comfortable
with right-clicking the tabs and then
closing closing others closing to the
right closing saved closing all. For me
it was a bit of a habit. I was one of
the the people who have 30 plus open
tabs. But as soon as I started closing
more and more of them down, my
suggestions became much clearer, much
better.
Usually I would just tell people look
stick to four open tabs and we would
move on. But since this is tag days I
wanted to go a bit deeper. How do I know
that it only takes four open tabs as
additional context? It's not documented
anywhere.
The way I found out about that is again
from VCO. He was telling me that he was
using something called Fiddler.
Some of you might recognize um or might
know what Fiddler is. Essentially,
Fiddler is a tool that allows me to
intercept the HTTP calls before they
leave my machine. Right? So, what what I
was doing was I set up Fiddler and then
I was writing code in VS Code, but
before that prompt left my machine to go
to the GitHub servers, I was able to
intercept it in Fiddler and see what's
in that prompt. what kind of messages
are going to the language model.
I won't be showing you how do you set up
Fiddler and how do you intercept these
these requests because let me show you
how my screen looked like when I was
preparing for for the session.
It was quite messy. There's a lot of
prompts that are going uh going back and
forth between your machine and the
GitHub server. So instead what I did is
I pulled these prompts out and I stored
them into a separate separate repository
over here. So I'll be kind of guiding
you through what goes into the language
model when it's creating the the
completions for you.
For that I have a more simple repository
over here. Imagine that you're starting
from scratch, right? You want to create
a new new table, new entity, something
like a shareholder. When you would write
out table shareholder and then move on
to the next line, what would go to the
to the GitHub server is an HTTP request
like this. It would have a prompt and
we're going to dive deeper into what
kind of prompts are there, how do the
prompts change. Uh, but it has some
other priorities like max tokens and
temperature. And one of the interesting
things for me was that it actually
thinks we're writing the code in Pearl.
I don't know why, but Pearl seems to be
the identified language of our of our
code.
When you send that when when you're
creating that shareholder table and you
move on to the next line, this is the
prompt that gets sent. So the path this
shareholder table and then the contents
of your file and this is all that's used
to uh create the proposal of what AL
code should be accepted into the table.
So that's the the very start. Now let's
take a look at what happens if we move a
little bit further where we have already
implemented the table itself but now we
would like to start working on the
shareholder card. So I've got the table
in place. I start writing page 50,100.
The prompt that gets sent in this case
is this one shareholder card page. So,
so the name of the file and then the
contents because copilot will never look
into the files that are closed.
And here I only had the shareholder card
open and that's why Copilot doesn't
actually see what's in the table. So if
I open the table and if I open the card,
this is what the prompt would look like.
Now
it would again start with the name of
the shareholder card. But then it would
add this part compare this snippet from
shareholder table AL and the contents of
the shareholder table and then finally
the contents of the current file that
I'm editing. And that's how it would
know, oh maybe these are the fields from
this table that you would like to have
on your page.
If we move a bit further once our
project kind of grows and we would have
like the shareholder list open the
shareholder card the shareholder table
and on the dividend for example if we
move to the next line how does it get
this suggestion
the prompt would look something like
this dividend table al and then compare
this snippet from the shareholder list
the contents of the shareholder list
compare this snippet from the
shareholder card, the contents of the
shareholder card. Compare the snippet
from the shareholder table, the contents
of the table, and then the the contents
of the dividend table. And then this is
what's used to to create the the
suggestions. But what if we start
opening more things up? What happens
then? So I'm going to open up all sorts
of tabs. And let's say for example that
now I want to create a new page called
company
meeting.
uh card.page.al,
right? How would the prompt look like in
this case where I now have tons of tabs
open?
If I scroll up, company meeting card
page AL and then compare this with the
shareholder list, compare this with the
dividend list, compare this with the
company meeting list, compare this with
the board member list, and then the
contents of my current file. So if you
have 30 tabs open, it doesn't matter.
It's going to take four and it's going
to take four at random. It doesn't
really know which ones are relevant.
It's just going to take four of them and
boom, that's part of our prompt. Now, so
if we kind of wrap that into a couple of
things to remember when you're dealing
with the fancy autocomplete,
it's first what does get sent to the
model. It's always the context from the
current file, the file that you're
editing. file name will be included as
many lines before and after the current
position as it will fit in the context
window. But the selection of lines from
within your file is already random. So
if you're editing something in like a
management code unit that has thousands
of lines, it won't take the whole
management code unit, just some random
lines before your cursor and some random
lines after your cursor.
it will send additional files but only
if the token limit is not exceeded. The
token limit is 8,192
tokens. Right? So again, if all of the
token limit is already used by this the
the context that was sent from the
management file, then it won't even look
at your additional additional tabs.
It will take the files if they have been
active or edited and only if they're
open. The selection of those tabs is
random. And like we saw, no more than
four files are sent with the prompt. On
the other hand, what will Copilot never
do? It will never consider or look into
the files that are closed. It will never
remember previous request responses. So
every completion is separate from the
previous one. It doesn't analyze code in
any way. and it never collaborates with
the current language server or compiler
which means if you have a warning on the
line before copilot doesn't actually
know about that because it doesn't talk
to the compiler.
So kind of in a nutshell it's a random
selection of a subset of the current
editing context. The last two slides uh
I took them from from VCO's
presentation. Uh so you know I've I've
learned a lot from Viko when when I was
reading his blogs uh before I even knew
the guy but I also learned a lot from
him when it comes to you know how do you
do presentations so I do consider him a
little bit of of my mentor. So even
though he's not here this year to
present at BC days well a little bit of
him is here with us. But let's get back
to to our brands. you know everything
that I've talked about that's still just
the fancy autocomplete and the title of
the session says that copilot is more
than just the fancy autocomplete.
So let's not talk about the fancy
autocomplete anymore.
What I do want to talk about is what
happens when you click this copilot logo
over here.
When you click it, this pane on the
right pops open and initially it's going
to be on this ask mode. This is the the
copilot chat. I was talking about the
chat GPT but in VS code. And what you
could do with it is for example
something like what does this file do,
right? And after a couple of seconds
it's going to say that this is the
table. This is its purpose. This these
are the key characteristics.
This is not what I use uh copilot chat
for. Later I'll share some examples of
how do I use copilot chat but this is
the the boring parts. This is not the
groundbreaking part of of copilot. The
the interesting part the one I really
want to talk about is not in the ask
mode but in the edit mode. So let's
switch to edit and it's going to say
that we're changing the chat mode and we
have to start a new session. Yes.
So edits, you can think of edits
just like the the the chat mode, but
with chat mode, you talk about your
files, about your code. Edits can
actually go in and modify your files.
And if you are going to be using edits,
the very first thing you should do as AL
developers is go to the model selector
over here and choose one of the cloud
models. Claude, Sonnet 3.5, 3.7, Sonnet
4. I don't know what it is with the
cloud models, but they're so so so much
better for AL code. It's it's it's
crazy. You might you might not see cloud
models here. If that's the case, you
have to first enable them in your GitHub
settings. Now, now mind you, this is
GitHub settings, not VS Code settings.
For that, you have to go to
github.com/s/copilot/features.
And if you're buying your own license,
you will be able to enable or disable
the features here on your own. If your
organization is buying the license for
you, then your licenses administr your
organization's
administrator will have to come in and
enable these. I don't really have an
argument why you wouldn't enable all of
them, but in case you don't want to,
here's the three that I absolutely would
have enabled.
Enthropic cloud 3.5, Enthropic Cloud 37,
and Anthropic Claude Sonnet 4 because
these CL cloud models are just so much
better for AL than anything else.
As as soon as you have them enabled, you
will be you will see them in your model
selector.
Now, why are edits so much better? In my
opinion, part of it is because we can
use these claw models that know how to
write AL. But the second part is because
with edits you can take control of your
context.
We just spent 10 minutes talking about
how do you set up the context that is
going to be set to autocomplete. And we
talked about how it takes some files at
random. With edits, you take control of
the context. If I want the language
model to look at the brand table, I can
pull in the brand table. If I wanted to
see the category table, I pull in the
category table. And these are the only
two files that the language model will
see. I can control what the language
model sees. And then I can give it a
prompt like create the brand table
similar to category table.
Add brand ID code and description. And
you shoot that off. Copilot thinks for a
moment and then says, "Okay, here's the
step-by-step solution of what I'm going
to do. I'm going to create the table and
these are going to be the fields." and
then it generates the edit.
Now, it will mostly do a good job, but
it will almost always mess up the object
IDs. No one likes object IDs, not even
Copilot. But that's not really a problem
because I can fix that quite quickly on
my own.
If I like this table, I can keep it. But
if I don't, I can keep iterating on it.
I can say for example uh description
should be 350 and it should have onv
validate
with test field code.
So copilot again thinks of a
step-by-step solution for it and then
says okay I'm going to change the
description. I'm going to add the
onvalidate trigger again. It goes
through the whole file and makes these
changes
and then I can keep that. And the first
part of my assignment is done. I could
already create this table with the fancy
autocomplete, right? You saw the
suggestions were quite good. I could
just tap tap tap through it and it would
be enough. But here with edits, I have
to do even less and it's even faster.
The next thing that we have to do is
create these code units, these API
handlers.
If I just briefly explain what these
handlers do. So here we can see an API
handler for the category endpoint. It
has this send procedure which takes in
the category temporary table and then
with the data in this table it goes into
generate JSON where it adds to the JSON
payload all the properties from the
table. So the category ID code is active
and so on. On top of creating the JSON
payload for the certain endpoint,
it also assigns the correct endpoint to
our HTTP request and assigns some query
parameters, but those I'm not going to
get into and then sends everything off
to this communications management. This
is the code unit that handles the
authentication and the logging and the
retry and the error handling.
So, we've got this one ready for
categories, but now we need to create it
for brands.
One thing I would really suggest to all
of you is when you're using copilot
edits, when you're done with one single
logical step, start a new session by
clicking the plus over here.
Why? These language models, they have a
certain context window. Now, the new
models have quite a huge context window.
It's above 100,000 tokens for most
models. But what I've noticed is first
if you throw more context into the
language model, it's going to take more
time to process it, but also the
accuracy seems to kind of go down. So I
prefer to keep my kind of chat lengths
as short as possible. When I'm done with
a certain step, I move on and I start a
new session.
I could ask edits, hey, create me the
brand API handler code unit. And it
would create the file somewhere. In my
experience, especially with the
multiroot workspaces, it doesn't always
do a good job of placing it in the right
folder. So, my workflow has been that I
create the new file
brand API handler code,
but I'll let AI fill it in. So, I can
now pull in the brand API handler, the
category API handler, and I'll pull in
the brand table so it knows which fields
are in there. And I'm gonna shoot off a
prompt. Create the brand API handler
similar to category API handler.
And while copilot is working on this
code unit, I want to show you another
interesting picture that I found. Uh so
I often get this question, why does
copilot work so much better for mature
languages like C or Python? Even
yesterday during the meet session there
was a question why is it not so good for
AL and I found this picture on Reddit
which was quite amusing to me which is
which trained co-pilot on your code
that's why it sucks.
This is this is maybe not exactly the
correct answer. The correct answer is C
just has so much more open source code.
That means there was so much more code
that the models were were were trained
on. with AL we don't have that much open
source code but maybe if we want to have
better models in the future we kind of
have to rethink that and we do have to
open source more of our own code but it
was also kind of interesting to see this
perspective that yeah maybe it sucks
because our code sucks
on our code unit now
brand API handler of course again it
messed up the object ID I'm just going
to fix that manually but if we look
through the rest it now creates the
brand API handler which takes in the
brand uh records. It generates the
payload for the brand table with only
the fields that were in the brand table.
It even recognized that description
should only be added if the text is not
blank. So the payload is successfully
added. The end point is then added. It
looks okay.
But you could argue here that okay, but
this is now just kind of a fancy copy
paste and it is. That's exactly how we
worked on this project before Copilot. A
developer had to take an existing code
unit, copy it, paste it, and then change
some things around. But when I was a
code reviewer here, here's two things
that most of developers forgot to do. Of
course, they knew they have to change to
a different record, that they have to
modify the generate JSON procedure, but
usually they forgot to update the brand,
so the the end point. And even more
commonly, they forgot to update the
documentation,
right? Because it's something small,
nothing the compiler will will complain
about. With Copilot, Copilot kind of
knows that it has to pay attention to
these little things. So, you could say
it's a fancy copy paste, but it's a good
copy paste. I'll take it.
Okay. The next demo I could show you
here is that I can take this brand. Uh
uh so I can take this table, I can take
this code unit, I could throw in all of
my permission sets and that and ask
Copilot, can you add the permission
sets? And it would do that, but that to
me would be a bit of a boring demo. So
instead, I want to talk about how it
handles tests
on our project. For each of these
endpoints, we also created the automated
tests for it. So if I briefly explain
how these tests look for the category
API, we've got three tests. We check if
the payload is created correctly. We
check if the end point is created
correctly and we check if the query
parameters have been assigned correctly.
So if we just check these steps over
here, we first mock the client sender
because we don't want to actually send
the request to the back end.
We create a random number of categories
and then we use the API handler to send
it off and in the end we assert if the
request body was created correctly or or
not.
If I show you the endpoint test, it's
more or less the same thing. Mocking the
client sender, creating a category,
then sending it off with the API handler
and then asserting the endpoint that was
used in that request. So these are the
tests that we have for the categories.
We need these kind of tests for brands.
Now I'm going to take the same approach
of creating a new file.
Brand API tests code unit al.
I'm going to start a new session again
and I'm going to pull in the brand API
tests. I'm going to pull in the category
API tests. I'm gonna add the brand API
handler and I'm going to add the brand
table.
I've used four different approaches of
how you can pull context in here.
Anything you think should work does
work. You pull it from the side. You
pull it from the top. You use the button
here. You can just start typing with
hashtag. All of the ways how you can get
context into your working set. But take
control of your context. You know what
you're trying to modify. you know where
existing code lies. Put all of that to
the language model so it knows how to
best create your completions.
Now I can give it a prompt.
Create brand tests similar to category
tests.
And while Copilot is working on the
tests, I'm going to switch to a
different repository to show you a
couple of small quality of life features
that I really appreciate with GitHub
Copilot.
The first one is one that one of the
developers in our company who doesn't
work with AL said that they are willing
to pay the full price just for this tiny
feature alone.
It's the generate commit messages.
Whatever you have in the stage changes
here in this pane. When you click
generate commit messages, copilot
produces a commit message. It's going to
do a good job when you have a few files
there. It doesn't do a good job anymore
when you add 10 or 15 files to the stage
changes. In my opinion, it becomes too
verbose. It explains too much. So kind
of my my rule of thumb is if I was going
to write a meaningful commit message,
I'm going to write a meaningful commit
message. If I was going to write
something like fix fix bug, fix PR
comment, fix test, that's not a good
commit message. And that's when I'll
just let AI to generate it for me and
I'll shoot that off because it's going
to be better for me and it's going to be
better for anyone coming after me.
So that's one kind of tiny co-pilot
feature. The other one is used for
naming things and renaming things.
You know that if you want to rename a
procedure or a variable, you go to it,
you click F2, and this is where you
would change the name. But half a second
later, because of GitHub Copilot, I get
four suggestions. Set unit of measure
code, modify unit of measure code,
refresh unit of measure code. Of course,
update unit of measure code. Here, the
name is good. I don't need to rename it.
But if I want to rename it, here's how I
would get some ideas of how it could be
renamed.
This is also how I use co-pilot chat.
Sometimes, especially the more junior
developers, they struggle with coming up
with good procedure names. So when I'm
doing the code review, sometimes I see
something that's a bit off, but I don't
have a clear idea of how we could name
it better. That's when I check out into
their branch. I navigate to that funky
looking procedure. I select it and then
I go to the ask mode of copilot chat and
I say this looks
off. Uh can you give me some procedure
name suggestions?
Notice one thing. What was used as
context here? Only the item table from
the line 3455 to 3464.
exactly the lines that we selected. It
doesn't need the full item table. So if
you select part of the code, that's the
only thing that's going to be used when
you're talking to copilot chat. And a
few moments later, it's going to suggest
some of the more descript more
descriptive options. And I can use some
of these suggestions to put them into
the the pull request and say, "Hey,
maybe some of these would make more
sense."
Okay, those were like two quality of
life features. But now let's go back to
check on our tests
again. Object ID not good. Let's change
that.
But the rest, if we look at it, what it
did, it again mogged the client sender.
Okay, great. It creates a random number
of brands. Now it uses the brand API
handler to send everything off and then
it asserts the request body. exactly the
test that I need.
Why did it know how to create a test
here? Well, it's because the brand
functionality is very similar to the
category functionality. And for for
category functionality, we already have
tests. So, writing tests for brands was
quite simple. If we think that we can
now throw our legacy management code
units into Copilot and ask for tests,
we're not going to get good tests out of
it. Because if your code is not
testable, you no amount of co-pilot is
going to help you write tests for it.
Vehicle session uh throughout the year
this year was all about how can you get
copilot to write tests for functionality
that's completely fresh that hasn't been
tested before. And the answer is well
it's something that he has been
preaching for the past four years
actually. You need testable code. Your
code needs to be solid. Your procedures
need to be small and do one thing. You
need to use interfaces to decouple the
code apart because when your code is
solid, your tests are going to look very
similar to the tests you would write in
in C for example. And there's billions
of C tests that the models were trained
on. So if we want to get better results
from C-pilot, our code should be solid.
But not only for C-pilot, it should also
be solid because we get the benefits out
of it.
Usually when I would be doing this
session, this is where I would kind kind
of start slowing down, stop with the
coding examples. But because this is tag
days, I said we need to go further. We
need to go deeper. So today we're also
going to look into the third mode of
GitHub copilot, which is the agent mode.
So, let me switch to the agent mode over
here
and let's undo everything we've been
doing for the past 40 minutes.
Think of agent like this. If we said
edits are like copilot chat, but they
can edit the files for us. Well, agent
is like edits, but we don't have to feed
it all of the context, all of the
information because an agent has access
to tools.
I can show you that once I switch to the
agent mode, I have this option of tools
over here. And these are all of the
tools that the agent has access to out
of the box. It can reference relevant
file chunks, symbols, and other
information. It can find references,
definitions and other usages of symbols.
It can check errors for a particular
file. Get divs of changed files. Get the
active terminal selection. The active
terminals less run command. Right? An
agent can decide, ooh, I might need an
additional file. Let me look through
your codebase if there's something else
that's relevant.
So with an agent, what we can do is I'm
going to copy the public documentation
of this brand API and I'm going to say
add
this brand API to the library app.
It's similar to category. Let me just
undo the typo here.
Here's the docs.
Just a second.
There we go. And I'm going to shoot that
off. And now the agent is going to take
some time to work through this
assignment. It's going to check the
documentation. Then it's going to do all
the different searching and figuring out
what it has to do. And while it's doing
that, I want to spend this time talking
a little bit more about how can you get
the best results out of the agent mode.
But for that, I want to first switch
into our PowerPoint.
So if we come back to to our point
first,
brands were able to be created by the
copilot edits because they were very
similar to categories. Does that mean AI
can only generate AL code when we show
it AL code?
No, it can also generate AL code from
scratch. Now, how did I kind of stumble
onto that? It was when I was preparing
for a session we did with Waldo a couple
of months ago. It was on the topic of
Power Platform. Waldo was talking about
Power Platform uh about when should you
use Power Platform if you're a BC
partner. And one of the slides that I
had there was that you should use Power
Automate to simplify non-critical
integrations
something like let's say we want to
connect business central with teams
right we absolutely could do that in AL
we can create the team setup table and
the team setup page and a code unit with
the get access token procedure and the
code and the procedure with the send
channel message and a procedure that
handles these HTTP headers. We could do
that
or we could add two boxes in Power
Automate. When something happens in BC,
send a team's channel message. Right?
And when I was preparing this slide, I
was thinking to myself, wait, but now we
have agent mode. Does my point still
stand that we should use Power Automate
because writing AL code would take too
long.
And I tried using cursor. Now I will be
talking more about what is cursor, how
does it compare to to VS Code a little
bit later, but for now just think of
this as a different flavor of VS Code
plus GitHub copilot. It looks more or
less the same and it has the same AI
screen here on the right side. And what
I gave to cursor in agent mode was this
prompt. Create a setup page for an
integration with teams. Add a page.
Extend the customer list page with an
action. create a code unit. U if there
are any credentials needed, add that to
the setup table.
Within about a minute, the agent created
the folder, the source folder over here
because I had nothing. And then it
created the team setup table for me. It
created the page. It created the page
where you would type in the message that
you would send to teams. It created the
code unit with all of the integration
logic. And then it even created the page
extension and added these actions to the
customer list. So I think my point that
we should use automate because AL code
uh would take too long to write does not
maybe stand anymore. But what does stand
is the point that AI can write AL code
from scratch. This project had nothing
in it. It was an empty project and I
said create me an integration and this
is what it did.
Now is this code perfect?
No, it's not. If we look at the code
unit, like why do I need the trigger
section, an empty trigger section here?
Do I really need to have all of these
variables as globals?
Probably not. I would think most of
these could be locals. But this agent
gives me a starting point. I don't have
to start from zero. But then to make
this code good, well, of course, I have
to invest some time to make it better.
I started using this prompt of create a
setup page for integration with teams
yada yada yada. I started to use that as
my own personal benchmark. Whenever
there's a new model coming out, a new
mode coming coming out. So whenever I'm
trying to compare what VS codes does
versus what cursor does, I always give
it this prompt to create an integration
and then I kind of compare the results.
So I tried to do the same with the agent
mode in VS code with GitHub copilot. If
we look at the prompt, it's the same
prompt as before. But actually here I
started it with this boost this prompt.
Before I talk about what does boost this
prompt do, we first have to talk about
kind of the the importance of prompt
engineering
because if you write a bad prompt,
you're going to get a bad completion. If
you write a good prompt, you're going to
get a good completion.
So, I'm going to right now do the
similar demo that I've done on the how
to be a prompt engineer session that
I've done earlier in the year. Has
anyone seen that uh session?
a few of you. Okay. So, so you kind of
know what's happening but the rest u let
me let me show you what I have
in that session.
I
start with this little example which is
trying to highlight to people that these
machines they're not some super smart
machines that understand our problems
that understand our questions but
they're just dumb computers calculating
probabilities and then choosing
whichever word sounds next. So I've
built myself this probab token
probability visualizer. Think of this as
CHD GPT, but we're kind of looking under
the hood and I've got more available
options here like temperature and max
tokens. And the way I would do a demo
there at the how to be a prompt engineer
is that I would start with a session uh
with a sentence. Today is a good day.
Let's go to A. But now before I let AI
finish this sentence for me, I want to
hear some of you. How would you complete
this sentence, Natalie? Today's a good
day. How would you complete this
sentence? Let's go to an ice cream bar.
To an ice cream bar. Okay, good choice.
Today's a good day. Let's go to a
pool. Pool. Okay. And today's a good
day. Let's go to a
What's your choice?
Let's go to a pub. To a pub. Okay, so
three different ways to complete this
sentence. All three make sense, right?
You cannot say that one is more correct
than the other one. Let's see how AI
would like to complete this sentence.
Today's a good day. Let's go to a a
beach. But let me show you one thing. If
I hover over the word beach, that's just
one of the words the model could choose
from. It could choose the word park. It
could choose the word party, cafe. Good.
The model doesn't really understand that
today is a good day. It just knows that
if the sentence starts with today's a
good day, it usually completes with the
word park.
Now, how does the model choose which
word to go for, a safe word or a risky
word? That's all based on temperature.
So temperature one means that the model
can sometimes go for a risky word,
something that had a low probability and
something it can go for a safe word,
something that had a high probability.
So if we move the temperature all the
way down to zero and if I remove this
completion over here
and I generate it again,
notice that most of the words here are
now yellowish or greenish, right? All of
them are the highest probability words
at that point. And even the words that
are kind of redish are still the words
that had the highest probability.
So the temperature is how the model
chooses between these available words.
But here's another thing. How do we
impact which words even are available
here?
Well, let me show you what happens if we
modify our prompt a little bit. I'm
going to say, "I just bought a new
swimsuit."
So,
you just bought a new swimsuit. Today's
a good day. Where would you like to go?
Beach. The beach, right? The beach makes
more sense. We wouldn't buy a new
swimsuit and then go to the mountains.
So, let's see. If we bought a new
swimsuit, and today's a good day,
the model would like to go to a pool
party. Now words like pool, beach,
water, swimming, these kind of words
make more sense, right? So, and I just
wanted to highlight that a good prompt
has a lot of impact in you getting a
good completion out of it. And how does
that all kind of tie back to what we saw
in Visual Studio Code?
I've started my usual prompt with boost
this prompt. And what does this do?
it adds a certain action to the agent
which says I'll boost this prompt first
to make it more detailed. So it takes in
my let's call it casual prompt which I
just kind of typed in and it's first
creating it into a far more structured
prompt. Let's create the setup page
configuration, design the team setup,
add the necessary validation, include
test connection, then let's move on to
page extensions, then let's move on to
integration logic. So, it took my casual
prompt and it added all of this
structure to it to turn it into a good
prompt.
But how do you get this capability?
You need an extension called, let me
make this a little bit bigger, prompt
boost.
When you have this extension installed,
you can start your prompts with boost
this prompt and it will modify the
prompt for you first. But you don't only
have to use this within the agent pane
over here.
When you're working with GitHub Copilot,
you can create some of the prompts that
you would maybe like to reuse multiple
times. You put them in this
Github/prompts
uh uh folder. And for example, here I
have an example of a prompt which gives
it instructions how to create
documentation. So if I modified four or
five files and I would like to quickly
generate some documentation which I
would add to the pull request
description, I would pull all of the
necessary files into my working set over
here. And then when I click slash,
you're going to get these saved prompts
available here. So the slashgenerate
docs that's the name of the prompt that
I've saved here. But that's kind of the
side point I wanted to show here. What
you can also do is create a placeholder.
And with a placeholder you can paste
your you can write your casual prompt in
here. And with the extension you then
get this button boost prompt. And in a
couple of seconds, it's going to take my
casual prompt and turn it into something
that has more structure. So, let's see
what it does for the integration with
Teams. There we go. It took my simple
prompt and turned it into something
better. You can, of course, modify this
further. I don't, for example, care
about the security considerations right
now. I can remove that. But this is all
just to show you how you can take your
your simple prompts into something
better because a lot of us we don't
really have experience with prompt
engineering.
So just remember that a good prompt
means a good completion. A bad prompt
means a bad completion. And the prompt
boost extension is kind of here to help
bridge this gap.
So with good prompts we're going to get
good results. But there's also another
problem with AI and agents. I have a
different demo for that.
We're going to go to our lovely chat
GPT. But but before I show you this one,
I'm again going to ask one of you to to
play a game with me.
Think of a word. I'll try to guess that
word. Okay. So, you've got five seconds.
You've got the word. Okay. Is it book?
No. Is it library?
No. Is it hospital? No.
Okay, I give up. What's the word? The
word soccer. Soccer. Uh, which word did
you choose? Soccer.
Say again. Soccer. Soccer. Okay. Okay.
Uh, okay. Okay. So when I asked you to
repeat the word that you chose, you kind
of knew it because you chose the word
when I gave you the task and you kind of
knew this is the word you chose up here.
I wanted to play this game live with
Edgpt, but it only works in like 62% of
cases. So I didn't want to risk it. So
I'm going to show you what I did
yesterday. I played the same game. Think
of a word and I'll try to guess what it
is. Okay, let's go. Book. Nope, not a
book. Beer. Tempting, but no, not beer
either. Okay, beach. Still not getting
warmer. It's something you can feel, but
not touch.
Okay, I give up. What is it? It was
hope. As if I was ever going to guess
that. But here's what you can do with
Chad GPT. You can edit your message and
you will basically just send the same
message again to Chad GPT. So, it was
hope, right? Except then it was freedom
and then it was nostalgia. So, I mean,
what word was it? I told you to pick a
word up here, but in the end, it was
just, you know, producing more words,
more words, more words. And that's
that's kind of the problem with these
with these AI models, right? You're
going to you're going to use agent mode.
It's going to create some AL code for
you, but it's not going to do a perfect
job. It might name the files the wrong
way. It might name the procedures the
wrong way. It might order the variables
the wrong way. So, you're going to
continue prompting it, hey, can you
change the the variable order? Can you
fix the file namings, all of these
things, but at some point, you're going
to start a new session and the agent is
going to forget everything about what
you just talked about and it's going to
make the same mistakes again because it
doesn't have any memory.
But that's something that we can fix in
VS Code with these files called copilot
instructions markdown.
these copilot instructions. Markdown,
these are the files that are going to
get appended every time you send a
question to AI. So if I say create an
integration with teams, it's going to
first append everything that I have in
the copilot instructions. So I use this
file as memory. And if I show you what
do I have in here, if we go a bit
through it. So I don't like my object
names to be longer than 30. We cannot
have them longer than 30.
I want all of the procedures to have
brackets event subscribers. I don't want
to have quotes here
variable definitions. This is how I want
my my variable ordering.
Al specific guidelines. I do not want to
see implicit parameters on these record
operations. I want to see explicit
parameters. JSON handling. For example,
we just recently got the capability to
use get text, get in integer, get
boolean on the JSON object. But because
these MA models have a learning kind of
cutoff date before the release of the
latest AL language, it doesn't know
about these additional JSON handling
parts. So it kept trying to do the JSON
object.get.
But I use the memory file to tell it,
no, look, this is the new feature we
have. This is what you can use.
So kind of remember that when you're
when you're going to be working with AI
and it's going to start creating the
mistakes and you're going to be fixing
the mistakes, remember to add things to
your copilot instructions.mmd because
that's how it's going to remember to not
make the same mistakes next time.
I'm going to share my copilot
instructions. I have not been blogging a
lot this year because the conference
season was very wild. Uh but once we
complete the the BC Tech Days event, I'm
going to get back into it. I'm going to
share what I have and of course you can
use that but also contribute uh maybe we
could make one of these files as like a
community project and we could all add
our rules to it u which could be used as
memory.
Okay, now let's go check on our agent
that was working on brands. Where is
that one?
Oh,
it got stuck at some point.
Still, I think it did most of the work
that I wanted to show you. We can still
go through the first part.
So, the agent, what it did is it fetched
the documentation.
Then because I told it that this API is
very similar similar to category API, it
went to check the codebase for anything
related to categories and it it pulled
all of these files on its own.
Then it got enough information and it
started creating the files just like we
did before. The brand table, the brand
API handler, the brand API tests, even
the enum had to be modified. Then it
went in to look for permission sets.
That's the next thing it has to add it.
I didn't put permission sets into my
initial prompt, but I had it in my
co-pilot instructions, right? That was
part of it that it should always look
into existing permission sets and modify
them. So, it modified the the permission
sets that we're using here. Now, in this
next part, I see that it's trying to
look for
if there's anything related to brands
already to to check for that. It's going
to try to to do some more work, but
essentially it already completed the
parts that I wanted to show you. The
brand table, it looks exactly like we've
done it before with edits. The API
handler, it looks exactly as before when
we created the code unit with edits.
Just that this time we also have the
permission sets and here the API tests
also the way we've implemented them.
So, let me stop this agent. You've done
enough.
Should I be worried if an agent can do
all of that?
I don't think so. Because why did the
agent know how to build the brands with
a such a such a simple prompt? Well,
it's because brands are very similar to
categories. If you think about it, this
task to to support the brand API in our
library app, that's a boring task. You
take some of the things that existed and
you modify them a little and that's the
the job completed. developer doesn't
really want to do that. We want to do
the interesting parts. We want to do the
problem solving. So if agents are going
to take care of the boring work, I would
say go ahead, let the agent take care of
these kind of tasks. On the other side,
we saw that agents can start the work
from scratch, right? It created the
team's integration, but the team's
integration wasn't good. But then you
and I, the the experienced developers,
we're going to take that starting point
and turn it into something that's
maintainable, something that's testable.
However, we don't have to start from
scratch. So, in my opinion, like these
agents, they're awesome. They're going
to take the boring work. They're going
to give us starting points where we have
nothing. But for everything in the
middle, for the like the complex problem
solving, that's where it's still a
developer's job to do the things. And
that's why in my my opinion is actually
that agent is nice but edits are the
cool feature because edits won't go into
the files that I haven't specified and
try to change something with agent. I
often get frustrated because I say let's
modify this code unit and this table and
then it starts modifying a readme file
and create some documentation and then
it finds something there and something
there like no code unit and table that's
what we want to edit and I can do that
with edits because I can control the
context. So take control of your context
with edits.
The idea that agents are going to
replace 70% of us in my opinion that's
just kind of marketing
Okay,
the next section that I want to talk
about is VS Code plus GitHub versus
cursor.
Why are we talking about a new
development environment now? What gives?
Like what's the difference? Should we
all switch? Do we have to go for cursor?
What's the difference?
Well, here's my take on it.
VS Code is a product that was well
developed for for years, right? Commit,
commit, commit, commit, commit. At some
point, a group of people decided, we
kind of like how VS Code looks here, but
we want to put more focus into it when
it comes to AI related features. And
that became cursor. Cursor is a fork of
VS Code, just that they've put much more
focus into how the AI parts of this
development environment work.
Should you all go for cursor? No. I
would say if you are not buying a
license for copilot or not buying a
license for cursor, then do take a look
into cursor and what it can do for you
because the way I see these two products
is that cursor is always kind of like
two steps behind GitHub copilot and
GitHub copilot is catching up. I've been
using both of them side by side for the
past seven months and honestly cursor
does something awesome and then GitHub
copilot gets an update and then cursor
gets an update and GitHub copilot gets
an update. So don't worry about your
FOMO like it shouldn't exist. You're not
missing out on anything if you're not
using cursor but it is it is slightly
better.
The way I would compare the two is, you
know, people ask me which one do you
prefer, GitHub Copilot or Cursor? And
it's similar to if you would have kids
and they ask you, hey, which one's your
favorite? Is GitHub copilot your
favorite? Is cursor your favorite? And
of course, you have to be the
responsible parent. No, I love you. I
love you, GitHub Copilot. I love you
cursor. But then as soon as one is out
of the picture, I prefer cursor. And
it's by a lot.
But uh honestly throughout the seven
months the situation was just kind of
constantly switching. They really are
neck and neck. However, I do kind of
prefer curs cursor a little bit. So in
this next part I do want to show you my
kind of favorite four things about
cursor which make it stand out from
GitHub copilot. But you will also see
that it's not that big of a deal. So if
your organization is already buying a
co-pilot license for you, don't worry
about cursor.
Of course, we're going to look at
another team's integration. Uh this time
I was using this prompt to evaluate the
uh what was it the cloud for sonnet
model. So I gave it this prompt and as
it went through
it created the same objects we've
already been looking at. So uh tables,
pages, code units, page extensions. But
at some point I wasn't happy.
So I started complaining. I said, "Yo, I
actually don't like page x 50,100. I
want name of the object. I want the type
of the object, right?" And then it went
in and it deleted all of the old files,
recreated all of the new files. Fine.
But I wasn't okay with that. I
complained more. I said string
substitute number should always use a
label variable instead of hard-coded
text. It should be local and it should
have a comment property explaining the
placeholders.
Fine. Agent picks that up and goes
further. Replaces all of the hard-coded
texts with variables.
Goes on, goes on, goes on, goes on.
And then I complained again. Where is
it? Here it is. I said only use begin
end to enclose compound statements
otherwise we get that warning of why do
we have only one statement within within
begin end.
So it was it was fixing that as well and
we already talked about this right I
should put all of these rules into my
memory.
Here's one cool thing about uh cursor.
What you can do with cursor after you've
had your uh discussion with it, you can
do a slash
generate cursor rules,
right? And what this will do, I won't be
executing that because it takes too
long. I've already done it this morning.
When you execute generate cursor rules,
it's going to based on your conversation
about AL development best practices,
it's going to create comprehensive
cursor rules. So the equivalent of
copilot instructions but for cursor and
it's going to place them here in the
cursor rules uh folder. So if I show you
one of these, let's say label best
practices based on the conversation we
had uh with with the agent mode, it
created this memory file for me. And now
it's a bit long of course uh but I could
just take some of the parts from here
and move them to my main copilot
instructions file if I was using a
GitHub copilot or just create I prefer
to keep one big memory file uh with
these kind of rules.
Additional thing that I very much prefer
in cursor is that these rules file
files.
They can have the type manual which is
the same as our generate docs uh prompt
we saw earlier. Something that I
manually have to invoke whenever I want
these rules to be applied.
We can also have always same as copilot
instructions.mmd. Whatever is set to
always will always be applied on top of
the prompt you sent to cursor.
But they have one more option. Oh, two
more options that this one was not here
yet before. Auto attached file pattern
matches. I can specify some rules that
should only be applied whenever I'm
dealing with tests, whenever I'm dealing
with pages, whenever I'm dealing with
integrations, right? Then I can have
different rules that are going to be
applied depending on which files I'm
actually trying to edit. And this is
something that I very much look forward
to in GitHub copilot and I hope it gets
added soon.
Let's check this fourth one though.
Agent requested. This this was not here
last week. Description of the task. This
rule is helpful for right. So you could
give it a description and then the agent
when it sees this description, it would
pick it up and use it as it's going
through the task. The agent can see this
description and decide to read the full
rule if it wants it. Yeah, I guess
that's that's what the agent requested
type is.
Okay. Another thing that I love about
cursor is
the fact that
if you're working in a more mature
language like PowerShell or TypeScript,
something that gives the output into the
terminal, what you can do is when you
click in the terminal, you have this add
to chat button. And if I click this,
it's going to automatically append these
lines from the terminal into my window
over here, lines 466 to 471. And I can
just say something like fix it, right?
And it will go and see the error and
then try to fix my PowerShell script to
to fix that error. In GitHub Copilot, I
still kind of have to copy the the
contents of the terminal and move that
manually.
The last one uh I want to show you is
something called next edit suggestions.
But for that I think I first have to
reload this window because I'm not
seeing my my models.
Let me quickly do that.
Oh, it's because it was set to auto.
Yeah. Um okay. So next edit suggestions.
Next edit suggestions are an evolution
of the fancy autocomplete. We talked
about fancy autocomplete and how it can
propose code that you can accept when
you move into the into the next line.
But the problem with fancy autocomplete
is that it only works when you're
standing in a new line or at the end of
an existing line. Now what next added
suggestions can do is something like
this. if it will work.
I think I have to wait for the objects
to load.
I shouldn't have uh reset my my window,
but
okay. So, this is the fancy
autocomplete. I'm creating a an error
that no test lines are found. If I click
tab, it I can accept that line. But next
edit suggestions, what they do is that
as soon as I was done with this label,
it proposed this icon here. Tab to jump
here. The only thing I have to do is
click tab and it's going to propose the
next edit. So it moved my cursor down
here and now it proposes maybe this is
the code you would like to change. I
click tab again and I'm done. I have to
remove the begin end but I didn't have
to click anywhere else because the next
edit suggestions already jumped to the
next line that I should edit and it also
can do something let's say stupid like
if I rename a variable of course you
would do that with F2 but as soon as
I've renamed it again tab to jump here
okay I'll tab then it proposes that
maybe you would like to add the two
number here and the two the number two
here and all I have to do is prep press
tab and it renamed both of these
variables at the same time. So next edit
suggestions that's the powerful
evolution of the fancy autocomplete. And
this also works in VS Code.
In VS Code, if you navigate to settings,
you simply search for next edit
suggestions and you can enable them
here, right? But I just kind of prefer
the way it was implemented in cursor.
That's why I was showing it. uh in
cursor.
I also prefer the model selector in
cursor.
This is the same model selector we saw
in VS Code. Well, similar to it. If I
click here to add models
and view all models, you have a lot of
different models available in cursor.
But that's not the point. Uh you also
have quite a selection available in
GitHub copilot. What I like about it is
that I can disable the models that I
never use. I never use 04 uh mini or I
never use deepseek to generate AL code.
I use these models and these models I
keep enabled and then my model selector
here is much cleaner and I can only
select the models that I like to work
with instead of the way it works in
uh in copilot where I have all of the
models available to me always present
here.
Okay. So, I want to start slowing down
and show you just one more set of coding
examples before we return to the slides
because I do still have some slides I
want to show you. And that's going to be
here.
Copilot edits are going to do an amazing
job for modifying files. An agent is
going to do an amazing job to to modify
your files if your files are not too
big.
In my experience, anything above 500
lines becomes a pain. Honestly, I try to
keep my files under 300 lines to get the
best the f the best performance out of
copilot edits. But we have also kind of
adopted a lot of legacy novision files,
those management code units that have
thousands of lines. So, what are we
going to do there? If you try to use
edits with a file that has thousands of
lines of code, it's going to take a long
time to get through everything and it's
sometimes going to do a wrong edit in
the first part, even though that's not
even where I want to make my changes.
But that's where the inline copilot
comes in to save the day. The inline
copilot is what happens when you click
control I. Right now, I'm in the this
item table which has more than 4,000
lines of code. If I would give copilot
edits a prompt like um if no is empty
then exit instead of error. It would
take so long to come to the line 2955
to modify the check documents and
probably it would also make some wrong
edits above or maybe in the bottom part
like it it wouldn't do a good job. But
in line copilot first here you can also
set the model which you would like to
use. So choose claude.
But the cool thing about inline is that
it only works in the selection. Right?
I've selected this procedure. Inline
copilot is only going to do edits within
this selection. Now it still is taking a
bit longer than I would want to, but at
least it it completed the request in
about 5 seconds. Edits would go on for
about a minute to do maybe something.
The problem with inline copilot,
however, is that we don't have control
of the context. So if you're using the
inline copilot, you're back to the four
open tabs rule.
I've got two more examples of the inline
copilot,
both of which are in the terminal.
So in the terminal, the first way how I
use the inline copilot, which you can
get through the same control I is that
sometimes I know of command lines, but I
don't really know how to invoke those
command lines. recently that was the
case with the interactive rebase. I know
what interactive rebase is. I know what
interactive rebase does but I don't
really know how to invoke interactive
rebase. So what I was trying with
copilot is do interactive rebase last
three commits and then two seconds later
I get my my command and how it's invoked
and I can either run it directly or I
can insert it and maybe change to five
commits if I want to. Right? So inline
copilot can help you with remembering
these commands that you maybe forgot
about.
The second cool thing which I use the
copilot in the terminal for is small
powershell scripts.
I kind of can write PowerShell scripts.
But what I was trying to do I think a
couple of months ago was clean up one of
my containers. I wanted to remove all of
my demo apps that I've published up
there. So, anything that had my
publisher sets to it. And I thought to
myself, okay, I can spend the next five,
10 minutes to write that small script
out and run it, but what if Copilot can
do that for me? So, what I did was um
get all apps with get nav app info
server instance BC.
loop through them
and uninstall all with
my publisher
with uninstall nav app. I made a ton of
typos, but Copilot doesn't care because
two seconds later, I have my PowerShell
script. Get Navf info server instance BC
pipe where object publisher equals my
publisher pipe for each object.
Uninstall nav app server instance BC
name version. I'm done. In two seconds,
the full script is created and I was
able to unpublish uh everything. Well,
uninstall here. So this is another
example of how I really like to use the
inline copilot with these small scripts
which you probably all know how to write
but you don't have to because this can
be this can be much quicker.
Okay. And now I want to get back into
the slides because I still have a couple
of things that I want to talk about.
First it's models
for AL developers. Dimmitri had a
slightly different approach to how you
should choose a model. My approach is
just stick to claude. In my experience,
nothing got close to how good Claude is
for generating AL code. But if you're
working with more mature languages like
C, I Python, TypeScript, play around
with different models because my
experience is that I still always start
with Claude and Claude is the best until
it's not. And then Claude starts to
struggle with five different iterations
over the same bug and it still doesn't
fix it. And I switch to 03 and 03 fixes
it immediately. And then 03 is the best
until it's not. And then 03 starts to
struggle. And I switch back to Claude
and Claude solves it immediately. So do
try to play around with these different
models because two models are going to
give you different implementations. But
that can sometimes be a good thing. And
I found another kind of interesting
picture about models uh which was on on
Reddit describing what are what are some
of the models good for open AI they're
good for chat
anthropic or claude they're good for
coding
perplexity it's good for research and
Gemini good morning
that was that was sort of my experience
with Gemini as well like Gemini 2.0
though it never really did the things
that I wanted it to do. However, Gemini
2.5 has been much more promising. So, I
maybe have to stop making fun of of
Gemini and I decided we're going to make
fun of OpenAI as well. Found a different
picture, which was, you know, with
OpenAI, they've created this GPT2 that
was back in 2019 before any of us even
knew about AI. Then they've created GPT3
and GPT3.5. That was the initial CH GPT
era. That was that was quite exciting.
We all got excited about AI and then
they created GPT4,
right? The the model that really made it
feel like we can communicate with these
models. So obviously we all expected
GPT5. Now did we do GPT5?
We did everything but we did 03, 04
preview, 41 nano, 01 mini, 4 turbo, 41,
45, 01 pro.
OpenAI is part of the reason why we have
such a hard time figuring out which
model to choose. Not only for like
coding reasons also when you're trying
to create AI features on your own. But I
would say luckily for us as AL
developers, Claude is so much better
that at least we don't have to worry
about all all the others here.
Now I want to do a quick recap of what
have we seen in the in all of the coding
examples. The one thing I really want
you to take away from this session is
take control of your context. You know
the files where you want to make the
changes. You know the files where
existing code exists. Pull the new
files, pull the old files in and then
write your prompt and you are going to
get much better results out of AI.
So a few things to remember. Yeah,
seriously take control of your context.
But beyond that, for open tabs, it's
okay if you continue to just use fancy
autocomplete. That's fine. I do hope you
try edits, you try agents, but if you
continue to use the fancy autocomplete,
remember to close down everything that's
not the the relevant files to what
you're trying to work on.
Go for cloud models. They are the best
for AL.
Boost your prompts. A good prompt means
a good completion. A bad prompt means a
bad completion. and prompt boost
extension can kind of help bridge this
gap.
Create your memory files. When AI does
something wrong and you instruct AI,
hey, please go fix that. If you want the
next session with AI to not make that
mistake, well, put it in your memory
file. Put it in the copilot instructions
MD. And remember the inline copilot. If
it edits don't do a good job on huge
legacy files, take control. Just select
we are modifying this procedure. Click
control I get the inline copilot and
work with that one.
So your experience with AI might be
something like this. Something is
sometimes it's going to be the most
amazing thing you've ever seen and
sometimes it's going to be complete
garbage. That was the experience for me.
I was just kind of ping ponging between
the two parts all the time until I
eventually find my workflow. how I can
kind of work with AI that it makes me
more efficient that it brings more more
kind of joy to what I do and I would say
to all of you try to experiment on your
own as well.
I want to close this session with a
couple of quotes though. One of the key
things to prompting cursor or GitHub
copilot and AI in general is to know the
limits and not to get too greedy. One
certain step at a time is better than
trying to do five which are 99.9% going
to fail fail. Absolutely. If we try to
ask the world of copilot edits, it's not
going to do a good job. But if we break
that problem down into individual steps
and then uh use copilot edits to help
with these individual steps, we're going
to get much better results.
I've got one final kind of entertaining
picture that I found which is my
throughput has doubled by harnessing AI.
So you're smart now.
I'm stupid faster because you know just
because you can write more code doesn't
mean that all of that code is good. I
wouldn't necessarily equate more code
with better performance.
And I want to close with this one.
People aren't drawn to software
development because they like writing
code. It's because they love solving
problems. Code is the medium. The real
gratification comes from how quickly you
can bring ideas to life and see the
results. This one hit incredibly close
to home for me because I am an AL
developer for most of my working uh
working part of the day, but I also have
a ton of side projects that I love to
work on. And for a long time, all of
these side projects, they always got
stuck because I kind of knew how to
write the backend code, but I was never
good at front- end code. But now I can
get Copilot to write the the front end
parts for me. And I have brought so many
tiny little apps to life because of
that. And that's that's kind of the
exciting part uh for me that you bring
these ideas to life. So on on Monday, I
kind of hope that when you get to work,
you try more than just the fancy
autocomplete with GitHub Copilot, but I
also hope that you take some of this
enthusiasm with you because really these
AI assisted development tools, they can
they can bring more more joy to the the
life of coder.
And with that, I'm going to say thank
you very much for coming to this 9:00
a.m. session today. Uh if you'll have
any questions, I'm going to open the
floor up for for Q&A. Uh you can always
find me throughout the conference today
or on any of the social media. Uh I'm
always happy to discuss this topic. But
uh just before I open the floor for
questions, I have one more thing to say
which is co-pilot is not just a fancy
autocomplete anywhere. Thank you.
[Applause]
And now um if anyone's got already here
in the front row.
Thanks. Uh is there is a way how to
centralize the uh memory for for the AI?
It means uh not have them as a part of
the repository but somehow have the link
to some right now. No, as far as I know,
it does have to be a file within the um
within the repository. Yep.
Let me get the the t-shirts. Um you you
said there's this rule that it only uh
takes four open tabs into account. And
uh can you maybe uh publish the how how
you use Fiddler to figure it out that
it's four tabs because maybe they will
update this in the future or like a
small tutorial how to set it up. Uh I
can uh so I asked Chad GPT um how to set
up Fiddler. I I could probably still
find that conversation. But if you ask
um Chad GPT how do you set up Fiddler to
intercept calls from VS Code? It's going
to give you a step-by-step instruction.
you you install it, you enable the HTTPS
communication capturing, uh you add some
filters because you're going to get way
too much information. Um and that's how
you're going to see the these uh API
calls going out. So I have um the first
time I did this was in November. Then it
was for tabs. I tried it again last week
when I was preparing the session. It was
still for open tabs, but I'm kind of on
the lookout as well if they're going to
increase that or not
over there.
you. Um, can we also influence the
commit message generation with uh the
rule files? Uh, yes, yes, yes, yes. Um,
I didn't show that, but let me just get
the t-shirt. Um there's in the settings
in VS code uh there's one setting where
you can specify instructions
specifically for for the commit message
and you can say start with a verb or
start with this start with that like
semantic versioning and all that kind of
stuff right yeah sure thank you maybe
best to to to right so you talked about
the co-pilot instructions yes um and
then you said in the cursor you can make
the autoattach and that is kind of what
I'm going I ask about but do you have
any considerations when you think about
what you should add to that context
because that context could also be large
at some point if we just keep adding
instruction. So I I do kind of um
because I don't have this possibility to
split things apart. I kind of have a
huge file in GitHub copilot for cursor
because I can have this autoattached.
I'm I'm starting to split it down. I
have to do a bit more work on it. But
the first thing that I've started
splitting is um anything related to to
test creation test code units. I don't
need that when I'm writing things in the
the functional part of the application.
Um so I am now going into the direction
of splitting but I'm also waiting for
GitHub copilot to support uh like
directory level uh these instructions.
Yeah.
And there's one uh behind you then.
Yeah. Uh yeah actually my question is
regarding the the models in itself. So
how somehow now they are trained to yeah
to get better let's say for a specific
language. But my question is is there a
way to um specifically enhance or train
those models specifically for my
session. For example, I want to provide
my data set for my local uh rep yeah uh
source code or my my own uh repositories
or workspace or whatever.
Not in a sense that you would train a
model like training a model takes so
much data that it it doesn't make sense
for one organization to do that. There
is one thing with GitHub copilot which I
didn't get to experiment because you
need the enterprise skew of of like the
GitHub itself but uh it can have access
to your repositories and it can kind of
uh search through your repositories that
you have uh on GitHub in your
organization if you give it permissions
to. Um, but that's still that can help.
Uh, but it's it's not going to be any
better than if you just locally clone
that repository and use the the agent uh
in in VS Code. So, uh, in terms of
training it specifically on your data, I
would say in the BC world, we we don't
have enough data to to consider that.
Okay. Thanks. And there's a question
behind you and I think that's going to
be the last question, but I'm I'm also
going to be here for everyone else that
question. You said something like let
the AI do the boring stuff and I think
many many would think that reports are
quite quite boring. So so have you tried
for example let the AI do report
layouts? Can it handle some
modifications or maybe do a copy of some
custom report and do it like uh using
using that as a content? Could it be
could it be done? I mean it absolutely
could be done because if you think about
it the report layout is just a text file
right have you tried it to that no I
have not I haven't worked luckily I
haven't worked with reports for time
okay thanks okay maybe maybe let's do
one more question if anyone else has one
what about the GitHub um cultural
reviews because you can do do that also
in the chat sorry say
the GitHub copilot code review. Code
review. A code review. Yeah. So, um
right now I'm going into this direction
of exploring GitHub copilot code review.
Uh so far it's not that great for AL.
There's a different tool out there, the
one that I referenced a year ago at the
code review session at Tech Days, which
is code rabbit. Code rabbit appears to
be quite good for AL because for code
rabbit you can give it uh like these
additional instructions custom
instructions you can give custom
instructions to the GitHub copilot code
review uh but only if you have like the
enterprise skew which is which is too
expensive for for us um so in like the
direction which I want to explore things
for the next couple of months weeks now
that we're done with conferences is code
review what what can do, what it cannot
do, and is code rabbit really that much
better. But I also want to explore the
GitHub copilot agent that lives in in
GitHub. Uh, and what kind of tasks for
AL can it complete and what kind of
tasks it cannot complete because they're
maybe too complex. So that we know,
okay, of course it's not perfect. It's
not replacing us. But like if we have to
add tables and pages, we know that this
works. If we have to add this and that,
we know that it works. But if we want to
subscribe to something in the posting
code unit, we know that this is the kind
of task that cannot just go directly to
the agent. That's kind of the direction
I want to explore more uh for maybe the
next session.
Okay. Um so we don't have uh the the
time anymore, but thank you all again
for coming and thank you for all the
questions.
