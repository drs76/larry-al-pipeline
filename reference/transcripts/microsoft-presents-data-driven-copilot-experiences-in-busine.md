# Microsoft Presents: Data-Driven Copilot Experiences in Business Central: Summarize and Autofill

- **Source:** https://www.youtube.com/watch?v=m5xsLNhJ5_0
- **Video ID:** m5xsLNhJ5_0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 38m02s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Welcome ladies and gentlemen. For the
following 90 minutes, we will have two
sessions with multiple speakers. For our
second session of today, we'll have uh
what's new in Microsoft Copilot Studio
and how you can leverage this with
Business Central. But right now uh let's
get our hands together for data data
drive and co-pilot experiences in
business central summarize and autofill
please.
Everybody
call me
welcome everyone. Hello. My name is
Monica Alja. I'm a senior software
engineer in Microsoft's Business Central
team in Denmark and I'm here with Vasil.
Hi, I'm Vasil. I'm a senior software
engineer for Business Central clients
team in Denmark. and together we are
really excited to talk about datadriven
co-pilot experiences in business central
summarize and autofill. In this session
you'll not only see very detailed demos
of these uh experiences but you'll also
get to know how we actually built it. So
you'll get little bit under the hood uh
experience. Uh but the most important
thing you'll learn how you can integrate
your custom extensions to be ready for
these co-pilot experiences. So let's get
this started.
It was almost two years ago that we
introduced co-pilot, your AI assistant
for work in Business Central. And since
then we have built a diverse set of
features um in Business Central for for
your productive experience.
Uh and we have been learning we've been
learning learning learning a lot of
things. We have been learning how to
build and manage uh these AI generative
AI experiences at scale. We have been
learning um how to make sure that they
are safe and secure. And more
importantly, we have been learning how
users are interacting to these co-pilot
experiences.
And one thing we have learned is that
even though AI uh is definitely more
approachable in ERP experiences, our
users are not prompt engineers. So we
went ahead and challenged ourselves to
come up with more ways for users to be
productive where they don't have to
think what should I type? Is this the
right way I'm typing? Will the machine
understand these words? And they in fact
just get out of the box experiences
without having to think of these. And
that's why we are going to talk about
autofill and summarize.
Why these? As I also already mentioned
that these experiences are have low
learning curve for users. They can just
get started with these experiences. But
these are also broadly applicable
concepts right in every software. These
concepts can apply across every
industry.
But not only that, these experiences
have been longstanding challenges,
right? We know that data typing is
tedious, repetitive typing is tedious.
We also know it's very hard to get a 360
view of your ent and of your entity
because there's so much data in business
central and then even more richer data
with your custom extensions. So these
are the copilot experiences that will
help user be more productive because
they can now get autofill suggestions
and they can get summarized record with
insightful
uh data then that they can know what is
important and urgent for them.
Uh and not only that there are also
significant opportunity for you and for
us to grow business central.
So Ail, let's get started with autofill.
Thanks Monica. So let's talk about
autofill. As we mentioned, repetitive
typing is tedious. And we all have our
smartphones. We have a keyboard, smart
keyboards. We type and then we get on
the top bar predictive suggestions. What
can be your next uh course of letter? So
you get the word so you can don't need
to type the rest. So autofill is your
data entry co-pilot in Business Central.
It helps you remove that barrier of TDS
typing and it's not just the typing,
it's uh the uh finding new information
within Business Central and cross
reference that. So uh let's go in
business central and see autofill how
you can access it and how you can uh use
it. So, at the moment, I'm on the
currency card and I'm typing currencies
and uh I'm on the Japanese yen. So, we
have plenty of unf uh uh empty fields in
here. And uh I want to add a symbol. And
of course, I can go look it up. I can
find the character. I can copy it, go
back to Business Central, paste it, and
so forth. But I lose my context. I don't
want to go out of business central. My
task is here. there was this sparkle
icon that we saw. I pressed it and
within seconds I get suggestion of what
uh what that symbol is and it seems that
it's correct. I can uh find additional
information about the suggestion that
I've received here. And uh I can see
that okay, it's commonly used. That's
the symbol. That's amazing. I want to
keep this. But we also get two
additional suggestions in here. I don't
know where these two come from. So I can
uh see that this is a frequent choice.
And right now I know that most of the
data that is entered here comes from
business central and this is a great way
for me to stay and see what other places
uh what what the value for this field is
in other places.
So in essence this is autofill but uh
let's dive under the hood and understand
how it works. Um
so as we saw we were in the currency
card um page. So uh what autofill does
is tries to understand the context where
you're at. So we look at at your page,
we look at your user, we look at your
role, we look at the fields, we look at
all the metadata and then we take that
metadata and we pass it on to our data
sources, our suggestion providers. So
for every field and the current
implementation is that we take the scope
of the current fast step where you
invoked autofill from um and we ask
these data sources please give me
suggestions and all of these runs in
parallel. We ask all of these sources
independently what do you think is the
best suggestion within your realm within
your domain of responsibility.
Each of these data sources
provide suggestions for every field.
So we end up with multiple suggestions
for every field. But as we saw earlier,
we only get one. What do we do then? We
uh have to figure out what is the best
one for you for the user within the
context that you currently are. We pay
attention to how much how much data
you've typed already. what does that
mean for your role? What how does that
how is this how are these suggestions
applicable for your current context? And
we try to ground that within the data
that we sent to the um uh to copilot and
once we've ranked them once we figure
out how to uh provide a co coherent
suggestion set that is what we surface
to the user. So we use AI as a decision
engine. We uh look at captions. We look
at uh tool tips. We look at teaching
tips. We look at data types. We have we
look at a lot of metadata to help us
understand what is the current use case.
We look at which fields do we need to
provide suggestions which data sources
are applicable for these fields. Um we
uh we also look what is the what data
makes most sense here. Um and we have at
the moment um five or six uh data data
suggestions uh sources uh the most
recently used value the most frequently
used intelligent lookup selection AI
generated and web search which will be
available later this wave. So um let's
look into all of these suggestions
provider individually and understand how
they work. So for the most recently used
value, every time that you access a
record, every time that you select a
value from a lookup, we take a note when
did you last access this record. That
helps us understand the recency of the
data for how important it is to you to
be able to understand if this is the
most relevant suggestions for you at
this very uh moment. So this data is not
this suggestion provider does not
include an LLM. This is strictly
grounded inside your business central
data.
We also have the most frequently used uh
data source. So unlike um unlike uh
recently used this looks at the scope of
your whole company within of course
respect of your permissions. So uh we
try to find based wi within the uh scope
of your company what is the most
frequently used value
when it comes to lookup selection. Uh
lookup selection data source is uh in
fact uh does include an LLM. It tries to
find what is the best suggestion within
a finite number of options. So if you
take for example a lookup a simple
lookup you have defined 50 100 rows and
that's it and the user can go and scroll
through filter and find the what is the
best option for this uh value we take
this is a finite uh number of options we
get those and we ask an LLM like what do
you think based on this context is the
best this also applies for option fields
and uh and of course lookups.
We have a data source which is AI
generated and this is something that is
uh of general knowledge something that
the general foundational knowledge of
the model can answer but in here we have
the risk that this might be fabricated
as as you might have seen working with
LMS it starts to come up with weird uh
things. So we saw earlier in the slide
that we tried to guard against that. So
we try to ground the data within your
business central data
and uh of course we have uh web search
which is powered by Bing uh and this is
this data source tries to uh do a Bing
search to find what data can be found
online for the data for the context that
you're currently at. So all of these
data sources, we try to mix and match
which fields on your on the p on the
page make most sense and we select the
ones that uh that are just the best with
for your context. Um
can you tell us more about summarize?
Definitely. Uh but I just want to
rephrase that this is a very powerful
co-pilot experience that can help make
our users be more productive. And in
each of the slides that Vas was showed,
there is a thumbs up and thumbs down
icon. And we really appreciate that you
encourage the users uh to to actually
give us the feedback because it helps us
improve the responses for that.
So moving from one powerful copilot
experience to another, let's talk about
summarize, right? So, as I said, Copilot
is your AI assistant for work. And now
it comes with the ability to summarize
any entity by identifying what's
important and what's urgent for the
user.
And it does that seamlessly because it's
integrated seamlessly into your business
central card pages and document pages
out of the box and without you having to
export data to a lot of business
applications or without you having to do
lot of intensive training on the models
or without even users having to get
started uh by writing uh on the prompt.
So let's see a quick tour of it.
So here I am on the customers list and
let's go to any customer. In this case,
I'm going to Alpine ski house
and you can see that uh now there is a
dedicated new area right here what we
call as summary fact box where you can
see the uh the top three most important
thing that the user depending on its
role in this case
accounts receivable administrator would
need to know on this given entity.
Um in this case it's saying it's telling
me that the balance of this customer uh
is this much and it has overdue payments
and I think an account receivable
administrator would be interested to
know if a customer has overdue payments.
It's also telling what's the outstanding
invoice amounts to and what's the total
sales for this customer for this fiscal
year
and it's telling how many invoices has
been recorded for this customer.
So these are the three things that it
figured out behind the scenes by getting
the data from Business Central database
and scoring what would be the important
understanding the user context and then
giving these three important points.
But that's not it. It's also
interactive. So let's see where this
points to.
So you can see here for example when I
clicked what uh clicked on the payments
received total it actually highlights
the fact box it highlights the field in
the fact box where it got the data from
making sure that you know where the data
source came from.
Let's also try another one. In this case
it opens a related page to this entity
and shows that this is where the data
came from.
But if you want to know more then we can
just go ahead and click show more. And
in this case what it will do is it will
show you the three bullet points that
you have already seen and then also
extend more bullet points if you want to
know more about this customer.
So as you can see here and this is also
interactive.
So in this case for example the average
collection period is 40 days. uh gets
pointed and you can notice that it
actually expands the fast tab that uh
that was collapsed before. Uh and
imagine now if all user has to do this
manually they would have to actually go
and find where the data is from. But in
this case it just points right where
what is important and right where it
comes from.
And since this is in chat pen and now
that you know that this customer has
overdue payments maybe you want to take
uh some action based on this
information. So you could just continue
having chat with it with the chat pane.
So let's uh try let's say
let's set up reminders.
Oh
let's try again
live demos.
And in this case, I'm hoping that
copilot can come up and tell me uh how I
can set up the reminders within business
central and it does.
So this is very powerful in the sense
that you can further interact and with
the information you got and make the
right decisions and even further maybe
you can just go and do some actions
based on it. So let's say I contacted
this customer and maybe this customer
said sure I will do the payments
um but I prefer paying by bank. So we
could go to
any purchase invoice
let's say
picking a different customer but uh my
idea is to show you that it's also
available not just only on cart pages
but also document pages
and we could change the payment method
here and Now that we changed for example
some data and we want to see a new view
of this entity we could also click
refresh and this will now generate new
data new summary based on the updated
data that we changed.
So that's the overall uh summary
experience.
Let's see how this was built behind the
scenes. What's happening behind the
scenes? So in this case we start first
with collecting data about the user. We
understand what is user's role about
and then we collect all the related data
that we can find for the entity to you
are trying to summarize. So we get the
fields, we get the fact boxes
information, we get some related pages
that has high aggregated data and then
we send all this data to LLM
to figure out what are the insights
based on the data. And how does it do
it? It does it based on understanding
the entity that we got in the data, the
metadata and also understanding the role
of the users and then it comes up with
set of insights
and then what it does it it scores those
insights based on the context that we
have provided in the data
and then it pretty much produces the top
three bullet points with the markdown
interactive markdown and that's how we
see the summary.
And this is how we built the overall u
insight full summary generation process.
But that's not it. It's not a one-time
thing. What we plan to do is to evaluate
the summaries that are generated based
on the feedback but based on the manual
tests and automated test. And then we
want to understand is it good good
summary. Is it a five out of five star
rating or do does it needs to be
improved? And when we get something that
needs to be improved, we want to make it
an iterative process where we can add
more data sources, maybe data from
ledger entries, maybe data from outside
business central. And we want to
understand more about the user. What was
the intent of the task of the user? Uh
and then we want to make this an
iterative cycle. So better insight
generation and uh better summaries.
So as was said in these features AI is
the decision engine be it to understand
what facts are reachable from business
central be it to understand what are we
looking at what data are we dealing with
metadata we are dealing with and which
of these is important or urgent and what
can be correlated together to pro to
present a comprehensive insightful
summary.
And how does data uh how does AI decides
that based on the data sources? The data
sources in summarize case are record
fields, fact boxes, related tasks and
the context of the user. Let's deep dive
into each of these. This is where you
can also contribute as an AL developer
because if you understand how these data
sources work, you can make sure that
your custom entities are built in a way
that improve these co-pilot experiences.
So let's see
first and foremost data source for a
given um entity is the fields that are
visible on that page definitely.
Um
this also includes for example for
document pages the the subp parts like
lines they will be also sent to LLM for
figuring out the insights
and of course it respects permissions.
So there is never ever going to be a
case where AI can access more
information than the user uh who's
trying to get the summary
and it also respects users
personalization and customization. So if
you have spent time uh uh deciding this
should be the layout for this particular
user's role or this particular user's
experience that will be respected.
So when we get the fields from the page,
we also want to make sure that we get
all the surrounding uh related data. And
there are multiple ways to define how a
data can be related to an entity, but we
want we wanted to prioritize and make
sure that we send the one which has more
insightful uh data to LLM already. So we
went with fact boxes as these are
related facts that are already visible
uh on the page. And in this case now
let's deep dive a little bit more
because not every fact box that you
would see on a given page will be sent
to LLM. For example, we are excluding
some um metadata some system fact box
for example links and notes for now. Uh
we are excluding some fact boxes which
has a provider property. If you are an
AL developer, it basically um if you are
on a document page, a provider property
tells which sales line is selected. Uh
for example,
and this again respects permissions, I
repeat, and respects personalization and
customizations.
Next is related statistics pages. Um
in this case we defined the related st
related pages as the actions that you
have defined on your current page. Those
actions lead to some other pages right
and those are the pages that we think is
related pages. Um and that's how we
started building on those. So we wanted
to get all the related data.
Uh but then over the time we realized
that we want also the summary to be very
performant. So we wanted to filter out
the data. So we started filtering out
the data with pages that would have
names, statistics or stats.
So in that case all your statistics
pages will now be sent to the data from
that will be sent to LLM for generating
the summary. Why statistics pages?
Because they provide aggregated and
analytical data view already. they they
already have the statistics in that.
Um, as an AL developer, you would want
to know these two things. The actions
that you define on your AL page where
you're getting the summary, they need to
have they will be only sent for
summarization if they have run object
property defined. So they deci that
property decides which page to open and
the filters that you will define on
those those actions will be respected.
So
if you're on a sales card and if you
have an action that goes to um customer
and the customer is filtered by the
customer that is defined on the sales
card sales document then that filter
will be respected. So only that data
will be sent to LLM for that particular
customer.
Okay, these are the data sources, but we
also send information about users. And
where do we get that information from?
It's the settings that you have already
defined for your user.
For most important setting that we care
about in summarization is the role
because we want to make sure that the
summary is role tailored
because co-pilot and agents they deliver
more accurate relevant and valuable
responses when they know user context
and summaries specifically become more
effective when they are personalized to
the user's role.
So that was all about how we built
summarize but now we want to know how
you can integrate your custom extensions
to make these experiences better. So
let's talk about extensibility was
thanks Monica. So uh let's talk about
extensibility. So
autofill and summarize are features that
are our platform. So uh they come out of
the box and they work for every page for
every field for every extension. So they
are not directly extensible. So you
cannot write any al extensibility to
these two features for the time being.
But we are exploring options like how we
can enable you to do that. and uh
what you create and what you place in
the metadata can heavily influence the
performance and the accuracy of these
two features. So it's very important to
write good metadata. Let's look into how
you can do that. So for this particular
exercise we thought let's write a small
extension that we can uh define certain
rewards and we can assign rewards to a
customer.
We have created a small table where we
can uh place a reward ID and a
description of what these uh this uh
reward does. And then uh we have some
parameters which uh define certain
criteria of whether or not people uh
customers satisfy that.
We created a page where you can create,
edit and view all of these. And as you
can see on this page, we have defined
tool tips, descriptions, teaching tips
where we explain very precise what this
does, what this field does, what is this
page all about. As we showed earlier, we
take the context from the metadata. We
the AL uh the AI LLM
understands the context as much as this
metadata tells us. So uh writing good
metadata is key. We draw inspiration
from the tool tips from the description
from teaching tips. that's helpful for
your users to uh onboard them to your uh
extensions but it also helps platform
features such as autofill and summarize
to understand your use case better. So
all of these we have defined very spe u
very precisely very verbosely and uh we
have a extension on the customer card
where we have added this field. So if I
go now to business central and uh I see
let's uh take adm corporation we can see
that we have these fields here but let's
create a new customer. I want to create
Microsoft as a customer and I'm going to
write Microsoft development center
Copenhagen.
So uh we have these two and we can see
that autofill appears for these as well.
So I can invoke it and uh we get your
extension as well to understand the
context of the customer card better and
Microsoft gets no discount. Oh why is
that? No. All right because yes. So this
is a new customer. It doesn't have any
purchase. we're not entitled to
discounts. So, uh this way you can help
the platform, you can help these two
features to give better results for your
customers.
How about summarize? Of course, it also
works with custom extensions. So, let's
let's uh continue on the reward
extension. And here we have a
rewards page. So, let's go there.
I'll just close this. Let's keep this. I
think it's fair that we don't get
discount.
Okay. So, let's start with the rewards
page.
Um and here you can see that
we also have a summary fact box
available for this custom page
and it shows the summary for completely
uh custom page and it mentions that the
top three things that we need to know
about this custom reward uh card.
Awesome works. Um, so remember that all
copile copilot features rely on good
metadata.
Please use descriptive English text to
describe your apps so the LLMs can
understand it better and uh use role
tailored profiles because that is really
important for you to get rotailored
experiences. It helps with security. It
helps with segregation of duties. It
helps copilot give you better results.
Definitely
and we can't talk about copilot
experiences without talking about
responsible AI. So I want to make sure
that uh the you you understand that
these features are built with
responsible AI in mind which means uh we
follow all these six core principles
while building uh co-pilot uh these two
experiences and I suggest if you're
building copilot experiences please also
follow these principles. Fairness means
how AI allocates um opportunities,
resources or informations in a way that
is fair to all the users. Reliability,
safety, privacy and security ensures
that we are considering how the system
functions for people across different
use conditions and context.
Inclusiveness
looks at how the system should be
designed to be inclusive for people of
all abilities. And finally, transparency
and accountability accounts for how
people could misunderstand, misuse or
incorrectly estimate how the AI could be
used. So we need to make sure that we
are creating the experience with all of
these six principles in mind.
And uh one more thing that we would like
to mention that with these experiences
admins are in control. So they have the
control in the sense that these features
are on by default for all the users but
they can go to copilot capabilities page
and turn them off um if if needed.
They also come with distinct permission
sets. So admins can choose to enable
them for few selected users only if
that's what they want. So admins are
always in control.
Okay. Uh last but not the least because
we want to have some time for Q&A is
that both of these features are in
public preview currently. They are
available in all business central uh
online experiences in desktop.
They support all type of environments be
it trial, sandbox and production. Uh
right now they are only supported in
English but officially they are
available in all the languages. So that
means uh there might be um some uh some
behaviors that we not support in other
languages but English is fully supported
and as we said they work with custom
pages and fields already but they are
not directly extensible in AL yet
and do you want to talk about uh what's
coming next in autofill? Yes. So uh we
have demoed multiple times Bing uh and
web search with autofill. We are working
on releasing that later that wave. So
for those who have used autofill that's
coming up soon. Okay, that's it uh for
this these two experiences. Uh now it's
Q&A time and I can see a hand already
there. So let's start it.
Yes. Okay.
Um you saw uh you you showed the um tool
tip property in the page and since the
new version it's possible to do this uh
with the tables. Is it also planned to
have the about properties in the tables
in the future or does it uh interrupt
with your features? So uh the about
properties are part of the onboarding
framework in business central which
define teaching tips for pages. So uh
they are related within the page
context. So uh we don't have any plans
yet to move them on a table level. All
right. Thanks.
There's a question here. I'll get back.
Thanks. Um, you mentioned that in
principle all fields can be autofilled
but in the example I once saw credit
limit being filled and once it not being
filled. How do you influence when a
field is is can be autofilled or not?
Thank you. Great question. So at the
moment there are some limitations of
what autofill supports. We don't support
boolean fields and date fields. We are
working on expanding the coverage to all
fields on the page, all data types in
essence. But when it comes to supported
fields and sometimes getting results and
sometimes not, it also depends on the
context. It depends on what the data
sources have provided suggestions for
and whether copilot evaluated are these
good suggestions for your context
because sometimes
the suggestions might not be relevant
and we don't want to force wrong values
onto users. So not receiving suggestions
is better than receiving bad
suggestions.
Yes. I have another question regarding
autofill. On one of the first screenshot
you showed on on the currency card, the
account number was prefilled but account
number is a lookup to another table. How
does it work? Do we fit all the
available accounts to copilot and can we
control it somehow? Does it consider the
filters on the table?
So
yes, I believe so. Uh so when
when it comes to lookups there are
multiple options that multiple data
sources that can provide suggestions for
so I'm not sure like I can't remember
whether I showed which data source
provider provided that suggestion but uh
in certain cases it might just be the
most frequently used values and in this
case that particular filter is not
applicable but uh in the cases of lookup
selection as we saw where we get to
choose bas on the finite number of
option that is respected. I see. Thank
you.
Any more questions?
No. Good. Thank you very much. We have
the t-shirts for first two uh people who
asked the question. So I guess it was
one of you was it
was
go
No more questions. Thanks everyone. Okay
then. Thank you everybody. Thank you for
your time.
