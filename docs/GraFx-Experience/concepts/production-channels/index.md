# Production channels

A production channel defines where output goes after an end user finalizes a project. Channels are created by admins and made available to specific user groups.

## Channel types

**Print**
A print channel routes output to a print partner. The production partner receives the order details, layout files, delivery address, and quantity. They can update the order status so users can track progress.

**Digital**
A digital channel routes output to a digital endpoint — for example, a digital asset management system, a media platform, or an internal distribution channel.

## What a production channel contains

Each channel has a name, a type (print or digital), and contact details for the production partner (name, phone, email). Channels can have custom fields attached to capture additional order information, such as a cost center or internal reference number.

Access to a channel is controlled by user groups — only users belonging to the configured groups can see and use that channel when ordering output from a project.

## Production outputs

When an end user sends a project to a production channel, a **production output** is created. A production output is a record of that order — it contains the project details, the layouts included, the delivery address, quantities, and the current status.

Admins can view all production outputs across the platform and monitor their status. End users can track their own orders on the Orders page of the portal.

![The Production Channels overview in the extension admin console showing Print and Digital channels with their contact details and user group access](production-channels-overview.png){.screenshot-full}

## Output previews

Separate from production outputs, the extension also generates **preview files** for templates and projects. These are preview images or PDFs used to check the visual result before sending to production. Preview settings (file type, output options) are configured per layout intent in the extension settings.

See [Set up a production channel](../../guides/set-up-production-channel/) for step-by-step configuration instructions.
