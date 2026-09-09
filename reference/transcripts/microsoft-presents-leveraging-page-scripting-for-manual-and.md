# Microsoft Presents: Leveraging page scripting for manual and automated acceptance testing

- **Source:** https://www.youtube.com/watch?v=qj_KHQ1V60Y
- **Video ID:** qj_KHQ1V60Y
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 43m29s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Hello,
welcome everyone. Um, today we're going
to present to you how you can leverage
pay scripting for manual and automated
uh tests. My name is Vasel. I'm a senior
software engineer in the business
central clients team, the team that
developed uh base scripting and with me
here is Thomas who you've already met.
Um, so same as Arita, we're on the same
team. He's also my manager.
And um interestingly enough two years
ago today Vincent stood and introduced
uh page scripting for the first time in
busy tech days and we stand here in
front of you having a dedicated session
for it.
So uh how many of you are using pay
scripting today?
Lovely. And how many of you are using it
in an automated environment?
Fantastic. So uh I hope that after this
session next time the same question is
asked like you will have the opportunity
to raise your hand. I forgot to raise my
hand because we are using it for as
well. Yeah. Yeah. I I did it on our
behalf. So um today we're going to show
you what page scripting is, what it can
offer you and how you can utilize it um
uh to its fullest. We're going to talk
about best practices, something that we
learned using it ourselves to share with
you. We're also going to talk about BC
Replay which is the uh script replayer
for automation and then we're going to
share with you how we use page scripting
internally.
So what is page scripting? Uh we are
aware that user acceptance test can be
very tedious and lengthy process and
it's it is often uh prone to regressions
due to its purpose. So
pay scripting is a tool that will c help
you capture all of these user flows um
in a single file that will allow you to
streamline that process to be more uh
effective and to reduce cost. Uh what is
important also to note that today's
presentation is going to be about the
feature as is today
and it's important to highlight what
page scripting is not and page scripting
is not just a generic HTML automation
tool. It is instead a tool that works
with AL with the business logic coming
from your apps from your extension and
it works across different platform
versions. So, um, Thomas, can you show
us? Um, yep.
So, I'll be doing a bit of layman's
examples uh because we always have uh
new people as we just saw from um hands
raised. We always have new people coming
in to this feature. So I'll show a bit
of happy path uh and is going to
complement me with a lot more hardcore
technical knowledge how to make this uh
a lot more flexible and useful for your
own use cases. Uh so first let's just
create some uh page scripting uh
scenarios. So in my case I'm starting I
want to have a page script that creates
sales quotes. Uh
I'm just clicking around. I'm not
thinking at all about paid scripting.
I'm just going about doing my business.
What I want to achieve. Uh I created the
sales quote. I actually want tree
research to be my customer.
No, I'm editing sales quote. That's
wrong. Scratch that. So you stop and
start a new one. Very easy. You can and
page scripting tool forgets all about
your mistakes. Uh very nice.
start recording again. We click a new
sales code.
Let's pick Trey as our customer. Uh it's
gonna I'll leave it uh to the app
validation to figure out uh the customer
name and trying to just give enough um
not to hardcode too much but at the same
time just give enough for the platform
to figure out the right uh presets.
Let's pick an item. It doesn't matter
too much. Let's pick quantity.
Yes,
that's it. I'll stop recording.
And now pretty much I have a page script
recording that can give me uh infinite
sales quotes because I can keep running
it and it will keep creating uh sales
quotes. So that's pretty nice. Uh no
script failed.
Well, I think since I was in the last
session, I know how to fix this. I made
a mistake. I should not have used the uh
selection uh at the dialogue to pick the
value because the index has changed. So,
that was a really useful tip that I can
now use uh from a previous session that
Luke and Tina Tina did. Thank you.
It's going to save my day. Uh, right.
So, but but that was the thing. I tried
to I relied too much on just trying to
do uh everything out of the box and it
was not as straightforward as that. I
still want to fix that because the next
one is going to rely on that. Uh, the
next thing I want to do. So, I have one
free research. I'll try a new one just
for the sake of it. I'll just close a
little bit of this.
Yes, new page script. Now, what I want
to do is to start a new one. And in this
case, I will be relying on
doing a bit of filtering uh beforehand.
So, I want to see only the quotes from
tray.
I want to open tray quote and I want to
simply make an order out of that.
So what's different about this case is
that I'm now also relying on selecting
things from the list and yes
I'll record all that dialog is also fine
we are able to record uh which options I
do select and now it's became an order
I'm going to close the page
and stop recording
reset a bit of state
and let's try to See, fingers crossed
now it's going to work. Yes, that should
work.
Tray
going through dialogues. All is good.
Confirming. Making a sales order. And
that worked. Uh, so now I have
feeling of confidence from my last
mistake. I recovered. Now all is green.
I'm very confident that I know how to
use paid scripting. Uh, because I see
all the green check marks. But what
happens if I run it again?
The problem is there was only one tray
uh sales code that is no longer there.
Uh so was again making a mistake trying
to rely on the data setup. I didn't set
up my own data. I tried to rely on what
was in the data. And while running the
test, I changed the state. So the state
was no longer the state that the test
started with. And well, that's a
problem. As a lame man uh test coder, uh
I'm stuck here. And I need help from
you. How can I make this scripts
smarter? Yeah. So what did Thomas do
wrong?
So uh he took a very bad assumptions
from the beginning. So uh he tried to
create a flow to uh for example convert
a sales quote to a sales order but he
assumed that the data that he was going
to use it's already there. So one should
not assume the state of the system. just
create it. So, uh I have this particular
scenario here. Um
yes,
let me just switch from the presentation
slowly. So, uh I have this flow where uh
I did exactly what Thomas did. I went to
sales quotes. I selected a row and I
have a validation that I'm using that
customer because I made the same
assumption. So uh rule number one never
assume the state created. So how can I
recover from that and how can you
recover from uh from this? Some of you
may already have noticed that but we
have the concept of a current step of
the recording and it is highlighted a
bit. So uh I would like to insert
certain steps before this one and we
have received feedback from you that
it's very cumbersome to modify the
recordings from the UI. We are aware but
there are some tips and tricks that uh
that we can do. So since I'm already
somewhere along this scenario I can
start from the beginning. I can rewind
like I can go back. So my current step
is at index zero. So uh what can I do? I
go to state zero where I started and I
can click record.
If I go now and perform certain actions,
we can see that the next steps are added
from where our current step was. So, uh
I can go here and then I can create this
customer which was Trey and add an
external document number which would be
this. Then I'm gonna go back again at
point zero and I'm going to stop my
recording. So I have successfully added
steps prior the recording that I've made
to recover from this scenario. And since
I've already did that before which we
recorded, I can continue from this. But
same thing again. What do we do? So uh
same thing as Thomas did like now I need
to go back. Where do I need to go back?
So, uh, yes, I want to discard them. So,
I'm here and before I invoke a row, I
can go couple of steps before where the
page was shown and I can click record
again and then I can input a search
string of my external document number.
That's it. I have my filtered ro
and now I can confidently select this.
It is stray my recording works and it's
all good
and I have done my acceptance test and
it's only natural that in your uh apps I
have tested one but now you want to test
another action. We have tested the
conversion from a quote to an order. Now
I want to test the conversion from a
quote to an invoice. So what we learned
is that we need to create the quotes. We
need to filter down. We need to uh now
invoke and assert our next uh test to to
create. But I can do and click through
all of these um steps yet again. But I
shouldn't because that's best practice
number two. You need to create your
scripts to be modular and atomic. This
way you can create building blocks for
your next steps. So I have created these
prior uh the presentation. So I can show
you that I have um
created two. I have create sales quote
which does what we saw and I have split
them into
convert sales quote to order.
But how can I then reuse these two?
These are independent. This there's this
is not a single flow. what can I do? And
now this here comes the challenge. So um
now it's no longer UI. Now I need to
open Visual Studio Code. And then I can
I need to create a recording myself.
And the way that you can create these
suits and import previous scripts and
bundle them into one is that in here in
the steps there is a special type which
is called include.
So I can still add the name and then I
can say create sales quote. I can add my
description then say create sales quote
and then I can point to which file. So
uh in here I have them as you can see in
a folder which is in a different
directory and I can create them.
I just want to be sure that I have the
right name here. And this is the way
that in my suit I create like I import
and include one script and then I want
to do the other one. So uh I can do that
and then another include and do the name
convert
just a different one. So, uh if I now
take this and then load into um
into uh the product I need to grant the
browser permission to access these files
first. I can see that these are included
um independently and in this way you can
uh read the scripts a bit better. So uh
if we run this scenario we can see that
we do exactly the same as we used to
record and it works. So I can create yet
another just atomic script of converting
to sales invoice and just include that
one as well. But what's the problem here
that the scripts that we have created
are tightly coupled with the data right
we input tray as a customer we input 1 2
3 4 5 6 as the external document number
and we now do we need to make sure that
every single script uses these files
like that's that's not the way to go and
in here you can use best practice number
three I think I got there and that is to
use parameters
so
your scripts can take input parameters
and you can define them again in the uh
YAML.
Uh the way to use that is that I'm here
on the sales uh create sales quote and
this is the script that we created. I'm
going to hide the steps because they're
not important for now. You need to add
another property in the file which is
called parameters. And then in here you
can start defining your parameters. I
know that I need to create a customer
name. Uh sorry I don't need a quote. And
then I can say that it's a type string
and that the default value uh is going
to be tray.
But I'm also going to make this uh
required parameter.
So uh I have this one and then I have
the external document number which is
string. Thank you co-pilot. Um, but I
have defined and said that I that this
script requires these two parameters.
How do I pass them in the input field?
So I'm just going to search for input in
my script and we can see the value that
that is being passed to the field. So
this is very important that in order to
evaluate certain expressions, you need
to use the equal sign and since this is
parameters are expressions, you you need
to start with equals. and this time is
capitalized.
So it's uh parameters and then you need
to supply the correct name. So you can
use spaces. So if you use spaces in the
parameter names, make sure to quote them
and make sure that the um that the
casing is um is correct because this is
case sensitive. And in here we have the
value and we can repeat the same thing
parameters external document number.
I'm going to repeat that for um for the
um convert uh for the conversion script
and then I'm going to say parameters.
But we know that in here we only
required the external external document
number
and step string is this and we're done.
Let's uh update the steps to for that
again parameters external document
number. So we have parameterized these
two scripts that we pass along. So this
now turn out to be dynamic. You can
define what data you're going to enter
and this is something that you can
assert on. But then how do these scripts
receive the parameters? So I'm here in
the include we saw that earlier. This is
how we create the suits. But uh in order
for my included scripts to receive them,
I still need to pass them. So uh I will
define them the parameters um option in
inside this step and then I'm going to
pass them as a each each one. So
this is fine. But now I can pass the
values and this was three and this was
four four and this is something that I'm
going to do for these ones. So if I take
uh let's say the sales quote and I put
them side by side
and we see that customer name is spelled
like this. It needs to match one to one.
So pay attention to the uh to the casing
and to how the parameters are called. So
uh let's load this script
again and uh
ah sorry about that.
I think I'm here. Yes.
And uh okay, I have in here created yet
another one. But uh if I require
parameters and they're not passed,
you're going to see this dialogue. So I
can say a customer name and then I can
say BC tech is um25
and then something
and then
this.
So um we have defined we have passed the
parameters and the they get transferred
into the scripts. So uh you might have
noticed that every time that I create a
recording I start from the RO center and
then when I'm done I close it and that's
on purpose because if you are to utilize
all of these atomic scripts you need all
scripts to have a same starting point.
So uh that is also uh important to note.
Okay well you kind of need to take my
word for it now. Um but um in this way
uh you can create atomic scripts. You
can use them as building blocks and you
can reuse all the steps that you have
created in order to create these uh
these suits for um uh for your uh user
acceptance test. But some scripts like
as we saw for example creating a
customer can be a user acceptance test
independently and can be used as part of
uh an an included script. So how do you
know that I can run it independently and
then and as an include one? Well, if you
define a particular value, you might end
up with data collision. You might end up
with validation errors. So you need to
make sure that sometimes you create
unique data. Um, and the way that you
can do that is um actually really
interesting that if I open up this
script in here,
I you can see that I have the uh I have
defined a parameter which is called
customer name and I have passed in a
default value but I have not specified
that this is a required parameter. uh
instead when we input the value in here
I have created a power f(x) expression
saying that if I
uh pass in a parameter a value to it
which is different than the default one
then use that one otherwise uh post uh
post spend the time stamp so you get
different value every time that you
execute the test. So uh to summarize
what we just uh what we just uh talked
about is that in order for you to uh may
to be able to take um good assertions,
you need to create the state. In order
for you to not end up with data
collision, you need to create unique
values. In order to be able to create
these uh uh atomic scripts, you need to
uh you need to use parameters. And in
order to get the exact same data that
you assert on, you need to filter. And
um something that uh that we showed as
part of the include is using suits where
you can define the deterministic order
of how you want all of these scripts to
be included. So uh those are the best
practices that we learn that we've
learned by using it internally. But uh
let's hear Thomas what you can show us
about uh how we can run all of these
scripts in an automated manner. Yep.
Let me switch.
Yes. Uh so I'm going to talk about BC
Replay MPM package. Uh that's the
addition additional helper uh for page
scripting that allows us to run scripts
without user uh uh intervention
programmatically specifically this helps
a lot in uh CI/CD pipelines. Um so what
I did I tried to forget all about I I I
know about page scripting and try to use
it as a new person I would would using
the library and try to capture all the
gotchas that I I I had and I'm trying
going to share that uh with you. So
first of all uh it's a p public open
source uh mpm package uh that you can
import uh we don't have the source code
published uh I don't believe I think
that could be really useful especially
for some of of the ideas we saw uh from
uh Luke's and Tina session uh but
basically what it does it allows us to
take the page scripting uh recording
that we produce in the browser take that
as a file and and run it uh in uh any
environment. It could be uh docker
image, it could be cloud uh environment,
should not be production. Uh it should
be hopefully sandbox environment. Uh and
it has a couple of parameters that we
can use. Uh first we need to define
where is our tests. Uh so we need to set
which files to run. We need a starting
address and that's how you give it a
context of where to run uh the tests.
We need to set authentication and right
now by default it runs on Windows uh
because that would most likely be how
the Docker setup works or username and
password. That's the second option or uh
AD or Entra ID. Uh with Entra ID there
is a bit of caveat right now. We still
don't support uh uh MFA um but that's
something we are looking into how to
make this better. Uh to make my demo
work I
uh yeah don't tell our security people
but in my separate outside of Microsoft
tenant not connected at all this MFA is
disabled for an hour.
Uh yes
then we also need to provide username
key password key u and this was a gotcha
for me. So this key word is specifically
important. So you don't provide username
and password here. This is the
environment variables where the password
and and username is. So how that looks
in a in a power p PowerShell. Uh this is
here. Uh so I have MPX replay. MPX is a
is a shorthand in npm to run uh any
package you have that has a way to be
invoked as a command. So you don't have
to necessarily make a uh node JavaScript
project and run some kind of JavaScript
code. That's neat. I think we have that
in in documentation as well. Uh I
specify which step recording to replay.
Starting address is my uh sample tenant.
I have authentication set to AAD. I have
username key here. You see variables,
password key. uh so they are set as
environment variables because that's
usually how we set set up CI/CD
pipelines. So we set environment
variables we don't specify user name or
password directly in scripts. That's a
really bad practice. Uh yes and lastly I
want to set all my results in certain
directory. I just hit run. Uh the only
thing it's going to do is going to
create one item uh and it's going to
run. Hopefully that's going to be quick
and then I can share some of the
results. So this is running completely
let's say what is the term is headless
meaning that you not see you're not
seeing any UI it's all running in the
background um and usually running in the
background is faster and that's how you
would run it in CI/CD because you're not
so interested in visually seeing what is
happening but if you do if you are
debugging something uh headed mode is
also uh very useful and then you can
visually see what is happening uh in the
browser
and it's complete one test passed uh we
can take a look at the result of it. In
my results directory, I have played
report. I have one test. I can see that
everything went fine. And lastly, I can
see the recording uh
tenant loaded
and one item has been created. So even
though I was running headless I the
recording is still very useful to know
what happened because you might be
running in a very different environment
very different setup not having
necessarily environment variables or I
don't know so suddenly MFA is enabled
again and your test is starting to fail
that happened before uh sorry I need to
drink so what's important also to note
here that if there are test failures you
have the logs attached to the uh
particular recording where you have a
copy of your scripts where the logs are
also embedded into it.
Sorry, I will cough mute the mic.
I also got sick along the way. Um yes.
Uh and the neat part is since it's
running headless, I can also run many
tests. So in this my case I run uh only
one items YAML file but I can use uh
glob patterns and just run all the
tests.
They're going to spin spin up
independent instances
and run in the background but you still
need to know that it is the same user is
the same tenant. So whatever state
you're changing that might interfere
with each other. So you need to follow
all the best practices that Vasil has
outlined to make sure that tests are
running efficiently. And it doesn't
matter if uh I don't know this is the
day when time zone daylight saving came
into effect or the new year came and
suddenly all your test pipelines are uh
red and it happens every year. Uh then
you definitely have a problem. You
should look into that. Uh speaking from
experience,
yes. Uh and my test now failed. Uh and I
can rely on uh the recording again to
figure out uh what happened. So I have a
second one item of error. And then I can
go here look through the recording.
Yeah. And here I was trying to find an
item that didn't exist and delete it. Uh
so it failed. So that's really neat.
I think we can go next.
And there's actually since an open
source uh package and it's being
continuously released. Uh it's already
leaking some things that we're working
on. Uh and we're going to talk about
that. If you're very diligent in reading
the MPM package uh description, you can
already see ahead a little bit what
we're working on.
Don't spoil it. Don't spoil it. Yes.
So
how do we use it internally? Um I think
the first thing is we are using it
internally. We are relying on page
scripting. Sorry,
we are relying we are relying on page
scripting uh for every single change
that uh our developers does. We have set
of end to end test that we have
converted into page scripting because we
want to dog food this tool and figure
out is it useful, how it's useful, what
we can uh change, how we can improve it
starting with our flows because we have
a lot of tests. We have thousands or
tens of thousands of tests and some of
them are really good candidates for paid
scripting. So we started with a few and
we've been converting and so far I think
the message or the learning for us is
it's pretty good. We of course we fixed
bugs, we found bugs along the way, but
at least even with the limited set of
capabilities that we have right now, we
are able to get a lot of value from pay
scripting and it has already caught some
really bad bugs that would have ended up
hopefully not in production but at least
in some of the test strings uh that we
have and it caught that on the check-in
time. So every time someone makes a
change in the in the repository before
they can merge, we run some of the uh
tests that are being uh made with page
scripting recordings and page scripting
and specifically mpm replay library is
running that for us in uh see the
pipeline in Azure DevOps.
Um second thing where we found a lot of
use for it was performance tests. uh we
previously and still are using uh
selenium and migrate we're in progress
of m migrating to playright and we found
that being dependent on UI was making
our test very flaky there's just so much
variables I mean one machine is faster
one machine CPU is busier and then
there's small tiny rendering differences
that makes targeting specific UI
elements very finicky and this is where
uh page scripting allow us to first very
easily create scenarios
uh run them in parallel load uh it's not
really for load testing but it does
provide a little bit of load on the
machine since we can run in parallel uh
and it allowed us to very quickly start
converting our um performance test
infrastructure as well. Other case where
we found it useful was uh sharing as bug
repros. So every time a PM in our team
or other teams finds a bug, we
internally also say have you run page
script script and could reproduce this
bug for us. Same as we would ask you
when creating a support request. So we
trying to dog food through that flow as
well. And lastly, the last place where
we're using it, we're also using it as
the last step before the build actually
goes out and becomes the production
build in in cloud. uh we run additional
uh full feature set tests in real
production environments where page
scripting is launched uh and we try to
validate if the real basic core
functionality is not broken um and
that's another awesome area we found
page scripting being very useful for us.
Yes.
So main message that you can carry out
even though it's in preview
we are dog footing it internally every
change or breaking change we would make
it would affect us equally as you we
don't have any special powers in the
like BC replay or page scripting we
using exactly the same production
release of page scripting of course
we're looking at one ahead in the next
version uh but at least all the versions
of the product that we still support are
running the version of page scripting
that is uh in production right
Cool.
Yeah. And uh now who can guess what's
next?
It's uh of course from the lab.
Yeah. So uh same disclaimer as a
previous uh section. Like doesn't
necessarily mean that we're going to
ship this. Doesn't necessarily mean that
it's going to be uh in the product ever.
But uh we'd like to share some of the
things that we've done for page
scripting. Um
um
so one of the things that I demoed and I
empathize with you when I demoed
parameters that it can be errorprone and
that uh it's a bit cumbersome. So uh
what we did is that we extended the uh
properties for the recording that now
you can define them in the UI and
they're backwards compatible. So I
created these scripts in the YAML and
then I added the parameters there. So as
soon as I load them, we can see them
here and we can um we can uh change
that. Additionally, what we uh what we
played around was that uh we started
thinking a bit more of how to extend the
capability of how to allow you to script
like more complicated scenarios. So uh
we added the option to iterate over
lists to uh iterate o over items to um
copy rows either a single row or all
rows and my personal favorite is the uh
exception whether it satisfies
something. I love love power effects uh
ex expressions. So uh my favorite use of
this is that you can run different uh
tests based on different users. So uh
you can create suits, you can create
recordings just simply as saying if my
session user ID equals
admin
then run this otherwise if this is my
user otherwise don't do anything. So um
this is like one of my favorite
improvement also uh maybe in the future
when uh you will have extensions that uh
also extend autofill you can uh assert
on certain suggestions that that you
want to see. Um
what else Thomas?
Right. We also cannot do a feature
without sprinkling in a little bit of
co-pilot and LLM into it. Uh so we also
have added an ability to have LLM steps.
Uh so in this case building it a bit on
top of Bugsy's um example today creating
an item with uh how we called it uh
funny uh funny items, funny toys. Uh
for example, I'm creating an item and I
don't want to specify description, the
same description all the time. I can
actually uh
add a step
that's called run prompt.
My prompt is going to be generate item
title for a silly toy product. Add a
representative emoji as well. Max 20
characters. I'm going to direct the
value of the output into a control. I
can drag and drop the target. Pick a
description field. That's going to be my
target. I'm going to stop recording.
I'll reset the state. That's the best
practice.
I'm going to run it.
Yes, I do want to in production this
time.
And this is going to be surprise both
for you and me what it's going to come
up with.
Wacky wobble worm. That's a really safe
uh toy. So really awesome. And an
awesome emoji. So this is really great
way to generate first of all random data
uh because you can figure out all kinds
of prompting patterns. Uh but we're also
thinking how this could be more involved
in making phase scripting even more
dynamic. That's at least where our
thinking is going to really make you
be really creative uh how you rely
utilize page scripting and it could also
help to remove or recover some of the
error cases in the page scripting as
well and it could be even a lot more
creative scenarios that you can come up
with. Awesome.
Um and uh one thing that Thomas hinted
about uh earlier is that we are aware
that when you create all of these
lengthy uh scripts that it takes time to
execute them. So uh we are as we said
like we also have a bunch of tests that
run for each merge validation. So it
also takes time. Uh so what we are
exploring is to uh run scripts server
side and something that won't require a
browser which will greatly improve um
execution duration. So uh yeah we are
currently in the process of testing
this. Unfortunately I cannot demo this
live for you but uh we are adding
support for that uh uh in the uh
replayer and we are testing that in
product how it performs.
That is what we have prepared for you
today. Um, thank you very much. Are
there any questions?
Yes, the comment was that we should also
take a look at the conference app.
There's also some questions. We'll of
course prioritize. We'll let me we'll do
one each uh from the app. I I saw this.
I saw you first.
uh will there be a uh scheme file for
the YAML so we can validate the steps
and the parameters and the variables and
yes whatever options is available. Uh
good question. So uh the feature is
still in preview so it's subject to
change and uh once uh as we're working
on ging that is one of the uh steps
towards it that we can define schema for
the ML file and where we can document
what each of these represent.
Yeah I'll take one from the app. Uh is
there any plans to use pave scripting to
prepare a test scenarios that can be
used in performance toolkit?
Uh that would be you really cool
synergy. I think we'll need to take that
back to the to the team
which we showed in a previous session on
I have one question. Is there a
possibility that I have something like
um a reset point or something that if I
running my script and I can go maybe if
I don't have a posting something that I
can go back and maybe don't have the
issues you showed because I already
processed the data maybe also say set a
restore point running the script return
to restore point and everything is nice
maybe this helps a little bit you still
thinking about
So
from navigation perspective maybe that
would be easier to achieve but from
resetting the entire environment state
that will be quite difficult because
changing certain data have side effects.
Uh
though what you can do if your script is
created in such a manner that you can
probably create scripts that reset the
data in essence.
Yes. Yeah. We'll take one from the app.
Uh is there any plans to add a kind of
library for scripts? Some way to
organize it. Um yeah, it's still in idea
phase. I guess that will be more in the
browser instead of having the files on
the like on your own file system or
versioning system. U having that more uh
no code way. I guess that that is the
intention of of this question. Yeah,
that's something on yeah in the future
list that we're considering. I think we
have time for one or two questions.
Um I was thinking maybe there is there
any way to tag the scripts with some
versioning so that you can run some
specific scripts only in some business
central versions or something like that.
That's a that's a good question. I can
probably think of some hacks how you can
go around it maybe soon. But uh not at
the moment. But great idea. Thank you.
I'll take one more from the app. Is it
possible to execute a YAML file from the
MPM library containing a prompt type
instruction to generate a product
description as we have seen in the
presentation? Uh not at this moment. Uh
what we have shown from the lab is is
still experimental. Uh we also need to
make sure this is going through our
entire AI feature review process. So to
make sure it's safe back going back to
harms testing that Bugsy uh mentioned in
in keynote. Uh but we hope we can do all
of that and provide you this uh step in
the ammo.
I think we're yeah soon out of time. So
thank you everyone for attending and
thank you for all the feedback. We are
here if you know our faces. If you're
interested in any other conversation
welcome to reach out to us. Thank you.
[Music]
