# Transcript — Working with instructions for agents in Business Central

- **Source:** https://youtu.be/1IIlArcHpOY
- **Channel:** Microsoft Dynamics 365 Business Central (official) — 25:17, published 2026-02-27
- **Ingested:** 2026-07-06 (auto-captions, cleaned; artefacts: [snorts]=filler, "enom"=enum, "compilot"=Copilot, "RO"=role-centre)
- **Distilled into:** `reference/AL-REFERENCE.md` §28–29

---

[music]
Hello everyone and welcome to the
session about working with agent
instructions. My name is Nicolola Kukria
and I'm a principal software engineer at
Microsoft. In this session, I'm going to
show to you how you can write the agent
instructions and how you can iterate on
them to make the agent complete the task
within the business central. So for the
agenda today, I'm going to show to you
how you can structure the instructions
and how we are structuring them within
Microsoft. Then the next topic is about
using tools.
We are also going to go through
troubleshooting tasks and improving
instructions.
Then uh I will show you how you can use
the history to navigate between the
different versions that you have used in
case the previous version of the
instructions was better. And we are
going to end up with some tips and
tricks how you can improve the agent
accuracy within the business central.
Before we start, I wanted to share a few
words about the strategy that we are
using in Microsoft when it comes to
writing instructions. Before we needed
to be very verbose. So it was necessary
to outline every single step that the
agent needs to do in order to complete a
business process.
Today because the models became much
better. The rule that we are using is
that less is more. So you do not need to
outline every specific step that the
agent needs to do. It is sufficient to
outline the most important steps so the
agent can follow the business process
that you want it to do. As you probably
know, there are many different ways
within the business central that you can
complete a specific business process.
So, it is good to outline the steps and
the business process that you would like
the agent to do.
As you're writing instructions, it's
important to remember that instructions
are a part of the bigger prompt. So,
everything that you write, the platform
is going to take it and it's going to
wrap it as part of a bigger prompt that
you're unable to see. Within this
prompt, we are protecting you from model
changes, making sure that the agent is
able to use the tools and we are also
protecting you from attacks like prompt
injections and other similar attacks
that can be used for AI. So when you're
writing instructions, you do not need to
think about these things because the
platform is going to provide them for
you.
So that was all for the introduction.
Now we are going to move into a demo and
we are going to write instructions
together. For the demo today we are
going to create a rather complex agent.
So here we are going to say create. We
we are going to create the agent from
scratch and today we are going to
prototype in automating the tasks in
accounts receivable area. So for this
reason we are going to name the agent
account receivables agent. All of the
other fields are out of field. We are
going to leave the description blank
because it is not affecting how the
agent runs. And for the profile, as I
mentioned in the previous videos, it's
very good that you limit it and to make
the profile rather small for the agent.
However, for this demo, we are going to
use the full profile, which is accounts
receivable administrator. This might
make the agent a little bit slower to
run and it can affect the accuracy.
However, for these scenarios that we are
going to use today, the accuracy is not
going to be affected. For permissions,
for prototyping and demo purposes, you
can use super. As we have mentioned
before, agent is never able to do more
than the user giving it tasks. So, the
agent is always going to be limited by
the permission set of the user that is
interacting with it. However, it is
really a good practice to limit the
agent's permission set before using it
in production. And for the instructions,
we are going to provide a very brief
instructions which are describing the
role that the agent is going to do. And
this is called RO based prompting. It
helps setting the context for the agent
because if it knows who it is and which
task it is supposed to do, this tends to
improve the accuracy and overall
behavior of the agent.
The next section that it is very good to
add is called guidelines. The way how we
are writing it in Microsoft is that we
put a dedicated section like this.
Within the guidelines section, we
recommend that you outline everything
that is applying for this agent across
all tasks. So within the guidelines, we
are writing all of the instructions that
the agent should apply to all of the
task that it is doing.
We usually put some communication
guidelines how to format the emails and
the outgoing communication to the end
users. This is the prompt that we are
using for sales order agent and you're
free to use this example because we have
tested it and for us it works well. But
you can also specify some other business
process related things. For example, you
can say do not post any draft credit
memos before asking the user for review.
And then in any process that the agent
is doing, it is not going to post the
draft credit memo without asking the
user to review.
And the second one is for example if the
customer has not provided his email or
the number go to the customer list and
check if it exists because if you if it
is interacting with the customers it is
good to check if the customer already
exists.
The next section that we are going to
provide are the business specific
instructions and we put them in the
category for its own. And the first task
that we are going to give to the agent
is handling sales returns. So here I
have briefly outlined the process that
the agent should do. I wanted to
identify the customer by email, check if
the invoice exist and check if the item
is eligible for returns according to the
Danish law.
Now if I say okay, we will save these
instructions. And now we are ready to go
to the UI where we can edit the
instructions and run the task at the
same time. So I'm going to invoke this
action. It is going to ask me to save
the agent and activate it before
proceeding. I will say yes. It will
close the setup dialogue. And now I'm in
a dedicated UI which is allowing me to
change the instructions and run the task
at the same time.
For the demo today, I'm going to run the
task where the customer is complaining
about items that the customer has
received that are damaged. And I'm going
to quickly fill out this invoice. I'm
going to provide the title simulating an
email that the customer would send. I'm
going to provide an email address of the
customer and I'm also going to provide
some message text as a body that they
have received damaged chairs.
As the last part, I'm going to upload
the attachments. The first attachment
that I'm going to add is the invoice
that the customer has received from us.
So, they're referencing this specific
invoice.
And the second attachment that I'm going
to add is a picture of the damages that
they received. In the email they have
said that they want to return all the
chairs and because they have ordered the
lamps to match the chairs they would
like to return the lamps as well. If we
look at the invoice we can see that they
have ordered multiple items. There is a
desk. There are multiple chairs and
there is a lamp.
agent is going to be able to read this
document because platform is able to
send PDFs and images to Azure document
intelligence and extract text from them
and the LLM has the power to analyze
what is a chair and what is a desk what
is a lamp these kind of scenarios would
be impossible to code in traditional way
[snorts] however now you're able to use
them out of the box without writing any
out.
If I close this one and zoom out,
chairs, they have [snorts] attached the
chairs here. If we open the picture,
we can see that this is an image of the
Paris chairs that we are selling. It has
scratches and it has a broken leg. One
thing that I would like to highlight is
that the platform is only extracting
text. It is not able to do the machine
vision. So it will know that there is a
scratch of 30 cm, 50 cm and a broken
leg. But it will not know that there are
four circles here on the picture. So
this is the information that you would
need to use a different tool to extract.
Okay. So the task is running
and let's see how the agent is going to
do it. I'm going to maximize this part.
And now within this part we can track
how well the agent is doing and all of
the steps that it is performing.
In order to refresh the page you can use
either the refresh action or you can
easily press F5 and watch the agent how
it executes the step in real time.
Here we can see that it has logged in
and it is navigating to the customers.
It's following the instructions from the
PDF. It read and it remembered that the
contact is and detail. So it's searching
for the customers. It managed to find
the customer and now it is searching for
the sales invoice if it exists.
And now it is asking for the assistance
because it was unable to find the sales
invoice for this specific customer. I
have not created this one in the demo
data. So it's doing a good job. So here
I'm going to give it the instructions
simply to continue [snorts] because the
invoice does not exist.
So I will write please continue.
I have deleted the invoice
and I will say it is okay to create
credit memo.
This is one of the examples where it can
do some kind of a fraud detection for
you.
Now the agent is going to continue from
the step where it stopped and it is
going to proceed with the task at hand.
Let's continue refreshing to see what
will happen. So it has closed the page
on which it was. And now it is going to
say create credit memo sales document
and it is going to fill out the customer
name and it is going to add the rows.
all three items it has managed to find
successfully. It is going to fill out
the work description which is something
that we instructed it to do. So here I'm
going to click review draft credit memo
and this is the example of the review
experience that the user will have. So
the user will see all of the fields that
the agent has filled. They will have a
small eye icon next to them and there
will be a text above them explaining why
the agent did what it did and then you
can say that it did a good thing and
submit a feedback to us or a bad thing.
Also it has filled the rows and you can
see on each of the row which field it
set together with the justification why
it did it. So I think it did a good job.
I'm going to check the work description
that it filled. So here it says that it
is returning all chairs which is Paris
guest chair black Berlin guest chair
yellow and all lamps which was only a
single item because of the
justification. And you can see that the
chairs had the scratches of 30 and 50 cm
which was specified on the image itself
and one chair had a broken leg. And the
lamps are returned because customer
wants the lamps to match the chairs.
They're going to buy their chairs
somewhere else probably.
This has speeded me up a lot. I can edit
this text if I want a little bit. And
then I'm ready to say to the agent
continue.
And now the task is going to continue
further.
Let's see what the agent is going to do.
So it is invoking the post action. It is
posting the invoice
and it is printing the invoice,
downloading it. The next step it should
be that it writes an email to the
customer together with the attachment.
Now I can click here to review the
message that it's creating. I can see
that it successfully summarized all of
the items that are being returned
together with some justification text. I
can tweak this message here if I would
like because the end user is able to
edit it. There are attachments here as
well the invoice that it printed and
attached to the document. So this one is
ready to be sent to the customer itself.
Uh currently within the current platform
it is not possible that this happens
automatically. You would need to use the
SDK if you want to actually send the
email and there is a video which is
explaining how you can code and get the
email sent automatically. If you click
continue, the task is going to continue
and effectively it is stopped because
each time when the outgoing message is
generated, the task stops and we are
waiting for the new input from the
customer.
Now you have seen how you can write a
simple process instructions within the
business central and the agent is going
to pick up the task and start executing.
However, we are getting a lot of
questions when should you actually use
the instructions and when should you
write the information out in the task
because you have seen I have outlined
the business process in the instructions
itself but the agent is also able to use
a lot of information that are coming
from the task itself. So we are getting
questions from many partners that have
tried this toolkit already. When should
they use which tool to get the task
done? Because specifying instructions in
the task might give you some
flexibility.
And our guidance is that you should keep
in mind that instructions are always
going to win over tasks because platform
is giving a much higher priority to the
instructions compared to the tasks. Our
recommendation to you is that you should
outline the process description in the
instructions because there is no need
and it's not a good practice that you
repeat a business process definition
within each task and it will give you
this behavior that I have just mentioned
that instructions are going to win over
tasks and the agent will not be able to
do something [snorts] that it is not
supposed to do.
task message can still contain these
instructions as long as they align with
the main instructions. And the idea is
that you can use the messages to direct
the agent to do something that varies
between the tasks. So use the
instructions for everything that is the
same across all of the tasks and then
you can see if you can introduce the
message to provide additional
instructions for specific tasks.
You have seen how we have been using the
timeline entry in the example that we
were developing. It is very important to
know that we are introducing defaults.
The defaults that you cannot control are
the beginning message and the ending
message. You can control these through
SDK by giving a task a title. However,
in many cases, the platform is going to
control what is being generated.
the substeps that are inside you can
control by the way how you're
structuring the instructions. So if you
define your instructions as substeps the
platform is going to use them to provide
the caption for specific substeps. In
this example that you can see here, the
substep is named find item availability
and the next substep is named new sales
quote. And we are going to update the
timeline when it starts doing this step
with the task name that it is doing. If
I would go back to the agent that we
defined, we can provide additional tasks
that it can do. For example, it can
create reminders. It can find all
overdue entries. It can find the entries
that are close to be overdue and for
example it can also suggest money
raising opportunities which depth the
customer should chase first.
One additional question which we are
getting is how big the agent should be
because I [snorts] could argue that this
specific agent can be split in multiple
smaller agents.
To answer this question, I would say
that there is no silver bullet or a rule
that fits all. Try it out. see what
works and if adding the additional
instructions is lowering the accuracy of
the agent then consider splitting the
agent into multiple agents. From our
experience, if the tasks are different
enough, you can give the agent the
ability to do multiple tasks.
One of the additional things that you
can do is that you can reference a
another task that the agent should do
within the task.
>> [snorts]
>> So for example when it is creating the
reminders you can also tell it at the
end
start
suggest
money raising opportunities
and then when it is done with this
specific task it is going to continue
with the next task as you have seen in
this specific UI because this is how we
have written the sales order agent.
From the next topic, uh I would like to
explain the user interaction tools that
the agent can use. You have seen all of
these in the demo. The first user
interaction tool is the user
intervention. You should use this tool
when the agent is stuck and it needs
user assistance to proceed. In our
example, this was when the agent was
unable to find the invoice and then it
asked the user if it is okay to proceed.
The second tool that it can use is the
user review. And in this case, the agent
is asking the user to review the work
that it has done. You should use this
tool in all of the cases when the agent
has successfully completed the task.
[snorts] And now it is asking the user
to see if it the work that the agent has
done is correct.
The last tool is the response and here
the agent is generating the outgoing
message. You have seen in the demo that
it is able to attach specific files to
this outgoing message and this message
can be sent to the customer or any other
means that you can implement by using
the SDK
in the sales order agent. This is how
the response is looking like. Uh we have
generic UI for when you [snorts] are
building the agents within the sandbox.
However, if you are using SDK, you can
code your own re review pages for both
incoming and outgoing messages.
To summarize, the user interaction
tools. The user intervention is used to
ask the user for assistance. User review
means that the agent has completely done
it and correctly. And response is when
you the task is done and it is either
sending a message to a user that is
internal in the company or it is sending
it outside of the company. The important
difference between the response and the
two other tools that the agent can use
is that when it uses the response tool
the task is going to stop [snorts] until
the new message arrives.
Another tool that you can use is the
memory and agent is going to
automatically retain all of the history
of the actions taken. It is going to
store every action that the agent has
performed and it is also going to store
automatically any search results that it
does in the list together if it find the
information or if it didn't find the
information.
Now the things that it does not store
that you will need to use in your
scenarios is the state of every page
visited for example fields and the other
things that it can use. If you would
like to store the state of the page then
you need to instruct it specifically
which fields and which data it should
memorize.
The way how you can do this is simply by
saying it memorize the external document
reference number and then it is going to
store it within its internal storage. On
the troubleshooting page you can see
which data it had memorized for a
specific set. You should think of this
one as a key value pair and later you
can reference the values in the
instructions. In this case, I can say
set the value of a specified field by
using the external document reference
number which you have stored in the
memory in the previous step.
There are many more tools available. You
can access this list from the
troubleshooting page. For each step that
the agent does, you can see which tools
it had available so it can do specified
tasks. One of the interesting tools that
we have not covered today is making
to-do lists and you can check the
official documentation to see how you
can write these instructions. There is
also a way that you can write page
specific instructions. If you have a
complicated page where you want to
provide the instructions to the agent on
how to edit it, it is possible to do it
by using very specific syntax. If you
add the parenthesis like this and you
specify page ID, then these page
specific instructions will be available
to the agent only in the case that it
opens this page. If it is on any other
page, these instructions are not going
to be present.
Before we end, I wanted to demo to you
the instruction tab. Here you can access
the documentation article about writing
the instructions. Here we have outlined
all of the best practices that we are
using. You can see how to use some
specific tools.
We are going to be updating this page.
So we recommend checking it out from
time to time to see the updates. And the
additional thing that you can do is that
you can see the instructions history. So
you can see all of the edits that were
done to the instructions
and you can go between the versions if
you see that the changes that you have
done are affecting the accuracy in a
negative way. Another good thing that
you can do is that you can select
multiple instructions and download them
like this. Then you can get all of them
saved as a zip file.
So for the conclusion what we have been
talking today instructions are necessary
and keep in mind they are part of a
larger prompt. So platform is going to
protect you from [snorts] injection
attacks and other things and it is also
going to help you to write a more
accurate instructions. Try to write as
little as possible of instructions to
get the task executed with high
accuracy.
Use the right tools. I have briefly
explained some of the tools and I would
recommend that you check the
documentation article to learn more
about the available tools. We recommend
limiting access. If you reduce the UI by
using dedicated profiles, the accuracy
is going to be increased positively. and
also use the permissions to limit what
the agent can do. Emphasis, for example,
making the text bold by using asteric
signs or uppercasing letters and using
strong marketing, for example, do not,
you must not helps really with driving
the accuracy. Numbering the steps helps
as well from our experience.
If you see that the agent is not doing
the things that you want it to do, we
would recommend optimizing the UI, maybe
error messages, agent is able to react
to the error messages and recover. You
can also improve the tool tips and you
can write the page instructions with the
tool that I have described. You can
think of an agent as a usability tester
because if your users are struggling
with doing some task because it is not
intuitive, most likely the agent will
have issues with this specific task as
well. So that was all for this
presentation. Thank you very much for
your attention.