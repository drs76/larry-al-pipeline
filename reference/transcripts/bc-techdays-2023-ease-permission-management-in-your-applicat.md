# BC TechDays 2023 - Ease permission management in your applications, levering the latest permission..

- **Source:** https://www.youtube.com/watch?v=5uqWdHPGhb0
- **Video ID:** 5uqWdHPGhb0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 41m27s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

well I'm super happy that we just saw
the Rich Text Editor being made
available I think it's about five
releases ago something where kind of
sort of promised that we're going to
make that available as a standalone
component
two and a half yearly years later here
we are is finally in the product I'm
super excited about that
um but we're not here to talk about
client anymore we're here to talk about
uh permissions
so um well maybe a quick introduction
I'm yes I'm the engineering manager of
the application Foundation team and one
of the areas that my team has been
working on is permissions and it's an
ongoing story actually we've made
incremental permissions improvements
over the past I think four or five
releases or so
um so yeah I'm happy to show you today
kind of in a sort of
best off session what we have been doing
been doing and to help me with that I've
got Steve yeah I'm a software engineer
at the application Foundation team and
I've been doing a lot of the permissions
work yes
all right uh behind this you see fasten
your seat belts because we have tried to
squeeze everything into 45 minutes we
have pre-recorded some of the demos to
really make sure that everything works
smoothly
um so if you're having problems seeing
or something just move on closer or you
know we'll or you can watch the
recording if it's like too too fast or
something
um let's jump into it what do we want to
show you today
so first of all we're going to take a
look at composable permissions Steve is
going to start developing a little app
for you where we're going to make use of
composable permissions to show you how
to really you know make use of these new
features
then I'm going to talk about inherent
permissions a new way how you can reduce
the size of your permission sets
and then Steve is going to continue to
work on our little app
um and you know show how to how you can
exclude permissions
then we're going to go over to something
else or implementation of security
groups on business Central environments
how you now can Nest these security
groups how you can use security groups
within business Central to ease the
administration of business Central and
uh and permission sets
which and all of this then leads to the
deprecation of user groups
which now are a redundant concept so
we're going to get rid of those
and then finally we're going to quickly
look at how can you actually look into
Telemetry to make things better
Steve let's get started composable
permissions so first I just want to
recap what a composed permission set is
so a compose permission set is quite
simply a permission set that contains
permissions from other permission sets
so here we have the example with the
blue permission set at the bottom that
includes the permissions of the green
permissions set and the orange
permission set as well
so essentially you can include other
permission sets in your permission set
and let's jump straight into a demo and
create a demo app and then we'll create
some different permission sets and we'll
see how we can include those different
permission sets
um in in our app
all right so I'm here in business
Central I'm going to go to the users
page
and we see that we have two different
users we have Jesper
which is super
this is the admin user PC admin and then
we have Jesper here which is also super
we want to change that that's too many
permissions to give to a regular user so
we'll create a new permission set from
the permission sets page
and we'll do that now by copying the
permission set
but we see that we have some options
down here we'll call it my d365 basic
and then we can see we can do a flat
permissions copy a clone but we actually
want to do the copy by reference which
will just include the 365 basic we don't
need to notify
and that's it we've copied the
permission set
and now we can go ahead and assign that
permission set
so we'll remove super
and then we'll assign my d365 basic with
no company
we'll go to permissions and here we can
see that it includes the 365 basic we
can expand that and see what other
permission sets that include
and then we'll go back
and we'll just verify that now we have
those permissions so we'll sign out and
we'll sign in again
and now we see that the permissions have
been reduced
so now I think it's time to to create
our demo app as we can see there's
nothing installed yet
so let's jump into visual studio and
actually set up our team web
first we wanted to create some data so
we'll create PD data this is our data
table where we'll store important data
and want to control permissions on this
so we have a key and we have some data
and this is the data that we want to
control permissions on
then we have a setup table which might
include some setup that we need and
stuff like that we just keep track of
whether the feature is active not a
great design but we'll go with that
and then we have the logging table where
we'll lock some information
about the last execution
so that's what we look here
so that's our data of course we're going
to need some initialization as well
so we have this PD init code unit and
here we'll set up submission
initialization code
so all that we do here is basically init
a record set the feature to be active
and then we insert it which will require
insert permission
and then we'll do the logic
so we'll do that in the form of a report
and here we have at the top we have some
properties that we don't really care
about and then let's look at the on post
report
so first we check if the feature is
active otherwise we activate it this
requires setup and sorry read and insert
then we do the process data which
requires permissions to PD data then log
an event which requires insert
permissions to a logging table
and then we show the data which requires
again PD data permissions and then we
have at least our admin scenario which
requires PD log read
so actually reading from the log and
just to quickly go through the message
check active does it get and then it
calls the init app which we just created
in our code unit here
then it exits
then the process data simply just insert
I had permissions to insert this but
this would be the data we care about
controlling permissions for
and then we lock the event where we just
set the last execution and insert that
showing the data is just
throwing a message with the count in PD
data
and then showing the last execution is
our admin scenario where we say that you
need admin privileges and then we do a
find list and we do a message showing
the last execution
so that's pretty much our app we'll
deploy that
and then we'll try to run it
I wonder if that will work
and not surprisingly we get a permission
error we don't have insert permissions
and that's because we didn't set up
permissions in our app so we're going to
go ahead and create some different
scenarios for permission sets we need a
user permission set and an admin
permission set so for our user
permission set we'll go ahead and we'll
have a snippet here
which gives permissions to read insert
modify on the PD data
and of course we want to be able to work
with the data on the user
then it also gives read and insert we
don't really want to give insert but it
has to do it because of the setup
and then for the log table we just give
insert we want everyone to be able to
write to the Lux
then we can go ahead and we can extend
this permission set onto basic that we
already have assigned to a user
so we'll do an extension
where we include PD user in d365 basic
and we'll save that and then we'll
create an admin scenario permission set
which is assignable and public and it
also
um includes pdus permission set and then
we give the rest of the permissions rimd
to the two other tables
so we deploy that with the permissions
and now we should see that we're able to
run the scenario
so we'll run the demo app again
we get the number of Records in the
table as expected and if we try to run
the admin scenario well we don't have it
assigned so we get a permission error
how can we then fix that with composable
permissions
well
um we as we saw we created this admin
scenario that's assignable true so we
can actually go ahead and include that
in our permission set
so we'll go to the users page on our
admin user
we'll go to esper and we'll go to my
d365 basic
and
we see here that it now includes PD user
permission set
but we don't have the admin one assigned
so if you view the permissions as here
we can see that this permission set does
not give read permission to the PD log
foreign
we can also review the full permissions
of my d365 basic and see that it's the
same permissions as we defined in our
app
that we don't have a read permission
here
so now we can quite simply include
another permission set so we'll here
we'll select our admins permission set
PD admin
and now we've created a compose
permission set here where we also have
the PD admin permissions that included
and this one also include PD user
so if we view the permissions of this
we'll see that this one defines yes for
all of these
and it includes pdus as well
we can also view the permissions in this
set so this is the composed list of
missions and here we see that we have
everything assigned
and now just to verify that we have the
permissions we'll run the demo one more
time
and we get the number of records and now
we should be able to run the admin
scenario and we will so with that we set
up a compose permission set and we used
inclusion of other permission sets to
give our user access to more data but I
think we can actually improve our
permission sets even further yes let's
take a look at the next thing
I want to talk about inherent
permissions
um
so this is something new that you can
start using now it released with the
2023 wave one the second portion of
inherent permissions and what we're
basically trying to do is to give
you the developer the ability to elevate
user permissions in a given code context
what that means is that um
you can either Grant specific
permissions for the context of a method
for instance or you can now also Grant
it on object level there might be
certain objects where you're simply not
interested in controlling permissions
you will now be able to give inherent
permissions on these objects and then
they are out of the equation
and what this does is actually it puts
the power into the hands of the
developer and kind of eases the burden
on the administrator because you know
the less permissions the administrator
needs to manage well the easier the
administrator's job is right and the the
developer too sometimes just knows you
know if it's a buffer table or if you
know uh you know certain types of tables
or even code units reports and so on so
forth you don't really need to control
permissions on all of these objects so
um this is what we're trying to address
um
so yeah no longer need to add these to
permission sets and we're hoping that
this will give you more clean and
comprehensible permission sets
and also what this can potentially do is
to improve the stability of critical
code paths so if there is a code path
where you absolutely must have these and
these permissions
previously if the system admin somehow
forgot to Grant you these you would
maybe even not be able to log into the
system now with this you can ensure that
you always have the right permissions
so let's take our little oh yes no this
is important you can only use this on
your own objects So currently there is
no way that you threw a PT for instance
can grant permissions through inherit
permissions to other apps and that's of
course for security reasons
so let's continue to work a little bit
here on our demo app
um
so uh in order to to uh to get started
here let's reset a little bit
um first of all I don't want to be an
admin anymore let's remove that again
no more admin
and next of all quickly into you don't
need to see this this is tiny but uh um
we go into setup data and delete our
setup record again because we want to
kind of restart as if the the app was
newly installed so delete at the setup
record now it's again like it's freshly
installed
so now let's take a look at our
permission sets you remember our PD user
permission set
where we had this insert permission for
instance for the setup table we don't
really want to have that but we needed
to give it just for the initialization
of our app right else it would fail as
you saw in the first demo
so now if we remove this
um you know just to quickly prove it
again
now of course the the initialization
code would run and this is what I would
consider a critical code path and you
would get a permission error
which is kind of unnecessary so how do
we go about
actually sticking to this permission set
but making it work
and this is where our inherent
permissions come into play
so we have this init app and whoever
runs it should be able to initially
initialize the app it doesn't really
matter who you are whether you're a team
member or an admin so we do give the
inherent permissions
um so everyone in the scope has insert
rights
and now if we
try to run our little demo app again
we will succeed
there we go
but that's not all
um so now we got rid of this one
permission that we no no longer need to
administer so that's pretty cool but
there were some others so let's go back
to our permission set here
oops uh let me open that again
so you see there's also the
setup and the log table that we aren't
really interested in controlling we are
interested about the data so if we now
reduce our permission set to only
have the data permissions that the admin
administrator should control then how
can we get rid of these others and this
is where inherent permissions in
metadata come into play
so for a setup table every user should
kind of be able to read from this right
so we can say inherent entitlements not
so important but inherent permissions in
this case so now everyone gets to read
from this table no matter who you are
and the same kind of goes for lock here
we are interested in controlling who
reads from Lock that's only the
administrator
but everyone should be able to write to
log tables right so why not just make
this object give it inherent permissions
insert so that you no longer have to
control these insert permissions
so if we now go ahead compile and
publish this little app
which takes a minute here
and we now run our demo you will see
obviously it still works that's lucky
for us
um
but the cool part is if we now go over
into our admin role Center here and we
open up
my permissions
there goes Jasper
see now if we if we take a look at our
permission set
here
PD user PS
and review what's in there
and now it's only this one permission
that we are actually interested in
controlling that is still in our
permission set which makes this a much
cleaner much better permission and if we
go into uh into effective permissions
and let's just change the user here and
toggle show all objects
so of course we want to see that you
still have these permissions and this is
something that is actually not yet
released um but in a I think in the next
minor update this is going to come so
now if you see at the effective
permissions you will see that there is
actually inherent permissions down here
right it says Source inherent so you can
still see ineffective emissions that
these users do have permissions to for
instance insert interlock and read from
setup
um
yeah
so that was kind of what I wanted to
show here so inherent permissions we
have great hopes that this is going to
simplify the entire permission system
quite dramatically
we've also started using this ourselves
just a little bit
this was rather new when it came like
very late in the in the release these
inherent permissions so we didn't have a
whole lot of time for for 2000 2023 wave
one so what St here did is that he went
into the login permission set and try to
reduce the login permission set just to
show you the power of inherent
permissions and I just very very quickly
want to show you where like what that
looks like so if you in the latest
release go into
uh permission sets and you for instance
pick the login
um here the login permission set
and then we do some drilling because
this is obviously a composed permission
set so it contains a contains many many
small permission sets so let's go into
the system
application edit and then there should
be a view
and then there will be an object
here read
so it's very very nested but we started
with these system application objects
now if we take the first module here the
aid user management module from the
system application now what it looks
like in the current releases there are
two permissions there is a code unit the
API code in a page those you might be
interested in controlling permissions on
so those are still left but if you go
like one version back in the version
21.4 and you take a look what it looks
like there
you will see that the permission set is
just vastly more complex it has many
many more objects and you'll find stuff
that you would never be able to never
would be interested in controlling like
all of these code units you know
implementation code units it's all this
thing that previously cluttered The View
for the system administrator he had to
kind of you know figure out what is this
do we need permissions for these in
reality there's no point in that
um so now we can get rid of these which
I think is a very very cool feature
so but what if these permissions that we
now provide out of the box or that the
app spread of the Box aren't completely
right what should we do about that Steve
yep that's why I exclude exclude from
permissions come in because what if the
permissions that are defined by
Microsoft the isoes are not fine-grade
enough for you and what if they include
too many permissions should you then
copy the permission set no you'll then
end up having to synchronize the
whatever the copy permissions so instead
what you'll do is use in exclude
permissions
so the mental model for how exclusion
works is that you calculate the list of
included permissions then you calculate
the list of excluded permissions and you
subtract those and then you get the
final permission set yeah so very
important this is not at an eye
permission you can subtract from a set
you cannot just say all up something is
forbidden yeah
and excluding entire permission sets is
the same principle you'll just exclude
every single permission in that set from
the original set
so let's see how we can do that in in
the product
um with our app
so
we'll go here to the users page again
we'll open up Jesper
view the permissions
and now we see that we actually included
the PD user permission set here in d365
basic
but we can actually exclude the
permission still by just adding a new
exclude line
and we'll select exclude for all the
permissions
and this will effectively remove that
permission from the permission set
and just to verify that we view all
permissions and we search for the object
and we see that it's not there anymore
so we now effectively removed it from
the permission set
because of how we structured it we can
also do it in another way because we can
actually just exclude the entire
permission set so here PD users
permissions we can just press exclude on
that
and then you see a new exclude line over
here and you see that basic is now
partial because this is excluded
and just to verify that the user no
longer have permission we'll try to run
the demo app and we get a permission
error
so
this is pretty much the way that you can
exclude any permission from an existing
permission set and it gives a lot of
power to you in order instead of having
to create your own permission sets that
are based on other permission sets you
can use the original permission sets and
just modify them a bit to your logging
furthermore we also introduced in Wave 2
of business Central
um 2022 we also introduced exclude from
wildcard permission and this is a very
powerful feature because it allows you
to exclude objects such as pages and
reports um
um from permission sets that include
wildcard permissions so now you can
effectively it gives you more power
because you can effectively Grant
everything as most of our permission
sets do for for execute permission you
can grant everything and then you can
say accept this one and accept this one
so it's a new way of controlling
permissions
and I think that's it for
all right so switching over to a
different topic security groups on
Business Center environments we've tried
to make the entire Administration part
of permissions easier maybe especially
for for larger companies that have
multiple environments
um so what we've done is that we have
improved the update users from Microsoft
365 action on the users page which now
respects if you set a security group on
a business Central environment
previously if you would sync it would
just sync all the users and disregard
the the setup of security groups on your
environment
um so this actually empowers you to set
up the system prior to user login
previously the users had to log in to
get created
um and basically what we do is we just
iterate over the users which belong to a
security group so what does that look
like
um in business Central we have
a couple of users
and um
let's go over here and let's try to set
a environment a security group here
so if you
um if you want to have a security group
you need to create one first so let's go
over to active teams and groups and over
here you'll find a little button called
security and we can say add Security
Group and pick the security option here
then we give it a name let's for
instance call it BC access because this
is the group that will add the users
that should have access to our
particular environment
and we say create group and then after a
second we have our Security Group
and we can now add a user to it
um we go to members we say view all and
then we say add members
this list takes a little bit of time to
load because we have a lot of of users
in this environment
but once it's loaded we are free to pick
all the users that we'd like to have
added to this group
in this case you know doesn't really
matter which one we take let's take the
full user admin as the one user that we
want to have left on our environment
that can access it
and we click save and again this takes
just a little bit of time
and we now have a full user admin in our
access group so now we can go back to
our admin Center and we can I just
quickly need to refresh this by clicking
on environments and we can go back in
our production environment and now we
can Define the user Security Group and
we pick our BC access
and what we've now defined what we've
now done is that now only users in PC
access will be able to access and if we
now do the update
what it will do now is it will remove
the plants from all the ones that are
not part of this group so you see all
the other four users get removed or the
plans get removed so now it's only our
full user admin that gets to access the
system
yeah so that was that
um one more thing that we did is that we
added support for nested security groups
um
kind of give you the ability to group
One Security Group under another so that
you can have a like a structure
um
and again this very much simplifies the
setup and maintenance of security groups
because now you can actually have your
say business Central Sales Group under
access
and still allow that group to get access
without having direct without directly
being a member of the access group
um so let's quickly take a demo on this
because this is easier demo than it is
to explain it
so in the meantime we've created a
purchasing group here
and let's also go right ahead and create
a sales group so we create another
Security Group here which we call
sales
so this is uh now we have our setup we
have our access Group which is for the
environment and we have our two
organizational units here sales and
purchasing
and of course we also need to have some
members in the sales group so let's
again go into members and add members
and again this takes just a little while
to load
um and again let's just pick you know
accountant will do and the team member
this doesn't really make any sense but
let's take these two users just for the
fun of it
and
now what we can do if we also want to
Grant the accountant and the team member
access to our environment is we do not
need to add them any more individually
to our access group here we can just go
ahead and add the entire group
so if we say add members and we now
search for
for sales
you will now be able to add this you
were able to do that before but business
Central wouldn't care
[Music]
so
you would have to add the individual
users to the access group 2 you no
longer need to do that so now if we add
these two groups to our access group
they will still be respected
so by doing that
now we have the full user admin
purchasing and sales as part of our
environment so now if I go ahead and I
update users from Microsoft 365.
then when we click on next this takes a
little while
you will
see that we will append uh well just
just append all three of them we don't
want to work with permissions right now
there we go
they will all get a plan again so now
they are back at business these three
users that are part of the other two
groups
all right that was nested security
groups
but we did some more with excuses with
security groups right yes because
security groups and business Central you
can not only use it to control access
you can also control permissions in
business Central using security groups
so we actually Integrated Security
groups right into business Central and
now it allows you to control permissions
using security groups
so this will allow administrators to
manage what business Central permissions
you get based on the Azure portal for
SAS are based on Windows groups for
on-prem
so effectively this adds new
functionalities to control matching of
aad security groups or Windows groups to
business Central permissions and this
will allow you to just move one user
from one group to another group and then
effectively change their permissions
inside business Central
may be very important to notice that
this is optional you are not forced in
any way to use security groups but if
your organization allows you to or it's
good for you then you can yeah so show
us what you got yes
so let's jump straight into the demo
and let's go to the new page security
groups
and there we'll create some new security
groups
and we're able to select from the
security groups we have in aad
here I'll select sales press OK and that
will create it in business Central
so we'll just take a little while and
then we should have the security group
created in business Central
we'll do the same for the purchasing
and on-premely the windows user groups
here yes exactly great
so we create that
and here you see the member is already
here BC essential is part of purchasing
and we can then manage the permissions
for the security group so here I can
assign my own permission set for the
purchasing group
so my d365 purchasing
and I could do the same for the sales
assign permissions to that Security
Group
my d365 sales
and now you see here the permission sets
and the members that are part of that
and then we can go to license
configurations to ensure that new users
don't get any permissions assigned by
default so any essential user I don't
want them to get any permissions because
they get them through the security group
so I'll remove this blank it out
so that now any new users don't get any
permissions assigned directly to them
then we'll set up a new user
with an essential license
super quick
right here
and we'll just assign an essential
license to this user
so now this user won't get any
permissions in business Central based on
this license but this but by adding them
to a security group they get access
through that
so we'll add them to the Sales Group
find that user
edit and now it's part of this Security
Group
so kind of the entire permission setup
was now done inside the admin Center
rather than in business Central if
that's what you're going for exactly
so yeah here we've set it up in business
Central and now if we go to the users
page and we update the the users
we can we should see that we'll
synchronize the user
we don't actually have to do the update
the user would be able to log in just
right away obviously but this is just to
show that it works yeah so we get the
new user here with the plan
so we'll add that to you sir
and then if we look at that user we see
quite interestingly they get permissions
from the permission from the security
group because they're part of this
Security Group
but the user don't have any permissions
that's assigned to themselves
but still we should be able to log in
with this user
maybe also while this loads you can make
a hybrid where you get certain
permissions from security groups and
others directly assigned if you're in
for like that kind of setup
so it's pretty flexible
yeah and just look over to the vendors
page to make sure we have the right
permissions and we see we don't have
vendor permissions because we were
assigned to the sales Security Group
so that's the idea of how you can use
your groupings in Azure ad or in Windows
security Windows groups to control how
permissions in business Central assigned
yes
all right yeah getting to the end of
this
um how does this work on Prem it works
exactly as it does in the cloud except
we have no support for ad security
groups
um if you think this is important create
a PC idea and if there are enough votes
then we will might be going for it but
out of the box we don't have it yet we
only support Windows groups
now um almost the end of the session uh
with all of these Concepts that we
introduced today
um there is no need anymore for user
groups user groups are part of the base
application so they're anyway falsely
positioned you could say
um so we would have had to move them
into the system application sooner or
later also the concept is simply
redundant now you can Nest permission
sets which was one of the capabilities
of user groups previously on-prem you
could link user groups to Windows
user groups which you now can do through
security groups which is why this no
longer is needed and while this is
sometimes hard for people that are used
to stuff and need to relearn things then
I think it's easier for for a new
business Central users to only have a
single concept
um so we're going to streamline and
simplify the permission management by
getting rid of these user groups
and we've done so obviously by
deprecating
we've tried to make the transition as
easy as possible so we've created a
little wizard
um so let me just very quickly show you
how that works if you go into users in
this setup you will see we still have
plenty of permission sets
and we will also have a user group
membership my full access let's remember
that one my full access we got through
user groups
so if we now go into user groups in the
latest version you'll get this
notification of course see the user
group
and all the permissions that are part of
this user group and you will see the
notification that this feature is
getting deprecated and you can actually
go ahead and activate that in feature
management
activate the duplication that is so if
you do this we will open a little guide
for you
and that guide is gonna
help you transition away from user
groups and it should ideally work fully
automatically if it doesn't we would
very much like to hear from you because
this should be painless ideally
so there are two options let me just
maximize this there's assign permissions
to members this takes the flat list of
permissions and assigns it to the member
or we can convert to a permission set if
you like user groups I would actually
advise you to use the convert to Herb to
a permission set because then the the
structure of the user group remains
intact
so let's go ahead and convert our user
group to a permission set
we click finish here
and that's actually all it took and of
course if you have many user groups you
can convert them all at once so now we
see at our Essentials user that there
are no more user groups but there will
be a permission set on the user now
which is my full access
and if we go into permissions
the permission sets here and we look at
the
is actually on top my full access
it has the exact same structure
as the user group used to have
so nothing is really lost
um it just now is a permission set
rather than a user group
um
yeah that's kind of kind of the gist of
that and of course if we go into user
groups now after the conversion there
are none left which is kind of what we
went for
so
that should hopefully be easy we've had
some questions with what happens on-prem
if it if there are users that are
windows groups and they didn't
automatically
get created as security groups this is
something that we will look into if we
indeed have a book there so you know and
if you find other issues that make your
life hard let us know because we do want
to make this painless
one final thing before the first break
we will talk about Telemetry yes we
can't have a good session without
mentioning Telemetry so of course you
can use Telemetry to troubleshoot your
permission issues if you go to errors
and permission errors then you can see
for example which customers experience
permission issues what errors do they
see and which apps and objects do these
errors come from
so you can use this to to look at
permission issues and troubleshoot those
but you can also use it to track changes
to permissions so
um if you if you look here you could see
what which permission sets were changed
and you can track that you can also look
at which apps actually change these
permission sets and you can even go down
and look exactly at win with the
different field changes made so these
are the type of things that you can get
through app insights and Telemetry for
permission sets
yeah that is kind of what we had for you
so we hope that with all of these
little features you know composable
permissions inherent permissions exclude
from permissions that's all the security
group improvements that we've made and
finally the duplication of user groups
that you now have a toolbox that is just
enables you to do better permission
management because let's just face it
the past 15 years it has been quite the
struggle
um so we hope that this works our next
work is obviously to you know take our
own medicine we do want to start using
this to a much higher degree the biggest
problem that we have is obviously the
base application which is just one big
spaghetti mess so using this is very
very hard so we're going to start using
these features as part of our continued
componentization efforts of the base
application
um so you will see this in the center of
everything new that we built and I would
encourage you to start using this as
well in your apps it will make your life
and the admins live Easier
um this is a super difficult topic and
I'm also very happy that you stayed with
us here this morning uh it's a rough
start to the day but you know if you
have questions like later on you know
how to use that we're always happy to
help reach out to us on Yammer uh find
me on Twitter
um you know
if you are if you still think things are
missing
um lock your ideas we're very eager to
get your feedback there
um and if you think you know oh we need
to learn much more about this we're also
happy to host office hours just let us
know what we need to do to make your
life with permissions a little bit more
less painless less painful
yes that's what I want to say
and with that thank you very much for
listening
um
have a good day
