# How CHILI GraFx handles your data
*A plain-language guide — no legal jargon, just the facts*

> 📋 **This is an explainer, not a contract.**
> We wrote this so you can understand how we handle your data without needing a law degree — or a strong coffee. The binding details live in your contract and our Data Processing Agreement. If there's ever a conflict between this document and the actual agreement, the agreement wins. (Sorry, the lawyers insisted.)

When you use CHILI GraFx, you share some information with us — that's normal for any online service. This guide walks through the most common situations and explains what data is involved, where it goes, and who is responsible for it.

---

## Who's who

Before diving into the use cases, it helps to understand the different roles in the ecosystem.

**CHILI publish** is the platform provider. We build and operate CHILI GraFx.

**Our customers** are the organisations that sign a contract with us. This can take two forms:

- **A brand or company** using CHILI GraFx directly — for example, a retailer whose in-house team builds templates and generates output. In this case, the **template designer** and the **end user** are both part of the same organisation.
- **An ISV (Independent Software Vendor)** that builds a product or service on top of CHILI GraFx and offers it to *their own* customers. In this case, the ISV sits between CHILI publish and the end users.

**The ISV layer matters for data responsibility.** When an ISV offers a CHILI GraFx-powered solution to their customers, they take on the responsibility of governing how data flows within their product — including informing their customers about data processing, obtaining the necessary consents, and ensuring their own terms and privacy policies cover the use of CHILI GraFx as an underlying platform. CHILI publish remains the processor; the ISV is the controller for their customers' data.

---

## Use case 1 — Logging in

When you create an account or sign in, we store your **name, email address, role, and login credentials**. Your password is never stored as plain text — it's scrambled (hashed) so even we can't read it. Login is handled by a specialist security service called Auth0.

This data is classified as **Platform Data** and is always stored in West-Europe (Amsterdam), regardless of which data center your environment uses.

`Platform Data · stored in Europe (Amsterdam)`

---

## Use case 2 — Creating a template (no personal data)

When you build a Smart Template — adding frames, layouts, fonts, images, and logic — everything is stored in your environment. "Locally" here means the data center you selected when your environment was set up.

Available regions: Europe (Amsterdam), US (Virginia), Australia (New South Wales), UK (London), France (Paris).

Your template files, assets, and settings stay in that region. CHILI GraFx stores them but does not read, edit, or share them with anyone else. As long as the template contains no personal information about real people, there are no additional data responsibilities on your end.

`Service Data · stored in your chosen region · no PII involved`

---

## Use case 3 — Creating a template that contains personal data

Some templates include personal data directly — for example, a designer manually enters a person's name, address, or ID as part of the template content or as a variable default value.

In this case, **you (the template creator) are the data controller**. You are responsible for:

- Making sure you are allowed to use and store that data
- Ensuring it is handled in line with applicable privacy laws (e.g. GDPR)
- Not including more personal data than is strictly necessary

CHILI GraFx acts as the **data processor** — we store and process that data on your behalf, and we take that role seriously. We are contractually and legally bound to keep it secure, process it only for agreed purposes, and handle it in line with our Data Processing Agreement. Responsibility is shared: you decide what goes in and why, we ensure it is handled safely.

> ⚠️ **Your responsibility:** If you enter personal data into a template, make sure you have a lawful basis to do so. CHILI GraFx will handle it securely as processor — but the decision to include it, and the legal basis for doing so, rests with you.

`Service Data · stored in your chosen region · shared responsibility`

---

## Use case 4 — Template fed by a data source connector

Some templates don't contain personal data themselves, but pull it in dynamically via a connector — for example, a data connector linked to a Google Sheet, a PIM system, or a CRM.

In this scenario, the data originates **outside of CHILI GraFx's infrastructure**. That external source — the Google Sheet, the CRM, the database — is hosted and governed by a third party (e.g. Google, Salesforce, your own systems).

**What this means in practice:**

