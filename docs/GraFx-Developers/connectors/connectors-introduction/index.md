# Connectors Introduction

Connectors are a flexible framework that seamlessly integrates GraFx Studio capabilities with third-party systems, enabling efficient workflow automation and data exchange. Currently, the data model focuses on importing external data into GraFx Studio.

This comprehensive guide is designed for developers interested in building their own Connectors, providing essential information and best practices.

## Prerequisites for Building a Connector

To successfully create a Connector, you should have:

- Proficiency in modern JavaScript and familiarity with TypeScript
- Node.js or Bun.js installed on your development environment
- [Connector CLI](https://github.com/chili-publish/studio-connector-framework/tree/main/src/connector-cli) tool installed
- An Environment Admin user account with a Template Designer license

## Why Build a Connector?

Connectors are invaluable for organizations looking to leverage GraFx Studio while seamlessly integrating data from their existing systems. By building a Connector, you create a bridge between GraFx Studio and various external services, enhancing overall functionality and user experience.

### GraFx Studio and Connectors

GraFx Studio offers an in-browser document editor, and Connectors allow users to effortlessly import information from external systems. This integration enables real-time template modifications during editing or output generation. For example, users can:

- Pull images from a Digital Asset Management (DAM) system
- Import pricing information from a Product Information Management (PIM) platform
- Retrieve contact details from a Customer Relationship Management (CRM) tool

### Ideal Services for Connectors

The following types of services are particularly well-suited for Connector integration:

- Digital Asset Management (DAM) systems
- Product Information Management (PIM) platforms
- Content Management Systems (CMS)
- Customer Relationship Management (CRM) tools

## Types of Connectors

GraFx Studio currently supports two types of Connectors:

1. **Media Connectors** (Experimental): 

   - Purpose: Import images into documents and update variables with metadata
   - Status: Currently available as an experimental feature

2. **Data Connectors** (In Development):

   - Purpose: Import data to update document variables
   - Status: Currently in development, expected release in 2025

## Getting Started

If you're interested in building a Connector:

- For Media Connectors, please refer to our [Media Connector Introduction](../media-connector/media-connector-introduction/) guide for detailed instructions and best practices.
- For Data Connectors, please check back in 2025 for updated information and documentation.

### Common Questions

#### Q: Can Connectors be used to export data from GraFx Studio to external systems?
A: Currently, Connectors are designed for importing data into GraFx Studio. The ability to export data is not available at this time.

#### Q: How do I publish my Connector?
A: At present, Connectors must be shared via third-party means and published using our CLI tool. We are developing a Connector Hub where approved Connectors will be available in the future.
