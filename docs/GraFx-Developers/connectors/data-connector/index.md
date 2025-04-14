# Mockaroo Connector Development Guide

This document outlines a step-by-step tutorial for creating a data connector in GraFx Studio that pulls random data from [Mockaroo](https://www.mockaroo.com/) and supports filtering via a search query. The guide is organized into several sections that cover the prerequisites, project structure, detailed explanations for each file, instructions for building and testing the connector, publishing guidelines, and finally, a conclusion.

Please note that the code provided here serves as an example tutorial. When building your own data connector, you would follow a similar structure, substituting the sample logic with your custom implementation as needed.

## Section 1: Requirements

- **Node.js & npm:** Ensure that you have [Node.js](https://nodejs.org/) installed.
- **GraFx Studio Connector CLI:** Use this command-line tool to generate, test, and deploy your connectors.
- **Basic Knowledge of TypeScript/JavaScript:** The code examples in this guide include comprehensive comments to assist beginners.

## Section 2: Project Organization

Create a new directory named `mockaroo-connector` and include the following files:

```
mockaroo-connector/
├── tsconfig.json
├── readme.md
├── package.json
├── connector.ts
└── test.ts
```

Each of these files has a unique role in the project. The sections below provide details about the content and purpose of each file.


## Section 3: File Descriptions and Explanations

### 3.1 tsconfig.json

This file configures the TypeScript compiler. It enables strict type-checking, leverages the ES2020 standard, and directs the compiled JavaScript to the `out` directory.

```json
{
  "compilerOptions": {
    "strict": true,
    "lib": [
      "ES2020"
    ],
    "noEmitHelpers": true,
    "module": "ES2020",
    "outDir": "out",
    "target": "ES2020",
    "moduleResolution": "Node",
    "preserveConstEnums": false,
    "esModuleInterop": false,
    "removeComments": true,
    "declaration": false
  },
  "include": [
    "connector.ts"
  ],
  "exclude": [
    "node_modules",
    "out"
  ]
}
```

**Explanation:**  
- **`strict`:** Activates strict type-checking.  
- **`lib`:** Specifies the use of the ES2020 library.  
- **`module` & `target`:** Set to ES2020 to utilize modern JavaScript features.  
- **`outDir`:** All compiled code is placed in the `out` folder.  
- **`include` and `exclude`:** Determine which files are compiled.  

### 3.2 readme.md

The README file offers an overview of the connector, instructions on how to publish it, and details on the necessary API parameters.

```markdown
# Mockaroo Connector

This connector retrieves random data from [Mockaroo](https://www.mockaroo.com/), making it ideal for testing and demonstration purposes in GraFx Studio.

## Publish

To deploy your connector, use the following command:

bash
connector-cli publish \
    -e {ENVIRONMENT} \
    -b https://{ENVIRONMENT}.chili-publish.online/grafx \
    --connectorId={CONNECTOR_ID}

## API Configuration

The connector requires these parameters:
- **apiKey:** Your unique Mockaroo API key.
- **count:** (Optional) The number of records to generate (defaults to 10).
- **schema:** (Optional) A JSON schema for data generation.
- **search:** (Optional) A search keyword to filter the results.

For further details, please refer to the [Mockaroo API documentation](https://www.mockaroo.com/api/docs).

## How to Use

After publishing, configure the connector in GraFx Studio by supplying the necessary parameters. The connector will filter data by the provided search query if one is entered.

```

**Explanation:**  
- The **Publish** section outlines the deployment command.  
- **API Configuration** lists the parameters that need to be supplied.  
- **How to Use** explains the operational aspect once the connector is active.  

### 3.3 package.json

This file provides metadata for the connector and lists its configuration options, dependencies, and scripts. It mirrors the structure used in the Google Sheets connector but is tailored for the Mockaroo integration.

```json
{
  "name": "mockaroo-connector",
  "description": "Connect to Mockaroo to generate random data for testing and demo purposes.",
  "version": "1.1.0",
  "author": {
    "name": "CHILI publish",
    "email": "info@chili-publish.com",
    "url": "https://github.com/chili-publish"
  },
  "config": {
    "connectorName": "Mockaroo",
    "type": "data",
    "iconUrl": "https://www.mockaroo.com/favicon.ico",
    "options": {
      "apiKey": {
        "type": "text",
        "required": true,
        "ui": {
          "label": "API Key",
          "description": "Your Mockaroo API key."
        }
      },
      "count": {
        "type": "number",
        "required": false,
        "default": 10,
        "ui": {
          "label": "Record Count",
          "description": "Number of records to generate."
        }
      },
      "schema": {
        "type": "text",
        "required": false,
        "ui": {
          "label": "Schema Definition",
          "description": "Optional JSON schema for data generation."
        }
      },
      "search": {
        "type": "text",
        "required": false,
        "ui": {
          "label": "Search Term",
          "description": "Optional search query to filter the results."
        }
      }
    },
    "mappings": {}
  },
  "license": "MIT",
  "main": "out/connector.js",
  "dependencies": {
    "typescript": "^5.2.2",
    "@chili-publish/studio-connectors": "^1.17.1",
    "axios": "^1.4.0"
  },
  "scripts": {
    "build": "yarn connector-cli build",
    "test": "yarn connector-cli test -t tests.json && yarn connector-cli stress"
  },
  "devDependencies": {
    "@chili-publish/connector-cli": "^1.9.0"
  }
}
```

**Explanation:**  
- **Metadata:** Defines the connector's name, version, and description.  
- **Configuration:** Details the options used in GraFx Studio such as `apiKey`, `count`, `schema`, and `search`.  
- **Dependencies and Scripts:** List libraries and commands required to build and test the project.  


### 3.4 connector.ts

This file includes the main logic for the connector. It uses axios to perform an HTTP GET request to the Mockaroo API and retrieve random data. If a search term is provided, it filters the data by checking if any string field in the records contains that term (ignoring case).

```typescript
// connector.ts
import axios from 'axios';
import { ConnectorContext } from '@chili-publish/studio-connectors';

/**
 * Primary handler function for the Mockaroo Connector with optional search filtering.
 *
 * Expected parameters:
 * - apiKey: string       // Your Mockaroo API key.
 * - count: number        // Number of records to generate (default: 10).
 * - schema?: string      // (Optional) JSON schema for generating data.
 * - search?: string      // (Optional) A search term to filter records.
 *
 * @param parameters Object containing the above properties.
 * @param context Connector context from GraFx Studio.
 * @returns An object with a status and the (optionally filtered) data.
 */
export async function handler(parameters: any, context: ConnectorContext) {
  const { apiKey, count = 10, schema, search } = parameters;

  if (!apiKey) {
    throw new Error("Missing required parameter: 'apiKey'");
  }

  const baseUrl = "https://api.mockaroo.com/api/generate.json";
  const queryParams = new URLSearchParams({
    key: apiKey,
    count: count.toString()
  });
  
  if (schema) {
    queryParams.append('schema', schema);
  }

  const url = `${baseUrl}?${queryParams.toString()}`;

  try {
    const response = await axios.get(url);
    let data = response.data;

    if (search && typeof search === 'string') {
      const searchQuery = search.toLowerCase();
      data = data.filter((record: any) => {
        return Object.values(record)
          .filter(value => typeof value === 'string')
          .some((value: string) => value.toLowerCase().includes(searchQuery));
      });
    }
    
    return {
      status: 'success',
      data
    };
  } catch (error: any) {
    console.error("Error fetching data from Mockaroo:", error.message);
    throw new Error(`Failed to fetch data from Mockaroo: ${error.message}`);
  }
}
```

**Explanation:**  
- The function extracts parameters (`apiKey`, `count`, `schema`, `search`) and ensures the API key is provided.  
- It constructs a URL for the API request using the provided parameters.  
- Data is fetched and then filtered if a search term is provided.  
- The function returns the final data along with a status indicator.  


### 3.5 test.ts

This test script simulates how GraFx Studio would invoke the connector. It supplies sample parameters (including a search term) to verify the connector’s functionality.

```typescript
// test.ts
import { handler } from './connector';

const testParameters = {
  apiKey: 'YOUR_MOCKAROO_API_KEY_HERE',  // Substitute with a valid Mockaroo API key.
  count: 10,                             // Request 10 records.
  // Optionally, add a JSON schema for data generation:
  // schema: '{"fields":[{"name":"first_name","type":"First Name"}]}',
  search: 'john'                         // Filter results to only include records with 'john'.
};

handler(testParameters, {} as any)
  .then(result => {
    console.log('Connector response:', result);
  })
  .catch(error => {
    console.error('Test Error:', error.message);
  });
```

**Explanation:**  
- The script imports the connector's handler.  
- It specifies test parameters including an API key, the number of records, and a search term.  
- The function is executed, and the output is logged to verify correct behavior.  


## Section 4: Building and Testing the Connector

1. **Install Dependencies:**  
   Open a terminal in the project directory and run:

   ```bash
   npm install
   ```
   or if using yarn:

   ```bash
   yarn install
   ```

2. **Compile the Project:**  
   Build the TypeScript project using the defined build script:

   ```bash
   yarn build
   ```

3. **Execute the Test Script:**  
   Run the test script to ensure everything functions as expected:

   ```bash
   node out/connector.js
   ```
   Alternatively, use ts-node:

   ```bash
   ts-node test.ts
   ```

Verify the output in the console to ensure the connector is operating correctly and that the search filtering functions as intended.


## Section 5: Publishing the Connector

Once testing is successful, publish your connector with the following command:

```bash
connector-cli publish \
    -e {ENVIRONMENT} \
    -b https://{ENVIRONMENT}.chili-publish.online/grafx \
    --connectorId={MOCKAROO_CONNECTOR_ID}
```

Replace `{ENVIRONMENT}` and `{MOCKAROO_CONNECTOR_ID}` with your specific environment details and connector ID.


## Section 6: Conclusion

This guide demonstrated how to build a GraFx Studio connector that:

- Retrieves random data from Mockaroo using an API key and an optional JSON schema.
- Implements additional functionality to filter the data based on a search term.
- Covers all necessary files with clear explanations:
  - `tsconfig.json`
  - `readme.md`
  - `package.json`
  - `connector.ts`
  - `test.ts`
- Provides instructions for building, testing, and publishing the connector.

By following this guide and using the provided code examples, you can successfully integrate Mockaroo-generated data into your projects for testing, demonstrations, or development purposes.

Happy coding!