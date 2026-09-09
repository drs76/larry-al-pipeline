# AL Development in the AI Era

- **Source:** https://www.youtube.com/watch?v=VS7Ad4l0Ly4
- **Video ID:** VS7Ad4l0Ly4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 97m23s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music] ladies and gentlemen welcome back
welcome here to cafe poly's room 8 and
u as you can see this looks very much as
the last presentation of the day isn't it
so please welcome your bartenders it's
dimitri katson and arantan kman [Music]
so welcome everybody to our bar in cafe polish
that's a nice one um yeah well what can we say we
have a bar why is that uh you will see it's for
us okay it's for us that's for sure now we were
afraid that we have an overrun so we made sure
that we have our beer yeah you got it all right
so dimmitri okay let's start i'm gonna introduce
you okay yeah so that's dimmitri all the way from
thailand a long-term business central developer
and actually creator of central q everyone is
using that right can i see some lights come on
oh there should be more yeah yeah yeah that's
it look at that that is your audience man so um
he also built uh a co-pilot thing in business
central for number and he's a contribution hero
for in 2024 last year so let's see if we can
make that again this year well that's ditri
yeah and that's aj aj kuffman so it's he is
the father of rest client model in bc is 23 plus
years of experience in uh bc so well what can i
say here more so also cto of lumus and of course
mvp for long long many many years and the reason
why i took this picture i can tell you that now
is because you know we're going to talk a little
bit about ai and co-pilot and stuff but i like to
be the captain so that's why i have this picture
actually i do have a boating license h so i can
call myself a captain and there's my co-pilot
all right let's move on sometimes i want i i
like to be a captain as well but okay for this
for this session let's let's be so this idea
of the session started half year ago when we
actually had a whatsapp conversation with aj about
hey the modern way of doing developments using all
ai assistants copilots agents and so on if it's
like a good or bad uh can we trust the results
immediately without looking at that should we
like learn al anymore should we um should are we
responsible for the results or who is responsible
for the results so uh we we thought that well
it's a very good conversation it got a very good
conversation and this he he actually used some
words in the sentence i had to read five times and
still had no idea what he was talking about that
was the the truth actually yeah exactly so the
that's when the idea of the bc tech session was
born to teach you all these terms um today uh so
and um we we we decided well let's do this so but
uh to make it uh more fun uh we decided to do like
a challenge or whatever so aj so we we we will we
decided to create an app so and aj will created
an app uh in his oldfashioned way using all his
experience uh i will do this using just uh agent
in cursor without touching any al code at all so
uh we we we have the same or the same background
but for this session i will pretend to be a junior
developer uh because i think that it's important
uh for the junior developers to understand where
should they use ai where should they trust ai
in which areas and so on uh junior developers
already have some experience but they can't
100% rely on themselves so what i see they
more and more rely on ai if it's good or bad
let's see and at the end uh of the session uh
you will have a poll and you can then vote
for the approach that uh you like the most
the story of the app that we're going to build is
the brewery management app so so we are a brewery
company we are brewery company and uh we will uh
we will try to automate integrate the app for the
next uh business process so we sell the beer in
kegs the keg uh with the beer we sell it to the
pups the pups pay us for the beer and deposit
for the keg then they need to return back the
empty keg and we need to track this if they
returned or not if they returned they get the
uh refund we also want to know like who owes us
how many cashs uh how many deposits are there
should that we need to return uh how many pops and
and also we want to expose this information to the
pups so the pups will uh also can access to this
information through the apis okay um so we decided
to start with one document so this document which
is called product requirements document is just a
description of what we want in a very business
uh non- tech language and then to make it clear
experiment we actually divided and aj didn't see
what i did i didn't see what aj did so i actually
saw for the first time yesterday last tuesday we
saw each other's uh result for the first time last
week but anyway so just a few days ago we we just
saw from each other what we had created yeah and
we were like very surprised to say the least yeah
so we will start with a vibe coding i think that
everybody heard this term the vibe coding is when
actually you don't write code by yourself you ask
ai to write code for you and it writes the code so
i will just i will just go here and uh so this is
my workspace where i uh started this is the maybe
you need to zoom in a bit i think so okay so uh
this is uh i decided to start with a uh elgo uh
workspace um and we have here the uh folder for
the uh brewery management our app so this is our
uh app do all the work so i can just sit at the
bar yeah yeah yeah next three hours i i'll join
you so and then we have a a folder for the tests
okay that's our tests um and then we have this u
pr uh product requirement document actually this
is the same document just in a markdown format
we have like a key features here uh that we need
to implement the master data import from the uh
some third party uh service we need to track c
uh we need to track given and return uh we want
to uh to make it available to the pups and some
success criteria so that's it so this is like a a
very short description so what i'm going to do now
so this is i'm i'm working now in cursor and
this is the uh agent uh top so um what i can
do i can ask like implement and i will point
to my app json so this is the uh my app json
that i'm going to create and uh in the i will say
that in in the source folder uh because currently
uh the agent in corser doesn't really uh
work good in the multi-folder environment
in the workspaces so that's i specify that i
want to create code explicitly here and use
uh prd so this is our document
yeah
let's see
all right so you done yeah i'm done all right
that's good so how long is going to going to
take couple of hours uh well let's see maybe uh
some five minutes i have some beer yeah we can
just watch do you want this yeah yeah that's
good let's let's take that one whatever yeah
i will serve you yeah oh he's serving me he can
do that because he doesn't have to work he can
just watch so he can also serve some beer
yeah sure it's good look guys this is vip
coding okay this is how vibe coding looks like
yeah i mean cheers cheers cheers any questions
so what's going on there um are we done no
we are not done let's see man look at that
it's doing something it's doing yeah like you
say it's doing something it's doing something
so it's um had some plan uh so we checked that
i don't didn't have any code yeah perfect the
source folder is empty so i'm going to implement
this and man come on i thought that we will just
sit and watch how it's doing i mean aren't
we seeing it yeah we see but i'm not really
satisfied with that man what's wrong well look
it's uh create so it creates me the table brewery
it creates me the table beer yeah maybe i will
not so specific in the requirements but really
i want this to be like a a customer in the item
yeah that's how i understood the requirements
document so i think it should work also so
are you saying that that the agent is not
that smart just asking it is maybe i i'm not so
smart maybe if you're smarter than me should it
should be implemented like this but i i i don't
want to do that please really and also man look
how it's structured the code we have this this is
an old fashioned way i mean this is your way oh
do do you have waldo's app in there
uh well no but we we have this it's
splitted by by folders i i mean that's doing
something that's a blast from the past yeah
yeah that's a past and also well man look
let's use the api that actually is wrong
i mean this this this url doesn't exist
whoa h damn it so okay it still generated
something as long as you have your beer
yeah yeah okay you got that so let's let
let's let's i think stop this i i can't watch
this man okay let's return it back and i will
i will so what i have here i have here
the once again i will return back to my
where is my master
okay no never isn't uh so
i'll return back to my slides
look what you saw well it it works i mean if i
will continue that uh that will definitely work
uh but it will be implemented very wrong
completely not that i expected from that
but we have some we we have some options how to
influence on that so let's continue and see how
to do the wipe code in the right way well this
is the right way by the way yeah but we can do
better uh so first what we need to do we need to
prepare the context well context is the key we had
uh only the product requirement uh document which
was not technical so ai actually didn't implement
it correctly as we expected so then uh we need
to move step by step okay so we need to uh create
first the setup tables the setup pages so the main
core of our app then we are going to import master
data uh then we are going to implement business
logic uh then we will implement custom apis and
then we will implement testing so that's actually
how i uh prefer to work here so let's look into
uh into this one how to uh prepare the context
so why context is important so once again if
you ask something like create setup structure
without providing any additional information ai
has no idea what to do the output could
be generic very often wrong but if you
uh if you would be very specific like hey you
need to do to create me a setup table pages
with this numbers with the number series and you
need to create like installation code units and
you need to follow the development plan and you
need to use the uh like development instructions
for the bestl practices so it will do its job
much better okay so let's see how to do this
so so
so what i'm doing here well as we're not
going to wipe code everything on stage okay
uh because this will just take a lot of time to be
well i i'll be honest with you i really followed
our rules so i didn't touch any ale code but it
took me like two days to to make it work okay so
uh so hello yeah okay and uh so what i have
here i have a branch with a code that was
uh generated and also i have here a chart
so this is the chart that's actually i
uh used to uh do the work so um the first thing
that i want to do i want to generate development
plan so development plan is important
document that really help uh your agent
to focus on the tasks so i asked it hey can
you from the uh product requirement document
generate a development plan and it actually
let me show you so it's actually generated me
uh the plan with actually the all the
steps that are required to implement this
uh this app and also it provided me the uh project
structure but you see here it's splitted still
by the folders like tables uh pages and
so on which is the oldfashioned way once
again ai here i am using the cloudy uh foret
even if it's u uh the model that is very new
uh it was trained like a half a year before a year
before uh so it has a knowledge cut down and uh
that's why we really need to additionally teach it
some things so what i am uh can do uh here as well
so i'm going to add a development instructions
and i think i will let me check uh
so okay so what i did i asked then uh to use
this development instructions so what are these
instructions in corser they are called rules
so they are explicitly put it in the corsor
uh folder and then under the rules um but i
actually generated this instructions from the
um al patterns website so um it has all
the uh instructions how to write good
al code like best practices uh the
file namings uh the fold structure
uh and so on and then i ask it to uh regenerate
for me development plan so if i will look into
the new version of this development plan
uh now it's has the folder structure that i
uh recommended it to use and then it splited
the work into these development phases
uh foundation and setup first week okay so
that's our first week of work then master data
week number two so actually this it's supposed
to implement this app in six different in six
weeks so if you want to provide some estimation
for the customer this is your way to go okay
so yeah this was uh the the context part
so we we created the context so some tips
how to prepare good context you should have
the business requirements you should have
uh implementation steps you should
have like a coding standards and
uh that's also good advice you can uh say to
the agent that hey if you will write bad code
i know where you live i'll come for you okay
is that a threat to uh to ai or to yeah it is
a threat to ai yes i like it yeah it's how how
you usually do with but the question then is who
do we know in the business ccentric community
who is a violin psychopath uh any names that
come to mind let's not say it let's continue
okay yeah let's continue yeah so your prompt
should be uh short and specific and then this
is your way to go and also when you have this
information when you use encursor agent the rules
that you put there they automatically is added as
your context and send to the ai model so it's uh
always used uh but also you are free to mention
some files to mention folders maybe you have some
uh existing app and you can say that hey please
use please use this code you need to implement
something else so do this and also good trick
uh to implement something which is called lo
uh mgd file so after a implemented something
you ask ai to uh put what you implemented
what you learned what where you failed in
this file and next time it will uh run it will
generate some code it will use this knowledge
so let's continue and we will move to
the uh setup how how i generated the
uh setup part so i ask it to generate setup with a
number series some configuration and installation
uh code unit to be honest this first uh this was
from the first shot i actually didn't um didn't
correct it uh so this was quite okay so um let
me switch to the branch and show you how it looks
and i will change the chat
nope
so um let me close this yeah by the way aj is
also responsible today for the bad jokes so
when i'm doing something you can what what i
didn't know that what you're responsible for
the bad jokes yeah well i'm i'm like what a
lot of typing you need to do here i mean bad
jokes no not not at all at this point i know
there will be later okay funny thing is that
you did hear something that i when i saw the
first time i was like okay is that really all
necessary do i really need to learn how to work
i mean i was already on my way developing some
stuff yep no not i was not man yeah i'm just
reloading the screen to uh to load all the
chat because from this moment the chat becomes
really long so um yeah so what i asked here i
asked it to implement phase number one from our
development plan so it then went and implemented
for me uh setup it was quite good so it was
implemented the setup table uh it also used this
procedure that i actually use by myself
as well uh it created me the page um so it
was quite okay uh the permission set even the uh
extension of the role center um so we can go here
uh let's resign in once again
so we have now the brewery management in our
ro center and this is the setup so it's created
uh actually everything it created the number
series it created the installation code unit to
uh initialize number series for that uh so that's
uh how it looked it was quite okay i would say
next we need to import some uh data so we
uh i decided to import some uh master data
from the web service that is that is called
uh uh brewery guru or something uh that's a
web service with beers and breweries that
actually not exist so that was also fun
uh the idea here that we want to test
uh agent if it's okay or if it's good
uh to import from some external web service
uh into uh al tables so we wanted to
uh create api integration layer uh beers should go
to items breweries to customers and it should use
uh templates so it first told me that i did
everything correctly uh but then i told hey
no you actually uh didn't use the template
feature okay he replied okay now i'm using
the template feature then hey you did use wrong
uh api endpoints you actually made up everything
then he he he told me that okay i failed here but
let's do it right uh then he then i told you hey
you imported items uh from beers but you didn't
imported the images he told okay i'll do that as
well so then i told hey you didn't validate
any fields you need to do this so actually
that was like a back and forth conversation the
last thing that i asked it that when he finally
uh created the code that hey you are using
old-fashioned http uh client to import data
you should use rest client for that he just asked
i don't know what's that client i've heard about
that one yep so actually i will show you in a demo
how to teach it the rest client so uh let's go
there but the point the point here is that um uh
well from this point from this moment you should
really test and see and look into what ai was
doing so let me switch here so now we are moving
from four to actually eight iteration because
i will skip some that are not so important but
did you have time to drink some beer in between or
was the idea with i mean that's how i work i mean
uh i do have time i fetch a new beer
yeah yeah sure serve yourself i mean
you have time i'll wait my turn okay so
um where is that um yeah so what it did
uh let me go and uh show you this integration
we have here the the integration part
yeah let's first go and see where we uh
getting data from so this is the website
which is called brewbody uh dev and it has the
apis that's actually we want to import from
uh we wanted to import only beers and uh breweries
but uh i asked to implement uh this
um this apis and it created me a lot more so
it created me import beers import breweries
and then also get languages so actually it
implemented me all endpoints that i that's
presented uh there uh but how did he know
what uh how to implement this so what i did
uh i just exported from the postman
the collection in a json format and
just told him that hey uh can you just use
this collection implement me from that it
was like a one shot i mean it took time
but he did it but he used this well http
client okay who are using http clients when
we have rest client rest client exactly it's
a lot of code man yeah it's a lot of code
so what i asked him that's my another chat
hey can you let me load this because this
is interesting hey can you replace the http
client with a rest client actually what it
tried to do so it it didn't know what's the
rest client is so it search for the internet
so it search for the internet how to how to
implement this then it tried to implement this
but then it failed and it removed everything
so i removed that is that so i need to know is
that because of ai or because of the rest client
this is because uh there is no good documentation
about the rest client in the web okay somebody
need to write that exactly so well but i didn't
stop there uh i just i know that uh there is um
there was your webinar about the rest client this
will go for documentation so what i did i just
uh found the the first available uh service
to transcribe uh from the youtube i puted the
link of your to your webinar and it trans made a
transcription and like i copied this transcription
so this is the transcription for from your webinar
but the problem here is the transcription doesn't
doesn't uh have any information about the
code that you are showing on the screen
transcription is just your voice yeah but your
story that you describe there how to implement
rest client is very important so this is one very
important context and i i really uh think this is
uh a smart way to do honestly i didn't see this
one coming so documentation is missing period no
goes out the on the internet to find documentation
or created documentation and that is then fed into
ai i mean that is smart yep but that is human
intelligence to take exactly so i i am ruling
this okay i know that there is your webinar
and i i know where to find this information
but that's only one piece of the puzzle the other
piece of the puzzle is the code itself so but the
code okay we have the code uh in the rest client
i mean this is the system app this is the system
app but how to know take this and uh should
i just take everything and to the ai that's
not very smart so what i did um i asked it to
create a documentation from the rest client
from the code that's uh in the microsoft
system app and it created for me two files
the architecture [Music] the workflow
the relationship between models look at that i'm
that is correct that is awesome really that is
awesome and this is also the public models all the
description of that so this was really correct so
what i did so i took this document this document
and then uh together with this uh transcript i
uh asked it hey now use all this information to
reimplement to the uh to to the rest uh client and
uh let's return back uh where is my i'll find the
branch i think it's nine so yeah replace and now
let's see so now it's correctly used your rest
client so it's used the initialize rest client
from the transcript because you describe that
you need to do this and also uh implement this
using the code that is available so now it's
uh really works so now it's like one line of
code but what also i well of course the using rest
client is a general thing that we need to do okay
so i what i also ask it uh not sure if i can find
this but uh the idea is that hey now remember
remember that you need to use risk client and how
to use risk client so you can reuse it in a uh in
in other projects and it created for me the rule
so from this one from the chart it created me a
rule like always use rest client with a do within
uh with a examples and to do and remember these
rules are always used by the cursor when you ask
something to generate so this is like a continuous
flow so this is kind of a local training of yeah i
would know yeah i wouldn't call it like a training
but this is like the way how to make things not
fail once again yes so what kurser comes out of
the box is like somebody who let's say stopped
learning a few weeks or months ago is not going
to learn anything new or you have to switch to
a newer version of the model but anything in
between is saved by you and fed into the system
so he can reuse that every time yes exactly so
you can share these rules maybe you can include in
include them in the into the how you create your
uh the projects and so on so then let's go back
here let's see how it really implemented this i
have here the it created the api configuration
with the endpoint and uh actually i can test
it and it works and then i uh actually can import
from the brew body uh it works uh because it just
takes time i already imported this so let's see
so it's our items in the pc and that's our beers
i have the same list huh i have the same list
and tell you that well we imported from the same
api okay so and if we can go somewhere in any
any item i don't know why it's so slow now um
we have this brewery information as a tab with a
fields and these fields come come from the api so
uh uh well once again i didn't code anything here
i just ask it i provided i what i did i provided
context so this is you need to look at this need
you use it so i was like a manager here okay so
uh return back the business logic finally finally
so we created our we imported items we need to
create the business logic the business logic
is we should um track cake moving uh when we
post sales order we need to track if the cake was
given if we track if we post sales u uh return we
need to track that the kek was returned and also
during the return we need to create the refund
payment journal so it be there and that's where
it really went wrong no surprise so first it told
me that i did everything good now i uh actually
there were no compile errors the thing is there
were no compile errors then it works then if it
compiles it works right yeah of course that's a
rule that's a rule sure i mean but then i start
checking and told him hey you used the wrong
event this event actually make no sense there
um so actually he used the on um on after post
sales document the very last event and then it
pointed then to the sales header and sales lines
that actually were not existing anymore uh to get
some data from them yeah they're finalized and
they gone then yeah yeah it's already gone so then
i told nano you need to do this a different way
uh then it reimplemented something but forgot
to uh implement the main logic that i asked it
from the beginning uh then it's uh didn't then
forgot some of the business requirements so it
implemented one part and didn't implement another
part and then there was a big big big conversation
actually finally i think after 15 different rounds
i made it work because i knew from because from
that moment i switched back from the junior
developer to myself okay because i i couldn't
wait but so i pointed him to really really focus
where to move but look that's i have an experience
so you can actually find yourself in this
situation like you ask gor hey can you please
fix this and you do this for the 20 30 times but i
can tell you that guy needs some beer for sure for
sure yeah well you need to really understand
how things works especially with a business
uh implementing business processes with ai
very bad so also how to escape this uh please
fix loop there are some tips well the base app
actually is your very good helper so if you have
uh the code from the base app in parallel uh you
can go search for some code copy paste it back to
the agent and say hey please use this uh person
or use this code um that's well that's the option
uh but one smart thing that you also can do after
this long long long big conversation and if you
finally made it you can uh tell it hey based on
what you learned create me a good uh re uh reimp
recreate for me development plan or maybe remember
this for the future as a separate file how to do
this and also include this in your current project
and your uh future project so it's actually like
a junior developer where you are uh reviewing the
code telling him what he did wrong and hopefully
the junior developer remembers that for the
next time but you make sure by storing all that
information exactly yes so that's uh how it works
also uh don't uh create long charts so if you have
like a long chart it will start be very confusing
start every start new chart when you implement new
feature okay that's rule number one i would say
and also what you can do well obviously use git
okay so every time you uh implement with ai create
commit so then when you f uh after 10 commits
found out that hey this was really wrong i finally
made it but well the code is bad so you ask it
to summarize where you failed uh you ask it to re
uh recreate the development plan you roll back to
the previous commit and ask it to re reimplement
using new knowledge okay so that's uh really works
so yeah so uh i will i would i think
switch to this business logic but to
uh show you a little bit so we uh we were at
number nine now we moving to number 14 because
that in in between they all my my iterations okay
um and uh let me go and show you the the final
where is was like tracking i think
uh the handler so yeah so this was
so that's how it's actually implemented
so finally it was pointing to more or less
good event that i thought uh then it's uh decided
uh the movement type if it's uh given or returned
based on the uh sales header document type then
it um actually created the kek ledger entry
yeah so that's the code it's created the
calculatorure entry um and then it's also
uh created the um payment
journal line for the refund
so that's was also interesting part uh
because i appeared that he don't really
know accountant how it works so i really
needed to point him how this deposits
and refunds should work from the accounting
point of view it and that's why you came up
with a payment journal line yes so that's
my idea was that when the customer return
uh the ke we need to return him the deposit
and this is the payment journal line okay yeah
so because ai actually first created
this payment journal line and posted
it automatically so i actually didn't want to
post it automatically okay this is our payment
interesting yes so this were the main takeaways
that well that's didn't work very well but also
uh fixing the prompts is not only good enough
you really need to uh you were asking for the
model okay so let's now talk about the models
whoa dimmitri what are you doing now you can't
you can't see that oh no no you you told
me you would not do that uh i man okay i
get you covered oh man you cover and them
as well you you covered the models as well
yeah yeah oh yeah so uh that were the models
before the ai now we have the models gpt cloud
uh gro and so on so and we have a choice in cursor
which model to use in every call actually so yeah
switch models switch models is there something
like a divorce or how do you how do you should i
think about that uh let's be more uh clear so this
model doesn't work let me take another model yeah
yeah let's be more clear switch ai models oh ai
models okay okay okay i was already curious yeah
yeah so different models have different brains
no no i'm not going to make more jokes now
some bra some models are more logical some are
good at coding some are just better yeah so
um there are four different models uh that are
available in corser from the cloud provider uh
it could be 3.5 set four and some others uh gini
gemini uh 2.5 uh gpt 4 for0 uh 4.1 and so on 03
so well there are a lot of models out there um
so which model to use when so there is actually
a good slide from the cours documentation as well
uh but the idea is that uh there are like thinking
models and there are like classical models the
thinking models are more advanced more expensive
more long to execute but what they do they
plan their actions in advance first and then uh
action um so you can use this in more uh advanced
scenarios when you implement complex features or
if you want to create development plans and so on
uh there are more creative mo models like gemini
it's good for generating documentation uh it's
good for some generic uh code but if you work in
more some specific like specific code units uh
you want to implement some functions and so on
uh you can use um cloud uh sonet works pretty good
with al is is there a is there a difference in
cost between those models uh so it is but when
you're using the cursor you actually pay like
$20 per months for the subscription and they
are all available for you okay including the
more expensive models like 03 o3 actually is
more expensive and uh you pay extra if you're
using that there uh so really need to be careful
when you choose uh so what more what ai models
ai models uh is better for al actually the answer
is very different depending on when you ask this
because every company every provider release
their new model and at this release they say
that now we have the best model and then the next
week other provider release the other model and
they say hey now there's our best model so i don't
have answer here but the model that i use most is
uh cloud cloudet works pretty good uh sometimes i
use gemini and less i use uh models from the open
ai especially in al they are not so good in al
that's just my experience with that so let's move
to the custom apis that's almost the last part
that i implemented uh so i asked it to implement
uh uh to expose my data to the popups yeah and it
created me the custom apis what interesting here
is that i was actually wanted to challenge him uh
at him her i don't know it yeah yeah so um please
extend also standard item ledger entry api so what
what did it do and actually it went pretty good so
it created me a clone of uh the standard page
uh which was actually very correct however it
uh named this clone page item ledger
entry entries extension well okay so
um um just to show you u where is my api so this
was branch number 15 api i love apis sure you do
yeah this was the idea also to show that
yeah but that was pretty simple also one
shot um created me the api with a publisher
with the group version uh from my point it
was all good for me you have other yeah i
have a can can you scroll down a bit please
okay so this is okay now up up to the top so i see
only some code here to calculate this is based on
the source table customer right it is and you are
going to give pips who are customers yep access to
this api yeah okay now i'm so all customers can
see the balance from all other customers [Music]
damn it that is what is created here right yes
exactly whoa um i'm not so sure okay i'm not so
sure about that but that's a good point valid
point there's no security here no at all and
even i mean if you give somebody access to this
api would they have access to the other apis as
well the standard apis with financial data
and stuff like that they actually become a
full user in business central with access to all
data well of course there are like permissions
that you can assign manually it didn't assign
the permissions to the user but well who knows
what permissions would be assigned okay it's
something to think about it is i think you
are right and testing so we implemented
our app using the wipe coding let's test
uh let's also implement some testing uh so
i asked it to implement uh tests uh for the
brewery app uh covering the uh sales return like
everything actually it generated tests for me
uh quite quite okay so um let me i think
show you first so um so what it did
so this is the tests actually that it's
generated and just let's zoom in run this
look that's the picture that i
got from the shot from the first
uh shot there is some work to do it is but it's
very important to understand what's happening here
so your tests can't be better than your code
okay then if you want to fix your tests with
ai don't do this okay why because tests show
you where ai generated code failed from from
this point of time you really need to dig
in and un look into what ai generated this
is your good point where you can reimplement
something and find really bad patterns and so
on so take responsibility ai writes the code
but you ship this so please well you can use
then api maybe to help you to rewrite
something but well this is a good point
of time to understand what ai really did where
it went wrong and how to improve this okay um
and yeah i had one more uh one more before we
continue so um when i this was the only step
that i did manually okay so uh i fixed the
code implementation manually when i saw this
uh failing uh tests and then when
i did everything fixed manually
now my tests run very good but now i have a
confidence in what ai generated your turn yeah so
in the last uh hour or so dimmitri took us on the
path his journey to create this app which actually
took him two days two days two days um well i'm
going to share parts of my journey creating it
in the old-fashioned way um i'm not going to do
every step of the way because you all know how
that works right but there are some interesting
differences with the approach that dimmitri took
and the approach that i took so the first thing
i actually did was trying to understand the
requirements i will come to that in another slide
but that's the first step the second step i took
is have some kind of a functional design how is it
actually going to work in business central then i
did the business logic how is the process going
to work followed by importing some master data
and demo data finally the custom apis for the pups
and yeah some testing at the end is always at the
end right um of course i should write a test along
the way we all know but i know many people don't
do that i'm not going to ask to write to uh lit
your um your little thing but if i would ask i'll
probably see a lot anyway this is the difference
so what you see here is in the first two steps i
was not even uh working on the app itself i was
trying to understand how am i going to create it
then what is also interesting is that uh dimmitri
started with importing master data and i started
with the business logic followed by the master
data because in my mind the master data with
all it fields that it needs uh setup etc is
a consequence of how the business logic works
it's not the other way around like the master data
is going to dictate how the uh the business logic
is working the business logic dictates what
data i need in the setup and in the master
data so that is actually swapped and finally
okay we found each other in the custom apis
um and of course testing so the number one what
i did is trying to understand it in the right way
so the first question i had to demitri what the
heck is a beer cake okay no i i was surprised you
didn't you don't know no i don't know i'm not a
no i i think i didn't understand it right but this
this this container right i i got it correct right
this is not not a bottle but like a beer container
of beer yeah yeah all right okay so but then i
asked myself a beer cake what is it is that an
item for business central or do you keep stock of
it or is it just some disposable apparently it is
not a disposable because you are going to reuse
it that's why you ask for a deposit and when it
is shipped is it then your inventory is it your
property or is it from your customer and how is
that handled in uh accounting terms i mean is that
still on your inventory account or should it be
on another account is it completely gone and you
wait for it to come back um and how are deposit
actually handled in accounting that's a question
i had myself because uh this is money that i
owe to my customer but do not have to pay at this
moment until they return something but i still
need to know on my balance the the money that i
owe them so i have that money reserved there's
absolutely not about profit or loss that is just
uh an asset a liability actually um and then my
the next question is could we use business central
to automatically apply deposits on sales and could
we automatically do that with refunds and all of
these things i have been thinking about while i
was walking the dog that's why the picture is
there that's my dog and i had done quite some
walking and and trying to contemplate all of these
questions so you was using your thinking model it
was my thinking model absolutely yes you could say
it like that figuring out stuff then the second
part is okay so i have uh got some some questions
now i have to find the answers and now i can um
yeah design in my head how all of this is going to
work my goal is to use business central standard
features as much as possible so not trying to
create for example if the gs are um an item i i
do have an item ledger entry and i have in and out
there of positive and negative adjustments so why
would i create another uh ledger entry ledger for
for specifically this type of item why so i said i
can use uh the item ledger entry for that and then
how are deposits actually working in accounting so
i was looking at the internet actually finding
a well but i'm going to show you it is in it's
in dutch but there's a excellent explanation how
deposits are posted to gl accounts which accounts
should be debited and credited how they work with
your inventory accounts so they move from the real
inventory to inventory that is actually issued to
your customers and when it returns it comes back
onto your normal inventory account so you can see
what is the current value and the current quantity
that you have on stock and what is the current
quantity and the value the cost not the deposit
amount but the cost of the item that is under your
customers so c will be items just flagged as a
deposit item that's what i'm going to do and what
i then decided is i have something that's called a
unit of measure i'm going to link the deposit item
to a unit of measure measure so automatically on
a sales line i can see hey this is a sales line
that does have a deposit item linked to it i was
actually not using u any word geck or uh or beer
or whatever here it's going to be more generic
and then i decided to link this on the release
of sales order and invoice of course i could do
this automatically as soon as you create a sales
line i'm going to create a deposit line as well
but then you run into trouble with uh which line
number are you going to create so what i did is
let's do that on release um on the sales order
and when it reopen it the lines are removed so
you can see what happens there as soon as you
release your sales order or invoice finally um
not only finally on return orders hey there is not
something sold as a uh as beer with a gag as unit
of measure you just get back a unit of measure oh
sorry yeah an an item actually a g item so returns
are treated a little bit different than sales
orders it's going to be a refund automatically
when you have a return order with that item on
the line very important a deposit line should have
zero vit no vit is charged on deposit just that
you know i mean something that i figured and oh
wait a second when i buy it when i purchase from
a vendor the x i have vit to pay on it so i cannot
just say create an item with uh a zero vit no
vit should not be applied on the on the deposits
another thing and then i said well wait you know
what i have posting groups in business central
posting group take care of everything it's the
linking pin between what you are posting and
to which accounts it all goes so that is what i
uh used event and that inventory value i already
said that should reflect the cs that are inhouse
and those that are at the pips and then with all
these things in mind i could finally start
the logic knowing that dimmitri was already
struggling and doing some iterations and stuff i
was thirst thinking the first thing that i had to
do well he let the model think but then he needed
to tell the model that he need to think different
right so what i did is i created a few uh table
extensions a few page extensions obviously and
for this whole feature only four event subscribers
that's it only four the code is actually pretty
simple and straightforward so i have a um on uh on
the items go here on the item table i just um well
mark it as a deposit item um tell him what is the
vat product posting group that's the 01 in fact
etc and then have some flow fields that uh give
you the um number of outstanding items and the
corresponding amount and then um i have some
uh some code on the on the sales so on my sales
line i say well um on validating the item number i
need to set the vit product posting group that is
something that might happen because that might be
an deposit so i check hey is this a deposit line
if that is the case then take the one from the
item that is my zero uh vit in fact and what then
i needed to do is on release uh i need to create
the lines on the reopen delet so i created two
events subscribers for the on before release and
after reopen and this one is going to the sales
header saying create deposit lines and on the
sales header i go into an implementation code unit
and on the implementation code unit i have the
pattern with an on before with handled an on after
etc well they will be proud of me i guess so um
come on i hear him so this is actually uh the p
the the code that i wrote myself to um get all
of this so what happens when i go into a sales
order let me quickly show you how that works if i
create a sales order here come on get a customer
and uh come on i want to have a beer some uh
bubble gum beer whatever quantity i'm going to
have um uh 10 uh kegs and well it's usually sold
by the liter but i choose to have kegs in here
and when i say release i get another item line
here for the g itself with the price which is
actually the deposit that is in total is this what
the customer owes me well this is the vat only
on the first line so that is actually after a lot
of thinking not so many code to create i had some
drawbacks some challenges when i was doing this
one of them was how do i refresh a total on the
sales order after creating the deposit lines i'm
talking about this part here this is actually on
your sub form how do i update it because it didn't
update automatically after i created the extra
lines on release only when i closed the sales
order and then reopened it but hey the user wants
to see it immediately when he releases so what i
did is dive into the code how actually does that
work and i found out that i could do this with
just one line of code force totals calculation
um i had some iterations here to find it i
had some more code but after all this was
the single line of code that worked and i like
single lines of coding then i wanted to have a
flow field on the customer and the item table to
sum the total outstanding deposit amount so i was
going to create a flow field that sums up the
sales amount on the item ledger entry ah that's
not going to work because the sales amount on the
item ledger entry is a flow field itself to the
value entries so that was not going to work so how
could i solve that um i couldn't use that field um
could not calculate it in code because that is a
performance issue i'm not going to run uh iterate
through all the item ledger entries and then say
calc uh sales item whatever not going to do that
so the only thing that i came up with is the
deposit amount itself should be on the item
ledger entry that's it it's not a value entry
anyway so let's leave it there so i created
an extra table extension i'm not going to show
you it's boring um table extension for the item
journal line plus an event subscriber to move it
from the sales line to the item journal line to
um the the item ledger entry by the way this is
a very very complex task for the ai agent when
to make it right if you create a new uh field
in the into the item ledger entries it has no
idea about the process how to put it there so it
should because you need to do it through the item
journal lines and it has no idea about the process
yeah so it takes a developer and of course uh this
this you see the picture that's what happened to
me of course by walking the dog i was somehow all
sleeping at night something came up my mind oh
i need to think about this oh i need to do that
and then i couldn't sleep or i just said to the
dog uh we come home now so the master data import
you really love your dog right i do i do yeah but
uh i need to uh uh um yeah work on walking now he
got lazy um so um i i decided to uh have some
master data import for the gl accounts that i
needed to create just for demo um posting group
setups item templates and whatnot so how am i
going actually to to create that data as hardcoded
data nope i decided to go with gemo files and then
convert them to json during import so what you see
here in uh the demo data is a resource file with
um data in it these are the gl accounts that i
wanted to have this is a demo file that is added
as a resource to my app so in my app json i have a
resource folder the brewery demo/demo data and in
my uh code here i just say move it up json object
read from gml and then get the resource as text
that worked like a charm i mean i could have done
it as a json file but i decided to go with jammo
because it's more readable and easy to write yeah
and no ai model knows about that because this is
the new feature is a new feature so um the model
doesn't know about it unless you tell him to use
that right and then um of course i could use
those new stuff in uh in json like json object
get boolean get integer uh json object get text
all of that um because i know that that is new
and then i had to import the data from the from
that api beers include a picture and the breweries
well that was funny i i called dimmitri i said
"come on you had in your requirement i have to
import breweries but come on sell to pubs right?"
yep so how is that work brewery is actually your
vendor of beer not your consumer it was not your
customer it's just to have a list of customers of
course so i used the rest client module of course
i did supports get as json and i'm using the new
json functions as well and just to show you how i
do that very little code actually this let me zoom
it in now you see all the code of my connector
code unit to brewbody that's all it takes so i
just say hey get as json from beers well it knows
where it is because there is a base address here
um and that's it get as json as an array and then
in my code somewhere down here i can then say
um connector get beers and beers here is a json
array and that's it that works like a charm
actually so with that i could import everything
and of course by the way after importing
um demetri is something that i didn't show you
but what i have in here is a view for all the
beers i mean why not i'm not going to run the
import believe me or trust me it works by the
way you know fun thing ai actually when i during
his generation also created me a view of beers but
it didn't use the view uh from the property from
the page it just created an action to uh to filter
the items and then we had that api stuff and the
challenge for me was hey access should be limited
to only the api that they may use so should be
limited to only that one not being able to uh
get any data uh from other apis and it should be
filtered to only show the data from that customer
so what i did is i created a permission set
for pips with only access to that api page
that they're allowed to open to call and
only access to the tables that they are
uh that are used in that api including the login
permission set and to filter the data and add
the enter app id that the customer is using to the
customer and filter it man this is smart so i mean
um let me just show it in a code so here uh i have
my api and in the api i say on the open page get
the current user and it security id and then do a
set range on that id so this is the only data you
get out of it well the source table is in fact
the customer so the result of that looks like
this for one single customer not all the customer
records and that permission set is actually this
one it includes login and has the customer table
data and the item ledger entry table data it
needs to have the customer uh table to execute and
access to the two api pages that i have that's it
and is the only permission set that i assigned to
the uh azure app um the entra app uh registration
in business central and it worked so that is to
make sure that the customer cannot get access
to data that he should not get access to so with
that i think it's time to put us to a vote yeah
but i i want to admit before that you cheated okay
did i cheat yes you should because you used your
23 years of experience of coding to not do any
code here so so you really implemented so small
code man to do handcrafted coding it takes some
experience i'm afraid yep all right so um let's
put this to a vote which one do you think is the
best approach and we're going to have let's wait
for half a minute and then show the results okay
so you have three options there it is either vip
coating or handcrafted or a blend of both that's
actually the uh the three options vip coding
come on
so let's see
man
400 responses dimmitri do you want to
say something uh i i own you a beer
or maybe a keg a keg of beer a ke of beer yeah a
pellet i think that blend brew what you see here
is actually the the two combined yes so um if
you yeah together with five coding it's still
less than handcrafted but i'm i'm actually
surprised because i was like okay when i
had a discussion with dimmitri back in december
actually i was like okay i'm not going to stand
a chance against the master of ai himself no but
i but i pretended to be a junior okay uh yes you
you pretended to be a junior absolutely yes you
did well all right so thank you for voting i'm
going to change back to our conclusions that
um we had after we um uh well shared what we
created and in our conclusion generally spoken
ai is good for generating code we can use it but
um you should use it specifically to generate code
when you're talking about apis or test code or
documentation and that is what it is actually very
good to because it is not so good in understanding
the business logic has no knowledge about the
business central internals um does not know how to
utilize standard features so if you just give
it a um a list of requirements is not going to
judge it's just going to create what is in those
requirements is not thinking hey we are here in
um in an application yeah you want your screen
yeah yeah okay okay we are not here in um
uh extending an existing application it does
not know about all the features that are in
there and does not know about the latest al
features so in our opinion it still takes a
captain to use co-pilot exactly i fully agree
with that so um usually the story ends here
but we have 10 minutes left and some beer and
i need to return some points to myself okay so
um let's uh let's assume that um one year later we
got this app running and we have uh like a lot of
data like okay calculies a lot item ledger entries
a lot so you can of course analyze them using the
internal tools on business central but we can
do something special and uh let's do the data
insights with a copilot this is awesome on show
you knowing really yes so um what i have here
uh it's an app which is called data insights
copilot let me zoom it a little bit so i can ask
uh the questions in natural language uh which
pups have the most outstanding cs so let's see
so the popups with the most outs are this blah
blah blah with a c okay you see the the answer was
a natural language okay uh maybe i can ask it for
the distribution of my customers by using the cats
and i can do this also with some look
at that nice charts okay i can do i
can ask other questions about
the cs like uh maybe we have oh
like give me the movement volume per month
given this returned complex question by the way
okay let's see if it works generating better code
i like that phrase yep maybe i let's
see it has a three three shot three
shots okay let me maybe sometimes you
need to run it again switch the model
you mean ai model or yeah yeah i'm talking about
the ai model sorry okay let's try it once again
i mean can do this now we have like this was
a complex uh question if you ask how is this
done yeah okay actually i'm not saying i'm
not sending any data at all to the llm at
all so what is happening here it's actually
generating the python code that's run in the
azure function and it identify which apis
are available in the business central it
identify which apis are relevant to answer on
my questions it pulls the data uh from this
api combine this data together and so and then
return me back the data and the charts and then
i use it's interpret this data using also a large
language model the good thing is i need to return
some points you remember this is open source so
uh yeah it's for you so uh uh really yeah so uh
this is in my github bc code interpreter and there
is a aure function there is a business central app
uh there is a description how it works
uh with the architecture i also have a
blog post on that so you can go and uh learn
it so well it's it's really works quite good
so let's ask it really good really important
question about the beer which beer is the best
fingers crossed
okay that's a tough question oh yeah oh yeah
but it found everything it needs let's see
the selection of beers for the bct days
walking dinner includes a variety of
unique options enjoy discovering
your favorite during the event
[Applause]
there's there are beers there are
beers so and you know what what i say
so if we hurt you in any way take a beer let me
open up for questions uh somebody is going to
throw that stuff and i will then do the t-shirts
okay so you made ai build you an app in two days
yep how long do you think would it have taken
you to write one yourself how long did it take
you hold on no no hold on yeah then how long would
it take you when you combine your experience and
use these ai models to help you in uh you know
generating fields or whatever yeah it's a good
question so um from my experience i would say
that um it's almost the same amount of time
uh takes for me to write the code by myself or
the code using ai uh but with the code when i
when i ai help me to write the code actually
i get something extra always for example tests
i love to write tests by itself of course but ai
really good at that so um but also some additional
features uh you can always get maybe you forgot
about something to implement ai really can help
you not in the business logic that's is still bad
but uh in um like u these apis things it's really
uh helps you to integrate gentleman over there
has a question hi test hi um uh we had we had
similar i had a similar qu uh question we did it
on one of the social networks but i'll i'll give
it a try once again yep why is we always say uh ai
is not that good in al right um i didn't tell that
i think you did actually i i don't understand the
complexity so the answer is so if you have python
or whatever other there is a lot of sources on
the on the web and everything i understand that
that isn't bc if you only talk about standard
code that's something fixed that's something
microsoft can fit in in one of the models in
matter of minutes i guess let's not talk about
add-on size and so on that's just it python and
other languages they are much more you know not
not that fixed where is the complexity i chatted
actually with ai to ask why ai doesn't know al
that good um then they say bc is not only about
code it's about business logic and everything
right it needs to understand accounting posting
groups and everything but microsoft can take
this contoso or how do you say demo company
and feed in that it doesn't need 10 million
records it it needs couple of master records and
everything where where is the complexity why or
are we getting it soon or how we push microsoft
to do it i don't know i don't understand why is
it so complex okay a long question now we have a
short answer because sorry yeah so that's a fair
question uh so first of all uh why it is bad in
al well now it's not so bad in al syntax okay uh
but al is not only a syntax is a business logic
is the existing functions uh in a base app and so
on so it it it struggles there okay so um uh the
other question was why microsoft didn't uh teach
ai for the al and business logic well uh i don't
have i can't reply on behalf of the microsoft but
um what i know that they don't well microsoft
don't train their own models we we they have
some small models that they are trained like
uh uh p uh but um they're not really investing
in this so they are more interest as i understand
is consumption of a their asure from the from the
models of other providers so that's their business
model okay so that's why and um other providers
they train their models in a more generic way
is it uh yeah cheers no no no so just helping
yeah so the the companies like openai antropic uh
they well they don't know what is bc what is al so
what they are doing they train their models on the
github yeah so okay our app like a base app is on
the github but python for example there is like a
hundred millions of different repos on the github
and we have like okay if we have thousands it's
quite a good number so and a large language models
are trained to predict next word so they need to
learn on the existing data the more data they have
the good the good is uh prediction we just don't
have enough data for that all right so gentleman
in the back hi yeah um dimitri this question is
for you um again uh yeah all the questions man um
while you was being junior developer um did you
found or is there any way to give the capacity
to compilot in vs code to read the symbols from
installed app files because it keeps uh suggesting
standard methods that don't even exist and it will
really help if it if it stopped making them up yes
because when when i'm programming for me it's a
bit frustrating and i don't know if it happened
to others but uh it doesn't use or have knowledge
of the standard bc methods flow between cod units
or events exactly so uh we we we now have like a
two most common ide uh where we do al development
most common is a vs code and a cursor yeah there
are some others but uh they're not so commonly
used um corsor was always um uh before the vs code
so first ai features were released in corsor and
then vs code actually picked up and implemented
more or less the same features in github copilot
in vs code but the latest release in the latest
release of vs code copilot they have ability to
reference symbols symbol files in the chat so
in the chat you can reference not only files
but also symbols which we don't still have in
well not we but i using cursor so uh but uh
i don't have this in a cursor uh yet uh that's
why my workflow is more maybe old-fashioned okay
uh like i i have my base app always open uh and
then i i know where to search it and uh i grab
some code and uh uh put as a context by the way
also good good uh thing that uh in in when in this
is the same in the vs code or cursor you have a
base app and if you want to search something okay
uh uh the normal search you need to know what to
search okay you need like keywords or something
the name of the function and so on but uh if you
use in the agent tab you can ask a question and it
uh the base app is already pre-in indexed in uh
in the workspace so they can uh do the semantic
search uh through the base app and uh it's really
helps sometimes to find information that you don't
know where exactly it is so we have one last
question over there okay uh my question is um
did you try to provide to combine your two ways
and provide to ai for example functional design
at the beginning to prepare functional design
like in uh standard way and after that provided
like additional document to ai to understood what
vendors should be what it should be items what we
should use posting group and so on and so on yeah
so that's actually what i did uh at the beginning
when i told about context preparation part there
was a but i called it like a development plan
uh but in this development plan it was more
technical how this should be implemented yes it
was technical not logical not business logic yeah
yeah yeah but there were some logical stuff as
well uh but as a junior developer i actually give
this to the ai to generate this for me so actually
maybe uh as a workflow could be also import this
from somewhere or created by yourself so yeah i
agree if uh ai was fed with a functional design
with more specific instructions then of course
that combination would be uh would result in a
better app um and that is actually why i think
that a blend brew is the correct answer to the
question what which one is best it's not one is
the best it is the combination that can make it
really strong thank you all right with that uh
thank you enjoy the beer and the welcome dinner
thank you and ditri come on cheers cheers cheers
