# Transcript — Getting started with Agent testing: How to write Agent evals in AL (part 2/3)

- **Source:** https://youtu.be/aNRzlbxVPWE
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

Now, we are going to show you how you
can write the test yourself and how you
can structure your AL tests
for the agent demos.
And to begin, we are going to start with
the mapping the agent task flow. So,
let's map what
agent is doing when it is completing a
task.
The first step is that a message is
going to arrive, which may or may not
include attachments.
And this is usually the starting point
of the task.
Your agent might be triggered through a
job you or an action that the user
invokes,
but it is going to end up in a task with
a message and potential of you
attachments.
Then the next thing is that the agent is
going to log in and is going to perform
certain steps and actions, and this is
always going to end up with one of the
following.
It is either going to create a message
for you to review.
It is going to ask you to review the
specific records that it has created.
Or it is going to be stuck and it is
going to ask for the user intervention
for the user to actually unblock the
agent.
And if the task was a single turn, it's
going to end here. If it is a multi-turn
conversation or a task,
then we are going to give it a new
message,
and this essentially starts a new loop.
Now, since we know that ERP is quite
busy and there is a lot of users and
code that is changing the data,
data might be changed between the
messages. So, there can be a day passing
or even maybe multiple days.
Users and AL code might change the data
without the agent knowing.
So, this is one of the metrics that we
also need to take into the consideration
when we are writing a genetic test.
Mainly, the question is will agent be
able to pick up these changes and do the
right thing?
So, for the big question is how do we
test this flow?
And in order to test this flow,
we are going to write the evils. And
evil is going to follow this flow
exactly.
But, we will need few additional steps.
One step that we need to add is to
verify the outputs when the turn is
done. So, here you want to check
if it ended with message or the user
intervention or a review request.
So, you need to tell to the test what
you expect the agent to end the turn
with.
And you also have the ability to verify
the data that it created.
So, if it is supposed to create an
invoices or update customers or create
any other data,
you can verify this programmatically
now.
Then, you can also change the data from
AL programmatically and you can
instrument the messages which are
coming.
But, additional thing that you will need
to do in most of the cases is to do a
suit setup. And in suit setup, you're
going to create the data for the agent
to use. And the reason why this is is
important is because
either you're missing these records in
the demo data. And the second reason why
doing your own suit setup is important
is the fact that agent knows
our demo data from internet.
So, in our testing, we discovered that
it wasn't searching for the customer
10,000. It knew that the customer 10,000
is the Canon group.
It also knew all of our item numbers and
similar data.
So, the thing that we are recommending
to be certain that it is not a knowledge
that is coming from the training of the
model is to create your own master
records.
All right. In order to automate this
flow, we are going to be using AL tests.
So, we will be writing code in AL, but
our main component is actually going to
be animal data sets, because the test
that we are going to write
are going to be actual data-driven tests
specified in YAML.
The next component is library agent,
which is going to help you to automate
every step.
If you look at this picture, everything
that is colored light blue, you're able
to automate through data sets and
library agent.
The dark blue part, where the agent is
acting, is going to be running as a
separate session, and over this one you
will not have
control.
Maybe you can control it a little bit
through some specific AL code and event
subscribers,
but it runs as a separate session,
and you cannot influence the agent
directly.
When we were building the framework, one
of the main things that we wanted to do
is to make it fully customizable. So, we
were aiming to provide you with small
building blocks,
and keep in mind that you can arrange it
as you like. I will show you which parts
we have built to be extensible and
customizable out of the box,
but basically, you do not need to use
our framework. You have the atomic
functions, so you can arrange it as you
like.
All right. So, let's look at this main
component, which is the data-driven
tests, which are driving the
test execution.
And for this
example today, we are going to
show you how you can automate the sales
return process.
The process is that the email comes with
the attachments, the customer is
complaining, and we expect that the
agent should create a credit memo.
So, to look at the YAML file on the
left, you can see that on the top you're
using the suit setup, and here you would
be referencing the suit setup by using
the code. And this is the input test
input code.
If [snorts] you specify it like this,
we're going to read this file
automatically and provide it to the
test. And then you are able to do the
suit setup.
The next part that you can see
underneath it is the test definition,
and in the test definition, you provide
the name, description,
and turns.
The turns you can specify as you like.
We have built many predefined sections
already, which are mapping to the steps
that the agent is able to do.
If you need a single turn test, you
still use the multi-turns syntax, you
simply we just define a single turn.
Now, the thing that we would really
highlight is that it is very good for
you to use our own section,
and add to your structures to our own
sections within them by using the
predefined extensibility points. You can
also add your own sections if needed.
However, we would strongly recommend
that you follow the structure that we
have been talking here.
So, one of the main predefined sections
that we have here, which is the first
one, is called turn setup. And here you
are able to create the data before the
agent is acting.
So, you can create the data that is
existing before you give the task to the
agent.
Or you can simulate this thing that
something has happened and then you're
expecting the agent to pick it up and
continue.
In this example, you can see how we are
creating and posting the sales invoice
that the customer is complaining about.
So, we are able to continue with the
return process.
And this part is going to be fully done
in AL.
The predefined sections are on the top.
And things that I have highlighted here
is the free format. We have defined it
like this for our own test.
And for your own tests, you can define
it as you like because you will be
accessing this
data through the
by using the AL code.
Thus, you can name the properties as you
like.
Then the next section is here, the
message arriving. And you can
instruct the agent to do the task by
using query.
Within the query, you can
fill all of the things that are needed
for the task. So, you can define from
who the message is, title, the message
body. And also the very interesting and
cool part is that you can attach the
files.
In the first example, you can see that
you can use resources
and point to the resource that we should
attach to the message when you give it
to the agent.
So, it is possible to attach images and
different things for the agent to
process.
But also on right underneath it, you can
run the AL code,
which is going to print a report. We
will save it into the stream and
automatically convert it into
attachment.
And in order to use this one, you need
to name your own action type.
And then everything under the action
data is free format. You can
define it as you like because you will
be using it in AL code to generate this
report.
This dynamic structure is quite useful
because the dates are changing. Also,
some of the unit prices and something
else might change.
So, this is giving you a lot of
flexibility to generate the attachments.
Then when you give the task to the
agent, it's going to run. And then we
are going to move to verify the output.
And in order to verify the output, there
is a section which is called expected
data.
Here you can say that it is the
intervention request.
It's possible to specify which type of
the intervention request it is, mapping
to the three possible outcomes.
And you can also specify the codes
of suggested actions that you expect the
agent to provide.
Unfortunately, currently it's not
possible to check on the message if the
message of the intervention request as
as you expecting it. But we are planning
that.
The rest of the payload of the expected
data is a free format again, and you can
structure it as you like. And here you
can use it to verify if in this example,
you for example, the credit memo is
created
with all of the lines and unit price and
all of the other fields that you would
like to check programmatically if the
agent gets created correctly.
And then to start the next turn, if you
want to have a multi-turn test, so here
we would say to the agent is that it is
approved.
And please post the credit memo because
the agent should not proceed with
posting
before user approves.
It's quite simple. You follow the same
syntax as we did on the first turn.
In this example, we do not have the
setup data, so we didn't change anything
between the steps.
But you could have added it. We are
moving straight into the query.
And instead of the message, we are
providing the user intervention.
So it is possible to even mock
the user interventions providing the
steps to the agent what the agent should
do.
And then agent is going to start
running. And then on the next step,
we are going to verify the expected
data. Does the posted invoice exist
with the following date?
Yes. And also this part of the body of
the expected data is a pre-format. You
can specify it as you like and you would
implement the validation yourself.
So in short, the YAML files are allowing
you flexibility. And you are able to use
these YAML files to automate every step
of the agent flow.
And as I said, our strong recommendation
to use to follow the main structure to
make have test
name, description, and turn syntax that
you have seen.
And
our also recommendation to use to reuse
our sections. You can add your sections
as you have seen.
But let us know if you need more because
there might be concepts that we are
missing that we can add to the tool and
make the tool better for everyone.
So now,
before we proceed, there is an
additional cool thing that we have added
to the data driven testing and that's
placeholders,
which is making it even more powerful.
So, for the placeholders, the problem
that it is solving is that
you have some text that you need to
change dynamically.
Uh Business Central is using dates a
lot.
And a lot of business logic is
actually tied to the work date.
If I would implement this XML file with
the message and the hardcoded date like
this, which is mapping today,
the problem is that
in the tests,
I would need to change this one quite
often.
And the solution that we did is that now
you can replace the dates with
placeholders like this.
And this is going to calculate
dynamically the work date based on the
current work date and the formula that
you provide here.
So, now in the test, if you are trying
to get the input for the message when
you call it,
when we call today, the platform is
automatically going to calculate the
work date and return you today.
And then, let's say that next month
you're running it, it is going to
automatically replace these dates for
you. So, you can get the files that are
quite easy to support.
Besides the date formulas, we're also
supporting date time formulas and you
can provide them like this.
We have the ability to add even more.
So, if you need something,
let us know and we can see to extend the
tool to provide more placeholders.
And the everything is documented here
under the official documentation. So, if
you go on
to the agent testing
topic, you'll find the data sets.
The thing that I would like to really
highlight is that this is not specific
for agent testing. You can also use it
for data-driven tests
outside of the in tests.
All right. So, you have seen how we can
write the data-driven test by using
YAMLs. The then then the next step is
writing the AL test
and using the library agent to automate
every step.
So, let's see how we can use these data
sets.
The test structure is going to be more
or less similar for every test. The
first step is to initialize as we
usually initialize in the
tests.
And this one is actually mapping to the
suit setup.
If you look at how the code looks like,
within the test itself, the first
section that you will see in the example
is this one
where we are trying to get the agent
from the test suit.
This one is actually allowing your test
to use the picker that Quintin has shown
you in the demo. So, you can test
You can run the same tests on different
agents, change their instructions, maybe
change the model, and see how that the
test perform.
And you achieve this by adding these
three lines to your test.
Then the next
step is to set up the data per suit.
And here you're going to And the last
step is basically to clean up after
every run.
And the good idea is to clean up after
every test. And we would recommend you
to read more. In this example, we are
clearing up all of the sales credit
memos and unposted sales invoices.
So, be assured that the data that we are
giving to the agent is as we would like
it to be.
To set up this huge setup
to provide this huge setup to the test,
you're going to start by using the
dedicated keyword and check if the huge
setup was done.
And then
you can get the content of the file by
using get eval suit setup data input,
which is also a built-in keyword.
If you remember
the sections that I was describing, so
this huge setup that we have defined
here,
the platform code is automatically going
to find this input, which is looking
something like this.
And you can see it's a large file, so we
have moved it to a separate file.
And here we are basically creating
customers.
And then a little bit underneath, we are
creating items because we want to have
different customers and different items.
Important thing to highlight is that we
have not defined all of the fields, but
only the fields that are interesting for
the test and interesting for the agent
to test on.
So, we are going to default the other
fields like posting groups
units of measure automatically by using
test libraries.
Then, once you got to the content, you
are going to need you you'll need to
write real code to do the setup. So,
here we are using a test library
and programmatically through AL, we are
creating customers, items, and posted
sales invoices.
The code is looking something like this.
And here you can see that we are using a
library to create a customer, which is
our standard test library that we would
use in the other tests.
And then on all of these properties, we
are reading them from the YAML and
automatically replacing them.
If you follow this kind of the
structure, you're going to get a lot of
stability because libraries are there to
shield you from the product changes.
And we would recommend to you to set
only the fields that are necessary.
In the end, you're going to set the suit
as completed and then when the next run
is happening, you're not going to spend
time running this code again. So, it is
going to run once per test suite run.
Or you can even make it to run across
the different suits and across the
different code units.
Because you control when this code is
executed by using the old code.
Meaning, you do not necessarily need to
use this pattern. You can code it as you
like.
So, that [snorts] was all about the suit
setup.
The next step is the turn setup and this
one is quite similar to the suit setup.
It's following the same things.
So, you would still use the libraries to
create the data and then you're going to
use the YAML file to change the
interesting parts of the data itself.
Um
the difference between the two is that
this one is going to read from a
different part of the YAML. So, this one
is connected to the turn.
And then when each turn is happening,
you can do the different setup options.
Then the next part is when the message
arrives and to to mock this entire part,
you can use this building keyword which
is called run turn and wait.
And essentially, this helper method is
helping you to provide both the input
message and the user intervention to the
agent.
>> [snorts]
>> So, the helper method is going to read
this query that you have seen in the
input file. It is going to parse all of
the properties that you have,
import the attachments, and even call
your code to insert the files, and you
can run it automatically
and don't think about it.
Also, if you're providing the user
intervention, we are automatically going
to read it from the input. We will see
that you want to do the intervention
request, and we are going to call the
appropriate method
to unblock the agent and to continue the
task.
Once this one is done, you're going to
validate if the turn is successful.
And this is being done by writing the
code.
There is a built-in keyword, which is
called get expected data, which is going
to read the YAML file and give you the
expected data.
If you remember, this section is looking
like this. So, here now in the AL test,
you can use all of these properties and
assert if it is correct.
The thing that I would really like to
highlight here is that you're not using
the asserts to check the data. We are
actually using the text field, which is
called error reason.
And the idea is that
you check and you find everything that
is wrong, and you add it to the error
reason, and then you return true
if it is validated successfully, or
false if you have actually find any kind
of issues, and
you want to stop the test.
All right.
And the last thing is that
you need to finalize the turn.
You can use this by using the building
keyword which is called finalize turn.
This is a wrapper which is going to
store the result
and save a lot of data about the task
and the output to the
history and log.
And it also checks if there is the next
turn defined.
And then you can proceed with the next
turn or not.
The one of the reasons why you should
use this one is because if you use this
method that I have just shown you to
save the results, you in the UI you can
invoke the log entries.
And here in the error text, you're going
to automatically get why did it fail
in the fact box. In the demo that
Quentin did,
this fact box was not visible. We have
added it recently. So, this fact box can
give you a quick input why the failed.
And it is also providing you a quick way
to navigate to this to the steps.
And the second thing that you can do
here is that you can download it.
And then if you download it, you're
going to get a large file which is
containing the serialized output about
tasks, steps, inputs, expected data,
error message that you logged, and any
other outputs that you find relevant for
logging.
These files are built in so you can
upload them to the Azure AI foundry and
run the LLM judges on them so you can
get some analysis
if you use this kind of approach.
And the thing that we are also using it,
which is quite useful, is to use the
agents to analyze what happened to the
test and improve the tests and the
instructions by using these logs.
All right.
And the last topic is how you can
customize this. So, you have seen how we
have wrapped it and the main flow that
you can use to build the tests.
But, you are able to customize and
arrange the tests as you like. So, if
you would like to build different tests
or if you would like to use a different
approach to testing, you can do this.
For this, we have added the library
agent. It has 27 public methods
which will allow you to automate every
single interaction
that you can do with the agent.
>> [snorts]
>> It is supporting asynchronous
operations. So, every task that is
asynchronous, it has and wait
in the name. So, it is ending with and
wait.
Platform is automatically going to wait
for the specific operation to end.
One of the methods that I would like to
highlight is that is very useful is wait
for the task to complete.
And this one is quite good if you are
going to invoke the agent through the
action or AL code.
So, you would like to programmatically
invoke the action as you would like. You
can fetch the task that it was created.
And then, for example, you can wait for
the task to complete.
So, I would recommend to you check out
this library. We believe that the
methods are well documented and let us
know if you have any questions or if you
find any methods that are missing.