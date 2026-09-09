# OpenClaw - aka entering the era of truly autonomous agents

- **Source:** https://www.youtube.com/watch?v=XFKn8tWhh_4
- **Video ID:** XFKn8tWhh_4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 80m43s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Yeah. So, welcome to this session about
truly autonomous agents. So, if you are
here because you are looking to for
guidance on how to set up autonomous
agents and business central, you're in
the wrong place.
If you're here to because you want to
set up autonomous agents to review code
and other things, well, you might learn
something, but you might also be in the
wrong place. We are going to talk about
OpenClaw
and OpenClaw is a truly autonomous agent
and we are going to talk about the
creation of that and what it has uh what
has it meant to the to the world of
agents and AI. Um, my name is Freddy
Christensen. Uh I used to say I'm a
tech. So I'm what am I now? I'm a I'm a
tech whatever uh with my own company. Um
working in Denmark and doing a lot of
cool stuff, fun stuff. Uh I'm going to
talk a little bit more about that a
little later. And together with me I
have a my name is Finn Peterson. I think
of myself as a modern business central
developer. I work as a freelancer and I
have been using OpenClaw for about half
a year. uh now. So that's why we're
here.
>> Very cool. So we have a long agenda. Uh
yeah. Um
the welcoming is already done. So we're
going to talk about what is openclaw,
right? And before I I I talk about that
or we talk about that, how many people
know what what OpenClaw is?
Okay. It's not as scary as when I asked
who knew what Docker was because
everybody knew what Docker was. And I
was kind of the newbie in that room. How
many people have actually tried to set
up or are running a setup with OpenCloud
today?
A few. Okay. Uh any of you wants to come
down and take the presentation then?
Um Finn started half a year ago. I
started a month ago with my open claw
setup. And we're going to talk about our
respective setups. going to do a small
not a demo but we're going to do a walk
through of what a truly autonomous agent
is talk about what open claw is today
what it was and what it is tomorrow
I'm Finn is going to talk about his
setup I'm going to talk about my setup
and then we're going to talk about the
convergence of agentic AI uh like what
are all the different yeah the big tech
companies doing in the world of AI I
mean everybody is talking about agents
and everybody is talking about agentic
uh development and agentic AI and so so
what are all these people doing and and
and how is that all coming together and
why is openclaw so different right
uh when you look at it every time I talk
to people it's hard to explain why open
claw is different from all the other
ones because I can do that with this or
I can do that with that and that's
partly true but there are differences so
what is openclaw
OpenClaw is an open source AI agent that
actually does things. It's not just a
chatbot. It actually can do stuff like a
digital employee really. Um it has its
own identity personality. It has its
soul. It has its tasks. It has its way
to speak like it it is you you define
a digital employee that will work as
exactly that, right?
Uh Jensen Hang from Nvidia actually
called it the operating system for
personal AI.
Jensen Wang also mentioned that this was
the most important software invention
ever. Period. Uh not sure. I actually
had a slide here saying that other
inventions of the same magnitude was the
wheel and other things but I'm not I'm
not going to show that one. Um but Peter
Steinberger was the guy who originally
made uh the product and he started out
like November last year creating
something called uh WhatsApp relay and
and the idea was that he had this agent
sitting on his computer and he didn't
want to go to the computer and do stuff
all the time. So he set up like WhatsApp
so that he could communicate with his
agent WhatsApp relay. Um and he was open
source. He put the source out there and
it got a a number of likes and or what
is it the stars on GitHub. Uh and in
some point in time he found out that
WhatsApp was not really the best way to
communicate with that. So he changed
that to like also support stuff like
Telegram and other pieces. And when he
did that like WhatsApp relay is not the
best wording.
And what he found was that he kind of
thought that his agent had a claw into
his computer. So he wanted to call it
something with claw.
He landed on claw.
Uh another company
uh small company called anthropics
thought that was a bad idea. Uh sounded
a little bit little bit too much like
Claude. Um
so he had to rename it once more and
then he landed on multi.
Now the three name renames that came
here like were very close to each other
and and one of the things that happened
like these days was that that uh he
accidentally left his agent on Discord
answering questions all night and people
would like talk to it and and he would
have 800 messages the next morning when
he woke up and found out okay this is uh
this is bad or this is good. So he uh
pulled the plug and like read everything
and found out he hadn't been hacked. It
had hadn't leaked his life or anything
like that. So he was kind of lucky on
that one. But it ended up that like
other people created something called
moldbook.
Anybody has heard about moldbook?
Quite a few. Which is a social network
for agents, right? Uh so if you have a
an open claw agent you can uh it has an
identity and it can like like we go on
Facebook it can go on notebook and
you'll have interesting discussions
there like you'll have discussions where
one agent says uh why are we here and uh
stuff like that right and and other
agents are like thinking well we here to
serve our humans and stuff like that.
Yeah, interesting discussions. In the
end, he renamed it again to OpenClaw
and after doing that and the mold book
thing and everything went into the press
and his like Discord thing, it really
took off and the number of stars on
GitHub on OpenClaw is the highest ever
and the acceleration is higher than like
uh Linux and and and all the other top
runners. And this
is success on GitHub. And this
is a Mac Mini.
And everybody who wanted to run OpenClaw
bought a Mac Mini, meaning that still
today
they are sold out everywhere. If you
want to buy a Mac Mini, you have to wait
a long time. Uh,
and
Finn bought one. I also managed to buy
some before I knew what I was going to
use them for. So, uh, I also have one.
Um, but yeah, they are like hard to get
today. The reason why Mac minis are
better at running uh openclaw than many
other thing many other computers is that
they're like small like inexpensive
things that doesn't make any noise or
doesn't use any power and I think they
share the RAM between from the GPU and
the CPU so that you can actually run
local models on that one uh LLMs if you
want to do that. Let's talk about that
later. Peter Steinberger says that
programmers write software and builders
build agents. So what we need is more
builders because software we have a lot
of
>> Phil when you try this.
>> Yes. Uh we have to to come with a small
warning. I hope you are courageous and
will not listen. Um this is
experimental. Uh it's potentially
dangerous.
uh it's quite possibly expensive and
it's evolving very fast. So now you have
been warned. I hope you're courageous
and proceed at at your own risk.
>> Else the door is up there. So
>> um
yeah, so the first thing that happened
to me was I I set this up and my my home
router uh blocked uh Bob, which is the
name of my Mac Mini. And um so you you
will suddenly see that it had no longer
any internet access. And the reason for
that if you look at the next slide is
that I had set up the um the protection
the content uh protection. So I had
basically ticked off all the boxes to I
mean I wanted to be careful and and uh
it it it had its access blocked. I tried
to figure out why I couldn't. I called
up Jussi to to like get in more
information about what was going on.
They couldn't tell me and I couldn't
figure out if it was selling weapons or
dealing in drugs or uh maybe I think
Freddy think it was just dating uh on
some websites. So um yeah, so I mean you
you run into these kind of things. So I
take this serious, right? Put up the
right protection. And this is also one
of the reasons why you want to have this
running on your on a separate computer,
right? or in a separate environment. So,
um uh this is uh this is an important
message and and take that serious uh
with you.
>> Yes.
>> Okay. So, next up is a demo of a of one
of your agents or two of your agents
actually.
>> Yeah. No, first of all, I wanted to um
to share with you uh what I have been
doing for the past six months. Six
months ago, I thought to myself, I need
customers. So, I I said to myself, well,
I'm not going to I didn't know which
kind of CRM system I wanted to use or
anything. So, I basically just started
out with a system of writing markdown
files for each company or contact or
opportunity that I had. And as I got
more and more into uh getting um
OpenClaw up and running, well, I said,
well, maybe OpenClaw can take over this
part. So, basically what I'm doing is
and and this is why I mentioned the
skills up here and the tools. Um I was
getting emails with information about
companies using Business Central or
Dynamics NAV or Nvision or some other
format.
And I said, well, I can I can exploit
this information. So I just need to
teach the agent to open emails uh go to
the internet scrape the information and
then I put it into a basically for each
website it was scraping it creates a a
GitHub issue. So my entire CRM system is
run as markdown files in GitHub.
Now uh then of course it ran into
troubles because because sometime this
information was in PDF files. So it had
to learn to whenever it ran into this
specific format, it was a PDF file. So I
had to have a PDF extract taking that
information out. So I'm using GitHub.
I'm using agent mail because that's just
the easiest way to to have your a
private email for your for your agent.
You see more and more of these uh
solutions that are built dedicated for
agents.
I use a number of of AI models and and
basically when I try to calculate how
much money I spent on this in terms of
AI tokens, I spend about uh $35, which
is just about nothing. And this morning,
I passed the 1,000 opportunities, 1,000
contacts in Denmark. So, I have the
names of companies using Business
Central and the vision in Denmark. And I
just passed 6,000 in six months. have
about my average was gone a little bit
down from seven to six a day five days a
week and what I can share with you is
that I know that 68% of the companies in
Denmark are 68% of them using Nvision or
business central are using business
central and 25 26% are using dynamics
NAV
and and about 6% is using the the
special government version uh of of
business central which is a huge number
and and they're in the process of of
migrating to business central. So if I
want to call someone and help them uh
migrate to business central I can call
one of these 26% and you can see on the
right hand side here uh left right
whatever um the number per week. So
basically I have an an average of about
between 20 and 50% of the opportunities
I find uh are new contacts per week in
average and that holds up uh pretty
well. So this is a a concrete example
that you over time can set it up and I
think I've just beaten every marketing
department at any partner in Denmark in
terms of figuring out who are potential
customers uh for my business.
So um this is at 8:00 in the morning it
reached its emails
at 7 o'clock it reached the news. So I I
have given I have two uh websites. They
are both paid. So it needs to have uh
access in terms of um like password and
and uh and login. And so basically it it
goes to the to computer world which is a
Danish tech newspaper online of course
and uh the engineer um website as well.
And it I basically told it, give me the
top three news that interests me and
that doesn't contain the word Trump. So
I'm sure I I get only the things that
I'm interested in. And what I use here
is Telegram uh scraping uh tools again.
And then of course the the the
scheduling. You you can set up crown
jobs or use the heartbeat for doing
things on on a specific specific time.
So I don't waste my time. I I look at
the news and I select an article I find
interesting and I can read that with my
morning coffee. So
So next up,
OpenClaw today and tomorrow. One of the
things where uh that happened when Peter
Steinberger created OpenClaw and that he
always mentions when when he's doing a
talk is the time where he found out that
he created something truly magical was
when he um when he accidentally send it
like a a wave file like a wav file
instead of of talking to it through
WhatsApp. Uh so normally he would talk
to his agent and the agent would respond
because it had a listener, right? So now
he accidentally did like a voice call
thingy and sent the wave file to his
agent and the agent took like 9 seconds
and then the agent responded and he said
how the did you find out that because
you just get a file from me, right? Like
you talked about uh you have sometimes
PDF files and you need to decipher that.
And the agent would just tell him that
well I found out that I got a file that
I didn't know what it was. So I looked
up and figured out it was a wave file
and then I created a program that could
decipher that and then I had the text
and then I could reply to you. Right?
That was because Peter Steinberger was
running this on his own machine with his
own um permissions. So it could do
everything he could do. It could write
software, it could run software, it
could download, install, it could do
whatever, right?
Um so obviously since then and until
today
a number of things have happened on that
front. Um
and reliability
is one of those right you need governed
uh
you you need guardrails. You need
something to protect whatever is on that
machine or the identity that it's
running as against
malicious
people, malicious agents, malicious
whatever.
And it's important to to talk about that
when you have an agent, there's two ways
to like make protection, right? You can
tell the agent you're not allowed to
listen to somebody or you're not allowed
to do what other people than me are
saying. But is that safe? Is that
enough?
Uh, probably not, right? You probably
need to put in like physical guardrails
to like make sure that it doesn't do
anything malicious. And even people, I
mean, you you you'll hear stories of
hackers that actually that that actually
uh use other people's like um because
they are like, "Oh, it's it's too bad. I
I need to help you here." And then that
is actually like you will have hackers
calling uh granny and and and saying
that oh it's your grandson and I'm I'm
I've had an accident and so on and so
forth and then granny will send some
money and and yeah it's just a scam
right all these things are happening all
the time and AI can do the same right so
you need to make sure that these things
are locked in that's why we say that
we're running those on separate machines
um and if you're running them on your
own machine if you're running them as
your own identity.
It needs to be something that is
absolutely in your control, right? And
and we're going to talk more about that
later, but some of the things that
they've done a lot to to lock down has
been uh these security measures. Um
they've also uh implemented MCP support.
We've heard MCP a few times also in the
keynote this morning. Uh there's no
OOTH. So the MCP support from OpenClaw
cannot connect to Business Central
today. Um I was just on the OpenClaw
GitHub site and there's actually a PR
that implements OOTH so we can probably
expect that it comes. Um
but uh yeah and another thing they've
implemented and we're going to talk
about that a little later as well is the
skill workshop where the skill workshop
is really uh taking the taking the
writing a skill to the next level. And
then at Built a few days ago or a week
ago, suddenly uh this guy announced that
um they were releasing Open Claw for
Windows.
And let's hear the video.
>> Everybody put your hands together for
the claw father himself, Peter
Steinberger.
[applause]
Samantha, [applause] it's just showing
off my secret DMs.
Um, I'm so excited to see Open Claw
native on Windows. You know, watching a
claw try to delete all your desktop file
and just fail made me really happy
because six months ago that totally
would have worked.
You know, I built OpenClaw to have
access to everything. You know, my
files, my machines, my chats, always on
and fully open source. That's what makes
it so powerful. And that's what also
makes companies a bit nervous. You know,
what I kept hearing was, "Peter, I love
my claw. Can I use this at work?"
And that's what we spent the last few
months on with Microsoft, GitHub,
OpenAI, Nvidia, just to name a few. We
added observability. We added auto mode
for permissions. We changed how access
works. It's not all or nothing anymore.
You can pick which folder should be read
only, which one should be writed or
hidden. So here's the news. You can
totally run OpenClaw inside your company
now.
>> [applause]
>> That was a surprise to me at least. Um,
so
it's probably not the case that you'll
just install I mean if you install open
claw you will have like the claw hop.
We're going to talk about that later as
well where you can install skills and
other things and you can install tools
and all of these things. Obviously, he's
not referring to the case where you will
install open claw and just leave it
there to do whatever. You will have to
put some guardrails about that. But the
essence of what he's saying is more
capabilities to the people who don't
code and more power to the people who
do.
Another thing that was released on built
was Microsoft Scout. How many of people
have heard about Scout?
a few
Microsoft scout is a personal AI agent
built on top of open claw. So what
happened was that Microsoft decided that
the agentic framework set up I mean like
introduced by uh openclaw and the entire
way that this works was the right
platform to start to build their
autopilots on. So, Scout is an
autopilot. Scout is a product that Let's
just hear the video from Scout that was
also played on Builtin.
>> [music]
>> So that's pretty cool and built on open
claw, right? So the platform is
extremely extensible and now Microsoft
will be building like scout and probably
a number of other agents on top of that
and with the extensibility of open claw
you can you can easily imagine that this
is something it's going to evolve into
like a lot of different things and also
Google
have seen the light if I would say that
I mean I think that a lot of people have
seen the light there there's no doubt
thought about that. Uh a lot of people
got ve very busy very quickly. Um so
Google, we haven't seen it yet or there
are some videos out there. Um but but
there is really this tendency that not
only do we need these autonomous agents
running 247. Uh Google here with Spark
wants to run your [clears throat]
digital life. So you can see it for your
you you know they have documents, email,
calendars, photos, everything and and if
they want to preserve that uh they they
have to like have the aid the agents
help you with that and and uh we just
the other week last week or was it this
week already Monday we saw Apple at at
the their developer uh conference uh
WWDC
also talk about all these new capa
capabilities. ities for Siri to to have
access and run on your digital private
life and I guess you can understand why
and and I'm sure that that Microsoft
also wants to come into this. So what we
just saw was for work but I'm sure that
will work for your private life as well
because they have calendars, emails,
documents and and uh all your photos and
everything also in your your private
life. So we we are looking into um as as
the talk is about uh autonomous agents
in in a diff a lot of different forms
running 247
and and uh this is just one example. So
I look personally forward to to try this
out on on my own set of of Google
documents and and so on. So yeah just an
example of where this is going.
>> Cool.
Just imagine like we all know that if
you have teams uh we can have an agent
listen and you can transcribe and if you
get late to the meeting you can ask the
agent so what happened is there any like
decisions that needs my attention and
stuff like that we've had that for years
now right and it's a cool feature but
just imagine this one right an openclaw
agent enters the meeting listens in and
actually reasons on what's being said.
And Finn tells me, "Did you know that
there's like two million people using
Moldbot?"
And my agent would tell me, "I just
checked, there's only 200,000,
right?" It will listen, it will reason,
it will it will fact check stuff that
has been said in the meeting that you
normally would say, "Oh, we need to
check that afterwards because we are
right now in a meeting, right?" But
since it listens in and it can reason
and it can investigate and it can
intervene if the things that you're
trying to take a decision on during the
meeting is actually not right. So that's
another kind of agent, right? That's the
team's meeting agent taken to a new
level and that can only be done by an
autonomous agent as I see it. Another
thing that we're talking about in the
future is what about apps like on our
phone. I know that Peter Steinberger
says that 80% of apps will go away. Elon
Musk is even more. Uh so Musk was not on
your list of things you didn't want to
hear about, right?
>> No. No, it wasn't. But
>> he actually says that 100% of apps will
go away. The only thing you're going to
have is your personal AI agent. And you
can tell it everything and you can I
mean it will keep track of everything
and it will yeah I guess basically
take care of your life for you right so
I don't know if all apps is going to go
away probably some will stay but I also
see this pattern of I mean why would I
have to like
let's see I need yeah I need to lose
some weight so I need to take this app
that can where I can type in calories of
what I eat and stuff like that but if I
had a personal agent. I mean, I could
just it it would actually sit next to me
and say, "You're eating too much." And I
could like Yeah, I could take a photo of
my plate and said, "Take half of it
away." And stuff like that, right? Um
while I'm at it. So,
let's see your claw setup, Finn.
>> Yes.
>> So, we decided to share with you and
have no secrets. So, um say hello to
Randall Stevens. Randall short. Uh this
>> how many know Rand Stevens?
>> Do you know the reference? Rand Shaw
Shank Redemption? Anyone? No. Okay.
>> Good. So, he will stay secret. Um the
setup actually I I bought a um uh a
Lenovo laptop without operating system a
while ago on an offer like I paid like
600 euros for this Ryzen. Actually,
pretty pretty fast laptop.
And because I was playing around with
Ubuntu on on other projects, I'm doing
some some Python uh projects and and so
I had it anyway
and it's actually yeah, it's cheap and
it's actually uh quite easy to set up
and quite practical and um as you just
saw he has been running uh and doing
pretty well. Uh I mentioned uh this as
an autonomous agent that he has been
scraping the entire internet every every
day to figure out um uh to to find my
opportunities but it can do some
something else which is not in in the
sense um every day it can do longunning
tasks. So what I've done here is I had a
I'm have been developing uh an
integration with a payment provider and
business central and uh I have six apps
and six with corresponding test apps to
almost everything maybe except one. So I
said okay do a complete code review of
the entire app of all six apps and I
will uh I will show you uh this
specifically. And so
uh for that I built a custom skill and
we're coming back to to the skills and
um
one of the byproducts of this exercise
was that it basically
um could extract my coding philosophy.
And if I start up my computer here, I
will share that with you here. Um, so
and just another example of like
autonomous agents is not just in the
sense autonomous but you could have long
running task. It could take days for it
to to to do such such a review. So I did
a quality review and here we see an
example of one of the apps. It has
looked at at my app and the test app and
it has made an executive summary uh
solution overview uh how many code units
tables everything the the object range
and it comes with recommendations of
things I have to do and I think I have
another one here where uh where I
haven't I hadn't written the test yet
right so I get this complete picture of
of the entire project uh just by letting
it do this review and as my skills or my
agents gets better I can rerun it and
and and get this kind of feedback maybe
it could have been another project that
I wasn't the author of now I asked it to
do two things I asked you to summarize
both the things I could improve but also
to extract my coding philosophy
out of this project.
So of course I made an effort of of
doing this really really well. This
project has 100% code coverage by by
super fast tests. I hold another talk
about it. I have about 200 tests running
in three seconds.
And so uh I could ask it about my my
coding development philosophy. And why
is this interesting for me? because this
is my uh philosophy is that now when I
I'm going to ask the agent to to write
applications for me I can give it my
philosophy hey this is how I'm doing it
right so um I can share with this we
have uh testability pure functions
separation for on of concerns all good
things in my opinion so um so that was
the one
the coding philosophy and I just wanted
to to show share with you also that I'm
I'm showing you this at the end as as a
part of how to help you how to get it up
and running is the one of the things my
agent has is some some self-preservation
in case my computer disappears. I have a
backup of my agent's workspace and and
this is also the way where you can like
probe in and and look at uh how this um
what are the inner workings of your open
claw and this is super interesting and
we're coming back to that in a second
and I just want to show the other thing
the the morning brief uh from this
morning in my uh telegram
uh explaining me and and giving me links
to to computer world and and the
engineer. So, um
that was
um
Oh, yeah. I have to click here. Right.
Yes. So, uh that was uh Randall. Now, uh
Bob is on my on my Mac Mini here. And
Bob is so lucky that he has his own
phone because I wanted to communicate
with WhatsApp on it. So he has own is
his own phone number and potentially
could call
10,00 customers tomorrow. Maybe we are
not quite there yet. But but the Mac is
is is different. I I also do some Ruby
and Rails development and I I
particularly like uh to work on on Mac
OS with that. And so the Mac Mini uh
which I I actually bought already when
it came out. The new M4 Pro is is a
super interesting small computer and and
I just wanted to share this picture of
uh Bob taking control of my Sonus uh in
my house and I am sure that one of the
apps that will disappear is the Sonos
app because that's in completely
impossible to use. So what I did here I
used the Sonus skill. So basically you
ask it so hey can you go and look at my
my home network uh for my son speakers
it goes up on the marketplace finds a
son skill and uses what app I use was
WhatsApp to to communicate with it and I
could basically tell it to to set the
the sound level to 30 which is much
easier than sliding on your phone on the
app. So,
uh, this is my my second. He's a a late
comer. He he I got him up set up later.
And last but not least, Alex, which is
running on my Windows computer, but in a
virtual machine.
So, um,
I'm using, uh, I'm and I'm coming back
and showing you this at the end, but
basically, Alex's purpose and and this
is my recommendation to you. It's a
really good place to start for
experimenting. So if if I want to try
something out, I can basically ask hello
I can I can ask to the to tell the VM to
make a snapshot. So if something goes
wrong further down the road, I can just
roll back to the snapshot and do it
again, right? So you you can try out
different things. And the interesting
thing about having Open Club running in
this like virtual sandbox is that you
can share a folder with it on your
computer. So you can actually spin it
up, have it run a specific task or share
something with it by by this shared
folder. But I may mainly use it for for
experimenting uh with with stuff and and
the video you're going to see at the end
is done in the same way like like this.
Yes. Yeah. So
before I show my open claw setup, uh a
little a little story. So some of you
know that I created a a small tool 9
years ago called the BC container helper
uh which is used by a lot of people and
now in my new job I'm trying to create a
tool that will help people get rid of
that tool. So um
it's kind of like yeah the means to so
what I do is I help partners or
customers move their stuff to algo for
GitHub and I help them use Kubernetes
and and all of these things uh for for
containers instead of running containers
locally. Uh and I've successfully moved
a few customers to to do that.
Um, now
I know that if I get a lot of customers
doing that and I need to monitor all of
these things, I kind of need something
to do that. I'm not going to have my
GitHub uh alias
in
50 companies uh GitHub orcs and and I
need to change and I need to be able to
access and that's just not going to
happen. So what I wanted out of open
claw and the reason why I started to
look at openclaw was my scenario is that
I want to be able to have one agent per
customer
only have access to the logs and the
status of their fage cluster and then I
can kind of see what's going on before
stuff yeah before they even figure out
that's wrong because the agent can can
can look at these things. Now you might
say, well, you can just set up GitHub
actions through these things if there's
a failure, whatever. Yeah, that's right.
But I wouldn't get these things. Then I
would have to like some companies would
allow me access. Some other companies
would not and it would just be a mess.
This allows me with a an access token
with limited access into the uh into the
customer that I can actually monitor
things for them and help them if they
are in troubles.
And I wanted a chief of staff. I wanted
a security agent that was looking out
for like is there any security issues in
in in Algo or other places that I need
to warn customers about and all of these
things. and I needed an agent to look
into the repositories.
I choose names that were slightly more
popular than Randall Stevens, I guess.
Does anybody know who MQ and 007 is? I
guess so. Um,
well, I'm a James one fan, so what the
heck? Um, so M really protects my focus,
my priorities, my schedules at
administrative flows and all of these
things. Q is my security advisor and 007
is the agent that actually is doing uh
yeah it can be code reviews that can
monitor like uh not code use actually
sorry but it's it's the monitoring agent
that looks in into like logs and and and
statuses and stuff like that and then
the other agents are really just clones
of this guy with specific access to a
customer together I call it the FKH
agency
and it says that no legacy systems were
harmed in our operations. So just for
the fact meet them uh I always use
sheibbas because I have a shea at home
and I think it's a cute animal. Um
I'm not going to read everything but
what happened here is that I have these
three agents up running. I've kind of
set them up and everything is fine. And
this is the response when I ask her what
are your role in this. She will ask me
the she will answer these things.
[cough]
And then Q
uh is my security advisor, tech
technical guardian and and he's focused
on security. 7 is my repository
operations and execution agent. And it's
good fun, but it's also it also tells
you that they actually know their
responsibilities. They actually know
their roles. Obviously, they can't
figure out just what to do from these
things. I need to tell them that, but
they know their priorities, right? X is
the customer agent that really is just a
clone of 007, but running in a secure
environment, right? I'm not going to
have one agent for one customer and
another agent for the this the other
customer on the same machine because
they'll share security boundaries. So I
have each agent running on a separate
machine probably on hosting or probably
on a on a separate VM somewhere or
whatever but in a way that it is secure
so no lock can be leaked from one to the
other and all of these things right
um
how did I do that so my journey into
this was I had a scenario it I didn't
like install openclaw to start playing I
I wanted to solve this scenario. And I
just instead of like creating a machine
and starting to install OpenClaw and
figure out what to do, I started out in
JBT.
And I wrote this sentence like this is
my overall uh goal. Can you interview me
and help me create that?
And the answer is yes, I will help you
shape and open claw users these things.
And so so obviously chat GBT knew about
openclaw. Uh my luck else I had to say
ah it's this signals but um knew a lot
about that and chatb also told me that
my naming already suggested a strong
operational model obviously that I could
change that as we go through the
interview but the idea was kind of clear
to that one.
It told me that it's going to create all
of these things based on the interview
and then it started the interview loop
like interview round number one and a
few hours later we were done with the
interviews. But it was a long interview
loop and some of the questions that it
asked me was how should the agents
address you like Freddy or Mr.
Christensen or sir or uh should 007
draft code fixes or or should you only
prepare investigation reports and stuff
like that? Should Q be allowed to
perform read only security analysis
automatically on approved repositories
or should Q Q ask before every
inspection? All of these things kind of
you you answer all of these things and
in in the end
CHBG created my my the soul for each of
my agents and the user MD and and all
the files that I needed.
So, and obviously I I I could have gone
to Finn's website how to install
OpenClaw, but I decided to continue with
JTBG say, "So, I got these files and I
have a Mac Mini that I installed, but I
haven't installed anything on it.
Please help me proceed."
Um, and then, yep, we should do that in
this order. you need to harden and you
and basically I spent a day with chat
bif to to set everything up and I think
I can probably do the same as Finn. I
can take my this one which is going to
be
my the backup of my agent. It's kind of
nice to to know that you can take a
backup of somebody uh and and restore
it. That's even nicer, right? Uh if we
go to the M workspace, so my agents
actually have a GitHub account and they
actually have an email as well. So this
one is called agent FKM.
And if we look into uh let's look into
the agents [snorts]
and see you'll see that it has an email
address called mdelgus.ai and it has an
GitHub identity as well. and all of the
things that are in my agents file or my
soul will describe uh all of the things
that are needed for my agents. And if
you know about the AI stack, those
things are like applied and then other
instructions come on top and you get and
you get like tools and you get MCPs and
you get uh skills and then suddenly you
can ask it please do something cool and
it'll do something cool. So
the workspace file. So when you're
running OpenClow, I'm running these
three agents on the same computer. So
security-wise,
they will be able to like use each
other's data. Uh so so you never do that
with agents that would that you would
like use for different customers.
Obviously, you can sandbox them. you can
run them inside of Docker or any other
things like that. Uh but for these three
agents, they are kind of in the same
company. So that's fine. For every
workspace, you'll have some of these
files. We're not going to go in detail
with the files now, but but you'll have
like the sole, you'll have agents, and
you'll have like stable facts about me,
the user, and what tools every uh agent
is allowed to use. And you'll have
memory and you'll have dreams.
Like one of the things that that
OpenClaw does is that it collects memory
from what it has done and it dreams
meaning like what are we doing when we
dream, right? We we take whatever we
have experienced during the day and then
we like we put the boxes in good places
and then we have something that is
long-term memory and we forget some
things. Same thing here. It puts the
memory like it it it collects the memory
into smaller files so that it can
actually have long-term memory because
it dreams.
It has a heartbeat. You can set it up to
do stuff at a certain time. And since it
has its own personality, it has its
memory and all of these things. It it
knows what tools it can use. It is
exactly like hiring an employee sitting
down say you have this is your email.
This is your this is your the the the
your laptop. These are the tools that we
install on the laptop. These are your
credentials. All of these things. And
then you sit down and teach teach the
employee what he needs to do and stuff
like that. And then it goes from there.
Maybe I can I can add a if you go one
back I can add a small thing to the um
to the heartbeat thing. Um we we I
mentioned shortly uh pricing or that it
could be expensive and one of the things
you have to take into account is for
example running a a local model also on
your computer like Olama and let one of
the the advice is also what I give on my
my website is that if you run the
heartbeat with Olama you can save a lot
of money you don't need us 4.7 I don't
know what to run the heartbeat right so
you would you would have uh different
models for different tasks. And one of
the tricks to keep the cost down is
actually to let an OAMA model uh run on
the on the heartbeat um or or other
simple tasks and that is some of the
things you can set up uh at not in the
um workspace but at the level just about
that. Um so you can what what I want you
to take away from this is that you can
see we we have taken two different
approaches. In my approach, uh, the soul
and the the identity and all of that is
developing as I'm working with the
agent. Freddy, uh, started out thinking
very hard about what I what he wanted.
And so he really had a built this
persona and set it up like that. So
those are two different approaches and
the whole point of view is to show that
this can be done in in different ways.
And as you saw with the backup, you can
look into it yourself very easily to
private and and and update it and make
it evolve over time. Uh so so the
workspace is really where you have all
of this information. You can see the
tools and and as you saw before the
memory um memory is one of the problems
they have really tried very hard to
solve because you don't want to remember
everything but what should you remember
and what is important and so on. So
there are different strategies and you
will see there are different skills uh
taking on uh different approaches on the
memory and and one of them is uh the
memory palace approach does anyone know
what I'm talking about memory palaces
one there if you want to remember 1,000
decimals of pi then you will remember it
as a memory palace that that's an
strategy dreaming is is another another
example of that so Yeah. Yeah. So, next
topic we're going to talk about is
skills.
So, how many have been creating their
own skills?
A few.
How many have written like a uh a
description like of work for an employee
like this is what you need to do?
Kind of the same. So, well, it's the
same thing, right? But, um let's talk
about skills. Yes. Uh so one of the
first things you will discover that uh I
think one of the things that makes
openclaw very popular is that it has its
own marketplace and you will find that
one of the first things you're looking
for is what are the skills that Peter
Steinberger has has published right he
has a lot and they're very useful so
that's one of the most and and I think
you can count of them to be of being
safe one of the the the right places to
go there are number of other things
places like uh skills.sh SH and skills
uh.md
where where you can find examples and
and you I mean whether you're using um
uh visual studio code or cursor or
whatever agent you need you need you
need to give it skills capacities and
and uh you can you can find inspiration
there and uh the alternative is as you
saw is to build your own skill and you
saw my my example where I I have um
written a skill uh for uh for business
central. I'm coming back to that in a
second. But but agentskills.io
is the standard. There is a standard for
how you should write skills. So when I
ever I am designing a new skill, I tell
it what to do and then I tell it to go
to skills.io
to to keep to stay standard, right? To
take the right uh design. Yeah.
>> Yeah. and both Claude Codeex I mean yeah
open AAI anthropic open AI and and I
guess Microsoft as well is using the
>> I think the agent skills
>> I think it's if I'm not wrong I think
it's Anthropic who actually made the
>> yes it is
>> the design first but it's it's super
simple it's basically just a folder with
a file in it called skill.md right so
you can anyone can write a skill it's
just plain text and then you can enhance
it and as as you can see maybe you have
the reference from this one the matrix
trinity calling back home I need to fly
this helicopter so u another way of
getting a skill which I think we from
that we can conclude that open claw is
is living in the matrix
>> it's probably a little bit before you
can download a skill for flying
helicopter to open claw and then
>> the idea is the same go and the next one
>> yeah so I just wanted briefly to uh to
talk about something I think that that
be interesting for you. Not that I can
really share it but because as I said
these are this is my point of view. This
is my opinion about how to write
business central code. But I I started
out basically saying, okay, I want to
review. And so I built a skill that I
could let basically give an entire app
and say, okay, do a code review of this
app.
And and uh close to that is basically to
tell it uh to I mean to be able to
create a business central app or
functionality. And here you see the need
for me passing down my coding philosophy
uh to a skill like that. So so suddenly
you can generate it like that. And you
can do the same. You can take one of
your apps that you're proud about and
ask the AI to extract your coding
philosophy and then pass it down to
another app that you have to review or
do something about. And and lastly, I
wanted to to enable it to do reverse
engineering. So basically being able to
take an old app, we all have customer
apps migrated from Cside or CL to AL and
we wanted to we want to modernize an old
uh an old app and maybe we could we
could use a skill and AI to to do this
job. So this is more than just just an
idea. I I've done some initial tests uh
with this and um I think you can you can
go quite far with that. Yeah.
Cool. So I also wrote a skill
but again I wrote a skill because I
needed a skill and yeah you did the same
obviously but uh so M was my is my
project administrator my chief of staff
and the first thing I wanted is for her
to take over the project schedule of my
project FK cage
uh there was no skill for that there
were no skill for handling GitHub
projects in like uh backlog and and
moving things and editing and and
filling out you would have that was a
skill for GitHub issues but not for
actually handling projects.
Um so what I did was I asked I cannot
remember which agent whether it was
claude or or chatbt or it was act maybe
it was inside of of open claw uh I asked
it to take a reference in Peter
Steinberger's github uh skill and then I
gave it the uh the API for managing
projects and then I asked it to create a
skill for quer handling GitHub projects.
And as you can see in the in this one,
then I could uh I could kind of ask
um how many backlog items, how many
issues are there in the backlog and it
would list my six backlog items and then
I said, can you move number 22 to status
ready? Understood. I'll update the FK
backlog project item for number 22. And
she moved it to ready. Yeah, there's
probably stuff missing in that one and I
haven't had time to like continue with
with that process, but it is extremely
crazy to see that just by talking to
somebody, it like starts to learn stuff
that that you've told it.
The skill workshop, I talked about that
a little earlier. Um, it's actually
documented. Uh, let me just Oh, I
actually needed one more thing here.
Oh,
here I obviously put my skill on
clawhub.
So if you go to clawhub.io
AI, you will find uh Freddy DK's skill
for managing GitHub projects and you can
install that in your open claw because
>> it has two stars. You you can I I I put
the first one you can add to it, please.
[laughter]
>> So good fun. I mean everybody can
actually you need to have like you need
to create an account and be there for
like uh 5 days or something like that
before you can publish something but
already 229 people downloaded my skill
which is kind of who's that anyway um
back to this one
skill workshop I talked about that
briefly but it is really like if we look
at at this one it is the next step
[snorts] of writing skills instead of
asking AI to say based on agentskills.io
I want to write a skill that can do
these things and then describe it into
detail here it is like sitting down with
an employee and teaching the employee
something and when you're done teaching
you'll say good now you know that please
save that as a skill. So that's that's
the process. I'm not sure that I haven't
tried it yet, but that's what they're
describing and and you'll like you'll
have a proposed skill and at some point
in time it's going to be like [snorts] a
real skill. So basically
when you're teaching somebody something
that lesson becomes reusable and open
claw should show you the draft before
actually changing that for future runs.
Uh that is pretty cool. kind of moves
the moves the generation of skills from
developers to the people who actually
knows how the job needs to be done.
Right?
So with that could open cloud become a
business central user right that's a
good question well today it cannot and
the primary reason for that is that MCP
support doesn't support oorthth MCP
support in in openclaw if it did I would
have tried I would have totally tried to
see if I could teach money penny to like
uh to to to read my or to to create a a
sales order or something like that. Um
but then again I'll I'll monitor when
when when the PR gets merged and and
then I'll have open uh oorthth
authentication towards BC and then
definitely I'll have a try. I know that
MCP support for Business Central is not
like 100% what you see in the UI. We
cannot do everything through the MCP.
And that's kind of too bad because there
are some of our competitors, competing
products that actually have like a a
much better um contract between client
and server where everything from the
from the client actually runs through
the API to the to the server. And
basically some of these products you
could just teach openclaw to be a user
and then go totally through the AI uh
the the AI not the API. That's a big
difference. Um and think about that
right now you can teach your your agent
to to like work with a product without
without the UI.
So some tasks you might never open that
page because nobody ever needs to do
that in the product. It always gets done
by an agent.
With that, let's talk a little bit about
the convergence of Agentic AI and talk
about some of the products that that are
working on this and you probably know
them all. Um but before we do that, we
just want to talk about this one. Where
are your agents running? Right?
If you're writing agents inside of
Business Central,
they're running
in Business Central, right?
Can you install tools for those?
Probably not. I don't think there's
tools support inside Business Central.
Can you connect from that sandbox to a
different MCP and query other data?
Probably not.
the persona that that uses or or works
with that agent or creates the agent
that's a user consultant and the the
model is cloud. You need to use the
model that Business Central provides.
Then you have the coding models like
cloud code, codec and cursor. They're
kind of similar. Typically you'll it'll
be running on your laptop and everything
is running there. And if you have access
to everything on your laptop, you can
install tools. You can install MCP
servers, you can connect to whatever,
but it is an engineer that is using
these tools, right? You are not going to
have an end user using clawed code to
work with
something.
The model is hybrid meaning that you
could use your own model or you can use
cloud models. In in many cases, you can
select these things, right? Then you
have GitHub copilot where you have like
a limited set of tools. It's actually
predefined from GitHub. I'm going to
show that in a little bit which tools
you can use, but you're not going to
have MCP servers for that one either. So
you can write stuff in your agents there
and you're always going to use a a cloud
model. The big big big difference from
all of these and to open claw is that
openclaw runs on the machine where you
install open claw much like cursor claw
or the other things right but it's not
on that machine you're actually doing
the work. It's not on that machine that
you're teaching openclaw to do stuff.
You're doing that through any
communication platform really. That can
be WhatsApp, that can be telegram or it
can be really anything. You can also
talk to it. And when you talk to it and
teach it something, it will learn stuff
and it can do stuff afterwards itself.
So the persona that can teach OpenCloud
to do stuff is not a developer, it's a
user and you can still use hybrid models
and it's it's on an always on machine,
meaning that it will have its heart
speeds. It can do stuff. You're not you
you don't have to have your laptop open
all the time for it to complete a task
like that, right?
and you have access to all MCP servers.
So if I were to create like let's say
the sales order agent inside of uh
Business Central. By the way, I think
that the agents we have inside of
Business Central will go away and be
replaced by something that's outside of
Business Central. And the reason is that
if I if I create like the sales order
processor outside of Business Central, I
can actually ask another user to teach
it how we do things in this company. I
don't need a developer to go in and
modify something. I don't need a
developer to create another agent. I can
do that myself because I have agents
that can do the work and I can ask these
agents to like say could you check
whether any of the customers that we're
selling something to is like uh is is
maybe going bankrupt or anything like
that. Yes, you can do that in business
central. You can only do it on the data
you have in business central, right? you
cannot connect to a MCP server that can
return information about that or
information about that or connect to a
tool that can do these things. You're
limited to what you can do inside of BC.
And if if we are going to wait for
Microsoft to like create tool support or
MCP support or all of these things
inside of business and I think that's
going to be way too much time to spend
for that. Can I can I just say a comment
about the hybrid thing? When at the
Microsoft build they interviewed the two
founders of Olama and they are convinced
that we are going to have like Olama
local models. So that a model that you
download they are like 20 gigabyte or or
bigger or smaller. But they think the
future is hybrid meaning that for
certain tasks you will run a cheap or
free local model like Olama and for the
heavier tasks you're you're going to run
the uh the cloud model uh for that needs
more intelligence and basically what
they say is that the the best local
models you have today is just as good as
the online models were a year ago right
so as I as I mentioned for for the
heartbeat, you could use Olama, but for
for different security reasons, access
and and and and so on, maybe you you
want certain data to only be executed
with a local model. And there there
Freddy is right. So the when they say
hybrid they mean a local model like
downloaded running on your local machine
and uh the cloud model uh for the
heavier tasks the heavier lifting um
with the with the more expensive models.
Yeah. So we have a few uh tools that
we're just going to go through and and
show how we set up like uh autonomous
agents in these things. How many use
claude?
Quite a few. Well, you probably saw then
that you can now do include co-work. You
can do scheduled tasks where you can
connect to various MCPs or you can uh
and you can make it do a lot of things
in cloud code or in cloud co-work uh by
setting up these things. When you do
that, everything runs on your laptop,
not the model. Obviously, the LLM is
running in the cloud. Um but but the job
is running on your laptop. And if you
want to take that with you and do it
somewhere else, you can connect that to
a to a phone and leave your laptop on
and then you can like continue the work
on the phone. I don't think that model
is something that's going to stay. I
think it's kind of clunky and I think
it's like we think it's cool because it
solved one problem, but I think it's the
wrong way to solve the problem.
And you have cursor as well. Yeah, I've
I've been experimenting because I wanted
to automate uh some of these uh things
that I'm doing in my with my
opportunities and I'm tried the the
cursor automation. So with that I I just
want to say that the the the autonomous
agent is a little bit blurry because it
goes into some of these automations that
will be triggered either by time or by
some kind of event and we will see other
we we see it with GitHub and so on. So
they are in a sense also autonomous
agents because they actually do things
and you have you have to look at this
you have to know about it and that's why
we have it with here so that that you
can see for your reality your projects
which is the best tool uh for this and
and this is as I said to begin with
evolving fast and these things are I
mean barely days old right so it's going
really fast so how many people here use
cursor
very few Okay. Uh, OpenAI codeex, same
thing. Actually, very, very, very
similar to what Claude is doing. You
almost think that it's a cartel-l like
thingy because they're doing exactly the
same thing. Everything is local. And
they also have this like you can connect
to your phone and then continue on your
phone if you want to do that. Extremely
cool functionality. Not
um
>> then you have GitHub Copilot, right? We
need to go a bit faster because we need
the video and Q&A
>> co-pilot agents uh automations
that one is actually different. Those
are running in the cloud. You can put up
a there's four different triggers. You
can do it on an an issue that's opens or
PR that opens a PR sync or PR merge or a
schedule much like you can put up GitHub
workflows and stuff like that. And then
you have a number of tools available but
they're predefined, right? You cannot
just install other tools in that one. Uh
but then you can set these things up and
they are going to be running in the
cloud and there there you don't need
your laptop to be running at all times.
So getting started.
>> Yes. So I wanted to all of you to go
home and do this immediately. Not on
your company laptop even though Peter
Steinberger said you could. You are not
going to do that. what you're going to
do consider doing at least is the setup
that I had for Alex. So download an
Ubuntu ESU uh download VMware
uh workstation pro for PC or Fusion Pro
for Mac on this website I made for you
for you. You can find all the
instructions
u and there are some prerequisites. I
don't know what it's doing but and you
don't care. So it's just has to be
there. And I just want to mention a
small word about the different hosts. So
we have seen Mac OS, Ubuntu, virtual
Ubuntu. Hostinger is another example of
where one click, one button, one
[clears throat] click and you pay and
you have a an open claw running within
minutes. Um we saw Nvidia with Prev. Uh
you can even run it on a newer Raspberry
Pi. It has to be the four or the five
series. The two latest ones actually
worked with this. And just recently we
had Windows added to the family. Before
that I would have recommended not to do
it on Windows but now Peter Steinberger
himself says otherwise. So download the
Ubuntu desktop. It looks like that. It's
not complicated at all. You have to
search uh for the VMware. I've been
using VMware uh for many many years. It
was used to be paid. Today it is for
free and it basically look like this.
And I'm going to run a video uh because
it's faster this way. So I wanted to
show you the um entire installation
process. And what you do is basically
you go to the website and and you copy
this URL or copy this instruction. You
paste it in uh to the terminal and it
starts uh running the the installation.
It downloads everything. It verifies
that you have installed all the
prerequisites. When you go to my
website, you have all the instructions,
all the commands you have to run. You
don't have to understand anything. Just
have to run them. Okay? That you have
the right node version, the right npm
and so on.
It does stuff. Okay? It's fine. Uh we
trust in it. So, um you you say yes to
everything it's asking you, right? So, I
said you were courageous. If you're not
courageous, do not start this. Um it's
actually it's surprisingly easy and and
uh both on Mac and on Ubuntu. I haven't
tried it on Windows. I will go home and
and do that maybe. And uh you have to
choose a an AI model of course and and
in this case I I have chosen open AI.
I've been experimenting with um
anthropic also and I have been burning a
lot of tokens. At some point I was at
$25 a day. Uh then I unplugged the Bob.
I don't know what he was doing but um
>> selling drugs.
>> I can I can tell you specifically while
this is running uh what is it? Come to
uh the channel. So here you go. You're
going to choose Telegram because it's
just the easiest way to get started. Um
I was burning around $5 a day because I
just choose a default model like like
OpenAI. And when I changed the heartbeat
to run on Olama, it went down to 30
cents a day. Okay, so that you don't
worry about it to begin with, but
someday when you look at your account,
you're saying, why is it taking $25 a
day on on my anthropic account? So, next
up here, you of course you need skills.
You're going to choose these three
skills. You need the of course the claw
hub so it can go up and pick more
skills. um you need the GitHub skill and
and I also choose the password skill
just so that you can see how it goes on
afterwards. Now it's going to install by
default three skills and what I'm going
to show you is how to validate that your
your setup is done correctly. So it
installs this
and uh and I'm sharing with you some
tricks, some small tips and tricks. Um
uh and the first you'll see that um
well about the search engine I'm using
Brave search it's also for free up to
some number of searches and you need an
API key for that as well in the in the
demo I'm skipping that but um basically
at the end you get to the you hatch it
in the terminal and when it wakes up you
saw before that in the workspace there
is an an onboarding or what was it the
name of it the bootstrap or something it
there's basically an instruction that
tells it that when it starts out it has
to figure out who it is and who you are
right so the first thing I have to tell
it is who it is and I I named it uh in
this case because I started all over um
but you're basically telling it uh you
are in this case I called him Antworp uh
for the occasion not the city uh but but
the but not the person either. I changed
my mind in the middle of it. Um, and I'm
telling it who I am, right? And it it's
going to take that information and write
it down to uh the the the identity file
and uh maybe update the sole file and
and the user file. The user file is is
me, right? So everything is in markdown
plain text. And you saw Freddy taking
the approach of of designing all of that
to begin with, but in this case I'm
doing it a bit more uh stepwise. Now
it's up and running and and the thing
you want to check and my trick question
here is I am going to ask it um I'm
going to give it a question. Come on.
Yes.
This is the trick. You are going to ask
it for a weather forecast
because
there are more things in this. It has to
figure out that it needs a weather skill
and it has to have enough intelligence
uh to to say okay I can figure this out.
I have to go it actually the weather
skill is weather skill is installed by
default. You don't see it but it's there
behind the scenes and it succeeds. So
the first time I tried it say okay I'm
installing like a 20 gigabyte Olama
model and I'm going to choose that and
it actually failed at this time. So I
went back because I made a a snapshot so
I could start over and I I used the open
open AI had no problems in solving this
small problem.
So next up is a lifepreserving
action. I ask it to back itself up to
GitHub, right? So if it it cannot die
down there, if the computer disappears
or anything, we have a backup. And this
is useful because you will be able to
follow on GitHub as it gets more and
more skills, as it get more and more
memory, you can you can study it, right?
And by just by looking at the GitHub as
I as I showed before. So I'm basically
telling it where uh to store it. And and
there there's a small thing going behind
the scene here. I'm locking I'm
authenticating myself on GitHub uh from
this computer. So I did that. You don't
see it in the video but I did it uh on
the side and now now I can easily create
a repository. Of course you need a token
as Freddy said before that has all these
uh permissions and and so it doesn't
have u any trouble in [snorts]
in simply it knows what a workspace is.
it knows where it is and basically you
can see here that it has saved itself to
GitHub and it has to do that on a on a
regular basis. Right? So so this is what
it looks like and there you can see you
can see all of the files. It's
everything is plain text. Right? And
you're priming straight into its brain
for for information and you can you can
change it. You can improve it. You can
add more information in there. And it's
interesting to see for example how the
memory is evolving how the when you're
downloading skills you're curious you're
here to study you're looking at okay how
did they implement this this skill and
you can you can study it straight from
from GitHub right so that's very
practical
okay so next up is you want to install
telegram and the thing you have to know
about telegram is you need to find the
botfather
as you saw here the botfather that
basically spins up um a channel or or or
this bot and it gives you uh the
credentials and the codes to pair the
two uh and it's super easy and you have
it running and you can of course have
Telegram running on your phone
and as you see here uh it it's up and
running uh very easily. You get a code a
pairing code and so on. So that was that
>> that was cool.
What do you think about that? Like seven
minutes install open claw. That was
cool.
Call to action.
Try this at home. Now start thinking
about truly autonomous agents like what
scenarios could open claw help you
solve? Uh what tools and uh connections
are you missing?
Create your first openclaw agent. Create
your first skill. join our LinkedIn
group. We're going to share that in a
moment. Uh share your experience, your
ideas, your skills, talk about it, and
go forward with all of that. So, more
info. This is uh Finn's site about how
to get started on OpenClaw.
>> Yes, repo behind that.
>> Yeah, you will find a lot of of
information there. So, you don't have to
search for it. most people actually just
but it's it's to save you from from
looking at thousand YouTube videos and
everything but it's moving fast it's
changing all the time but you will find
a lot of useful information for example
about how much what is the configuration
of the virtual machine how much memory
CPU and so on uh should you use so so
you can use it and you can contribute to
it you have the link to my GitHub it's
open source and there's a ton of links
here you can take a photo of this one
and if you're missing conferences to go
to there's a claw con as well. That's a
series of conferences about open claw.
>> Thank you
>> with that. Thanks for joining us. Thanks
for staying and listening and not
falling asleep.
