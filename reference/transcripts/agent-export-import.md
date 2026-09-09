# Transcript — Exporting and importing agent in Business Central

- **Source:** https://youtu.be/3UcLmXqyl44
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
Hello everyone. [music]
In this session, we're going to talk
about how to import and export agents in
Business Central when designing them.
Why do we export agents? It is quite
useful sometimes to back up your agents
when you are working on them and you
want to make sure that you have uh
something to refer to uh and if you want
to restore your agents. The other thing
is that you might want to share them
across environments and easily import
them. And finally, if you want to
product to productize them uh via AL
code through the API, then you can use
this uh uh with the help of Copilot or
as a reference to fill in the
instructions and a few other things.
To export an agent, you can do this
either via the agent card through the
export agent definition action
or you can even export multiple agents
via the agent list.
[snorts]
Let's uh let's look at it in the product
to see how it looks like.
So we are here at the agent list and we
have a few different agents and I have
created this inventory agent which is
supposed to handle inventory and I would
like to uh export it so that I can share
it with uh my colleague who is working
on a different sandbox and prototyping.
What I can do is that I can go to design
and I can click export agent definition
and then I will be able to uh get an XML
file which contains uh all of the
information that is related to this
agent. It will contain its name, its
display name, the different permissions
it's using and also the instructions
that it is using.
After we have an XML file of an agent or
multiple agents, we can now import it.
The importing experience is designed to
offer both security and convenience uh
for viewing what changes will happen to
existing agents.
So in this process, you can preview the
definitions before you import them. You
can review different warnings that uh uh
give you a hint if something is wrong
with the definitions that you are
importing. You can select only the
agents you want.
And finally, you can activate your
agents when they are ready to be tested.
Let's look at how we import an agent
inside Business Central.
We are again in the agents list. And now
I have prepared a set of agents that I
would like to import to try them out and
prototype on my environment. Again, I
can go to the design submen and then I
can click import agent definition and a
wizard pops up that gives me
instructions on how to do it. Here
you'll get a description of uh exactly
what will happen during import and also
things that you should look out for when
importing agents. If I click select XML
file, I can now uh go into my file
system and find this uh agents
definition file which I can now import.
When I click import, I get the preview
of the agents that I'm going to import.
Here I can see that there are three
agents we are trying to import. Two of
them are new and one of them is trying
to replace our existing sales validation
agent. maybe with some changes.
Before I import them, I can check a few
different things. First of all, I can
see what instructions my uh agent is
going to have after I import it by just
clicking on the instructions. This way,
I can be sure that uh I am getting the
correct version of uh instructions for
my agent and that it will work the way I
expected to. The other thing I'm getting
is a validation status column which
gives me warnings and errors for things
that might be wrong with my definition.
For example, if I look at the sales
validation agent and I open up the
warnings, I can see that I get a few
different things, but one of them is a
warning which says that the profile that
it is being imported with was not found
in the system. So if I import this agent
that it will not have a profile. So it
will not be able to navigate the UI. So
I will need to fix it after I import it.
[snorts]
Another thing I can do is that I can
select if I want to replace existing
agents or to add a new one in which case
a new instance will be created instead
of replacing the existing one. After I
have looked at all of this and I am sure
that this is what I want to import, I
can click import.
And then after I import my agents, I get
a view of what was imported and I get
the opportunity to uh activate some of
them if I want them to work directly. I
can do this by clicking on the initials
where I will be taken to the agent card
where I have the buttons to uh activate
it and I can also review the permissions
and the user accesses and a lot of other
settings that are important to an agent.
Finally, I can click done. And now in my
list, I have my new agents.
You can read more about uh how to import
and export agents and how agents work in
general in our documentation in the
links below the video. This was
importing and exporting agents in
Business Central. Thank you very much
for your time.