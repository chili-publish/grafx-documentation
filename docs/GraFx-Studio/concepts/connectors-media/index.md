# Media Connectors

**Media Connectors** in GraFx Studio enable the integration of external media providers. These connectors offer access to a range of systems, including DAM (Digital Asset Management) platforms, as well as dynamic asset providers such as generative AI for images, real-time map generators, and dynamic chart generators. By leveraging Media Connectors, users can effectively utilize a diverse array of media assets directly within GraFx Studio.

![ui](connector2.png)

## Support

CHILI publish categorizes CHILI GraFx Connectors into 2 categories.

### Built-in

GraFx Studio connects to GraFx Media through the GraFx Media connector, utilizing the same framework as other media connectors. CHILI publish assumes full responsibility for the development and support of the GraFx Media connector and the associated media service, as all elements were built in-house.

### Built by CHILI publish

To facilitate connections to external services, CHILI publish develops Media Connectors for specific applications. For instance, the Media Connector for Acquia DAM is built and supported by CHILI publish. Support for these connectors encompasses their internal workings, including API calls made to external systems. However, issues related to availability, configuration, or API problems on the media provider's side are not covered under support. Our Customer Support team assists in identifying the origin of such issues.

An example: **The Media Connector for Acquia DAM**

### Built by third parties

Our open connector framework encourages developers to [build connectors](/GraFx-Developers/connectors/build-media-connector/) for their unique use cases. If a media provider develops a connector, such as for a generative AI application, it can be offered in our marketplace. Support for these connectors is provided by the developer.

### Custom (private) Connectors

In cases where a built-in or readily available connector is unavailable for specific needs, we encourage you to [build custom connectors](/GraFx-Developers/connectors/build-media-connector/). These connectors can be tailored for private use or offered in the marketplace for broader application. Building a private connector allows integration with custom media providers and customization to meet specific requirements.