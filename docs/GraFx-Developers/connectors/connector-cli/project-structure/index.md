# Connector project structure

!!! note "Requires Connector CLI 1.13.0 or later"

    Support for multiple `*.ts` files in a connector project was added in Connector CLI 1.13.0.

## Layout

| Path | Role |
| ---- | ---- |
| `connector.ts` | **Required** entry point. Export your connector class as `default`. |
| Other local `.ts` files | Optional helpers, types, and utilities imported from `connector.ts` (or from each other). |
| `package.json` | Connector metadata (`config`), dependencies, and scripts. |
| `tsconfig.json` | TypeScript editor and typecheck settings for the connector project. |
| `tests.json` | Optional test suite for media connectors (`connector-cli test`). |

New projects from `connector-cli new` scaffold this layout. You can keep everything in `connector.ts`, or split helpers into local modules as the connector grows.
