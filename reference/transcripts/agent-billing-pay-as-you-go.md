# Transcript — Billing agents in Business Central - configure "Pay as You Go"

- **Source:** https://youtu.be/9esVS6I4wrY
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

We're starting inside Business Central
on the co-pilot pane showing agent
tasks. After some time, a banner may
appear explaining that the evaluation
capacity has been used up. You can
enable more usage by setting up pay as
you go billing for the agents
consumption. Navigate to the Microsoft
365 admin center and select Azure from
the list of admin centers. Agent
consumption will be charged to your
Azure subscription. So let's define a
resource group for it.
Provide a descriptive name and click
next to continue.
Review the selected settings and click
create. The resource group is now
created. Next, navigate to the Power
Platform admin center to continue the
setup. Go to the licensing section to
add a new billing plan.
Choose the Azure subscription option.
Provide a descriptive name for your
billing plan. Then select the
subscription for which you created the
resource group and choose the resource
group itself.
[Music]
Make sure to select Copilot Studio from
the list of products. We are now going
to create a new environment. So for now,
just save the new billing plan. The
billing plan linked to your Azure
subscription is now added successfully.
Navigate to the manage section and start
creating a new environment.
Choose the environment type that matches
the type of your business central
environment where you run the agents.
Select the pay as you go with Azure
option. Pick the billing policy or plan
you have just created. The data versse
environment is now created and linked to
the billing policy. As a final step, you
need to link the data versse environment
to your business central environment.
Open the environment page and select the
link action. Pick the environment you
have just created and save the changes.
[Music]
In a few seconds, the changes are saved
and the billing setup is now complete.
Back in Business Central, you can see
that the banner is gone and the pending
tasks have started running again. If you
want to monitor your build consumption,
you can do that in the Power Platform
admin center. Go to the licensing
section, select Copilot Studio, and
click environments. Select the
environment that is linked to the
business central environment.
You can now see an overview of build
Microsoft Copilot Studio messages there.
Please note that while consumption is
reported regularly by Business Central,
it may take up to 24 hours for this data
to propagate to these pages.
You can also track your consumption via
the resource group in the Azure portal.
Navigate to the resource group where you
can find the cost analysis section
showing the actual and forecasted costs
charged to your Azure subscription. Here
you can create a budget to ensure you
control how much you want to spend on
pay as you go messages during a specific
period. Filter the budget scope to a pay
as you go messages. Provide a name and
set the period for your budget. Then
enter your budget amount.
[Music]
You can also configure an email alert
which will be sent to your email address
when you are getting close to your
budget limit.
The budget is now created and you will
be notified when your consumption
reaches the defined limit.