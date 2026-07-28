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

## Debug a connector

The `debug` command starts a local debug server with a browser-based debugger, where you can invoke your connector's methods and inspect what they return — without publishing anything to an environment first.

```bash
connector-cli debug -p 3300
```

Open the reported URL in your browser, fill in the parameters for the method you want to test, and invoke it.

### Watch mode

Watch mode is enabled by default: the CLI recompiles `connector.ts` whenever you save it and reloads the browser tab, so your changes are immediately testable. To keep a fixed build for the duration of a session, disable it:

```bash
connector-cli debug --no-watch
```

### Execution metrics

Every method invocation is reported in an **Execution metrics** panel next to the output. It shows whether the call succeeded or failed, how long it took, and a record of each outgoing `fetch` request with its URL and duration. Methods that made no external calls are reported as such — useful for confirming that a caching path is doing its job.

The result itself is rendered as formatted JSON, with errors styled differently from successful responses, and can be copied to the clipboard.

### Runtime helpers

The debugger provides these globals from the connector runtime, so code that depends on them behaves the same locally as it does once published:

- `ConnectorHttpError` — for throwing HTTP errors from your connector
- `sleep(ms)` — pauses execution for the given number of milliseconds; useful when polling an external job or backing off after a rate-limit response

!!! note "Requires Connector CLI 1.12.1 or later"

    `sleep(ms)` in the debugger and the execution metrics panel were introduced in Connector CLI 1.12.1. Watch mode is also on by default from that version onwards.

## Connectors in the platform UI

Connectors deployed via Connector CLI appear in the environment's Connectors settings page in a disabled state. The availability toggle is visible (showing the current state) but no edit actions are available. Hovering over the row shows a tooltip explaining that the connector must be managed via Connector CLI.

## Github

For more information on the Connector Framework and CLI, see the [public repository](https://github.com/chili-publish/studio-connector-framework)