- The data may or may not contain personal information — that depends entirely on what is in the connected source
- CHILI GraFx processes the data at the moment of output (to generate the result), but does not permanently store the incoming records
- The **template designer** who set up the connector is responsible for knowing what data that source contains and whether it includes PII
- If the source contains personal data, the same responsibilities apply as in Use case 3 — you are the data controller, and CHILI GraFx is the processor, with all the same obligations to handle it securely

> ⚠️ **Your responsibility:** Before connecting a data source, verify what data it contains. If it includes personal data about real people, make sure you have the legal basis to process it and that the data transfer from the source to CHILI GraFx is lawful. We will handle it securely on your behalf.

`Service Data · data origin is outside CHILI GraFx · shared responsibility`

---

## Use case 5 — End users working in GraFx Experience

GraFx Experience is the branded, end-user-facing layer built on top of CHILI GraFx. Your organisation chooses to offer GraFx Experience as a front-end solution, allowing non-technical users — customers, sales teams, retailers — to personalise and generate output from pre-built templates.

**GraFx Experience is currently available in one region only — Europe (EU).** This means that data handled within GraFx Experience is processed and stored in the EU, regardless of which region your CHILI GraFx environment is hosted in.

When end users fill in a template through GraFx Experience, data flows in two directions: output generation goes through your CHILI GraFx environment (in your chosen region), while data stored within GraFx Experience itself — such as projects and user inputs — is persisted in the EU.

**What this means in practice:**

- Your organisation — as the operator of GraFx Experience — is the data controller for what your end users submit
- You are responsible for informing your end users about how their data is used, and for having a lawful basis to collect and process it
- Data that flows through CHILI GraFx for output generation is handled as Service Data, with the same security and privacy obligations as all other use cases
- Data stored within GraFx Experience is kept in the EU, independent of your chosen CHILI GraFx region

> ⚠️ **Your responsibility:** If your GraFx Experience collects personal data from end users, make sure your own privacy notice covers this — including the EU data location — and that you have a lawful basis for the processing.

`Service Data · EU only (GraFx Experience) · your chosen region (output) · your organisation is data controller`

---

## Our promises

**🏠 Stored close to you**
Your template files and assets (Service Data) are stored in the region you choose: Europe, US, Australia, UK, or France — all on Microsoft Azure. Account and login data (Platform Data) and support tickets are always stored in West Europe.

**🔒 Encrypted everywhere**
Data is encrypted in transit (HTTPS/TLS) and at rest — secure while stored and while travelling.

**🛡️ Independently certified**
CHILI publish is ISO 27001 certified — an internationally recognised security standard, audited externally every year.

**👀 Monitored 24/7**
Systems are watched around the clock for unusual activity, with automatic alerts if something looks wrong.

**🚫 Not sold, not shared**
Your data is never sold to third parties or used for advertising. Certain trusted sub-processors (such as Auth0 for authentication and our support platform) handle specific data as described in this guide — all under the same privacy and security obligations.

**🔁 Backed up regularly**
Data is replicated across multiple locations to protect against loss. In the unlikely event of a serious incident, our recovery policies minimise disruption and data impact.

---

## Other situations

**Using AI features**
CHILI GraFx uses AI to assist with things like scripts (actions) suggestions. Your data is used *only* to produce your result — never to train AI models, and never shared across customers.

**Contacting support**
Support tickets are stored as Support Data in West Europe. Our support team includes people based outside of Europe — all vetted and contractually bound to the same privacy and security rules. Only include information in a ticket that is strictly necessary to resolve your issue. If you include personal data, the same responsibility rules apply as above.

**Requesting data removal**
Under GDPR, you have the right to request deletion or export of your data. How that request is handled depends on the type of data:

- **Service Data** (your templates, assets, and output) is controlled by the company that manages your account. We will direct you to them, as they are the data controller and decide what happens to that data.
- **Platform Data** (your login and account details) and **Support Data** are controlled by CHILI publish. Requests involving this data can be directed to [security@chili-publish.com](mailto:security@chili-publish.com).