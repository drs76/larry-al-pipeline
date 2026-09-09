# Transcript — How to create agents in Business Central

- **Source:** https://youtu.be/moPzf04Mwlc
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
Hello everyone and welcome to the video
about defining your first agent. My name
is Nicolola Kukria and I'm a principal
software engineer in Microsoft.
In this video, I'm going to show to you
how you can define your first agent in
Business Central in sandboxes without
using any code. Within the business
central environment, there is the A+
icon that you can use that will give you
a quick access to create your first
agent. When you invoke it, we will show
you a guided wizard. And we are going to
select this option to create the agent
from scratch.
Here we need to provide the name. For
this demo, we will be creating the sales
return agent.
And you can see that automatically the
display name and initials are filled
out. We do not need to fill out the
description because description is used
only on this page, not for the actual
agent runs.
On the next screen, I need to select a
profile. We recommend that you use a
dedicated profile for your agent, which
is has been reduced only to the tasks
that the agent is able to do. However,
for prototyping or for this demo, we can
also use the full profile. And I'm going
to select the accounts receivable
administrator.
For permissions, I'm going to give it a
super permission set, which is good for
prototyping or for playing around. We
recommend that you limit the permission
set when you're ready to release your
agent. Also, keep in mind that even
though the agent has a super permission
set, it is not going to have more
permissions than the user giving it
tasks. So agents permissions will always
be limited to the permission set of the
user that is interacting with the agent.
On the next step, we are going to
provide the instructions. I have
prepared the instructions in advance.
I'm going to quickly paste them in here.
And the scenario is that the agent is
able to help with returns and create
credit memos. So now I'm able to select
okay and go to the edit instructions
page.
>> [snorts]
>> The product is going to tell me that now
we are going to save and update the
agent and close the setup page. So I
will say yes and it is quickly going to
take me to the UI where I can give the
tasks to the agents and also edit the
instructions at the same time. To give
the task to the agent, I will select run
task action. And here I'm going to mock
an email from a customer. So I will say
that the title is that they are
returning the items. Here we will fill
the from field
and I'm going to also paste in the text
about the actual customer complaint.
We can also attach the files to the
message that we are sending to the
agent. Agents are able to read the PDF
files and extract text from the images
which you will see in the demo. So here
I'm going to upload a invoice
and I'm also going to upload the second
file which is containing the items that
have the damage and this image has text
that will be extracted. So now if I
invoke okay the agent task is starting.
I can see that the task paint has been
open on the right and I can also scroll
down and track the task execution as it
is going by using this task log part.
Here you can maximize this part to get
even more space. So it is more
convenient to track the task. We can see
that the task has started executing and
we can see all of the steps that the
agent is doing within the business
central. You can see the description of
the task that the agent did. Also, you
can see the reason why it did it. So,
this will help you to troubleshoot the
agentic task much faster. There is also
an additional information that you can
do by selecting view details. And if you
do this for a specific row, we will show
you all of the information that the
agent had available. for example, what
the data was on the page and the
information that the agent has
memorized. For example,
if we keep on tracking the task to see
how well is it doing, we can see that it
filled the work description and that it
invoked the action posting test report.
It printed the report as well. And now
it has drafted a reply and requested
outgoing message review.
Refreshing the UI, I can see what the
user is going to see. So there is an
incoming message. It has created the
credit memo. If I click it here, it will
take me straight to the credit memo.
And within the credit memo, you can see
with the little eye icons and
justification why this one was done. An
indication that this field was actually
filled by an agent. And it's the same on
the lines. You can exactly see which
fields were set by the agents together
with the justification why.
If we go back and we see which what is
the message that it created, it has
summarized the things that it has done
and it has also attached a PDF invoice
here.
Now if you would like to improve these
instructions uh let's say that we would
like to ask the agent to before creating
the credit memo to check if the invoice
exist.
I can simply update the instructions
like this. And now I'm able to say
repeat a task and a new task will be
kicked off with exactly the same
information as the previous task with
the same title and from and the
attachments. And now in the same UI I'm
able to see how this task is going to
run. Now we are going to wait for the
task to complete by either using F5 or
refresh action.
Now agent is executing tasks. We can see
that it has picked up the new
instructions. It is searching if the
invoice exist because it has read the
PDF and it knows the invoicing number.
And now it is going to ask me for the
assistance because it is unable to find
this invoice in the system which is
actually true. We do not have this
invoice in the system. In the review
pane, I can review it myself and I can
give a instructions to the agent. for
example, continue even though the
invoice does not exist.
And now the agent is going to be
unblocked and continue with creating the
credit memo.
On the same UI, you also have a quick
insight to how many copilot credits you
have consumed. The information is shown
at the bottom and you can quickly see
how many credits a specific task is
using.
And for the last thing I would like to
show to you in this video is that the
fact that we are saving all of the
instructions that you are editing. So if
you go to instructions, view instruction
history, you will see that we have saved
the two versions that I have edited. The
first version is without checking for
the credit memo and the second one is
the latest instruction. If you want, you
can select both of them and quickly
download them to the disk if you want to
keep the backup of your instructions.
That was all for this demo. Thank you
very much for your attention.