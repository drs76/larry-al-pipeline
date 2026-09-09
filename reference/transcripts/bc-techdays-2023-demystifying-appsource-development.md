# BC TechDays 2023 - Demystifying AppSource development

- **Source:** https://www.youtube.com/watch?v=uIxV14TEA2s
- **Video ID:** uIxV14TEA2s
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 48m13s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

let's have a look now at how to create
your create your offer in partner Center
so you've set up your partner seller
account and now you can go to
partner.microsoft.com that's where
you'll see your Marketplace offers and
if you go to this you'll have the
ability to create a new offer and you
have many different products listed
there but of course we'll have a look at
business Central
once you've created your offer and
specify the name for it you'll be
landing on this page and this is where
you'll start setting up your offer
the first important decision you have to
take is what time of package type you're
deploying there are different ways of
extending business Central capabilities
the first one is add-on app so those are
the those are the more traditional Al
packages that you're all working with
but you can also use connect apps and
those are point-to-point service
connections so usually extending
business Central functionality through
web services all the data or other
similar functionalities in this
presentation we'll focus of course a lot
on the add-on apps but it's important to
note that you have Alternatives there
the next functionality that you have
there and you might have seen it in
other presentations today already is the
ability to sell through Microsoft so we
have now the ability to directly
monetize your app through the appsource
marketplace without building too much of
your own licensing mechanisms but for
now I'll just say no to this field and
I'll choose to Define my own one we'll
go back a bit later on how to set it up
so if you specify that you do not want
to sell through Microsoft then the next
choice that comes to you is what type of
listing do you want to have and how do
you want people to interact with it if
you choose get it now your apps is then
free to be used it's also a good
approach for you to have a freemium
approach if you want some
functionalities to be paid for you can
also specify that you want to have a
free trial then in that case you will
have to build your own mechanisms to
restrict the number of users or of
transactions there
the last thing that you might be using
is the contact me offer and this means
that the app cannot be directly
installed from the appsource marketplace
on the customer environment but the
customer will have to provide some
contact information and then you will
get back to them helping them set this
up and that's usually something that we
require for connect apps because those
ones require some manual setting and on
just an Al app that we can deploy on the
environment
on this tab you'll also have the
customer leads so that's very related to
what we've just discussed now around
Connect app and contact me this is how
you will specify
the service that you will use for
receiving the information from your
prospects on appsource that will enter
their contact information
if we move to the next tabs you'll have
some fields that impact like how your
app is classified in the marketplace and
how it will then be discovered by users
and you also have an app version field
this one is a version that has to match
the version that you're specifying in
the app.json of your app so if you're
using an add-on app every time you
update the version there you'll also
have to update that field
if we move to the next tabs you'll have
all the marketing materials to set the
first one and pretty important one is
the name again that has to match the
name of the extension that you're
uploading in the marketplace
and you have also the ability to Define
some other marketing materials
everything you're specifying there will
be reviewed by some validation teams and
they have some advices that we sharing
to you today
um the first thing is uh look like you
need to pay attention to how you're
referring to business Central the first
time we're asking you to use the
explicit name for a Microsoft Dynamics
365 business Central later on you can
use one of the shorter versions
available on screen
you're also required to provide in your
file description the list of countries
and languages that your offer supports
you'll also be asked to not include any
of the business programs or eligibility
that you're part of even if you're proud
of them and would like to include them
um and then a little bit later you'll
also have the ability to set up
marketing materials there that include
screenshot videos and anything that can
make your offer attractive for potential
customers we have a lot of guidelines
online whether they're from business
Central or from the app Source
Marketplace in general
um but it's important there that you are
mindful of the copyrights and the
trademark materials that you have this
is one of the common reasons for which
submissions are refused on the marketing
validation and we know from experience
then fixing those marketing materials
takes time and it's one of the main
reason why offers are being delayed when
they go to appsource
on the next step you'll have to space if
I which markets your app is targeting
and those are the different countries
and regions uh for which your app would
be available in business Central and
again this has to match the list of
countries you're specifying in your for
a description any mismatch will cause a
failure of the submission
on the next tab this is where you'll
have to upload your dot app files for
your extension the first entry here is
the main extension so the one that is
tightly coupled to the offer as
mentioned earlier the name and version
have to match with the other fields that
you've already set up and the publisher
of that extension has to match the one
that you're using in partner Center as
well
you then also have the ability to
specify some dependencies some libraries
here either as a one.ap file if you have
only one or as a zip that contains one
or multiple ones and it's important to
note that from our point of view one
offer is one main app and its
dependencies it's not just a combination
of unrelated apps they have to be linked
together
and here is an example you could submit
your main app that has that requires
them to three libraries in order to
compile but if you upload as your zip
file a fourth one that is not required
by the main app or any of the libraries
then it will be ignored and won't be
validated by the service
of course if you know that some of those
dependencies are already published in
appsource through a different offers
then you do not have to specify them
there the service will automatically
resolve them and use them for you
next up will be pretty fast to cover so
supplemental content this is a tab that
is pending removal and all the
information that is there are currently
not used by the service so you just need
to specify some value to satisfy the UI
some of the fields are asking you to
upload a file as long as you have a file
that have the right extension it will be
fine for us so just specify something
there
you might be wondering now if the target
since the targets release field is
ignored how do we select which are the
releases of business Central that you're
targeting with your offer
we've seen from experience that current
next Miner and next major could be
ambiguous depending on what time of the
release process for Microsoft VR if a
new Miner or major is along the corner
or if your customer is an older version
that might not be very obvious what this
means so we decided to replace it by the
application property in the Manifest of
your apps
um and if we take an example here with
21.0 set it means that the app will be
validated from 21.0 and higher releases
until the latest one at the time of
submission
this also means that your app will be
available for environments on those
versions it won't be available for
environments that have a lower version
of business Central
and as a side note 30 days before the
release of the next major we are also
validating against this upcoming major
because we want to push all appsource
Publishers to be ready for the next
major so the customer can upgrade as
soon as possible whenever they have the
possibility
if you have multiple apps in your
submission then we are Computing what
the target releases as the maximum of
the application versions for all of them
so as an example if your main app
targets application to anyone but you
have a library that targets application
22 then what we will resolve as the
target for the submission is 22.
okay with this we went through all the
different fields in partner Center and
you should now be ready to to get it
right
um the next thing you'll have to do is
preparing your app for appsource so one
scenario uh is that you might have a
Pity and you've deployed on a few
customers you've been pretty successful
with that and now you'd like to expand
your business by going to appsource
there'll be a few changes that you need
to do the first thing that you might be
doing is setting up a new uh Source
control representory for your app so
that everything is there
but then we'll ask you to get a new app
ID
and this comes from some limitations in
the service currently pts and appsource
apps cannot share the same app ID as
soon as you will upload an appsource app
with that app ID PT is using the same
app ID cannot be uploaded anymore and
that might be impactful for your
customers because they might need to
receive updates for that pte and we're
receiving often support cases about it
so be mindful about it change your app
ID when you're moving to appsource
the next thing you'll have to do is
enable to enable appsource cop so you
can do this from cicd pipelines you can
do this from vs code using some of the
settings here we had other sessions that
talked about the improvements done to
the code analysis framework so this is
related to that appsource cup is what is
used to verify that your app is meeting
the requirements for the appsource
marketplace so if you're able to pass
the validation of the app Source cup
locally you'll be pretty likely to
succeed in the partner Center as well
as part of the app Source cop setup
you'll have to create an appsource
code.json file and this one has some
additional configurations for the
appsource cup for instance the field on
mandatory affixes this is where you'll
specify the ethics that was registered
for your publisher name and you can also
specify the list of supported countries
so that appsource cop can also verify
that you have translations for all the
language languages supported in business
Central for those countries
and once you've done this you'll have to
start fixing Diagnostics
so let's have a quick look at the
changes you'll have to do to fix those
Diagnostics if you have a pte and the
Manifest look like this the first thing
you'll have to do is change the app ID
to give your app a new identity and make
sure you won't get into the problems we
discussed earlier you will have to also
feel all the all these fields that are
not mandatory for pts but that your
customers can get a great experience and
have privacy statements and so on you'll
have to change the ID range that you're
using to match the app Source
Marketplace requirement and get the one
that was assigned to you if you're not
using the application property you'll
have to start doing it now because
that's needed for knowing which fees
have been essential you're targeting
this is not a requirement but we highly
recommend you to review your resource
exposure policy when going to appsource
you will have a much broader audience so
you might have to think about how you
want to expose and protect your
intellectual property so have a look at
the resource exposure policy and the
last thing you will have to also enable
translation files
if we look now at some sample of code so
here very basic page extension you'll
have to do some changes as well you'll
have to change the ID that you're using
to match the ID range you'll have to use
affixes on all your objects you will
also have to use affixes on all the
members of your page extensions objects
table extensions objects report
extensions
we will ask you also to move away from
the multi-language properties such as
caption ml to use the label ones such as
captions so that you can use them
through your translation files and we'll
also recommend you to move away from
errors and messages that are just
hard-coded in the in your code and use
instead label variables so that you can
also translate them with translation
files
the next thing we'll ask you to do also
is to think about how you want to
structure your offer in terms of
libraries but also in terms of Market
expansion layer if you're targeting one
country now you might maybe want to
Target more in the future
and this has to be taken into account
especially because Microsoft apps at the
moment are localized meaning that they
can have different content depending on
the country regions you're targeting
this is not something that we allow for
appsource apps that's the case for some
Microsoft apps because of Legacy reason
and we're working hard to fix it
and we can have an example now of how
that can cause issues for you if you
have an app that you've pushed to
appsource for let's say Canada and it
has a mix of objects that are specific
for Canada and for W1 the common
localization for all countries it will
work fine on Canada but as soon as
you're trying to move to another country
some of the references will be resolved
some others will not and it will fail so
that may cause you some issues we know
from experience that this type of
refactoring is hard to do when you
already have customers life so try to
think about it ahead of time and one
simple way of
like one way of doing it is to extract
some of your dependent live the common
objects into some libraries and then you
can have offers that are specific per
country it's just one approach there can
be other ways for you to consider this
but take it into account before going
live and starting to have too many
customers
another recommendation that we have is
to enable Azure application insights
you've seen it also in many
presentations here we are heavy heavily
investing on this to provide you a lot
of information so you'll have to create
your app insights resource in Azure and
then you can specify it on the
application inside a connection string
of your extension and this has many many
benefits for you you can get data on
your features you can get errors when
you're after your app goes live you have
also now ai insights into this you can
also use it to dive into the results of
your appsource submissions which we'll
discuss a bit later on and there are
many other cases there
just showing you one of the many power
bi reports that you've seen in other
presentations now showing you the offer
listings for them in appsource we have
many reports that you can install they
have all the right queries for you nice
visualization so it should be pretty
easy to get started
the other thing that we'll uh ask you to
do when you go to appsource is to be
mindful of how you're handling your
secrets if you're using API keys or
anything else Azure key vault is great
for that do not keep plain text secrets
that's not something we would recommend
because it can have some potential
security risks in order to enable the
usage of key volts you'll have to first
push it up to appsource and then you'll
have to go through some registration
process that is documented here and then
we'll validate that you actually own the
key vaults that you would like to
register for your app and after that
you'll be able to resubmit using do your
keyboards set in the key Vault URLs
properties so you can have multiple
keyboards set there
and once you're done with that we have
some code units that you can use in the
system app and base app to make it easy
for you
the next thing that you might want to do
on your app is to also enable
monetization so we have here an example
from one of the our example apps on the
app Source Marketplace
and you can see that it has different
plans those plans can have different
payment plans so monthly or annually you
can have some users different prices the
some of those plans can be private to
some specific customers some are public
and available to everyone so many
functionalities there
so this is currently like a new feature
it's in public preview it allows you to
purchase your customer to purchase the
app through different plans and it
supports currently credit card payments
so how do you enable this you would go
back to partner Center instead of saying
no uh as we did earlier with you have
now to say yes that you would like to
sell through Microsoft
and as soon as you've done this you get
a new plan that happy a new plan
overview tab that appears on the left
side here and you can select create a
new plan and now you'll be prompted to
select a plan ID and also a plan name
which will surface in the appsource
marketplace
once you've done this you'll notice that
you have to specify markets again as
soon as you opt in into this transaction
mode through plans
the list of the countries that you're
targeting for with your offer becomes
the list of all the different countries
targeting by all your different plans so
this is how it will be defined it will
ignore what you have said previously as
the list of country
and then you have many options that you
can configure regarding the pricing
model whether you want your plans to be
public private with free trial or not
and many other things
we should go back to the plan overview
then you'll be able to see your plan and
to see your service ID
you can copy that one and move it to vs
code and that's where you'll be
referencing it in Al through entitlement
so you can have here an entitlement
object you have here the reference to
the plan ID from partner Center and then
you can start assigning permissions to
your entitlement and there was also a
great demo that was done earlier in the
what's new in Al that shows you a bit
more how you're going to leverage this
in your extension
but for this we have also great
documentation so we advise you to have a
look there and we can also try to join
the preview at AK dot Ms slash BC public
review
there are other considerations before
you go to appsource so test your apps I
think you've been told this a lot over
time you need to have automated tests to
make sure you have high quality and you
don't have any regressions there
think about performance when you're
going to appsource will have many
customers you'll be running in SAS and
performance there is critical
you'll have also to take into account
some scenarios such as throttling you
might be getting four to nine errors for
sending too many requests so you have to
be able to handle them gracefully in
your app so think about that
you'll have to consider what kind of
public API you're exposing in your
extension uh do you want your objects to
be public internal what do you want to
expose to other apps how can they
leverage this uh to complement to add
value to your solution
and finally how would you upgrade
existing customer especially in the case
where you started with the PT and you're
going to appsource you might want to
have an upgrade path for them to move
from the PT to the appsource app
now
um
you're in the states where you've know
what to do in partner Center you know
some of the requirements and the changes
that you have to do in your Al app I
think we're ready to go through the
submission process in partner Center so
let's have a look at this this is how it
will look like once you've done all your
setup you'll be able to go to this
review and publish action and then you
can just submit it later on you'll get
this View
that shows you all the different stages
your submission has to go through
the first one the first stage that we'll
have a look at is this automated
application validation this is the stage
where we're running the technical
validation of your app this is a fully
automated process that is running within
a few minutes and we're using this to
make sure that your app is meeting the
standards for the appsource marketplace
it's relying a lot on the app Source cup
so we're really advising you to enable
it in your development Pipelines
we're also making sure that your app is
compatible for all the different
targeted country and releases that you
have specified so as an example if
you're targeting Belgium and Netherlands
for version 21.0 so in that case you
would have set application to 21.0 in
your apps then we will validate all the
combination of all these apps
and that means that they can be a lot of
validation run if we do the combination
of all the different releases countries
and apps in your submission there can be
a lot of them this is why we also
recommend you to use Azure application
insights because we will be logging some
signals for you when violating each of
these different combinations of country
and releases and that will allow you to
have more insights into what is going on
for user submission
when you have first submitted your app
and now go with another submission we'll
also be validating for breaking changes
and more specifically unannounced one
where you didn't absolute your objects
ahead of time and this will be run on
the latest release that is being
validated so if you're using App
insights you might be able to see this
pattern if you have some errors with
breaking changes
once you're done with the technical
validation the submission process will
keep on and you'll have now a preview
deployed uh and you'll have yeah you'll
be asked to sign off on that preview
there's one thing to take into account
here we're currently only support the
preview of the listing in the appsource
marketplace meaning that you'll see your
app with all your marketing materials
there you can review them correct them
if needed but you won't be able to
install the app in customer environments
yet
so the current approach for that is to
deploy it on sandboxes of selected
customers and here are some high level
steps on how to do it so we remind you
again check your resource exposure
policy there is a dedicated field now to
decide whether you want them to apply on
dev extensions or not and then you'll
have to get access to the sandbox
environments of your customer and then
deploy your extension from Visual Studio
code an important note is that once
you've published your app on the
customer environments when you're going
back to appsource to bonus Center to
publish your app in appsource you'll
have to change the version number
because we currently do not support
having the two of them like apps deep
private from vs code and from appsource
with the same identity and same version
but don't worry currently we're working
on supporting to have preview out of the
box so at some point in the future you
won't have to worry too much about this
anymore and it should be much simpler
once you've done through this and you're
satisfied with how your offer listing
looks like you might just press go live
and then the marketing validation will
start as the name mentioned uh with
manual validation on this stage this is
a validation that is done manually it
can take up to two business days but
generally is processed faster than that
so this ensures that your offer is
attractive for customers and for your
prospects it ensures that your listing
meets the requirement for the
marketplace it's checking for trademark
Incorporated materials checks that you
offer description is in line with your
metadata everything that we've discussed
a bit earlier
and once this is done the first time it
might not be performed every time so if
you're resubmitting your app a new
version of your app but you do not
change the marketing materials it will
be skipped automatically for instance if
you just change the version number and
publish a new version of your app it
will be ignored if you change your
screenshots your offer description it
will be manually validated manually
again
and then the last stage I would like to
talk about here is this one publish
application with the service and that's
when the app actually becomes available
for business Central
and once you've gone through all of
those this is how it should look like in
partner Center you should have a nice
green line where all the stages have
been validated and at this point
congratulations your app is on appsource
and you're ready to get some customers
will uh we know from experience that
it's not always
a success on the first attempt and there
might be some failures and some errors
on the way so we'll see how we can avoid
those
and we focus particularly on the
technical validation since we know that
this is a common source of Errors so
we're asking you for this please review
the requirements before trying to go to
appsource there is a lot of
documentation there on what you'll have
to do with your apps these are also some
scripts that you can run from nav
container elper repo so all the BC
container helper functionalities for
Docker images there there is also some
functionality out of algo for GitHub
we're also asking you whenever you get
an error have a look at the FAQ that
we've built it's available at ak.ms Tech
validation FAQ and it contains a lot of
information that we've gathered over
time based on all the support cases we
had and feedback from appsource
publisher and it's really a great place
to get started
uh we'll also remind you that we have
now documentation on all the different
compiler Diagnostics and uh and
codonizer Diagnostics online with some
good examples and how to fix those
Diagnostics the reason for them
especially for appsource Corp have a
look at the documentation online to
understand what is going on with your
app
and for more advanced scenario if you're
using application insights we have made
available a tsg as a Jupiter notebook
you can download this one into Visual
Studio code install an app for jupyter
notebooks and then by just specifying
your connection string into that uh into
that notebook you'll be able to execute
automatically some queries and you'll
get an overview of what is going on with
your submission
so let's have a look at some common
technical validation errors in case you
are facing them so those are some
numbers that we got from the last 30
days when the slide was created and we
can see different categories breaking
change validation that's something that
comes pretty often
so what are breaking changes there
usually changes that are not breaking
your app but are depending the other
apps
that depend on your app and
if such changes are done it usually
impacts your customers and they won't be
able to upgrade they won't be able to do
copy of their environments point in time
restores it might be pretty
annoying for them so there are different
types of breaking changes compilation
breaking changes so your change breaks
the compilation of another app for
instance if you've removed something
those ones can be done as long as you
obsolete things ahead of time and wait
for long enough for dependent apps to be
updated similarly you can have runtime
breaking changes for instance if you're
adding or removing VAR modifiers if
you're increasing the length of a field
and then you also have schema breaking
changes and those ones are currently not
supported and they are all the changes
that impact your table table extensions
or anything that has a SQL schema in
general
let's have a quick example here of one
of them if you have a table and you
decide to improve it by changing the
type of a field but also renaming it for
instance here changing a year into a
date that won't be allowed and you will
get an error when going to appsource so
not something you can do the
recommendation instead of this would be
to set the field as obsolete pending
provide also an absolute reason that
gives information for dependent apps on
how to fix it and what is the new
alternative introduce your changes in
addition there you also need to keep in
mind that
this field even if obsoleted might still
be used by other apps so you need to
keep on inserting the values there to
make sure you're not breaking them on
their runtime behavior and then later on
you can decide to mark it as obsolete
removed and there we would ask you to be
also mindful of the timeline in which
you're doing that to make sure that your
dependent apps have time to be upgraded
another type of errors that you might
commonly see is uh that we commonly see
is related to the app.json and the offer
not being consistent so you would
usually get an error that looks like
this one in general you should check
that they are in line pretty often on
first submissions we see that the
publisher name or the name of the
extensions are not matching later on it
is more often that you forgot to update
the version number in the offer
description when you're publishing a new
version of your app so that's something
to
take into account when you're publishing
a new version we're also seeing payoff
an errors related to code signing so
yeah the app is not signed or has been
signed using your own certificates so if
your app is not signed then you have to
sign it as mentioned earlier we have
documentation for that
uh if the other case as we see a lot is
that the app is signed but the
certificate that was used was not
trusted it means you use your own
certificate and then you need to uh use
one that has its roots in Microsoft
Windows and for that you can purchase it
from a trusted certificate provider you
can verify on your own before going to
the marketplace if the signature on your
file is correct and you can do this by
just taking a
any computer that you have with business
Central installed and you can then go on
the app file check the properties you
have the digital signatures you can see
the details there and you have the
ability to see the certificate whether
it's allowed or not in this case there's
a nice Red Cross that shows that the
signature was not trusted
the other thing that you might get is
related to missing affixes at this point
we presented what affixes are and you
must register them if you see such an
error it means that you haven't
registered them yet or you're not using
the right publisher name so in those
cases you should either reach out to
d365 viratmix.com to reach your affixes
or double check your publisher name in
your extension
the other thing that we've seen in
pretty often and that was not covered in
those numbers are apps that are not
compatible with all the countries or all
the releases targeted in the submission
and um for this you would get errors
where some objects are not resolved some
missing pages some missing tables and so
on we've seen an example before if you
have an extension that depends on
objects are specific to Canada you
cannot go to Belgium and then you have
different uh approaches there you can
either only target the countries that
you're actually compatible with you can
decide to remove reference to all the
country specific objects or you can
consider to have duplicated offers with
duplicated code there are different ways
around it
we're also seeing issues where your app
is now not compatible with all business
Central releases and for that what can
often happen is that you're trying to
use the latest features for business
Central While targeting older versions
that do not have those features so you
can either update the application
property to actually match what you're
required to use or you can remove the
references to those new features to be
compatible with all their releases
so with all of this in mind you should
be able to get to appsource publish some
apps for your customers and as time goes
you probably get more and more customers
uh but the thing is that the more
customers you have the more likely
you'll be to have customers that are on
an older version on business Central
than the current one and this can be for
many reasons their environment might
have a PT that cannot upgrade
and
um that means also that some of those
customers might end up running on older
version of your appsource app than the
latest
and you know then that the older your uh
the version of your appsource app is the
more likely it is to not be compatible
with newer business Central releases and
the question comes like how can you then
release a fix for those customers that
are on old versions if you're not able
to go through the validation
and this is something that we have fixed
with the latest release of business
Central and we have now support for
hotfixing uh older Target older versions
of business Central there so let's have
a look at how the scenario is
um we were in October 2022 you decided
to go to appsource you publish there an
app that is compatible with business
Central version 21. and then a few
months later you decide to go with
another version of your app that is now
compatible only with version 22 because
you had some technical issue making it
compatible with both that can happen
now you're finding an issue in your app
that is targeting business Central
version 21 and you need to publish a fix
for it but you know it's not compatible
with version 22. so what we did in order
to avoid this issue is that when you're
submitting a version of an app we are
looking if there is a next version to it
if there is one we will take uh the the
version of business Central that is
targeting in this case version 22 and we
will use this as the maximum release of
business Central against which our app
will be validated so in this case we'll
validate this version 1.5 from 21.0
included to 22.0 included and then your
app is good to go through the validation
and will be uploaded to your customer
as part of the technical validation we
mentioned that we are checking for
breaking changes to make sure that your
customer can smoothly upgrade from one
version to another and we discussed that
we have breaking change validation with
the previous version of your app but
since you're now pushing version in the
middle of other ones we also introduce
validation for breaking changes with the
next version of your app
this means that the type of changes
you're doing there is
more limited so what you can do is
change your business logic you can
introduce new local procedures you can
introduce internal objects but you
cannot add new public objects that are
not in the next version and you cannot
add new tables new table Fields again
unless they are in version 2.0 as well
here
another thing to take into account when
you do a hotfix so publishing a version
that is not the latest version of your
app you should not change the app
version in your offer description
because we want you to keep the latest
version stated there so that when
customers go to the appsource
marketplace they see what is the latest
version of your app and not what was the
last version you pushed into the into
the appsource marketplace
so we've been now through a lot of this
and how to do those validation manually
there are also a lot of things we ask
you to consider automated testing and so
on
and it might be a lot to take but we
have
a solution that to help you manage all
of that
uh and this is algo for GitHub so that's
a solution that we have for cicd
pipelines on GitHub repository you can
create your own from a template that is
available at ak.ms slash algo appsource
and uh once you've uploaded your app and
gone through some configuration step
you'll be able to get access to many
useful automated workflows that are
there for you
among those you'll be able to get
continuous validations on your pull
request you'll get the ability to deploy
to your testing environments you will
also be able to deploy to partner Center
automatically and deliver it to
appsource so a lot of good things there
and a lot more to come so check out the
presentation tomorrow at 11 in Room 5
and you'll get more information on this
so as a conclusion we've seen how you
can bring your app to appsource what
kind of consideration you can have when
you're bringing your app there going to
appsource will expand your customer base
give you more opportunities and will
also make you think about how your app
is designed and make sure that you'll be
able to scale with that and we hope that
with this presentation you you know how
to get there
if you're facing any issues in the
process of going to appsource we have
different support channels depending on
each of the scenarios of course if
you're using the wrong one we'll
redirect you to the correct one but if
you want to we have your queries
answered in the best delays you should
try to get it right from the start
and with this uh we're concluding this
presentation so if you have a few
questions yeah
yep
sorry for my English
okay okay yeah
um
the possibility to have the offer for
contact me yes you cannot download the
same app
so you cannot download it from the
appsource marketplace the customers
there will not be able to just click one
button and have it installed so why this
because if if a customer contact me then
I cannot give him the the app
so there are ways to do it uh you can
have a look at the documentation there
are ways to install the app into the
environment it's just for them they
cannot do it directly from the
marketplace but you can set up uh ways
to with them to do this okay so I I can
make them download or I can install the
app the the registered app
without let them download it directly
so they'll they'll be able to do it
themselves so they have to go to you
then you'll provide them with the steps
this is documented uh for the publisher
side and then they can get the
application installed and as a note on
this uh this is not replacing the
monetization and Licensing so you also
still have to build this on your own of
course okay okay second question is
regarding the auto fix part so are you
telling me that I can push my customers
or uh to to to download
a new uh version of my uh so what we
presented here was about making the
version available in appsource So
currently we are not automatically
pushing your new versions to customer
environments we're only doing this as
part of the upgrade of the environment
to the next major
they will have to go to the appsource
marketplace and so are you assuring me
that on every major release you push the
update rate of my app to all the tenants
all the tenants yeah when they upgrade
to the next major version of business
Central we'll upgrade all their
appsource apps to the latest version at
the time of upgrade okay thank you yeah
okay yep you can
hello okay so a quick question about the
shared libraries because for example
there's most of the times we have in our
offerings you have like a core extension
that has a lot of interfaces and base
functionality and then we could have
dependent extensions that could be just
for ex um integrating with different
third-party providers
how does that actually work when we're
trying to upload this to appsource it's
not sure library library isolated
between the two offerings or is it just
like a miss a match how does that work
so
from the business central point of view
uh your offer contains some extensions
and as soon as they become available in
business Central they can be reused by
other offers with the Assumption of
course that you're using the same app ID
for your library across your different
offers this is what defines the identity
of an app and any library that is
available to business Central then can
be referenced by another offer of yours
or potentially another offer from
another publisher that decided to make
his business rely on top of yours so as
soon as you upload it and it gets to
business Central into appsource you can
just reuse it from any offer that you
have and that's valid even though that
is not my main app because of course I
will upload it as a dependent share
Library when we're opening to appsource
so that also gets registered and can be
reused yeah it doesn't have to be the
main app so any of the apps that you
have included in your submission whether
it's the main app that has its offer on
its own or one of the libraries for it
those one can be reused from another
offer they they don't need to have their
own offer on the their own listing on
the marketplace to be reused so
yeah hope that answers the question
are there some other ones
there was one here
about the the monetization with the
entitlements and will Microsoft apply a
fee for Apple transaction or a
commission
this is a good question I think Stefan
knows
three percent okay it's three percent
okay thank you
yeah we had another question on the
other side I can
to the transfer
okay
[Music]
we have
changes to one of our customers in
they want to a field customer name with
the length
texts
100 and
after a month they sit but we don't want
to be a customer name we want to be
Source name in values
can we change only the the name not the
the type of the field
no so that won't be blocked
um that's a schema breaking change
you're renaming a field so we won't
allow you to do this snap Source we'll
have check that are preventing you from
doing so so you'll have to introduce a
new field with the new
you can change the the caption it might
be a bit misleading for other apps that
are depending on it now because the
field contains different value that one
it claims but that could be seen as a as
a workaround but including the another
field for it might also be a good
solution there
okay
any other questions
I don't see any ends up anymore
so thank you everyone for listening to
this presentation and
[Music]
