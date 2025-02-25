# Publish my Connector

You've built a connector! Congratulations.

!!! info
    PS If you are looking for documentation on "How to start building a connector", you need to be [here](/GraFx-Developers/connectors/media-connector/build-a-simple-media-connector/) for Media Connectors.

## Requirements

### Open Source

To make your connector available on the CHILI GraFx [Connector Hub](/GraFx-Studio/guides/connector-hub/), it must be made open source.

Below, you'll see it needs to be committed to a public repository, which will make it Open Source.

### GitHub

The connector must be submitted to the GitHub Repo

### Documented

Your connector needs to be documented

- Base configuration
- Authentication setup
- How to use

## Publish to GitHub

- Create a [fork](https://github.com/chili-publish/studio-connector-framework) from the connector Framework Repository<br/>(if you haven't done that allready while building)
- Commit your fork
- Create a Pull Request

The Pull Request will trigger the CHILI publish staff to review your code and connector.

## Write Documentation

We covered how to start the deployment of a(ny) connector.
We expect you to write documentation on the configuration and use of your connector.

The CHILI GraFx Documentation GitHub repository is public ([see license](https://github.com/chili-publish/grafx-documentation/blob/main/LICENSE)).
Make a fork, add the documentation pages and make a pull request.

An example can be found on [this page](/GraFx-Studio/connectors/connector-grafx-media/).

## Review

After your pull request, our team will be notified, and the review process starts.

The team will review your submitted code and validate.

- Functional
- Code
- Security

## Publish

Once the code and functionality is validated, the CHILI publish team will publish your connector. (merge the pull request)
At the same time, the documentation pull request will also be published.

Once the code is merged, the Connector will be available in the Connector Hub

Your Connector is now available in the [Connector Hub](/GraFx-Studio/guides/connector-hub/)