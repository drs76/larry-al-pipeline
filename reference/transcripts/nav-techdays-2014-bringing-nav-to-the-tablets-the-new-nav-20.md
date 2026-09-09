# NAV TechDays 2014 - Bringing NAV to the tablets – The new NAV 2015 touch enable client

- **Source:** https://www.youtube.com/watch?v=5CXHRxLw_g4
- **Video ID:** 5CXHRxLw_g4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 86m57s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

so ladies and gentlemen good afternoon
and welcome again sorry for the slight
delay we had some small technical issues
but that's all normally sold right now
will you please welcome the last
speakers in this room for today please
welcome versa and Lucas it's my mic on
all right when I was about to book my
trip to come here I went online and was
all that I was going to order ticket and
I type Andrew and to my surprise
actually the first city that showed up
was a city in the United States so there
is also an advert in the United States I
mean I mean do you guys were from
Belgium probably knew that but I'm going
to start with a little quiz do you know
how many cities in the US they are which
actually have the same name of a city in
Belgium you raise your hand if you think
it's more than 20 all right call hands
between 10 and 20 yeah all right few
hands less than less than 10 but more
than five okay it's going to be hard
because you had this as many hands every
time less than five okay so the actual
answer is is is nine me create my
presentation so these are these are the
cities in the US which have the same
name then a sit-in in Belgium but
actually when you when you when you look
it up there's actually quite a few
cities in the u.s. not have that have
same name than some European cities
obviously that has absolutely nothing to
do with nav and was just something I
thought I would you know entertain you
with good good afternoon everybody my
name is Vincent Nicholas I'm the
principal engineer lead of the client
team in nav and I've Lucas or bumski
with me with an engineer on my team
we've been really busy last year and
most of the time we have spent on on
developing
or tablet client for fri Navy so I guess
some of you have seen it already let me
see a show of hands how many of you have
seen the tablet client already quite
many people okay okay so we're going to
go through some of the specific tablet
stuff that I new to the product because
there's a lot of interesting things you
might not have seen already in the
tablet so let's just let's let's get
started so first of all it's on all the
three platform this we major platform
iOS Android and Windows of course so if
you want your customers to get the
tablet client it's very easy they just
go on the store and they look for the
tablet client and for nav tablet client
and and the dollar will instil it like
install it like any other and need the
other app from the store I'll show you
that in a second or that works but if
you go you know if you've tried it
already go and search for nav or
dynamics nav on the store you'll get a
few hits this is not the only app out
there which has something to do with nav
so if you want if you want your
customers to to get right to the proper
app you can send them a link all three
store support that you can link directly
to the clock to specific app so they can
just you know click on that they can
install and so that I'll show actual or
that works ideally you would you would
once you have your system set up with
your real server and a new application
you would go and inform at a mail and
send it to your customers containing all
the information on how they can install
install the app so let me show you what
that works so I'll switch to my surface
here
so a male could look like this one yeah
you can see it and this is the cyclone
over there they actually links to the
different stores and so you just go and
you know click on it from you mail and
that brings you to the store directly to
where the app is should do that that
maybe it'll check the connection yeah to
a correction from here all rights okay
all right let's try again all right
first team we affect sorry about that
all right but it's on the store and
that's how you get you get to the app
through that link so you can just
install it from here I don't do that
because I've installed it already so
once once you've you've installed the
app on your device you just launch it
and that's the that's the screen that's
actually the screen you get actually
before that because I've logged on on
that device already so that's that's the
very first screen you get as you can see
the the service name we see the URL of
your server is pre-populated because
I've logged on already but the first
time you use us are gonna use this app
it's not going to be pre-populated and
the URL URLs that needs to be nettles
can be a little bit complicated so
here's here's how you format the URL so
these are these are the apps the the
links so when you get going can download
presentation from for me boo so you can
get these links to to put in the mail
directly for reference so this is this
is the links you can you can use to open
the app and make it easier for your
customers to directly have all the
information on your server the port the
instance they use if you are using
multiple instances and your company and
your tenant
so there are a couple of example as you
can see we were actually uh so the way
it works is that we when the app is
installed on the device we register a
custom protocol pretty much like on
windows which going to bring you
directly to to the app so going to demo
that why now if I switch back to my
device here I switch back to my mail so
you see the the UIL I have on my mail is
actually starting with this with this
protocol and then that's the name of the
server instance and that's the name of
the nav instance and you can I could add
company and tenant and stuff like that
so if i click on instance on the on the
link sorry i get directly to the next
screen so i don't have to type the
entire URL and the only thing i have to
enter now is my my credential for my nav
credential
here we go so that's a that's a wall
centre it looks on the on the tablet so
one of the things that we like to demo
is this is this is the wall center in
the portrait sorry in the landscape mode
but we also we've done a lot of work to
implement something we call adaptive
device adaptive layout and you'll see
that if you switch to portrait mode will
change the old layout of of the screen
to adapt through to the new format I
can't show you that on that connection
because when it's a projecting it's
actually doesn't want to doesn't want to
turn I believe so yeah but I can if you
come to the desk after the presentation
I can I can demo it for you so this is
this is how you easily get get your
application to this application to your
customers now you as a you might
consider having a male formatted like
this to make it easy otherwise it's a
little bit can be a little bit
cumbersome to to get to to the app
itself and enter your credentials and
all these things so the only thing
basically that your users have to do is
enter their credentials from this link
alright so let me walk you a few of this
UI element we have on this on this
tablet experience so the well no ribbon
here instead we have this pop-up menu
that will that's popping up when you
press the three dots tap on the three
dots and it's only going to show the
promoted actions because you know as you
know the ribbon is can be pretty crowded
and pretty busy there's simply not
enough room on the tablet to show all
this stuff so we made that decision that
showing only the promoted action so
that's you need to keep that in mind
when you build your pages the navigation
is on what we call the burger menu looks
like a burger with three three lines
here so that's your navigation here and
the tiles as you know as you know them
on the side so another thing we have
which is new and only for the for the
tablet client so if you go to to a
listview where you have a lot of a lot
of entries for is in the items in the
demo database have have typically a lot
of entries if you do that on the other
clients you have to scroll back on the
web client we have this paging mechanism
where we go and and and we show a
certain number of lines I think 25 cash
to remember midnight show I think it's
15 on the embedded list and then 20 in
the dialog okay so let me show you yeah
we shall limited amount of lines and
then you have you have a you have a
button paging button that will bring you
to the next bunch of lines and this is
another we didn't think that was a very
good tablet lack experience so instead
we introduced what we call continue
scrolling so you'll see when I scroll
the list here if you notice at the
bottom of the list you'll see there is a
text appearing shorty saying fetching
rose and what it does is exactly that
it's fetching more rows and I can't keep
on scrolling like this indefinitely
you're pretty much like you know it from
you know when you do picture search on
on bing or on on Google should you be
using that engine so that's that's
similar similar thing we do here so you
have a natural experience where you just
you know you just swipe and then you
fetch more rows as we go so this were a
few of the things we we have we've made
I can show you briefly just use you've
seen yeah you've seen the the list view
we have of course a different layout for
each type of page web the lucas i think
is good yeah show you that in more
details so let me go back to my slides
here okay so i want to talk a little bit
about the architecture of of the tablet
app and how how we actually designed it
so the technology we have been using our
HTML Javascript and CSS pretty much like
the web client that you might already
know so basically the most of the code
is the same code we we just render it in
different way and formatted in different
way there's a lot of CSS tweaks we've
been doing to to render it fast and
fluid there's one major difference
though when you're going to tablet in
the one in web client in every web
client each time you click on something
you go an issue request to the server
that's going to download and create a
new page download a new HTML page and
that will make the browser re rendered
HTML we render the CSS and we pass the
JavaScript which takes of course
sometimes on the other client side so
this is this is basically the old way to
do websites today when you do when you
do browser-based development what what
we call modern applications are are
doing things differently when you do
requests when you click on something
instead of refreshing the entire page we
do go and fetch just the piece of the UI
that needs to be updated we get it get
it back to the client and and adjust the
DOM and just change the HTML and it to
be changed so that means you always stay
on the same page and we call this a
single page application or second page
architecture so the the web client is
still is still working your way the
tablet client is using the single page
architecture which gives actually the
result of this is that you get a fast
and fluid interface and you get a much
more responsive interface when you when
you touch and when you use switch page
and all that which is something we
thought was important for for the tablet
experience so Cordova crow device is the
the rapper of all this it is actually a
web application as you understood by now
and Cordova is an open source software
that provides you a shame so it looks
like it's a native application
and that's that's how you can publish an
application which is web based on the
store on the on the Windows Store and on
the apple store there is the only you
can only publish native applications so
Cordova allows us to wrap a web
application into into this shell so to
speak so we can publish it on a story it
also has some other capabilities with to
that allows you to interface with the
the actual device so that was just to
give you a little bit of insight of how
this app is built so inside the app it
looks like it looks like this we have so
as that's you know that's an
illustration of whether i was just
saying so here you have our tablet
client which is basically the web part
of it and we have a browser control
inside and then the native app which is
a call of a thing so in in iOS
objective-c on android java and and on
Windows platform is is that we enjoy in
with jes application so you might be
wondering if I want to develop for the
tablet what tools what do I need where
what tools we need to develop for tablet
if you want your app your application if
you want to develop applications for
your users for tablet the good news is
that you won't need any of these this
was just to give you some insight on how
it is made but you're not going to need
to learn HTML or JavaScript or CSS how
many of you know JavaScript HTML okay
quite a few so that's good I mean you
might be using that for something else
but I get back to that so actually the
tool you need is this one that's the
only tool you need to develop for for
the tablet so you know since I
development as we love it so if you want
to try it out if you haven't tried that
yet I recommend that to you register for
the workshop tomorrow if you haven't
done so already we'll be doing some of
this and you'll see how easy it is to
to bring you know any application to the
tablet the the only thing we recommend
the only thing that you need to be aware
of is that the real estate and and the
whole layout of the page is obviously
different many buddy would be in the
windows client or in the web client so
when you develop your application you
need you need to test it on the tablet I
get back to that and and and show you
how easy can be done okay so with that
we're going to show you some more stuff
on on the tablet itself and I'm going to
head over to Lucas who is going to show
you yeah I won't spoil it for him so you
could guess hello welcome everybody so I
have prepared for the most for you and
that will basically walk you through the
sum of the tub experience so the first
thing I am going to show you is the how
web public plant takes the advantage of
all this office integration scenarios
we've been developing for quite a few
releases and how many of you went to the
other session in the morning were Vlad
and turban presented all this office
integration scenarios so i decide i have
the overview ok so what I'm going to
show you in that area is how we can
generate the report and then output to
two different formats so when we go to
the customer list and then from the
pop-up menu select a report as you can
see when we have a groups in the pop ups
we can expand and collapse them so we
don't take that much space from the
beginning so when I select the customer
top 10 reports what you see is the nav
request page and in tablet client just
to give better user experience we slide
them from the top so you have the
actions available at the top and they
are reachable within your thumbs so
after and basically this kind of view i
will use in those cases when user is
giving basic a choice and is about to
provide some input as opposed to the
message dialogues which we rendered just
to give you some information and ask
about the confirmation what is something
he or she wants to do or just dismiss
the action
so when I will try to send this report
to the given output I am shown the
message dialog and I can select the
specific output so when I take the PDF
document and confirm my choice the
report will be generated and then I'll
be asked to open in the supported
application so i will keep Microsoft
Adobe Reader sorry and then we utilize
the advantage of the Windows platform
and then the report is wrong with this
free screen and I know if you notice the
UI of the list change a bit and this is
some part of the adaptive layout changes
that Vincent mention area and when we
have that much space we can see only
four columns in the grid and when I
increase the width then as you can see
more columns up here and also the search
box is getting wider and when I'm gone
the opposite side and give less space
then I see only three columns in the
grid and then also the caption for the
new icon has disappeared caption of the
list gets truncated and they still the
lease is usable so we spend a lot of
time making sure that regardless of your
real estate we can get the decent
experience so this is how it works and
also you can of course select different
output so I can do the same with the
Excel and then the application will be
opened after deer produce generated so
that basically covers the office
integration scenarios and how the tablet
client takes the advantage of them I
sorry I've just doing the meantime click
the specific grow okay so when I go back
to the aisle here is the exa what's open
behind the scenes so when I go back to
the application yeah so the second
scenario is basically a bit more real
user scenario so you know and this is
also what tablet classes for my design
for so imagine that you are sized person
coming back home with the train like
normally we do in der mark because are
the cars are quite expensive so and then
you just received a call out of a sudden
and then your customer is calling
confirming that the deal that you are
discussing gallier is about to happen
and then you just sit on a train without
tablet you wouldn't be able to do
anything you will need to just write
down all the notes probably come back
tomorrow to the office and continue from
there with tablet you can just take the
tablet and i'm going to show you you can
just go to the list of the customers and
then you can use the search
functionality and search for the
customer you are going to create the
sizing for as far and then when you
present her then the search has done
have any one of you noticed something
different in the search function
lighting the tablet plans comparing to
how used to work we have some t-shirts
like good answer yes yes that's correct
so in tablet client is the first client
that we allow to search on multi columns
so I have a search for you so Thank You
Vinton so i will show it again to you so
i will kill the third value and then i
will try to google it sorry being it and
then I would have Vince again and then I
have Vincent so when I open the customer
and also something works to highlight
that you can tap anywhere on the row in
the list and then it ring you the card
and the tablet plans we just want to
mention renders cards which a bit
differently on a crisp and human is
explaining the differences because when
you look at the web plan the north of
our client then carved in document pages
they look more like the same so it's
very hard to see the difference of the
data directly looking at and tablets
client for cartridges just because
historical data for skypage is a very
important like in the case of the
customer is very important to know what
kind of Russian says with this customer
whether he is paying bills on time how
many open invoices he has information
like this that's why can I got a clicker
alright sounds one
so that's why this delay sir so that's
why we render boxes in this area on
the left hand side in landscape mode and
then actually I have to boxes but
because our adaptive layout kicked in so
then the flag boxes they don't fit on
the page that will not be displayed so
as we need to consider this when you
design your pages how much content you
can put for the devices they're going to
support because it will affect how the
page looks on the screen and then as we
can see you have two columns
representing all the data about the
customer so if I would like to proceed
with creating the invoice for my
customer and for any chance I forgot how
many items of specific kind Vince want
to order I can just take the advantage
of D extent the data types click on the
phone number and then I will be asked if
I'm to call Winston so I can you skype
or an application that i have set up
make the call get information and take
it from there so if i want to create
sell you invoice and i forgot to mention
that here i use the small business
profile specific version for tablet that
basically got simplified so then the
tablet experience is even better and
simpler so we can make your task quicker
so when i'm at the customer card i can
quickly go to sales invoice and i will
be presented again tas dialogue just
because this page is from this model and
I can already proceed with filling in
the information about specific size
invoice as you already see the
information about the customers already
prefilled based on the count as I am so
I can just enter item number and then
the informations of the field in and
when I enter the quantity of 10 bicycles
I can just save it then also we had the
functionality to make it easier that
when you hit enter the value will be
saved and then on-screen keyboard will
disappear so I can actually see look at
your data but again as you guys point
out it's very very important to keep in
mind simplicity when you design these
pages for the tablet
and frankly most of the scenarios you
will do on a tablet of course even so
saying I was like this are a pretty
advanced already but obviously you can
imagine it doesn't take a lot of fields
on this on this dialogue before it
becomes unusable so keep that in mind
when you when you design your
application you know try it out on the
tablet on the real device and you'll see
you know whether it works or not but the
idea is the idea is targeting scenarios
that that that can be done at that make
sense on the tablet you still want you
still want the web client or the windows
client on a real desktop to do like hit
hit bounce type of work and here also we
have the yet another example of using
the integration with office so for
instance you can post and send this
invoice and then you are scented the
message dialog asking you how you want
to handle it and of course we have asses
added to define the behavior of how save
as PDF work but i want to show dialogue
or we want don't want to shove it so we
have this election of the behavior and
then if i basically decide to send this
PDF also get the invoice sean is PDF and
also i'll be having the wrong side by
side together with the nav application
and as you probably notice now adaptive
layout also katene and just because now
there is less vertical space for the
current page the adaptive layouts which
to the port right so then file boxes has
disappeared and this is what we called
focus on content mode that what you are
focusing is the content and boxes
are available and we shall all of them
in expandable collapse panel so we want
to you are able to see all the
historical data by the customer and you
can already embed all the information
that a very important about specific
entity in this case customer so when i
will go back so that's everything about
creating the sizing voice and then the
last demo i have prepared is basically
how to put an image that fills the row
center and the content area because
probably can easily imagine that when
your application is very simple you may
end up in a situation
where there is no really specific
content you want to put in the content
area and the content or is this white
part of the screen that you can scroll
up and down and the one on the Afghan
side we call it navigation area where
you have all the navigation lights so in
order to demonstrate this to you we have
created new profile called big image and
also how many of you experienced
difficulties or a bit not intuitive
experience of changing profiles in the
web client or that was the nobodies
escrow yeah that's correct as fast but
in my mind it was very cumbersome
because you need to go to the lease or
rod center page open the search dialog
set for the profile page update the
specific profile mega set default and
then sign in sign out and now with this
release nothing being calm much simpler
you can use the profile chorusing
parameter that I know we see it well I
will try to point it now oh ok now we
have this parameter profile and then you
just type the name of the profile and
then after you connect to this URL then
you already be running in different
profile which I think it hasn't been so
easy ever in a navy so I hope that you
will take the advantage of this
functionality so ? at the end of the
wire and profiles and then the name of
the profile that will bring go directly
to the profile which name you've put in
the URL without having to change it into
into the profile and you don't have to
go and change it for that particular
user as a default profile so that gives
you also an opportunity you know back to
the first slide I had where you can
manufacture you your URL to get directly
to the right to the right page and to
into the application you can we can add
that as well that will also bring you
two to the right profile by the way yeah
actually I was wondering how many jobs i
should prepare for all those times when
the Navy is loading and I think I cotton
up to 10 but I heard it without some
network is maybe the song connectivity
just just drive every stop you a sec
yeah it's not work on go routes on it
yeah so as I mentioned like this is the
example of very simple row center and
then as if Republican notice this very
big white area and then if in our
receive some of the feedback from
customers that would be really nice to
put the company logo to fill the
continent and this is basically what we
introduced for tablets line so i will
show you how to do it as the preparation
work for this page basically we added
simple part that contains one field
which is an image that points to the
compound information table so i will go
to that page and edit it so i am
presented again the company cars page
and then i can just go and select a
picture so this is how the file chooser
looks in the tablet client and then
already we take the advantage of the 95
choosers and we can go up so using
pictures actually that's where you kill
me you guys I forgot to feature there
yeah not just take a picture with the
the camera they'll be you know just okay
i will just disconnect the keyboard and
how do you actually take proof surface
do you know maybe someone can tell it me
technology always been surprising all
right we show that later right let's
give that yeah but basically if you go
back to your own yeah presentation so
the idea is that you know you don't
necessarily have content you want to
show you are on your roll center because
we found out that the tiles in in the
design we have the tiles if you go back
to your roll center the tides become
really predominant in this design and a
lot of people actually have desired to
use them as your entry point as your
navigation point for because it's very
tablet like this you know these big
buttons so so basically what you what
you can do there I'll illustrate to you
in a second you can you can put your own
logo or any picture you money the rest
of the content that's that's what this
feature also to you so that's all the
most about the right questions no
problem alright uh so why is the clicker
let's see what's next yeah so before I
was mentioning that you need to test on
the real device but you don't actually
need to test all the time on a real
device when you when you're going to go
and develop so the tablet experience
that you've just seen run just as well
as a browser you don't actually need the
app to do to visualize it so the only
thing you have to do is is hit this URL
so the URL G server and your part and
your instance as as always as you use it
on the web client so sem urs as you
would use for your web client but
instead you append this tablet or aspx
at the end and that will that will
render the in the tablet mode so I'm
going to show that right away so you'll
see how that works me switch back so you
can see my screen
alright
so just go and so I've prepared the URL
link here so you can see I just have you
know I just I just need to enter this
URL which is so the part before tablet
aspx is just if I don't so let me let me
show it to you know without so you
believe me if I just go to this URL this
this is the web client so I just log on
here and this is the web client so that
site look like right as you know it now
if I instead go tablet that aspx here
then it's a tablet client and I didn't
have to log off and log on because I'm
already logged on with the same user so
basically when you when you grow and
develop for your for the tablet you can
you can test the on your machine on your
Windows machine directly in the browser
so if you come to the workshop you know
we'll do a lot of that that's that's
really easy you develop your pages as
you as you always do in the in in
seaside and and and you go and just
press f5 on them in the browser and
refresh the page to see your changes as
you go now that doesn't really replace a
real development or real testing I mean
on the on the on the device you'll you
will always need to test ultimately on
the device to make sure everything works
as it should but there's something else
I want to show you because they there is
a lot we support a wide range of tablet
and with a sawi support of course the
surface and iPad but we'll also Android
and especially Android have a you know
it's very fragmented market as you know
there's a lot of devices out there a
different resolution different form
factor so you can you can use google
chrome from as we cool feature for which
are going to show you in the minute by
the way if you want
if you won't have an idea how your
tablet application is going to look like
on the surface then use internet
explorer but but if you want to have an
idea is going to look like on an iPad
you can use google chrome that's going
to give you almost the same rendering
that that's on the Empire now that's
because of the browsers that libraries
that are used by by by the ipad versus
the windows platform so it's always a
good idea to try non both there but we
need a lot of work to to basically
shield you from all that stuff you
shouldn't you should have to worry
whether it's an iPad Windows platform or
or an Android platform a it should work
on all three platforms there are very
very small differences they are so small
I don't even you know bother mentioning
them so yeah it is to you know we've
done the work so you guys wouldn't have
to do it but anyway the sort of cool
fish I wanted to show you in in chrome
wise you know if you go in and press f12
which is the developer tools for for
chrome so you'll see a whole bunch you
know what you see on the left side on
the right side here as you know aw d
HTML looks like and the CSS and all that
which is also great but they have this
they have this device simulation mode so
you can go and and and select you see
the old bunch of device here and let's
say you want to develop for the google
nexus 7 which is a seven-inch seven-inch
tablet and you selected the this
particular device and the screen and the
resolution are going to adapt so it's
simulate that device you can see how
it's going to look like and you'll
notice that we render fewer tiles for
example on this one and that's also what
you will see if you start the tablet
client on the google nexus 7 that's
that's how the rendering will look like
you will have you know you see how much
of the area you'll have to scroll on for
for showing the different parts you have
a normal center and all these kind of
things so I thought I'll I'll share this
with you because then you can that
allows you to do a lot of testing
directly on the browsers and without
having to invest in a whole bunch of
devices especial
if you're doing team development you
only need few devices to do your your
your final testing but you can do eighty
percent on the developer on the browser
actually that's how that's how we work
of course we bought a whole bunch of
device to test but most of the time we
we are using the browser and and and
testing on or on our windows boxes when
we when we developed so that was the
development experience let me go back to
my presentation yes the next thing I
want to talk I want to talk about is the
deployment because we have you know
through our tap program and and and you
know with the people who have been
already using the deploying the app
we've had a lot of issues with the
certificate so I know if you notice but
all the URLs we've been you have been
using and we've been using to to log on
to the server are using HTTPS and and
for various reason https is is required
from the device so let me get back to
that in a second so this is you know
this is the regular regular the
development topology you have for for
your application there's the server and
and at the database and the web server
and that could be other on-premise or in
the cloud it doesn't really matter for
for the topic here and your internet
could just as well be an intranet but
the problem is that so you might have
noticed that if you install the web
client from from the from the demo from
the Installer you just install the demo
and install the web client what we do is
we install what what's called a
self-signed certificate which is not a
real certificate is one that you just
can make yourself using some comment
line tools but that means that what it
means is that is this certificate is not
trusted by your browser so when your
browser sees this certificate is used to
encrypt the communication but
doesn't you know it doesn't it's not
registered so you know where you go and
do a payment online the certificate that
I use are known certificates that
trusted certificates so that's why it's
an exploit will show you a green bar and
all you've probably noticed that that
means that everything is okay the
payment you are placing is secure but if
you use ourselves a self-signed
certificate the browser wants you about
it and and it tells you you are going to
assign it has a certificate but I don't
know who these guys so it's going to
give you a red bar on the address bar
but you can choose to continue and view
that site anyway and this is all
something that that takes place in the
browser you get a dialog Boston telling
you this site is potentially harmful do
you want to continue and all that I'm
sure some of you have experienced that
this test netic does not exist on the
device or we would have had to implement
all this interaction if if we wanted to
provide a similar experience so instead
we chose to say okay we you have to use
HTTPS because you know of the will be
supported the different carling
encryptions and if you want to use https
your password and username might be
transferred unencrypted on the on the
wire and of course you know on that so
that means that you need to have a
signed certificate so the solution is to
acquire one usually it's it's you can
you can have you can buy one for for fee
which is a but I'm not sure with
something about five two hundred dollars
depending which which provider you're
using and you need to install it so
that's a that's a one time that's the
subscription that you only need one
certificate you don't you don't need one
for each for each client you only have
to have one on your own your web server
that's all it's just a file you copy and
it has to be it has to be manufacture
you know we had TB to the name of your
domain that you're using so you only you
can use it on you on your own domain and
so you'll need to invest in that if you
if you wanna be serious about providing
tablet to your customers tentatively you
can use there's other ways and and where
we can actually use a social scientist
ethical which can be good for
development and and we we have written a
blog post that describes out to do it it
is a little bit tedious you have to
actually install and trust the
certificate on device it's different on
all three platforms or that that is done
but if you if you want to do that if
you're interested at the end of the
presentation there is a there is links
to the blog post or just look it up on
the on nav team blog it is there there
is a very thorough description how you
can do that kind of thing alright a few
tips and tricks actually the most
valuable trick is to formal experience
to be able to restart the application on
the device and actually not not
everybody knows how to do it so that's
why I have that sly so this is different
all the three platforms on windows with
there's the good ol task manager which
you you know from windows so you go and
kill the the process on iOS that's how
you do it and enjoy this difference so
just for reference if you you know
should Europe go into a mode when you
you want to restart it it shouldn't
should but you never know alright so we
did a whole bunch of other improvements
to the client that's odd that was a
tablet but we also need a few things
which which one not only for the tablet
and Lucas is going to show you what
these things are yeah so I guess you
probably noticed that I don't do much
power point and start reason for it one
is that I wanted to actually present as
much of the cool features with it for
all of the clients and as was the second
one just before I went to this
conference my wife show me the article
containing the interview with satya our
new CEO and then he said that people
over 30 they do PowerPoint and people
below they use new tools so i decided to
have no power point whatsoever so what
I'm going to show you about new improve
my
there are basically four things one of
the things with it is to improve how the
mandatory fields are working so before
we were supporting only mandatory fields
on the primary keys now we hide the
behavior and I'm going to show you how
does it work also we improve the
rendering of the total ink on the
document pages mostly so the next thing
that was very well needed by men of you
and we got this feedback is to support
fixed layout in the web client and then
that works very nicely in bobov declines
tablet and web and then the last thing
is because we utilize design framework
between two clients also the web client
took the advantage of the features in
the tablet client and also support some
of the adaptive features that i'm going
to show you so i will start with
presenting to you the mandatory field
behavior and i will use the same
scenario as previously about creating
the sizing voice so i will switch back
to the original profile we started so i
will just always everybody know the
password it's a super secret password
don't repeat it to anybody yeah that's
why we surface otherwise ipod will show
it to you so not very smart so do i need
to use some of the tricks for instance
route or yeah i think it's good
suspended also probably yeah sorry
yep the application is back so if we go
to create synergy voice and then we
start from the north center this time
then you will see that this is the
document page in tablet client and if
you remember how the cart page look like
in tablet client was a bit different so
as you can see there is no book
sorry on the left hand side this page
actually doesn't contain five boxes but
it would have that will be on the right
hand side and that's the difference in
the ice cream mode and here's just
because we're creating the document and
the document is important at the time of
the creation later we don't have to
actually go back to that and see the
historical data I just needed how it
looks like at this particular view and
also the other difference is that
previously were creating citizen from
the customer it was shown as the task
dialogue just because it was run as
model and here we have as we call it
full screen page will have a bit more
content so as I is something you may
want to consider when you design pages
because times I does get a bit less real
estate because then you to have side
margins the looks like the ties dialogue
so on this particular page I have
actually two fields that are mandatory
one is the customer name and the second
isn't a number so I'm going to fill in
and then you will see how the behavior
is through the time so and this is the
example of the look up from model is so
then I co I so I can search I have the
textbook theory on the right hand side
oh that i can use and search for the
customers interested in or i can just
basically pick from the list and like
Vince I saw you earlier continues
crowing works here as well so i will
pick exemplary customer as you can see
now the mandatory field indicator is
gone and when i go to the item number
and type i want to disconnect and
connect a keyboard now i think it's just
because it's saving so it's just locked
Oh
I think that just disconnect from the
keyboard and hold it yes so now when I
safe as you can see mandatory fee
indicator has disappeared and now I got
the other another one for the quantity
field just because for item it is
important to us a feeling the quantity
and this behavior is control on the CL
side so now you have the flexibility of
making any field mandatory and also
control it on this year site based on
your business logic so you have full
freedom and power of guiding your users
how the specific data should be provided
there used to be something that was only
for I mean this you've seen the red star
before but there used to be something it
was only for ID fields which we are set
as as as mandatory but now we will
enable this for for the fields so you
can you can enforce the entry of any
type of info did I know yeah and the
other thing i want to show you on this
particular page is actually taught us
that the featured into the small
business application last release and i
don't know how many of you noticed but
there is a difference in the rendering
and doesn't one of you know how we used
to render this kind of layout in the
previous release i have few more
t-shirts so don't be shy sorry
you mean yeah but also we did some of
the tricks to create this space between
the list and the group and also to
create space between those two columns
but just don't to spend more time there
tisha anyway for ya 45 yeah so basically
here using the fixed layout with one
column spreading across the entire part
just to give some vertical space and
then for the horizontal we add yet
another group so instead of two columns
where like we have here we had free
column so then those groups in the end
got thirty-three percent of the entire
weight instead of 50 like it is now so
we have not now not better use of space
and actually you can see the fields
better so is one of the tiniest
improvements with it and I saw Thomas
alia show you some of the HTML
improvement so we take the advantage of
it the next thing with it is the support
for fixed layout and i added action to
go to the fixed layout page and you see
this lighting so it means that is very
quick to render so they see how it goes
and then I hope you should like it this
is the fixed layout page now in the
tablet client and looks exactly the same
in the web client of course with the
differences how the specific pages being
rendered and i will just switch to the
web client i hope i can do it and then i
will show you how does it work in the
web client so i will just use my
favorite browser remove the tablet that
SPX it's wrong project you need to
placate the protection it is not project
and so okay so i just need to oak is a
project sorry about that yes here we go
so i will go back to my right center and
i will show you the fixed layout so you
can see how is being rendered and when i
scroll down is nice and tidy fixed
layout page that you can take the
advantage of those kind of pages and are
very important to show any kind of
statistics for different kind of data
and the last thing I would like to show
you some of the adaptive layout features
so now this is the right center and as
you probably can see by default we
render all the content into groups to
columns so and that's very good when you
have very wide screens but when you have
a bit narrow screen what happens is that
instead of rendering this two column
layout the column switch and then render
them 11 below the unloader so we can
actually have less vertical space and
then actually you can see more data with
that in mind so that's 40 centered is
not that much of the improvement and
also you can use the feature from the
previous release focus on content and
you can actually see more but when you
go to list then the changes are a bit
more visible as you can see the faq
boxes got a bit more vertical space so
you can see more of the captions which I
want that are longer and you see the
vertebrae's narrow but when you will
continue decreasing the width then you
will notice that boxes will get
narrower like this and then they will
disappear in the end so then you can
actually see the lease and then when you
focus on content you actually can get
quite decent overview of the list page
and and also we did something for the
document page as you can see now the
layout like in the tablet client
transformed to the single-column layout
in fast tops and when I will keep
increasing and maximize the dialogue of
course I have two columns layout and
when I will go yet another time on the
opposite side five boxes will disappear
I will switch to two column layout like
now as you can see I have two columns
and the fact boxes disappear this is the
single column and I can keep going and
then the capsules go over the values so
then actually I can display the document
page on basically 200 pixels which is
quite a I think very very narrow and
done of course ribbon adapt to it and
all the groups get compacted so there's
all the demos I have
for you thank you so you guys can you
please switch of you are done with the
surface right yes I no no please switch
to the ipad to the ipad yes tonight Wow
ok so the the next thing I want to talk
about is about it is extending the the
tablet client last year how many of you
were at the conference last year so if
you've seen the if listener session on
the on the client we showed demoed how
to do a an ad in you I add-in for the
client using HTML and JavaScript so I
want to I want go through the demo again
there's lots of resources on the net
that the demo are to do that we have
walkthroughs in or in msdn and they're
also you know people have a code they
more to do that and there are some
videos on YouTube that show you how to
do then details but I want I want to
repeat the message about you know if you
have you still support the the dotnet
added framework for for you I but if you
want to do future-proof edits if you
want to invest in this UI you have to
switch to that with HTML because that's
the only technology that is
cross-platform and supported on all the
clients so today if you do well if you
do an ad in or have an ad in which is
developed using the.net technology you
will only work in the windows client if
you if you do the same thing in
JavaScript and you can do everything
that you can do in C sharp and-and-and
dotnet you can also do in javascript
HTML you're you're adding will
automatically be rendered and surface in
all the clients that's the windows
client the web client and the tablet
client so if you want your you are
adding to be on a tablet there's only
one way is HTML and JavaScript so
I'll show you actually some of you know
the fact that now we are on a touch
interface hope this works yes you go so
now that we are on a touch interface
that gives you the opportunity to to do
some some cool scenarios see that's the
trigger but we starting the other use is
so it works all right so you by the way
so this is this is the eye it looks on
the iPad you know I could be lying to
you it could be not be an ipad but it is
an iPad so you see there's not much
difference between the surface and I
panelist that's you know what what we
were striving at so the UI will be the
same so once you have your application
on 11 devices you can have a lot in all
the eyes but i think i can i can show
you the adaptive layout on the on the
ipad i couldn't show you on the surface
when i'm projecting but the ipad
actually is a little more responsive to
that so you see if i look I'll show you
some of this already by resizing but but
thats also happens when you of course
turn from portrait to landscape anyway
so i have ever smaller a small adding i
want to show you if i go on the sales
invoice take any cell divorce no less
than success coach sorry icons escort
and open any insects quote
so I have lost the connection we go so
what you see here is a JavaScript head
in which which I've made and that's
that's far if you want to sign the
document directly on the tablet he can
take a pen I'll take your finger and can
just write in the box so that's an eye
as you can do with the tablet and you
can go and and actually save the picture
and we can have a blood-filled in the
table and you can go and when the user
press accept can go and save the
signature and and save it for later are
the printing or for reference for any on
any type of document or page so that's
just that's just an example of the cool
things you can do with javascript and
HTML and and with with the with touch on
the device this this particular adding
published the sample on on our blog on
our blog team side and and you can
actually download the code for for this
from the image DN sample library for
those of you were coming to the workshop
tomorrow we've got to do some some
tablet development but if you're very
fast and you can go through what we have
on the program then we can we can look
at some of these things if you're
interested all right
so yeah this is slide on the on the deck
with all the resources so when you
download or if you want to download the
the presentation there's all the links
to how to the blog post i was talking
about i've been talking about during the
presentation and there's plenty more
just choose these ones as the you know
because that's the one that i've
mentioned during this presentation but
there's a lot of resources out there
we've put out there for you know getting
you started sorry and sorry Vincent yeah
and that's what if you go back yeah and
I so there is this link at the bottom
and there's explain step by step how to
add the image to the row center so
because we couldn't make it here so then
you can go and refer Today article and
basically go through it and then you
will see how the page looks like in this
particular case do they know that with
you know that Lucas was showing you it's
described the earth step by step alright
so the message we wanted to convey to
you guys during this this presentation
is that there is absolutely you know
almost no learning curve for developing
for the tablet the development you know
development process you have you can
keep you can develop the same way than
you always been developing and and you
can get you up very easily on the tablet
that was there was alcohol and and as
you as as you can see you know there's
basically no way for the only thing you
have to be aware of is the real estate
and which is obviously smaller and would
be on the on the on a desktop but also
the user experience you you really want
to think of your application and you
users using touch so not too much
keyboarding so you know keep these
things in mind there's a lot of real
possible we use I mean the pages you
have already you can you know you can
take a page you have and you know seal
you put render it on the tablet an
opening on the tablet co it looks like
maybe you can use it as it is maybe you
can't maybe you have to tell you it a
little but the
you can reuse what you already have so
although all the code you have written
the business logic you have written on
your page is basically reusable and
there's low cost the development is is
low cost you don't need to invest in in
a lot of device you only need to have a
few of them you can do most of your
testing and most of the development on a
regular windows box and and and there's
no there's no additional deployment
costs when you got to deploy your your
your application you deploy it as any
other application if you have a web web
client a web server install that's all
you need so if you want a tablet client
you just go and install the web plan and
you'll get a tablet client with it so
basically that's it I hope it's going to
be easy for you guys to do a lot of cool
applications for the tablet so now we
have about 20 minutes for plenty of time
for Q&A so if you're any questions fire
away all right is anybody you can help
us with the mic okay go ahead hey good
yes yes so the question the question is
I repeat the question so everybody can
hear this very good question the
question is is there wait we have a way
to differentiate I guess you mean in the
code whether we're running on the on the
on the web client on a tablet and the
answer fortunately is no so in the
current version of nav you can
differentiate between the windows client
and the web client but you don't know
you wouldn't know in your code whether
you're on the tablet or on the web
client but the good news is that we
actually have that in scope for for the
coming beliefs so and we will will
implement that actually we implement
again by now and so we might we might
even consider back touring it to a
cumulative update if you think that's
important but let us know but that's
that's something with that something
will have any time soon excuse me
there's a question here on this yeah
yeah so the question was do we need two
pages yeah you might or you know you can
control it through the profiles as well
question over there all right why can
you collapse first step on a cart page
I'm sorry can you repeat you have car
pages you have lots of fields yep you
can fast steps except I can't collapse
them now so that's not the that's not
the device we have run out of the tablet
but that's also something we are we have
been considering force which you read
well it's not instant that's not
possible now on today's implementation I
cannot answer to that because also why
this is not supported since two thousand
or two it's just because with the modern
UI like office without slides
introducing we decided the for sympathy
reasons we decided not to have the
functionality and then with the modern
no changes this feature got removed and
then also we got the feedback that is
very needed and you know we might do it
but they're not really yeah but we are
considering in there for the next
release but that was like conscious
decision that we decided to remove
to simplify the UIF have less clutter
together with the modern I changes the
question over there all right sorry hey
are there any plans for offline
application I think this one is only
online when you're on the internet or
extranet that's correct it's we don't
have any plan currently for for offline
but that's that's correct this one is
requires the online connection there is
a restriction on a screen size is it
defined actually by a physical size or
by number of pixels so so when you when
we resize no no I mean oh no what size
devices may tablet client work oh yeah
ok so we support down to seven inches of
screen I mean that doesn't mean you
cannot run on less than seven inches
yeah do you want to deal teach yourself
to people were asking nothing do you
want to build t-shirts out yeah yeah
yeah I can do that no problem yeah so so
we support with a recommendation is that
you you go for tablets which are seven
inches and above I and the resolution is
pretty much any resolution on the
tablets which on the market today it's
more you'll find that the limiting
factor is model screen size rather than
the than the actual resolution of
debates almost tablet today the one the
one the operating system we support have
high enough resolution so that's not
what's the problem the problem is the
size if you go below your like if you go
on a smartphone so first of all we don't
support phone but thats that's not going
to end well well you can try though I
mean we officially support 77 inches so
if you come to us with the request for
something that doesn't 1.5 inches we
might not do it but but you potentially
you could design a page that would one
on five you know try it out if it works
for you it works for you right
but we chose we have to limit our our
matrix of testing you can imagine you
know when you take you know all the
devices all the form factors all the
resolutions all the u.s. that can be
installing there's really really a lot
to test on so yeah that's another thing
when you might want to choose for your
application for your users it's a little
bit dangerous to go and say uzak use any
device you want because you know you'll
have to support all the devices so
you'll be aware of that you might want
to say we support that particular device
but up to you of course sorry and I
classic on to that Vincent we could also
the reason why we support seven inches
an app is that our you know Kyle's do
the experience is designed to use with
two hands right so when you look at all
the menus and items that are designed to
us with two hands so that's why they're
either on right or right hand side and
for fun most of the tine earphones use
with one hand and then design is not
ideal for phones that also is the other
decision is why we don't support phones
but should I give one teacher to someone
Vincent oh yeah just your people are ya
with their asked questions yeah deserve
it assure the question over there let it
go I is it possible to disable the
adaptive UI so for example if you have a
list with ten columns and you want to
show all of them at the same time always
and have a horizontal scroll bar is it
possible you mean on the tablet yes no
it's not possible so right now so did
you we will cut your code so that we
made that choice very constantly because
we want we want the development to and
the developers to really think about
providing a simple user experience on
the tablets but now we realize you know
that's that's that's the decision we
made we've got a lot of feedback on that
especially the number of columns we knew
that that would be a sensitive area and
that would be something that people
would challenge so I can tell you that
we are actually looking into providing
some solution to that particular problem
for for the next version of the tab
but we are aware of the fact that it is
it is a limitation that you know which
with that you know you'll get back to us
and tell us you know that work for you
this this limitation can you actually
make it work and you make you said I
work with you know with this you know
limited number of columns you keep in
mind that the you know what we're
thinking is that the same tiles you've
got to do on the tablets are not going
to be you know the real adventure
neither the head stamps another it's a
small like you know you're going to go
look and you kpi's you know do simple
tasks you know it's like you know you
know the things you do with your tablet
today you don't go and write long word
documents long letters what you did do a
lot of formatting or stuff like that on
your tablet you know most people
actually go and do that on desktop so we
expect you know we expect that would be
the same for for fine alien any RPG but
we're looking into providing your way to
show more columns with a still cool you
using user interface and experience in
case you run into troubles with the
rendering of your page is there an
alternative for the control out of one
the about page said you have any normal
client so you mean whatever troubles are
you thinking normally you you can say
ctrl alt of one and on the windows
client to show up we on which page you
are and for Deeping testing purposes is
there another way to go on which page
you are on the not other tablet but you
can always you can always run the
windows client next to it and and and
see you know you can have both
environment running at the same time and
show the same page and if you want to go
and look at the page and a page
numbering again yes so it's still only
the windows client that allows that
today but that's all you can use you
know like what you call it fiddler and
the last to see the JSON and the
metadata we use and then as we can see
what the page name is right that's a
little bit is a bit low level but of
course but your way of getting around
this problem right I can with that but
you have to go through the complexity of
the communication right but yeah that's
yeah I'm just ask one question and do
you plan to support some kind of
notification systems or are you planning
to to include push notifications or
something like that that's a good
question we don't have that so you're
thinking about can you use can you
integrate with a notification for
example on the iOS or on Windows now we
don't we don't have that at this time
but that's definitely something that
we've been talking about but that would
be cool we could send things into the
either on the tile and the things like
that and I was like that that become
interesting of course but we don't
support it at this time hello you said
you don't support offline mode yes is it
in plan anytime soon it is not a planet
at the moment because it's all fine when
the network is table and say and when
it's good network but there are a lot of
third world countries and the country's
development that require offline mode
and they will always choose some other
customization of dynamics mobile
application than this yeah we're aware
of that so what we did beside beside the
rendering part of it and delivering the
UX on the tablets we aware of that that
you know we we don't have a complete
offline mode at this time but I don't
know if you see the last connection a
couple of times during the presentation
so we invested the first thing we did
when we started developing on a tablet
we invested a lot in in in making the
whole connection resumable we call this
saucepan resume so you'll experience and
that's something also that benefits the
web client today's it's the same
codebase basically if you lose
connection which is much more likely to
happen if you want a tablet like you
know sitting in a train and go in at all
or whatever that will we've done a lot
of work to to make the resume
seamless so so no we don't have offline
but but we have a better experience
where the connection is shaky you can
you know you get the gray bar saying
your connection got lost you click
resume and what we do is that we try to
get you back as you know as close as
possible to wear you wear when the
connections got suspended so of course
if you have a dialogue open and you know
in the middle of it including a lot of
cl code on the server side we won't be
able to recreate that entirely and
resume where you wear but you most of
the time we can get you back to the page
you wear you wear on at the moment of
where you lost the connection when the
connection recovers we try to recover
first automatically so sometimes you
won't even notice that the carnation got
lost temporarily and if you if we really
don't then you get the you get the
dialogue you get the bar at the at the
top and you go resume when the
connection is back and and you can get
back to the page most of the time it's a
possibility of an automatic lock out of
the period of time especially if you
lose the connection for example so
that's the that's the usual time out of
nav we have that on the web client today
and that's exactly the same you have
here and there is of course most device
also support locking out the device
itself which we might want to use but
but for nav we have we have a timeout if
you see the session is not used for a
while then we'll go and and and logo de
Graaff automatically some question on
the other side the other question over
there would it be possible in future to
be able to specify a different default
card and list paged for use with the
tablet client or different clubs or a
different card in this page so obvious
you've got a property to say what your
card pages what is your list page for a
particular table so you've only got one
kind of like choice I just wondered if
you consider in a future be allowed to
specify and have another property
specify the card page for the tablet
client and the
page the tablet okay you made your media
development environment specify that the
ends I yeah so yeah so we we consider
that as well so I guess you know just
just correct me if I'm wrong with what
you would you suggest that we would you
would have a page so one version of the
page for for the tablet and another
version of the page for the following
web client and the page would render
automatically depending on which which
which device you're on right that's what
you're thinking right yes yeah so if you
go like from from a list and you open
the record instead of hope we're not
just one page and it has to be a
compromise between yeah we were so
different clients if you had to two
properties on the one time if you run
under say like the windows client here
I've got one page if it was on the
tablet client to get open up a different
page so so you could customize for
running on this so you would you would
customize in the development environment
so that we don't we don't have that's
also something we discussed at this
stage we don't have we don't have any
plan on implementing that particular
feature it's all the reason why we we
didn't go that way was first of all we
wanted to provide as much we use as
possible for people you know for the
existing pages so the idea was that you
could take any page you have and and
basically you know rendering on the on
the client actually we you know the most
of the apps you've seen is what we call
the mini up it's not it's not made for
the tablet originally that's the app we
had so we didn't actually you know when
and develop an app for the tablet we had
this one which was for you know simple
use and which was that was that was our
target apt I was the app we use for
testing the tablet so that that's you
know that's that's the idea behind it
the keep in mind that if you if you go
down that route you're going to add to
the complexity of your application
you're going to branch in essence you've
got a branch your code into into 22
paths which will have to maintain we
didn't think that was a good idea now
will you know let's see how you know how
the future goes with this maybe they
will have to do that some stage but but
I'd rather you know I'd rather advise
you to
you know use the profiles use you know
maybe if you have pages which are very
complex you know don't put them in your
tablet app use a different profile for
your tablet app and just go to the pages
or do a simplified version of these
pages that's that's what we will come in
oh that um is it practical for a partner
to manipulate the native CSS to brand or
reskin the tablet app so a good question
are you asking whether it's practical or
it's doable so it is not actually
something we saw it's possible yes I
mean we can't we can't prevent you from
doing it the CSS is is available on the
on the on the web server and you can you
can actually override it if you want
like any other web application if you
have access to the server now that's
that that was that was actually a
feature we have been considering and and
we might we might do it at some stage so
so basically there are many ways to do
that we can we can what we would like to
do if we get you know if we get the time
to do it we let literally all the other
features we want to do for you we would
like to isolate the CSS like the few CSS
stuff that you could override easily
like in one file so you would go and and
you could say okay change that color
color of the tile of color background
and and you know like like the five
things that that would be interesting
for you to bring your your your
application actually in order to mention
that if you read in the in the small
small pamphlet that comes with the with
your badge it says that on the
description of this session it says that
we will also talk about some more
advanced things advancing I also if you
want to you know do your own app on the
store that's what it says actually I
didn't talk about that and there's a
reason for that when we started
developing for the tablet we did we
didn't actually plan to develop the same
app and publish the ad on the store when
we
at the very beginning our idea was that
we would only do the you know the the
web part of it so so you know we /
tablet that I specs are shown in the
browser and we let you guys do your own
app the idea being that you could read
it with your with your own your own
partner name or you wanna ice be named
or you know whatever kind of branding
you would do you want to do and then you
could publish it under your company name
on the store because back then we didn't
know how hard it is actually to make the
same part of it we thought it would be
relatively easy we thought it's just a
web control you just put it into some
native app and just a web control and
that's it I can tell you where that we
got a lot wiser and and I mean you must
be you should be glad that we did the
work for you because this is really a
lot of work and I think I think that
would be almost you know very difficult
to actually go and do this now we're now
to Dueling if you want to do it it's
possible but it's it's really a lot of
work and our intention was to actually
show you from all that these
technicalities and we publish this app
for you guys so you wouldn't have to do
that work now we're aware of the fact
that branding is important and and
that's this is something we'll will you
know will consider in the future as well
giving you possibility to brand the app
and we might even at some stage make the
code available for for the actual shame
also be aware that's that's that's kind
of you know that's kind of complicated
it's nice re an easy thing to do any
other question in the demonstration you
showed telephony and skype opened yes do
we have any possibility or ID to use
local telephony possibilities because
every tablet has its functionality yeah
I believe I can take it because we use
the call to protocols or whatever
application you have installed on your
device to handle calls like link or
whatever we can use that one for making
a call in this case we just had a device
with skype setup so that's why open is
the default application
sorry quick yeah can we use this from
our every tablet has a possibility to
phone without nav Asian clap we use this
telephone by nerve Asian yeah it's multi
embedded in a telephone that is possible
if you as you cash said if you if this
application on your tablet actually
recognize a the protocol which is the
one we will put in the inner tablet you
know what I happen what we do the way
the weights render you see it's rendered
as a link as a hyperlink in the tablet
you can you can tap on and there is a
there is a tag in front of it that says
that this is a telephone number and if
the if your app on the tablet support
that protocol that should work but it's
not something we have you know it would
be depending on the app whether it's
support it or not but but we know for a
fact that you know you can install skype
it works you can install if you only
have link link is going to work with
linux got a kicked in if you have any
other 30 app that is supporting the do
telephony protocol that would be the one
that unless you default one that's been
the one I going to be launched when you
when you tell these things so try it out
you know try that just take a customer
card and put a put a telephone number in
it and and and see you know see if it
works oh hey and am I able to hide and
show feels on the page by an action or
something so is there personalization on
the page no with some code with an
action yeah actually I can yeah we can
do that then that's on pages in the SMB
profile small business profile that
actually do that so I think on the sides
infos you can show additional bill to
address and stuff so we can use the
actions and show in height so dynamic
visibility supported by code that's very
cool yeah but you know we can control in
CI by expression and initial height
items and you can trigger this by a kiss
that works sorry for it's another
question here
so the profile parameter in the service
URL is that something that's also
supported in the other clients even the
windows client would be handy to make a
quick switch to another profile that
it's supporting the web client for sure
whether it's supporting the wheels
client I don't I don't remember i have
to dress but give it five yes shouldn't
be shooting me a mail and I'll uh I'll
find out okay or find me you know find
me off in the expo group it makes poor
area they don't I'll find somebody who
can answer that question but I that's a
good question or river so you mean
through the you know the regular
protocol if you go like ms dynamics nav
and you know yeah I'll find out I don't
remember sorry any other question you
look at 40 seconds all right then if
there's no question thank you all for
attending this session there was a
pleasure thank you thank you vincent and
actually see thank you cash actually
been asked to announce that the the next
important thing is the is the dinner
