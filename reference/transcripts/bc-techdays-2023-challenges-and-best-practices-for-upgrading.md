# BC TechDays 2023 - Challenges and Best practices for upgrading to Business Central on Cloud

- **Source:** https://www.youtube.com/watch?v=BfaSeO8j4BA
- **Video ID:** BfaSeO8j4BA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 87m09s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good morning everyone
thank you all for being here first of
all so today we will cover the topic on
best practices and challenges for
upgrading to business Central on cloud
so from our experience doing good
upgrades in the past years we have
covered a lot of issues and managed to
uh
fix those and we will share with you
valuable insights and basically the
strategies which will help you navigate
the upgrade process
moving to the cloud is not easy task but
if you plan it accordingly and follow
your average strategy you can do it with
less issues facing during the upgrade
process
however
uh upgrade to business Central on cloud
brings us also some new functionalities
which new customers can benefit of so we
will share a lot of things now further
in presentation but before we start let
me introduce myself
so we can move to the presentation now
so I am Stefan schlotzich I am co-owner
of basility together with me it is
he is also co-owner as bisility
so our careers generally are pretty
similar so it's at the early beginning
of our careers we started with nav and
at early beginning when business Central
was announced and released we started
basically business Central investigating
and doing development at that point uh
really small amount of functionalities
have worked but after Time and Time
Microsoft managed to fix those issues
and bring also some of the Great
functionalities
so I will leave now
staged to tell us more what we will
cover in this session
okay
uh so in this session we'll call Main
aspects of the upgrade to the list the
latest version of the business Central
as you can see in the agenda we have
several topics why to move to the cloud
when is the right moment for the upgrade
we have for the argument reports there's
two ways one way is up to the bc14 for
any previous version and the second way
is from the bc14 to BC on cloud you'll
see what are the common that immigration
challenges and best practices during the
upgrade and for the Android
customizations extensions and code
related challenges that we faced and
that we will share with you
and for the last we will cover case
studies and lesson learned during the
upgrade process
okay so first thing first let's cover
some basic stuff at the beginning so why
even move to the cloud so first of all
like already mentioned Cloud brings us
some great functionalities some of those
we will mention now so first of all it
is enhanced security
business Central is
on client environment which has firewall
routines and Microsoft has already told
in previous session yesterday are
fighting really hard against hackers so
they're really giving some efforts to
keep the environment safe and your data
inside that environment safe not to leak
outside the environment
next thing would be the centralized
location because if we move everything
on cloud it would be much better to for
integration with other Microsoft apps
then we have regular automatic updates
so Microsoft releases continuously bug
fixes features and
security patches
which helps your company to benefit from
it and keeping your PC version up to
date
and now we have also the cost of
Maintenance when we move to the cloud we
will reduce our cost bit why because
on-prem infrastructure can be really
expensive all the data centers servers
and mini maintenance of those servers
can be really expensive on the cloud we
have of course some limitations which
we'll cover
later in the presentation but we will
have reduced cost and we'll have a
possibility for scalability
what does it mean so the environment can
scale up to our needs so if R needs of
business basically increase we can
basically increase our environment
resources or uh if the environment needs
decrease we can also decrease the
environment resources and on that way we
can also save the costs at some specific
time
and the flexibility also which Cloud
brings us so we can access the business
Central cloud from each device which has
internet access all around the globe
so now when we covered why you want to
move to the cloud let's cover when is
the right moment for the upgrade
so first of all let's ask or serve ask
ourselves some questions so first of all
is the version of your solution still
supported by Microsoft and that will
tell us more
let's take a look at the picture so
Microsoft introduced for the business
center from version 15 Modern Life Cycle
policy that policy includes uh 18 months
frame of the upgrades first six months
covers the features bags and Regulatory
fixes and after that we only have 12
months for the bugs and Regulatory fixes
so as you can see on the right side we
can see all the versions and until when
they are supported for the versions
before bc14 vc15 we have fixed lifecycle
policy and that that means that bc14
will be supported mainstream until
October 23 and final date until you will
be able to use it or there will be
additional change charges is October 25.
okay so there is a high chance that your
solution which you are planning to
upgrade is not supported by Microsoft so
there it is one more reason to upgrade
it
next next question would be do we have
demand for the new features
the new features which business Central
Cloud brought to us is enormous so uh
more more and more benefits are coming
and
Microsoft One Stop at this point
so next is is your solution lightly or
heavily customized and that that
question will basically tell us is now
the right moment to do the conversion
immediately or we need to do some
additional steps and then to proceed
with the upgrade and more about that
pneumonia will cover
okay let's see what Solutions can be
moved right now to the cloud if you
don't have customizations go for it
obsolete customizations so if you have
any solution that you want to obsolete
or already that feature is covered by
Microsoft to in the newest version or
you have light customizations let's see
what do we consider as light
customization
so light customization is also known as
additive changes so as you can see on
the slides changes in standard objects
but addition additive ones so Fields
page actions or any new functionality
that you add to the base application
that can be slightly easy to move to the
cloud but or custom new objects or any
your custom functionality that does not
have much impact on the standard one
Solutions uh that are also easy to
implement are the solutions that are
already set as compatible has web client
compatible we will see later on what the
client limitations are and that you have
all standard event Publishers available
for your customizations so
on another side we have heavy customized
Solutions and those Solutions have
destructive changes in the standard
objects so if you change or removed
primary key change some standard fields
or increase the length of the fields
removed standard code or play some other
parts of the code that we consider as a
destructive change
a lot of customizations or complicated
standard functionalities like posting
routines or something else where you
have a lot of customizations that's
sometimes harder to implement refactor
and to implement
or some any other complex situation so
that is look like in few steps if it is
heavy customized so you have the URL
solution you need to upgrade to BC
on-prem bc14 the latest version and from
there you can go to the BC SAS
when are you ready to move to the BC SAS
there are several things that we will
cover
you need to analyze our all standard
events publisher created maybe some of
them in the upgrade phase you requested
based on your needs are add-ons created
on app source so if your solution had
any add-ons
you should investigate is that add-on
already an app Source or when it will be
or what you will do with that add-on
that implementation is completed so
after we move to the bc14 we identify
all the places that needs to be
re-implemented and after all of that is
implemented we can move to the step to
the BC on SAS and any other possible
limitations that are removed
so
already on the upsource your add-on well
we have a lot of applications on the
upsource so maybe there is highly
possibility that your add-on is already
there
if you take a look at the these changes
among the versions We can see that the
growth of the anoms and the interfaces
and the events that
increases the flexibility and
impossibility to adapt to the new
solution and we can see in the next
slide in the next picture that the
number of events increases very much
during the years but maybe in some point
we'll reach the point that it will start
decreasing because there are a lot of
events that are not used or used very
few places so Microsoft may consider to
start removing them and maybe in some
points one of the other events that only
you use will be removed we'll see
okay let's let's continue with what is
the right moment for an upgrade
so let um the important thing in the
upgrade is also the database we need to
keep the Integrity of the data and
everything so one key factor is also the
size of the database so if it is bigger
than 80 gigabytes it will bring us
additional costs and complexity will
increase so also the time needed for the
upgrade to the cloud will increase even
though so you had a chance yesterday to
listen to the presentation where data
migration to the cloud is done and new
procedures are being made to basically
fast up on the process for migration to
the cloud
the important question there is do you
really want to keep all your historical
data what does it mean so
we could move to the cloud with clean
start so not to bring any data from the
old solution we can partially move just
some of the data like Master data
ledgers
or we can decide to move everything
do you want to keep your customization
and business processes
so from our experience in a lot of
projects a lot of solutions have a lot
of business processes which they don't
use regularly so those processes maybe
if they are really hard to implement or
they are using
um stuff which are not basically
compatible with the cloud those are
worth reconsidering to be left behind
and if there is really really a need to
develop those functions later on maybe
those will be included even in the base
app or system app or you will use more
modern techniques and helper code units
to accomplish that logic
add-ons also are key role in our hybrid
so all add-ons which we want basically
to use need to be either available on
appsource or the the add-on provider
needs to provide those add-ons spte
extension or pertinent extension so if
you don't have those add-ons we really
need to reconsider what will we do with
the upgrade so in those cases we cannot
just continue using those add-ons maybe
we'll reach to the partner with add-ons
and basically see what is the timeline
when when is the plan that those add-ons
will be on cloud
are you ready for the life and to life
and to live with web clients so from the
conversation with uh basically clients
we hear this a lot so most of the
clients tell us that they are not ready
basically for the web client uh they
still want to use latest BC on-prem
version which contains 30C because they
are used to it but web client brings us
also additional functionalities which
can improve our productivity so for
those clients I recommend highly to
basically train those customers and show
show them additional functionalities
which web plan brings
to Disney Central
let's move to the upgrade process so we
have
more complex Subway process and the edel
case scenario operate process
so more complexes of course if we are
moving from the classic or older
versions of nav
and then in that case we will upgrade
from earlier versions to Dynamics nav
2015.
only because we want to keep the data if
we decide that we will do the clean
start we don't need basically that
middle step we could skip that middle
step and migrate to bc14 which will of
course bring us some challenges doing
the obsolete functions and missing
procedures but that is a possibility
in this more complex scenario we'll have
to face two migrates to data migration
so firstly doing the upgrade from the
earlier version to nav 2015 doing the
that code upgrade and the data migration
average and afterwards
we need to take that converted uh code
in nav 2015 and converted to business
Central 14.
so we can keep the data after BC uh bc14
we can use intelligent Cloud toolkit
from Microsoft and connect to bc14 with
the cloud and on that way just move the
all the data to the cloud
that is a more complex way
of course if the solution is that old
the more easier way
an ideal scenario would be if the client
has already on-prem version of business
Central so that's from the BC Central 14
and in that case we don't need to double
the process we just need one basically
upgrade and we can move data migration
directly so without using any Microsoft
toolkits to migrate the data
so we can directly use intelligent cloud
and move the data to business Central
and Cloud
on this picture
we will check how customized your base
app is so again we will start from idle
scenario and that is when we have
unmodified base application
so in that case it's pretty
straightforward we can directly convert
our database to higher version and all
the code which is basically on top of
that old solution can be moved to
extension then we handle basically the
compilation errors if any or
compatibility issues but that is the
easy stuff
so the hard harder stuff is if the base
application is customized so it could be
held customized or just lightly
customized what name I already covered
and that
customization how much it is basically
affecting base up will determine how
much effort you will need basically to
re-implement all that stuff because all
that stuff from base application need to
go to extension
so
starting from customized based
application we need basically to convert
the code from CIO to Il
then to do refactoring in merge so these
options because we are speaking for
cloud environment these these three
options are no go
so we don't want any on-prem version
containing basically customized base
application maybe that will be scenario
for a short term so in case that you are
missing some of the events like name and
you already said
in that way in that point so you will
stop at customize based application and
everything what was possible you will
move to customer extension
system application is no go so you
cannot at all modify system application
and in that case then you can move on
on-prem and keep it there for some time
until all events are there but we are
nearly 12 20K events so really a lot of
events and with our discussion with
basically Microsoft you need basically
to rethink is it really basically
necessary to request on that place
exactly that place event so maybe there
is event
few lines up few lines down it requires
some replementation but
on that way we will not have too much
similar events and like now when I
already mentioned the similar events
will be most probably reviewed and we
will see for the future because uh first
first thing it was Target to move
everything to the cloud so no question
says but uh now it it started basically
to
Trend a bit down and we can review
basically those events and even when uh
the open source of base base app and
system app is coming we'll see some
events going off
if that is not the case
you have all events necessary for the
upgrade you can uplift it for the higher
version on that way you will have clean
base application
and clean system app and on top your
customer extension separately
in that case we will again upgrade to
the Microsoft base application
let's move to the average process
in order to successfully do the upgrade
process we need to follow some steps
first first step is preparation and
Analysis
it's marked red so it's really important
to prepare accordingly and do the proper
analysis before even starting the
average so it can really help you to the
the predict basically the issues which
are upcoming on in the library process
and basically think the strategy how to
resolve them we will cover that a bit
later
so next step is of course
merge to bc14 that's in case we are
going from the older versions of nav
we will be using uh standard Microsoft
tool txt tool
afterwards we'll prepare to conversion
to extension but what does it mean
so in that preparation we will check our
solution
if first of all we have some reports
which are highly customized and those
reports need need to be created as a
copy on our standard range
so we can when we do the extension
easily substitute those reports and use
them
on the extension
also we need to see if there was some
field expansion
in ways like description field
increasing its size so we need to cover
that but also to cover the crease of
field size if there is any so that
especially because that will break data
immigration uh immediately and you will
need to come back to this point again
next thing is data migration so at this
point we can start data migration to
bc14 we'll be using just Microsoft
toolkit officially available at
Microsoft documentation and afterwards
at some point when we are starting data
migration well we can do the conversion
to extension
so after conversion conversion to
extension we need also to fix some
things so when you do the conversion you
will have some compilation errors and
also unsupported changes compilation
errors so removed functions and obsolete
stuff maybe so we will cover that also
later more detailed
but those two are also tending to be
fixed so after those fixing you you can
complete basically conversion to
extension
after conversion to extension is
completed you install that app on the
cloud environment and you can complete
data migration to the Target on cloud
environment
when we are speaking basically of the
upgrade process
and until now we have spoken basically
of analysis so we need also to analyze
uh the issues which can occur in the
project
so most common issues are automations so
those are not supported on the cloud so
we need to see if we have any
automations
Cody units XML ports which clients used
basically in all all the environment to
search them in RTC directly
those won't be searchable anymore in web
client
custom code in standard objects of
course those need those are unsupported
changes and basically need
re-implementation
and benefit of basically on-prem
infrastructure is direct access to
server resources and basically file
manipulation so different way those are
pretty limited on the cloud and only can
be used as a stream options but director
access to the even local file system or
server resources is highly prohibited so
won't work at all
then fields we already mentioned this
but fields which needs to be extended
for the Target and you will most
probably occur on some obsolete
properties on pages tables like Thursday
table relation validity table relation
so
but that's not all
so we have also modification of data set
and layouts or standard reports uh
already mentioned that so we need to
Define
determine basically how much is
customized that report and decide if we
want to do report extension or we need
basically to create the copy and
substitute that report but when we are
substituting that report also keep in
mind that you will not basically get any
updates from the Microsoft so there was
any bug in the report which we was
copying you will transfer that bug also
to the Target
file operation or Dimension so now we
are only available to use stream
operations
change parameters in standard functions
are prohibited so those you won't be
able to implement on anyway but in case
we experience a lot of clients modifying
basically dimensions
so increasing of number of Dimensions
can be re-implemented so most of the
partners and clients just added
additional parameters and on that way
increase the standard logic but now we
can use the events and extend basically
Dimension number
accordingly so that's just one example
in which parameters modifications is
able to be re-implemented but most of
the stuff stuff will be basically
blocking
so you need to rethink what will be the
object action for those those
issues
standard Fields cannot be basically
parts of custom keys in table extension
so you cannot combine those two on the
cloud standard Eternal functions
those some of the procedures we which
you have been able to use before you
will be most probably limited and you
will face an issues
again those you can copy to your
coordinate and use but with functions
which have in scope on-prem those will
be more complex because they are using
functionality which is not supported at
Cloud still dot Nets maybe so those
needs to be
re-implemented so those logic has to go
away and use new technology
some of table relation changes are not
allowed what does it mean so we can only
add additional table relations and not
modify the only one existing so no
deletion or not modifying the existing
one but in addition to existing one we
can add
and of course dotnet variables not
supported we need to either use Azure
functions or re-implement with wrappers
already existing in base app and system
app
we have covered
only
analysis phase which is really important
to check what issues can occur now it is
preparation phase what you need
basically to prepare from the
prerequisites so you need basically to
prepare the whole database which you
want to migrate to clean it up and
decide what to merge so most probably
you will have multiple companies so even
copies of production environment test
companies and so on so those doesn't
really make sense to migrate so those
has to go away and you decide only to
migrate what is really needed you create
database backup you need to provide a
license for the all the environment and
then to mandatory fields which are
required for the cloud are object range
and solution ethics
so that depends whether your extension
will be pertinent extension or your
extension will be available on appsource
so if it is pertinent extension object
range can be 50K
and solution ethics can be PT pretty
easy but if you go to appsource so you
need to request a custom range from the
Microsoft by submitting one just one
Excel form for the object range and one
Excel form for solution ethics and that
can be handled pretty pretty fast in
less than five days so you need to do
that before converting to the cloud
because appsource validation then
pipeline will fail on those two
not add-ons are definitely thing to
remember also in the upgrade process
either we are speaking to data migration
or the basically code upgrade so what is
the plan for those add-ons
we need to decide what is the average
plan so we will have multiple actions so
we can
migrate the whole data of add-on
together with add-on business logic or
just move the data from add-on if we
want to use to keep just the data and
then we move just the tables from the
add-on
or we want to clean up the whole add-on
and then we don't have to worry about
the next thing coming
but if we plan to migrate some of the
data
or to get the clean start to Fed on we
need to get the base version of add-on
and get Target pte add-on or if it is
existing on appsource so you need to
have both both versions why base base
version it will it will really help you
to determine what is basically
customization and what is the add-on
customization so when you are doing the
merge an average process to business
business Central 14 and the target
version of course if it is not existing
you will not be able to use any more
data add-on
and important stuff is data immigration
tools so if that add-on provider has
provided you data migration tools so you
will have to have basically data
migration tools on either way so if the
add-on provider didn't provide it you
you will have to spend some effort and
create the mapping and your data
migration tools by yourself
if you still want to use that add-on but
the easier way and I think most of the
add-ons have data migration tools so you
need to get get in contact with that
add-on provider and get those migration
tools
okay we finished analysis files and now
we are moving to the code upgrade steps
so first what you need to do is Stephen
mention is to upgrade the code to the
bc14 it's mostly by the merge after we
are on the BC 14 we should fill all the
missing and encaptions and properties we
should add the prefix as Stefan
mentioned either it is requested from
Microsoft or you just had pde but keep
in mind that maximum is 30 characters
and you should pay more attention to it
for the fields that we have more than 30
characters
uh usage category accessible permission
application area all of that can be
easily moved by using the Microsoft tool
translation many suit objects to for
search by using that tool it will fill
uh and basically replicates your menu
suit and all properties will be filled
after and after you do the conversion
and you need to review all the field
expansion based on the standard Finland
change so if standard change some Fields
you need to during the merge increase
the length for those fields or decrease
whatever happened that is very important
for the data immigration in case
anything is different in the Shema SEMA
that can break the average of data
migration
after we are successfully merge
everything and resolve the ratios there
we are commenting our CL code to the IL
and using again Microsoft tool takes
that to IR
then we have a little bit more work to
do after we do the commercial
we need to move our customized code to
the extensions either by subscribing to
the standard or customer and Publishers
customer and Publishers are the long way
that Stefan mentioned and think of the
implementation how how you can avoid
them try to try to find a better way to
implement Your solution maybe something
is not needed anymore you just need to
pay more attention and of course you
should always use and even the tool will
create multiple table extensions page
extension report extension but that will
also be a lot of things that are
completion errors or unsupported
features later on we'll see what are the
most common and after everything is done
just we'll create a translation files in
order to have everything translatable
so what does required implementation
usually so limit web client limitations
automations I also already mentioned and
net variables Integrations with external
web services those are handled
differently what we do the communication
on cloud
file system limitation already mentioned
and other technological constraints
which means accessing to system tables
those needs to be re-implemented or
implemented or the harder way
modification of standard Keys variables
and table relations
some of standard Fields cannot be used
basically as custom Fields some of
standard object properties are not
supported and some of UI features are
not supported by white web client
let's move now to UCI so interesting
part so if you want to go to the cloud
you need to keep keep in mind universal
code initiative otherwise yeah Microsoft
introduced already a fees for it not
basically implementing the UCI so this
is Microsoft first Cloud first strategy
what does it mean only extension and all
base up modification and from this
quarter this year
there are already fees if you are not
basically compiled with the UCI
how let's go through once again so that
means only extension no base app
modification and Target on cloud
if you still want to use UCI you will
have to pay fee which will cover the
next slide but typical issues which
prevent basically UCI compilence will be
file operations.net print operations
direct access to SQL or just missing
events for implementation so maybe we
are just waiting for that event that's
okay and that will take shorter time but
if it is some of the other issues above
you need to think about re-implementing
those
what are the fees basically for using it
this year so these are the fees and from
the 2026 we will see what will be the
cost if you don't follow the UCI anymore
how does it look now when you want to
purchase basically the licenses and you
are not compliant with usci so you you
will have to buy also that implemented
code is not Cloud optimized and
implemented code is not in the extension
and in the order we can see basically
for the basically two licenses of
business Central premium we also have a
two fees one for code not being Cloud
optimized and one for code not in the
extension
so yeah you can prevent a bit a little
bit those fees and Microsoft has also
partner programs which you can basically
participate and you will have basically
a discount on those those values
technical tasks which you need to cover
for web client redesign so we will just
go through this this list which should
be
reviewed when we are going to the web
client and that's grid layout and its
properties for rows columns and row span
those are not supported anymore on cloud
needs to be reviewed this design can be
re-implemented on another way most
probably it can so we then didn't face
any issues with re-implement
re-implementation not to look on same
way on the cloud review on lookup
trigger for the fields which are not
editable
reviewing the Triggers on close page and
on query close page
we'll cover that separately a bit later
reviewing a
basically report run without basically a
request
page.net with property run on client
those of course cannot be re-implemented
at all and needs to be basically
replaced with standard functionality
and reviewing again file functionality
because that is really really common to
see in all solutions
data migration challenges so we can
focus until now on other processes now
it's time for data migration so it is
really important like I said to ensure
all the data is moved to the cloud
but in order to do that we also
mentioned the cleaning of database we
maybe don't need all the data so we need
also to analyze the database
if the database is specific to some
region like German Finland Norway so
using the special characters you will
have to pay attention to collation and
basically region settings so your
machine which you are doing the upgrade
and you need again
like we did for the upgrade process you
need to create our bus data strategy for
data migration also
some of the SAS limitations which are
existing now are no direct access for
Azure SQL so
all data checking modification of single
records directly on database or writing
custom queries bets and everything that
is no go anymore so manual backup is
also not possible and you can only get
emergency restore through Microsoft
support
common things to remember before
starting even the data migration so all
debugger breakpoints which you have in
your solution is to be removed
usually table reservation entry is only
with one
one primary key so you need to get also
let knowledge plot no as a secondary key
empty records in item category product
group table will also make you an issue
when you are starting data immigration
and those are just some of the issues
which you can face while doing the data
migration most common ones
but uh yeah it pretty much depends uh
from which version to which version you
are doing the data migration so uh if we
are if you are doing the data migration
from classic to nav or nav to business
Central 14 you would use Microsoft data
migration toolkits all available
or if you are doing basically date
migration from bc14 to Cloud you will
use as mentioned before intelligent
cloud data migration tool
again I put it uh add-on date
immigration tools not the thing to to
forget so especially if you use some
add-ons which contains your data your
documents which you are uploading to
them so that's most probably that client
wants to keep that
one thing goes to remember system data
won't be migrated either using
intelligent Cloud toolkit or standard
Microsoft toolkit so users
personalizations saved use and record
links cannot be basically migrate but
let's focus on the record links so
you cannot use standard Microsoft tools
but there is a way still so
with record links challenge so record
links for those maybe uh who don't know
what they are used so all the notes from
the old environment won't be transferred
to the Target environment and in those
case you can really easily Implement
those data migration so either you
create I just put one way of migrating
those data but there is plenty of it so
point is just exporting and importing
hint on the new Cloud the new Cloud
environment so one way is creating XML
port
exporting on the old environment then
creating same XML port on the cloud
environment and doing the import you
don't need basically to use XML Port you
can use basically also XML creation code
unit
on the target to parse that XML so
really really plenty of ways but in this
way you can get all the notes from the
old environment to the new
that's a related all to date let's see
about the code after we convert our
solution to the IL we would need to do
little cleanup and there is pretty
handful extension that you can get I'm
sure most of you are already using but
not sure about this command so code
cleanup actions that can do a lot of
things so the after you after the
conversion
files are not formatted or anything so
instead of going to every file and doing
the save or something like that you can
just Define the set of actions that you
want to run run and you can do it for
the whole project so either it is form a
document add missing parent is sort
variables or form a document whatever
you want so yeah for the Phantoms types
okay yeah that is about that extension
another extension that is pretty new not
sure how much of you heard of it it is
all packages and we have I hope you can
see it
that extension allows you to download
any package version and that can be very
useful to compare against different BC
versions and how your solution works so
yeah that is pretty new and also works
only on the latest Visual Studio
uh Visual Studio code version so as you
can see in few moments we already got
symbols we don't need any environment to
download those
some things that usually needs to be
implemented are listed in the list so
how to implement all the XML things that
now have different types
streams encoding HTTP documents XML down
management or even record templop moved
to the code unit template all of this we
provided as a PDF file that you can scan
and you can download and many things
from there you will find easy way to
implement it
I will give you few moments if you want
to scan it but you'll always be
available also after the session
I hope that you will be able to scan it
and that files look something like this
so we have old how it was implemented
and in new syntax is how you can how you
can try how what how you can Implement
that that
that line of code and for that is
another example for the templops and for
many more that he mentioned
so ref the rest of those you can find
basically in the document provided which
you can download but I already mentioned
a few times uh basically Implement that
you cannot use any more extension to
system tables so you can still or
Implement those so if you have
some customization like this so adding a
few fields to just a user table you can
still create a
you will get an error when converting of
course but you can create a mapping
table and basically re-implement that
functionality on that way this is just
one of the suggestions so there are
always multiple multiple ways but it's
still still possible to do
uh we also mentioned before on close
page and on query closed page triggers
so when running those triggers now on
cloud with the Run command uh the
trigger on query closed page will always
trigger so when we had an old
environment
just run command it won't it didn't
trigger basically on query close page so
what you need to do is basically
analyze the solution after the
conversion and basically search for all
on query closed pages and review if
those are containing any piece of code
which will basically be triggered
not intentionally so definitely one
thing to pay attention to
and now it's time for a little exercise
so we have only one question for you
please if you can grab your phones and
we would have also one more QR code to
scan
I hope that you are connected to
wireless and have internet connection so
this is the clear code that you can scan
I hope that it can be scanned
I make it big enough
I will give few more moments and move to
next slide it will also be available on
the next slide
and I hope this will work yeah
okay we already have some answers so
this is live
let's see
about the results how you are doing your
merge
if you cannot join by your code you can
always join the
link with the code
okay we have a lot of answers and as I
can see most of most of you are using
3mm mirror that's good but for you that
are using two-way merge let's see and
that for ones that never did it it's
totally fine
okay I think we have pretty good result
no need to wait anymore
so what do you think this is to emerge
we have on left side source and on the
right side Target this is some code
piece of code in the standard so there
are no comments maybe someone forgot it
maybe it's custom change
or it is standard change
based on these two average view we
cannot tell it let's take a look at
freeway merge
on the right side we have our customized
application in the middle we have base
application without any of our
customizations and on the far left that
is our Target version that is the newest
bc22 how it looks like and we can see
between these two versions when we
compare the base and are customized
based we can see that this line is
additionally added and we are sure that
this is the customization or add-on
basically if we had an add-ons and what
we are doing about them but we can now
see that there is a conflict between
these versions because Microsoft added
one line and we also added one line and
down there we have conflict and the
automatic performer does not know what
to do we need to tell him what do we
want to keep if it is for example add-on
or something else we can exclude it but
in this case that is our custom change
and developer forgot to put a comment so
we can choose both and also add for
custom comment in editor down there we
can add custom comment in the future so
we know that that is custom change and
we don't end up in the same situation
again
so let's let's see uh what to do after
the upgrade so let's imagine you you
have successfully done basically the
data migration part you have done in the
code upward part so what now so uh first
thing first we need several things to to
check uh one of those things would be
the page layout so we need to have the
whole solution also available
so we need to compare basically all
solution layout with the new solution
layout
in those scenarios layout could be a bit
different of course to add standard
modifications of the fields of removal
Fields moving the fields creating
additional groups so those are those are
really things to reconsider basically
but again the
page layout should be as similar as
possible
same as report layout so
we mentioned two ways so if we was doing
the copy we will still we could still
experience some of the issues so first
issue can be maybe to lay out related
but we can also get the issue regarding
basically the data inside the report and
that would indicate us that we didn't do
a data migration properly so maybe some
of the data is missing in the report
maybe in the report some of the special
characters don't show up
correctly so all of those things we we
can basically check in the Target
version of report but of course the best
way is to print both the reports and
compare it
if they are one-on-one that's basically
the target
and the goal uh then we do some data
comparison so to check if data migration
is done successfully all the data which
was existing should be existing now on
the target except again of the system
tables then basic Master data input test
should be done what does that mean so
for that kind of tests
you should basically test Master data in
which ways so creation for example of
Master data then in order to see if
there's any
error by creation uh what what was the
results basically on the old environment
did on the old environment
he had any basically trigger on insert
or event which would uh basically fire
upon insertion of that Master data or
something like that but after insertion
you will also fill some fields of course
and check before the validation works
properly so in that case also you need
both environments running to compare the
behavior so if you are expecting an
error from the old environments and not
getting it on the target so that's again
the issue which needs to be developed
and the result
and of course
deletion of those Masters data
after we've completed that that phase we
can proceed to basic posting routines
testing so most of the clients basically
modify any of the posting routines so
uh now on the cloud we have even the new
posting routine when that is enabled so
I'm pretty sure that 95 of all solutions
will fail so
uh each partner should expect to
re-implement their posting routine so
it could stay like this for now but in
future management if you want to try out
the new feature you can still enable new
posting routine so in that case when the
new posting routine is basically turned
on you will
use totally different events than
existing previously so your codes won't
be triggered at all so
that's one thing to expect so if you
want to use all the new stuff from
Microsoft on the new features and you
enable everything through
feature management then
you will most probably get an errors
so sales purchase those other two
mandatory things to recheck and
automation tests now so that's that's
really important so
the guesses that you have automated
tests and if you have those automated
tests those will help you a lot in which
way so you can run on both environments
and determine easily if your core
functionalities are working
uh that's CDL scenario but if you don't
have any automation tests
again best way would be to create some
automated tests for your core solution
in order to test all the changes because
even after conversion to extension and
everything when you think you are done
you are not still done and again at some
point you will be most probably also
required to create automation tests so
it is really nice thing to have
yep
so
let's move now to case studies and
lesson learned so we will cover now all
those issues which we had before in
previous slides
so what has occurring the most what was
the issues in regards even to data
migration compilation errors most common
warnings and so on
so
for the data migration
I'll we just mentioned a few of those so
any company names there are a lot of
companies which use their symbol inside
those names needs to be cleaned up
otherwise you get an error like you will
get for the rest of this points so
decrease of field length it also happens
not not that often like you get for for
the fields which needs to be basically
extended but it happens still navigation
already mentioned that you will have
special characters for some regions and
do you need you need basically to adjust
Collision in nav and basically the
region settings in your environment
where you are doing basically the
upgrade and where you are doing the data
migration
and also one of the common things is
empty product group and item category
in those case we need just to remove
that record
and when we visualize those things
of course there is really big section
which represents other issues it is
pretty big list of issues which can
occur during the data migration and each
data migration
has its own issues
not the ones these ones repeat but you
will have the unique ones
maybe you will have additional
challenges resolving them but you will
definitely have some unique ones
for the smaller solution of course you
will you can do the data migration
without even any issues but in most
cases you get
so except other things so the company
name is really huge we just analyzed
based on the number of projects
summarized everything so
it could also mean that a few few of the
solutions had really big amounts of
companies like hundreds of companies we
had also those cases and at 100.
companies used the dash inside it so it
can be also related to a few of the
solutions not basically generally but
yeah this is the generally summary of a
really big amount of projects so we have
a field length like we mentioned nav
collation empty data and other
let's move to the compilation errors so
of course you will get for sure the
scope on-prem so a lot of procedures
which you have been using before on your
old environment
won't be available
on the cloud so those those needs to be
re-implemented so those are using either
like as a dotnet so Microsoft will also
re-implement those with the new
procedures new code units and everything
but you cannot use anymore those those
functionalities
uh language records 10 block record
those are basically similar ones but
needs to be re-implemented with uh code
unit
and you will face also again more and
more action control fields which are not
for found in the target
uh why that happens basically there was
a reason to obsolete it so those were
obsoleted at one point and
after some while now we have onsas a lot
of actions which existed before but
doesn't exist now
and file management issues those are not
limited to what was previously said but
are mentioning that that uh
direct access to a file system for
example or manipulation differently with
files than with streams
so we have also visualization of those
ones so most of the things are on-prem
so for those on-prem things
or implementation is needed so expect
when you basically operate to the cloud
that you will have some of the time
needed for our implementation
then we have not founded the target the
absolute things which we mentioned so
also again those need to be removed and
if those are really crucial for your
business processes you will need to
check if you will add it in your
solution or there was a reason for its
removal at first place
so then templop code unit and language
code unit so records to code unit it's a
really simple simple re-implementation
so want to basically spend too much time
on those those two but uh but still
um
there is a lot of occurrences in each
project so that is really one of the
things which will occur for sure
file management six percent but also
depending on the solution so also we
have the solutions which which were just
doing the file management so in your in
your case it could be 100
but yeah this is just the average and we
have also the other other stuff
which could occur of course
okay we covered completion issues and
now let's move to the unsupported
features most common supported feature
is the property modification you can add
property notifications either to tables
or Pages or other places and let's see
what are the most used and not
extensible properties so you will see in
the list that there are a lot of
properties that cannot be used in
extensions so some of them are Auto
split key plant numbers you cannot
change card page ID you cannot change
the behavior on the page is it delayed
the inserted the delete allowed insert
allowed you can change the mixman value
on the fields not blank multiple line
you cannot run object run object link
those are all the things that you cannot
change save value sub page link or sub
page view
usage category and so on and so on there
are many more properties that are not
extendable
other things than properties you cannot
modify standard triggers so insert
rename the read modify for them in most
cases we have our implementation we have
the events that we can use but there are
a lot of situations that there are
radical change in those triggers that
needs to be rethinked some of them also
have is handle parameter in the event
that you can skip that code and place
yours but there are also the situations
where it is not possible and you need to
find another way to do it so we are
going to the cloud and any modifications
that are destructive or changes in the
Visa are not allowed
code modifications on validated triggers
so validate triggers
any changes there
if there is no event you are not you you
cannot do it you can subscribe on before
or not or after but all the changes in
valid triggers or standard procedures
very common is that we see that Partners
insert parameters into standard
procedures so extend the procedure with
the parameter or a return type or things
like that nothing of that is allowed and
very very use the common is key removal
or extent do you have some possibilities
to extend some keys but we cannot we can
only extend the keys from the same
application so if you want to extend the
standard key we can only use standard
Fields if we want to create a new key we
can only use a standard fields or we can
use extension Fields but we cannot
combine those two and if we take a look
at the graphical view of those
most of them are other okay we cannot
list them all but property modifications
very big part standard procedures
and others in smaller amount but yeah
trigger modifications holiday trigger
parameters and standard procedures yeah
similar to those but yeah a lot of
things that are changed
other and next to the unsupported
features are common warnings
so most common warning is marked for
removal so that is the thing that is
smart for removal or maybe something is
already removed and you cannot use that
and you need to find implementation
you can use if it is smart for removal
for some time but after that time after
that version that they mentioned it will
not be able for using
sort sorting should be part of the sort
field should be part of the keys for the
table in most of the cases that that
code cap reports that warning in some
cases it makes sense in some other not
there are situations even if you add
that they will still keep the reported
so maybe in that cases you can use
pragma to ignore that warning or to
leave it with it
ah implicit conversion options to anoms
and other way around that is very common
one and that is the place where a lot of
mistakes can be made why that so if you
previously extend the start done option
and that is now in them you will create
an extension right
if that genome extension it will have
your ID range either it is 50k or your
Siberian sermon on something
then you will have places in standard
where enum is not uh when their option
is not converted to the enum that place
is then enum is assigned either to
option or other way around and for the
options that you extended for example if
you are still in the customization phase
of the base up not yet on the cloud IDs
will not match and you will have the
situation that you are signing ID of the
Anon
that we are assigning the enum the value
to the option ID value that doesn't
exist because inum ID is much higher
on the reports usually we have create
totals page number and other things that
are usually reported as a warning in
most cases those are can just be deleted
not much work there to do
promoted properties for actions only
spots is very also common one and let's
see the graphical View
so we have most of them are marked for
removal and for those we need to
implement implicit conversion I
mentioned pay more attention to it
invest some time to resolve it to find
the best way to do it create totals on
pages the numbers on the reports very
common because there are a lot of
flippers that are usually changed and
copied about Stefan already mentioned
that those should be paid attention
because the whole library that you will
get later and so on and so on then we
have others like promote list Parts in
smaller amounts sorting fields and
others
so yeah uh
when you do all of that stuff so we
covered most of it but uh what are the
things to do when you basically complete
everything does your work uh end there
so after the conversion the job is not
not of course done uh
development basically brings us a lot of
functionalities we which we can use so
code re-implementation is a really big
part of it so converted code is not
either or solution it is uh just the
fastest way to get to extension and to
have a starting point for the future of
your app you can do
developments with your app but one thing
not to forget when you are going to
appsource is that you can Mark a lot of
your procedures and objects as internal
on that way when you decide later on to
either delete or change parameters or if
your procedure so to do breaking change
you will not have to face basically that
issue in validation pipeline of the app
source so that's really smart option
before you are publishing to appsource
so of course the code
updates so
keep all the new guidelines
from Al all the regions through
implementation so maybe you're also
solution can be re-implemented
differently
so also we mentioned the events so
events have been used on first line
second line so maybe there is a way to
better integrate your changes into base
app customization and uh again so uh
parallel to this presentation uh vehicle
and Waldo are presenting interfaces so
uh the great way also to re-implement a
lot of standard functionalities and to
have all the customization then
extendable later on in the cloud and to
bring new functionality are interfaces
if you have not used them we highly
recommend to start using them basically
and to explore the benefits how you can
basically dynamically
modify your solution
uh yep uh we will leave now this time uh
for the questions uh not uh not to more
and more dig deeper because the topic is
very large we wanted to end the end on
some place not to be continued further
but yeah we are still open for the
questions we have also uh here a few
shirts uh for those who ask questions
and yeah
just a second so
just to see which which one to use
this one is working
that also okay
okay in conversion to apps there is a
standard pattern you can suggest
how to spare the new customization in
one app to app and or for um the
customer you decide
um what do you think at start Do you
have a
okay
um
now we have
a problem how to separate the the
customization okay yep okay uh have some
tips
or to design the the configuration the
final configuration what would be the
way how to resolve the limitations of
basically moving to extension
the standard tips to choose if uh one
one uh one a vertical app is the
solution or a family of either the
solution to
uh to go there is some tips or no to
create multiple apps or to create one
right the question is yeah an app or a
family so that's basically basically the
decision which each partner needs to be
uh aware of because uh you can create
multiple solutions that will also fast
up your development environment one big
gap also slows down you can use
Microsoft principle of creating apps so
having one big app inside its multiple
apps but when you're doing it internally
you will compile one by one extension
but when you are publishing to appsource
you will publish the main extension and
push everything but if you are planning
to create multiple apps you need to have
in mind also CI CDs issues and efforts
to create basically cicds with
dependence is and also publishing on
appsource also is more difficult
maintenance also brings also more
analysis of course the difference from
one only app in a data immigration
process or family
um
when you done only one uh it should
therefore less from a family so you will
also you will get basically the errors
uh that you are missing some some tables
on on basically on the target extension
or uh if you basically publish at the
same time and do that at that time data
immigration you will have again all the
tables at the Target so it won't be any
problem so uh the thing is when do you
want to publish those apps so if you are
planning to publish those apps one by
one so you are finishing one extension
let's move the data to it and let's
publish it then you will have to force
data migration because you will have uh
structural data changes and it will
occur errors will require but if you
finish all the apps which you are
planning to do and put it on an
environment and then trigger the
standard Microsoft data immigration
tools there won't be any issues
thank you no problem
thank you
um
we can use bc14 as a stepstone to move
to the to migrate to the cloud how long
will they still be supported
be supporting bc14 will be supported the
it's under fixed lifecycle policy and
the end date after it is supported is
October 25 but after October 23 there
will be maybe some additional charges
more of the more about that you will see
on the Microsoft website about fixed
lifecycle policy what is supported and
what's not and you always need to
upgrade your to the latest your version
of that to follow all the security
patches and so on but you can still use
it up till some point but maybe in the
future there will be some additional
charges the point with uh maintenance
and supported version is that at some
point you will not get basically the
security patches bug fixes and
everything so you can still request for
Microsoft to edit but those are really
low priority and not to expect to be
done soon or maybe not not to expect to
be done at all so that's the main and
crucial thing to remember
is that all thank you
you can throw it
so coming back to the three-way merch
thing so when I'm starting like in Old
nav version
and I want to merge and compare with my
changes do you recommend that as a base
version and I have some yeah old other
customer
extensions customizations then should I
get like for the middle Chronos database
with
the other customization okay yeah we
understand so the question is uh what
what should be used for the base when we
are doing two-way merge okay base for
the two-way merge is the base of same
version and same CO as our custom as
your custom version so it should be same
version and same CU and basically if you
have add-ons or not depending what you
will do with them you should also put
add-ons or you will should already have
received add-ons from your partner in
that base version of that you're needed
it so that I think that answers your
question so base version is the same
version as your custom version just
without any customizations
thank you in that way you will be sure
what is customization and what is the
standard that is the main point of those
two views and also you benefit if you
have any add-ons also so you can put in
uh First Column base then you can put
the base with add-ons and then base with
add-ons and customization and so in
multiple steps yep so on that way way
you will split each txt to have
different different ones and uh freeway
merge will basically be able to
recognize what is the customization
exactly so that is the most common case
when you don't have any documentation
what has been done and happens to all
solutions let's drop some Fields here
there some procedure here there so at
the end you'll get a mess but you can
still get out of it
yeah
um in case of the preparation for the
migration has had a large databases or
database
above 80 gb
um is it an experience from your
projects or is there where you will come
from Microsoft
sorry 80 gigabytes is value you are
asking about that yeah so 80 gigabytes
is the default that you get on the BC
SAS and that is the value that we
compare you can add additional gigabytes
that are by the users that you buy and
so on but the 80 gigabytes is starting
point and that's why you need to decide
uh how big is your solution is it much
more or a little bit more and to analyze
the data where where are the which
tables are most of the keyboard choose
and so on that is the point yeah okay
can be data reduced in some tables doing
yeah all the data if you can drop some
data yeah and of course if you are using
basically a lot of images those are
basically killing the database much
quicker and quicker the its size so you
can like Microsoft presented so in the
system app you has you have now a blob
connector uh so you can drop them online
and then of that that way it's much
cheaper to pay uh Azure blob storage
than to basically pay additional storage
to have in your environment okay
do we have some more pressure
yeah I have questions regarding strategy
like let's say I have bc14 now we fixed
can you put a little bit because lots of
I have busy with a lot of modification
and we wanted to go to the cloud and
what should we do should we first remove
all those uh extends go to extension
model and have complete bc14 and with
this go to the cloud or should we first
come back to pc22 on-prem and with this
go to the cloud
um that's that's basically one of our
first slides so you have to make make
some analysis of your solution uh first
of all maybe just some of the parts are
not implementable and then you go to the
cloud but uh if you are using too much
uh features which are not supported on
the cloud uh too much customization of
base base app not existing events so and
yeah you really need that customization
there is uh no another event to
implement it similarly then uh first
first thing is to go to on-prem of
course but yeah and to request basically
the event but like mentioned before
event also requesting won't be like
one-on-one until it was like like this
point so those all requested events
upward so this is just from the
conversations and so on so those
requested events in future will be
reviewed much carefully and questions
will be asked for maybe why do you
really need it here and not there why
can you can you use basically event
which is just two lines above so
uh yep uh if you really think that the
event is needed at that point for your
implementation and that is that other
partners can benefit from it then it is
way to go and go to on-prem request
basically Publishers which are missing
and then basically go to cloud or if it
is not basically the crucial
functionality you can go to the cloud
make to-do's basically for your missing
functionality if it is just some of the
functionality and you can live without
it
then after the events are added you can
just bring it back that's that's on the
same way but it really depends from
really lots of factors and the whole
analysis of uh also database and objects
needs to be reconsidered and yeah of
course database decisions should be made
so
there is no unique basic step to tell
really depends from your goals and the
company goes how they want to go with
that strategy
thank you good
take the box back do you hear any more
questions
I don't see any hands so okay thank you
very much for your time and for
listening yesterday
I hope that we answered some of your
questions thank you
thank
