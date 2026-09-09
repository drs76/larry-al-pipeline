# BC TechDays 2022 - Cloud Migration

- **Source:** https://www.youtube.com/watch?v=939lUywd-q4
- **Video ID:** 939lUywd-q4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 46m04s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

is Nicola and I'm an Al developer and
one of the areas that I'm working on is
the cloud migration the next area that
I'm also working on is the upgrade so
I'll be covering these parts today today
with me I have Roman
yes hello my name is romance Alber I'm
the engineering manager of the control
plane team we are part of the business
Central platform and are responsible for
the services that manage business
Central environments in the cloud for
administration and among many other
things also for cloud migration and
that's why we're here today
yeah hello my name is Julia and I'm a
developer in business Central and before
I was a developer in a vision
so I've worked in many areas and today I
am responsible for cloud migration
replication engine
all right thank you
so we have prepared a lot of content in
front of you we are going to start with
the journey overview so I'm going to
describe to you how does the cloud
migration Journey looks influent so you
get an overview of all of the components
that are in play
then I'm going to show you all the steps
that you need to do to prepare for the
cloud migration Journey so all the
things that you should do before you
start replicating data into SAS
then Roman is going to do the demo how
you can set up the cloud migration and
he's also going to go deep into the
technical details and Julia is going to
describe to you how is the tool actually
moving the data to the SAS database
during this part they're also going to
cover most commonly occurring errors
they're also going to show you how you
can fix them so you get a more smoother
Cloud migration trend
we are going to end with upgrade so I'm
going to demo to you the improvements
that we did to the cloud migration from
previous versions so we have implemented
some nice functionality there and we
have also improved the on-prem upgrade
so we have few changes that I believe
that you really like at the end
we will not have time to go into details
for the API so I'll just briefly mention
it at the end
so
if we are to start the cloud migration
Journey the first stop would be actually
the version 14.
and this is a rather important version
because this is the last version which
is supporting CR
as you probably remember
in version 15 we have stopped the
support for CR so we could develop Al in
an easier way and to give you a nice
features that we have implemented over
time
when we have discontinued to the 14th
the promise was that you need to upgrade
to the other side because the grass is
greener on the other end with version
15. and if you have been here three
years ago on the BC Tech days in 2019
you may remember this slide
so this was the story back then today
the journey is looking like this and as
you can see we have been busy we have
released seven new six new releases
and we have added a lot of functionality
so you can see that each release is
bigger than the previous release
the good news as well is that the grass
is still green and let's take a look how
does the average Journey look like
the first step is to upgrade to 14 if
you're coming from the previous version
then you can do a single step upgrades
to do version 21 skipping all of the
versions in between
and if this is what the customer wants
you can go live on 21. or you can
replicate the data to SAS and go live in
South bush
this spot is bringing benefits because
you're able to get more control in the
on-prem operate and replication is
usually a safer step
for last step than running the operating
right
but the problem with this part is that
you need to write the average scripts
and to do the on-prem upgrade
alternative part is that you can go to
14. and then you can replicate the data
to Source you can go straight to the
latest version of the cloud and then we
will run the object in the source
version
this part is better because you don't
need to do the on-prem upgrade and the
second benefits that you're getting is
that the upgrade and Cloud replication
is going to be a bit more forgiving when
it comes to Breaking changes
and I will cover it a little bit later
now before we go forward this picture is
showing one important thing which is
also one of the questions that we are
often getting from you and that question
is for how long are we going to support
the one step upgrade path from 14th and
direct Cloud migration from 14.
and as you can see it's a very important
build for us because it is serving as a
bridge from all of the customers that
are on CR to the latest version so the
answer to this one is we are going to
support this part as long as we
technically can because we want to make
you as efficient when you're running the
operator
now there are two technical challenges
which are also visible from the picture
as you can see the longer you wait the
longer time it's going to take to do the
upgrade because with each functionality
that we add we are also unfortunately
adding time to operate
we are aware of this problem and we did
few improvements in this release to
address this problem to make the upgrade
actually take shorter time
the second problem is that the software
on the previous versions before 14 is
getting out of support and in today's
world it's presenting a huge security
risk to run your business on a software
that is not officially supported anymore
and this is actually one of the main
drivers for the cloud migration that we
have also heard from you guys is that
the customer wants to go into SAS so
they do not need to buy the new licenses
for SQL Server windows and other
products
so this is one of the reasons to
prioritize the cloud migration to source
for a few interesting statistical
details in the last 30 days we had 564
unique customers migrating and we can
see that this number in the last few
months was between 500 and 600.
and as you can see the version is 20 and
versions 14 are the most popular ones
so approximately one third of the
customers is coming from the version 14.
and we are of course supporting all of
the versions between the version 14 all
the way up to the version 20.
and we planned to do this as long as we
can
now this was the overview so I hope that
you have understood which steps do we
need to take and now we are going to go
into specifics
and we are going to start with step
number one and that's upgrading 214.
oops ah it works this right so as part
of the upgrading to 14 there are two
things that you should do
first one is to align the table
definitions and to clean up the date
aligning the table definitions this
could sound like a big task but in
reality it's relatively simple because
out of all of the properties that we
could have on the table objects
these properties are must for both Cloud
migration and for operate so you must
align primary Keys both in the source
and the target database
and you need to align the field names
and data types if you don't do this the
cloud moderation and upgrade is going to
fail
now following things Cloud migration is
able to handle but if you're running the
on-prem upgrade you're going to be
affected
so
if you have different names
if you need to prefix you the table name
with the three letter prefix of suffix
you can use table mapping and Roman and
Julia will show how you can do that
now this is a biggest problem that we
have heard from you because almost all
of the customers have added additional
fields to Microsoft don't tables
and if you have not refactored them in a
good way the cloud migration is going to
ignore these builds currently so we will
replicate the Full Table ignoring the
fields that you have added to the main
table
if you're running operate upgrade is
going to fail now the good news is that
we understand it's a big problem and we
have a prototype that we are currently
testing so we believe that during the
cloud migration we'll be able to split
the main table with table extensions
into main table and table extension
without the need for you to write any
code and if we are successful we are
going to announce it so just keep your
eyes open there might be an announcement
coming in few weeks
and as the last things is the table IDs
and secondary Keys Cloud migration does
not care about this at all
they are only important for the on-prem
update so if you are Cloud migrating
from 14 on an earlier version you can
also change and renumber the objects
we are basically unlimited when it comes
to the size of the data that you can
Cloud migrate but it's a good idea to
clean up the data before it triggers the
cloud migration
and if you're going to do something our
ask is to clean up the corrupted quote
fields
so the corrupted quote fields are
usually coming from the times before we
had a SQL database
so customers were able to enter new line
characters lowercase characters and
other non-printing characters to the
code fields
SQL doesn't like it and this field if
you copy it you will not be able to see
that it has an online character you need
to detect it with a dedicated SQL query
issues that if you Cloud migrate with
these fields any code modifications read
delete operation is going to fail and we
are often seeing issues with the loop
like this one so if you do customer find
set and then you Loop and modify the
customers when we reach one of these two
customers it is going to fail with the
arrow records does not exist
because platform is unable to read the
records with new line cards
to fix it we have invoke nav sanitize
field action
and my recommendation is that you take
the copy of the customer database run it
once to identify which tables have the
problem and then you can sanitize their
production database even before you
start doing the Cloud migration
you can optimize them and you know which
tables have the problem with Dash table
ID parameter and customers are going to
be happy because they're most likely
experiencing issues with these records
on front
company names could have the same
problem they're not going to be covered
by the Powershell commandlet because
it's not a code it's a text field but
the problem is basically the same you
can use a query like this to detect if
the company name has a problem
and the issue is that the cloud
migration is not going to pick it up and
you need to rename the companies before
the cloud migration
now for cleaning up the data you should
know all of these reports but I would
recommend that you go to the data
archive page because it is listing all
of the reports that you can use to
compress the entries
or to delete the records that are off to
date and it's a good idea to do it
before the cloud mirrors
all right and with that I'm going to
hand it over to Roman for the second
part
but thanks
um
all right let's have a look
[Applause]
let's have a look at the cloud migration
under the hood
so on the left hand side here we have
our source
environment a business Central on-prem
installation with a SQL Server database
on the right hand side we have our
destination a business Central online
environment
with an Azure SQL database
so we're using Azure data Factory for
cloud migration and Azure data Factory
is a cloud-based data integration
service that allows to copy move
transform data across various data
sources
one of the
main concepts of azure data Factory are
pipelines and these pipelines are
essentially groupings of activities and
these activities copy move transform the
data or also orchestrate the flow of
data
the third piece here is the integration
runtime this is the compute
infrastructure that Azure data Factory
is using and especially for a case like
here where we have
our source in a private Network in an
on-prem installation on on the customer
side it is a self-hosted integration
runtime
and this is installed within the network
of the customer on-prem and then
registered with our Azure data Factory
and in that way it allows us to do
secure copy of the data from from
on-prem into the cloud where we then
take it further with an Azure
integration runtime to copy the data
into
the destination SQL database
important to know here that there is no
NST needed no NSD running needed we
really connect directly to the database
and the self-hosted integration runtime
is also doing only calls to the outside
to the Azure data Factory that has been
linked with
if your Source database is in Azure
already then we can use an Azure
integration runtime
and then the data goes into the cloud
and from there we follow the same flow
copied into our destination database
so the first step to make this work is
to do the setup so if you go in in your
destination environment to the cloud
migration
wizard the setup wizard you need to
provide the information about the SQL
Server
what are the the connection string and
what is your integration runtime that
you want to use
we have several Azure data factories
running and we use load balancing to
find the best one for for a particular
um
Cloud migration run
and in the first step we register
the your integration runtime we exchange
the authentication key and then these
two are linked
once that is done we create a
preparation pipeline
and this preparation pipeline does a
couple of checks so checks the
destination
and the source for example looking at
the compatibility level
looking at the version do the versions
match
and if the checks succeed then we
continue and create a bunch of stored
procedures
again on both sides on the source and on
the destination
we also read the list of companies from
from the source
and look at the list of extensions that
are installed on the destination
and then based on this information
prepare a list of tables
that need to be copied
and also how to copy them
with this information then we create a
replication pipeline and this is then
the actual pipeline that is going to do
the copy this pipeline is going to sit
there basically knowing about all the
tables the extensions what needs to be
done
and is is ready to run once you actually
trigger the replication
so once all of these steps have have
been done we Mark the environment as
ready for migration and we clean up the
preparation pipeline
so we're actually quite excited to see
many Cloud migrations running over the
last month and also years
and um
we we're continuously looking into
improving the flow improving the
experience and as part of that we we are
regularly looking at what are the most
common errors and failure cases so I
want to give a bit of
advice maybe some some tips to to avoid
these these common pitfalls that that we
see
um so one of the things you can imagine
is that the user requires certain
permissions
um
if those permissions are missing we have
error messages like like these ones here
and
it it
basically points to a couple of things
so one is that the user
that is doing the setup in BC has to
have the super role
if it's a delegated admin
then there needs to be the customer
consent given to run successfully
the SQL user itself also needs a couple
of things so on server level the
sysadmin role and for the for the DB DB
owner role
that allows us to to do all the
preparations and Creations of start
procedures
so user permissions we also see
frequently errors in the connection
string
[Music]
for example keywords that don't match or
parameters missing and I just pasted
here A A an example a link so it has to
be exactly like this and the connection
string we have it also documented in the
documentation and if it's a Azure SQL
database you can find your connection
string on the Azure portal go to the
resource and you can you can copy it
from there
um we also see SQL timeouts
um which then look like an activity
timing out in the Azure data Factory
and the mitigation for that is so there
are certain minimum requirements for the
self-hosted integration runtime
um one of them is also
minimum.net 4.72
um
and we have seen a couple of database
query performance optimizations that
help
um in in those steps so one of them is
to update the statistics the query
performance statistics which you can do
by running this stored procedure
and also the indexes
um so by reorganizing the indexes we
have seen
um also performance improvements and
avoiding timeout situations
so there's a couple of tips
um also we we post this on the on the
documentation
um have a look there
we also see cases where the product type
or the version is not matching and
this shows up as a more generic error
messages error message so
pick pick the the current version if the
major version so it's important that the
major version is matching here from from
your source and the destination
otherwise pick previous version and one
thing maybe that is also easily missed
is there's this property in the
attendant database property table the
application version that needs to be
updated manually after an upgrade
on-prem
um so if that one is missed and doesn't
match then we also see see this error
okay
um finally also we see a SQL failures to
connect
um
this is typically
um showing up like this so we have a SQL
failed to connect
um
or some firewall issues and
and we we recommend to do some
some some essential connection checks
before so verify that the user can
connect to the on-prem DB user correct
check also that the machine that is
running the integration runtime has the
ability to access the SQL Server
you can run a simple query here
using the
basically a remote execution and
check the connection there on the
firewall level make sure that the client
IP address has is is whitelisted and it
has access so this can be done with this
dot procedure and finally also the SQL
Server that's
um a running needs to allow remote
access
which you can do with with this dot
procedure
so once the checks are successful and we
have created this replication pipeline
we can actually do the migration and the
replication and with this I'm going to
hand over to Julia
so you go to start the replication run
you go to Cloud migration management
page and there is an action there
so run migration now and that would
start a new migration run so what does
it do it makes a call to the Azure data
Factory to your replication pipeline
that is stored during the setup
and this replication pipeline stats
execution
and it instructs the self-hosted
integration runtime to pick the data
from the on-premise database and copy it
into an Asia blob storage we use that as
a temporary store for the data and its
original so your data is not moving
outside of your region
and then the integration runtime in Asia
would take the data from The Blob
storage and move it to the channel
database in the cloud we do it in two
steps for for a couple of reasons so one
is the performance the most
slow process is the transfer of the data
from the on-premise database to the
cloud and self-hosted integration
runtime has the ability to compress that
data so this step is actually running
faster of course then we have to
decompress when we are in the cloud
already but it's faster because we are
in Azure so this this is how it runs and
if you have large tables that have to be
replicated then these tables are going
through exactly this path so they're
open one by one uh through the Azure
blob storage and you can watch the
progress on the cloud migration
management page if you refresh the
status each large table that has been
replicated would show in the statistics
there immediately
but for the smaller tables we introduced
an optimization
so we actually collect the data from all
the smaller tables we serialize them
into huge Json then we compress it and
then we chunk it into the records of a
special table and then just this one
table is being replicated go on the same
path
and or in the Asia side the stored
procedures that are running in the
tenant database they would get these
records again combine a huge Json
decompress it and then put the records
one by one into the corresponding tables
in the tenant database so if you watch
for the status this process is moving a
lot of tables but you won't see the
progress immediately so you have to wait
because we reported by the end when the
records are actually in the channel
database
uh so when you do the replication the
first time we replicate all tables we
call it a full replication uh run and
then we actually use uh SQL change
tracking versions
uh to make this subsequent runs faster
so if you run replication again we won't
move all the data but only those that
are Delta change so incremental that
would make it faster
um
we are using change track and so it's
important that you do not replace so you
don't change your on-premise database
otherwise the change tracking becomes
invalid we have to drop it and we have
to do the full replication again and if
this happens you'll see a longer
replication run again
so that was
um for the process and now uh
so the replication is done by Azure data
Factory and it's mostly very stable we
don't see so many errors as in setup you
see that it's completely different scale
but like three major errors something
happened in Don premise during the
replication run
or you hit one of the limitations in
Asia data Factory itself it could be
either large metadata or large data
so let's see Photon premise intervention
you can have
integration runtime is offline
or you can have invalid object name and
could not find stored procedure on the
SQL level
so for the first one our recommendation
is you keep the machine that hosts your
integration runtime online all the time
while you're doing Cloud migration so
sometimes people shut it down to
interrupt to cancel a replication run
that could be done no problem but if you
keep it offline too long then we
actually have some automated clean
procedures that might just wipe out the
whole you know all the Asia resources
that we are associated with your
replication and then you cannot resume
it easily you have to go through the
setup again
and for them
SQL errors this is happening when you
actually replaced the database maybe you
restored it from the backup but you did
it before the replication run completed
so it couldn't continue it didn't find
the objects
now these are the most difficult errors
that you faced they're not very common
there are like maybe 10 errors per month
that we see large metadata and
um so what is metadata metadata is a
Json serialized description of all
fields in all tables in all extensions
and for all companies that you are
replicating in this particular run
and Asia data Factory has a limitation
for this text description to be less
than four megabytes so it's not very
much so if you try to migrate to many
companies you might get an error message
and the error message is coming directly
from Azure data Factory so it's maybe
not easily understandable
so one could be the lookup activity
result exceeded the limitation or the
user payload too large
we it's during the runtime of which data
Factory and you see them directly we
don't have a chance to to intercept them
and change the the warning there
so yeah if you see that you're uh you're
trying to my probably trying to migrate
to many companies at once
so we suggest that you kind of reduce
the number of companies for migration
you can do it on cloud migration
management page there is an action there
to select the companies to select few
companies run the migration then select
the next batch that would be a much more
stable and probably a faster at the end
than trying to migrate a lot of
companies at once
um right sometimes you have a lot of
extensions installed in your tenant
already in the cloud but you don't have
data for these extensions in your own
premise database so
um
it's not harmful as such but why to do
that it also contributes to the large
metadata I think so we recommend that
you uninstall unnecessary extensions
from the cloud prior to Cloud migration
and then install them back as you start
working with them
right and finally you can for your own
extensions you can exclude some of the
tables from cloud Migration by changing
the attribute on the table on the L
table duplicate data to false
then the next kind of
type of Errors is when you're trying to
migrate large data and that could happen
if you if you you can get it in in two
different paths so when there is a bulk
copy many small tables going as one bulk
right in this case what we see most
often out of memory exception this out
of memory in the Azure data Factory
infrastructure it's not the business
Central infrastructure so we don't have
any control on that but yeah our task
failed out of memory
so
what we say
what we see is that usually it happens
when tenant media table is going through
the bulk and it contains some large
images so it's like a it's a very big
value in a single field that does it
this images are they are not
compressible so if you see out of memory
exception like that so we recommend you
[Music]
work around a hack so you can find a
stored procedure that was installed in
your on-premise database it's called is
full copy
stored procedure and add a block like
that that would redirect tenant media to
be copied one to one to the cloud and
hopefully you will avoid out of memory
exception
if you still get it then just create a
support ticket and we'll try to help you
out
another large data could happen when
it's table to table full copy but the
error message would be different so you
see the specified row delimiter is
incorrect this is happening when the
Azure data Factory cannot read The Blob
storage the temporary blob storage
so the workaround is the opposite try to
see which table failed because it's one
one to one so you'll see the neighbor
the name of the table and try to
redirect it into the bulk so hopefully
it is compressible so it will it might
succeed we reported most of these errors
to Azure data Factory so maybe at some
point they'll prioritize the fixes and
we won't see it anymore
but today this is what we face
right so the next okay some performance
tips something of that we already talked
about so for you and on-premise
infrastructure the most important is the
machine with the integration runtime
they have specified their own system
requirements that we have to honor
then if your sources as a SQL then you
you can monitor the CPU and memory
utilization or in the Azure portal and
you should upscale your database if you
see high consumption during the cloud
migration process
then what Roman already mentioned we
have update statistic and recognize
indexes for the source database we
recommend to do that before you set up
your database for cloud migration just
once
and then use a dedicated SQL Server so
don't use this server that is already
busy with some other production you know
activities but have have a server that
is only doing client Cloud migration
then it would be faster
yeah and yeah Universal reduce the
number of companies set up for cloud
migration so what we see is an optimal
size is about 10 15 companies it could
be more it depends on your data and
depends on the how many objects you have
how many extensions
um yeah but try and see
what works for you
and one topic that I wanted to talk more
so when you replicate data we do some
default mapping so you normally you
don't think about it but if you have
tables with the same names both and on
premise and in the cloud then we just
copy them but we copy them because the
SQL names match so if you look at the
SQL names and that usually the company
name the table name and the extension ID
so if there is a full match the data is
copied apart from the extra fields and
Nikola just mentioned so if you edit
some fields that are in the on premise
but they are not in the cloud we will
just silently ignore them the nothing
happens nowhere or snow warnings but
they're just not there
so another case if you have a table in
the cloud but there is no matching table
in on premise database
in this case we replicate the data for
all the other tables but for this table
you will see a warning
a warning like this that the the table
doesn't exist in the local installation
so
in most cases it's safe to ignore it but
uh just make sure that this is expected
that this is what you wanted and you
didn't miss this table just for some
reason
right and if you have different tables
for example if you have installed
absorption extension and you were forced
to use three letters prefix
but you have data for it in non-prem is
it just the table name is different you
still can migrate
so in the cloud migration management
table we have an action
called table mapping and there if you
use it you will be there is a drop down
to choose the extension and the table
and you just type the table name in
don't premise that should be a matching
table and we respect this mapping
student the next migration run we will
take the data and move it to to a table
with a different name
yeah move all the fields that are
compatible and that have the same names
in both tables so that was it for the
replication process and now Nikola is
going to talk what's happened next after
you replicate the data right thanks
[Applause]
so for the last step it's going to be
the data upgrade and I'm going to show
to you two improvements that we did to
the existing process
the first Improvement is that we are
leveraging the upgrade Logic for the up
if your Cloud migrating from previous
versions
to explain this one in a little bit more
details for version 20. when we have
written the upgrade code that is
specific for version 20. we needed to
take the changes and to adopt them so we
can use them for the cloud migration
and the reason why we need to do this is
because we are unable to invoke the
upgrade code units
and as you know the change is needed
because you cannot access obsolete
removed fields from non-upgrid scope
now some of the partners that have also
written the upgrade code that would like
to use it would essentially need to do
the same change
take it and adopt it so it serves the
cloud migration
and then the problem is when the upgrade
21 comes we need to do the same
operations both you and us so and
essentially we should not be doing this
because we should be able to reuse the
upgrade code that we have written and we
should be able to remove this extra code
and extra logic that we did
so this is the first Improvement because
we are triggering the full upgrade
quotes all apps are going to be included
and you will have a single upgrade logic
the next benefit is that we are going to
move the tenant to the status of
upgrading which means that hotfixes are
not going to interrupt the upgrade also
it is going to be a single session which
means you will get a more stable upgrade
also you're going to get all of the
reporting and Telemetry that we have
automatically included and in case the
upgrade fails you'll get an automatic
bit restore
to show you the flow in action so if you
go to the cloud migration page and
invoke Run update now we are going to
warn you that you are going to lose the
access to the environment because
upgrade will start and that you can
track the status in the admin Center
so if you say yes you will get the
message that the update was scheduled
and now you can go to the admin Center
and you will see that the status has
been flipped to updating if you go to
the operations tab you will see that we
are logging the history and you will see
that the object operation is running
if you try to access the environment
you'll get sorry you cannot access it we
are running upgrades and the main
benefit of this one is as I said no
hotfixes will be running and upgrade
needs to be this only session that is
running on the server because if you're
using the system you may incidentally
cause locks and cause errors during the
operator process
now if you go back to the
admin Center and you refresh
approximately after three minutes the
status will flip to active and then if
you go back to the business Central
you're going to
so okay and back to the cloud migration
page
the status is going to be flipped to
completed you will see it in a second
and now you're able to go live after
this step
now in case the upgrade fails then in
this state
you can go back to the operations Tab
and you'll see that the operation has
failed you'll get a full stack Trace we
are looking into providing you with a
nice error message as well so you can
see why did it fail and you can go back
to the business Central you'll see that
the tenant is operational because we
have restored it as point in time
and here you will see that upgrade is
pending because it was restored to
before we run the operate so now you can
fix the errors replicate additional data
or try to run the upgrade again
so with this new flow you're also
getting an automatic point in time store
the good news as well is that because we
are just rolling this one out we are
still supporting the old upgrade flow so
if you took any dependencies to how the
system used to work in the past it is
still possible to trigger the old
dungeon we just we can programmatically
enable the old upgrade parts
if your solution is affected by this
then for the last topic we did some
faster upgrades and faster an upgrade
are usually not the words that you can
hear together
right you usually it is much slower
so for this one we got the data transfer
feature and unfortunately I will not be
able to talk about it much I will just
briefly cover it
the problem is that most of our
long-running object is actually being
caused because we are moving obsolete
removed Fields onto the new fields and
we are doing it in an inefficient Way by
using the loopy loopy solution where you
are looping over the entries and
modifying them
the problem with this one is that it is
rather slow so if you want to update 1
million entries it's going to take
anywhere between 2 hours or 24 hours and
more
the reason why is it fluctuating so much
is because it depends on how strong is
the SQL Server how many table extensions
you have and how many subscribers you
have to do on modify it so it can be two
24 hours or even more
now
with data transfer features we have a
much more efficient way of doing this
so instead of doing the air Loop you
would say which table is being mapped to
which table you can add Source filters
you can add join statements you can map
Fields one to another and when you call
Copy fields we are actually going to
invoke a SQL query and we are not going
to raise any events so it is going to be
very fast
to give you the comparisment numbers
with the data transfer one to million
entries is approximately taking two to
five minutes
so with this feature now we are able to
update the large tables like customer
legendaries
yep
now it has some limitations because it's
a very powerful feature we can only use
it in upgrade scope to initialize the
new Fields so the only usage we can use
it for is to move the obsolete removed
Fields onto the new field because
otherwise it would be a breaking change
if we do not raise the events
and since it is a powerful feature
currently it's marked as targets on-prem
which means that you will unfortunately
not be able to use it for SAS solution
but you can use it for your on-prem
upgrade if you want to make it faster
now with every new release we are
getting questions how many long running
methods have introduced and I'm happy to
say that for this release we have
shrinked the number of long running
methods by 11 because we use this new
data transfer feature to optimize the
long running upgrade that we
historically know that it has existed
so hopefully the journey to the cloud is
going to look like this
it should take much less time to upgrade
the on-prem
and because we are reusing the same
engine
it should take much less time to also
Market the sauce
since we are using the engine we get all
of the benefits that we usually get
and I hope that the ultimate task
basically is going to be done by you
guys so we are looking forward to your
feedback but we believe that the upgrade
to 21 it's going to be faster than the
operator 2020.
so with this I hope that we have fixed
the long-running upgrade problem
and for the end we have the API for
managing the cloud migrations end-to-end
so this is very useful if you're doing
many Cloud migrations or if you want to
move many companies like 50 or something
like that you can basically the entire
flow of that you can see in today you
can automate it through the apis you can
do the setup company management and then
you can manage the cloud Migration by
doing it on the BC Tech GitHub you have
the example of all of the apis you can
try it out
and in case of any issues if you would
like to provide this feedback we
recommend that you join us on the BC
Cloud migration Yammer you can see that
we have 870 Partners here partners are
also providing with a lot of interesting
information helping others
so please join us on Yammer and with
this
we are ending the presentation we are
just out of time so if you have any
questions I would invite you to come
down and ask us a question and then we
can discuss it otherwise you can find us
around and we can talk about any topic
thank you
[Applause]
[Music]
foreign
[Music]
