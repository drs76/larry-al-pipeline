# BC TechDays 2023 - What's new in cloud migration and upgrade

- **Source:** https://www.youtube.com/watch?v=hAYcVIx1AbY
- **Video ID:** hAYcVIx1AbY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 49m08s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

all right hello everyone and welcome to
this session about the cloud migration
my name is Nicola and I'm mostly working
on the UI part of the cloud migration
and together with me I have Yulia
hello I am a developer responsible for
the back end of the cloud migration tool
yes so in this session we have prepared
a lot of content for you so we are going
to start with the some problems that we
did in the backend that you always going
to talk about we will mostly talk about
the performance optimization
stability improvements and also some
really nice improvements that we got
under the hood that is going to help you
to spend less time on the cloud
migration
then I'm going to demo to use some of
the improvements that we did to the UI
also the feature that is here going to
help you to move the customized fields
to the table extensions
and we are going to end with the
Telemetry new upgrade strategy and we
are going to briefly discuss what are we
planning to add for the future for the
cloud migration to link
okay then clinical
so
before talking about the recent
improvements in the cloud migration
replication engine
let's take a look at the usage of the
tool between the years
here there are two charts showing some
very nice growth and we would like to
thank you for using the tool
we cannot show the relative increase
here but trust me the actual numbers are
also very impressive so thank you very
much
so on the left chart we can see that the
number of business Central tenants
migrating their data from on premise has
almost doubled last year comparing to
the previous year and on the right we
see that the amount of data transferred
to the cloud has almost tripled in 2022
comparing to the year before
and this tendency still continues this
year business Central tenants are
getting more and more data migrated from
on-premise
we take year 2021 as a base because back
then we removed the hard limitation on
the amount of the on-premise data that
can be replicated to the cloud
and that enabled Cloud migration for
large installations
and in tune it revealed some technical
limitations and Performance challenges
that we had to address
to better support high volume Cloud
migrations
that is on premise setups with a lot of
companies and tables and containing huge
amounts of data and that was the project
that we now completed
so before presenting the results to you
I would like to briefly describe how the
replication engine works and highlight
the parts of the replication process
that have been improved
and then we'll talk about each of the
areas in more details
as you probably know we use Asia data
Factory pipelines to copy the data from
a source database to the destination
when a migration runs triggered the
replication pipelines gets executed and
it instructs special compute Services
called integration runtimes to access
the data in both the source and the
destination databases
The Source can be either an on-premise
SQL server or an Azure SQL database and
the destination is always an Azure SQL
of a business Central tenant
so first of all we made quite a lot of
improvements to the replication
pipelines so now they can support larger
Cloud migrations and also can migrate
wider range of data types
during the execution the replication
pipelines use Asia blob storage as a
temporary staging
unfortunately blob storage introduces
its own limitations and we applied some
optimizations to minimize them
the data replication itself is done by
two distinct processes the large tables
are copied table to table by dedicated
copier activities
this process has been optimized
the smaller tables are going through the
process called bulk copy during bulkope
the stored procedures in on-premise SQL
database collect box of data from many
smaller tables serialize and compress
each bulk and then split it into records
in a special table
then only this table is copied to the
cloud where the stored procedures in the
tenant database apply the opposite data
transformation combine the records
together decompress this realize and
push the data into the corresponding
tables
this process can be repeated for many
bugs until all data is replicated
and it is very efficient for copying
thousands of tables faster but at the
same time it's very demanded on the SQL
Server compute and input output
capabilities and here we made some
improvements as well
finally it was mentioning that we use
SQL change tracking to identify the
changes made to the on-premise data
between the replication runs and copy
only these incremental changes if it is
possible
this path has also been improved
allowing us to recognize more situations
where the Delta sync as possible and
reducing the overall migration time
most of these improvements affect
migrations from both on premise SQL
server and Azure SQL but there are some
that make a huge difference specifically
for Azure SQL sources
so let's look at these improvements in
more details and see how you can benefit
from them in your future migrations
looking at the replication pipelines we
change the way the replication metadata
has been passed between the source and
the destination instead of using the
data Factory
activities input and output parameters
we now copy the metadata through a
database table and this allowed us to
bypass the four megabyte data Factory
limitation on the activities input and
output
so it has become possible to replicate
an unlimited number of tables in a
single migration run and we removed the
limitation on the number of companies
being replicated
of course it's important to remember
that business Central supports not more
than 300 companies in a single
environment but now all these companies
can be replicated in one simple run if
you have a powerful on-premise SQL
Server
apart from this we also remove the
calculations on the on-premise database
size from the replication runs
this calculation is done once during the
cloud migration setup and not repeating
it during replication can save between
15 and 45 minutes for large Source
databases and reduce the probability of
timeouts
and finally we expanded the replication
pipelines with the activity scorpion SQL
sequences specific for business Central
so now the AL number sequences data type
is supported by Cloud migration and the
numbering can continue in the BC tenant
after migration instead of being reset
so for table to table copy
let's look at the optimizations here
table to table copies used for large
tables
however
we reduce the threshold
now the replication engine Peaks would
pick a table for table to table copy if
the data size to be migrated exceeds 250
megabytes and it used to be 500 megabyte
before so this means that more tables
are going through table to table copy
now and the replication status is
updated faster for these tables
also tables with a lot of data tend to
have many indexes defined when the data
is copied all the syntaxes have to be
updated on every insert now we disable
the indexes in the Target table before
copying this data and rebuild the
indexes after the data is replicated
and our test measurement showed 8 to 22
performance benefit for the new process
comparing to the old way of inserting
the data with all indexes enabled
because both the cleanup of the target
table and the data copy are now
happening is no active indexes
the replication runs are much faster and
disallowed to prevent the timeouts for
the latch
tables replication for the bulk copy of
the smaller tables in addition to the
reduced threshold they also reduce
the bulk size
so this resulted in higher numbers of
smaller bulks and smaller bugs are
easier for the SQL Server to serialize
and compress so the timeouts occurrences
become rare also they may still happen
for the extremely weak or busy SQL
servers
in fact this gave a significant
performance benefit on our not very
powerful test servers the whole process
of bulk copy became 60 to 80 percent
faster
the replication status is also updated
more frequently if the Box are smaller
we also made the diagnostic grants
respect the bulk size
before they tried to process all data in
a single huge bulk and that often led to
timeouts and out of memory exceptions
now diagnostic runs utilize the same
smaller box as the normal replication
runs they don't time out and you can
safely use them to quickly test the
future replication
finally optimizations for the Delta Sink
of the incremental changes which are
related to our usage of SQL change
tracking
so if the changes between two change
track inversions can be reliably
collected the replication engine
performs a fast Delta sync otherwise the
whole table has to be cleaned up and
replicated again
so we forced a longer change track and
retention period that allowed the change
tracking versions to stay valid longer
and that increases the probability of
the fast Delta synchronization for the
repeated replication runs
and we change the code to use change
tracking in a wider range of the
situations for example Delta sync is now
possible also for the databases that
first enable change tracking
specifically for cloud migration
and now Delta things are happening more
often reducing the overall migration
time
so all the improvements mentioned
earlier I applied to boost SQL server
and Azure SQL sources however if Asia
SQL is used as a source it is possible
to link the source and the destination
Azure SQL databases directly without the
requirement of the serialized staging in
a nature blob storage
and removing staging allowed to make the
replication faster
so now we don't have to serialize and
deserialize the data and it has become
possible to replicate the fields of C
covariant type also the errors caused by
the bloop infrastructure are gone away
for example trying to copy a record with
large value in a single field like image
sometimes fails in the staging loop with
the message that the specified row
delimiter is incorrect
so this won't happen for the migration
from Azure SQL anymore
so in general these all these changes
Asia SQL becomes a more powerful and
better performance alternative to the
SQL Server as a source for cloud
migration
so if you have plans for some high
volume migrations you might consider
deployment on premise database to an
Azure SQL first
and if you want to migrate SQL variant
Fields or Fields with large images then
is your SQL as a source would be the
only possibility
so the process of deploying an Azure to
Azure SQL is it can be quite fast if you
have the right service tier in your
Azure SQL database
it is also well described in the SQL
online help
how fast it can be depends on the
serious tier that you have to choose for
your SQL for the for your Azure SQL
database
and our recommendation here is to
prioritize its compute and input output
capabilities
of course the Azure SQL is not for free
and you would probably have to balance
the cost and the benefit
but the more powerful service tier you
get the fast and smoother your Cloud
migrations will be
and with that I pass it over to Nikola
to present the new UI and other UI
driven improve
Improvement thank you Julia so we are
going to proceed with the new UI
and for the new UI we are going to go
straight into the demo
we are going to start in the old UI and
the thing that you can see here is a
rather large Cloud migration that I did
in the old UI beforehand so you can see
how it is looking like
and one of the things that you can
notice here it is extremely hard to get
an overview which data has been moved
and if there has been any problems
with the cloud migration because you
needed to select the specific records
and then to search for the tables field
if they exist so for example on this
replication run you can see that the
three tables have failed but you have no
idea what is the current status of this
date
we have also seen that many partners
were doing similar mistakes when going
live and these mistakes will costly to
fix
so in order to address this we have
introduced a new UI and for the first
feature to demo today I'm going to show
you how you can switch between the old
and the new UI
we have decided to support both for the
time being because we believe that some
of you have done the customizations to
the old UI
so in case you need to switch between
the uis you can invoke this action
enable disable the new UI so if you
select here and they say that you would
like to use the new Cloud migration UI
the product will take you to the new
Cloud migration UI
the new Cloud migration UI is going to
be shown to you by default each time
when you set up BC Cloud migration
GP Cloud migration and SL is still using
the old UI
the thing that you can see here is that
now we have laid out the data in a
different way so we have a overall
status showing you what is the current
status of the cloud migration like this
and the reason why we did this is
because you have a single Cloud memory
so now the UI is actually representing
the state much better
and you also have a set of steps that
you did to This Cloud migration
so you can see the history as the
migration log which is below
when we have also split it like this now
you do not need to select a record if
you want to start the upgrade or any
other action we will check the overall
status when performing the actions
another thing that is very visible is
that you have actually failures and
there are six tables that have failed
the replication
if you invoke the drill down here
it is going to be visible which tables
currently have the problem that you need
to address and fix
then if we go back
now if we add up here the system is
saying Six Tables but if we add up there
is more failures in the log
so you can see that here is nine tables
that you filled your application
and the reason why is because if you
select for example this one here
the thing that you will see is that the
text is not highlighted The Dread and
you will also see that the last
replication status is successful
and if you drill down on this section
here you will be able to see that there
is a later on which has copied the data
that has failed which means that you do
not have the problem on this table so
there is no action it is required from
you
if you would like to analyze what has
happened you can also invoke the show
all replication actions
and then we can show you all of the runs
in which this table was involved and
this is the same data as you have seen
before so you see that there was one run
that failed and then there was one run
that was successful and one record was
copied and told
so with the new UI now you're able to
see which tables have failed the
replication and which tables are
requiring your attention immediately
one of the flaws that we wanted to
improve is if a small table fails in
many cases Partners would just like to
migrate the data from this specific
table
unfortunately this was not possible
because we would block it and then you
would not be able to move this data
either through a customized solution or
through a rapid start
so
to enable you to be more efficient we
have added this action which is called
unblock the table so if you invoke it we
are going to Mark the table as pass and
we will allow you to write the data to
it so if you invoke this section here
we will say to you that the table was
successfully unblocked and now you can
move the data through the configuration
packages or the other means
one thing that you should do before
invoking the action is to note down in
which company and which table failed
because we remove it out to the list so
when you invoke the action it is going
to be a bit harder to find which table
has failed
so unfortunately we did not keep the
track of the field tables
then in the new UI you can see the
overall status of the companies
so you can see that I have missed eight
companies to be moved
if you are wondering which companies are
moved
and which companies are not
here you can go to the replicated filter
and say
no
and here you're going to see which
companies you have not moved from the
on-prem
so we are not going to include it for
the purpose of this demo so we'll just
connect the exit here
then another thing that you can use this
new iPhone is that you can see the
overall status of all of the tables that
have been moved so if you invoke it here
you will be able to see the status of
all of the tables across the different
ones
so here you can see all of the tables
that have been moved from the specific
companies
you can filter
per company and one of the things I
would strongly recommend you to do is to
select predatabase tables and to check
what is the status for the predatabase
tables
here you can see that the custom report
layout and Report selections were
completely replaced and you will see
that these tables have the Delta and the
reason why they have the Delta is
because they are tenant mediatives
so tenant media if it was copied
successfully it needs to have more
records than they are in the on-prem
database because we never replace the
data
in case the data was replaced or in case
we have copied less records than the
repeats in the source database please
open a support ticket and we are going
to help
this should not happen but it is good to
verify because unfortunately we do not
have the warning system in place yet
and the last item that you can see here
is the upgrade tax and here we are not
able to get the records because the
table is marked as internal thus we will
just put a small work
the tables that are internal or marked
as obsolete removed we cannot do
anything about them unfortunately we
cannot provide the account so we just
show a warning and keep an eye on the
data that is being pulled
then the next functionality that you can
use this page for is that if you are
wondering what has happened to the
specific type of data we would need to
select all so we can go back
and then if you go to the table name
and here
if I would like to know what has
happened to the change log entry so I
can type
and when I invoke okay
and I select the change lock entry table
we are going to tell you that the table
is excluded from the cloud migration
because it has replicate data property
set defaults we are also going to show
you the message that it was empty on the
on-prem table so this page can provide
you additional details what has happened
to the specific table and why the data
is not moved
all right so that was odd regarding the
overview of the data
then the next thing that you can use the
new page for is that now we have a
complete Cloud migration status and if
you try to invoke it we are going to do
the sanity check
and in this case I cannot complete the
cloud migration because there are failed
tables
so I need to pull the data to make sure
that all of the data is moved and then I
can complete the cloud migration
but if I would like to stop the cloud
migration so I can do something I can
use the pose and abandon actions and I
have them here
so I can use post Cloud migration and we
recommend to use this actually if you
plan to continue it
and the second one is the abandoned
Cloud migration which you can use if you
are planning to delete the environment
and completely abandon the cloud
migration
there is no difference between these two
actions except sending the Telemetry and
telling to us what is the current status
of this environment
so if you regret abandoning the cloud
migration you can simply reconfigure it
again and everything is going to work
I have done this in the log so you can
see it here
I have abandoned the cloud migration
because I needed to reconnect Dr which
is both the wrong step but I simply did
it to show you that it is possible to
enable it again and pulled the date if
needed
and for the last expert feature that we
have we have added an action so you can
sanitize the data so if you go to the
actions and sanitize the tables so if
you forgot to run invoke nav send it by
stable on-prem which we strongly
recommend that you do you can sanitize
it in SAS but you need to select the
company
and you need to select the table that
you want to sanitize
so it has to be a specific company and a
specific table and then when you invoke
the sanitize table we will run the code
that should have been done on-prem by
the invoke nav sanitized build action
this can affect the performance of the
tenants we recommend to run it outside
of the business hours
and again I will repeat please run this
action on-prem to make sure that the
data that you're copying to SAS is
correct
okay and that was all for the new UI so
moving to the next UI feature is moving
customized skills to the table
extensions
on the previous Tech days we have
announced that we are planning to do
this and we have invited you to help us
to test the feature and to provide this
feedback and I would like to use this
opportunity to thank 20 partners that
have participated in this effort and
provided the feedback and tested the
functionality which we have developed
we have shipped it with the version 21
actually because we back ported the code
to make it more efficient
to explain the feature if you have not
used it before is if on-prem you have
customized Microsoft owned tables so
let's say that to the table customer you
have added three fields
that you want to move to source and you
have some fields that you wanted to
leave behind
so in SAS of course you cannot have
customized fields in Microsoft on tables
so it can only contain Microsoft on
fields
all of the data needs to be moved into
table extensions and let's say that you
want to split the data into table
extensions
customer is going to be copied
automatically because it has replicate
data properties set to true so we are
going to insert the default mapping by
name and we are going to search for all
of the fields that we can map by name
and type and we are going to
automatically replicate
if we do not do anything the other
fields are going to be left behind
but now you are able to do this simple
migration table mappings
and this will copy the custom fields to
the Target table if the fields match
so if you specify two table mappings
engine will be able to split the data
between these two table extensions and
automatically map the fields that it can
by name and type
one important thing to note here is that
you need to rename the fields so you
will need to prefix them so they are
called the same as in on-prem and in
source
you can do this in either CL because CL
allows breaking changes but you can also
use SQL scripts because the only thing
that the engine is looking at is the SQL
definition
so it is even possible to rename the
fields in SQL
on the keynote you have seen that we are
planning to introduce name spaces and
the goal of the development team is to
eliminate prefixes and suffixes in all
of the objects including the table names
and table fields so hopefully this
rename in the future is not going to be
needed
to show you this feature in the action
we are going to move to the next name
here in SQL I have two tables one is
customer and the second one is real
entry and as you can see they all have
customized fields as you've already
renamed them through the SQL script so
this one is named pte1 and this one is
pt2 and pt3 because
I would like to split this customer
table into three table extensions
and it's the same for the Glen entry
table I wanted to do the same so I want
to move two Fields into ep1 and the
other two fields to the pt2
if I switch to the cloud migration UI
and and if you go to the extensions
management page
and under the manage extensions
installation status
you can see that I have already uploaded
three PPS that I'm going to use as a
target for the cloud migration and this
is of course the necessary step that you
need to do before you can Define the
table mappings
now if we go back to the cloud migration
UI here is the action which is named
manage custom tables
and if we invoke it here
when it opens you can use this page to
define the table mappings
you could Define it in line by selecting
table accession and then filling out the
other fields however we can see that
this is error Pro
if you make a mistake when you define
the migration table mappings no data is
going to be moved across
and these kind of issues are a little
bit difficult to troubleshoot
to help you to add migration table
mappings in an easier way but also in a
less error problem way we have added a
dedicated UI for that and you can access
it through this section which is called
add table mappings if you invoke this
section here
on this page the only thing that you
actually need to provide is the name
and if you would like to add it so you
are sure that there won't be no mistakes
we recommend that you copy the
definition from the sequel including
square brackets and you just paste it
into this name field here
so if I do this
the system is automatically going to
burst and it is going to set the app ID
but this is only applicable if the table
is an Al table
and it is also going to update this
property is the data per company or not
because we customer is the data per
company is going to set it to true
then you need to say that you want a
table extension here
and you need to select which extensions
you want to map so we can filter down
the list
so we want these three table accessions
that I have uploaded
so now here I can see all of the table
extensions that the extension is
containing I could even walk okay
however that would insert one migration
table mapping and then I would need to
repeat this process three times
this is not needed because if you select
three rows
then we are going to insert three
migration mappings
the next if we would like to add the GL
table mapping I'm going to invoke this
action again
and back to the SQL management Studio
I'm going to copy the table name and the
thing that you can see here is that the
value is already escaped so it has the
underscore instead of the Slash
so I'm going to copy it like this and go
here
and paste it
the system is going to parse the values
again and then I just need to select
these values
and when I invoke okay
it's going to insert three additional
mappings
so now you have seen how quickly you can
Define six migration table mappings and
split two tables onto the three table
extensions
if you would like to save this
configuration that you've done so you
don't need to repeat it again you have
the ability to import and to export this
definition into a Json file so you can
use it across the environments and
across replications
however if you're a large provider like
an icv and you're going to have many
people using the immigration mappings
that you're defining it's possible to
programmatically provide migration table
mappings by subscribing to on insert
default table mappings event
from codion 4001.
so if you do this true code then table
mappings are going to be inserted each
time when you complete the setup wizard
or if you invoke reset migration table
mappings action on the migration table
mappings page
before we move on there is one important
limitation that I would like to
highlight
so we have seen that some of the
partners have tried to do the following
so let's say that on the customer table
they have added a field to
and they already have the table
extension in the on-prem database
and then during the cloud migration they
would like to move this field from the
customer into the table extension
and they would try to do it like this by
specifying a migration table mapping
so if you do it like this it is not
going to work because the table
extension is now replicated from two
sources
and that is simply not supported by the
engine engine is not able to merge the
data coming in from two tables into a
single target tree
if you would like to unblock this one
you can either move the field to the
table extension on-prem
or you can introduce a new table
extension
and then Define the migration table Mac
most of the partners select the solution
tool because it's easier for them but
you also have the solution one in case
you need to use it
moving on to the next topic and that's
telemetry
approximately a few weeks ago we have
added support for the telemetry and we
have added a lot of events to the
partner Telemetry that you can use to
track a and analyze what happened to the
replication runs so you can see the full
list here we have also linked in to the
documentation Topic in the slides
so you can get notified whenever the
replication run is started most
importantly when it completes and if it
completed successfully then companion
tables you can get the Telemetry if it
was started and completed because in
some cases it would throw errors
then you can also get the status on the
upgrade events and in case it failed if
the recovery was completed successfully
and for the completeness sake we are
also tracking when you have disabled the
cloud migration
this part is quite interesting because
you can use it to build the power bi
dashboards to track the progress of your
Cloud migrations
the example that I'm going to show to
you you can access it by this link so it
was done by our pm and you can download
it so you can use it as a base to build
your own dashboards
to show you what is within this
dashboard
so if we zoom in
the first thing is of course navigating
to it so you navigate to the report by
selecting the cloud migration part of it
and then the first tab is going to show
you what is the status across
environments so if you're running the
cloud migrations for multiple
environments you can see what is
happening there and you also have the
link to the admin Center and also to the
client so you can quickly access the
environment itself
you can use the data to build some
dashboards with errors and the other
kpis so you can get a quick overview of
what is happening
and to think that I like the best
personally is the fact that you can
access the cloud migration lock so you
can see what is happening within the
environments without actually accessing
the client
so if you're running many Cloud
migrations I would invite you to try out
our power bi and to see if you can get a
nice overview of what is happening
across the markets
if you want to access the queries
they're also on the BC Tech GitHub so
you can use it to build your own
reporting
and these are the most important events
that you can use to receive the email
notifications so if you would like to
get email notification whatever the
replication run completes and when the
data operate completes or fails you can
subscribe to these events on the
previous busy Tech this event there was
a dedicated session on how you can set
up these alerts
I would invite you to watch the
recording of that one if you are
interested and we have also put some
documentation articles that are going to
guide you how you can set up the email
notifications based on the partner
telemetry
so that was all for the apartment based
Telemetry and now we are moving to the
new upgrade strategy topic
few months ago we made an important
announcement and we have also talked
about it on the directions and we have
published it on Yammer and we are using
this opportunity to repeat it because it
can affect some of you
if you would like to access the
announcement you can use the link on the
right to access it on the official
documentation site
in short the changes that we are
stopping the direct Outlet in Cloud
migration part from version 14. we
currently support the upgrade path from
14 straight into the latest version on
Prime and you can also connect the 14
database and directory Cloud migrated
into SAS
with version 26 unfortunately we will
need to stop this up report
this is in approximately two years so we
are giving you an early heads up because
we believe that to some of you this
ability is rather important
the reason why we need to do this is
because we need to clean up absoluted
fields and tables
we have not deleted anything from the
table schema actually from version 12
and across 14 versions no table objects
have been deleted
so far we have seven years of obsolete
removed objects and these objects are
taking around 10 percent of the database
we need to remove these objects so we
can save in space and the second reason
why we need to do this is because it is
affecting our delocalization effort
about moving all of the localized
functionality into the extension and
providing you a much better code
we have also received this request from
many of the partners to be able to
finally delete the obsolete removed
objects and to clean them up from the
schema which is something that we as
developers need to do and we all have
around seven years of scheme objects to
delete
the second effort which is being
affected by this is that we are looking
into moving the tables between the
extensions
so you will be able to push the table up
and down dependency chain and both of
these changes are actually quite
breaking for both upgrade and Cloud
magnification
we have received the request from the
partners to ship the ability to remove
the obsolete objects earlier before
version 26 and we are looking into this
we have not started the implementation
of this feature yet however the current
thinking is that it is going to work
like this
so we have a table in version 25 that
has been marked with oscillate remote
and also field that is marked with
obsolete remote and we would like to get
rid of them in version 26.
the only thing that you would need to do
is to delete the objects from the C the
second item is that you need to clean up
the upgrade code because now the
references are going to be broken and
the upgrade is not going to compile
and then the next step is to Simply run
the output and the engine itself is
going to check if the table and the
field has been marked with obsolete
removed and it is going to allow the
change then it is going to drop the
definition and remove the field and the
table from the SQL definition
so in short the only thing that you need
to do to remove the table in the field
from schema is to have a version in
which it is obsolete remote and then in
the next version you can delete it
we do not enforce any kind of schedule
to the partners regarding the breaking
changes however we as Microsoft we need
to follow the schedule otherwise we
would be breaking it
to understand better how this new
schedule is going to work this is the
visual representation of the changes
that are going to have
in year and a half the active version is
going to be 25.
and here the things are going to be
exactly the same as their current
you would still need to go to 14.
you can go from all of these versions
into version 25 and also all of the
on-prem versions are able to go straight
into sauce
as we are working on the version 26 we
are going to start with deleting the
objects so we will introduce the
breaking SQL changes immediately at the
beginning
you will be able to see what we have
done through The Insider builds and you
can prepare for the changes if you're
like
and then when the version 26 is released
then the version 25 becomes the junk
build
we will be forced to delete the upgrade
code in version 26 which means that in
order to get to 26 you need to go
through 35.
so all of these on-prem versions they
will need to operate to 25
and then from 25 to 26 as a separate
operate step or both versions 25 and 26
will be able to Cloud Market directly
now if you look further in the future we
are planning to do these updates every
five years
so in every five versions We are
planning to introduce a jumper build
when we start working on the version 30
you will need to update from version 25
to 13 and all of these versions will be
able to
call my red however when we introduce
the version 31 it's going to contain
breaking SQL changes
and then you will need to go to 30.
and then from 30 to 35
and all of these versions will be able
to go online it
during the session we got one really
interesting question that I would like
to raise here as well one of the
partners has asked us
if this picture means that the on-prem
is going to be supported at least until
version 35 and the reason why I would
like to highlight this question here is
to tell you that this thing that you
have just seen is our current thinking
and these are the things that we are
planning to do with the current
knowledge
the reason why we are sharing with you
is because we would really like to get
your feedback and to also give you an
early heads up about the things that we
are planning to do so you can adjust
and regarding the topic if the on-prem
is going to be supported until version
35. currently there are no plans of
stopping the on-prem support and if
there are any plans there are going to
be announced in advance
also the second thing is that it's
really hard to make any plans seven
years up in the future
so this current schedule that you have
seen it can change and in case of any
changes we are also going to announce it
to you so you can prepare in time
all right so that was all about the new
Apple strategy and the next topic is
plans for the future
for the plans for the future I'm going
to talk about our current roadmap and
all of the items that you can see they
are currently on the backlog and I will
present them
probably in the order in which we will
be delivering them to you
the first item is that we want to allow
you to specify the company batch size
when you're replicating the date
as you have seen during Julia's part of
the presentation now you can move
almost a limited number of companies
here in their application
so we want to allow you to be able to
specify if you wanted to move 30 40 and
50 in case you're limited by reset it
we also wanted the enabling to handle
these batches in an easier way and for
this we need to improve the UI
then the next item is to give you the
ability to include or exclude tables
from the cloud migration
currently we in Microsoft we decide what
is being replicated and what is not for
Microsoft owned tables and if you would
like to overwrite this decision you need
to do workarounds either to delete the
content from the table or to use some
customized solutions to move the data
like XML ports apis from Json import
expert
so in order to enable you to be more
efficient we are thinking about
including a new UI so you can overwrite
the decision that we made so if you
would like to move to change lock
entries
and maybe record links or any other
table you will be able to do this
without the need to write any codes
straight in the product
the only requirement will be that the
table is not marked as internal and then
you will be able to overwrite the
decision that we did
then the next topic is that we want to
improve the candling of all predatabase
tables so we do not replace the entire
table but to Delta sync it in the same
way as we are Delta sync internet media
the next item is that we want to disable
assigning intelligent Cloud permission
sets to all users when you enable the
cloud migration we have received
feedback from many of you that this is
quite disrupting
and that you also are not able to use
service to service authentication
because of this Behavior we are going to
ship these functionality as an expert
feature there will be a small action so
you can disable this default Behavior
for the beginning we will not disable it
automatically
we also want to add warnings to the new
UI
warnings functionality is one of the
things that is missing so we are going
to warn you if for example if the tenant
media table got completely replaced and
also if you have defined any table
mappings and no data was moved
if we see common patterns in the
mistakes that are happening during the
cloud migrations then we can extend the
Warning Systems with additional works
and last item that we want to add is to
add the ability to cancel the ongoing
replication
currently you can do it by disabling the
integration runtime in on the machine
which is hosting the integration runtime
however this does not cancel it in all
of the cases
so we want to give you a simple action
in the UI so you can cancel the upcoming
application
so this is our current backlog based on
your feedback and our thinking if you
have more items or if you have any
feedback to the things that I have just
presented please reach out to us
so that would be all for today for the
summary we have following
recommendations
so please consider migration from Azure
SQL if you have large databases to
migrate or otherwise you have to have
very strong on-premise setup
um also for the if you want to enjoy
longer periods of Delta sync then set
longer change track and retention period
and consider diagnostic runs to quickly
test your future implications
yes awesome you have seen from yulia's
part that the cloud migration tooling
can now support really large tenants
and we have shown you that you can now
move customized Fields with migration
table mapping and we would highly
recommend the setup Telemetry if you
want to be able to troubleshoot the
cloud migrations get notifications
through email or if you want to build a
nice dashboard
we would like to invite you to join us
on Yammer so if you have any feedback to
the content that you have seen today or
if you have any questions you can reach
out to Julie and me on Yammer we also
have many other partners which are on
this channel that are helping out so we
would strongly recommend that you join
us here
thank you very much for your attention
thank you
