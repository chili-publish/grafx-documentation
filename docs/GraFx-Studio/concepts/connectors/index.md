# Connectors

## What are connectors?

Connectors link CHILI GraFx with the tools and systems your organization already uses — such as a DAM, PIM, or cloud storage platform. They let you **browse, search, and insert assets directly** into your templates without leaving the editor.  

Instead of downloading files from one system and uploading them into another, a connector gives you **seamless access to approved assets** right where you work.

## How it works

1. **Choose a connector**  
   Your administrator configures one or more connectors (for example, Canto, Keepeek, Sitecore Content Hub, Kadanza DAM, or Google Sheets).  
   Once connected, you’ll see the source listed in the **Media panel** or as **Data source** of GraFx Studio.

2. **Browse or search**  
   Use the familiar folder structure or search bar to find your image, video, or data record.  

3. **Insert into your design**  
   Click to place the asset into your frame. CHILI GraFx links it directly to the source system, ensuring you always get the latest version.  

4. **Update automatically**  
   When the source asset is updated, your linked materials can be refreshed automatically — keeping all local variants consistent with brand or product updates.

---

## Example 1: Connecting to a Google Sheet

Imagine you manage a weekly product flyer. Your product information — such as names, prices, and promotions — lives in a **Google Sheet**.

With a **data connector** to Google Sheets, your template in GraFx Studio can automatically read that information.  
Each product frame in your layout can display live data from the sheet:

| Product | Price | Promotion |
|----------|--------|-----------|
| Apple Juice | €2.49 | 2 for 1 |
| Cereal Bars | €1.99 | 20% off |

When your marketing team updates the sheet (for example, changes a price or adds a new promotion), your layout instantly reflects those changes when refreshed — **no copy-paste, no errors, always current**.

---

## Example 2: Combining Data and Media Connectors

Now imagine the same Google Sheet also contains a **reference to an image** for each product:

| Product | Price | Image ID |
|----------|--------|----------|
| Apple Juice | €2.49 | `IMG-00123` |
| Cereal Bars | €1.99 | `IMG-00456` |

Those image IDs correspond to assets stored in your company’s **Digital Asset Management (DAM)** system — connected to CHILI GraFx through a **media connector** (for example, Canto or Sitecore Content Hub).

Here’s how it works together:

1. The **data connector** reads product information and image references from the Google Sheet.  

2. The **media connector** uses those image references to automatically fetch the correct visuals from the DAM.  

3. GraFx Studio combines both: the product data from Google Sheets and the matching product images from the DAM.  

The result?  
Each product block in your flyer shows the correct text *and* the correct image — all pulled automatically from your connected systems.  
When the content team updates the sheet or replaces an image in the DAM, your template stays up to date with one click.

---

## Typical use cases

- **Marketing teams:** Pull the latest approved product visuals from the DAM into campaign templates.  
- **Retailers:** Connect to a PIM or spreadsheet to automatically fill in product names, prices, and images.  
- **Agencies:** Work directly with client-hosted content systems without manual transfers.  

## Connector Hub

The Connector Hub is the central repository where you can find connectors to install into your environment.

As an Environment Admin, navigate to:

My Environments > [Your Environment] > Settings > Connectors

![screenshot-full](ch01.png)

Select the **Connectors** tab.

![screenshot-full](ch02.png)

Here, you will see an overview of the installed connectors.

![screenshot-full](ch03.png)

## Types of Connectors

### Built-in

**CHILI publish** develops and supports built-in connectors and the associated services.

For example, GraFx Studio connects to [GraFx Media](/GraFx-Media/) through the **GraFx Media connector**, utilizing the same framework as other media connectors.

### Built by CHILI publish

To facilitate connections to external services, CHILI publish develops connectors for specific applications.

For example, the Media Connector for **Acquia DAM** is built and supported by CHILI publish.

Support for these connectors encompasses their internal workings, including API calls made to external systems. However, issues related to availability, configuration, or API problems on the media provider's side are covered by the third-party application.

Our Support team assists in identifying the origin of such issues.

### Built by Third Party, Approved by CHILI publish

Our open connector framework encourages developers to [build connectors](/GraFx-Developers/connectors/connectors-introduction/) for their unique use cases. If a media provider develops a connector, it can be offered in our Connector Hub.

Support for these connectors is provided by the developer.

### Custom (Private) Connectors

In cases where a built-in or readily available connector does not meet specific needs, we encourage you to [build custom connectors](/GraFx-Developers/connectors/connectors-introduction/). These connectors can be tailored for private use.

Building a private connector allows integration with custom media providers and customization to meet specific requirements.

### Default Connectors

Each type of connector has a designated **default** connector, and there can only be one default connector per type. The default connector is the one that is automatically used in the Template Designer (TD) Workspace unless otherwise specified.

For media connectors, **GraFx Media** is the default connector. This means that whenever you work in the TD Workspace and access media assets, the GraFx Media connector is used unless you configure another connector as the default.

You can change the default connector by selecting a different one in the **Configuration** tab. However, only one default connector can be active per connector type (e.g., media or data).