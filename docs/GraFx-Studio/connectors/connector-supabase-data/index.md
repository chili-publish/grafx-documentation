# Supabase Data Connector

:fontawesome-regular-square: Built-in  
:fontawesome-regular-square: Built by CHILI publish  
:fontawesome-regular-square-check: Third Party

[See Connector types](/GraFx-Studio/concepts/connectors/#types-of-connectors)

The Supabase Data Connector lets you use any [Supabase](https://supabase.com/) project as a data source in GraFx Studio. Designers can bind template variables to live rows from your database — for example, looping over products in a campaign, pulling brand metadata, or rendering personalised cards.

The connector is **schema-agnostic**: it does not assume a specific data shape. Each template picks its own Supabase table, view, or function, and the connector adapts to whatever columns are returned.

## Query modes

The connector supports two ways to read data from Supabase. The choice is made per template binding.

- **`rpc` mode** *(default and recommended)* — calls a Postgres function you control. Use this when you want a stable, named, version-controlled API surface that's decoupled from your raw schema.
- **`view` mode** — reads a table or view directly. Useful for quick exploration or simple cases. View mode is gated by an admin-only setting and is **disabled by default** for safety.

If you're unsure, start with **rpc**. You can change the function later without re-publishing the connector.

## Installation

[See installation through Connector Hub](/GraFx-Studio/guides/connector-hub/)

You can deploy multiple instances of the connector, each pointing to a different Supabase project.

## Configuration

### Base Configuration

Once installed, navigate to the **Connector overview**, select your deployed **Supabase** connector, and start with **Configuration**.

- **Name**: Choose a name to distinguish your connector setup — for example, `Supabase – Production` or `Supabase – Staging`.
- **Description**: Give more context about what this connector does and which project it points to.
- **Version**: If available, choose the version you want to use.
- **Proxy settings**

```html
*.supabase.co
```

### Runtime options

The connector exposes two runtime options that an admin can set when publishing or editing the connector. Both are admin-editable in the **Configuration** tab.

- **`SUPABASE_URL`** *(required)*: the project URL, e.g. `https://abcdefgh.supabase.co`. You can find it in your Supabase project under **Project Settings → API**.
- **`ALLOW_TABLE_VIEW`** *(default: `false`)*: leave it `false` for environments that should only allow rpc mode. Set it to `true` when designers need to read tables and views directly. You can change this later without re-publishing the connector.

!!! warning "Pick the smallest blast radius"
    Keep `ALLOW_TABLE_VIEW` set to `false` in production environments. Anything sensitive should be exposed through a controlled rpc function — not directly from a table.

## Authentication

The connector uses **static key** authentication: a single Supabase API key sent on every request as the `apikey` header. Supabase reads the JWT inside that key and resolves the role automatically — no separate `Authorization: Bearer` header is needed.

You can configure **Server Authentication** and **Browser Authentication** separately or use the same key for both.

- **Server Authentication** *Always required* — defines how the CHILI GraFx Server talks to Supabase.
- **Browser Authentication** *Optional* — defines how the browser talks to Supabase to pull data into the editor.

### Choosing the right Supabase API key

Supabase issues two main keys. They have very different security profiles, so the choice matters.

| Key | When to use it | Notes |
|---|---|---|
| `anon` (public) | Browser editing flows; most server flows that should respect Row Level Security | Public-by-design. Protected by RLS policies on your tables. |
| `service_role` | Server-only flows that need full access | **Bypasses Row Level Security.** Never expose it to the browser. |

For most setups, use the **anon key** in both slots. It is meant to be public-facing and is protected by your RLS policies.

Use the **service-role key** only if you need server-side rendering to bypass RLS — and only for the **Server Authentication** slot, never the Browser slot.

You can find both keys in your Supabase project under **Project Settings → API**. See [Get your project URL and API keys](supabase-setup/#get-your-project-url-and-api-keys) for the full setup.

### Set the key

In the **Authentication** tab, fill in the static-key fields:

- **Key**: `apikey`
- **Value**: paste your Supabase API key.

Repeat this for **Browser** and **Server** if you want different keys per slot.

!!! info "Privacy"
    Once saved, the key value is hidden when you reopen the settings. If you need to update it, re-enter the full value before saving.

## Try it out

Before binding the connector to a template, verify that it can read from your Supabase project. The fastest way is to check directly with `curl` — that confirms your project URL, API key, and database setup are all working independently of CHILI Studio.

See [Verify your Supabase setup](supabase-setup/#verify-your-supabase-setup) for the exact commands.

Once that works, [add the connector to a Smart Template](in-smart-template/) and preview a few records in **Run Mode**.
