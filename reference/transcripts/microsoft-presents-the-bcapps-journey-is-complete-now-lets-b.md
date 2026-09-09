# Microsoft presents: The BCApps Journey Is Complete — Now Let’s Build with Agents

- **Source:** https://www.youtube.com/watch?v=hlgaOZB2ZIg
- **Video ID:** hlgaOZB2ZIg
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 87m05s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

I guess after yesterday's keynote, there
is only one way to introduce myself. I'm
Yesper.
But besides being Yesper, I'm also a
principal engineer on the Business
Central team. Um, and for those of you
that are interested in Business Central
team's open source journey, you might of
course uh come across my name. uh for
the rest of you um you know B taking BC
uh to the cloud no not to the cloud to
GitHub has been like um you know my
dream um my main mission for the past
eight years so this session is actually
very very special to me as it marks a
massive milestone um but I'll talk much
more about that in a minute with me I
have Augustine
want to say a word or two about yourself
>> well uh hello everyone I'm Uh it's also
very early for me. I'm uh also an
engineering manager at Microsoft. I lead
the integrations team and uh this is a
pretty lovely thing to do this in front
of everyone. We were talking about busy
apps. We were talking about AI and all
of these things around for a while. So
it's nice to get here and share it with
you.
And also we have Jeremy, fellow MVP.
>> Yes. Uh I am not Yesper.
Uh, but I'm also not Microsoft. But one
of the things that is lovely about the
open source journey is that Microsoft
works with partners to help make things
happen. And a lot of what we're doing
today is presenting some of the
different ways that BC and partner
community can work together. So I'm
looking forward to representing that.
Right. So before we dive in, a quick
look at the agenda. Uh, so first I'm
going to talk a little bit about the
current state of our source open source
mission. Uh, and then I'm going to dive
a little bit deeper into the new agentic
vision that was presented at the keynote
too. Uh, then Augustine is going to talk
about building and maturing these agents
because that's actually much harder than
it seems. And then finally, but
certainly not least, Jeremy is going to
talk about this new initiative that we
have which is called BC Quality, which
is going to bring these agentic
capabilities out to you, make them
useful for you. And then we really hope
that we have enough time for Q&A because
we really would like to hear your
thoughts, your, you know, questions that
you may have to this entire thing.
Um, so what we will hope that you will
be leaving with today is kind of a
feeling for where we are, which is my
part, what's hard, which is Augustine's
part, and where you fit in, which is
Jeremy's.
So, as I mentioned in the intro, this is
a very special day for me. Um, it's
something that the Business Central team
and I have been working on for now I say
eight years, but it's actually even a
little bit longer. So, it's been coming
for a long time. The BC apps journey is
complete.
And that's how excited I am about that.
So, um, what's the BCF's journey? Again,
let's quickly remind ourselves. Uh it's
synonymous to the business central
team's co-development initiative um
which is the ambition to jointly develop
um the business central business
application together with you the
community and of course since it's a
community effort it's centered around
GitHub here right so whether it's
Microsoft whether it's partners or as
something new whether it's agents we
will all be working on the same platform
we can help each
you know, bring Business Central into
the future.
Um, and where were we before today? Just
a quick reminder, we didn't have one
repository as is what we're striving
for. We had four,
three uh GitHub ones and one internal
ADO. So, the first one that we had is
the 8-year-old one AL app extensions. Um
that was our uh the first one where we
originally only posted I think a handful
of firstparty apps just to see now how
is the community responding to that. Now
the problem was that the team was still
working internally on Azure DevOps and
partners would contribute to AOLAB
extensions
and already that was a little bit
confusing because it was just a copy and
to confuse it even more we also decided
hey let's put all the extensibility
requests out there which are not related
to the code that are in this repository.
So yeah then we decided hey let's make
this even more confusing. let's create
business central apps because we also
wanted to see how will the community
respond when we put the base app out
there because it's after all still the
repository with the most code right
um now this was a pilot but everyone
could join um and we started out only
with W1 but again internal developers
worked in Azure DevOps you guys could
contribute to Business Central apps and
then I had the very fun task of porting
these large PRs into our internal
codebase integrated to local countries
and I just hated that. Sorry to say but
that's another reason why I'm so happy
that we are moving away from that.
So now it's already been a little bit
confusing but then we decided to add BC
apps. Now BC apps was the first
repository which is truly open source.
So here we put the system application
but now both internal Microsoft
engineers and the community would be
working on the system application
together. And we then added uh a good
selection of first party apps. Um but
yeah, well are you guys confused by now?
I know I am. So it was about time that
we clean this up because you know having
four repositories with four different
workflows, four sets of issues and this
fragmented experience was just not
sustainable.
So no more. From today there is only one
repository and that is BC apps. Whether
you are community, whether you're an
agent, whether you are internal
Microsoft developer, if you want to
develop the business application of
Business Central, this is where it's at.
So let's roll a short video to make the
launch official of BC apps. Let's go.
Five 4 3 2 1
[gasps]
Huh.
>> Well, that was an unexpected turn of
events right there. Um, I guess first of
all, it's clear to see that I should not
get into the business of creating AI
videos. I'll leave that to everyone
else, I guess. Um, that's clearly not my
strong suit. Uh, but let's get a little
bit more serious. So I really wanted to
click the button today and say like from
tomorrow you know BC apps is the place
to be. Uh but unfortunately GitHub has
playing a few tricks on us lately. Uh I
think it's drowning a little bit in its
own success with all these agents
pushing in code. Um so it has been a
little bit flaky. Um but our engineering
system team is working really hard on
stabilizing these thing. So, long story
short, give us two more weeks and then
re-watch this video and then cut it in
the success part. Uh, but it will come
hopefully before this month is over.
Um, all right.
So, I do have a a repository that I want
to show you though, which is exactly
what you're going to get.
So, this is BC apps private as you can
see up there. That's the uh local fork
for engineering systems team working on
this. Um but basically I mean it looks
like BC apps right? Uh the big kicker
though is when you go into source and
you go into apps will find all the
country apps right and when you go into
layers
and you go into W1
will find the base application. But even
better, if you for instance go into
Germany,
you will too find the base application
and all the local objects for the German
version. So no matter which local you're
working in, if you have something that
you want to improve, now you can.
Going forward, uh things will, you know,
for now kind of stay the same as it was
on BC apps before. You are free to
create issues. um you know if you found
a bug that you want to fix just say hey
I want to implement or I want to fix a
bug chances are we're going to approve
that because bugs we just want to get
rid of right um you can also still go in
and say like hey there's this cool BC
idea that Microsoft never is getting
around to why don't I do it myself uh
and then you can suggest that idea going
to triage it and then you are free to
push in your code
um so I really hope that that's gonna uh
uh become a huge success.
Um yes. So BC apps now the single
collaboration hub for the business
application. Um
very important here all of this what
we're building is going to be built on
algo for GitHub. We had a session about
that yesterday which I hope you attended
when you're curious about that. But
basically what that means is I mean algo
go for GitHub is open source. BC apps is
open source and BC apps is using algo.
So if you want to have the exact same
build system or the exact same setup
that we have now you can and that's
really why we did all of this. So this
really levels the playing field um as
you know the business central
collaboration platform.
So the BC app's journey is coming to an
end then
and what a ride it has been. Um but that
doesn't mean that the uh story all up
ends. Um no it's actually quite the
opposite
because what this does is that this now
enables us to build the future right it
enables uh us to do what's next.
Um now it is time for us to reimagine
how this application platform is built.
Um, and you know,
with all these new things, I mean,
that's what this entire conference has
been about, right? Agents, AI, and like,
oh my god, how do we build stuff? You
know, it's it's a little bit hard to
just say, let's throw all of that
overboard. Let's skip code reviews. You
know, that's just not a thing anymore.
Let's just directly ship uh what the
agents code. That's not really a
comfortable feeling, right? Um so what
we decided was that we're going to use a
crawl walk run.
Um so basically what we're trying to do
here is we're in the crawl state. We're
going to experiment going to make sure
that the individual agents behave going
to mature them. Now when they do we
start walking we assign more and more
issues to them and make sure that you
know it grows with these. And the larger
the issues the more complex the features
get. um you know the more we are then
ready to get into the run state which
could be you know collapse all of them
into this uber agent engineer or
whatever the future may hold. I think
that's actually rather far out in the
future. That's a strange thing to say
when it's about AI so far in the future
maybe half a year but uh let's see about
that.
So what that looks like uh this crawling
state uh is what we presented
uh in the keynote yesterday. I do want
to add a few more notes to that though
for instance. So everything starts with
an issue, right? What's wrong with the
product? And here for instance, we I
mean we envision to have this signal
agent that could for instance be Waldo's
uh um project where he's looking into
telemetry and then trying to say, hey,
what's what's wrong with the system? If
it's find something, it will create an
issue and say like, hey, in this
repository, in this code, something
seems to be fishy.
Could of course also be things that are
coming from viva engage. in our case uh
could be you know bucks that you report
but it all starts with a signal agent
catching all of these diff different
signals and then making them accessible
to the community by putting them on
GitHub.
Then comes the triage agent.
Um now the the most important part about
this triage agent is not just to say is
this valid or not. It's just as much to
say how complex is this? How dangerous
is this fix? So if someone says like
well I found a typo in a tool tip well
fine you know go fix that agent. If
someone says well I'm getting wrong
lecture entries no agent don't go fix
that. We definitely need the finance
team to be included here or some subject
matter expert for instance you know MVPs
or other of you knowledgeable folks out
there you know it should then be marked
and say like oo this one's dangerous how
do we make sure that we build this right
and what would that cost us
and then the planning agent kicks in
once the triage agent has decided on the
plan for it or the path for it sorry and
then the planning agent will you know go
in and say like hey this is how I
envision that this is coded
And then that plan will be made
available to all of you where you can
see well is this right from a design
perspective and is this right from a
functionality perspective. So we've got
the engineer and the product manager uh
aspect of this. And once everyone says
like well this sounds like a sound plan
the development agent kicks in picks it
up develops it writes the documentation
all of the above and then hand it over
to the review agent. Um, and the review
agent then takes a different perspective
on this code and says, well, is this
code secure? Were there any performance
regressions introduced? Looking at the
larger picture until it's then handed
over to the shipping agent when that PR
has been approved. So, as you see in
between every single one of these
agents, there is still a human in the
loop. And very important, the agents
that we envision, at least the automatic
ones, they do not replace developers.
Even though the picture kind of looks a
little bit like it. No, but they, you
know, they help you. They help us
getting through the different stages.
And whenever one of these agents fails,
we can go back. We can improve it. We're
not going to say, "Ah, why did you do
that wrong? Let me just handcode that."
No, we're going to teach the agents to
do the right thing in every single one
of these steps.
So, let me just show you real click
quick what that looks like.
Um, so this is very early days, right?
And I'm I'm going to show you what's
actually on BC apps right now. Uh, but
then later on, Jeremy and Augustine are
going to show you what this is going to
evolve to in the very near future. So,
there's a a pull request here. All good.
Um, and then you can see, well, for
instance, uh, GitHub actions here kicked
in and says like, well, uh, here's an
issue.
Actually wanted to show this one.
I know something's fishy. Anyway, so the
the agent leaves a whole lot of
comments, right, that that you can fix
or not. And then very important here at
the bottom, you see, you know, was this
a useful comment? Was it especially
valuable? Or was it just plain wrong? If
it's plain wrong, we kindly ask you to
reply with why that is. Because that's
the only way that we can teach our
agents how to do proper code reviews.
Honestly, even if you use like the most
expensive models, um they still make a
ton of wrong code reviews when it comes
to AL code because I mean you might ask
the agent like, hey, you know, what does
calc do? And it will explain to you how
it works and everything and then you
give it some code with calcs and it just
gets it wrong.
So we do need to teach these agents uh
how to become better and also you
shouldn't always be running with the
most expensive models right it's going
to ruin us all. So how can we teach the
cheaper dumber models to also become
very good AL developers that's what
we're working on
and I just very quickly wanted to show
you you know what that looks like in the
code because it's actually really really
simple. Um, here in the GitHub folder,
you'll just find a GitHub action that
just invokes uh the agent. And the agent
as such is hidden in this folder called
code review hidden in plain sight. In
here, you have the orchestration. I'm
not going to go into detail of the
orchestration at all, but it just kind
of, you know, knows how to write these
commands on GitHub. Then it has a skill,
which you've probably heard more about
at this conference. And the skill as
such is simply like hey you are an AL
code reviewer and you are you know
specialized in architectural awareness
and so on and so forth. And at the end
of this instruction uh at the end of the
skill it basically just says like follow
these instructions and this is what we
have for now. It's not a whole lot. Um
but for instance if you go into
performance we've just written down what
we think is important when you do
performance reviews. Like for instance,
we've given the agent some table sizes
um so that it understands which table
should I be looking out for when I'm
doing the code review.
Um so yeah, that's the very early days.
That's the first step. That's how
everything begins. And that's where I
also would suggest that you begin when
you have any agent dreams. Start simple
like just get started and then evolve
from there.
have a second demo which is the triage
agent. Now that one is a completely in
prototype mode. Um
so this will definitely change
completely but the idea here is you get
an issue on GitHub.
Um and then right what it posts right
now is simply well AI triage completed
product groups please validate and if
you click here nothing will happen. But
when I click here,
I get
hopefully nowhere. No, now I got
somewhere.
Um, so what the review agent does is it
collects a lot of signal. It it tries to
look scout everywhere like hm what is
this issue about and is this something
that we should build? And in this case
it says well yeah well this is a strong
implementation candidate. Subscription
building is producing blah blah blah
blah blah blah. Fine. It it says, you
know, it has a rather high priority.
It's medium complex, medium effort, and
so on. Um, but let's take a look at the
rational. How did it get to that?
Well, the complexity it says uh well,
the likely fix subscription building
document generation path rather than a
base posting and so on so forth. So, it
says, you know, it's probably medium
complex. The value is high um because of
all of that. Well, you get the picture,
right? Um then the important part is
this implementation path. So here it
says well a human should choose the
exact correction strategy whether to
reenter standard sales lines and so on
right. So it says well there needs to be
a human in the loop for this one for
sure and it's it's actually taught to be
a little bit cautious and not say like
hey I can do that because by default
they are very uh you know they like
themselves very much these live language
models. So you got to tone them down
just a little say like hey you know be
critical here.
Um so it calculates the priority out of
the value and times the urgency over the
effort and the risk and then it says
like well you know on the backlog this
should range in this area. The
confidence is calculated based on the
quality of the issue. Is it a clear
issue? Is it reproducible? Do we have
enough context to be sure that this uh
you know is is uh that we know what the
issue is all about. Are we specific
enough and is this actionable?
And all of the above just to show you
what the sources is actually crawling
through is like for instance we go
through BC ideas and say okay how many
BC ideas are related to this. The more
ideas there are, the higher it's going
to climb on on our backlog, right? It's
going to go into community discussions
to meu dynamics user well you name it.
Um soon also Viva engage of course and
it says like you know strongly relevant
because it directly discusses the same
configuration area and so on. Looks at
the competitive landscape looks at the
marketplace if there are many that are
trying to fix this or many that are
depending on this. It also gives you
some learn articles in case that you are
not so much aware with this particular
issue but you want to learn more then it
kind of hands it to you on a platter. It
even goes to YouTube in a buck case
that's nonsense so that needs to go
away. Um but you know there might be
videos where they're talking about oh
wouldn't it be great if Business Central
could do this and that that we're also
considering and of course it looks at
the code. So you get the picture.
Um the triage agent um is going to help
us a lot to assess
how we should build this uh this issue.
Uh why is this prototype and nowhere
near ready? Well, that is because I mean
you saw the sources that we're going
through, right? That's probably not how
you triage your issues. Um so I mean you
won't be looking at BC ideas most likely
because there's probably nothing there
for you. So when we build this triage
agent, we need to build it with
extensibility in mind. It needs to be
just a a core skeleton and then you get
to decide which connectors, which
sources are relevant to triage your
issues. And that makes it a whole lot
more complex. But that's what it takes
for us uh before we can say here's the
triage agent um and now we're going to
make it part of Ago for GitHub.
Yeah. So that brings us to the end of
the first section. Um what will the
future hold? Uh the agent framework will
slowly but steadily light up in BC apps.
You will see more and more agents being
there uh to help us get the issues into
the product.
Um you will be able to just grab these
agents right off the shelf with Algo for
GitHub. division being that all you need
to do is enter your uh um LLM key and
then you're off.
Um and that you then get this by default
if you want. There's no complex setup
needed. Uh you're just good to go.
Um and these behavioral rules and best
practices uh should of course be
configurable.
Wait, that's not something that I spoke
so much about, but that's exactly where
Jeremy's going to come in. He's going to
show you later how do we envision that
these agents become configurable.
Finally, uh before we hand it over,
before I hand it over, let's talk about
the elephant in the room. [snorts]
Um when will you be able to see all of
these agents in action and when will you
be able to get their hands on them? Now,
that's a little bit more complex than
such. So, I wanted to hand it over to
Augustine to say to to show you like
>> what's the challenge here? Why aren't we
just, you know, sprinting ahead?
>> Lovely. [sighs]
Thank you. Thank you, Jasper. I have to
follow Jasper and I don't have, you
know, funny rave songs and I don't have
um nice personalized pictures. So, I was
wondering what I could do and I just
>> Well, at least you didn't burn a
rainforest to create the slide
[laughter] deck.
>> Made it black. That's That's all I can
do.
>> I also save it. I'm also uh improvising
a little bit too much. So you have a
task to try to figure out when I forget
what the slide is and not you know see
if you catch me up on a on a going back.
This is the message that I want to say.
Agents are easy like creating the first
agent the first orchestration get it to
run getting to fix your bugs you can do
it after we exit the room. So I will
challenge you. You haven't played much
with like creating a skills and and
running it and just just try try before
the end of the conference because that
part is very easy because you are anyway
you are checking it yourself. The same
way that when you're calling claude or
you're calling copilot or whatever it is
you are going to run it and then
validate if it did a good job.
Tricky part is to get it to production
ready. Right? So is to actually get get
it to be autonomous. Get it to minimize
the amount of effort everyone has to
put. And that's what I'm going to talk
about. I'm going to use the same example
that Jasper gave uh the PR agent
reviewer and I'm going to show you more
or less what is the journey that we had
to go through.
It's a little bit superficial. We don't
have a ton of time. So if you want to go
deeper into some of the things that we
are uh going to be talking well there
were some cool sessions yesterday but
there is some new ones today uh that
will dig deeper into some of these
things.
Um [sighs]
so what I would recommend you is as I
was saying walk outside create the skill
play with things started small and then
slowly but surely earn earn the autonomy
right
this looks something like this you start
with that you know initial prompt that
I'm assuming most of you um have tried
and played with and whatever is your
favorite harness
and then you start making it available
for the rest of the people. You you
share it with your organization. Then
you make something like everyone that
fixes a bug should run this skill. And
eventually you say, "Oh, why do I need
anyone to write the skill? Maybe I can
just ask u one of these magical beings
to run it for me." And uh slowly but
surely you move that ladder until you
can get to a place that you can trust
and you can run it which is a journey
that pretty much everyone in the wall is
trying to figure out at this stage.
Um
oh
this is slightly different. This is not
the right slides. See the first
improvisational part.
So you caught me in the improvisation.
So what I wanted to say is like we did
we did that right as we started back in
the
back in the I don't know six months ago
or so we started just playing with
things we created some instruction this
is not even you saw that fancy structure
that um Jasper had and um
>> this is not even like this is a
performance instruction that says in
there but at the top it compiled the
instruction. It's the first time we try
to ask our agents to or agents or uh
scripts to do a a PR review. And if you
can read it, it shows a nice table with
uh table sizes because we were trying to
get this agent that didn't know much
about BC and AL to understand that some
of these tables in your customers may
have ton of records like tens of
millions of records
uh to see if you will be able to catch a
performance regression.
And as I was saying on the left, uh the
first orchestrator is you. You just
don't need an autonomous agent to go and
run stuff. You write down a prompt and
you tell it go and take a look at my
performance instructions and validate
that this code actually um is doing
something naughty. And that that was
actually my my chat to Jasper like maybe
six months ago saying hey I got it to
work is actually figuring out that this
will screw up uh our performance in
production. Um, and so what I was doing,
let me go backwards because that's what
I was saying.
That that loop that you want an agent to
do, absorb, decide what to do, run some
code or validate a review or check your
security and then you know ensure that
everything is right. It is something
that you can do. Maybe let me swap to
the other computer for a second because
I have I wonder why this didn't
>> Yeah, that's happened when you make
lastm minute changes to the slide deck
because my computer is not wired up to
the internet right now.
>> I made those changes longer ago.
>> Let me grab this for a second.
And
yeah,
tada. Good. [snorts]
Lovely. [clears throat]
Yeah. So, as I was saying,
I is changing yours. [laughter]
Okay. Again, improvisational time,
right? So, let's let's make this
properly.
Now that you have that skill, right? You
you have that that prompt. You have that
first attempt at fixing things. Um let's
make it common. Let's put it in a
version. Let's put it in a repo. Let's
share it with the organization. Let's
ensure that not every one of you have to
figure out that we need to write a a
complicated prompt, right? Like you
don't have to write every time, hey, be
careful. This is a code. Hey, be
careful. there is all of this uh large
tables that you have to take into
consideration. So from now on um we just
create a skill and Jasper show it to you
before but I want to
like like Jasper show we end up with
like a very structured folder. you have
a skill that now you can just go to your
you know copilot cle or you can go to VS
code and do whatever and you just say
hey go and review my code and because
everything is encapsulated in that skill
now it knows just go and and check for
performance check for security and give
me an output and then then I as I as an
engineer I will validate
again this is still you right it's not
autonomy you're still running this
you're still checking the results. It's
just on your machine. It's not. But now
someone else in the organization can do
exactly the same.
[snorts] And now it comes starts to
become a little bit juicy.
Replace yourself. Now, now we want to
get into that workflow. We want to get
something else to run it for you. You
don't have to come into manually and and
run it all the time. Um so start pushing
it somewhere else. And when we started
doing this,
there was not a lot of options.
But as I'm sure you're aware now, AI
world moves fast, very fast. So Jasper
show that PowerShell script that we had
in there coordinating the uh the
execution and the orchestration and we
have uh pretty fancy GitHub actions
running behind the scenes, spanning new
uh containers in order to run all of
this. But if you want to start doing
this these days, this is much easier
actually.
[snorts]
You have things like
you have things like um
um agents in GitHub. Right now with
agency in GitHub,
you can actually just pass all of the
instructions, tell the skills, you can
set it up to run on pull requests and it
will automatically um run a session like
the same thing you will do locally. You
can actually run it on the cloud and and
this is maybe a small
uh teaser, but you can do very fancy
things now with this. Uh this is
something we're working on that we hope
that we'll be able to share sooner than
later.
Uh but you can get those online agents
to actually span a container. And you
can see that it's installing, you know,
busy container there and it's setting up
all of the necessary work from the
environment. So when the agent is
running is running on a valid busy
container that they can execute, they
can compile code, they can get all of
the necessary bells and whistles that we
before had to do manually. So this is
you know go to your favorite um platform
and start pushing those skills to
something that can run uh autonomously
in the cloud. Again we are still not in
the autonomous phase. So be careful with
um what is running and we will get to
how you go to more autonomous but
continue validating that the outcome is
the right one
and
this is where you know things become a
little bit uh trickier right now you
want this to you don't want to be the
one like checking every step of the
process you want to have clear gates
like Jasper was showing before we are
running this we generates a PR at the
end. We want to validate that everything
is right,
but you don't want to have to like
validate every step on the way. And
that's where,
you know, you have a bunch of work um
[clears throat] to do. This is where the
engineering piece comes in that normally
people don't talk that much about. But
you need to ensure that if you want to
automate this, you need to ensure that
the the context that comes in into the
agent is is trusted that um the input
and the output is secure and there is no
options in there to get strange uh
instructions to come in. If you want to
do something autonomously like fixing
bugs or code reviews or think very hard
about how noisy they are going to be,
right? If you suddenly throw 300 pull
requests to your developers, they're not
going to like you very much.
So think about how you do that in a way
that most of the things that the agent
is generating
are actually signal and not noise. and
be sure that you can, you know, keep
track of what happened. You run a static
tooling, all of those things that you
normally do in CI/CD, you should think
hard how that agentic loop is actually
um incorporating them, right?
>> And speaking of like signal to noise, a
big part of the challenge of what we're
experiencing as devs is everyone's
talking about my agents are doing all
this extra work, but how many people in
here actually trust their agent to fix
everything?
No hands. [laughter] Exactly. Because
we're the quality control. We we need to
make things boringly reliable. So, it is
important for the folks in this room to
learn all these things that aren't on
LinkedIn, that aren't being promoted in
blog posts, these important uh controls
and quality.
>> Absolutely.
So then we went to that thing right up
until here is a great prototype and you
can you can quickly get all of these
things in. You just need to write a
skill actually ask your you know LLM to
write a skill for you based on whatever
session you've been trying to do for
fixing a bug. You can share it. You can
version it. You can work into like you
know how do I make this more stable.
But the tricky part with all of this
work with LLMs um is can we trust what
they why they bring you and this is
because you know inherently anything
with AI is a statistic is not
deterministic like we are used with
code. So how many show hunts? How many
know what evals are? And because there
was a lot of stuff.
Okay. Cool. Uh so this is like there
were more advanced sessions and there
will be more advanced sessions. So we'll
just brush over and show what some of
the things that we have to do. But that
is the tricky part. How do we get it to
be something that we can trust?
And
it it it it it
lets you [sighs]
bring in some less chaos in this, you
know, wall of of confidence. And and
the this is the part that you're going
to have or at least we've seen that we
consistently spend most of the time
there. And I'm going to give you a tweak
that both people talk about offline
evils and online evils is maybe a little
bit simplistic but think about them as
offline evils are your tests but they
are the test that you run against AI
and online evils is your telemetry is
your reports that look at what is
happening production.
You can expand it a bit more than that,
but it's a good mental model to think
about these two. And you're going to
have to do this if you want to say,
okay, I can run, you know, my automatic
bug fixing skill to um to fix most of
the bugs in my system, right? And I'm
going to start with online evils because
they are maybe uh a little bit simpler
to understand. Again, it's mostly what
you used to do before with telemetry and
dashboards and and all of these things.
So once you have something running that
uses LLMs um you must like even more
than before check how good is doing
because there is so many chances that a
new model or a new a small change on an
instruction or you know the flavor of
the week that they made that change
behind the scenes it's going to screw up
with your results and that is kind of
what we had to do. Uh so talking again
about the PR reviewer,
we had to build things like this, right?
And this is this is some of the metrics
that we were tracking every time we were
looking at a new pull request. So we
build this we look at how many people
are accepting the comments we create,
how many people are rejecting the
comments we create, what are their code
changes after. Um you saw that thumbs up
and the heart that Jasper did right so
we we went pretty pretty detail into
this stuff right so we will be tracking
consistently every time an engineer will
say ah that comment wasn't great uh this
is why this comment wasn't great and we
will be looking at the different uh type
of domains that we have right see which
ones are doing better which ones are
doing worse
um and even to the level of like
tracking individual commands and replies
to those commands to see okay this is
why this is not working what did let us
do so very quickly we will see when if
we make a change to the performance
instructions and then suddenly this
takes a dip that's not a great sign it
also let us do cooler things like now we
can pick up all of those comments about
why this is not working and give them
back to the PR reviewer and tell it hey
this wasn't
How will you improve yourself? And we
end up with good things like
uh where did it go?
Or self-improving. So this is
periodically running and grabbing
anything that people say this is not
great and then coming up with a solution
and trying to constantly trying to
improve itself. And now we get into a
tricky thing, right? We don't want to do
this for then coming back and
all the way down to where people are
already suffering see that this was a
terrible change. [sighs]
That is where [gasps]
offline evils come in.
And I want you to think about this and
this is probably the trickier part. Um
you are going to have to test what your
agent does, right? The problem is it may
be very different. You may be bug fixing
in one site. You may be code reviewing
somewhere else. You may be creating a
security thing or triaging an agent. So
one of the tricky parts that you have to
think about is okay what what are some
of the cases that can prove that this
works well in the PR reviewer is it was
pretty obvious is previous PRs. So we
look at all their PRs. We see are these
comments great? Do we create new
comments? We create synthetic PRs and
then we're going to use those to test
this and we're going to have to figure
out what is success uh in the triage
agent is trickier, right? Because you
end up with like a big report, right? So
how do you know is this a good report or
not?
>> Yeah, I actually started trying to do
these uh offline evals with the triage
agent. Turns out the triage agent says
you should build all of these things and
our product manager says you should
build those things and there was
virtually no overlap. I was like, okay,
there's something that needs to give
here, right? So, so this is actually
it's a very healthy exercise to say like
how should this agent work? What does
our organization think about this?
>> So, you're going to have to think about
that. You're going to have to think also
what are the metrics you want to
measure, right? Again, in the PR
reviewer, uh you want you want to be
sure that the comments that you're
expecting and there are no comments that
you're not expecting are in the PR. Uh a
bug you want to validate that it works.
So probably you're going to have to find
a way maybe run a test and you will hear
more about that in BC bench session like
a test that you can run to see that it
did the right thing. But at the end of
the day, you're going to have to end up
with a proper set of metrics and a
proper set of um data sets. And that's
what we had to do. We ended up with
uh offline evils. And there is a ton of
like cases in here as you can see. I'm
not going to go deeper. Maybe I can show
you one or two of them.
Uh see, so this is a PR and it's
>> very tiny though.
>> It's very tiny. Let me make it a little
bit bigger. [snorts] and it's expecting
you know a comment in line 21
that is kind of like this you still need
to get probably an LLM to to evaluate
that is the right comment
and so it's expecting for all of these
test cases that we are running is
expecting that it generates this thing
so now I can do nice stuff I can go and
modify a um
a one of the domains you can see in here
Maybe it's big enough. Good.
That we are modifying the style domain
based on particular one fixes in APR.
And it's applying this change. And now
it's running all of the evaluation,
right? And it's telling me, oh, overall
this is 90%, be careful about what this
change does. This is the findings. This
is the ground truth. There is a proper
calculation in here. So when we go and
say now I want to you know improve my
security instructions before I can say
yeah I'm going to put this to production
I need to get good numbers in here.
Good. But that also shows how important
it is that when you're rejecting
something like even in your own
organization when you're trying to train
these agents. So instead of just saying
like won't fix this is or
whatever you know do take the time to
write why this is a wrong command
because then you can build these
self-improving loops where an agent
picks up says ah okay so I got this
wrong and this is how it's right now let
me rewrite the instructions. So you'll
get this self-improving uh system which
is so much more fun than you manually
having to update your instructions or
even manually having to ask an agent to
update the instructions. So the more you
put in initially the faster you will you
will you know see great results
>> and it let us do cool stuff. There is a
session after this one uh called busy
bench which and you heard about it also
in the keynote uh about benchmarking and
stuff. So it let us now we can run all
of our PRs all of our synthetic offline
evals as part of this benchmarking tool
and get like similar results right
precision macros uh F1 all of these
metrics that let us know how good this
is doing. And now we can do fun
combinations. We can try different
models. We can try to like use a cheaper
model maybe for some of these pieces. we
can try to do something like BC quality
that we'll hear in a few minutes and we
get like a clear measure like are we
improving or we are not because we have
no idea unless we get some numbers.
Uh so I recommend you you go to that
session in like an hour time [sighs]
>> and a quick check how many people are
still kind of starting the agentic
journey in the room
>> still quite a lot of people so if you
were looking at eval going I'm not
entirely sure what to understand out of
this how does this become part of my
journey remember that techdays on
mubuso.tv TV is going to have this great
session. In about a month or two, you're
going to go, "Oh, thank goodness he just
explained how to eval these agents." So,
make sure to mentally bookmark this as
something to revisit again because it's
improvement. You're going to want to do
improvement loops.
>> And and and just to be fair, I I said
before, this is the tricky part. This is
the hard part to get here. So, until you
actually get your hands dirty, it's
going to be difficult to pick up all of
the nuances. But remember, you have this
part of the journey to do if you want to
get to truly autonomous aliens.
Um, we are still going through this,
right? We're still learning a ton of
stuff and figuring out how to do this
for all of the domains we are automating
>> and we promise to share with you as we
go along this journey and make these
things available to you. Like just
yesterday with this BC bench uh you know
there was a question uh that I got like
hey you guys mentioned you have 103 uh
you know of these scenarios how comes on
GitHub there are only three well the
answer to that found I found out
afterwards is that we are still as I
showed earlier we're still running
internally in in uh in Azure DevOps
right um and and the tests are depending
on whatever is down there so they
wouldn't make much sense to you right
now but again since we are now moving to
BC apps in two weeks time. Uh then all
of our code is there, all of our build
system is there, all of our commit
history is there and then we will also
be able to share uh our benchmarking
tools. So you can kind of tag along and
all of the code whatever it is that we
are doing, you can at least see ah okay
so this is how how it's built uh by
Microsoft. Anyway, so this is my last
slide. Um as I was saying, it let you do
cool things, right? that in the moment
you have this properly set up is when
you can do this scientific loop of like
oh I'm I I have an hypothesis this is
not working great uh I'm going to try to
modify my instructions or my prompt or
whatever the tools that I give to this
agent and I'm going to first apply it
replay the things through the offline
evals if those do well I can ship it and
closely monitor it with my own line
evils until I see what works and what
doesn't and then with that learning
story we can go back to this loop right
is the is is what we are trying to do
with everything we're iterating on and
as soon as you have the first version
you need this you need to know if that
new context that you're giving it or
those articles or what Mr. Jeremy is
going to talk about like you saw that we
have those instructions in there for
security and performance and and all of
the rest they were hidden within within
the the PR review agents but that
doesn't make sense right because this is
something that everyone can use this is
something that the community knows many
cases better than we do so why not you
know make it something that everyone can
contribute to so that is one of the
experiments we're running now we are
moving into this different model and we
will go through this journey to see that
that actually works as we expect
>> and eval as the release gate. I love the
explanation on that. But if you're just
getting started, think about it this
way. When you meet with a junior
developer and they did something wrong,
you might do pair programming. You might
do code review work with them. You might
even say, "Okay, I need to get them into
some training. I maybe need to do some
sort of new certification story." This
is that story for agents.
This is the process where you make the
agents go through that process because
after all the agent gets thrown out.
What persists is your instructions, your
skills, your harness. So this is the way
you can simulate that agent takes all of
your skills, your argent agents, your
harness, all of those different pieces,
test runs them and go, did it do a good
job? And if it didn't do a good job, we
need to send it back to class. M
>> and that's due.
>> Sure. Sure. White again. [snorts]
>> Yep. Nice. Nice blam. Flash blank for
everyone. So uh BC quality is kind of
the next topic because it is one of the
ways that we are bringing uh more
knowledge and more skills from the
overall community into the ecosystem. So
quick question for you. How many people
in the room have tried out BC code intel
MCP?
That's actually a pretty good showing.
Awesome. Thank you everyone. And that's
part of why I got invited to spot uh
work on and participate on BC Quality is
because there's a lot of lived
experience with that tool. For people
who didn't know, it was an agentic uh is
an agentic library of a lot of BC
knowledge that agents can use on demand
to solve different tasks. It's a
pre-built harness built off of AL
guidelines and a lot of my experience
and that's been improving and iterating
for several months. But, uh, one of my
favorite moments after I released that
to the community was, does anyone want
to guess how long it took for someone to
say, "But we don't do it that way."
Anyone think that it was one day?
[laughter]
Does anyone think it was one hour?
>> [laughter]
>> it was the very first hour someone said
we don't do it that way so I can't use
your tool so that's what we learned uh
what I learned as part of running that
system is that one size fits nobody
u immediately people wanted to say yeah
but in Germany we do it this way and in
Czech we do it another way so we ran
into non-stop problems not only in the
localization story but also in the
partner story um unfortunately we're all
exceptional uh partners as in there's
always exceptions.
[snorts]
So um the challenge with introducing a
tooling that is supposed to be this is
the way that you do things. It we can't
be that prescriptive. We cannot be that
clear. So any sort of knowledge tooling,
there's a bunch of things we can all
agree on. The platform rules, some of
the performance rules about how to use
things like set load fields and all
that. That's consistent for a lot of
people, a lot of organizations, but even
then there may be exceptions.
So what I got push back on is we need it
to be configurable and we need to add
our stuff. I worked with Danish partners
and Belgian partners. A whole bunch of
different people said, "Yeah, but we
have some extra rules that we want to
add." So we Yesper and I got together
and said, "We need to bring this bigger.
We need Microsoft to contribute
knowledge to these sort of toolings, but
we need it to be the default because
agents are spinning up all the time, all
the time. So let's introduce BC quality.
BC Quality is a lovely new repo on
GitHub that is the Microsoft uhBC
quality. No akams, it's nice and easy.
We're developers, we love GitHub.
Um, and the idea behind BC quality is
that it is the knowledge an agent needs
specifically that a model would need to
know these things to be able to work
with business central code. And it's
also useful for agents working with it
and humans working with it. Now the
knowledge that we've migrated so far is
around performance and security because
we can do easy evals for those things.
We want to make sure that the engine is
working right with two very measurable
areas before we before we start doing
like the fun flavor things of you know
action bar recommendations and fast tabs
and all those sort of things. We want to
do the hard stuff the measurable
improvements. And what that started with
is all of the performance and security
guidelines that came out of
alguidelines.dev as a project.
So if you look at the BC quality repo,
you're going to find that it's this
forest of all sorts of different
knowledge files. And each knowledge file
is designed to be consumed very easily
by agents to be able to be token
efficient, to be very smart in
pipelines, not burn through your very
precious and shrinking budgets. Um, and
it's built so agents can use it. So, uh,
rather than spend all of the time just
talking theoreticals, I want to show an
hands-on example. Uh first off, so
Yesper set up a lovely test drive of BC
apps running against BC quality and we
can see that as part of a poll request,
we got a code review from our GitHub
actions bot and we have a high severity
performance issue. Okay, so open uh has
open sales orders is using count where
it really it doesn't need the record. we
don't need to do that cache hit. So is
empty would be the right way to do that.
And we can see that it's giving us the
ability right in that pipeline to apply
that suggestion. And we can absolutely
give lovely advice uh response back to
the feedback team. But you can also see
where did that knowledge come from. So
this links right through to the exact
knowledge file that that data why did
that happen that way? Maybe you have a
specific reason in your organization
that you don't follow this pattern. So
what do you do? Well, what you do with
that
is BC quality is layered.
BC quality is built in mind for the fact
that there's different needs for
different circumstances.
So the way we've structured all of the
knowledge files is into three main
layers. Microsoft is going to constantly
contribute all sorts of great
engineering practices that everyone can
benefit from.
And then we also have, lovely enough,
the community layer. This means that all
of you, as you find your agents are
doing something really daffy.
You can absolutely add this to the repo.
Nice and easy. Just do a pull request,
get this into this. But if it's
something special about your company,
your products, how you support your
customers, what do you do? The repo for
BC quality is built with an empty custom
layer and that is designed so that the
skills know where to find any custom
instructions. You can clone this repo,
fork this repo, bring this into your
organization and populate that custom
layer and know that you can always keep
things in sync.
And the great thing about that is that
if you make some sort of new rule and
you're testing it, you're doing eval
organizational and you go, you know
what, I think this should be a community
rule. You can absolutely do a pull
request to move that back to the
upstream repo. And then we're going to
look at whatever comes into the
community layer and say like, "Wow, this
is so good a rule. It should apply to
everyone because it just makes sense."
And then we're going to lift it into the
Microsoft layer. And it's not just us
designing it. This is a community
effort. So even you can suggest hey I
think this should be moved into the
Microsoft layer. We have to approve in
the end for that layer because you know
it's very important else our agents go
off rails. Um but other than that also
feel free to make suggestions like hey
this rule should simply apply to
everyone because it's so good.
Absolutely.
So uh just to take a look at
mechanically how does this work? Uh
what's in this repo? Uh first of all the
readme is helpful.
We we have a readme. Everyone does
useful readmes, right?
Yeah. Um so first of all, it outlines
that we've got the knowledge files. This
explains that you can have this as a
repository for not only the knowledge
but also skills that you develop. So
when people ask the question of I'm
developing all these cool skills and I
want to share them with my team. How do
I get them to my team? Well, this is one
of the ways that you can not only get it
to your team, but you can also get them
to your agents and have the
infrastructure understand how to work
with things. And then the very next
question that I got once we started
talking about this a little bit, some uh
mentions of it online, the top question
I got is how do I get started? Well,
right now it's in preview. Um, algo is
working to start to consume this, but we
made it easy to get started because some
of the builtin skills in BC Quality have
some agentic skills that get things
started. And there's a nice easy one
here, the entry point skill.
This is the instruction point where your
agent, you can point it to it and say,
"I need to use this repo, but I have no
idea how. Go get it."
Um, and additionally then there are some
skills around reading and doing and
that's how the agents are actually going
to make use of this. So if you're
looking at how do I start building
skills, good news, there's some uh
reference material.
But then one of my favorite skills is
there's also a nice one to create new
knowledge. This right skill, how do I
know what a good knowledge file looks
like? How do I know how to create
knowledge that I could contribute back
to the community layer or use for my
organization?
We have a bunch of cool stuff built into
the knowledge files. How do we know how
to do the different formatting? So,
there's a lot of great info in here.
For example, a knowledge file is a YAML
file because after all, it's it's
language being poured into an agent. But
rules don't necessarily apply to all
versions. How many folks slept on things
a little bit and then version 27 came
along and you had a really bad month
when number series officially moved.
[laughter]
>> Not too many. See, isn't that much of a
problem as you always keep saying?
>> Ah, no one wants to raise hand in a
Microsoft session. I get it, guys.
[laughter]
But some of the knowledge files around
number series are different. If you're
working with an older client, you're
supporting an on-prem client. So, how do
you create knowledge files around number
series for the older clients you're
still maintaining and uplifting to the
cloud? But it's a work in progress. So,
there's front matter here that allows
you to tune your knowledge to the
different domains. Is it related to
performance? Is it relating to security?
Is it related to specific versions? And
then there's stuff that's also
localizations. My company is based out
of Sweden. We uh have the Swedish
localization app. And there are key
things about uh the infrastructure of
how we do business in Sweden. So
absolutely we could create knowledge
files that are specific to what we're
working with for our PTE because all of
our PTE are based in Sweden, but all of
our apps are worldwide one. So we can
make knowledge files that make sense for
the context in which we need them. Also
the the previous project for these
patterns was called AL guidelines right
here we called it BC quality because as
you can see there's also a technologies
front matter because not every code that
we're writing anymore is AL right
Business Central has so many other
things you know like Walder could tell
you a story about how to write KQL we
don't want to write that ourselves
anymore but there are certainly good
rules for how to query uh telemetry
that as well could be a knowledge file
that is absolutely applicable for
Business central. So at the end of the
day, I hope that this is going to be
this shared repository that everything
that is useful to agents for working
with Business Central, no matter the
language, that's going to be found here.
And if you want to just try this out on
some of your existing code with what's
already in here today, just point your
agent at this because Yesper, lovely
enough, has already written in here.
There's a agent consumption guide that
the agent will load this repo. it'll
read this and go, I'll give it a try.
So, if you're not using it as part of
your pipeline story, your automation
story, you're getting started and you
just want to open VS Code and try it,
you can still do that. Lots of different
surface areas because all of these
different things can be used in
different context.
>> Putting you on the spot here, Jeremy,
why isn't this an MCP?
>> Why isn't it an MCP? I don't know.
That's a good question. Let's talk to
the AL extension team. [laughter]
>> As you see, this is very early, right?
it's it's preview. Um, but we are going
to hopefully very soon and and Jeremy's
going to show that in a minute. We
hopefully going to see uptake of this
and then hopefully it's going to very
quickly evolve and then we're going to
see it all the different ways that we
can make this available to you. Uh, also
like maybe you don't want to use GitHub,
right? Maybe you just want to be in
Visual Studio Code for the time being.
Wouldn't it be nice if there's just an
action to say like well connect me to BC
Quality, get those rules in here and let
me get started. Um, so all of these
things we are considering and we would
appreciate all that feedback. So you can
lock issues on the BC quality. It
doesn't have to be around, hey, could I
add this in this knowledge file, but
hey, could I get this in Visual Studio
Code piece because that's what I need.
So give us feedback and then we can
evolve this project to be exactly what
we dream it will be.
>> Yeah, absolutely. So to understand how
this kind of connects with some of the
different pieces that we've been talking
about uh is that the agentic
orchestration the harness these are the
things that we've seen so far in the in
this session about algo is going to be
building all these agentic skills and so
for those of you who are algo uh GitHub
users you're going to have this
experience over time become part of your
default behavior. So this is just going
to be something you just get. But and I
I'm this is the I'm not Microsoft so I
can say some of these things. Uh the
knowledge file being a separate repo.
How many folks in the room are Azure
DevOps users still?
Yeah. Me too. So Algo story I love the
agentic orchestration story that they're
building but I need this quality data in
a different way. And that was one of the
reasons that we architected this at the
beginning and said let's get that
knowledge surfaced because it needs to
be agentically consumable in pipelines
like ALGO for sure but there are still
plenty of partners who have very
legitimate reasons that maybe they're
not using ALGO that's okay but we should
make sure that this is available but we
also wanted it to be human consumable we
wanted to be part of your VS code your
cloud experience uh whatever your agent
toolings cursor all these different
frameworks works, you should still be
able to leverage this value. So that's
part of the idea of the agent has a lot
of the engine, the orchestration, the
harness, and then the Microsoft uh
community layers uh and your custom
layers go together.
So, uh, let's look at an example of, uh,
how the heck did Yesper set up that, uh,
because I think it's actually really
easy to see an example. Um, how hard is
it to plug and play to work with your
own choices? Well, uh, your lovely
example that you set up for our demo
today, uh, this BC apps BC quality, this
is Yeser was test driving BC quality
with the base app.
So, um, we have this lovely little
settings file. It's just a YAML. Nothing
nothing too scary. I hope everyone's
comfortable with that. Um, but what we
have here is a great amount of
documentation. Uh, the repo URL by
default, Microsoft BC quality, but you
could fork this. You could move this to
your own ecosystem. Just change where
the repo is pulling from. Okay, that's
pretty good. Um, and then one of the
things that I love about this layered
approach is you may decide I don't want
to use the community layers for some
reason. Well, you can absolutely because
these knowledge files are broken out
into those different layers, different
rules can apply to different contexts.
So, for example, working with the base
app here, we only want to enable the
Microsoft layers. That becomes very easy
for the agents to understand. Maybe if I
may add, if you scroll up a little bit,
you saw like this was pointing to the
main branch down at the bottom, right?
>> Uh that's probably not how you want to
do it because the main branch is going
to get updated with every single pull
request that goes in, right? So your
agents will just start behaving
differently as time progresses. So you
will probably want to say, well, this is
an improved version or one that we've
verified of BC quality. So we're going
to stick to this commit. And then you
will do some again, that's where the the
testing come in. And then you say like,
hey, you know, now a month has passed or
two and there are so many great new
knowledge articles that my agent should
know about. I'm going to try to take a
newer version of BC quality. I'm going
to run my evals and see, you know, did
all the wheels fall off my agents or is
it actually still, you know, good. So
that's how you were you're going to
control that.
And then [snorts] in in the lovely sort
of sense, Yesper also provided us
examples of uh being able to disable
skills or be able to restrict individual
knowledges, tasks, uh you know,
different countries, whatever sort of
logic you need to have. Because these
are all lovely little atomic files
neatly organized by layers. With that
front matter, it becomes very easy for
you to choose for your organizations.
What do we care about? what should we
include? What should we not include?
That story becomes very easy for agents
in pipelines to understand.
So,
uh by starting to make use of these BC
quality knowledge files, what do you get
day one? You get some proactive code
quality. You get a bunch of rules that
you can rely on to say, hey, you know,
there's some performance things that we
didn't catch.
Does everyone do code review and read
every single line of code that walks out
of their building?
>> We still a few. We're still We're still
a few. Uh but would you feel safer,
those of you who do not, knowing that
there's a whole long list of checks that
are going to happen automatically to
everything you produce?
Yeah. So, this is really cool stuff. I'm
super excited about it. Uh but I love
that it is tailored to your solution.
So, uh, in our organization, we have
foundation apps where we do a bunch of
utility libraries. We add all of our own
stuff that makes things good. We can
build that into our custom layer. And
agents now know how to use our utility
layers. So, that way it's smarter. The
agent's not going to build a new HTTP
client. We have a wrapper that handles
that in a secure way. Okay, that's fine.
You can give the agent those
instructions. And one of the things I
love about this is that it is something
that is in preview, but you can start to
get familiar with it right now. I mean,
not right now. I want you to hear the
rest of the talk, but I encourage people
to definitely contribute. I was super
excited. Uh I I mentioned it in one
place the first day we made it public
and a couple of the MVPs immediately
showed up with about 20 or 30 topics
that are impassionately to their heart.
I hate having to correct this in every
single code review I'm doing with my
team. So if you find yourself having
these scenarios where I feel like I'm
beating my head against the wall, my
team is not listening to me on how
important these things are. Oh, you got
yourself a good knowledge file. Point
your agent to the right skill. Create
that knowledge file as a custom layer
for yourself or even better bring it up
to the community layer. Because if it's
an a campaign that you get all the time,
why not automate it? Why not make that
part of the bigger story?
>> And another thing that I really like
about this is it kind of uh like when
you normally ask an agent without any of
these knowledge articles or any rules or
anything, it will sometimes, you know,
find the code issues, but it will
describe them in very different ways. So
whenever you do a code review and it,
you know, isn't grounded in any of this,
you feel like you're talking to a
different person every single time. And
that is like when you're doing code
review and you're just you want things
to be the same way muzzle memory and all
these things that's just very confusing.
So by adding these knowledge files you
get a more consistent experience like
every single time even though you run
the review agent for 10 times you get
approximately the same result which I
find extremely valuable.
And as one last thing I will show uh an
actual demo piece of I just wanted to
make mention since there is such a large
DevOps uh group in the room and I'm
allowed to kind of go off script on that
a little bit. I do want to mention I did
for example a workshop here at uh BC
Tech Days where my teams uh in my
workshop were working in Azure DevOps
environment and one of the things we did
as part of that workshop was we did
quality checking in pipelines. How can
we do quality checking? Well, nicely
enough, I'm an ALO ops guy. So, platinum
sponsor. Thank you. Uh uh I'm an ALO ops
guy. So, they introduced a lovely new uh
command to easily run uh agentic code AI
CLI. This invokes claude and I was able
to write a very very simple prompt that
came back with a bunch of rules that
validated BC quality rules. So, I can
see what layers uh of knowledge did they
come from. Uh this will show me exactly
what it was in this table. This
procedure this is loading the full
customer record. It should be using set
load fields. And uh I did this as a
surface as a warning for my team just to
go quick. I know a couple of people who
are using uh Azure DevOps for this uh
and they did this instead as pull
request comments.
So much like the ALGO experience, you
have to build a little bit your own to
decide what makes sense for you. It's
not as out of the box and that's the
whole purpose of ALGO. But if you're a
DevOps user, you can absolutely still
get the value out of this just as just
as everyone else does. So, I'm hoping
that lots of people start incorporating
this into their day-to-day environment
in Visual Studio Code that you start
looking at opportunities to bring this
into your poll request pipelines because
those automated validations are going to
catch a lot of stuff. And when you find
something wrong or get something gets
through the automation and you have to
do a code review correction on it for
the third time in a row, use the agent
skills to do it right. Make a new one.
So with that in mind, uh let's
bop back to
last bit here. So in this time we've
been together, we talked about three
different stories. We talked about the
BC app story. We talked about the ALGO
and eval story. And we talked about the
agent quality story. Do people start to
see how if you bring all of these
different things together, we can see
how agents maybe could put together
something a little bit better than you
thought before you started today.
That is a lovely amount of hands.
Excellent. So, yes, I'll pass back to
you.
>> No, I was just wondering, Jeremy, I
mean, we haven't really actually shown
the knowledge file. Maybe I just want to
quickly open it like just one of them to
like with the
>> Oh, show show a knowledge file. Sure,
sure. Sure. Let's
>> just to show they're actually not that
scary because one of the concepts with
these knowledge files is that they are
not supposed to be more than a 100
lines.
>> Absolutely.
>> So they're very atomic and very easy
also for you to understand. So if you
think about authoring or have your agent
author these knowledge files it's not
like you have to write these huge long
you know uh uh descriptions and whatnot.
It's enough just to be very concise.
>> Absolutely.
>> And there are like there's only two
rules. um you need to have this front
matter as we described so that the agent
is very quickly able to to see like uh
you know is this relevant for me in this
particular situation.
Um then there's the most important part
that is the description like in this
case calcute materializes flowfield
values for one record. So it describes
you know what's the premise of this
knowledge. Then there's a best practice
and then there's an anti pattern. And
this very short and simple uh uh
structure makes it very easy for the
agent to consume it and then to leverage
this
>> and importantly save your tokens.
>> Yes. And that is also why you won't find
actually there's a rule that you cannot
add code in here because agents actually
I mean they do like code but it gets
very expensive. So the the model here is
if the agent says like I don't really
get this I need code then the code is
actually put in these sidecar uh files
where there's a you can add a good code
example and a bad code example which the
agent then will revisit if needed.
>> Um so yeah that's that's a knowledge
file. Um and we hope that we're going to
get a whole lot of these.
>> Yeah. And the defining principle of
should this be a knowledge file is if
this file does not exist would an LLM uh
make this mistake that a file would have
prevented and here very important here
we're not talking about you know the
latest mythos model that costs a billion
to run no take the cheaper models like
at Microsoft build where we presented
that Microsoft's going to come with
their first models and where which have
a clear focus on being fast and cheap
and tailored to your needs. And that's
exactly what we're trying to do here.
Take a cheap model, feed it with all of
this knowledge, and just watch it, you
know, do things very good, very well,
and very quickly so that actually your
code review, you know, doesn't cost $5
every time you just want to run it, but
it actually you can get away with a
couple of cents.
>> Lovely.
>> So,
ready for questions?
>> We are ready for questions. We do have
12 minutes.
>> Great. And we have some t-shirts as
well, so you should be the first ones to
pick up. I'm gonna grab you there.
Catch.
>> Hello. Hello. Hello. I just a quick
question. I mean, it looks great. Looks
great. But how does the knowledge files
can you give a little bit more detail
how it gets loaded into context? Is it I
don't think it's is it all the files?
>> So, that's the part that we're working
on right now. Actually, just before I
came here, I was experimenting with a
little bit of indexing because really
all it needs to understand is the front
matter, right? Of course, if it says
like, so generally when you start out,
it's fine to say, hey, let's build a
code review agent. As you progress, it's
better to say, let's build a performance
review agent, a security review agent.
And if you even, you know, you might
even get even more specific. If you have
many problems with indices, then you can
say, let's build an index optimization
agent. And of course, depending on the
scope of the agent, only you know, a
subset of these knowledge file is going
to be important. And that is what was
listed in the front matter where it said
like you know this is a performance
relevant article. So it will only then
read these and load those into context.
>> Yeah.
>> Gets cheaper.
>> And now we're working on you know can we
build some index file or something where
the agent can say like what do you have
for me like where where do you start
looking? Uh and that's something that is
to come.
>> And that is where also your evals are
extremely valuable right now because we
can play how much we load how less we
load how do we modify these files how do
we index them and is it improving or is
it degrading the results.
>> Yep. And if you're doing the code review
using this, then you can do just the
diff and then the agent will take all
the changes that are in that poll
request and it will load the different
contexts that need to accomplish that
goal.
>> Hello, we are using BCOD Intel extension
of VS Code.
>> Yep.
>> Is this extension consuming the BC apps
quality repo?
>> That is an excellent question for anyone
who didn't catch it. If you're using BC
code intel, what happens to code intel
as BC quality comes online? Uh the game
plan on that is my summer project this
year uh is to take code intel uh make
sure that all of that knowledge has been
migrated into BC quality. Uh and then BC
code intel is going to be a layer on top
of that and I'm going to be doing a
bunch of evals to evaluate is there
still a benefit and I'm hopeful that
we'll be able to work with the AL
extension team to become make that part
of the VS code extension story but many
of the users of the BC code intel MCP
aren't using VS code they're using other
uh CLI tools uh so there's still
potential benefit but the goal is to
migrate the embedded knowledge in the
MCP to consume BC quality. So that way
it's not just what I've been
maintaining, it's what's we're all
maintaining.
Um, and that'll include toolings to uh
migrate their custom layer knowledge.
>> Is there any merit in having industry
specific
um
parts of this? So that I'm thinking if
industry stand industry standard
references that
>> that need to go in there.
Gotcha. Um the the industry standard
stuff is part of the you in the BC
quality story that would be become part
of your custom layer because your
knowledge of your industry is kind of
part of your company's assets. I would
think that um maybe over time we may
look at
>> if it's really standard standards and
it's something that really any agent
should understand then I would assume
yes I mean makes sense to do this. Again
it's a it's atomic knowledge. it doesn't
get loaded into the agent unless it
specifically is looking for hey how do I
deal with these standards um
>> yeah absolutely
>> I love the idea
>> so there might be a new uh uh knowledge
front matter for industry
>> there is also one thing that that we
have noticed it's a little bit
counterintuitive but as we start
building this benchmarking and these
evolves we figured out that sometimes if
we give the agent context that it
already knows
it and end up doing worse. So that is
where some of these things be like be
aware that some of the knowledge may
already be part of the training model if
it's a common standard, if it's a common
industry thing, if it's a EU regulation.
Uh so it's good to to to be careful with
what you put in and play with it and and
test it.
>> Yeah. And part of the story is is that
we need to make sure that the eval are
running regularly because models evolve
over time. After all, BC quality is
public and that's going to become part
of the training data of the next models.
So, we may need less knowledge over time
and that'll be great.
>> Yeah, thank you. Um, one part is adding
new knowledge files, but when do you
know how when you can remove one again?
>> Great question. Yes. And especially
because u I don't know fable the new
myths model might be able to you know
live without a lot of these while you
know a super cheap uh haiku model may
depend on these right so that might be
another dimension but then it gets too
complex but you are right these
knowledge files will have a much shorter
half-life than classical design patterns
have um and this is again where evolves
come in right um new model comes along
we go even I mean all the cheap
supported models we still want to make
Sure. And we're even going to make
recommendations like you know for
certain skills which model does perform
well.
>> And if you want to like what I was
mentioning briefly we also do all that
benchmarking. Uh there's a session at 11
on this event bench and it does a lot of
that story right new models come in new
information comes in. We rerun the
evaluation with all of the combinations
and we figured out ah this is doing
worse. So probably we need to go and dig
deeper and understand what we need to
remove.
>> Yeah. And there are very uh popular
agentic development speakers who talk
about for example I built myself you
know a thousand skills and then they
realized after a few months that the
models had improved enough that they
could throw out about 700 of them. Yeah.
>> So unfortunately part of the improvement
loop means you can build these buildings
for yourself, these knowledge files,
these skills, but you also have to come
back and revisit and go do they still
have value? Do they still have meaning?
My recommendation if you build custom
layer knowledge files is you might even
be able to link to your project
management system and say this was the
ticket where it had failed us so we can
emulate it later as part of the eval
story.
>> Yeah. But for now I'd rather have you
know too many knowledge articles than
too few because
>> yeah it just makes the life so much
easier and the agents perform so much
better when you have the proper
knowledge grounded. M
>> um I want to ask uh I see a lot of uh
overlap with the code cups. So how do
they uh work together? Isn't it better
to get a compile error?
>> Yes, compile errors are preferable
because it happens earlier, right? Um
but also it's a little bit annoying when
the agent starts coding something that
then later doesn't compile and says
like, "Oh that didn't compile. I
need to go back." It's again, I mean, it
burns a lot of tokens. Um, having the
code cup rules is definitely better uh
for now, but also the agent
understanding these is also important.
So I I think we're going to find a
balance there. If we run into something
that the agent constantly gets wrong,
even though there's a very clear
documented coding rule, we might add it
as a as a knowledge article, too.
>> Remember also the distinction between
there are things that you can code
deterministically to for a code cop rule
to check. So if you can do that, you
know, consistently and it's always going
to flag the proper uh errors, the proper
signal, do that because it has an extra
advantage. It means that your agent loop
when the agent is like generating code
and compiling code and testing all of
these things, it's going to catch them
at that point and it's going to fix them
and create better code at the beginning.
But there is a bunch of rules that you
can't easily codify. is going to need an
LLM to kind of understand what is there
pick up the context and then say nah
this is not good that is a very very
natural thing to go into knowledge and
visuality
>> and in the agentic era it's a lot easier
to build custom llinters as well so you
know there's a little bit of as you're
developing your internal story around
you do evals and all these things you
might look at some of the knowledge
files that you've built uh and as those
surface you go these are simplistic
enough that we can make them hierristic
and get them into a llinter instead
because a compile is much cheaper than
an agentic decision. A commit is a very
valid thing to call in most
circumstances, but in a lot of
circumstances it's not. And it's a
little trickier, not impossible, a
little trickier to build uh the llinter
story around commit messages. But agents
can look at the whole context and make
judgment calls. And so if you give them
a knowledge file of when is it good,
when is it bad, then the agents can
explain to someone in a review scenario
scenario.
>> Cool. I think we have time for one more
question.
>> Yeah, let's do one final one.
>> Uh different question. Uh you said that
>> you said that agent will be able to spin
off the container and they can be run
inside of the business center
environment. Agents are online agents at
least are Linux based. So Windows
container how
>> uh this is actually for me. Uh yes
[sighs and gasps] the we had a a bunch
of you can actually spin a windows agent
as well and I will if you want to know
more go to the session that I said after
because that's one of the things that
they are doing there busy bench the
benchmark one uh but yeah we we are
doing some work to be able to also be
running some of this stuff in the Linux
base but it's still a bit early but you
can also spin a Windows latest machine
and it has some weirdness and some
things that you have to here but it
works.
>> All right, with that I mean we hope that
you uh you know got a little bit of idea
of where we as business central team are
headed and how you can tag along and how
you can leverage everything that is will
be coming out and I hope that next year
when we're back here that we will be
able to present a much more complete
circle of agents that are out of the box
for you ready to uh to use in your
business. Thank you very much for
listening.
