# Generating A Token

To utilize the Environment API, you need an access token. Here's how to obtain one:

## 1. Create an Integration

Before you can generate a token, you must create an Integration. Check out our guide on [Manage Integrations](/CHILI-GraFx/guides/integrations/) to get started. 

## 2. Find Client ID and Secret

After setting up an Integration with the necessary permissions, navigate to the General tab. Here, you'll find your Client ID and Client Secret.

![img](img)

## 3. Request a Token
Use the Client ID and Client Secret to request a token. Make a POST request to:

```
https://integration-login.chiligrafx.com/oauth/token
```

Here are some examples for making this request:

=== "cURL"
    ``` SH
    curl -X POST "https://integration-login.chiligrafx.com/oauth/token" \
     -H "Content-Type: application/json" \
     -d '{
         "grant_type": "client_credentials",
         "audience": "https://chiligrafx.com",
         "client_id": "<YOUR CLIENT ID>",
         "client_secret": "<YOUR CLIENT SECRET>"
     }'
    ```
=== "Python"
    ```python
    import requests

    endpoint = 'https://integration-login.chiligrafx.com/oauth/token'
    client_id = '<YOUR CLIENT ID>'
    client_secret = '<YOUR CLIENT SECRET>'

    resp = requests.post(
        url=endpoint,
        headers={
            "content-type": "application/json"
        },
        json={
            "grant_type": "client_credentials",
            "audience": "https://chiligrafx.com",
            "client_id": client_id,
            "client_secret": client_secret,
        }
    )

    if resp.status_code == 200:
        print(resp.json()["access_token"])
    else:
        raise Exception(f"{resp.text}")
    ```
=== "Node v18+"
    ```javascript
    const client_id = '<YOUR CLIENT ID>'
    const client_secret = '<YOUR CLIENT SECRET>'

    fetch('https://integration-login.chiligrafx.com/oauth/token', {
    method: "POST",
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        'grant_type': 'client_credentials',
        'audience': 'https://chiligrafx.com',
        'client_id': client_id,
        'client_secret': client_id
    })
    })
    .then(response => response.json()
    .then(data => console.log(data)))
    ```
=== "Go"
    ```go
    package main

    import (
        "bytes"
        "encoding/json"
        "fmt"
        "net/http"
    )

    type AuthResponse struct {
        Token		string  `json:"access_token"`
        Expiration	int 	`json:"expires_in"`
        Type	    string  `json:"token_type"`
        Scope		string  `json:"scope"`
    }

    func main() {
        posturl := "https://integration-login.chiligrafx.com/oauth/token"

        body := []byte(`{
            "grant_type": "client_credentials",
            "audience": "https://chiligrafx.com",
            "client_id": "<YOUR CLIENT ID>",
            "client_secret": "<YOUR CLIENT SECRET>"
        }`)

        r, err := http.NewRequest("POST", posturl, bytes.NewBuffer(body))
        if err != nil {
            panic(err)
        }

        r.Header.Add("Content-Type", "application/json")

        client := &http.Client{}
        res, err := client.Do(r)
        if err != nil {
            panic(err)
        }

        defer res.Body.Close()

        response := &AuthResponse{}
        derr := json.NewDecoder(res.Body).Decode(response)
        if derr != nil {
            panic(derr)
        }

        if res.StatusCode != 200 {
            panic(res.Status)
        }

        fmt.Println("Token:", response.Token)
    }
    ```
=== "Java"
    ```Java
    // This expects a ResponseType class to be defined with the response JSON properties
    // `access_token`, `expires_in`, `scope`, and `token_type`
    Map<String, Object> body = new HashMap<>();
    body.put("grant_type", "client_credentials");
    body.put("audience", "https://chiligrafx.com");
    body.put("client_id", client_id);
    body.put("client_secret", client_id);

    BodyBuilder requestBuilder;

    try {
      requestBuilder = RequestEntity.method(HttpMethod.POST, new URI("https://integration-login.chiligrafx.com/oauth/token"));
    } catch (URISyntaxException e) {
      log.error("Invalid URI: {}", url);
      log.error(e);
      throw new InvalidRequestException("Invalid URL");
    }

    requestBuilder.contentType(MediaType.APPLICATION_JSON);
    RequestEntity<Object> requestEntity = requestBuilder.body(body);

    ResponseEntity<ResponseType> responseEntity = restTemplate.exchange(
      requestEntity,
      new ParameterizedTypeReference<ResponseType>() {}
    );
    if (!responseEntity.getStatusCode().is2xxSuccessful()) {
      // The error handler built into the RestTemplate should handle 400 and 500 series errors.
      throw new RestClientException(
        "API returned " + responseEntity.getStatusCode()
      );
    }

    log.info("Got response: {}", responseEntity.getBody());
    ```

If all goes as intended, you will receive are response like below:

```json
{
    "access_token": "<YOUR TOKEN>",
    "token_type": "Bearer",
    "expires_in": 79045,
    "scope": "font:list font:read font:write media:list media:read media:write myproject:list myproject:read myproject:write output:animated output:static template_collection:list template_collection:read template_collection:write template:list template:read template:write"
}
```

Where:
- `access_token` is your token which you will use in further API calls.
- `token_type` will always be "Bearer".
- `expires_in` is be the time the token expires in seconds.
- `scope` is the permission that we set in the Permissions tab.

!!! note 

     Tokens are cached, so making the above API request again will not generate you a new token and return to you the original.

!!! warning

    Keep tokens confidential. Currently, leaked tokens cannot be deactivated or replaced. Avoid unintended sharing.
