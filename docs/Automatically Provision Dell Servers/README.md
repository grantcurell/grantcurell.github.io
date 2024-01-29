# Automatically Provision Dell Servers

This tutorial covers the various ways to automatically provision Dell servers.

## Helpful Links

- [OME Template Function](https://www.dell.com/support/manuals/en-us/dell-openmanage-enterprise/ome-3.4_ug/create-a-template-from-a-reference-device?guid=guid-c4b89f0b-7e15-48f6-9210-3ea1e2f74c61&lang=en-us)
- [OME Server Initiated Discovery](https://www.dell.com/support/kbdoc/en-us/000192340/training-video-that-covers-server-initiated-discovery-in-openmanage-enterprise)
- [OME Download](https://www.dell.com/support/kbdoc/en-us/000175879/support-for-openmanage-enterprise)
- [OME Licensing Info](https://infohub.delltechnologies.com/p/new-openmanage-enterprise-advanced-ready-to-bring-new-customer-benefits/)

## Overview

There are two predominant workflows for automatically deploying and provisioning Dell servers.

1. Use [OpenManage Enterprise (OME). OME is free](https://www.dell.com/support/kbdoc/en-us/000175879/support-for-openmanage-enterprise).
   1. The auto deployment feature requires the OME Advanced license to be present on the iDRAC but this is usually added by default by Dell. In my personal experience, I've never seen a server sold without it in all my time at Dell. More info about the difference between the licenses is [here](https://infohub.delltechnologies.com/p/new-openmanage-enterprise-advanced-ready-to-bring-new-customer-benefits/). If this is a concern just ask whoever is selling you the server (whether it be Dell directly or a partner) to make sure they put the OME Advanced license on the server if they haven't already.
   2. I have seen two variations of how OME deploys the server depending on how you want the initial discovery to occur.
2. Manually via the Dell APIs.

### When to Use OpenManage Enterprise (OME) and When Not

**Warning**: Honesty based on personal experience ahead. Forthright commentary serves to save others from mistakes I have personally made or watched others make.

Unless there is a compelling reason not to use OME, it makes life significantly easier and is probably the better solution. 

Potential good reasons to not do **automated deployment** with OME (I bolded the automated deployment bit because for reasons I explain below, you're still going to end up using OME):

 1. You are using Bare Metal Orchestrator (BMO) and have a workflow built there. If this is the case you are probably a TELCO or something of equivalent size and aren't reading this article
 2. You have a significant investment in a multi-vendor deployment solution and already have the in-house personnel and talent up, running, and using this solution

**The worst reason to not do this with OME:**

1. You are me at 27 years old and think building everything open source is better because you haven't yet had to handle or pay for manpower in the maintenance phase of code you have written. (Ok, so I actually never made this mistake with OME, but I did with other things.)

**Benefits of doing this with OME:**

1. Dell is on the hook for support
2. Unless you're going to build an entire patch management framework from scratch, which is a very bad idea because new you are on the hook for making sure patches are applied in the correct order, handling failures, reporting, code maintenance, repository maintenance, and all the other not-so-fun things that come with a custom patch management framework, you are going to want to use OME for patch management anyway. 
   1. I've worked with the TELCOs, they use OME. I cannot think of a valid reason to ever re-invent this wheel.
   2. I am also assuming you are not so cruel to your administrators that in 2024 (or whenever you read this) you will make them do manual patching.
3. OME will automatically take care of BIOS-config templating.
   1. Again, this is another function you will have to manually build and maintain if you don't use OME. I have personally done this one. It's doable, but requires a lot of tedious, boilerplate, code and you will have to write a bunch of logic to handle all the boarder cases you might encounter. This becomes particularly miserable if you have multiple different servers you have to independently account for with multiple different BIOS templates.
   2. Again, this is why TELCOs use OME
4. OME provides power monitoring
5. OME provides config diff tracking
6. OME gives you a one stop shop to monitoring to including grouping servers and applying policies to them based on those groups
7. OME provides a convenient panel for getting to all the iDRACs
8. OME will track all your warranties

Those are just the common benefits, there are a bunch of niche things it does as well that don't apply to everyone (ex: ServiceNow integration).

## OME Workflow

There are two workflows I see with OME: one using server initiated discovery and one where you do discovery with some code framework and load that into OME. If you are in a Dell environment then you probably just want to go ahead and use server initiated discovery. It's one less thing you have to maintain and it again is supported by Dell end to end. If you have a multi-vendor environment and have to build a discovery framework regardless, it may make more sense to centralize discovery in your custom framework. I describe both below.

Here is an overview of the process for either:

1.	Configure OpenManage Enterprise (OME) with the BIOS templates you want.
   You’ll configure the BIOS templates by taking a representative server and extracting the BIOS from it. [OME has a function for doing this](https://www.dell.com/support/manuals/en-us/dell-openmanage-enterprise/ome-3.4_ug/create-a-template-from-a-reference-device?guid=guid-c4b89f0b-7e15-48f6-9210-3ea1e2f74c61&lang=en-us) so you just make one server look exactly the way you want the rest, point OME at it, it saves that config, then you make that your template.
2.	Configure OME to push whatever ISO it is you want to boot from
3.	You get a list of service tags when new servers are given to you and put them in an excel spreadsheet.
4.	Assign the service tag whatever template(s)/iso(s) you want in OME
5.	Set up a job to run Ansible or Python (or I guess PowerShell, but I wouldn’t use PS for this kind of automation) to load (discover) new servers in OME as I described above
6.	Turn on new servers


### Using Server Initiated Discovery




You can have it setup so that as soon as a service tag goes live on the network, you have it contact OME, OME checks its service tag, and then applies the appropriate BIOS template, updates it if you want (to a specific patch level if you need to control that), and then can automatically mount whatever ISO you want. There are Ansible modules for OME here and there is a GitHub repo for Python/PowerShell I manage here. I strongly recommend you use the Ansible modules unless you have a very compelling reason to write custom Python instead. The custom Python you want is here if you go that route. That script is used to register devices in OME automatically. This is the equivalent Ansible module that I recommend. They are actively maintained by paid developers. The Python repo is meant to just be examples of how to use the APIs rather than an out of the box solution. The APIs for Dell are documented here.

What your workflow should probably look like:

