# Versioning your integration

Welcome to the versioning strategy documentation for GraFx Studio. This guide will help you understand how to pin your environment to a specific version of GraFx Studio and explain our versioning strategy.

## Why Versioning Matters

Versioning allows you to control when and how you update your integration with GraFx Studio. This ensures stability and compatibility while allowing you to take advantage of the latest features and fixes at your own pace.

## How to Pin Your Environment Version

1. **Navigate to Settings**: Go to the settings of the environment you want to pin.
2. **Locate Version Settings**: In the general settings, find the pencil icon underneath "GraFx Studio version." By default, it is set to "latest" to always use the latest version. Click the pencil icon.
3. **Select Version**: In the modal that appears, you can select a specific version or choose "latest" if you want to always use the most recent version.

## How Does Versioning Work?

Our versioning strategy follows the common Semantic Versioning (SemVer) approach. If you are not familiar with SemVer, you can find detailed documentation [here](https://semver.org/).

### Key Points

- **Minor Version Importance**: When you select a specific version, the minor version is the most significant. This is because we align our versions with the Studio SDK, Template Designer Workspace, and End User workspace.

- **Patch Versions**: While patch versions are shown, they have minimal relevance for integrators. We automatically apply patches to our most recent version, so it's best to use the latest version of a certain minor release for your integration.

For example, the Studio UI can be accessed via a URL like this:
[https://studio-cdn.chiligrafx.com/studio-ui/1.27/latest/es-module/bundle.js](https://studio-cdn.chiligrafx.com/studio-ui/1.27/latest/es-module/bundle.js).

## Things to Take into Consideration

- **Document Compatibility**: It is not possible to open documents created with a newer version inside a session of an older version.

- **Patch Updates**: We only apply patch updates to the latest release number. If there are issues in a version that already has a successor, we will not fix them. You will need to update your integration to stay current with the latest features and fixes.

- **Grace Period**: We allow a grace period of one year, so your version can stay up to one year behind. However, we highly recommend staying as close as possible to the latest released version to benefit from the latest features and fixes.

## Best Practices

1. **Stay Updated**: Regularly check for updates and plan your integration updates accordingly.

2. **Test Thoroughly**: Before deploying a new version in your production environment, test it thoroughly in a sandbox or staging environment to ensure compatibility and stability.

3. **Monitor Deprecations**: Keep an eye on deprecation notices and plan to update your integration before deprecated versions are removed.
