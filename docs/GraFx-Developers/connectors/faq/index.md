## Using of 3rd party package

**Question:** "I want to add my `superlibrary` to the project dependencies and use it in my connector code, but seems it doesn't work as expected".

**Answer:** Due to the limitation of our `build` command that doesn't support bundling,  everything that you refer as an external dependency (except types) will be treated as external dependencies and not bundled in produced JS file, means not working in runtime. Following this approach allows us to keep connector's code small that leads to lightning-fast initialization and use.

## HTTP request

**Question:** "I want to make HTTP call in my connector. I've tried to use `window.fetch` API and 3rd party packages like `axios` but it doesn't work"

**Answer:** The only way to make HTTP call to connector's services is by using `this.runtime.fetch(...)`. See [link](../media-connector/fundamentals/index.md#http-request) for details.

## Logs are not visible

**Question:** "I'm testing my connector in Debug applicatoin and using `console.log` to log some important infromation. Once deployed to environment and work in Studio, my logs are not visible anymore"

**Answer:** You should use specific `this.runtime.logError(...)` API for both Debug application and Studio integration. See [link](../media-connector/fundamentals/index.md#logging) for details.