# Build a Simple Data Connector

This guide walks you through the process of creating a simple data connector using the Connector CLI tool. The connector will display mock user data from Mockaroo in the data selector of GraFx Studio Designer Workspace.

## Requirements

- Node.js or Bun.js
- [Connector CLI](/GraFx-Developers/connectors/connector-cli/) tool
- Environment Admin user with a Template Designer license applied
- Mockaroo account (free tier available)

## Prerequisites: Setting Up Mockaroo

Before we begin, you'll need to set up a Mockaroo account, create a schema, and then create a custom API endpoint:

1. Go to [Mockaroo](https://www.mockaroo.com/) and create a free account.
2. Once logged in, navigate to the **Schemas** section.
3. Click **Create New Schema** with following fields:

    - `id` (Type: Row Number)
    - `first_name` (Type: First Name)
    - `last_name` (Type: Last Name)
    - `email` (Type: Email Address)
    - `gender` (Type: Gender)
    - `ip_address` (Type: IP Address v4)

4. Save the schema with a name, for example, **Users**.
5. Next, navigate to the **APIs** section.
6. Click **Create a new Mock API** to create a new API endpoint.
7. Set the route (e.g., `/users.json`).
8. In the Handler script, reference your saved schema and set the number of records to generate dynamically:

       ```
       schema "Users"
       generate params['count']
       ```

    !!! note
        Schema should match the name from step 4, **Users** for example

9. Save the API. Note the full API URL, which will look like `https://my.api.mockaroo.com/users.json?key=YOUR_API_KEY`.
10. Save your API key from the API settings page - you'll need it for the connector implementation.

## Creating a New Connector Project

1. Execute the command to create a new connector project:

    ```bash
    connector-cli new --type=data
    ```

    and follow the prompts to configure the project settings.

2. Enter to the project directory:

    ```bash
    cd <projectName>
    ```

3. Install dependencies:

    === "NPM"

        ```bash
        npm install
        ```

    === "Bun"

        ```bash
        bun install
        ```

4. Open `connector.ts` as this is the main connector file we will be modifying.

## Modifying the getPage Method

Our goal is to display mock user data from Mockaroo in the data selector. The `getPage` method is utilized by the default Studio GUIs to retrieve a list of data items for display.

### Updating Capabilities

First, we need to modify the `getCapabilities()` method to inform the UI about our connector's supported capabilities:

```typescript
getCapabilities(): Data.DataConnectorCapabilities {
  return {
    filtering: false,
    sorting: false,
    model: false,
  };
}
```

### Implementing the getPage Method

Next, we'll modify the `getPage` method to perform the following tasks:

1. Fetch a list of mock users from Mockaroo according to provided `limit` and `continuationToken`
2. Transform the data to match the required format
3. Return the data within the expected `DataPage` type

We'll use the following endpoint to retrieve our mock data (replace `YOUR_API_KEY` with your actual key):

```
https://my.api.mockaroo.com/users.json?key=YOUR_API_KEY&count=${limit}
```

This endpoint returns `limit` number of mock users with the following structure:

```typescript
{
  "id": number;
  "first_name": string;
  "last_name": string;
  "email": string;
  "gender": string;
  "ip_address": string;
}
```

Now, let's update our `getPage` method to handle this data and return the expected `DataPage` type:

```typescript
async getPage(
  config: Data.PageConfig,
  context: Connector.Dictionary
): Promise<Data.DataPage> {
  // We use the limit from config to determine how many items to fetch
  const resp = await this.runtime.fetch(
    `https://my.api.mockaroo.com/users.json?key=YOUR_API_KEY&count=${config.limit}`,
    {
      method: 'GET',
    }
  );

  // Handle error case
  if (!resp.ok) {
    throw new ConnectorHttpError(
      resp.status,
      `[Mockaroo connector]: Failed to fetch data: ${resp.status}-${resp.statusText}`
    );
  }

  const data = JSON.parse(resp.text);

  // Transform the data to match our expected format
  const dataFormatted = data.map((d) => ({
    id: d.id.toString(),
    firstName: d.first_name,
    lastName: d.last_name,
    email: d.email,
    gender: d.gender,
    ipAddress: d.ip_address
  }));

  return {
    data: dataFormatted,
    continuationToken: null // Mockaroo doesn't support pagination in free tier
  };
}
```

!!! warning "API Key Usage"
    In this tutorial, we're using the API key directly in the code for simplicity. However, for production connectors, you should implement proper authorization following the [Authorization for Connectors](/GraFx-Developers/connectors/authorization-for-connectors/) documentation. This ensures secure handling of credentials and proper access control.

## Publishing the Connector

### Step 1: Logging In

Before publishing your connector, you need to log in to CHILI GraFx. Run the following command and follow the on-screen instructions:

```bash
connector-cli login
```

### Step 2: Publishing

After successfully logging in, you can publish your connector using the following command:

```bash
connector-cli publish \
        -e <environment-name> \
        -b <base-url> \
        -n <name> \
        --proxyOption.allowedDomains "my.api.mockaroo.com"
```

#### Command Arguments

- `-e <environment-name>`: The environment where you want to deploy your connector.
- `-b <base-url>`: The base URL for CHILI GraFx API. Use one of the following formats:
    - **Production** Environments: `https://{environment-name}.chili-publish.online/grafx`
    - **Sandbox** Environments: `https://{environment-name}.chili-publish-sandbox.online/grafx`
- `-n <name>`: The name of your connector as it will appear in the GraFx Studio.
- `--proxyOption.allowedDomains "my.api.mockaroo.com"`: Specifies allowed domains for all requests that we're making from the connector.

### Step 3: Enabling the connector

The connector published in the previous step is initially unavailable for use in GraFx Studio Designer Workspace. To activate it, access the connector's settings in the Platform for the desired environment and turn on the `Availability` switch next to the newly deployed connector.

### Step 4: Verifying

To verify that your connector has been available successfully:

1. Open GraFx Studio Designer Workspace.
2. Create or open an existing template.
3. Add text variables with same name as keys of the fileds we're returning from the connector. Assign them to text frames in your template
3. Open Data Source Panel and select your connector.
4. Go to "Run" mode

You should see the mock user data displayed in the template

## Conclusion

Congratulations! You've successfully built your first Data Connector for GraFx Studio. This connector allows you to integrate mock user data from Mockaroo into the GraFx Studio Designer Workspace.

### Key Accomplishments

In this tutorial, you've learned how to:

1. Set up a new data connector project
2. Implement the `getPage` method to fetch and display data
3. Publish and test your connector in the GraFx Studio

## Next Steps

1. Review the [Comprehensive Connector Documentation](/GraFx-Developers/connectors/connectors-introduction/) for in-depth information on connector functionality and best practices.
2. Implement proper authorization by following the [Authorization for Connectors](/GraFx-Developers/connectors/authorization-for-connectors/) documentation for production use.
