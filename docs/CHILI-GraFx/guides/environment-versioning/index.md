# How to Set a Version in CHILI GraFx

## Accessing Available Versions

To view and select from available SDK versions, use the following API endpoint:

GET /api/v1/environments/settings/available-sdk-versions

This request retrieves the list of available versions, structured as shown below:

    {
      "latest": {
        "sdkVersion": "1.17.1",
        "engineVersion": "2.0.0"
      },
      "1.17": {
        "sdkVersion": "1.17.1",
        "engineVersion": "2.0.0"
      }
    }

## Setting the SDK Version via API

To pin a specific SDK version to an environment, apply the following API call:

PATCH /api/v1/environments/{environmentId}/settings
    {
      "sdkVersion": "1.0.0"
    }

Ensure that the SDK version you wish to set is validated against the list of available versions to avoid errors.

## Setting the Version in the Platform UI

1. **Navigate to the Environment Settings Page:**
   - Go to the main dashboard of CHILI GraFx.
   - Click on "Environments" to list all available environments.
   - Select the environment you want to configure by clicking on it.

2. **Access Version Settings:**
   - In the environment's settings panel, locate the "Version Settings" section.
   - You will see an option labeled "GraFx Studio version." Click on this to open the version selection modal.

3. **Select the Desired Version:**
   - In the modal, you'll see a dropdown list with the option "Latest" followed by all available versions. "Latest" will display the actual version number beside it, e.g., "Latest (xx.xx.xx)".
   - Choose the version you need from the dropdown. If you select "Latest," the environment will always use the most recent version available.

4. **Confirm Changes:**
   - After selecting the desired version, confirm your choice to ensure that the environment will use the specified SDK version.

## Handling Documents Set to Future Versions

When a document is created or edited in a version of GraFx Studio that is later than the version set for the environment, users will encounter a warning. This warning will state:

    "This document was created with a newer version of GraFx Studio. Opening it can cause loss of data or can break the template."

In such cases, the document cannot be opened or edited until the environment's version is updated to match or exceed the document's version.

## Additional Guidelines and Tips

- **Do not downgrade the environment's version without considering the implications on existing projects.** Downgrading can lead to loss of functionality or data if the projects were created with features available only in newer versions.

- **Regularly check for version updates and end-of-support notifications.** Staying updated can help avoid sudden disruptions due to unsupported versions.

- **Use the "Latest" setting judiciously.** While setting the environment to use the latest version ensures access to new features and improvements, it might introduce changes that could affect ongoing projects.

- **Plan for version testing.** Before rolling out a new version in a production environment, use a sandbox or development environment to test the changes to ensure compatibility with existing projects.

## Conclusion

Setting a specific version in CHILI GraFx is facilitated by both the platform's user interface and API endpoints. This feature empowers users to proactively manage their environment setups, aligning with their project requirements and stability needs, while ensuring that all team members and projects operate under compatible and supported versions of the software.