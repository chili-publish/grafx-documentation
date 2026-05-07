# Prepare your Supabase project

This page walks through everything you need to do **on the Supabase side** before connecting the database to GraFx Studio. The exact steps depend on which [query mode](../#query-modes) you intend to use.

## Get your project URL and API keys

In your Supabase project, open **Project Settings → API**. You'll need two values:

- **Project URL** — for example `https://abcdefgh.supabase.co`. Used as the connector's `SUPABASE_URL` runtime option.
- **API Key** — either the **anon** key (public, RLS-protected) or the **service-role** key (full access, bypasses RLS). See [Choosing the right Supabase API key](../#choosing-the-right-supabase-api-key).

Keep both values handy — you'll paste them into the connector's **Configuration** and **Authentication** tabs in GraFx Studio.

## Set up your data

The connector reads data through Supabase's auto-generated REST API (PostgREST). What you expose to the connector depends on the [query mode](../#query-modes) you choose.

### For `rpc` mode — create a Postgres function

Create a Postgres function in the `public` schema. Two rules to follow:

1. **Mark the function `SECURITY INVOKER`** *(this is the default)*. The function then runs as the *caller* (the `anon` role for browser flows), so any Row Level Security policies on the underlying tables still apply. Avoid `SECURITY DEFINER` unless you've thought carefully about the consequences — it bypasses RLS entirely.
2. **Grant `EXECUTE`** to the role you'll use the connector with — usually `anon`.

Example: a function that returns the products of a specific campaign.

```sql
create or replace function public.get_campaign_products(campaign_slug text)
returns setof products
language sql
security invoker
as $$
  select p.*
  from products p
  join campaign_products cp on cp.product_id = p.id
  join campaigns c on c.id = cp.campaign_id
  where c.slug = campaign_slug;
$$;

grant execute on function public.get_campaign_products(text) to anon;
```

The connector will call this function with `POST /rest/v1/rpc/get_campaign_products` and a JSON body containing the arguments.

### For `view` mode — create a table or view with RLS

Create a table or view in the `public` schema, then enable Row Level Security and add a policy that allows reads.

```sql
-- Enable RLS on the table you want to expose
alter table public.products enable row level security;

-- Allow public to read all rows
create policy "public read products" on public.products
  for select to public using (true);
```

The expression `using (true)` is permissive — every row is readable. You can tighten it later (for example, `using (is_active = true)`) without changing the connector.

!!! warning "RLS without a SELECT policy = silent empty results"
    If you enable RLS but forget to add a SELECT policy that matches the role you're calling as, the connector will return zero rows for every request — with no error. Always verify with the `curl` check below before assuming the connector is broken.

## Verify your Supabase setup

Before bringing GraFx Studio into the picture, make sure the data is reachable through the REST API with your API key. This catches almost every "it doesn't work" problem at the source.

### For a table or view

```sh
# Replace <ref> with your project ref and <anon-key> with the public API key
curl "https://<ref>.supabase.co/rest/v1/products?limit=2" \
  -H "apikey: <anon-key>"
```

You should see a JSON array with one or two rows.

| You see… | What it means |
|---|---|
| A JSON array of rows | All good — the connector will work. |
| `[]` (empty array) | RLS is on but no policy matches your role. Add a SELECT policy. |
| `401 Unauthorized` | The API key is wrong or missing. |

### For an `rpc` function

```sh
curl "https://<ref>.supabase.co/rest/v1/rpc/get_campaign_products" \
  -H "apikey: <anon-key>" \
  -H "Content-Type: application/json" \
  -d '{"campaign_slug":"spring-fresh"}'
```

If `curl` returns rows, the connector will return rows. If it doesn't, fix the database side first — debugging from inside GraFx Studio is much harder than debugging with `curl`.

## Further reading

- [Supabase API documentation](https://supabase.com/docs/guides/api)
- [Supabase Row Level Security](https://supabase.com/docs/guides/auth/row-level-security)
- [PostgREST query syntax](https://postgrest.org/en/stable/api.html) — used internally for filters and sorting
