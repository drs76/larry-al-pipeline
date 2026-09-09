# Transcript — Business Central agent instruction history

- **Source:** https://youtu.be/WFAZLsUTk20
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
Hello everyone and welcome to the video
about agent instruction history. My name
is Nicolola Kukria and I'm a principal
software engineer. One of the areas that
I'm working on is agents. In this video,
I'm going to show you how you can use
the agent instruction history in order
not to lose any work. We are autosaving
all of the instructions that you are
typing in the agent playground.
Every time when you run the task, we are
going to save a version to the
instruction lock. And this way we are
ensuring that you do not lose any work.
You are still able to save the specific
instruction version to the history. If
you want to do it manually. So if you
have typed something that is quite good
and you would like to preserve it as a
specific version to history, you can do
this through this specific action.
Now I'm going to show you how you can do
this within the business central UI. To
show you this one in product, if we go
to this agent that I was developing in
the background and invoke the edit
instructions, you will see that I have
the buttons now to save history, view
history and also download the
instructions.
If I invoke the button to download the
instructions, I will get it to saved
automatically to disk.
If I invoke view history, you will see
that it was saving everything that I
typed in if I ran a task. We wanted to
avoid saving too much and creating a too
long uh list. Thus, we believe if you
run a task with a specific instruction
that you have created a significant
amount of work that you would like out
to saved. You can quickly navigate
through the list and you can give them
also a specific name if you want. So for
example for this one I can name this one
to say that I added
create reminders
functionality
and then I can quickly see what this
version is about. You have also the
option to multi select it and to say
download selected. Then we are going to
zip it and you will get all of your
versions back to the disk. Because we
don't have good capabilities to do the
diff within the client itself. You can
use this functionality to download it to
disk, open it in Visual Studio Code, use
Beyond Compare or any other tool if you
need to analyze the instructions to get
to the version that you would like to
get restored.
Also, you will see here that they are
arranged by the specific time. So, it
should be relatively quick to find the
instructions that you need. However, if
you are in the situation where you need
to use the download selected, you have
this capability as well.
The last thing is that you can do the
save to history. So if I would like to
save this to a history. Let's say that I
make a change that I would like to
preserve to say do not create sales
invoices. And imagine that I typed more
text here which I would like to save.
Now I can say save to history and I can
give it a name
and it's up to you how you version these
specific things. Now when I got it, it
got saved to the history.
And if I update the agent like this and
if I go back to it
and then I edit the instructions and
let's simply like delete a dot and
update it again. The thing that you will
see now is if I go back to the history
is that it preserved my previous version
and it added a dash two to the change
that I'm just made by deleting few dots.
So to summarize the video, you have seen
that we are saving instructions to
history each time when you run the
tasks. Thus, you should not worry if
you're going to lose any of the work
that you did.
You have the option to manually save and
edit the version names. So you can
quickly find or go back to the specific
versions. And the thing that I would
like to highlight is that you need to
export manually as you have seen me
using the download button because we are
not exporting the instruction history
when you are exporting the agent. If you
have any feedback to this functionality
or would like to reach out to us, please
reach us through the Viva engage. And
thank you very much for your attention.