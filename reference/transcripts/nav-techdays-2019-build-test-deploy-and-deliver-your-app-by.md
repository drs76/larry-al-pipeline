# NAV TechDays 2019 - Build, test, deploy and deliver your app by one file

- **Source:** https://www.youtube.com/watch?v=eBytbBNCd3w
- **Video ID:** eBytbBNCd3w
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 90m33s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome everyone on second day of
Navtech days I hope that you enjoy the
beer tasting history and you already
wake up from the night you are ready for
some new knowledge you can gain here and
I will try to transfer what I know - I
hope that you will be able to use that
during your standard workday which I
think you you left for for a while
somewhere else than here and you had a
great time to listen everyone and speak
together
the subject is build tests deploy and
deliver you up by one file I will try to
show you how you can do that but and we
will see what does it mean but before we
we go to that small recapitulation
because we had a session last year here
about the CI CD we were talking about
how to create repository and create the
build pipelines on water we have which
branching policy we had delivery
pipeline what is a deployment pipeline
even you see you saw that picture what
does it mean for you the CI CD if it is
that someone was talking about some wife
in connection to that but I want to see
what's the current state of adopting CI
CD please take your phones and please
vote now use that URL and we will see
how we are successful if we were
successful or how it looks today with
this these things I will try to look at
the results and show them to you
I will keep the URL still visible that's
I think very good result but still the
yellow yellow column is yeah that's we
need to go down and have bigger blue one
because there is no why to not do that
and just plan that planning is okay we
want to do but we don't have time maybe
you don't have time because you didn't
do that yeah think about that okay how
many people were voting 100 all 200
people that's that's nice sample I think
okay thanks
I will close that voting for Y or you
can still vote we will continue that
thanks for for this information because
I think it's very very valuable for for
everyone okay how long it takes when you
need to create a new app to create that
app to do something with that test it
put it to those different environments
sandbox and then install it or somehow
deliver it that to to production
environment
that's the question because we need to
be as fast as possible in these days and
questions what you need around along
that way because it's not short way from
when you create the app to the
production environment you need to
create that develop built-in test deploy
to QA because consultants wants to test
that then you you need to do the
deployment to the sandbox for the
customer to test that
do some acceptance of things around and
and deploy it to the production and then
you need to maintain that app for maybe
infinite time we don't know but you need
to count with that because the app is
not short time things that's something
what maybe we'll be there in 20 years
maybe that longer you need to think
about that and you need to count out you
need to maintain it because you saw what
Microsoft is preparing for us for next
release and we know that there will be
some some changes we will need to adapt
to our our application again I mean
situation that the PowerPoint is not
reacting to the clicks how complex is to
create the CIC the pipeline for that
process maybe that's what you think
that's it's so complex we are planning
to do that because we don't know how to
do that right now and and it's so many
steps we need to do to have we are
afraid of that that's just do everything
else between eat and that's that's
everything that's I will try to show you
how to do that in in one file we will
see the result but
[Music]
questions if it is good for us or not
maybe it looks like nice idea
first we will see later of course we
will do that by M L file we were talking
about the M L already of last year even
even Eric world of mentioned that during
his session but we will go to more
details this session and I will show you
what I'm doing in my pipelines and maybe
it will inspire you what you can do and
that it's not so so hard to implement
something and we will try to keep it as
simple as possible keep it simple stupid
yeah that's the KISS principle that's
that's all what we need Yama pipelines
have few parts which we can use inside
we can use variables inside to set up
some configuration we can use resources
which are on Azure DevOps like some
other repositories or other pipelines
which are there and so on we can define
triggers when to run the pipeline that's
when someone puts new thing to the
repository or maybe we want each day or
if each each week to do something that's
that's the trigger and the main process
is composed from from stages jobs and
steps stage is some isolated thing which
you can if it fails you can rerun the
stage it will do again what is inside
jobs are run to separate a
it means some small applications running
somewhere on some server are doing the
job and the job have different steps
which are executed inside that job
that's whole idea of the pipeline this
these jobs are or the steps are doing
what you need like when you are doing
that manually it means you take some
source code you can compile that put the
output somewhere and and so on those are
the steps you can use and of course you
can use the PowerShell steps or you can
use some steps which someone some on
other prepared for you because the azure
DevOps is extend them extendable and
others can create extensions to Azure
DevOps which you can use and they will
save you time we have two types of jobs
we have built job and deployment job
because we have CI and we have CD CI
taking the source code and Forge it to
application that's the the product
that's the build job and CI pipeline and
deployment is taking that application we
create it and deliver or deploy it some
somewhere that's the deployment part of
that process and we can now do both
through y ml there are some possible
things how to work with the variables
inside the Yama file this is one one
example one expression which is used to
define things which are known already on
the beginning when the process the
pipeline process is starting it has some
limitations but our ru stone on many
types and many places that's another
example how to write the expression but
that's evaluated during runtime
it means later in the process it means
it has no access to some things like
parameters because they are already
processed when we are running the the
pipeline am there is cert form which is
some time named macro because this is
what is expanded in runtime and during
the runtime this is replaced by the
value which is referenced inside we will
use that later during the demo now we
will go to some examples we will do
first the build it means take the source
code create the application we will
deploy that application to some test
environment and to run tests because I
want to test that the application I
produced is still working
then I will deploy that to QA database
if you don't know what is QA q is
quality assurance it means it's the
environment where your consultants for
example are testing that application and
then we put that the process which will
take our company's certificate will sign
the application and will deliver it to
to final destination from where you can
install it to environment you want I'm
doing the signature after all that
because that's the the place when I I
say ok it's ok it is working it is
tested it was I was able to install it
to somewhere and so on and I put the
stamp on that that's our official app
and the lasts that will be deployed to
sandbox in the online environment that's
we will do by one Yama file and we will
look at the Yama fight right now
I will go back to or go to the vs code I
think that's understandable for everyone
yeah that's that's the mo file okay
we'll make it more understandable now
for you I think it's much better now
yeah what we see now is definition of my
variables there are two two possible
syntax is how to work with the variables
but if you are working with variable
groups which is something you can
predefined some values in Azure DevOps
and then later use these groups with
some variables predefined in your
pipelines in this case you need to use
this syntax when you have a name and
value I am using different parameters or
variables here to have all the values I
will need during during my built
pipeline process another part is the
trigger part when we can say on which
branches we want to trigger the CI
pipeline then we can say when some files
were change changed we want to trigger
the pipeline and when some files in some
folders are changed we don't want to
fire the pipeline for example when
someone changed the documentation in my
app I don't want to rebuilt the app
maybe I will have another pipeline which
will take the documentation and process
that and place it somewhere maybe and it
will be different process I can use the
triggers here to filter when I want to
run the process as it is defined
that's the triggers and branches and
paths which you can use during the bat
and then we have another type of
schedule
that's a sorry trigger that's the
schedule it means you can define when
the pipeline will be run started based
on the time for example each week or
each month and
Microsoft is using the Quran syntax to
entering that that information the zero
zero means midnight and the asterisk
means each day each month each day of
the week you can set up like I wanted to
run in midnight on Sunday first and and
so on that's that's really really you
have many possibilities how to set up
that and again you are starting on which
branch you want to run the pipeline in
this case the always parameter says ok
run that even when there was no change
in the code because maybe Freddy just
generated new master image for BC until
one just test your app with that master
image that it is to still working and
running ok first stage that's the stage
when I'm building the app and even
installing the app to the container and
running the tests on that application
that it is still working and that's all
is ok and you can see that there are so
many yellow lines that there is
something with the syntax that's a
problem that I'm using the syntax
highlighter for as your pipeline in the
vs code but the the vs code know nothing
about tasks I am using there because I'm
using extension for Asia DevOps
which I created for our out purposes
it's open source is available on store
you can use it freely for no price it's
only with if you want on if you if you
want to change something you can just
create the pull request for that that's
extension if you want if I switch to
just plain llamo syntax highlighting it
will be much better for me right now
each job have some parameters again we
have a display name name of the job of
course and then we can select on which
agent we around this process agents the
small applications running somewhere
connecting to Azure DevOps could run on
some hosted virtual machines or on your
own servers doesn't matter and you can
choose the pool you want to use and even
some futures you can demand some
features and the agents have defined
parameters if they are supporting that
feature or not I am for example here
requesting that it support docker then I
set some settings about the workspace
that I want to clean up the workspace it
means the folder when the process will
be running I mean I want the first to
clean it up because maybe there is some
leftovers from previous processes and I
want to have a clean green folder and
first step for me is to take the code
the source code of my application from
the report repository I am working on
that's the first check out step if you
don't put it there it will do it
automatically for you I am having that
step here because I want to set up the
recursive parameter for sub modules and
questions what are the sub modules who
was on my workshop this is this week
about the deep dive we were talking
about the sub modules if we will have
time during this session I can touch
that but I think we will not have enough
time for that
but please look at the sub modules it's
something like git repository in another
git repository you can you can connect
for example the depending apps together
to have them available from one pose
as you need another task is just
installing some modules like enough
container helper and my partial modules
I'm using because I don't know if they
are already on the computer where the
agent are running is running or not
that's that's just another task from my
my extension then I create a container
with the parameters I set the through
the variables that's why I have these
these dollar blah blah things here
because I thinking the values during the
preparation of the pipeline that it
means it's it's on very beginning
replacing these these values and of
course I'm not including seaside anymore
but I'm including the test suit with
test libraries only here for example
then I will I am working with nougat
packages to deliver
for example things which I'm depending
on because if I want to install my
application and the application is
depending on another one during
installation to my container
I need this depending depending app and
if I I don't have it somewhere I will
download it from line you get a server
which is Azure divorce for me and I will
install it automatically that's that's
why I have this this parameter this step
which is installing the nougat at all
because I want to be able to download
the new get packages then I will compile
the application that's that task will
find every up Jason inside the work
directory order them in order of
dependency and will compile the apps in
in this order automatically it means if
they are depending apps it will compile
them install them first and so on that's
that's complex things and of course I'm
enabling different code cops to to check
the results and if there is warning from
the code cop it is error for me and I am
failing the the whole pipeline because I
don't want my my developers to
have a code which have warnings from the
cold cup of things from Microsoft
then I will publish the application to
the container it means install sync and
so on and I'm of course skipping the
verification of the signature because
the app is not signed yet then there is
a some partial I want to show you how
you can work with the variables in in
Yama pipeline for example from from
partial that's partial is here because I
need to find out the application ID of
my application or of my test application
because I'm using the lighter step which
run all tests from that application
that's the power shell which will find
it for me and we will set through the
right host here the variables in the
pipeline that's the special special
things which is supported to be able to
run to set up some external variables in
the pipeline through the scripts I'm
just writing them to the log and later
using them for example here to run the
tests because here is the variable I
will use and you see the difference in
in the expression that I'm using the
dollar brackets not not the other one
because it is during runtime because I
need to wait till the preview step was
finished it means it must be in run time
and it's expanded as a macro then I will
publish the results take the information
about the main app because I want to
know the name of the lineup because next
step is just exper just exporting the
runtime application for me from the
container because as a product of this
build I will get my application or main
application I will get my test
application because I have both in one
repository then I will have runtime
application ready
be deployed for on Prem installations
and I will have the translations as a
result of the compilation because you
know that the translation itself or the
translation G file is not source code
its product of compilation then the
translation G file should be in your kit
ignore because it's not source code it's
generated each time you compile the
application and I have here other steps
which will take the or other translation
files for the different languages I have
and put them as a as a result of this
compilation because for example my
consultant could take that translation
file translate it send it back to the
developer and it he will just update the
application with the new new
translations just simple copy files task
to move the files between folders
because I want to publish some files as
a artifact as a as a output of my
pipeline that's for the the app is for
the translation and then I just throw
away the container that's the whole
build pipeline it's long but it could
make everything what you need next stage
is to take the application I just
created and just install it to a
container and run the test again because
for example I want to try if I'm able to
update my previous version to this
version I'm not doing that
exactly in this stage yet but I'm
installing the application as it is to
to my container for example to check
that all the dependencies are still
available somewhere to download and it
is working together there is a same
parameters same things like in previous
case display name environment and new
one is environment but first I skip the
depends on depends on is studying
as your DevOps after which stage will
this state run it means I am depending
on the preview stage there could be
multiple stages I am depending on it
means I can run multiple stages in
parallel and one stage could start after
all these parallel things are finished
and in reverse versa
I can run multiple stages after one
stage finished it means I can run out
and find a fun in that's the the pan
depends on we have a environment here
which is new and we see that the job is
deployment job deployment job is each
time connected to some environment
environment is something for me defining
that ok I'm putting something to the
sandbox or to life environment an
environment could have some settings
like if someone wants to use this
environment the owner of the environment
needs to review that and need to approve
that it means okay I can set approvers
to for the environment and the pipeline
will wait till the the approver will
approve that and then it will do
something that's the environment you can
see that deployment jobs have some
strategies there are multiple strategies
to deploy something azure develops right
now are supporting two and only one is
have some meaning for us in business
central we are using the run once it
means just deploy yet because another
one is deployment canary which is
connected to kubernetes and these kind
of things which are totally unknown for
us yet maybe in some years yep we will
see what right right now each time you
will use the run run once deployment
strategy and of course the deployment
have steps again install modules create
container finds the info
about my application this time I have
only the app file it means I will take
the app file through the PowerShell I
will read the information from the add
file which ID name and so on it have I
will install nougat deletes files like
runtime app because I downloaded all the
apps I produced and I want not to work
with the runtime that's I will just
delete it and that's that's all publish
the application to the container and
during that publication if there is a
missing dependency I will download the
dependency from my servers from my
nougat package server and install it
automatically run the test publish the
test and remove container you can see
for example the step or on the task
remove container that there is a
condition always yeah I want to remove
the container each time even when the
the pipeline fails or I cancel the
pipeline I want to remove the container
because next time if I will try to
create it it will fail because it
already exists for example yeah you can
clean up after your run just to set the
through setting the conditions another
value for condition this succeeded or
failed always is even when you cancel
succeed or fail is if it fails or
succeed but not if you can store the
pipeline manually next stage release
took to queue a database you need you
see that it's AG a deployment step to
another environment only but not only
the same it will automatically download
the the produced application from the
build build part build stage I will
delete the test application because I am
NOT installing test application to QA
database because nobody will run the
test there why I run it already two
times I will delete again the runtime
just publish the application to some
container and
so I'm not creating container I'm doing
nothing else I will just put the app and
install it somewhere afterward that
there is a sign in the river East stage
which is nearly the same just calling
another task to sign the application
with some certificate with some password
certificate is saved in Azure DevOps as
a secure file which is automatically
downloaded in step download secure file
the path of the downloaded file is then
placed to some variable here download
secure file dot secure file path which I
can use in my next steps to work with
that file then I will create new
artifact with science application as a
product of my whole pipeline and this
signed application could be used
somewhere when I need that delete the
files get the the version from the
application because I need it and now I
am doing some magic to create nougat
package nougat is is package management
for four different purposes used mostly
with dotnet and so on
I'm creating that package through my
Parishad scripts which are freely
available on internet and I am just than
pushing that our packing and pushing the
resulting package to Azure Deb's
artifact server or service and the last
part I am releasing to online sandbox in
one pipeline it means it will be
triggered automatically when someone
update my app but because we are working
with the environments I can set up the
review process on that environment it
means the pipeline will wait before it
start this stage to that someone needs
to approve that and it means it it could
be here for example one week and someone
will press the button that accept to
release to that set box of this version
and this version will be released to the
to the environment this process is very
simple just removing not needed
applications and calling one one task
which will in this case release the
application to this tenant to the
sandbox through the automation API
version 1 and it will include it it will
not include the test for a test
application and to authenticate to the
tenant it will use my application ID
which I created in a ad that's another
step I need to do we can look at that if
you have enough time and it will login
me through my login and password as a
partner to that that tenant that's the
whole pipeline but you can see that it's
five five five lines five hundred fifty
eight lines long that's that's
everything what's inside the result will
looks like that template that and that
is the result what you can see is multi
stage pipeline first stage second is
test release to my queue a database
that's that's the these steps or all
these tasks were running to deploy that
then I signed the application through
these all steps and creating the new get
packages pushing them removing the
container and then I was releasing to
demo sandbox you can see that I have
multiple attempts here at them
here's a show previous attempts attempt
one it felt from unknown reason because
that there was just error salaries not
available anymore it means I had a
possibility to run these steps again or
this stage again and it was deployed
successfully later this rehren
functionality is really really new it
was not there one month ago it was added
the last month there was some back in
that probe but it's already fixed the
the assured efforts are really going
fast forward even the the multistage
pipelines were not existing last year
when we were talking about CI CD they
were planned but they're not implemented
now are implemented and are we can use
them that's the result of our pipeline
if we have this file in our repository
it's very very easy to create new
pipeline manually oh sorry
[Music]
pipelines new pipeline I just select the
the repository where my far is select
existing as your pipeline Yama file
select the file I have and click
continue it will take the file prepare
the pipeline I can just click run it
will save that and and the pipeline is
ready for me if I need to change the
process I will change the file commit
the message in vs code push to the
server and the pipeline will use that
new process to do what I need that's the
strongest way strongest thing of having
the pipeline as a code because if you
don't have it as a code you need to
manually edit the pipeline somewhere
else and yeah it's it's a lot of
environment and and so on now you can as
a developer can maintain the pipelines
themselves just by changing the Yama
file
okay going back to presentation
Oh
now I have additional requests because
that's that's the one thing we did built
to deliver somewhere but for example I
want to use this pie pie for my pull
requests I can't imagine that I will
create pull requests it will trigger the
build and the result will end somewhere
in the customer sandbox I don't want to
do that as a part of my pull request
when some someone wants his code be
integrated to the product and I am just
testing that what he produced is correct
I don't want to release that part I want
to build only in this case not the rest
of these stages or for example I want to
deploy on the master or release branch
because I want to run this by a pipeline
only for this these branches not when
someone creates his own branch and is
just testing somewhere there I don't
want something there I don't want to
build that and then I want to schedule
the build with the master image because
I want to be sure that the next version
will not break my application that it
will work there are no some things which
are obsolete now and so on I need to
solve for example I want to test it for
example one per week we will look at
that how we can extend the existing
pipeline with these these things going
back to Yama file I will switch to
another branch which I have here instead
going through all the things here I will
go to my get lands and I prepare compare
here
I'm comparing the current extended
version of the pipeline with what we did
in previous previous example all the
values of the variables are same I just
added one thing that's resource the
resource is about that I'm using another
pipeline as an input for my built or I
can trigger my pipeline when the
pipeline another one is finished in this
case I will use it to download some some
product produce of the output as a input
to my pipeline which will deliver that
to some sandbox or live environment
because as a part of the change I am now
trying to solve once problematic things
which we had in a previous case in
previous case we build it tested put it
to the QA and then we were ready to put
it to sandbox and if there is a approval
and it is not approved it will fail
whole pipeline and that's what we don't
want because it was builded it was
signed it was successful only the
release somewhere was not approved it
means I will now separate these two
processes but still trying to use the
same file for that it means I can have
two pipelines defined connected to one
Yama file but internally I can do
something else when I run one pipeline
or second pipeline that's what I'm
trying to do that and you see that here
we have some condition expression could
be even condition in the condition I am
just comparing if the
finishing of my pipeline ends with
release it means if I create a new
pipeline ending with release at the end
of the name and I will run that pipeline
it will release only the application if
I will run another pipeline which is
don't ends with release it will do what
we did in previous case build test put
two QA sign and safe summer that's one
part of the condition another part is
that I don't want to use that built
stage when it is scheduled it means it
is triggered for the case when I want to
test it with the master branch a master
master image because I'm using the
schedule for that if it is scheduled it
is not the standard common build process
it is different one and I want to test
it with different image that's in the
condition and you see that the stage is
part of the this this condition because
it's indented it means it will be
running or this stage will be included
only if the condition is fulfilled
I will move down there that all was the
the process we had and now I have
another condition which is just slightly
different it is only if it is scheduled
pipeline if it is killed I have the same
process but when creating the container
I am using different variable master
image name that's the only difference
but you see that it's it's really crazy
that I needed to copy-paste this hope of
all part here okay those are the changes
and there is another condition for the
test the builded app but it's just
extended that it is releasing when the
source branch for which I am running is
release branch or master branch that
the condition if it's master it will be
installed to my Q a database and
something if it is not master branch
then do nothing and including even and
it is keeping the pull request build it
means if this pull request it will do
just the built stage but not the rest
that's all that's the conditions are
here and at the end we have another
change just for the manual think when I
run the pipeline manually and the
pipeline and sweet release or and it is
for master branch or release branch that
definition ends with that it will run
the release to sandbox if I run just
common build it will not do that part if
I run the release pipeline manually it
will only take the result of the
previous pipelines and release that what
is the result it looks like that if I go
back to my pipelines I go to the
template up that's the second pipeline
you see that this is regular pipeline
which was triggered when I push some
change to my repository and it was
master a master branch it build it it
tested it released due to the QA and
signed the app and publish it somewhere
there is no release to the sandbox if it
will be pull request there will be only
the first stage not the other and I have
another pipeline here created which is
template at release which leads to the
same file and when I when I trigger that
manually it had only one step releasing
to the sandbox it means when someone
decided okay that app is ready for
release run will run manually that that
pipeline and that pipeline will take the
app and will install it to the sand
that's that's possible and it's still
using one one pipeline okay going back
to presentation be ready to use your
phone because we are near the next
voting do you like the results please go
to that URL and vote
I will show the result here for you
yeah still at you are feeling that I'm
going somewhere yeah because we have
still 40 minutes left from the session
yeah that's okay as you are thinking
about that
definitely not yeah okay yes definitely
yes that's cool but yeah we will see
okay
thanks for the voting I will say okay
how many people few voltage there is 200
again okay that's good
thanks for for the result I will
continue because the question was if you
like it I don't like it I guess really
it's it's a mess
it's my son I can't imagine to use that
pipeline in my processes the pains of
the one file rules them all in this case
it's that it's hard to combine for the
different triggers for example because I
can't make the triggers dynamic in one
case only to have the schedule and one
have triggered when someone pushed
something somewhere yeah I can't can't
separate that it means both pipeline
will run when I push something there but
they will have different
stage is running inside based on the
conditions I have having the deployment
to sandbox and production as a part of
the CI pipeline's problem as I told you
if you cancel the deployment it will
cancel the whole pipeline release will
take sometimes the wrong result because
if you take the pipeline which was named
release and you run manually it will
take the last successful build of the
second pipeline but the second pipeline
is even doing the pull requests for
example or builds of another branches
okay that there is a filter for the
master branch only but it will take
maybe some time wrong built wrong result
it's impossible to separate the result
to have them for example on some
dashboard to see if releases are okay
and standard builds are not okay and so
on because there is no no difference how
to how to make that there is a complex
it's complex file to maintain of course
change of the process mean you need to
update all the repositories and for
example we have a shriek customers with
BCE running and we have over 40
applications already updating these 40
applications
oh it will be maybe 20 hours of work to
just take the app take the file update
the repository push it sorry okay maybe
five minutes per one up but yeah you can
imagine that it's a big time you need to
for that and it's really a heavy
copy-paste it means if I want to change
something I need to make it on multiple
places let's simplify that we have of
course some tools to do that we will
move what is shared to shared place to
have only one place to change that what
is similar watch it
what is shared
with all the pipelines we have brief in
the app repository only what is really
specific for that app or which could be
specific it means I will be able to
change something if the app needs
something's different
then I still will be able to do that and
we will separate the things by purpose
it means there will be one built
pipeline one check pipeline with the
master a master image and one for
deploying the app to send books and live
environment let's go and break the file
found the correct mountain for that we
will template the Emma file we will use
the templates and Emma fire is
supporting templates we were talking
about the templates already last year
but we will look at them closely now
again the demo time
going back now I switch again to my
pipelines here exit the Zen mode and get
a good lens and look at different
compare here first thing is that I have
now four four files here one is the
original pipeline I had you can see on
the left on the left is the one we had
on the right is the new new things we
the simplified one you can see that many
many variables were moved to separate
file which is named built Yama file and
I'm including that file and all the
variables inside in my my Yama file
which will create the pipeline that's
that
template as four variables I leave some
variables in the pipeline file because
they are more more technical
I am not expecting that they will be
changed too much all the variables which
are in the beauty ml are connected for
example to which server I want to
release this up and and the developer
could change that and in this way he can
decide to which QA database that will be
installed automatically it means
developer could change it more often for
example but the predefined things and
will never be changed for example I
removed the schedule because the
scheduler is for for another reason
therefore to test with master image it
will be separate file we added one
resource one resource because that's the
resource where our templates are placed
that's the central repository for the
templates we will use in our pipelines
if we want to change something I will
change it in these templates in some
specific repository I have for them and
all the pipeline's using that templates
will automatically use the new process
next time when they are they will
trigger that's the repository in this
case it's on my same server it means I
don't need to tell the server name I am
just telling ok use the master branch
for this case because I can have for
example better template branch where I
am preparing some new things and only
one app could use that and I can test
the templates on that app and the stage
this whole stage this whole things which
is right on the left it's now only these
few few lines on the right because I'm
calling the template file from the
repository that's the the CBL stage
llaman from repository templates and I'm
passing some parameters there
I can define in my template which
parameters I need and the coring process
could set these parameters if it will
not set these parameters some defaults
will be used I can define even the
defaults in templates it means if there
is nothing changed I don't need for
example the parameters there are some
other parameters compare is just moving
them so that we replaced with the
template and there is another template
for another stage I have still having
the the conditions here I can remove
part of them but still I want to run
that only for the releases and for the
master and that's all that's the release
and test stage then we have the release
to contain our stage it means the to my
QA and you see that the template is not
named release to QA it's raised to
container stage because maybe I really
really use this stage for some other
database I have because I have a
template I can just copy this part and
do something else and because we are
dynamic now and the temp I don't know
what is previous stage on which it
should be depending I have one parameter
here where I am passing the dependency
and if I want to change the pipeline
somehow to have more parallel things or
serial things I can just play with the
depends on parameter and do what I need
in that and the last thing is sign and
deliver again just few parameters and
that's all it means if I switch to that
branch I will have only this file with
few variables some basic triggers
resources and few steps with few lines
we
only 86 lines now from 558 that's much
better for maintenance and doing
something if I want to release to
another server there I will just copy
these few lines and change the
parameters that's all
another file with which we have that's
the the the one with with the parameters
nothing curls and another one is for the
built with the master image few
parameters resources schedule no trigger
because I don't want to trigger that
when someone update the repository I
want to use only the scheduled one and I
have only one stage here which is very
simple because that's the build stage
with just a master image as a parameter
nothing else and once in this case it's
once per day it will take my my source
code and build it with the master image
and I will see the result if everything
is OK or there is some problem and I can
start to work on that problem if there
is some and then we have a really spy
plane which again have only a few
parameters taking from the my file with
with the variables no trigger because I
will run that manually when I need that
but if I want for example release each
week or something automatically I can
use the schedule and there is only one
stage using some template and in this
case I prepare template which allows me
to release to two environments through
one call of the template you see that I
have here two parameters or the one
parameter release two which is
structured there are two records and
trees objects with different
things one for sandbox one for
production and the release for
production is depending on the release
to sandbox if I just remove that that
depends on it will do para release it
means both will be triggered
automatically and if there is approval
then for example the project to release
to the production we wait for the
approval but the the release to the
sandbox will run automatically if I want
to have it first release to the sandbox
if it will fail
don't try to release to the to the
production that's what I like more it
will be defined in this way
second is depending on the first one and
how to how the template looks like we
can we can go to the repository for
templates and we can look at that we
have this pipeline template stay
multi-stage okay I will try to make it
bigger that's the template for the stage
have some parameters with some defaults
already and there is expression using
each for each something from the
parameter container name create stage
with some variables it means I can
dynamically create new stages based on
some parameters I passed it means in in
vs code we have here test environment
test environment and test environment
and now we are going through the
parameters and container for each
container I want to release there
because we have even the the container
of somewhere
okay let's release - there should be a
release - and we create call - template
trees - container with the appropriate
values here that's the template for
releasing the template for for building
is something similar just default
variables and what we had on the
original file is splitted to different
templates for the stages and the stages
are using again templates for the jobs
it means I have here job to build and
test release and test release -
container and so on and I can reuse them
if I want because I for example want to
have different stage with new jobs and I
don't need I don't want to copy and
paste the values again and again in the
round that's the template and the
simplification of the Yama file I will
go back to presentation
[Music]
now we have this situation there is no
one file to lose them
we have only one file to build them one
file to deployed to all and one to must
test them because those are three things
we want to do wet with the wit of a
pipeline and we have three files for
that fourth with some parameters that's
the result we have repeatable blocks we
have configurable plans we need to
create a three pipe lines for each add
to build release and test and we need to
create a pipeline manually or maybe we
don't need to do that manually because
three pipeline for each each app it will
take some time to create that for us
okay it's few clicks but still too much
okay another voting how many apps you
can create per hour with all the three
pipelines created with distinct ID
ranges assigned inside the app Jason
with nougats applied to up Jason and so
on it means how many apps you can
prepare for for developers to develop on
in one hour please vote what do you
think that's the question
and I would show you result up gang I
don't like that okay
yeah yeah good why not that they are
there are expecting something 157 okay
there's still 50 people not decide it
what's can be okay we will not wait more
for that I will show you what I'm using
of course PowerShell as your default API
rest or REST API and everything you can
ultimate ice even that I will switch to
my application I have a small script and
I will run that I know that I will
remove the pads after the presentation
that there is nothing nothing hidden
inside that now my script is creating
the application so there is only 10
applications to be created and I am
counting the time it will take to
calculate the average of the application
I can create through that all depends on
the network speed you can see that I'm
downloading the application from the
remote repository and that is taking
most of the time I will see the result
but when I was trying that on a hotel
that work it was around 200 applications
if I was trying that on a virus which
was faster than than the hotel one there
is was 500 applications per hour I
was able to create it means all depends
on the speed of the network and I think
even maybe the 1,000 could be doable on
fast network if I run that and assure we
have only only few developers and of
course we will not need so many apps but
you can see I can create 477
applications per hour if I want it means
you don't need to be afraid of creating
new apps even if you have depending apps
the pipeline will work with that even
the multi route workspace in vs code is
able to work with multiply the pending
apps don't be afraid of that but maybe
the question is ok how I will find out
which idea range I can use because in
this case it generates new idea range
automatically for me because I am using
or three that's I am using even Azure
defaults to keep track of my
applications because I think ok we have
for example feature work item and
feature for me is application I modified
the template for work item of type app
feature and I added few few fields there
to help my cast my developers to find
correct application when they need to do
something because they get the user
story and task and the user story is
assigned to some feature and the feature
is application for me it means there is
a decision process when someone tells ok
this user story will be done in this
application this this feature and the
application is in this repository and
it's using this ID range and I can work
through the rest API with these work
items and finds next empty
I'd arrange if I want and so on it means
yeah I can ultimate eyes that and even
the pipelines for these apps were
created for me and were triggered and
you see that I have three pipelines for
each up up master to test up release to
release it when I am ready to release
that and the app which is pipeline which
we were built the application when I
update the source code or when somebody
wants to merge pull request it will be
triggered and it will test the result of
the pull request that's just about
calling the REST API and doing these
things automatically it means everything
could be automatized and the rest api
are our strong tool going back to that
presentation much faster is to clean up
all that I have script which just
cleanup or the work items and
repositories and so on and see much
faster than creating the app okay how to
deploy to on Prem that's another
question of course you can take the
application copy to the remote server
and do it through PowerShell or you can
have built agent on the server to do
that but of course be aware of the
security because if there is if the
server is the customer server the agent
have access to that server and if
someone triggers something which is
dangerous it could make problems I will
not go this way when it is not my own
server on my own server when I'm hosting
for someone for example okay I can run
the agent on that server and let the
pipeline's
install something to do this environment
easily I will not use that for customer
service automation IP I could be used as
we were using it in online you can use
the same API even for the on-prem why
not but you need to have access to that
API from the agent on which the build is
running you can use hybrid network for
that maybe just try that or you can mark
the bills somehow on in Azure DevOps and
run script on the server of the customer
and it will connect to the azure devops
filter all the bills which are marked
for with some tech download the product
from these pipelines and run scripts to
install that yeah I have this script I
will not go into that because not enough
time for that but it is doable and it's
semi automatic keeping for example if
you have a problem to take files and put
them to the customer server because
there is a security which is forbidding
that you can use that you can connect to
the azure DevOps and download the apps
the the file through through this call
you can install that through new get
because we have now NuGet packages on
our server we look at that in a while
and of course don't forget to update the
license for the customer and the
question is ok how you will get the list
of objects you have in the application
before you had the one database and you
saw all the objects in the object
designer now yeah it's not problem to
create the tool but this session is not
about that but you need to think about
even that part and how you will assign
for example the ID range 500 - 500 nine
four tables which are pre assigned in
the license
will you be able to use that in multiple
applications I think no okay
we're skipping that summary we have all
in one file or we had that but we find
out that's not nice and not practical we
created multiple files which are better
for maintenance
we ultimate eyes upon pipeline creation
which is not problem if you want we
ultimately end appointment or we can
Tama theis we didn't go deeper into that
you can download the app from the or
it's good to allow download the app if
you are ice V to your partners if you
create new version they can have access
to your nougat package or something like
that server and they can download new
version each time that you release that
and of course the translation is product
of the build if we look at the server
now window in artifacts because I was
running some pipelines in before I have
applications one is main application one
is the test application for that and if
I look at the test application you can
see that because it's nougat
it's even keeping the track of the
dependency that it is dependent on
another application I'm using nougat
just because that because I need only to
download the top application and if it
is have some dependencies nougat will
download them for me to automatically
that's that's one strong point there are
some something like universal packages
from Microsoft which are very simple to
use but don't have this this
that's one way how to work with that
because from there I can download the
app file and I can see for example how
many times it was downloaded and so on
that's the artifacts going back to the
presentation I need to wait it's so slow
to load some time tips around the Yama
file because I hit some strange things
and I want to save you some time records
if expansion if you use the this kind of
things to write your variables they are
sometime recursively expanded at some
time not the difference is that if it's
part of process which is creating the
pipeline on the beginning it will not go
another round
it means if it is display name of your
task or something it will not be
recursively expanded if it is parameters
to some script it will be expanded in
run time because you can't update the
display name in run time it means it
will not be recursively expanded here
that's one thing another one if you get
this cryptic error on the beginning
that's the error occurred ronk number of
segments who knows what does mean yet
nobody knows that I find out that mostly
there is a problem in my Yama file that
I'm using the wrong version of some task
or the task was renamed for example and
now it's have different name and the
error just means you are using something
I don't know
that's all I don't know why there is no
error like I don't
understand I don't find this task or
there is no version like that ronk
number of segments oh another thing you
can skip CI if you want for example when
you are committing some changes and you
don't want to trigger CI see the
pipeline you can just put some of these
text to the commit message and when you
push to the server it will not trigger
that pipeline please be careful when
using that and be aware that everyone
see that commit message it means
everyone will know that you wanted to
skip the CI CD pipeline it means yeah
you can but it's documented that you
want it to do that but it's it's hidden
cam I think which can help you to work
with the pipeline's I think we don't
have time to talk about the sub modules
let's be that for example for some next
conference maybe okay now that's time
for questions I have of course some some
shirts here some microphone here I was
already some hands up okay three here I
see you first I think Thanks
maybe I don't call it how you organized
the pipeline's because there's a list
with all pipelines is there a
possibility to temporarily disable it in
this list and the next one is if I saw
it right you have your own repository
for the pipeline templates for the
pipeline time passes separate repository
the pipeline's itself as a definition
could be separated to folders if you
want to organize that if I understand
the question
and the pipeline I think there is no way
to disable temporary the pipeline
itself okay so and you have to really
remove them then create again for
example if you do want something to do
that with that but you can skip them
through aramid mess which skips a I back
because most of you if you if there is a
pipeline you want to use it yeah okay
yeah that's true you can override the
triggers in agile devops directly
it means you will overwrite what you
have in the Yama file and you can change
that in this way okay so you using to
build pipelines to deploy to send boxes
and so on why don't you used to release
pipeline because your tent and have to
release tracking the release pipelines
are part of the technology which was
there before the Yama pipeline's game
you can use the classic design things in
agile devops to create them and they are
connected mostly to the classic
pipelines for the build and I see them
as a technology which is going to fade
away and I'm focusing on on that because
in this way I can version the pipeline's
through the version called source code
management and I can keep track of what
was there and how to do that and I can
easily create them again when I create
new app in the classic release pipelines
I need to go there and manually copy
everything or or use some templates
there manually and so on of course the
Yama pipeline are missing some features
to track something but that's only
question of time when it will be
available because they are really new
they are there for
not not full year already but still
getting more and more features and I
think that's the only question of time
they're on at the end of the line if you
can throw that OH
yep and there is a shirt for you it's
okay I got it
so my first question is related to the
variables I saw that you saw you put the
variables in the young fire and is that
correct
because there is a place where to put
the variables even on Asia
second thing is every time you change
something at a young file if for example
I have some policies okay
even if I'm changing the build file the
CI we ran yeah of course the variable
could be defined in the variable groups
in Azure DevOps and variable groups
could use the azure vowed to save the
parameters it means if I have the group
variable inside Miami it will take the
value from the azure dev ops group
variable which is defined on Azure
DevOps and that could lead to the azure
world and I could take the parameter
famous the direction because actually I
don't want when I change a variable we
start built I am using the variable
groups for example for the password and
use a username and the application ID
which are used to publish something to
the customer environment that's our
defines not in the Yama file of course
and they are defined in these these
variable groups order in the actual
world
okay your templates wearing a different
repository but in the same project if
you have in a separated project it could
be you can define the connection in the
service connection in the azure DevOps
and it could then if you are defining
the resource you are just using the name
of this connection from the service
connection and it means it
could lead even four to github or
somewhere else and you can use the
templates from there okay I have to try
that because I'm using an extension to
the data and I don't want dependencies
the last one sorry about this
I lost my points I will ask you later
yeah okay and that was the last one last
t-shirt and I another question you
showed that you could create many
pipelines with a script but how long
would it take to to build all those apps
and what environment will you use to
build those apps so how long do you take
to to run those pipelines actually it
depends on the speed of our servers in
Breaux because I'm using agents running
on our server and right now of course
there is only one agent running it will
take so long to run that but the one
pipeline runs around 10 to 20 minutes
depends on how many stages you have but
most of the time is just creating the
container that's the biggest part
because I'm importing the test
applications from Microsoft and that's
it's making it longer because the
container is up and running maybe in 30
seconds but importing the test libraries
is taking another two minutes or
something like that and this is the most
time of the pipelines which it spends
somewhere okay some questions question
yep
you remember it was a simple question
it's the code available freely available
will be it will be definitely on github
I already have some templates available
on github
those are somehow fine tunes and they
will be ready for your fork
or whatever you need to do with them and
it will be available definitely I say
thank you
yeah I remember it sorry it is a it is
about the group tasks I know that you
can create group tasks yeah and a few
times during your presentation you were
saying I can just copy and paste this
yeah because I'm using Yammer and group
tasks I think they are for the old
technology of the classic pipelines so
we shouldn't use that I think no I'm not
sure that's true I never never looked
into that because I'm using templates I
was starting looking at that if I
understood well is the way to copy and
least on steps yeah and paste you create
yeah yeah but but the problem is there
are not source code managed managed you
can't commit different versions and so
on you have only one current version and
it is problem to update them because if
you update them even the old pipelines
had a problem sometimes with that
because they were included in time when
when you put them to the pipeline and
copied and were not nicely updated when
you update them centrally I will not
connect that technology with the amaura
I think okay okay then if that's all we
have just time to to finalize that
session thank you for attending that
enjoy a rest of the conference and safe
trip home as you will go and travel
thank you
