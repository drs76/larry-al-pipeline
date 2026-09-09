# Transcript — What's new: Admin Center MCP Server

- **Source:** https://youtu.be/U1dAdtUjidc
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
>> Hi everyone and welcome to this Business
Central Launch Edition session on the
new Admin Center MCP server. My name is
Joost. I'm the product owner for the
Admin Center and I'm presenting today
with my colleague.
Hello, my name is Yuri. I'm a software
engineer and I work on the Admin
functionality in Business Central.
The Admin Center MCP server lets you
interact with the Admin Center API using
natural language just like other MCP
servers.
Yuri, can you show us how to how to set
this up?
Yes, sure. So, let me do that. All
right. So, let's focus
on the demo part.
I'm going to manage Business Central
environments using natural language in
VS Code
via Admin MCP service.
And it's nice that I can set it up
smoothly here in VS Code
because we're using standard intro
authentication. In fact, we're using the
same authentication as we already do use
for Admin API that we have.
And let me just demo how to set it up
locally.
So, I have VS Code here.
If I go to configuration tools
and then if I click onto a button to add
MCP server
I pick HTTP MCP server.
I put the URL for our Admin MCP that we
have.
Give it some name
and maybe pick global environment.
And then there's a
window notifying that it needs to
authenticate.
Um
I picked a user that I want to use and
just click continue.
And after that
the MCP server will run and it will
discover all the tools that are
available.
Um I think yeah, that's how we set it
up. All right. So, now that we're
connected to the MCP server, can we see
what environments we have in our tenants
and and what updates they have pending?
Yes, sure. So, um
I go to um
a chat and ask it in natural language
if um
I can see a list of my Business Central
environments.
So, we can see that agent is using the
tool and then I have
all my four environments available for
me.
So, just using a natural language
question, the MCP server figures out
what tools to use, what API endpoints to
call to give you an answer to your
question.
Um I can see there that there's an an
update that failed recently. Can we
figure out why that happens? Can the MCP
server help with that? Yes, sure. So, I
have a sandbox demo two environment
where I know I was running the upgrade
and it was failing.
So, let me just ask agent um
if we were seeing
upgrades and failures.
So, agent will naturally discover
which tool it needs to call
and then
query for upgrades and present me the
results.
And yep, we have latest failed upgrade
operation which was created
um basically yesterday and it failed.
Yep.
And it also tells me that failure
message indicates that it failed in data
upgrade because of some logic in AL that
that was failing essentially.
All right. So, can the MCP server
figure out where in the extension things
are actually going wrong? What what is
causing this update to fail?
Yeah, of course. So, in our case,
we were creating this
per tenant extension and we made it fail
on purpose
so we could demo. And
therefore, we have source codes here
available. And then maybe we can ask
agent to investigate in the source code
what was causing the failure
and maybe if there is a way to mitigate.
Let me just ask agent about that.
So, we can see here that it's analyzing
the the source codes of the PTE
because it's open in your VS Code
environment. Is that right? Yes,
exactly. Because it's available here
locally
it discovers it automatically um and
then it analyzes the source code.
All right. After some analysis that it
did
we can see that um
it has located the fault
and actually it has found exact place in
the source code that
that we're using to fail.
And it says there is a direct blocker
and and the reason and everything else.
So, the practical fix it said is to
clear failed upgrade.
So, um
and it also told me that um
if you cannot get back into the source
code then you can uninstall or replace
this PTE before you try an upgrade. So,
the MCP server here correctly identified
that we have a PTE that we installed for
this demo to make sure that the update
fails.
Um can we ask it what it would do about
that beyond fixing the extension?
Um [snorts]
yeah, of course.
So, actually
we can ask to uninstall the extension.
If we really need to upgrade and we
don't care about this third-party PTE,
then we can ask it to uninstall. Right?
So, maybe let's do that and see how it
works. Yep.
So, I'm asking this question.
Let's see.
So,
um agent told me that there is no such
tool in the MCP server to uninstall the
extension because we intentionally are
not introducing breaking changes during
preview.
And then it proposed if I could go and
uninstall it manually.
So, maybe we could do that and then I
could ask the agent to check that
extension is really uninstalled and
schedule the upgrade.
Yeah, let's let's go ahead.
So, this is my tenant Admin Center and
this is sandbox demo two environment
that we had.
Um and I can actually
um go to apps here.
Go to per tenant extension and then I
can see that this is the PTE that was
failing
and I can just uninstall it.
I don't need the data and um
yeah.
I'm uninstalling it.
So, now when I have uninstalled the PTE
I can actually ask agent to verify that
it's really gone from my environment and
um
I can ask it to schedule upgrade.
Let's do that.
So, it's going to poll the apps for this
environment until it finds out that the
PTE is gone and after that it can
schedule the upgrade.
So, this is polling for the operation to
complete and once it sees that that the
app has been uninstalled, it will
automatically and immediately schedule
the update?
I think so. Yes. Cool.
Actually, I can give it a hint. Please
check
installed apps on
sandbox. So, it should check
the extensions for this environment and
then upgrade.
So, we discovered that uninstall
operation has completed successfully.
And now it will schedule the upgrade.
If we go to tenant Admin Center
and we go to our environment that we
were trying to forcefully upgrade
we can see that next update is actually
scheduled to current date.
Um and it will run as soon as possible.
Um so, yeah, I think that's it.
Yep. So, you can connect to the MCP
server at this URL as Yuri just showed
in VS Code.
Um but of course, you can use any client
that supports MCP servers including um
Microsoft Copilot Studio to connect to
the new MCP server for the Admin Center.
During the public preview, there are
already a few scenarios where the MCP
server can be really useful
in managing your environments.
As Yuri just showed, the MCP server is
really good at analyzing failed updates,
especially if the source code of any
extensions that might cause updates to
fail is available in the same context.
Um you can also use it to poll. So, for
example, if you are wanting to test the
updates on a production environment you
can ask the MCP server to copy that
environment, wait for that copy
operation to complete and once it
completes, immediately run the update on
the environment.
And finally, the MCP server can also
help you manage what extensions are
installed on your environments their
dependencies and their updates.
Um there's a few things that are good to
know as you're getting started with
this. For now, this is in public
preview.
So, we're still actively working on this
and we have some ideas on how to improve
it in the future. But we're now at the
point where we believe it delivers value
and and we would like to to hear from
you as you start using this. During the
public preview, there's a few API
endpoints that that are available in the
Admin Center API but that are not known
to the MCP server. So, right now you
can't use the MCP server to to manage
the security group settings on your
environment.
You cannot execute potentially
destructive operations like deleting and
and renaming environments
or uninstalling apps.
And also the the settings related to to
linked Power Platform environments are
not available yet. This concludes our
session on the Business Central Admin
Center MCP server as part of the
Business Central launch edition.
Um we're very eager to hear from you as
you start using this, what you think,
how are you using it. Give us feedback
on what's working and what's not
working.
Share ideas on how this could be better.
And please engage with us on on the new
community on Viva Engage. Yuri, myself,
and other engineers that work on this
functionality are very active there and
look forward to hearing from you. Thank
you.
Thank you.