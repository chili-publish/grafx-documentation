# Section 8: Authentication and Environment Configuration

The following section will guide you through the essential steps for setting up and managing authentication credentials and environment configurations for interacting with the GraFx API. By the end of this section, you will have accomplished the following objectives:

**Objectives:**

- **Understand Integration Roles**: Grasp the concept of integrations as special users within the GraFx ecosystem and their role in API authentication.
- **Secure Client Credentials**: Learn how to create an integration and obtain a client ID and secret, which are pivotal for API authentication.
**Environment Setup**: Configure your project's environment variables to securely store and manage your API credentials.
- **Token Generation**: Implement and utilize a function within `chili.js` to interact with the authentication endpoint for generating API tokens.
- **Token Management**: Develop a function in `utility.js` to manage the 'dangerous' token lifecycle, including generation, expiration check, and storage.

## 1. Integration Client Credentials

In order to interact with the GraFx API, you must create an integration which acts as a special user within your environment. An integration provides a client ID and secret used for generating authentication tokens.

Integrations play a crucial role by associating all user Projects under their credentials.

!!! warning
    
    It's important to note that Projects are bound to a single user; hence, they are not accessible by other GraFx users.

To create an integration, navigate to your preferred environment setup and ensure you assign all necessary permissions.

Learn how to create an integration by visiting the [integration guide](/GraFx-Developers/grafx-studio/integration-overview/04-managing-integrations-and-authentication/).

## 2. Configuration with Environment Variables

After obtaining your client ID and secret, proceed to configure your environment variables.

Create a `.env` File

=== "Linux/macOS"
    ```sh    
    touch .env
    ```
=== "Windows (PowerShell)"
    ```powershell
    ni .env
    ```

Edit the `.env` file to include your credentials, the base URL, and environment. Replace the placeholders with your actual values:

```
SERVER_ID = "GqPbzZD8u2OODsBMXFY2fmeJRsfYvX1J"
SERVER_SECRET = "o-bDz-U1vAFLWUUiZs4keQXMPCtyTgCa0Uzh-1ffkMM3o72j-Vgyw6Ekr4k8IlT9"
BASEURL = "https://example.chili-publish.online"
ENVIRONMENT = "example"
```

The base URL will typically follow this format:
- For production environments: `https://{environment}.chili-publish.online`
- For sandbox environments: `https://{environment}.chili-publish-sandbox.online`

!!! note
    The provided values are examples. Replace them with the credentials from your integration.

## 3. Install dotenv for Environment Variable Management

Use npm to install the dotenv package which allows your server to read the `.env` file:

```sh
npm install dotenv
```

In your `server.js`, add the following import statement:

```js
import 'dotenv/config'
```

## 4. Token Generation Functionality

Tokens are necessary for authenticated API interactions. To handle token generation, and all other CHILI related API calls, we use the `chili.js` module.

Create a `chili.js` file:

=== "Linux/macOS"
    ```sh    
    touch chili.js
    ```
=== "Windows (PowerShell)"
    ```powershell
    ni chili.js
    ```

We generate tokens using the authentication endpoint "https://integration-login.chiligrafx.com/oauth/token`. This endpoint takes our client ID and secret.

Insert the following function into `chili.js` to request tokens from the authentication endpoint:

```js
export async function getToken({ id, secret }) {
  try {
    const response = await fetch(
      "https://integration-login.chiligrafx.com/oauth/token",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          grant_type: "client_credentials",
          audience: "https://chiligrafx.com",
          client_id: id,
          client_secret: secret,
        }),
      },
    );

    // Check if the status is not 200 (OK), and if so, throw an error
    if (!response.ok) {
      const errorBody = await response.text(); // or response.json() if the server sends JSON error details
      throw new Error(
        `Server responded with status ${response.status}: ${errorBody}`,
      );
    }

    const data = await response.json();
    console.log(data);
    return data; // Return the data for further processing
  } catch (error) {
    console.error("Error fetching auth token:", error);
    throw error; // Re-throw the error to be handled by the caller
  }
}
```

This is generic code that will allow us to generate a token, but note that we haven't utilized the environment variables here to. The reason is because we will eventuall have two tokens:

- One for the server, which we will call "dangerous" in our code base because it has all the permissions
- One for our frontend, which we will call "readonly" in our code base because it has only readonly permissions


## 5. Function For Getting Our Danergous Token

Within `utility.js`, we will use the `getToken` function from `chili.js` to implement token generation and handling logic.

Firstly, import `getToken` at the beginning of `utility.js`

```js
import {getToken} from "./chili.js"; 
```

Then, define the `getDangerousToken` function:

```js
export async function getDangerousToken(db) {
  const {readonly, dangerous} = db.getTokens();

  const now = new Date();

  if (now.getTime() > dangerous.expires) {
    const {access_token, expires_in} = await getToken({id:process.env["SERVER_ID"], secret:process.env["SERVER_SECRET"]});

    db.setDangerousToken(access_token,expires_in);

    return access_token;
  }

  return dangerous.value;
}
```

This code does three things:

- It looks first for a token in our database and checks if it has expired
- If a token has expired, it generates a new one with `getToken`
- It updates the database with this new token and returns the token value


!!! danger

    Once issued, tokens cannot be invalidated and will have their permissions until they expire. Always handle the 'dangerous' token with extreme caution.

!!! note

    The authentication endpoint caches tokens. A new token is usually generated around 1 hour before the current token expires.

With our ability to create a "dangerous" token, we are ready to update `/template/:id` path to both get the template name and check it exists.


