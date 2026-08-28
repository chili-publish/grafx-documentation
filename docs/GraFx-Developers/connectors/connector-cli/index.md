# Connector CLI

The CLI (Command Line Interface) is part of the tooling we offer to get you up and running.

This will help you to instantiate, build, test and deploy your custom connector.

## Installation

The "-g" option will make sure the command line tool is available on a "global" level, meaning also outside of your directory. In case you want to work on several connectors, you can call the tool from any directory.

```bash
npm install -g @chili-publish/connector-cli
```

You can now execute the command (in the terminal, in any directory)

To understand what the CLI can do, you can now execute

```bash
connector-cli -h
```

This will give you an overview of the available commands

## Project structure

!!! note "Requires Connector CLI 1.13.0 or later"

    Support for multiple `*.ts` files in a connector project was added in Connector CLI 1.13.0.

Connector projects use `connector.ts` as the entry point and may include additional local `.ts` helper modules. The CLI bundles them into a single `out/connector.js`. See [Project structure](/GraFx-Developers/connectors/connector-cli/project-structure/) for the full layout.

When the CLI builds your project, only these imports are allowed:

1. **Relative / local project `.ts` files** — e.g. `./helpers`, `../utils/format`
2. **`@chili-publish/studio-connectors`** — types and interfaces for the connector runtime

Any other npm or third-party package is rejected at compile time.

## Build a connector

```bash
connector-cli build
```

Compiles the project to `out/connector.js`. On a one-shot build, a compile failure exits with an error.

### Watch mode

```bash
connector-cli build -w
```

Recompiles when any project `.ts` file changes. If a save introduces a compile error, the CLI logs the diagnostics and **keeps watching** — it does not exit.

## Debug a connector

The `debug` command starts a local debug server with a browser-based debugger, where you can invoke your connector's methods and inspect what they return — without publishing anything to an environment first.

```bash
connector-cli debug -p 3300
```

Open the reported URL in your browser, fill in the parameters for the method you want to test, and invoke it.

### Watch mode

The debug application always runs in watch mode: the CLI recompiles whenever you save any project `.ts` file and reloads the browser tab, so your changes are immediately testable. There is no flag to turn this off. Compile errors are logged in the terminal; the previous successful build remains loaded until the next successful recompile.

### Execution metrics

Every method invocation is reported in an **Execution metrics** panel next to the output. It shows whether the call succeeded or failed, how long it took, and a record of each outgoing `fetch` request with its URL and duration. Methods that made no external calls are reported as such — useful for confirming that a caching path is doing its job.

The result itself is rendered as formatted JSON, with errors styled differently from successful responses, and can be copied to the clipboard.

### Working with IDs

Methods that take an asset ID — such as `detail` or `download` — are usually tested by running `query` first and copying an ID out of the JSON result. Fields that expect an ID normalize what you paste, so surrounding quotes or braces are stripped instead of being passed through as part of the value.

### Runtime helpers

The debugger provides these globals from the connector runtime, so code that depends on them behaves the same locally as it does once published:

- `ConnectorHttpError` — for throwing HTTP errors from your connector
- `sleep(ms)` — pauses execution for the given number of milliseconds; useful when polling an external job or backing off after a rate-limit response

!!! note "Requires Connector CLI 1.12.1 or later"

    `sleep(ms)` in the debugger, the execution metrics panel, and ID normalization were introduced in Connector CLI 1.12.1. From that version onwards the debug application also always runs in watch mode.

## Connectors in the platform UI

Connectors deployed via Connector CLI appear in the environment's **Connectors** settings page in a disabled state. The availability toggle is visible (showing the current state) but no edit actions are available. Hovering over the row shows a tooltip explaining that the connector must be managed via Connector CLI.

## Github

For more information on the Connector Framework and CLI, see the [public repository](https://github.com/chili-publish/studio-connector-framework)
