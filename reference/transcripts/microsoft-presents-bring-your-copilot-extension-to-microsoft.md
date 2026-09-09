# Microsoft Presents: Bring your Copilot extension to Microsoft cloud

- **Source:** https://www.youtube.com/watch?v=uife7ZUOb_g
- **Video ID:** uife7ZUOb_g
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 47m55s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome ladies and gentlemen for our last session
of the day uh we have two sessions with multiple
speakers so the second session will be new
capabilities in reporting and analyzes views
presented by Blanca and Mirro but uh first get
our hand gets your get your hands together for
the first session bring your co-pilot extension
to Microsoft cloud presented by Yfkeni and Peter
and the feeling goes on and on and on and the
feeling goes on and on and on come away tonight
yeah so uh welcome to this uh session as we just
heard um yeah we have a lot of topics for you
today we would like to show like an inspirational
video what can you as a ICO partner build with
Copilo toolkit like for real users for the real
products we're going to cover a lot how we can
support you on your journey given your capacity
and models which will power a lot of magic you
can build these days and then we're going to talk
about models testings why Microsoft loves MCP and
why it's important and we'll hope to address
all the known questions by end of 45 minutes
yeah and as Tim Yini said the context of this is
the uh developer tools for Copilot and Business
Central um how many of you have actually tried
out using the tool so not a lot how many have
actually built something they released to a
customer in production sam you don't count
there on the front so a few as well okay so um it
is it is a toolkit that is there to help you build
uh your own interactive co-pilot features
we call them interactive classic co-pilot
features in Business Central as opposed to the
autonomous agents that you probably heard as well
about everything will probably be rolled into
a common toolkit but our focus right here is
uh mainly on these interactive um co-pilot
features but the uh toolkit really allows you
to build features very easily focusing mainly on
your value ad and not all the plumbing for uh sort
of uh calling LMS and setting up connections uh
you know focusing on UI etc but you can use the
the toolkit for that and the toolkit as I said
you know as I show here comes with UI pieces it
comes with some system module functionality with
common functions we'll talk a little bit about the
test tool that it has you can use telemetry
for insights into use um it comes with now
business central AI resources that we're going
to talk about as well as as guides and samples
and you can go to the aka PC start coding uh with
AILARN if you want to read more about the toolkit
we can we can spend hours to show you what
we built in Microsoft in our core product
but people prefer to see what the real
people doing like you are in the field
and we asked our former MVP Kristoff to share
his experience so we're going to show you what
he built his company Dyninoway for their
customers and how they use Copilo toolkit
uh for their solution so we have a
5 minutes video which is long i'm
going to play you some pieces and walk you
through what's going on let's see how it goes
so in business central they have the IC solution
and there's always a step to make it set up kind
of you always has the step to set up the solution
where the user need to go through multiple steps
some configuration and here she can do it manually
of course but in this case they decided to bring
copilot to maybe help help out with that so here
is a step where you need to set up some asset
uh statuses and I'll pause it for a second and
you can you know type it manually you can use
some you know import from Excel blah or you can
describe exactly what you need for your industry
for your case and take it from there so they
added like a small compiler button to basically
simplify that setup step and what's happening
here you say I want to create that category for
my customer use case maybe it's a consultant
on the phone maybe it's the end customer just
couple of clicks way you have your initial data
set up and then you move on to the next step
yeah and their solution has a multiple
steps so on the next steps get was guess
what ex kind of same situation you want to
set up more data and again you create very
specific prompts and you have your test
data generations uh continue from there
and again you can always discard
select reiterate uh get what you need
believe me or not this solution has at least
five or six steps where before having to do it
manually now you can kind of add a copilot action
for every step away so I'll just scroll a bit
through that to come to the most interest
interested step maybe at some point yeah
yeah somewhere here so at this point of time you
went through setup for a solution and you create
a lot of data and then you have like a little
bit more advanced step now you want to create
some templates or like a document templates again
to get your solution going and you can bring your
templates from somewhere or you can use again
copilus functionality with a little bit more
advanced prompt or very advanced prompt with a
gallery of prompts can bring to help your users
with those initial steps and in this case you
create this uh form template card but it's it's
like a document uh template for whatever the
solution need to do and you continue with it
it's kind of interesting we're all waiting some
magic to happen and feels long but I just show
you how within five minutes video you can set
up your solution with a customer on the phone
without spending before like 45 to 50 minutes
if not more so actually it's quite fast even
sometimes you see like you know you're waiting
for this magic to happen and this animation to
finishing uh so that's really the scenario very
grateful for Kristoff to show how he can build
that he always has this uh conversation with
partners it's your choice you can go for it
you can leave it empty but one of the kind of
generation of test data for your ICV solution
setups looks like a very like a straightforward
case where you can bring things like that in
your solutions yeah and as we said before all of
this is built with the uh tool kit itself right
so uh in this release as you probably heard in
the keynote uh yesterday we are moving something
we call the business central AI resources from
a private preview which was by invitation to
a public preview which makes uh it available to
all of you who want to build a copilot features
uh and we'll talk more about that and it includes
also a billing mechanism so that you don't have
to care about billing but can rely on Microsoft
actually building the customers directly for their
use in production environments and so basically
it gives you a choice between that you can use
your own Azure OpenAI uh subscription for your
features or you can rely on the BC AAI resources
um most likely you will use both because
the BCI resources is really for production
use typically hopefully you're going to try the
actual calls out while developing while testing
etc and there you need to bring your own
subscription as part of that but we'll talk
more about that so what is Business Central AI
resources it's a key feature of the developer
uh tool for coil and business central because
it really makes life a lot easier for you as a
partner when you build uh and deliver co-pilot
features for customers uh apps source publish
can then now use uh LLMs uh via the Microsoft
managed aure open eye resources it eliminates the
need for publishers to independently uh procure
and manage an Azure OpenAI subscription towards
uh their customers and and handle sort of the
billing for each of the customers as I said you
can still bring your own subscription the business
central AI resources is seen as the default uh
recommended approach uh it might not fit all of
the needs in all of scenarios that's why you can
bring your own still for production environments
and as I said most likely you will use your
own for development and and testing so just to
show how it used to work uh we in Microsoft uh
would typically build our functionalities the
features we have the copilot features we have
it will call through the toolkit as well and use
the BCI resources but you would uh up until now
have brought your own subscription for everything
including production but going forward you can
actually choose for your apps to also rely on BCAI
resources for production as I mentioned still use
your own for test and development so some of
the benefits of using the business central AI
resources uh first of all you don't need to handle
all of the infrastructure uh requirements on
uh on um uh you know um having many customers on
board and making sure that that uh that you you
uh manage deployments update deployments etc
for for customers we'll take care of that it
also means that you very quickly can onboard to uh
using uh the or to inter in integrate AI features
in your IP uh it means that we handle everything
related to scaling for example to throttling load
balancing etc as hopefully your feature will take
off and and have users actually use that it also
has the benefit for customers because they can get
a single bill basically across ISV solutions that
makes life a lot easier and then it also makes
sure that it's compliant or it helps out with
additional compliance in security and privacy
etc we will take care of of that and especially
on the content safety we will have uh blocking
policies enabled uh we will also include some
uh sort of systematic prompt for for harms hate
violence sexual and self harm filters we'll also
have jailbreak uh detection and uh cover for
cross prompt injection attacks and and and more
of these kind of um sort of safety mechanism
and and safe safeguards also from a privacy
uh perspective we just want to mention that your
prompts are your IP it's not something that is
shared or being used for for sort of training
of AI or co-pilot or anything uh like that we
sometimes get that question so let's look a little
bit about how you can use um the Azure or the BCA
resources in your own solution we actually have
some samples so on ak.ms/bct you can go to the
Ashure OpenAI sample how many are are aware of
the BC tech samples on the GitHub so actually have
quite a lot of different samples uh there for many
different uh types of solutions one of them being
building copilot features but in that sample for
uh making uh copilot features we actually show you
how you can connect to BCA resources so there's
two different scenarios there's a scenario where
you want to use uh the ones that we manage the BCI
resources you use something called uh set manage
resource authentication on the Azure OpenAI uh
and um you have to put in basically which model uh
that uh you would like to use and also you need to
provide your um partner Azure OpenAI subscription
and that might seem a little bit strange when
we're using you know our subscription for
But that is only because we want to have a proof
of of access to Azure OpenAI that's parts around
knowing sort of the having accepted the ulers of
using Azure Open etc so we only uh use what you
provide there to make sure that uh you are aware
of uh of those ulers we don't uh you know bill
you or anything like that we build a customer uh
directly and then we give you your model if you
want to run with your own subscription of course
you just uh use the set authorization uh and
uh provide your own uh account on that now
sometimes as I said you will probably use your
own for testing and development and uh the BCA
resources for production and so how do you do that
well uh we actually have the a context object that
you can use and and and use in in AL code so you
can test whether you're running in production in
SAS and if you are not you use your own and if you
are running or if it's the customer's production
it will use BCA resources right so it's the same
app same source base it's just contextual to the
environment now let's talk about uh the billing uh
of uh of AI resources so if you are using your
own subscription you'll likely run into some
challenges with managing billing across customers
so you can imagine maybe a customer having
uh three different ISV solutions installed
each of those ISVS have their own billing
mechanism because they have their own Azure OpenAI
subscriptions and that means that the customers
will have three different bills for example and
that can be confusing also if as an ISV hopefully
you have more than one customer maybe you have
many customers h but maybe you only have a single
Azure OpenAI subscription for your features
and that means that you need to distribute
out the consumption to each of the customers
in a way and you need to handle that right
and that is a bit tedious as well and hopefully
you scale even more which means that you might
need to manage a lot of traffic so you need to
manage the Azure load balancer and traffic manager
and regional instances etc and by using the BCI
resources you get rid of all of that complexity
let's look a little bit of how then billing
actually works and and you know what it costs so
uh we use a shared currency across uh all of the
Microsoft services it's something which is called
Microsoft Copilot Studio messages or MCS messages
and you will see that used across our product or
other products in the Microsoft portfolio when it
comes to billing and the billing is measured by
some shared meters uh these shared meters for BCI
resources will be the tokens used so that will be
the sum of the input and output tokens how many
are aware of what a token is around half so super
super quick basically when you ask the LLM you
ask you pass along some user instructions and some
co-pilot instructions it's you know text uh and
then a token amount is computed based on that it's
not the equivalent of a character you know it's
somewhere between characters and words there's
actually tools available that can sort of tokenize
uh that so you can get an idea of how much tokens
you're using actually in our test tools when you
run those we will also show the amount of tokens
used but that's the way you can get an insight
into the tokens and then it also depends on which
model you're using right a more powerful model is
more expensive than a less powerful uh model and
then that uh billing is consumed from a quota so
the customer can uh will have a free base quota
from their license of BC then they can either have
a prepaid quotota that typically has some discount
because they're buying upfront quota or they can
go with a pay as you go uh quota billing basically
they pay from what they're using so let's let's
see how that works it's a little bit convoluted to
be honest uh but let's let's go over it right so
billing as I said is done in messages and for AI
tools that BC AI resources follow the messages
are computed from something that is called
uh responses so you'll see I put a link in here
from the documentation it shows how responses
are mapped to messages right so if we see if we
take the middle column middle row there we see
that if you use the standard sort of skew then 10
responses is the equivalent of 50 messages or one
response is the equivalent of 1.5 message right so
far so good then we look somewhere else and then
we can see when we're talking about these AI tools
uh which is what again we're following you will
see that one response is per a thousand tokens
right and it doesn't matter which of the models
right now that you're using that's the mapping and
then you can go some third place and you can see
the pricing per message and as I said it depends
a little bit on whether it's pay for go or whether
you do the message packs because you get a little
bit discount but if we just take the pay as you go
it's about 1 cent one US cent per message so if we
do a quick calculation right uh it means that if
I'm using a GP34 model for example that means the
standard skew then uh 10,000 tokens equivalents
10 responses equivalence 15 uh messages is the
same as 15 US cents so another example is if your
feature in a call to the LLM is using 4 and a half
thousand tokens it's actually five responses or
5,000 tokens because we round up and that becomes
7 and a half messages or 7 and 12 cent so that's a
way to compute what the cost of using your feature
what is the customer going to be built you can see
this afterwards right there's going to be slides
and recordings uh also in the UI the customer
will be able to see in the co-pilot and aging
capabilities page where um they can enable the
copilot features our features from Microsoft as
well as your features uh and we are going to add a
new column which right now is called billing type
and there the customer can see who is in charge of
the billing right maybe the feature is not built
it could be part of the license the base license
it could also be built by us Microsoft that's when
you use the BCI resources if it's built by you as
a publisher it will say I think custom billing or
something like that i just also want to me mention
that this is only billing for the AI consumption
or the large language model calls if you're a
publisher and you're selling your apps you still
can charge independently on the customer's right
to use your apps just like today on AppSource yeah
yeah okay so we talked about you show example of
something you can build as Kristoff built uh
you heard about Metization that will give you
a lot of models so you can build your solutions
but the question is which models so imagine for
a second we all will meet in this room back
in February i'll probably told you that as a
Microsoft we're looking on a latest models from
deepseek and also from a latest reasoning models
we just came for openAI and back in February Sam
Alman had a vision how all the models will evolve
um kind of upcoming months if you would met
together in April I would told you that that
vision materialize and we have a new model like
GPT 4.5 and we all looking at Microsoft how can
benefit from those no capabilities with this model
but at the beginning of today what's interesting
is that some models disappears some models get
added so they're changing all the time but the
great news there's a new GPT 4.1 models which
is built specifically for developers in fact we
call them like a new API and this is something we
want to kind of make a bet or this something we're
going to use to build our features and your
features on our DCI resources going forward
one of the benefits staying with us is that
we kind of give you this staying current with
whatever happening in if you will LM world and
we just saying that over the summer we will move
all our integration to the latest and greatest uh
models from OpenAI now in our toolkit we give you
those abstractions which will look something
like that so it's very easy for you to say I
want to just be on the latest and here you go i
really abstracted a bit from you now one of the
question you can ask like why would you move to
the latest models like what's the point moving
from maybe apple to bananas and I just ask a
compiler to summarize for us as a developer
community what is the benefit of those models
latest ones specifically and you can see a lot of
improvements of things which you should care or we
should care following instructions more precisely
uh latest capabilities of function calling
MCP definition support and responsible AP
response APIs so a lot of innovations come
to those models Specifically if you define
your instruction it will better follow the
format you'll have a better way to select if
you need to prioritize on rank some definition or
prompts is do it will do a better job to classify
problems you can describe more specifically
what not to mention to kind of deal with the
situation that I will never say i don't know i'll
pretend and talk about something else there's a
lot of great stuff in those models which help
you as a developers to build uh real features
every time we talk about new models and migrate
to to the new models we always say like how hard
can it be and we always want to remind you that
new models bring new features and improvements
uh latest version doesn't mean it's better
it usually means differently and they can
perform differently compared to previous
versions and they're not back compatible
and here we usually take a step back and tell
you a story which we experienced as Microsoft
last summer it's a great story it takes a couple
of minutes so I want to share with you that so
the story was that we as a team been here before
we constantly moving from previous models to uh
newer models to benefit from all the improvements
and we had a prompt like that i realize not many
of you maybe do a little prompting right now but
you can take a look at this example and you have a
prompt kind of very structured prompt following
all the guidelines basically saying hey you
have a small assistant which will help to draft
emails to respond to confirm booking appointments
uh you know be clear about uh work you need to
do place be professional be respectful things
like that so that type of prompt could
result in an email like that dear Peter
will come to you to do the work on a given time
that work will take in that place or do this type
of job if you have some questions don't hesitate
to reach out to us we're happy to assist and then
you have like and you probably have some link so
you as a user can click this link and go to your
booking system and see the right order okay so
from instructions like that it'll probably it it
work like that and you can always have a link
to confirm and verify what has happening like
very straightforward and then overnight the
features start working slightly differently
so it starts saying like hey thank you so much
for appointment we'll come to you and ready to
help and you still have a link you can click
uh to go ahead and confirm your appointment
so one more time from pro from prompt like that
from initial experience like that suddenly to
experience like this now if I would ask you the
audience to rate if this is like five stars and
this is like how do you think that behavior
just changed and regressed from zero to five
two not good we feel something going wrong so
obviously like I mean it's pretty straightforward
it's the lack of details it's just fall down
significantly we called it accuracy but the good
but the good news was or interesting news that
actually the feature still worked you still create
kind of confirmation of the bookings you still
have a link it grounded you can verify and maybe
it'll be great SMS for sure but it's obviously not
as good as a bin and the reason of that because it
it went from a model change because models have
a versions and you can increase the version so
went from one model to another and there was some
let's call it sign significant change in accuracy
behaviors but of course Microsoft writes write
write tests time to time uh we're doing a good
job and we could detect and code the regression
we went back adjust our prompts slightly and get
feature back on time with no major drama and the
main takeaway and I really really really love to
put this picture we have Sam one of our like
a senior principal engineers in team and you
ask him Sam what is a good prompt he will tell
you good prompt is great structured and it's
concise and it looks beautiful but what matters
that you really have a good test coverage which
allow you to make this prompt still work as you
evolve your integration of compiler features so
okay I told you the story that migration can be
hard can be challenging and need to be have a
good test coverage and now I'm telling you that
we're going to move to the latest model over the
summer so there's a couple of good news on this
pass so here is an example of real of real PR we
did in a team last week and so basically one
of our engineers had a task to make sure we
can migrate some kind of small component from
a old model to previous models and if you look
on his PR and by the way you see we have some AI
summaries of a change it's saying hey we moved a
feature from version A to the latest GPT 4.4
for mini there is some changes from version
and not that much else so why obviously we
have a lot of test also passing so what we
experiencing so far that maybe this migration is
much less painful uh compared to previous ones
you still want to pay attention and run your
test if you have them uh but we don't foresee
significant maybe regression this time as you're
going for this migration from a previous model
uh to the latest model which is a good news how
how many of you use chat GPT in your phone pocket
did you did you notice like a model selection on
topic you can select different models when you ask
your questions did any pay attention to that do
you really care one of the questions happening in
the industry these days is that uh if you look at
what Azure does and actually Amazon does the same
there is the idea that maybe for some integration
you can abstract from large language models you
can say like why do you talk about us about
a model can I just write my problems it just
magically work and there is some infrastructure
coming across AWS and Azure which allow you to
do things like that it allow you to say given
your scenario we can find the best model for
you to do your work and you kind of abstracting
from that and that works great for a maybe chat
experience say some categorization but for BC
we truly truly believe it still holds that you
really to be really model aware do a good prompts
do a good job making sure your feature really
works because prompts are very specific everything
very specific and we want you to stay in this path
If you build compilot features your feature
design sometimes could look like something like
that you have some user input you run some logic
magical LLM you always validate your response to
deal with hallucinations and then you do work
if you fine with it and we could suggest you
might use more powerful models to do your real
core processing and maybe use cheaper or faster
models to validate some of those response so that
can that can be how you can use those models in
practice uh in your solutions as Christo have
built before finally I guess our main call
to action that new models are coming we roll out
them across BCI resources available in all regions
for all your customers with good capacity with
good throughput and that's how it is thank you
so let's talk about since we talked about uh test
you probably heard that a couple of times now it's
super super important uh it's really a must when
you develop copilot features we heard that in a
keynote yesterday as well whether it's for testing
the feature itself uh accuracy and for harmful
uh handling or whether it's to detect
regressions when you modify the prompt
or when the models change you really need uh
the tests uh or test coverage and that's why
uh we have a co-pilot test toolkit uh or test two
which we actually launched a couple of months ago
so how many how many have heard about the
test tool so far yeah so not a lot so it's
an AL extension that you can use in sandbox
environments um and as I said it's uh shipped
and now available on AppSource i put in a QR
link to the AppSource location you can also
actually see the source uh on the BC apps uh repo
uh on on GitHub in the AI test toolkit subfolder
um so what can you use the test tool for well
you can uh use it to efficiently test your
copilot features end to end it has the ability
to create a test suite uh where you can run um
test cases with actually datadriven input so that
you can create uh files data sets for all of your
different tests and then iterate over each of the
basically rows in the data set to call each of the
test cases in the suite so that allows you to to
run a whole suite in in one go and see the results
uh from that as I mentioned before you can also
as part of that evaluate things like uh token
consumption you can then uh evaluate the results
in different ways you can of course always do
human evaluation sometimes that's required but you
can also use evaluation functions or methods from
within your test cases or you can rely on Azure AI
foundry How many are aware of Asha AI Foundry so
Asha AI foundry is a tool from Microsoft platform
uh that you can use to develop um AI features not
just for BC obviously uh it has some features
that are relevant in connection with BC it has
a playground where you can actually play around
with prompts and try them out that's a super good
place to start don't start with building something
in BC start with understanding uh whether you can
express your intent or your feature with a good
enough instructions in the playground and then you
can also use foundry for things around evaluating
for uh harmful content safety and whether you know
the responses are in alignment with the questions
basically you can also use Azure AI foundry for
generating test cases typically you want many test
cases 500 600 700 test cases to cover different
kinds of ways of asking your copilot features
different user biases etc uh the tool itself uh as
I said I'm just going to show it here we're going
to get back to this a little bit more in a moment
but it's basically you can define as I mentioned
the suite uh with the data set you can have a data
set for all of the test cases or you can have data
sets per test case you can then include the actual
test that you want to run when it has then run
you can see the the stats for for the sweet run
um yeah let's skip this part I think and then
quickly go you know it it shows how you test
the code but I think we're going to skip that
and then go to this which covers the same so
uh we have as I mentioned guides and samples
online and uh we have now a video half an hour
so if there's anything you should take from this
uh session it's probably this one because this one
is a guided tour of building a co-pilot feature
so it will go through how you use the toolkit how
you are going to use BCI resources and connect how
you're going to write test cases etc and we have
a video if you like videos and we have a written
document if you prefer going through instructions
and it's actually based on workshops that we had
at directions um that we that we put in public now
uh we did a small poll before the session
and we're changing topics again and we ask
you question like would you be interested as
ISV to be able to bring your skills whatever
it means to our AI features in the core product
and some of the question is yes I would like to
extend your features No I dis I disable all
copilot fastes and telemetry it's my favorite
choice and then of course maybe depends how
hard it is meaning do I really need to learn
something specific or I can do with the skills
I know so we would like to talk quickly about
the story and and that's why we bring this
beautiful picture of Microsoft heart and MCP
and if you don't know what MCP means this
is like a great picture to illustrate that
uh yeah sell me a pen it has MCP and you
you kind of hook up with that but actually
actually it really solves MCP if you want to take
something like take away from here mcp solves a
real problem it really standardize in a very
standard way how LM features can uh describe
them almost on the real time so I want
to show you the demo and we'll have a
conversation later what has happened after
the demo so I'm going to switch to my PC
no yeah yes so um I'm in a business central and
I'm just opening a chat and you know chat is
a great tool it has some predefined skills or
capabilities so in a chat you can say show me
latest in quotes from Alpine well we'll figure
out that quotes mean sales quotes we'll figure
out Alpine probably mean customer we'll try to
kind of help you with that request if you will
in a couple of seconds of course so let's see how
it works yeah we found some quote from Alpine and
you can you know we can take you there and maybe
in a core product you have another features like
another capallet which can help you to maybe
suggest more sales lines and this feature has
also capabilities or skills you know you can
bring lines for example we can copy from a from
a previous invoices and you can press go and we'll
do all the magic for you but the point is that the
first experience and second experience experience
is a little bit like hardcoded or concrete it has
some skills and it can only do that and not that
much so let's say for experiment you would like
to ask chat do you know anything about all the
beers on a BC tech days recently so you're asking
a question and imagine you have a skill which
can help with that but obviously there is no
way right now to chat to know that because
like what is a what is a PC like this what
is a beer like like it's it's it's something
else so imagine you would like to be able as
I is to extend those features to bring your own
skills for example to answer question like that
so I'm going to skip to another machine uh it has
some very fancy pain on the side you you don't pay
attention to that and in this in this build I have
some configuration to some MCP server so in short
I'm saying there is something else exist which
has some skills which are defined which I might
consume and then if I go to chat and say do we do
we have BC take this beers suddenly chat can aware
that there is some another skill exist it can talk
to it work with it get some information put it in
my conversational context and hopefully uh help
me to reply with it yeah question in this case
so yes here is the beers which look uh announced
yesterday and obviously we tried them out and to
prove that it's all real which is obviously is
uh on the right side we have some like a more
engineering pain but what I want to show is
that when the chat was running it figured out
that there is a new skill and that skill can help
us with a user intent so I asked can you help me
about this information or that work I need to do
and suddenly we found some skill we can call it
we can bring information to business central and
it just works and it's all from a lab I want to
start with that but it's some of the ideas how we
could extend this experiences or similar compat
experiences in business central now how did it
all work if I go back to back to presentation
somewhere behind the scene We configure small MCP
server which basically do work which describe I
can help with the type of questions call me we
call it it provide all the feedback back in this
list it just kind of hardcoded list of beers but
it can be any kind of integration or information
from here and then somewhere in we can say hey we
have this new definition of the skill which coming
from IC solution or somewhere else and now it's
part of our m platform we know about the skills
we can call it and it just works So I guess if
someone asks you why Microsoft so excited about
MCP there's many many answers to that question
um and we're considering if you also need to use
that technology to extend our features like chat
or another compile experiences if you in ISV can
do a better job to suggest sales lines come to us
if you want to Iv want to bring your skills to the
chat come to us let's have a conversation
and how we can enable you on this path
we have five minutes left maybe we can talk
quickly about what's next and then walk some of
the typical questions yeah so I'm not talking to
that one yeah so um I guess some of the feedback
we got from uh the partners that have used the
co-pilot test tool is that you know they they
would like to see more support for flexibility in
the UI right now it's just sort of one uh dialogue
uh format um something bigger something inline so
that's something uh we are thinking of also many
scenarios involve images you know putting in an
image and having it uh analyzed could be simple uh
simple assessments about what is in the image uh
typically the models that we have are multimodal
so GP441 they will actually be able to handle
images to some degree but it could even also
sometimes be uh pure vision models which is more
about finding features and and and deep analyze
uh of images and then we have asked for the
reasoning models also the the O uh kind of models
um and then in general it can be a challenge to
uh to troubleshoot uh just in general building
co-pilot features is very much a trial and error
you have to modify problems you have to try out
again that's where the tests come in but being
able to better to have better telemetry feedback
loops and and understand customer prompts um and
then we often hear from partners that they would
really like to have better search capabilities
right so that customer is asking about a certain
thing but they're not using the words that are
what we have of in the objects or in the data
right maybe they call it a product and we have an
item or something like that and so these kind of
uh lookups or search where you find by similarity
so semantic search we call it that's a big ask
also we are actually building first semantic
searching platform for metadata but also later for
data so that you can actually come in and search
in all of the customers data for something similar
to what it is that they're asking about that's
an important thing when building copilot features
yeah frequently asked questions usually
have a question okay how do I know if I
take a bet on you as your cloud provider you
have resources models how do you know that
something has changing like version
and we're saying we'll give you some
telemetry signals for sure and find a
way to communicate if you're changing
models so you we don't break your
extensions or obviously in production
another question we getting all the time
can I get access to latest models outside
of what you guys have if I go to Azure Foundry
I have a list and on a BCI resources this list
is shorter again give us feedback maybe we can
enable more models for your scenarios over time
that's for you Peter
uh yes um so as as uh Yini mentioned before
uh you know sometimes uh there can be changes
in in or prompt changes can change the behavior
right and actually we have some additional system
prompts that we apply when you're running
through the the toolkit and again uh that
can have an impact so always you should use uh
testing right and you that could also lead to
some subtle differences between when you're
using your own subscription where it's not
and then using our subscription as part of
PCI resources where we do apply this so make
sure you test for both of those scenarios
when you test the uh the features towards
customer use let's take a few questions
I think there yeah do I dare to throw it
oh that's um I have a bit of a like I'm a bit
confused about the building the monetization oh
sorry yeah um so depending on how we build
the whole AI uh extension for for instance
um depending on the prompts we provide I guess
it will like depend on how accurate we get the
answers that's how much the client I guess
will have to pay if the prompt fails and he
has to do it over and over to get the actual well
accurate answer so um my my point is uh that we'll
have to make the extension supremely accurate to
actually you know not impact the client's wallet
yeah typically so so that is by and large true
right that that uh the amount of data involved
in the LLM call um the model used in the LLM call
and of course also whether the the feature will
give the right result in the first try or
you have to do it five times can impact the
billing right but but first of all when you saw my
calculations actually quite cheap that's one thing
uh and it is very likely that if you build a good
feature which I hopefully you will uh the cost of
that is a lot lot less even if they have to ask
you know three times than if they didn't have the
AI support in the productivity right so I would
argue that in in all realistic cases it's not a
big issue but that doesn't mean that you shouldn't
focus on getting a good accuracy still right and
so the experience we have is that it's uh I mean
you will not get a 100% accuracy we have sometimes
discussions with partners what is good enough
right it's really up to the partners knowing the
scenarios about what is a good enough scenario um
but but but that's part of the testing if you feel
that it performs well you monitor the customers
users I mean you should monitor if they're asking
a lot of times that's probably something wrong um
but I don't think it's a real life issue as such
I guess it's try to I don't know what you should
set up a buy it's hard to say what a buy is but
you know 85 or 90% or 95% coverage or or accuracy
should be a good target right it's a help you
saw in the video in the beginning of all those
different suggestions for the different asset
categorizations etc typically it's a co-pilot
right it's the the the user is in control so
they can modify parts that they don't feel is good
enough without having to call the LLM again that
would be the typical scenario see yeah we are out
yeah i think we need to stop now for next session
thank you for your time but we are afterwards
and you can ask us a Yeah yes thank you thank you
