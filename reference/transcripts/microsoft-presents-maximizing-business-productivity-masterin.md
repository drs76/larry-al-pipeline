# Microsoft Presents: Maximizing Business Productivity: Mastering the Shopify Connector

- **Source:** https://www.youtube.com/watch?v=oFiGCwQpiwE
- **Video ID:** oFiGCwQpiwE
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 44m11s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome to today's session where we're
going to talk about the Shopify
connector my name is onad I'm a senior
software engineer in the Integrations
team working for business Central so
what's on the agenda today first I'm
going to give you a brief introduction
to the connector and his capabilities
what can it do um then we're going to
straight jump into demos uh we're going
to first set up the connection and then
immediately start selling products
online then we're going to add our
business Central customers to our
Shopify store and then we're going to do
some fine-tuning of items management and
then we're going to snc orders for
company representative uh that is a new
feature businessto business connector
came with uh version 24 so we're excited
to share that then I'm going to showare
you some tips and tricks on how to
troubleshoot the connector and finally
I'm going to show you how to extend uh
what are the extensibility points of the
um
connector so capabilities what can the
connector do uh first things first you
can connect uh the same business Central
company to multi multiple Shopify shops
so if you have shops in different
countries or if you are selling multiple
products in different shops you can
connect them to the same business
Central company uh you can buy
directional listing items products um
and customers and now companies uh you
can sync prices and cataloges to Shopify
inventory levels from business Central
to Shopify again you can import orders
uh from Shopify to business Central uh
you can import returns and refunds and
you can find send the Fulfillment
information when your orders are shipped
to Shopify I'm going to demo uh almost
all of them uh except the returns and
refunds because time restrictions uh so
that's why I want to have another slice
talking about return and refunds so what
can you do with them uh you can define a
a location for returned Goods so if
someone returned an item you can specify
a location and that uh item will be
restocked in that location uh for
refunds without restock so if you're
selling subscriptions or the item was
faulty and you don't want it back you
can create create a GL account and then
point it to that one so that money goes
into that account you can automatically
create credit memos from returns and
refunds and you can access all of them
from the Shopify order page in business
Central so without further Ado I'm just
going to jump straight back into the
demo first I'm going to create a shop
and connect to it and then set some
settings so first let's create a shop
and call it demo what you're going to
need here is the Shopify URL you can
copy your shop URL your admin URL will
automatically as you can see convert and
then you can enable when you enable the
connection you're going to have to
install the business Central app in your
store after this is installed I'm going
to set some
settings done and now uh I'm going to
just switch off allow background sy so
that all the thing happens in the
foreground no job cues I'm going to sync
items to Shopify uh syn item image to
Shopify
sync item attributes and I'm going to
track inventory the default inventory
policy I'm going to set it to deny so
that I cannot sell out of stock items
then for customer synchronization I'm
going to also create unknown customers
with order import and set a template so
when there's a new order for a new
customer that customer will
automatically create it in business
Central with that template now I'm going
to set shipping charges account and a
tip account so if you get money for
shipping charges or your tips they will
go to that ja account this is basically
the uh the most the essential settings
and one thing we need to do is also set
some location mapping and you can get
the Shopify locations I only have one
and then map them to business Central
locations with a filter so I'm going to
do it an empty and East and the main
location this is going to be my default
location and I'm going to calculate the
stock by the projected available balance
today so when I sync the stock it will
calculate it by today and send it to
Shopify that's all done um I have a
connection established this is going to
be our first scenario start selling
products online so you have business
Central already running you want to try
Shopify as an online store and you don't
want to spend too much time on setup uh
you already maintain your items in
business Central and you want to launch
your store quickly as possible get some
customers and possibly get some tips so
what I want to do first is I want to add
all my chairs to my Shopify store then
I'm going to start selling my chairs if
you go to uh Shopify products page from
the shop card uh you can use the add
items to show Shopify action to run a
report and then add all the uh items
with chair category code so what this
will do is get all the items add them to
Shopify store sync images sync inventory
and sync price levels and then you can
see them both here in the Shopify
products page in business Central and
also your Shopify
store that's done uh items are here now
let's go back to the customer facing
online store how does it
look so items are there with um pictures
prices and also some of them are sold
out if there are no stocks this is my
all catalog because I only have sync
chairs and let's say I want to buy now
the batt in chair uh you can see the
item attributes are also synced in a
table if you hit buy
now uh you're going to have to fill in
some details this is the uh the checkout
uh experience from Shopify um I'm going
to uh create a new customer claudo loen
and then for the payment I'm going to
use a bogus credit card uh for your
development you can set that very uh
easily from your Shopify Store settings
you can set a bogus credit card and then
then you don't have to pay for real
transactions you can just do them for
testing that's done so so for uh in the
last uh set setup you can see that
there's an ed tip uh action uh this is
not uh this doesn't come with uh outof
the Box in standard Shopify checkout
experience but from your shop store you
can add this so that uh your customers
can add tip so I just added like 10% tip
and I see how that will sync order is
complete uh now that they actually we
need to take this order back to business
Central and then create a sales order
for this and then fulfill it so what I'm
going to do is go to orders from my shop
card and just use action sync orders
from Shopify very simple and then this
is going to run a report you can also
set filters on it but I'm just going to
sync all
orders so there's a Shopify order now
created you can see that it's paid and
unfulfilled and the customer is already
created for this collodial aen and there
are two lines one of them is the item
itself and the second one is the tip so
let's just create a sales document for
this this we going to create um a
business Central sales order from this
Shopify order and what's going to be
different is that instead of two lines
we're going to have three lines in this
business Central order so orders created
let's take a
look yeah as you can see three lines one
for the item the second one is the tip
and the third one is the shipping
charges so they go they both go to the
GL account I just set in my shop uh
card so what I can do now is because I'm
going to ship this I can add the
shipping agent and I can add a package
tracking number to this
order yeah I'm just going to add a
shipping agent
here DHL is fine oops I have an error
I need to uh release the uh reopen the
order and then release it again after I
change it this is also a setting you can
set in your shop card so if you want
sales orders created from Shopify orders
to be open or released you can set that
up as well now I'm going to add a um a
package tracking number and then just
post the shipment
yeah all good uh invo created order is
shipped but if I go back to my shop and
I can see that the order is still
unfulfilled so how do I syn that right
um that's also very simple uh you just
need to go to uh your Shopify orders
page in business Central and then sync
shipments to
Shopify that's sync when I go back to
the order you can see it's fulfilled now
and if you want the latest changes from
Shopify in this page as well you can
just sync them again and then this uh
fulfillment status will change from
unfulfilled to fulfilled so that is
basically it that's how easy you can add
your items selling them online and we
also got some tips as well that was nice
and then that leads us to our second
scenario right uh we just sold our first
item and then we want to uh add our
existing C Business Central customers to
our Shopify store and we also want to
use some businesso business flow as well
and add our companies businesses to
business companies to Shopify and then
send them probably invite so that they
can look take a look at our store and
then they can also buy some stuff and
get us some
money so what I will do is I'll go to my
shop cut again and then go to my
customers just like items you'll see an
at customer action in this page claudon
is already created as you can
see so now I can select the business
Central customer or more uh to add to my
Shopify store so I'll just select one
and then sync
it so Helen Ray is created uh in Shopify
so when I go to my customers Helen Ray
is already there and you can see the
default address of this is taken from
the contact information of the customer
that I've just syn and you can use this
uh send account invite action in Shopify
to send an send them an invite through
email and then they can access your
Shopify store and then uh start buying
your products now I'm going to do this
for B2B flow with the companies so I
just go to companies again same flow at
company uh we try to do as unified
experience as we can and I'm going to uh
select the school of f out and sync it
so one difference is that you can see
that there's a main contact right now
and that's the megum bond and how that
come is that it comes from the uh the
contact information of this
customer because in Shopify you can see
that it creates One customer and that
customer will be the main contact of a
linked company School of Fine
Art and this company has one location
and it has no cataloges right now which
I'll show you how to add catalogs and
sing special prices for that catalog
later on and if you want to send an
invite to a B2B shop which is going to
be different because it's going to have
a different catalog and different prices
you can go to customers
again select that mean Bond and then
choose the send B2B access mail and then
this will send them an email you can
they can just click go to account and it
will be a completely different
experience than your customer facing
shop because you're going to sell
different products maybe discounted
maybe more priced to your B2B
companies so customers are now exported
to Shopify uh they can already go in and
then buy um but we want to do some fine
tuning of item management so we're going
to have more flexibility and control
over the processes uh for item
management and we want to probably have
some product description so that they
look nice in our store and we want to
have some review steps before products
go online because we don't want to push
them to Shopify and that they go uh
directly active and we also want to
probably create some B2B cataloges set
some uh be special B2B prices for our um
Partners so what I will do right now is
go to BC and create a customer
group so if I go and create a customer
price group called Shopify then I can
set some line discounts set some prices
on that and I want to and I can set that
up in my shop C so that uh prices will
be sync uh through that customer price
group then let's uh let's modify some
item that we choose have some
fine-tuning I'm just going to go and
select ATT
desk and first thing I'll do is I'm
going to create two variants for this
item one premium and one essential which
one will be uh expensive than the other
yep and then what I'll do next is I'm
going to set prices for each variant
differently and also probably some
discounts uh marketing text was the
first co-pilot feature that we released
so you can create a marketing text for
this item and you can also sync that to
Shopify I'll show you how to do that
later on first for for now we're just
going to create it and keep it and the
next thing I'll do is I'll going to I'm
going to define a sales discount uh for
two variants that I have
so first sales prices price
group and then I'm going to use the
Shopify one um you can see there's no um
variant code uh in this page uh what
what we can do is just customize the
page and add that field so that you can
have different prices for different
variants of the uh the same item
so first premium 4,000 and essential
will be
700 all done now we can Define the
discount as well
and I'm going to use the retail uh
customer discount code which I can again
set it up in my shop card so that it
uses that price group so I'm going to
put a 10%
discount and finally I'm going to create
barcodes for this um two variants that I
have for this item if I go to item
references I can just create a barcode
and put it 777
maybe more sevens
Y and then another barkode will be just
once set it up for the two variants that
we
have so I think I'm done with AdSense
desk for now um but what I want to do is
I want to select another desk or a table
and then uh change some inventory so
I'll just go for ANB conference table
since we're in ANB and I'm going to
adjust
inventory what I'm going to do is uh put
some inventory for East and West
locations and when I add this item uh to
Shopify you'll see that because we
haven't mapped West in our location
mapping it's not going to consider that
stock when missing to Shopify
okay before I add these uh tables and
desks to Shopify I want to set some
settings so first uh we're going to do
uh enable sync item marketing text uh
we're going to change the uh the SQ
mapping from uh empty to item number and
variant code and then I'm just going to
allow uh inventory policy so that I can
sell out of stock items uh status for
created products now they're going to be
draft and won't be shown to in the shop
and action removed products will be
archived so if I remove a product from
the list in BC it will be archived in
Shopify and for Price synchronization
I'm going to use the uh the customer
price group I created and Retail so that
it gets that 10%
discount and now uh let's do the same
thing and add uh tables and desks uh to
Shopify for the products some of them
are already there the chairs and what
I'm going to do add items instead of the
chair category Code table and desk inste
so what's going to happen now is that
the three created products will be in
draft and when you go to your customer
facing online store that you won't see
them but you only see them in Shopify
admin Center so you can have more
control before items go live you can see
three of them are in draft and they're
not visible in your online store but
what you can do is when when you're
ready uh you can actually set them uh to
active from business Central so what I'm
going to do is set ANB conference table
active and I'm also going to add an SEO
title here as well uh this will uh this
is a um a think that Shopify has you can
create SEO titles and uh when you search
the products on online uh it will show
up like
that and what I'm going to do also is I
am not really interested in aens Mobile
pedestal so I'm just going to delete
that and since I have deleted this here
uh because I set that up it's going to
be automatically archived in my store
now let's just refresh this
list yeah you can see ANB is active at
since is still draft and the mobile
pedestal is now
archived so let's look at the uh the an
uh conference table uh and then see what
changes are
there if you scroll all the way
down you can see that uh search engine
listing is exactly the title that I have
and then you can see that the the
quantity is only shipped uh synced from
the uh the location mapping I have and
for the add
desk you see two variants are there
essential a premium that I've created if
you want to create more or um man manage
your variants in Shopify you can also
have them by this edit button and then
sync them uh back to VC um and I want to
see how does it look if if I open one of
the the variant so I'll just open
essential so first thing you'll notice
is the uh the SKU so it uses the item
number and the variance just like I
selected and the barcode is also synced
weight is synced and the uh if you look
at the prices uh for example for premium
you'll see that compared price uh is
,000 and then the actual price is 900 so
it's like 10%
discounted so how does the this AdSense
dis look uh in Shopify store um by the
way you can see in the description that
um marketing text is also synced just
like we set it
up so how does this look as I said uh in
your store just continue shopping and
then you'll notice that I don't actually
see that why is that because uh we set
it up to be draft and then we haven't
activated so it's not actually available
in the store so what I can do is
activate that
again and just refresh my store and it
will be available yeah U what Shopify
does that they have this good UI you can
see the two variants are there and then
the prices as actually you can see the
discount so that they can see that they
are getting this 10%
discounted so now let's try to add this
AdSense desk to my B2B catalog I want to
uh sell this to my busines to business
partners I'm going to create a new
catalog and then I'm just going to say I
want specific products not all of them
I'm just going to call it
B2B and then you can actually manage
product and pricing uh within Shopify so
you can include or exclude uh products
you want to see but what I'm going to do
is just include AdSense desk and let the
uh the information seeing from business
Central
so catalog is created let's just add
that to my company that I've already
created before so if you go to school of
fine art you can use this at catalog
section and then just pick the one I've
created so Shopify does this in the
background but should be relatively fast
yes it's already created there uh in
this location we have one catalog so
this um B2 company can actually use this
catalog to go through your store and
then uh buy them so that it is only
available to them to with those uh
attend desk item so what I'll first do
is I want to set up a large account
discount because there are my B2B
companies they buy a lot from me so I'm
going to set a 25% discount for this
AdSense desk in large account uh sales
discount
group so instead of the retail that I've
just set for my entire shop for my my
d2c customers I'm going to use large
account and I'm going to use 25%
discount for
this okay but how do I do this right how
do I sync it I'm not going to go back to
my shop card and change this because
that means everyone will get a 25%
discounted I wanted to do it for this
specific company so I open that company
from my companies and then you can see
there's this uh Shopify catalogs action
and then you can get catalog specific
for that company and when you you sync
it you'll see that there's a a bunch of
settings that are available so for each
catalog you can Define how to sync
prices or you can choose not to sync
them with the sync prices Boolean and
then you can set the customer price
group the discount group and use the
action sync prices so that your B2B
catalog uh will have special prices just
for that special
company so it's sync so if I go and open
my catalog back instead of the the 10%
discount now I'm I'm going to see 25%
discount is for two variants as you can
see and if I go to my online store the
customer facing d2c one this is the
still old prices so you have two prices
one uh for the catalog and one for
everyone else um so we just fine tuned
our items uh we create even created a
B2B catalog uh this brings us to uh a
final demo and how can you uh sync those
orders B2B orders uh when they have
those special prices in the
catalog so I'm just going to create a
sales order from my admin Center someone
called me from this uh Mega Mod called
me actually and they want as the school
of fineart they want to have an AdSense
desk so instead of the personal roller I
choose uh the um the company for mean
Bond I just need to change the market
because as you can see school of Finance
is in us but my shop is in Denmark so I
just select the market and now I can
actually sell them and add the product
again yeah I'm selling them premium
because they're already getting a
discount
anyways and then we're not going to get
the payment in Shopify right away we're
just going to say you can pay within the
next 90 days because we have a trusted
relationship with this
company so orders
created let's sync this uh order back to
business Central and possibly get paid
outside of Shopify and then how you can
sync that to Shopify from VC
and I'm also going to add a PO number as
well and when I sync this and I create a
sales document from this the PO number
will be carried all the way through the
business Central order as the external
document
number so the um the flow is extremely
uh simple and exactly the same uh
there's one page for orders you just
sync orders and instead of the the mean
Bond uh customer you'll get it through
School of Fine Art company
ORD created as you can see for school of
fin out is is order status is pending
and is
unfulfilled so let's just open it and
try to create a sales orderer for
this and you can see the email is the uh
the main contact of this company so that
is our main contact so we're just going
to send it an email when we actually
ship the order to
them so business Central order is
created that means I got the money uh
what I can do is use this Mark as paid
actions and say that I got this money
out of uh Shopify it's paid it's all
good and then this will sync it so you
can see the uh the status of uh Finance
is paid for this order now um I'm not
going to go into fulfillments because
it's exactly the same you ship the
orders you sync orders uh you sync
shipments to Shopify and order will be
fulfilled same as uh the the d2c
flow so um it's all done we created a
shop we fine-tuned our items we added
our customers uh we even created B2B
catalogs we sold to d2c and our B2B
Partners um this is basically the
capabilities uh of the connector as I
said other than returns and refunds
which I'm not going to go into because I
want to show you how to troubleshoot the
connector and how to extend it properly
um
properly um so troubleshooting the
connector in case there are issues we
hope not but you know it's is an
external system that you are
communicating with so some things may go
wrong um and then we gave you some bunch
of tools uh to troubleshoot the
connector first thing you want to do is
run the tasks in the foreground that way
uh it won't run it as job key entry so
you'll catch the errors immediately and
then the error will be shown uh in the
foreground so you can actually see this
STX race copy the session information
and send it to us if you need help the
second thing you want to do is take a
look at the logs there are three
different uh logging modes um first is
all so it logs everything all the
requests made and the responses we got
from Shopify error only uh this is the
default one so if there's an error in
the Shopify uh graph qu query that we
sent or response we got it will be uh
logged automatically off we don't
recommend but you can turn it off
completely so nothing will be logged in
these logs you can see the request sent
and the response that we received uh we
also put the request ID we get from
Shopify so in case something that we
cannot fix and it's on Shopify and we
can use that Tim stamp and the request
ID and then they can immediately point
out the uh the request and then fix it
properly um then you can see the query
cost information in the logs as well so
uh for each shop uh you have a set of
tokens and each query that we send
actually uh a waste those tokens uh
because we are a premium partner with
Shopify we get double the tokens but
still um if you run your things way too
often you might get get um model act and
then some uh query cost will be u high
then what Shopify will do is just say
wait and then we have our system to just
wait uh wait and wait until we actually
uh get more tokens by the time passes
and we can send that so you can see that
in the logs as well how many retries it
took and what's the query cost of the
query that we sent data capture is just
like logs uh but it is for specific set
of records and it doesn't care about the
logging mode so for ERS shipping cost
transactions those sort of stuff we
always lock the response we get so if
you see there's a a mismatch between the
Shopify order and the business Central
order that you created you can always go
into that Shopify order in business
Central and see the response we got from
them and then see where the mismatch
came from reset sync um you can reset
sync for all the syncs uh companies
customers items and orders um this is
for let's say you want to uh one order
did not sync and then you want to
include that in the next sync again so
you what you can do is sync the uh reset
the sync time put it back a couple of
hours so that it includes that order and
then sync it again or let's say there's
a faulty order that doesn't uh sync and
then there's an errors and then you want
to actually try it try it again after
you enable uh tasks in the foreground so
that you can see the stack trace and
everything so you just enable the tasks
in the foreground reset sync so that
that is included again run the sync that
order will be try to sing again and you
can see the um the errors uh let me show
you that all of those in actually um in
BC so if I go uh to my shop cut as I
already did allow background things is
already disabled uh when you enable this
it just creates a job ke entry for each
sync so if you don't do this then you'll
see uh you catch the errors in the run
time logging mode is as as I said
default error only and if I go to
Shopify log entries page you'll see that
it's completely empty because every
single request we sent so far there
hasn't been any errors but what I can do
is change it to all and use one of the
troubleshooting actions test
connection connection was successful and
let's see how that request looks in log
entries
now you can see uh we actually log a lot
of stuff the URL the method the status
code the request ID to sent to Shopify
the request we sent and the all the
response we got in Json format and this
is not only for troubleshooting actions
this is for all the things right if I go
in and then add another
item and hit Okay so this how item will
be added and then we're going to send
bunch of graph queries to Shopify and
they all will be
loged so as you can see for one item we
already send one what six uh and then
you can open each one of them and then
let's pick product create you can see
the request that we sent with all your
information and the response we got uh
from
Shopify um this might sound very heavy
logging everything especially for one
item we did like six entries so what we
did is when you switch the loging mode
to all we automatically enable retention
policy for that table because Shopify
only keeps them for one week so request
ID is and all the requests are basically
irrelevant after a week so you need to
reset the thing retry and then contact
us so that we can uh get the uh correct
help for
you um let's look at this uh retrieve
Shopify data on Shopify order and that's
the data capture so it doesn't log the
request ID or anything it just logs the
response vot so that you can do uh some
business logic uh if there's a mismatch
you can check
those and finally as I said reset sync
it's just an action for each of the
syncs and then it will ask you to put a
time uh you can just set back in two
days one one year or whatever if you
want to include all the records that you
have so that is basically how you can
troubleshoot the connector yourself and
finally uh how you extend it so for the
connector we took a different route and
the connector is mostly internal so you
won't be able to access most of the
objects uh extensibility is done through
uh interfaces and events this is to
follow the rapid changes in Shopify
because they release a new API version
every 3 months and they are known to uh
introduce some breaking changes so
because we don't want to break you uh
and your to customizations we said what
we can do is give you some interfaces
and events and then you can use those as
extensibility points you can get them uh
in this uh Al app extensions GitHub
project it's a first party app is
available uh as the source code uh so uh
let's look at some code and then uh some
extensibility points that we have I have
this um project uh it has a dependency
to the to the connector and then I have
three folders here inventory order and
product so for product uh I have two um
subscribers they all subscribe to this
code unit you can see this is the
product events and these are all the
extensibility points that we have for
product sync and the first code that I
have right here is on have to create
Shopify product it just basically puts
the U the vendor in Shopify product as
the manufacturer so it gets the
manufacturer code and then put it on the
Shopify product as vendor the second one
is modifying the item mapping if you
want to use GT mapping instead of SQ
mapping when you sync uh from Shopify to
BC you can use this code what it does is
basically tries to find an item um and
map matches the uh Shopify variant SQ to
GTI in business Central items so let's
just publish this this and I want to try
the first one cuz the second one I need
to change the sync and we don't have
much time so let's see how this
manufacturer sync
Works
published now let's just add an item
first I want to set of course the
manufacturer code and how U how it looks
yeah let's go to the items
list and pick one um have remote
pump then set the manufacturer code to
fabric
residences so when I add this item to my
Shopify store uh it will add the
manufacturer as the vendor uh for that
item so if you want that information or
if you want more you can use those uh
extensibility points in uh item product
thing to add uh additional
stuff yeah items added and if I open
that in uh in
Shopify right there you'll see that on
the right hand side uh vendor is
fabricom residences so that is how you
can uh modify with a small extension the
item syn um let's look at the uh the
some Auto modifications so the first one
uh and again again it is a different
code unit for orders so it has many
extensibility
points you can get all of those from uh
GitHub repository B alab extensions the
first one is just an extra step when you
create a sales order from a Shopify
order and I want to make sure that
payment method code is not empty when
you create a um a sales order the second
one is I want to add the external
document number for d2c because it may
not be empty for B2B because the PO
number We sync but for d2c you want to
have the Shopify order number as the
external document number when you create
a sales order from it and the third one
is uh adding information to the line not
the header uh so what I did is I have
this fine Shopify Dimension uh procedure
it basically looks for a dimension with
Shopify and the dimension value the
channel name so the channel name can be
point of sale uh online store or the
Shopify admin so if not it will just
create that Dimension and then put that
dimension uh in the line itself so what
it does is just creates a temporary uh
Dimension entry and then we get that
Dimension sets uh number and then just
put it on the sales line very simple so
let's see how that
works yeah I'll just create one order
just buy something
let's put in some
details no tip this time
so let's sync this order and then see
how our extensions
work oh I'm debugging so I just need to
hit
continue yeah order should be created
now yeah so order will be created with
an empty payment method
code and if I want to create a sales
document uh for this my code should just
say no you
cannot yep test for build failed let's
just continue and see how that error
looks and it is logged in the error
message that payment method code uh
needs to have a value so we's just put a
value
here and then create a sales document
from
this Y and then let's open that
so you can see that there's this channel
name that didn't exist before uh where
did it came from uh if you look at my
code I have a table extension for the
sales header that has a um a flow field
and it looks at the Shopify order header
and gets the uh the channel name because
we actually link them with the order ID
field and I also have the page extension
to show that of
course and um if you go back to the
table extension you'll see that I also
extended the lines and but this time I
put the variant description on BC order
lines again with a flow
field and then of course the page
extension to show
that and you can see for ens de
essential Edition I get the variant
description from Shopify uh for that
sales line uh and then external document
is there as I already uh have the code
for that and if I go back to line and
then look for diens
Dimensions you'll see that Shopify
online store is there so that is
basically how you can extend uh the
connector with the small examples we
have a lot more examples in our
documentation in our GitHub preo um but
if this is not enough for you right all
the uh objects are internal and uh
extensibility points are not enough for
you uh we encourage you to actually
contribute um so what you can do is go
to ALF extension create an issue or
maybe even create the code yourself and
what we're going to soon release is that
step by-step walk through on how to you
can actually uh locally develop on
Shopify because we have our onor app and
it's the client ID and secret are saved
somewhere safe so you cannot reach them
but we'll uh provide you documentation
on how to register an app uh how to edit
standard graph cils and add more ones
and then have the how to run the
connector locally basically and that
will be coming soon so that if this is
not enough sensibility for you you can
always write your own code uh contribute
uh because we are always open to that
one yeah so that is all I wanted to talk
about thank you for listening and if you
have any questions we have three and a
half minutes so I can take
some
yeah oh you want to send
it thank you
oh hi is it possible to add more than
one tracking ID per
fulfillment yeah yeah uh the uh the
tracking ID I just added uh you can sync
that and you can also extend it to
because we al already um have
extensibility points for shipments as
well you can add like multiple tracking
idas and everything and and another
question um is there an easy way to
provide PDF invoices through Shopify
that is a good idea and then something
that we haven't considered yet so if you
want to create a BC idea for that that'
be great because that is something that
we can definitely look into because
there's right now no PDF
thing um about the shipping yeah agents
you've just got the whatever they choose
for shipping on the website comes
through as a shipment method code yeah
so wouldn't it would it make more sense
to have it as a shipping agent so that
people can choose want
AG well yes that is also possible so
because Shopify provides many shipping
agents so if you ship from Shopify you
also support that flow as well how did
you switch that on because I couldn't I
was looking for it and I could only see
the shipment method being set um yeah we
can definitely look into that there's um
you can set it up up from uh should be
very simple actually you have time for
one more I
think just just quite quick um do you
support non-stock
items um sorry uh non-stock items yeah
um as in um items that are they don't
have
stocks uh no the data time on
stock oh I don't think I get the
question if you can explain that
better maybe you can talk after the talk
yeah yeah yeah
yeah thank you
