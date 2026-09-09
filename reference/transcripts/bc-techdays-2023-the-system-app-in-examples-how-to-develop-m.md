# BC TechDays 2023 - The System App in examples. How to develop more with less lines of code

- **Source:** https://www.youtube.com/watch?v=a1p8fTFPVwI
- **Video ID:** a1p8fTFPVwI
- **Channel:** mibuso.com
- **Published:** 2023-06-29
- **Duration:** 88m28s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Hello and good afternoon to everyone.
One final session between
this and the beer. So
stay stay with us.
Let's get to it.
We hope you will enjoy.
All right, but we would like to start
few words about ourselves before we will
go to the session. So my name is
Krzysztof Białuś.
I'm from Poland and I know that it can
be for most of you very hard to
pronounce. So
a lot of people say me Chris or KB.
I'm a developer and I'm a system
architect.
I'm working for ESV and also have my own
company. You can find me on my blog and
also on the meetings which we called BC
Beer in Us from time to time we have
online meetings and also live meetings.
So please follow to see when you can
drink a beer and have fun.
Highly encourage you to join the BC Beer
in Us. That was a lot of fun. So I'm
Jesper Schuldt Vedel and I'm the
engineering manager of the Business
Central application foundation team.
My team is mainly responsible for the
system application
developing all the modules that you need
to build you know, world-class
totally ERP products on top of it.
And then also the reason why I'm here
today with KB is that I'm also
responsible for our open development
story.
So I'm going to talk about half an hour
like
about like if you would like to
contribute, if there's something that is
missing then how can you go about doing
that?
I've been on the BC team for 15 years
now. Time flies when you're having fun,
I guess.
Um
And then well then the last mission that
I have is kind of you know
trying to bring the community in
Microsoft even closer together than we
already are and I think open source or
open development is one of the ways to
do this.
So yes.
Okay.
to it, KB.
Yeah, so let's start with the system up,
but
how Business Central is structured now.
So,
let's go through from the
from the top in fact, not from the
bottom. From the top, we have PTE apps.
This is which everyone of you probably
is doing those
apps. So, pertinent act
apps
where customers need some special
development.
Then we have also ESV apps where you can
find them on AppSource. Uh and with some
uh new functionality which probably
extend the base app in a lot of places.
Uh of course, we have base app where in
fact all the business logic should be
and only business logic.
Uh but we will find their customers,
vendors, and uh this kind of this uh of
objects.
But the main goal today is to talk about
the system app and what we can find in
the system app and what it is. So, at
least for now, how it is, the system app
is a by is a
a lot of libraries which can be useful
for developers. So, I guess most of you
are developers here.
So,
that can be uh used and in
uh few clicks, we can just develop new
functionalities.
So, how the
by a system app looks. In fact, it's uh
it contains a lot of modules which you
can think about LEGO blocks. And one of
them, for example, can be Azure storage
integration or camera and image. I will
try to show you all of that.
Um but there is much more.
And
likely, uh thanks to Yesper and his
team, we have access on GitHub to all of
that. So, hopefully you can see it.
Uh if you will go to GitHub
/microsoft/al
app extensions, you will find modules,
and then you can go to the system, and
you will find a lot of
modules in that system.
Uh,
good to know is also how you can see
later what you can see in all those
modules. So, let me just find any
which can be
let's say confirm management.
So, when you will go to the
GitHub and then you will open any of the
modules, first of all, you will see what
is the structure, you what is the
documentation, like what are the public
objects, like for example, confirm
management, and what are the function in
that. And also what are the examples,
like for example, here we can see and
parameters and so on. So, you will find
all of that here.
How is if we will go a little deeper, if
we will go to the source of the
of that, you will mostly see two
objects. One is
confirm management in this case, the
same as
name of the module. The second one is
confirm management implementation.
Very important is that we don't have
access to the implementation. So, we
only use as a developers, we use
something which is
uh, without the implementation. So, it's
like
a so-called facade.
facade uh,
pattern. So, you can see that here is
this function which was in the
documentation, get respond or default.
And is just returning the
value of the function from the
implementation
code unit.
As I said, you cannot go to the
implementation and use that. You see you
can see the code, but everything with
the implementation will be marked as uh,
access internal. So, we cannot use it.
Only Microsoft can
Okay, let's go back to my presentation.
So,
we will not only find, uh,
on the in this repository modules, we
also will find much more. I will not
focus on that today, but I would like
that you will also know it and you will
be able to find that code as well. For
example, you can see the source code or
of all standard APIs or Shopify
connector and you can also do the pull
request to fix something in uh,
SharePoint connector if there is
anything.
One, uh, another one which is, uh, nice
to know is also demo data for
manufacturing and for example test
libraries. So, where we can find all of
that? We just need to go a little higher
and as you can see, I'm just now in the
modules and in the dev tools and I can
find test framework for example or as
you've seen,
uh, on the screen, for example,
performance performance toolkit.
If we will go even more higher
and we will go to modules
and for example to
I didn't want to go to system, but I
wanted to go to apps
and for example to W1, you will find
APIs.
And if we will go to apps, you will see
also all the APIs, for example. All
right, so this is the place where you
also can contribute, but also you can
see that.
All right, but this session is in
example, so that's almost all my slides
which I have.
Uh, but, uh, we got a task. Normally, we
got in getting the development task. So,
what is our task? Uh,
the customer wants or the end user wants
to export all
customers in the XML file.
Easy?
Easy.
But they also would like to compress it
with zip.
And
they would like to send this file with
the Azure function.
Oh.
That is going going more.
But they would like to store the copy on
Azure blob storage or on SharePoint.
And they also would like to send email
confirmation that such such thing was
sent to the
to the Azure function.
And only from the production
environment, of course.
And every second
Monday of of the month.
So,
question to you,
how much time you think it could take
without code pilot to develop that?
Half an hour, someone said. Okay.
Do you agree?
I agree, but okay.
All right. And
I should be I should ask before the
session if there are any managers on the
uh
on our stage here or or in our room. Uh
because what you will see, you will see
that to be honest, I will be talking and
showing you
no more than 100 lines of code today.
Right? So, that's how easy it can be,
and I will show you much more examples.
I don't know even if you will go through
all examples, but
it doesn't take a lot thanks to the
system up.
So, let me uh dig into the
um
to Business Central.
I will just refresh this one.
All right.
And I would like to show you this
scenario, but as I said it's a building
block, so all of that will be like we
will just build the blocks.
We could do it at the end.
Before that, maybe some other things
also which can be useful from the system
up. Let's start with the photo, maybe.
Right? We like photos.
So,
let's go to the purchase order.
So, how Business Central can do the
photo
of both of us. And remember, it's maybe
much easier if we talk on tablet or
phone, but I hope you can see us.
You know, when I'm doing demo for our
system is
I have a lot of pictures like that.
Oh, and I have photo.
All right, so how we did that? Let me
just go to
our examples.
I will go to
camera.
And yes, I created an action, but I will
not talk about the action here. Let me
just take you see how I use the system
up just to take that
photo.
You can see that I'm using the code unit
which is called camera, and
I just need to check if it's available.
It is.
And I just need to use one function.
Right?
So, this is how easy it is, and then I'm
just saving the picture which is
in stream just to save the in stream
with the temp block.
Okay.
So, now I've got what, 95 lines of code
left for the remaining demos or what?
Yes.
Go for it. But okay, I I will take it
by myself.
But yeah, sometimes you just need to
flip the picture as well.
Oh, okay, I flipped it the
wrong way.
But you you get the point, right? You
can also flip the picture, you can get a
size, you can also shrink the picture
like for example, if you want to have a
thumbnail size and so on. So, again,
let's see how we did that. And this is
one more. I used the same module, so I
used camera, but I also needed to
transform the image. So, let's go to
this
to this function. As you can see, I have
only one code unit to do that.
It's called image. Right?
So, I want to flip it? Yes. Rotate,
flip, and I just need to say which which
direction I would like to flip, and I
also shrink it
right? So, with one function, crop, I
just crop it.
That was pretty much easy.
The other thing which I'm using also on
daily basis is that I need to know
geolocation of some of the records which
we have in the database. So, let's try
to find where we are.
Let's go to the fixed asset.
I could just tell you.
Yeah, I know sometimes it's easy just to
look on the phone.
Uh but
I can just get geolocation, and this is
a geolocation of this fixed asset.
This is also not very complicated to
get, so let's see uh how we did that.
And uh go here, and as you can see, this
is only two three lines of codes. Right?
So, I get the geolocation, and I just uh
put two decimal values here to get it.
Very easy, right?
I know, this is why I said it take a
half an hour.
Um
Okay. But one of the example which I'm
always showing, especially if you are
working with the cloud, and uh
there is a lot of apps on AppSource.
Sorry, guys, if you have them, which
allows you to print the barcodes.
Right? I'm not using any of the apps.
I'm just using what inside Business
Central is. So, can I use system up to
generate the barcodes? Of course, I can.
So, if I will go to the items
and
I think it's called barcode.
Uh
No, item barcode, yes. This report which
I would like to. And let us just choose
one and do the preview.
Oh, you can see that I really printed
the barcodes.
Oh, like this. And it's not only not
only one dimension, but also two
dimension barcodes.
And that's only the example. There is
much more
ones which I need to do. How I did it?
Let's go here and let's go to the
report. You can see that I have just a
columns which I could name exactly the
same as the
variables for the
for the barcodes.
But to generate the barcode, in fact, I
just use one function or with the animal
as well. So,
first I just do the implementation of
interface, and then I just get encode
function.
And I said what
enum I would like to have.
So this is how easy you can do the
barcode, but there is one more catch. We
just need to open the
Word document just to show you how it's
look when we are printing.
Not great, right? Because
if we will just click one, you can see
that this is the font which we are
using.
So maybe on the layout it doesn't look
nice, but when we print it, you seen
already barcodes. Right? So with two
lines of codes we can just get a print
print of the barcodes.
But of course you if you are using on
from I heard from one of the partner
that you need to have a license for
those
fonts. On cloud you don't need to
because Microsoft is paying for it.
Okay. So let me go to this example which
we were talking
a bit.
So
we were talking about that someone would
like to export a customers to the
XML. And yes, we could use
XML port for that.
I know, but there is also one another
another module which can help us with
this. So let's go to the customers.
And let's click export to Excel to XML,
sorry.
You can see that my XML has been
created. Sorry that I'm showing it here,
but let me just not switch switch now.
How we did how I did it? Little more
lines of code, but also something which
was very easy, especially using chat
copilot. So there is a XML writer which
just allow me to start the document,
start the element, and just write the
code
for each customer. And I'm just adding
the element, and if I would like, I can
also that add the attributes, but I also
can add the elements strings inside this
uh this attribute.
Right? At the end, I'm just saving it to
the big text. That's all what I needed
to do. Right? So, with the with the
module, I just was able to quickly
create an
XML. To be honest, I hate using XML
ports, but
that's everyone's opinion. But,
they also ask that we would like to
uh we would like to export it to zip
file.
So, let's see if we can do it again very
simply.
So, let's go to the zip file.
And as you can see, I have two files
with the customers.
Mhm.
How much I need work for that?
Let's go to our zip.
And you can see that again, I use one
function from the code you need, which
is called data compression. That's also
part of the system up, and I just create
a zip file here, and just put those two
to the data
at entries from the
from in stream. Right? Customers one and
customer two.
In this case, I just use the same.
But, if we will go to the data
compression, you can see that it's
little more than only that we have also
G zip compression, but we also can open
zip archive, we can remove the entry if
you would like, and we also would can
get entry list of all the files.
So, as you can see again,
we using just a few lines of code, and
and we didn't need to develop so much
just to do it.
All right, the next one will be a little
more tricky because we would like to do
it on Azure blob storage, right? We
would like to put it on Azure blob
storage.
I will not put it on Azure blob storage,
I will put it on SharePoint, but
also in system up you will find
something for Azure blob storage. So,
let's go to Azure blob storage.
And as you can see,
I just need the storage key and Azure
account name to connect to Azure blob
storage. So, that's not a lot.
If I will click list containers, it will
can it will get from the Azure storage
the whole list of all the container the
containers which I have.
So, if I will choose one, I also can
choose the files which are there. So,
let's go and
choose list of the files.
And you can see that I have three files
there, and I can even show you that that
this is exactly what I have, so let me
just switch
in Azure.
Go to the storage.
Which one I said it is?
BC Tech Days.
Okay, and let's go to my containers.
You can see that I have my container,
which is called BC TechDays.
And I also have exactly three files
here.
So, if I also will click that I would
like to get this file,
I get it also to to my uh
to my
computer.
So, how we did that?
Let's go to the Azure blob storage.
Here I needed to do a little more work,
unfortunately.
First of all, I needed to create some
pages. Yeah, the setup page, that's
something which you probably will also
need to do, and the table.
In this case, I have my Azure account
name and storage uh key
for that, and that's the minimum which
we need. And also the container name
would be helpful. Then we can need to
create a page which is for Azure
containers. It can
It is based on the system table, system
up table, which is ABS container.
There is no such page in the
system up uh because everyone can use
different different things. So, I have a
one field there, which is just a name.
And that was my preparation which I had.
Oh, sorry, maybe one more.
Again, the page for the
container content. This is the page
which you have seen, and this is again
based on the system table, which is
called ABS container content.
And I just put the fields from that
table. But, in general, the whole
configuration
in in
connection is very easy. If I would like
to list a containers, you can see that I
just get the
my table. I just make an authorization
to that. So, this is the interface with
the storage service authorization and I
I create a shared key and and put the
shared key here.
And I initialize the container client
with my account name and my
authorization and interface. And then I
just use the function to list the
containers.
There is also few more. You can create
containers, delete containers, and much
more. Right? So, all of those function,
you don't need to care about it. You
just need to run one function, for
example, to delete the whole containers.
And that's how it easy it is. I just run
my page later.
The same with the
download file. Story is the same. I get
the file I get the setup. I made an
authorization. I just lead list the
blobs. And
to my
table to to to system table, which is
container content.
That was quite easy
to send files or get files from the
Azure
storage and I don't need to store those
files in the
blob.
But I also can do connection with
SharePoint.
So, connection with SharePoint is a
little more tricky
only because we use in standard system
up authorization and you just
system to system authorization. AJ can
confirm that.
Uh So, you need to first register the
app on
on Azure to be able to
to connect to that. But, if I would like
to just list the folders of my
SharePoint, you can find that this is my
folders which I have there. And for
example, one of it I think is somewhere
is shared documents which I have one
document there.
But, I would like also So, let me just
show you. This is exactly this. I have
just one I have just one file.
But, let's
try to put some file to the to the
container to the SharePoint.
So,
Yeah, we will just take the same file
which we took from the Azure Azure
storage, and we will get an error.
That wasn't expected.
Demo gods, right? So, let me just check
another one. And if it will not work,
it's
Forbidden. Okay.
Ah, of course I know why. I
I delete the
Let me just
do this and
and take that one.
Okay.
Yeah, this is when you just
go to fast. So, as you can see, my file
has been just created. Uh
Again, how we do that? Um
So, let me just go to the SharePoint
connector.
Uh
The same story with Azure blob storage.
Uh Set up page. Yes, that's something
which I needed to do. And table, I
needed to do the page for the files. So,
I have it also on
My source table is SharePoint, uh,
SharePoint uh, SharePoint file, which is
an system up file, uh, system up table,
and I just put uh, two fields here.
Uh, the same with the uh, SharePoint
list. I also use the SharePoint list
folders, and I can just see all the
folders.
Uh, but how we upload the file, maybe
that can be um,
uh, nice for you. Uh, we get the uh, we
get the
uh, uh,
we get the setup, uh, we just use file
management to uh, get the blob, uh, but
later we initialize, uh, sorry, we get
the tenant ID, we initialize, and we
just use the function which is called
add file to folder.
And I think here I will just say a few
words because um,
uh, we cooperate, my company and one of
the developers, Conrad, uh, he uh, uh,
he made that uh, that uh, whole
uh, SharePoint module, and we just
uh, do the pull request uh, to uh,
Microsoft. Uh, the nice thing there was
that we also get a lot of that. It turns
out that there was some issue which was
fixed by someone else, and I know that
there were also a lot of questions and
why there is no one function or
something, and I think that a lot of
people already contribute to that. So,
you can see that you also can contribute
and make something uh, that everyone
will
be using.
Yeah, and we as Microsoft learned a lot
of from this as well. I mean, there so,
you know, every developer and every
company has a different coding style, so
having to go through the code that uh,
uh, KB's company delivered was quite
interesting and then very, you know,
giving for us, and then figuring out how
to get this into the stage was actually
a very cool process, so I I you to
do the same if you feel for it.
Yeah, uh the same is with the list
files. As you can see, I just need to
another function from SharePoint
SharePoint client code unit, and that's
get folder files by server relative URL.
But, if I will just
show you a little more, you can see that
there is much more like create folder,
create list, create list item,
attachment. I know that is also a
something which I hope will get soon to
the system that you will also be able to
do the metadata for the files.
Right? And that's all with the just one
function, which we just need to run uh
from the
system code unit.
Okay, our customer also wanted that we
will be able uh to push it with the
Azure function, right?
Uh
okay. So, how we can use Azure function
from Business Central and don't do a lot
of coding for that. If we will go to the
example of Azure function,
you can see that I have only URL for
Azure function. There is much much more
option, but I will just use the easiest
one here. So, only with the URL. If I
will run function, I hope I will get a
message
that uh
we run the Azure function here.
Yeah, welcome from the Azure function.
So, uh
let me also show you how we how we did
it.
Let's go to the Azure function.
And yeah, setup page is the same story.
So, we just I just added one field to
store someone the URL.
But, in fact, to run the Azure function,
that was quite easy. I just needed few
few functions.
First, I get the setup, then I made an
authorization again
authentication in this case
and I create code authentication where I
just put the URL. But of course, there
is little more options
here as I remember. For example, create
OAuth.
And
just to get the respond,
I just use the code you need Azure
functions and set and get respond.
And so, this is where I just send the
dictionary and I also send the
authentication.
But you can see that you have little
more. You have also send and you have
send get and respond. So, I always going
to the
to add the functions if I need and you
can get all the documentation in every
place like that. So, send request, send
post request, but you also see the send
and you have everything in the
documentation. And again,
you can see how much code Microsoft
needed to write in this case. I think it
was Kenny who was needed that function
and how much code in the background you
would need to
write if you will just not use this one
line of code. So, pretty much
more lines, 84, right?
We do some sometimes get the question
like where can we find user examples of
all of this what KB is showing right now
in the base app for instance?
And sometimes I have to answer, well,
there are not always usage examples
because not all of these things have
actually been uptaken by ourselves yet.
A lot of these modules were actually
contributed by a partner that needed
that for his, you know, ISV or his or
her ISV or PTE app.
So, actually we are still, you know,
working on uptaking some of these
ourselves.
So, I would encourage you if you want to
have usage examples, you know, either
rewatch the session on YouTube when it's
out
or going to the test code units and take
a look because very often the test code
units you will find usage examples. Um
In the meantime, I also can say that we
will publish this repository with the
examples. So,
you can also
take them if you want.
has something to go on.
Co-pilot it.
Feed it.
Okay. So, we have Azure function as
well.
Let's little switch to different
examples.
I have a question to you. How if you
have two values, integer values or
decimal values, how you will check or
choose the bigger one or yeah, the
bigger one?
Would you use if X bigger than Y than X
and if not than Y?
And I was surprised that
one code review which I was doing and
one of developers with whom I'm working,
he did a little different approach.
So, you already seen today
Vincent showing math. I think it was
Vincent, right?
Showing math module. But there is a lot
of other things as well or functions in
this. If I would like to have,
let's say,
here we have 10, here we have 32.
21 and if we will just get max, it will
show me the max
max value of that.
If I would like to get the minimum value
of those two, I will see the minimum
one.
Okay, let's just put here something
more.
If I would like to do the floor,
213.
Maybe I should do like
Yeah, and ceiling
214.
If I would like to truncate it, 213.
And if I would like to get reminder, I
have no idea what will happen here, but
let's just make
and
five.
I will get two.
So,
you can see that
yes, you can use the math also in
Business Central and there is not a lot
uh needs for that. In fact, I even
didn't create a code unit for here
because we just need one function. And
this is from code unit math. Not a lot
of us are
going there, but you can see that if I
would like to have a max, then I'm
getting a max. If I would like to have a
minimum, I will just get a minimum. So,
let me just only
That particular module is a good example
of a .NET wrapper. So, in reality, what
we have been doing in the module is
simply to take the .NET API and wrap it
and make it available. So, if you ever
have any API from the .NET framework
that you would like to use, obviously
you can't use it in PTEs and so on.
Make a pull request and we will happily
accept it if
Yeah, and as you can see
Yes. So, as you can see, I have quite a
lot of other functions as well. I never
use logarithm
logarithm in Business Central, but the
mix
min and max and mix
happened to me. If you would like to do
the
value of the P, you also don't need to
hard code it. of the P, you also don't
need to hard code it. It's already
there.
So, all of that things you would find
also in the
in the math
code unit.
Um
Let me also show you another thing which
I even after I did an example, I checked
how we did in
in one of the projects and I decided
yeah, we need to also
do the refactor of the code there
because we made something with more
lines of codes and a little more
complicated that it can be. So, let's go
to the customers again.
Oh, I was already on customers, but I
can just go to one of the customer. And
I added the field which is responsible
user. So, I would like to choose the
user or I would like to write and check
if such user exist. So, if I will just
put X X X X X
that username doesn't exist. Right?
Makes sense. Uh if I will just go here,
I can see the page with the user lookup.
Right? So, if I will just click admin
I will have my admin.
So, as I said, we could do the find set
of the users and
do the page with the users and so on.
However, there is a little easier way to
do it. As you can see I just need one
code unit again, which is called user
selection. And I if I would like to
validate username, I just use validate
username.
And if we will just go down, you can see
that they already handle all kind of
that stuff If username is empty,
if uh
generally is empty and and so on. If
doesn't exist, it's error.
Let me go back here. And the same is
with the lookup. So, for that I just
needed two fields, two two variables.
One is as user record and the second is
user selection. Why I needed the user
record? Because I can filter first uh
users and then I open uh that. So, in
this case, I just filter system users
and group users. All right? So, if you
will go here, you can see that they
already handle uh for me all the
external users, license type, uh AID
group, license type, Windows group. All
right? So, I'm covered. I don't need to
do it. And uh moreover, let me just
uh show you here. I have also uh
another one also to filter. I can also
hide uh users in this code unit and so
on. And
the thing, I even didn't need to create
a page. This page, in fact, exists. So,
I just open open the page and you can
see that there is a uh user lookup page.
What it gives me, if ever Microsoft will
change the page or whatever else they
will change in that code uh or fix, I
will also get.
And by Microsoft, maybe I'm a little
wrong here.
Anyone can can do that. But, let's not
go so far.
Um so, this is only that I just needed
two fields to uh
two uh two lines of code or three lines
of code to handle uh on validate and
lookup at the same time.
All right.
Let's go further. I remember there was a
requirement from from that from that
function that we wanted to check if it's
only for production, right?
So, let's go to the custom
to
company information.
And let's check information about this
environment.
So, what I can see, I can see this is
the
this is the sandbox. Good. This is the
production. No. It is
SAS or cloud. And there is an
environment name.
Yes, exactly. It's sandbox.
I also have some information about the
tenant ID because I'm just using here
that tenant ID without the display name.
So, how we get that? That should be also
pretty easy. So, let me just go to
user.
Not to user, to environment.
And I just made one function. And to be
honest, I just need for this one code
unit. And this code unit is called
information environment information. So,
what I have here, if
it's production, and then Microsoft is
handling if it's really production or
not. I don't need to do anything with
that.
I can get the production name. I can get
the sandbox. I also can do SAS.
SAS, you see that I also can check if
it's on prem. Financial
infrastructure, get family name, and so
on, so on. Version installed, blah,
blah, blah. Yeah, I can check also that.
So,
with just one functions again, we get we
getting much more information. And the
second code unit is called tenant
information. And if we will go to tenant
information, I have get tenant ID and I
I have also get display name. So, if I
will just go here, you can see that they
also handling that and I don't need to
to be honest do anything with this.
The one requirement as well if which I
had from our users, they wanted to
re-authenticate
themselves when they are using Business
Central.
Um we cannot force Business Central at
least for now to put another like
re-log them and put one more time the
password. Uh but there is a
functionality to set up the password.
So,
password.
So, what we what we did is that
I also can set up my personal uh
password and let's say
BC
tech days
BC
Oh, okay, it must have much more. BC
tech
days
21. I hope it BC tech
days
21 Oh.
Let me just Maybe I should have some
password which is
I
You're doing all the best practices here
showing the password, reading the
password loud.
I don't do it so you know, it's like but
okay, I will not go to that but you can
see that I can put the password and it's
even working better than I would call
code it. Uh and I just need to put the
password and confirm the password. I
also can change the password and match
the password. So,
again, how we did that? Let me just go
to our password
operations, and you can see that I have
one function, which is called from the
code unit, password dialog management.
And in that, I have open password
dialog. And here I have uh
some methods which I just that are all
only overloaded with some additional
parameters, like display disable
password validation, disable password
confirmation, uh and so on, so on. I
also have open
dialog password, which automatically
have some. I also have function to
change the password, so I can just put
old and and new one. And there is some
uh
which probably I hope I can put minimum
uh number of
records. But as you can see, I have just
password and then I get password to
check with my password, and I can show
the error if the password is correct, if
I would like to
type the password, and if I would like
to change the password,
uh I have the same open
change word
uh
password.
This is how easy it is. Give me just few
more minutes.
five more minutes for
even more examples, and then we switch
to something else.
Yeah, good. So,
that Another example which I would like
to show you is uh related to choosing
the object. And that's something which
from time to time we need to do, that
someone need to choose the
table, for example, and also field from
that. So, let's choose the object.
Choose.
Okay. So, let me just choose my table,
and let's uh choose uh not the first
one, maybe locations.
And then field name.
Okay, I just need to choose base uh unit
of measure.
As you can see, two fields, easy, just
name and field. Uh how many uh filters
and so on I needed to do. Let's go and
check.
So,
uh choosing the object.
And I just put two uh uh uh
put one and you can see that again I
have just one
Let's say go here, code unit, which I
just filtered all objects. And uh from
the page objects, I just set the record.
I don't need to create my own uh pages
for that.
Uh the same is with the filter uh
fields. I just use the selected fields.
Oh, that's was
uh table 27. I hardcoded it.
Uh
and so I have a for that.
And I just use uh one uh code unit,
which is uh field uh selection, and I
just uh use uh only one uh function,
which is the open. Right? And this is
how much I needed. But again, I just
would like to show you that
this is not what is only happening. It's
something which is in the background, so
we don't need to
code all of this which you can see here.
This is already coded for us.
Um
I hope you know functionality which is
called retention policy.
So, a retention policy
uh retention policies
uh is the functionality which allows you
to
delete the data from the log tables to
don't uh
have everything in the the
Uh all the records which are very old,
like change log, like uh retention
policy log, and so on.
And in general, you have I this
requirement I've heard from time to time
from the customers. Oh, can we just
delete this
uh uh all data? We will not need it. And
yes, we could create a job queue and try
delete that data delete that data and so
on. But Microsoft at some moment
uh at some moment also, let me just only
create a new one.
Uh at some moment also introduced such
functionality, and this
uh will just go automatically. So, why
we should bother with all the job queues
and all kind of that stuff if we can
really use this functionality.
Uh
the only one catch is that they didn't
add all the tables there, and that's
make sense because we should control
which tables users can use can uh set up
there.
So, uh that makes sense too. When I will
open a table ID, I will not see all the
tables, but only those which are really
should be deleted. And as you can see,
there are few standard.
Uh but you cannot add anything to this
table without small code. So, I added my
table which I called my log table, and
you can see this is my table which is
there. So, how you can do it?
Uh if we will go to the retention policy
install
again, very simple. Uh
I'm even embarrassed to showing this
that I'm just showing you one line of
code. It looks like I'm not prepared. Uh
in uh we just create a code unit which
is called uh which is called um
uh sys uh
uh sub type install, and per company, we
just adding our own table.
And now customer can use this
functionality with our uh logs which we
also have, right? So,
just easy. Don't don't over
do any additional things.
Okay.
I need to speed up, I see.
So,
maybe from our from our solution, as you
can see, I will not get to all of that,
but we said that customer also should
get an email. So, how easy it is to send
an email with Business Central. Let's go
to this customer which is not paying his
invoices in my in my case.
And I hope this is one which I choose my
email. And let's just
edit. And first, I will just see what I
will send. So, you see that I added
please pay.
And also to whom I should pay and why
to whom I should send. And I put also
some message here.
And I have
work.
Yeah, that should work. And I also have
very nice very nice
rich text editor, right Jesper?
Yeah.
Okay, good.
I can keep a draft. I can discard the
email, but in fact, what I did in my
scenario is only just I choose the
code unit. Maybe before I created a
scenario because you know that you can
send
different scenarios from the different
email accounts. This is exactly what I
did. So, I create my own email scenario
for that.
And then I
I just created an email and open it
in editor. That was so easy. And the
same if I would like to send it, I again
need to create it, but instead of email
open in editor, I just send it. So,
that's
how we have and but you can see also how
many we have function that for example
and queue the email so it will be sent
will will be sent.
All right, I think you've spent your 100
lines of code by now. Give or take a few
hundred more.
So I cannot use more but nevertheless in
the repository you will find some more
maybe I should also only mention it like
for example encoding to base 64 right so
like if I would like to
from base 64 and to base 64.
Sorry.
And also right
They can stay they don't like beer. So
checklist and telemetry all kind of
stuff yes and then I will stop.
That's a lot of good stuff in the
system.
Yes as you can see if you want to show
everything that's not enough 90 minutes.
Nevertheless I also would like to show
my last slide here
and also ask you a question. How many
times you were waiting for Microsoft
that to to fix something?
Anyone?
See that rarely ever happens.
Yeah that's not
Seriously almost no one.
No no.
And we don't record them right so it it
will be on the recording but also who of
you fixed by yourself not waiting for
the Microsoft?
Okay and those who raise the hands keep
it and who of you fixed it in the
Microsoft repository?
There you go. You should almost have a
t-shirt.
Yeah you you would get a t-shirt t-shirt
but we don't have it. So
We ran out of t-shirts. I don't know
it's like
Sorry that you are
in the section please stay in this
place.
What I wanted to say that our world
really changed. I remember when I was
starting in 2010 and there was a one guy
in the company who was doing
only talking with Microsoft.
And
13 years later,
we first of all, you see Microsoft on
all the conferences. The second, you can
ask questions on Twitter and they will
really reply on it, not only on Yammer
or anywhere else.
Chat GPT is also
Chat GPT, yeah. Okay, so now I know how
you're replying. And
but also, the most important part is
that we also can contribute to that. A
lot of things which I was showing you
today,
it wasn't wrote by Microsoft. For sure
not Azure blob storage, for sure not
barcodes, for sure not SharePoint
connector. Probably some of them also,
sorry, I don't know, but some of them
which I also showed, they are not done
by Microsoft. They are done by partners
as you are. And to be honest, that's
also our message here. It's like you
also can contribute and you also can do
something that we will all
be able to code faster.
You can see five lines of code to
connect to SharePoint. This is because
Conrad did that and just put it. If you
see in Azure blob storage,
five lines of code and you were already
be able to connect that. And now I will
just
my cue. So
And we're actually going to speed things
up a little. Um
so some of the videos that I'm showing
are the demos that I wanted to show, I
actually take a long time. Like one of
them is 1 hour long, so I had to
condense it to 5 minutes.
Uh so I can't do it live. Uh so these
are recorded. I hope that you can see.
Uh try to find the right screen
resolution and so on.
If not, feel free to come closer.
So very quick agenda for my end. Um
I quickly want to talk about why having
an open development model. Um I think we
probably covered that already.
And then I want to show you how easy it
is actually to contribute. So, how do
you get your contribution suggestion
approved?
How do you set up your development
environment on your machine to actually
make a contribution? And then how do you
get that contribution across the finish
line?
And I hope to be able to take you like
really from one end to another uh
within these 30 minutes.
And then I'm going to take a little look
into the crystal ball of what's next,
what's more to come. Um we'll talk about
how we are going full open source on the
system application. We are currently
only halfway there.
And then I will be introducing the new
layer, the business foundation.
So, very quickly, why should we have an
open source development model?
Um
Well, I guess it's it's no secret that
everybody by now knows that I do love
GitHub and open source. I think it's a
brilliant way to collaborate.
Um and as turns out, there are more and
more fans of it. Um and I do believe
that there's a really good reason for
that. And that is because when we work
together like this, we become more than
the sum of our parts.
Um we actually are able to achieve much
more by collaborating this closely
together. And this is why my tagline is
together we win. I keep saying that. I
keep tagging that in my tweets. Um and I
really do believe that message is true.
Very quickly, a recap of some of my
previous sessions why I do believe this
is a good thing.
Um well, it will accelerate product
growth. Instead of competing against
ourselves in like the lower level
modules, if we collaborate on this, we
can actually, you know,
develop what is important and not
reinvent the wheel over and over again.
And also, I do believe that the quality
and auditability of um the product that
we're doing is getting better. I mean,
the the source is open. It's there for
everyone to see. Um so,
you know, bugs just shine more than they
do if if you develop in private.
And then also, if everyone can see what
you're developing and they maybe have,
you know,
other ideas how to how what to use that
module for, uh then there will be nice
discussions about how to extend it, how
to customize it, how to make it
compatible to other solutions. You will
simply end up with a better API than if
it was only tailored to your specific
one scenario.
And then the last two, um
we've talked about that plenty. I think
it really fosters collaboration and it
develops the community even further than
where we already are.
And all of that allows you to build tall
verticals on a strong foundation that we
built together and it allows you to
focus on the last mile, which is really
where innovation happens. It doesn't
happen in the blob storage module. It
happens, you know,
when you go beyond that.
So, how do you get your idea approved
for contribution? Let's say you have,
like, a a module that you need to
develop
and you want to have it in this
application.
So, first of all, I want to talk about,
like, how do we work internally in
Microsoft? Because on GitHub, you know,
we've got issues. So, how does that map
to our internal processes? Because
that's currently a little bit of a
challenge.
At Microsoft, we've got bugs and slices.
Those are the two things that we work
with.
And if we take a look at what the
difference is between these two,
then we see that
a bug can either be, that's the most
important, the most critical thing, the
one that we always prioritize highest is
if it's a customer reported product
defect. It can come through a support
case, hotfix request, you name it,
everything. I guess most of you have
tried to lock one of these.
These can be procedural issues, like
some process isn't working, which is
blocking um business processes,
or it can be data issues where data is
being corrupted, deleted, wrongly
stored, and so on.
Those are, as I said, the most important
for us.
And then there's another category, which
is partner reported product defects.
Those are the things that you usually
probably fixed yourself when you got our
code base and you had the code
customization model.
So, it's all these paper cuts or like
small missing functionalities where
things aren't aligned, like this list
works like that and the other list
doesn't. Um
it can be collaboration requests where
you're asking like, "Hey, can we work on
this together to make our stuff work?"
Um and also can be extensibility
requests where you want to build upon
something, but it's not quite
extensible.
And then there internal reported product
defects which come in all shapes and
sizes.
So, that's the bug category.
The other category is slices, and those
are usually um part of larger stories.
We call refer to these as epics. It's
like the investment areas that we're
doing for a given release.
Could be fundamentals, could be
onboarding, could be manufacturing.
The important part here is that these
are much more complex. Um and that is
where our product managers come in. So,
we can't do everything at once. So, we
pick our battles for every release.
Uh and that comes into play in a minute.
I'm going to explain. And then there are
of course all the partner reported ideas
that you know so well. They come from
AKA BC Ideas. And if for instance, let's
say we have opened the manufacturing
box, then we look into BC Ideas how many
ideas are there that would flow into or
fit into this epic, and we'll try to
address them.
And important is these slices have exit
criteria. They need to be documented. Um
they need to maybe have security
reviews, release notes,
maybe there are some deprecation that
needs to happen. So, there are all these
things that need to fit together. So,
there's a lot more planning involved in
these slices than on the on the issues.
So, what of this then
is a good contribution candidate? Well,
customer reported product defects aren't
because there's a customer out there
hurting. They're losing money by the
hour. Um and open source sometime takes
a little while, right? Um it might have
to go through some code review processes
and stuff.
So, those are not good. Do use our
support channels for that, and let's
make sure that these are ironed out as
quickly as we possibly can.
My favorite actually are these partner
reported product defects. These are
perfect examples of what we should
collaborate on because there is no like
competitive advantage in having like
fixing
one of these little paper cuts in a PTE.
So, we really shouldn't do that. We
should work together on getting these
out of the product.
And when it comes to the bigger work, um
yeah, right. Uh so so the top category
is is what I would consider a GitHub
issue. So, it's very very easy to like
explain what the product how the product
is misbehaving, and you can log it as a
GitHub issue. The bottom part, um I
still believe we should start with as a
BC idea.
So, do bring your idea for a feature
out. Let's see how many agree that this
is a great idea. Uh and then we can
approve that idea for a contribution uh
candidate, and then you can start
working on GitHub on that idea.
But again,
like it depends a little bit. So, I've
tried to put that in writing.
Um
we will always approve paper cuts
most of the time unless they're too big
and complicated, the horizontal building
blocks such as the SharePoint was and so
on.
Uh bug fixes without production impact.
The sometimes
uh boxes like uh if our product managers
decide that yes, we have already opened
the the box. Let's say we are looking
into manufacturing,
uh and they have a complete idea about,
you know, how would things fit together,
then we're very inclined to also accept
pull requests in that area.
If you all of a sudden come with a
complete restructuring of item tracking
while we're not looking into item
tracking,
then that probably, you know,
becomes a capacity issue on our end
because things do still need to fit
together, right?
Um so, this is on a
per discussion basis.
What we currently will never ever accept
are product defects with customer
impact. Also localizations, we cannot uh
because we only have W1 in our um
uh GitHub repositories.
And currently also actually event
requests because we have a dedicated
team trying to make this as quickly as
possible um and we don't want to have
competing ways uh of
of doing these things and it just gets
confusing.
So that's kind of what you can
submit.
All right. Um
let's get ready for implementation.
So let's see uh let's say you know you
are in Business Central and you go to
the demand forecast feature.
Um and then you hover over, you know,
the the headers here
and you see nice tooltips everywhere and
then uh what is source type? And there
is no tooltip.
Now this is obviously too small a case
to log for a support case for, right? I
mean that that makes no sense.
But let's just use that as an example
for something that we want to fix. Um
now in this case it's not the system
application but it's the base app but
the entire process is is the same or
will be aligned.
So we can go into
um now I'm logged in as a developer.
So I will actually now go in first and I
will try to search.
Um
and I will find nothing. Search first
because others might have already logged
it or are working on it so it's always a
good idea to search.
Then we can say, "Hey, let's make a
feature request." Um but then there's a
little disclaimer saying, "This is not
the way. You should use BC Ideas for
feature requests."
But you can create an issue. Um and
again there's a little disclaimer here
saying like if it's a customer defect,
please do not use GitHub. Um
but other than that we've got these
sections where, you know, you need to
um
uh describe the repro steps so that
everyone can reproduce it, provide a
saying title, um and you know, provide
all the information
uh that might be needed here for others
to understand the issue that you're
logging and also for obviously Microsoft
to understand what it is you're
attempting to do.
So, for instance, you know, go to the
demand overview
and hover over the field source type
and now I would expect that I see a
tooltip, but I don't. So, that's the
issue.
And there you have it. That is actually
enough sufficient for a little issue.
Going to tag this as sample
and we can submit it.
So, now if in the Microsoft office, I'll
be sitting at my desk and I'll see,
"Ooh, there's a new issue. Nice, let me
take a look."
Uh so, I open that one and now I'm
exaggerating a little bit here. So, I'm
So, the idea here is that we will
discuss until both parties or everyone
understands what really is to be
implemented here.
So, I could for instance say, "I would
agree that the tooltip is missing, but
before we go ahead and implement let me
know which tooltip you would like to
add." So,
you know, just to
showcase that can be clarifying
questions.
And you see by now that it has the
approved label, meaning we agree this is
an issue, but it doesn't have the ready
for implementation tag, which allows you
to start creating a pull request.
So,
um
the developer says, "Well, sounds good
that you agree with my findings and I
would add something along the lines of
specify the source type
of the availability
calculation."
Comment.
And now I get an email and I'm super
excited to see what has come out of here
and and I'm going to say, "Yep, that
sounds about right. Let's do this." And
then we're going to add the ready for
implementation tag,
which means now anyone who wants to work
on this
can go ahead and work on that.
So, this is actually all you need to do.
Again, if if there is a larger feature
that you'd like to contribute, start
with a BC idea and maybe in the comments
right you would like to contribute this.
Then we're going to tag the BC idea and
it's going to show up in here as an
issue.
That is already approved. But the rest
of the process is the same.
So how do you then get your development
environment set up? And now it's good
that this is recorded on YouTube because
this is going to go seriously fast. I'm
going to go in a minute from a
completely new Windows 11 machine that
has just booted
to you being able to compile in this
case the base application.
So let's see. Once you know how to it's
actually rather easy, but it is one of
the biggest hurdles that we've been
facing. So let me show you how this how
to do this
in a 10-minute walk through.
Um
So first of all, of course, you need a
PC.
Um does a small laptop suffice? Well, it
depends on what you what you want to
develop. Like if it's a if it's
a first-party app or something, it's
fine. If you want to play with the base
app,
uh it's more like this thing that you
need.
32 GB minimum I would recommend 64. The
more cores the better, the more fun
you'll have developing.
You just go for a longer coffee when you
have 4 GB
Yeah, but you'll drink a lot of coffee
then. It's not healthy for you that
these amounts that you'll drink. So a
little bit of a bigger machine is good.
Then you need a in this case a Windows
machine. I'm sure someone has played
with Linux and so on and can make it
work. I can't. So Windows, you need a
GitHub account
and a very basic understanding of what
Git is. You know, just take a Git 101 if
you haven't. It's you know, that's
really all you need. And then there are
some tools like Visual Studio Code,
the AL language extensions, Docker, etc.
So let's roll the demo and see how we
get all of that.
So you can Again, you can slow it down
on YouTube later on. You can follow the
steps.
Let's see how this is done. So this is a
Windows 11 machine.
There's nothing installed at all. It's
completely new.
Just to prove it.
And off we go. So, the first thing that
we need is obviously
and this is where it gets fast. Visual
Studio Code.
Off we go. Uh we take the Windows
version, we download it, we install it.
You can just use all the default
settings unless I say anything else. Um
so, Visual Studio is installed. Yum,
that was fast, right?
Now you go in and you get the AL
language extension.
AL and you install it and whoops, done.
Now you get Git, Git for Windows.
Yep, install, default settings. You can
change them, you don't have to. Install
Git, it's all good.
Done. Done. Well, that was a little bit
longer.
Three so far.
Now you can take Git CLI. It's a cool
tool, we won't get into it in this demo,
but it really really helps you work with
Git if you aren't familiar so much with
these complicated things.
PowerShell, PowerShell 7. You can also
use the old PowerShell, but PowerShell 7
is just so much cooler. I encourage you
install PowerShell 7.
It's again much easier to work with.
Done. Done.
Uh oh yes, Hyper-V. Now we need to
install Hyper-V on Windows 11 because
else you cannot run Docker. So, install,
restart. Now we've got Hyper-V on our
machine. Woohoo.
So, now we're ready to install Docker.
Let's go.
Docker is actually one of the few apps
where we need to change the settings.
So, I'm going to slow down for a second
here. In in this case, we install Docker
for Windows.
Um and that actually takes a while. But
here's a very important setting, it says
use WSL 2 instead of Hyper-V. And if you
do that, nothing works. So,
uncheck that one.
And install Docker. That takes actually
quite a while.
Um not here though. We've fast-forwarded
through this.
So, now we've got Docker, we need to
restart, we are back in the game, and
now I actually have everything installed
that we need. The next thing that we
need to do is for Docker is to currently
still run on Windows containers. Very
soon you won't have to, but for now you
still have to.
Um
at least last time I checked.
So, you click down there in the bottom
and you say switch to Windows container.
And now Docker runs in Windows container
mode and we are ready for some Freddy
magic with his
container helper scripts. So, how do we
get those into our machine?
We open
PowerShell 7
in this case.
And all we need to do here is that we
need to say import or install module uh
and then the BC container helper. And we
force the installation. So, now we get
all this magic that Freddy is developing
for us um which just makes it so much
easier to work with Docker containers
and Business Central.
Now there are two minor settings we need
to do. I don't know exactly why uh but I
just always run into this. We need to
set the Git username and the Git
password. So, don't ask me why, just do
it because else the system is not going
to work.
Um
so
just setting these two.
There we go.
And that was it.
Now our system is actually set up.
So, the next thing that we then need
obviously is the code.
So, we will go to
uh
GitHub.
And we will start with AL app extensions
just like we used uh the rest of this
presentation for.
And
you will find
the repository.
And now, well, let's sign in. That's
always a good thing.
And now what you can do here is that you
can go to code and you can say
you want to copy uh this and you can
clone the repository. A clone is a
one-to-one copy of whatever is on the
GitHub repository, a one-to-one copy on
your local machine.
You cannot use clones for development.
Um going to talk about that in a second,
but you can use this if you just want to
see what's in the system application.
You want to have a local copy of it.
Then you simply go and create a folder
like repos and you write git clone and
you paste in the URL that you just got
from the web page and next thing you
know
you have the entire code of the system
application and first party apps on your
local box.
If you would like to develop,
you need to actually use a fork. So,
let's go to the Business Central apps
repository here.
Here we create a fork.
You can read more about forks, but it's
like where you create a copy out of the
of the repository. But the rest is the
same. You can now
from your local fork, you can again
clone to your local machine and this you
can use to develop on.
So, now we have actually the base app
code on our machine as well. System app
and base application code.
This took a little bit longer.
So, now we need to compile this, right?
We need to start developing.
So, how do we get there?
We go into our repository. In this case,
it's the Business Central apps
repository for the base app.
And we go into AL Go and we write local
dev env.
And the only thing we need to do here is
to specify a password.
And
that's about it.
And wait. And it used to take like I
think when I did this recording, it took
an hour and a half or something, but
Freddy has in the meantime brought it
down to half an hour. The more power you
have, the faster this will go and we are
hoping actually to make this even
faster. For the system application, it's
a matter of a few minutes.
So, what's
going on here is like it's
setting up the containers. It's
compiling all the apps. It's creating
the demo data you need. It's doing
everything you need to have a running
instance of
Business Central
that you can develop in.
So, after a while
even though I speed it up like a 100
times, it still takes forever. Uh, after
a while you will
more or less be ready to go. So, here we
go.
It said 5,263
seconds. So,
that's how long it took.
But now if you go into Docker
you will see the BC server
um, and it's running.
So, that means we now have a running
instance of uh, Business Central on our
machine.
And we can now actually open the code.
So, if we go again to our repos app
layers W1 base up in this case.
Um, now we need to take two small
settings. We need to create a settings
file here.
We hope to be able to automate this, but
right now you need to point to where the
.NET assemblies are. And the .NET
assemblies, they are stored in the
folder that you maybe cannot cannot see
it. Maybe a little bit too small. But
it's somewhere in the BC container
helper. Uh, there's a .NET packages
folder. That one you need to reference.
And the last thing that I also hope that
we will get rid of real soon is that we
need to specify the runtime that we want
to use this in.
That's it.
F5
and
depending on what machine you have like
you now can drink a cup of coffee
normally or not depending on the
machine. Uh, it will actually compile
and run the uh,
the code.
Woo!
15 minutes to beer. I think we really
need that now, right? So, now you can
actually you can log in
um, and you will have Business Central
running. You can debug. You can do all
the things that you would like.
And contribute. Now you're ready, right?
Because now you've got the the code that
we have on GitHub on your machine
running. So, you can now start the
contribution.
Woo! All right. Need to breathe.
Um what other things settings should you
do? One thing that I would advise you to
do is enable rapid application
development, especially when working
with the base application. It just makes
it so much more enjoyable when you
recompile and republish. Much faster.
So far, so good. So, the last thing that
we need to do here, um we need to create
our pull request.
Um in interest of time, I'm going to
make this really, really short and not
actually go through all the the steps of
writing tests and so on. So, you find
your issue, right? That we've created
and that is now approved and ready for
implementation.
Um and you say, "Well, I'm going to do
this one." So, you assign yourself. In
this case, it's my MSDYN365BC dev
account.
Um
and now we actually need to develop
against the fork, as I mentioned.
So, this is the the clone uh of of the
fork that we're seeing here and I
already opened the file and the only
thing that we need to do is here in the
source type text, we need to add our
tooltip that was missing, right? So,
let's just put that in. Now, normally
you would obviously compile, run it,
test it, and all these things.
All that we skip here in interest of
time. You can now see that this is the
change that we're trying to make. We're
just adding a tooltip. That is great. Um
I now usually take the ID of my of my
issue to identify the branch. We can't
work on the main branch, so we create a
feature branch.
Um with the ID some name. This is really
up to you what you want to add here.
Um
and now we've got this branch
in a second.
There we go.
So, now we can uh write a commit
message.
Update the tooltip.
And we can commit the change that we
made in our local code repository. We
can commit that
to our
uh branch here.
And once we have committed it, we can
hit the publish branch. And now what's
happening is that the code that we've
changed is being pushed up into into
GitHub.
And if we go over here, you'll see the
had to recent pushes that less than a
minute ago.
You can create the pull request. Again,
the better title and the better
description you leave here, the better
off everyone else is going to be when
they're reviewing your code or trying to
contribute maybe even to your PR.
You can see the changes.
Um
So, yeah, add a little commit message
here.
And
when we have written that one, in this
case it's add a missing tool tip to the
source type field,
we can create click create pull request.
Now, what happens is that
our CI CD pipeline kicks in. It starts
compiling. It's It will soon start
running the tests and run all the other
gates like performance regression tests,
code cop, all these things that that you
might that we will need in a CI
pipeline.
Um and then at some point it's going to
tell you if your code passed or not. If
it failed, you need to get back and try
to repair it. If you succeeded,
then the next thing you need to do is to
get some reviewers.
So, you can go into Oh, oh, first of
all, we need to This is our pull request
now, right? We need to link that to our
issue so that we know this issue that we
created and that was approved
corresponds to this PR.
Um so, now these two are linked.
And we can go back and forth between the
discussion that we had in the issue and
the code that we develop in the pull
request.
Um and now we can add
a little tag which is called
uh needs
community review.
And this is where then I hope that
because it it can't be a one-way street,
right? Where where
the entire partner channel makes pull
requests and Microsoft gets the role of
reviewing. It simply will not scale.
Um so,
just as important as coding or making
pull requests as reviewing other
people's pull requests. There's also a
whole lot of value in these reviews. You
will learn a ton of good stuff.
So, I highly encourage you to take go in
and maybe for starters just to pull
just to code reviews rather than trying
to create PRs.
It's fun to do the pull to do code
reviews.
It absolutely can be.
Um
So, this is it actually.
Um now the things are going to take a
turn at some point Microsoft is going to
say yes, this looks great into the
product it goes.
So, I know that was very very quick, but
you can watch it in slow motion and then
you can try to follow along. It is
actually I promise you it's not that
difficult. And if you get stuck, do
reach out to me. I'm always happy to
help. So, what's next here?
First news is the system application is
moving.
It's like, what? Um
AL app extensions uh is well like we
will be moving away from that. And why
is that? Well, that is because AL app
extensions
uh is polluted. Let me just put it that
way. We've got a lot of issues which are
not related to the code that is in
there, right? All your event requests
and so on and so forth. They are in AL
app extensions together with the code.
Um there has never really been any
process around AL app extensions. Um
the stuff that you just saw actually
doesn't really work like that on AL app
extensions.
So, this was just kind of heads through
wall, let's do open source. So, we need
a fresh start.
Um why do we need a fresh start? Well,
it's because the
Business Central application team also
will start developing on GitHub.
We will have a common backlog that is
open for everyone to see.
Wait, wait. Can I will I be able to do
the pull
code review on your code?
Absolutely.
Okay.
So, and and we're going to switch from
being on the release branch to being on
the main branch. So, you're going to see
what's coming in the next major release.
Um
so, this is quite the change.
I also need to convince our developers
that this is a good thing because we
also aren't, you know, always perfect
and write some really weird code and
then it's really embarrassing. Now the
world gets to see it, but um
I think it's a good thing.
Um and, you know, why do I think this is
a good thing? It's because only then
will we really have the full benefit of
open development. Um you know, this give
and take is is really the what makes
this a win-win. The one-way street, not
so much.
So, where we will be moving? Uh we will
be moving to
github.com/microsoft/bc-apps.
Yeah, that's nice and short. Um
you can't go there yet. It's still
private because we're trying to set up
all the CICD pipeline that we need. Uh
we are establishing the process to make
it bulletproof.
Um and you know, this has been ongoing
for quite a while, but now we're really
getting there. Um so, I do hope that
when we are done and we have wrapped up
2023 wave two,
that this will be a good time to say,
"Now we're internally shutting down the
repository for the system application
and we will be opening on GitHub for
everyone." It will probably be from one
day to another.
Going to make a quick tweet and a Yammer
announcement about it and off we go.
Uh of course, the AL app extensions
repository's going to be made read-only
then for the system application or we're
going to remove it altogether.
So, that's happening.
Is that it, you ask? Nope.
We've got more. The system application
will be getting a new upstairs neighbor
as we introduced in the
keynote.
Um and why are we doing that? It is
because we actually want to continue our
efforts to componentize the business
application platform. I really do
believe that the the the design and the
structure of the system application is
so much better than what we have in the
base application. So, we do want to push
this forward.
Um and the system application was
actually only ever meant for non-ERP
specific platform-like capabilities such
as blob storage and the likes of it.
Um and now we actually want to continue
to start taking the things that um
have a business purpose, that have more
of an ERP flavor.
Um
So, we will be establishing the business
foundation. We will be developing it
fully in the open. Um, soon we will be
making the first pull request where next
to the systems folder, there will be a
probably foundation folder. And then
we're going to push it out there, and
you can see what's going on, and you can
start contributing,
commenting on it, adding event requests,
whatever it is that you would like on
that module.
Not even Yeah, even request maybe
because now it's we're redesigning it
from scratch.
Um, so how are we going to do this?
Well, you all know that this is the
structure right now, system application
base application application under the
application umbrella.
So, we're just going to squeeze in a
little layer here, um, our business
foundation.
Um
The functionality in there is what is
used by all or none of the application
domains.
So, for instance, an application domain
is finance. So, if there is something
that is used in, you know, finance and
order processing, and so on, you know,
if it's a common thing, then it will be
moved into the business foundation, or
if it's not used by any of the of the
specific domains.
Um, it will be completely implemented
after the same principles as the system
application. We will have the better
cleaner APIs. We'll have them well
documented. They will be fully
extensible. They will have improved
capabilities, and there won't be any
localizations whatsoever in those
modules.
Um, it will appear non-breaking to all
the apps above, um, because you're still
under the application umbrella. So, if
you're referencing application, um, you
won't break. We will probably have to do
some lightweight deprecation,
um, here and there. Exchange some
things. Time will tell. Um, again, we
will be developing this in the open. You
get to see what we do.
Uh and we will be starting out slowly.
For 2023 wave two, our only goal is to
get number series out. Sounds easy, it
isn't.
Um especially thanks to Italy who has
like some really funky number series
stuff that
now
we somehow need to figure out what to do
with.
Um
but then given time
other things will come to the uh to the
business foundation. Dimensions,
currency, location, company info, you
name it. Um we also still have stuff in
the base application that needs to go to
the system application. So, we're going
to keep pushing or pulling things out of
the base application, making it even
slimmer, and start establishing these
two
or
establishing this layer and enriching
the system application even further.
Woohoo!
That was it.
I don't have any thank you slide because
I wanted to go back to your deck, but I
Then I will go to my deck, yes.
We actually only have 3 minutes for Q&A.
Um I will be at the Ask the Experts
booth. Uh so, if you have any questions,
um you know
do come visit me. I'm happy to talk
about this all night long.
And me, too.
Um
But maybe you have any questions.
We also have no t-shirts. So, what's the
point of a Q&A if we don't have any
t-shirts?
They still can.
Yeah, do you have a question?
Oh, there is a question.
Can I have a beer now? Is that the
question?
Thank you.
Hello. Hello.
Um
just
for me again to understand.
I am
I need unpopular model.
Louder.
Um it is it should I go with ideas
because potentially there will be not
much people who support my
um model.
It's really hard to hear. Maybe we can
just take this offline. Like it's like
this.
I don't know what's wrong with these
microphones today, but it's all
I can just speak.
No, it's can't can't barely hear you.
We'll take that. All right. Thank you,
everybody. Beer time.
Thank you.
Well done, guys.
