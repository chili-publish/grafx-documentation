<h1 id="chili-grafx">CHILI GraFx v1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

# Authentication

- HTTP Authentication, scheme: Bearer Enter a bearer token (JWT):

<h1 id="chili-grafx-environments">Environments</h1>

## get  api v1 environment {id}

`GET /api/v1/environment/{id}`

*Gets environment information.*

<h3 id="get--api-v1-environment-{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|Environment Id.|

> Example responses

> 200 Response

```json
{
  "id": 494,
  "name": "cp-000-001",
  "type": "development",
  "usedStorage": 2048,
  "usedStorageDetail": {
    "assets": 1280,
    "documents": 3560,
    "fonts": 1280,
    "cache": 2560,
    "backup": 5120,
    "other": 10240
  },
  "tenantName": "Tenant",
  "region": "westeurope",
  "renders": 2500
}
```

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401
}
```

> 403 Response

```json
{
  "type": "https://httpstatuses.io/403",
  "title": "Forbidden",
  "status": 403
}
```

> 404 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404
}
```

<h3 id="get--api-v1-environment-{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns environment information.|[EnvironmentModel](#schemaenvironmentmodel)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If environment with such Id is not found.|[ProblemDetails](#schemaproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {id} renders

`GET /api/v1/environment/{id}/renders`

*Get environment renders information.*

<h3 id="get--api-v1-environment-{id}-renders-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|Environment Id.|
|groupBy|query|string|true|Groups render information by: `year`, `month`.|

> Example responses

> 200 Response

```json
[
  {
    "date": "2021-11-01T00:00:00",
    "totalRenders": 2048,
    "renderDetail": [
      {
        "name": "Pdf",
        "renders": 1024
      }
    ]
  }
]
```

> 400 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "Bad Request",
  "status": 400
}
```

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401
}
```

> 403 Response

```json
{
  "type": "https://httpstatuses.io/403",
  "title": "Forbidden",
  "status": 403
}
```

> 404 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404
}
```

<h3 id="get--api-v1-environment-{id}-renders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns environment renders information.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If groupBy is missing or invalid.|[ProblemDetails](#schemaproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If environment with such Id is not found.|[ProblemDetails](#schemaproblemdetails)|

<h3 id="get--api-v1-environment-{id}-renders-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[EnvironmentRenderModel](#schemaenvironmentrendermodel)]|false|none|[Response model with environment render information.]|
|» date|string(date-time)|true|none|Render date.|
|» totalRenders|integer(int64)|true|none|Total renders count in bytes.|
|» renderDetail|[[EnvironmentRenderDetail](#schemaenvironmentrenderdetail)]|true|none|Render details.|
|»» name|string|true|none|Render name (`Pdf`, `Image`, etc).|
|»» renders|integer(int64)|true|none|Renders count.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-info">Info</h1>

## get  api v1 info

`GET /api/v1/info`

*Gets information about API.*

> Example responses

> 200 Response

```json
{
  "data": {
    "serverVersion": "1.0.0"
  }
}
```

<h3 id="get--api-v1-info-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns information about API.|[InfoResponse](#schemainforesponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api ping

`GET /api/ping`

*Checks server availability.*

<h3 id="get--api-ping-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|If server is available.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-roles">Roles</h1>

## get  api v1 roles

`GET /api/v1/roles`

*Gets supported user roles in GraFx.*

> Example responses

> 200 Response

```json
[
  "string"
]
```

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401
}
```

<h3 id="get--api-v1-roles-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of supported user roles as strings array (e.g. ["SA","FA"]).|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|

<h3 id="get--api-v1-roles-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-subscriptions">Subscriptions</h1>

## get  api v1 subscriptions

`GET /api/v1/subscriptions`

*Gets all existing subscriptions.*

> Example responses

> 200 Response

```json
[
  {
    "id": 44,
    "name": "CHILI - OnlineTrial",
    "isActive": true
  }
]
```

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401
}
```

> 403 Response

```json
{
  "type": "https://httpstatuses.io/403",
  "title": "Forbidden",
  "status": 403
}
```

<h3 id="get--api-v1-subscriptions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of subscriptions.|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|

<h3 id="get--api-v1-subscriptions-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[BasicSubscriptionModel](#schemabasicsubscriptionmodel)]|false|none|[Response model with subscription information.]|
|» id|integer(int32)|true|none|Subscription Id.|
|» name|string|true|none|Subscription name.|
|» isActive|boolean|true|none|`true` if subscription is still active.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 subscription {id}

`GET /api/v1/subscription/{id}`

*Gets detailed information about subscription.*

<h3 id="get--api-v1-subscription-{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|Subscription Id.|

> Example responses

> 200 Response

```json
{
  "id": 1,
  "name": "CHILI (Online)",
  "usedRenders": 1000,
  "maxRenders": 2500,
  "maxStorage": 250000000000,
  "storageUsed": 81959236,
  "environments": [
    {
      "id": 494,
      "name": "cp-eee-001",
      "region": "westeurope",
      "type": "development",
      "usedStorage": 1093314335,
      "backOfficeUri": "https://cp-000-000.chili-publish-sandbox.online/cp-000-000/interface.aspx"
    }
  ],
  "licenses": [
    {
      "id": "CPF-2022-0000001",
      "coresTotal": 16,
      "coresUsed": 2,
      "url": "https://chili-publish.com/Licenses/Details/00000000-0000-0000-0000-000000000000",
      "licenseType": "Production"
    }
  ],
  "startDate": "11/12/2022 12:15:32 AM",
  "endDate": "11/12/2023 12:15:32 PM",
  "subscriptionType": "OnPremises",
  "status": "Inactive",
  "clientName": "CHILI Group",
  "billingClientContact": "simple@example.com",
  "templateDesignerSeatsTotal": 6,
  "templateDesignerSeatsUsed": 4,
  "tenantInformation": {
    "sandboxEnvironmentsTotal": 4,
    "sandboxEnvironmentsUsed": 2,
    "productionEnvironmentsTotal": 4,
    "productionEnvironmentsUsed": 1
  }
}
```

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401
}
```

> 403 Response

```json
{
  "type": "https://httpstatuses.io/403",
  "title": "Forbidden",
  "status": 403
}
```

> 404 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404
}
```

<h3 id="get--api-v1-subscription-{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns subscription.|[SubscriptionModel](#schemasubscriptionmodel)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If subscription not found for the authenticated user.|[ProblemDetails](#schemaproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 subscription {subscriptionGuid} {environmentGuid}

`GET /api/v1/subscription/{subscriptionGuid}/{environmentGuid}`

*Checks if environment is under subscription.*

<h3 id="get--api-v1-subscription-{subscriptionguid}-{environmentguid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|subscriptionGuid|path|string|true|Subscription Id.|
|environmentGuid|path|string|true|Environment Id.|

> Example responses

> 200 Response

```json
true
```

> 400 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "Bad Request",
  "status": 400
}
```

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401
}
```

> 403 Response

```json
{
  "type": "https://httpstatuses.io/403",
  "title": "Forbidden",
  "status": 403
}
```

<h3 id="get--api-v1-subscription-{subscriptionguid}-{environmentguid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns `true` if environment is under subscription.|boolean|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If subscriptionGuid or environmentGuid is not a valid GUID.|[ProblemDetails](#schemaproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 subscription {id} renders

`GET /api/v1/subscription/{id}/renders`

*Gets environments render information included in subscription.*

All environments under that subscription are returned in the descending order based on renders.

<h3 id="get--api-v1-subscription-{id}-renders-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|Subscription Id.|
|groupBy|query|string|true|Groups render information by: `year`, `month`|
|top|query|integer(int32)|false|When top parameter is provided, the information for the `top` number of environments is returned and for|

#### Detailed descriptions

**top**: When top parameter is provided, the information for the `top` number of environments is returned and for
all the rest of existing environments in the subscription the renders are concatenated under "Others".

> Example responses

> 200 Response

```json
[
  {
    "date": "2021-11-01T00:00:00",
    "totalRenders": 4680,
    "environments": [
      {
        "name": "cp-itm-000",
        "renders": 4680
      }
    ]
  }
]
```

> 400 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "Bad Request",
  "status": 400
}
```

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401
}
```

> 403 Response

```json
{
  "type": "https://httpstatuses.io/403",
  "title": "Forbidden",
  "status": 403
}
```

> 404 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404
}
```

<h3 id="get--api-v1-subscription-{id}-renders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of environments render details.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If groupBy is missing or invalid.|[ProblemDetails](#schemaproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If subscription with this id is not found for the authenticated user.|[ProblemDetails](#schemaproblemdetails)|

<h3 id="get--api-v1-subscription-{id}-renders-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[SubscriptionRendersModel](#schemasubscriptionrendersmodel)]|false|none|[Response model with subscription render information.]|
|» date|string(date-time)|true|none|Renders of environments date.|
|» totalRenders|integer(int64)|true|none|Total count of renders for environments.|
|» environments|[[EnvironmentRenderInformation](#schemaenvironmentrenderinformation)]|true|none|Environment render details.|
|»» name|string¦null|false|none|Environment name.|
|»» renders|integer(int64)|true|none|Total count of render for environment.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 subscription {id} users

`GET /api/v1/subscription/{id}/users`

*Gets users that use the subscription.*

<h3 id="get--api-v1-subscription-{id}-users-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|Subscription Id.|

> Example responses

> 200 Response

```json
[
  {
    "id": "auth0|630f8c2b524936fea93c0e75",
    "email": "simple@example.com",
    "firstName": "John",
    "lastName": "Doe",
    "avatar": "https://www.chili-publish.com/",
    "lastSeen": 1668540708,
    "status": "Active"
  }
]
```

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401
}
```

> 403 Response

```json
{
  "type": "https://httpstatuses.io/403",
  "title": "Forbidden",
  "status": 403
}
```

> 404 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404
}
```

<h3 id="get--api-v1-subscription-{id}-users-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of user details.|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If subscription with this id is not found for the authenticated user.|[ProblemDetails](#schemaproblemdetails)|

<h3 id="get--api-v1-subscription-{id}-users-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[UserModel](#schemausermodel)]|false|none|[Response model with user information.]|
|» id|string¦null|false|none|User Id.|
|» email|string¦null|false|none|User email.|
|» firstName|string¦null|false|none|User first name.|
|» lastName|string¦null|false|none|User last name.|
|» avatar|string¦null|false|none|Link to avatar picture.|
|» lastSeen|integer(int64)¦null|false|none|Last login datetime in seconds (unit timestamp).|
|» status|string¦null|false|none|User activity status.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-users">Users</h1>

## post  api v1 users manage add

`POST /api/v1/users/manage/add`

*Adds new user in GraFx.*

> Body parameter

```json
{
  "email": "simple@example.com",
  "firstName": "John",
  "lastName": "Doe",
  "subscriptionIds": [
    "d28986ef-ad97-4172-92c9-59b768febd79",
    "9afe8a46-27f4-4c39-76b1-db89e8ad9daf"
  ],
  "customerGuid": "d28986ef-aa11-4372-92c9-59b768febd79"
}
```

<h3 id="post--api-v1-users-manage-add-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|signature|header|string|true|Signature used to verify that the request called by an authorized party.|
|body|body|[AddUserModel](#schemaaddusermodel)|true|none|

> Example responses

> 200 Response

```json
{
  "userId": "auth0|630f8c2b324946feb93c7e75"
}
```

> 400 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "Bad Request",
  "status": 400
}
```

> 409 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.8",
  "title": "Conflict",
  "status": 409
}
```

> 500 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.6.1",
  "title": "Internal Server Error",
  "status": 500
}
```

<h3 id="post--api-v1-users-manage-add-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns ID of successfully created user.|[CreateUserResultModel](#schemacreateuserresultmodel)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If one of the following params is missing: signature, email, firstName, lastName.|[ProblemDetails](#schemaproblemdetails)|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|If user with the same email already exists.|[ProblemDetails](#schemaproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|[ProblemDetails](#schemaproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## put  api v1 users {userId} manage update

`PUT /api/v1/users/{userId}/manage/update`

*Updates user's first name and last name in GraFx.*

> Body parameter

```json
{
  "firstName": "John",
  "lastName": "Doe"
}
```

<h3 id="put--api-v1-users-{userid}-manage-update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|userId|path|string|true|UserId in GraFx.|
|body|body|[UpdateUserModel](#schemaupdateusermodel)|true|none|

> Example responses

> 400 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "Bad Request",
  "status": 400
}
```

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": 401
}
```

> 403 Response

```json
{
  "type": "https://httpstatuses.io/403",
  "title": "Forbidden",
  "status": 403
}
```

> 404 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404
}
```

> 500 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.6.1",
  "title": "Internal Server Error",
  "status": 500
}
```

<h3 id="put--api-v1-users-{userid}-manage-update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|If user has been successfully updated.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If one of the following params is missing: firstName, lastName.|[ProblemDetails](#schemaproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If userId not found in GraFx.|[ProblemDetails](#schemaproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Server Error|[ProblemDetails](#schemaproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 users {userId} manage email-status

`GET /api/v1/users/{userId}/manage/email-status`

*Gets user email verification status.*

<h3 id="get--api-v1-users-{userid}-manage-email-status-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|userId|path|string|true|UserId in GraFx.|
|signature|header|string|true|Signature used to verify that the request called by an authorized party.|

> Example responses

> 200 Response

```json
{
  "isEmailVerified": true
}
```

> 400 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "Bad Request",
  "status": 400
}
```

> 404 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404
}
```

> 500 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.6.1",
  "title": "Internal Server Error",
  "status": 500
}
```

<h3 id="get--api-v1-users-{userid}-manage-email-status-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns user email verification status.|[UserEmailVerificationStatusModel](#schemauseremailverificationstatusmodel)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If one of the following params is missing: signature, userId.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If userId not found in GraFx.|[ProblemDetails](#schemaproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|If data cannot be retrieved due to internal failure.|[ProblemDetails](#schemaproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## put  api v1 users manage migrate

`PUT /api/v1/users/manage/migrate`

*Marks user as migrated to GraFx.*

> Body parameter

```json
{
  "userEmail": "simple@example.com"
}
```

<h3 id="put--api-v1-users-manage-migrate-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|signature|header|string|true|Signature used to verify that the request called by an authorized party.|
|body|body|[MarkUserMigratedModel](#schemamarkusermigratedmodel)|false|none|

> Example responses

> 400 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "Bad Request",
  "status": 400
}
```

> 404 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404
}
```

> 500 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.6.1",
  "title": "Internal Server Error",
  "status": 500
}
```

<h3 id="put--api-v1-users-manage-migrate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|If user successfully marked as migrated.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If one of the following params is missing: signature, userEmail.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If user with this userEmail is not found.|[ProblemDetails](#schemaproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|If user cannot be marked as migrated due to internal failure.|[ProblemDetails](#schemaproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post  api v1 users manage migrate subscriptions

`POST /api/v1/users/manage/migrate/subscriptions`

*Gets user accessible subscriptions.*

> Body parameter

```json
{
  "userEmail": "simple@example.com"
}
```

<h3 id="post--api-v1-users-manage-migrate-subscriptions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|signature|header|string|true|Signature used to verify that the request called by an authorized party.|
|body|body|[UserAccessibleSubscriptionsModel](#schemauseraccessiblesubscriptionsmodel)|false|none|

> Example responses

> 200 Response

```json
{
  "userEmail": "simple@example.com"
}
```

> 400 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "Bad Request",
  "status": 400
}
```

> 404 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404
}
```

> 500 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.6.1",
  "title": "Internal Server Error",
  "status": 500
}
```

<h3 id="post--api-v1-users-manage-migrate-subscriptions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns user accessible subscriptions.|[UserAccessibleSubscriptionsModel](#schemauseraccessiblesubscriptionsmodel)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If one of the following params is missing: signature, userEmail.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If user not found in MyCP.|[ProblemDetails](#schemaproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|If data cannot be retrieved due to internal failure.|[ProblemDetails](#schemaproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

# Schemas

<h2 id="tocS_AddUserModel">AddUserModel</h2>
<!-- backwards compatibility -->
<a id="schemaaddusermodel"></a>
<a id="schema_AddUserModel"></a>
<a id="tocSaddusermodel"></a>
<a id="tocsaddusermodel"></a>

```json
{
  "email": "simple@example.com",
  "firstName": "John",
  "lastName": "Doe",
  "subscriptionIds": [
    "d28986ef-ad97-4172-92c9-59b768febd79",
    "9afe8a46-27f4-4c39-76b1-db89e8ad9daf"
  ],
  "customerGuid": "d28986ef-aa11-4372-92c9-59b768febd79"
}

```

Request model that is used to add new user in GraFx.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string|true|none|User email which should be used in GraFx.|
|firstName|string|true|none|User first name.|
|lastName|string|true|none|User last name.|
|subscriptionIds|[string]¦null|false|none|Ids of existing user subscriptions.|
|customerGuid|string(uuid)¦null|false|none|The guid of the customer this user is linked to.|

<h2 id="tocS_BasicSubscriptionModel">BasicSubscriptionModel</h2>
<!-- backwards compatibility -->
<a id="schemabasicsubscriptionmodel"></a>
<a id="schema_BasicSubscriptionModel"></a>
<a id="tocSbasicsubscriptionmodel"></a>
<a id="tocsbasicsubscriptionmodel"></a>

```json
{
  "id": 44,
  "name": "CHILI - OnlineTrial",
  "isActive": true
}

```

Response model with subscription information.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|true|none|Subscription Id.|
|name|string|true|none|Subscription name.|
|isActive|boolean|true|none|`true` if subscription is still active.|

<h2 id="tocS_CreateUserResultModel">CreateUserResultModel</h2>
<!-- backwards compatibility -->
<a id="schemacreateuserresultmodel"></a>
<a id="schema_CreateUserResultModel"></a>
<a id="tocScreateuserresultmodel"></a>
<a id="tocscreateuserresultmodel"></a>

```json
{
  "userId": "auth0|630f8c2b324946feb93c7e75"
}

```

Request model that is used to return new user ID after creation in GraFx.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|userId|string|true|none|User ID which has been created in GraFx.|

<h2 id="tocS_EnvironmentModel">EnvironmentModel</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmentmodel"></a>
<a id="schema_EnvironmentModel"></a>
<a id="tocSenvironmentmodel"></a>
<a id="tocsenvironmentmodel"></a>

```json
{
  "id": 494,
  "name": "cp-000-001",
  "type": "development",
  "usedStorage": 2048,
  "usedStorageDetail": {
    "assets": 1280,
    "documents": 3560,
    "fonts": 1280,
    "cache": 2560,
    "backup": 5120,
    "other": 10240
  },
  "tenantName": "Tenant",
  "region": "westeurope",
  "renders": 2500
}

```

Response model with the information about environment used by user.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|true|none|Environment Id.|
|name|string¦null|false|none|Environment name.|
|type|[EnvironmentType](#schemaenvironmenttype)|true|none|Environment type.|
|usedStorage|integer(int64)|true|none|Total used storage in bytes.|
|usedStorageDetail|[EnvironmentStorageInformationModel](#schemaenvironmentstorageinformationmodel)|true|none|Response model with detailed information about environment storage use.|
|tenantName|string¦null|false|none|Tenant name.|
|region|string¦null|false|none|Region name.|
|renders|integer(int64)|true|none|Render count for environment.|

<h2 id="tocS_EnvironmentRenderDetail">EnvironmentRenderDetail</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmentrenderdetail"></a>
<a id="schema_EnvironmentRenderDetail"></a>
<a id="tocSenvironmentrenderdetail"></a>
<a id="tocsenvironmentrenderdetail"></a>

```json
{
  "name": "Pdf",
  "renders": 1024
}

```

Response model with environment render detail.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|Render name (`Pdf`, `Image`, etc).|
|renders|integer(int64)|true|none|Renders count.|

<h2 id="tocS_EnvironmentRenderInformation">EnvironmentRenderInformation</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmentrenderinformation"></a>
<a id="schema_EnvironmentRenderInformation"></a>
<a id="tocSenvironmentrenderinformation"></a>
<a id="tocsenvironmentrenderinformation"></a>

```json
{
  "name": "cp-itm-000",
  "renders": 4680
}

```

Response model with environment render details.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string¦null|false|none|Environment name.|
|renders|integer(int64)|true|none|Total count of render for environment.|

<h2 id="tocS_EnvironmentRenderModel">EnvironmentRenderModel</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmentrendermodel"></a>
<a id="schema_EnvironmentRenderModel"></a>
<a id="tocSenvironmentrendermodel"></a>
<a id="tocsenvironmentrendermodel"></a>

```json
{
  "date": "2021-11-01T00:00:00",
  "totalRenders": 2048,
  "renderDetail": [
    {
      "name": "Pdf",
      "renders": 1024
    }
  ]
}

```

Response model with environment render information.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date|string(date-time)|true|none|Render date.|
|totalRenders|integer(int64)|true|none|Total renders count in bytes.|
|renderDetail|[[EnvironmentRenderDetail](#schemaenvironmentrenderdetail)]|true|none|Render details.|

<h2 id="tocS_EnvironmentStorageInformationModel">EnvironmentStorageInformationModel</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmentstorageinformationmodel"></a>
<a id="schema_EnvironmentStorageInformationModel"></a>
<a id="tocSenvironmentstorageinformationmodel"></a>
<a id="tocsenvironmentstorageinformationmodel"></a>

```json
{
  "assets": 1280,
  "documents": 3560,
  "fonts": 1280,
  "cache": 2560,
  "backup": 5120,
  "other": 10240
}

```

Response model with detailed information about environment storage use.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assets|integer(int64)|true|none|Used asset storage in bytes.|
|documents|integer(int64)|true|none|Used documents storage in bytes.|
|fonts|integer(int64)|true|none|Used fonts storage in bytes.|
|cache|integer(int64)|true|none|Used cache storage in bytes.|
|backup|integer(int64)|true|none|Used backup storage in bytes.|
|other|integer(int64)|true|none|Used other storage in bytes.|

<h2 id="tocS_EnvironmentType">EnvironmentType</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmenttype"></a>
<a id="schema_EnvironmentType"></a>
<a id="tocSenvironmenttype"></a>
<a id="tocsenvironmenttype"></a>

```json
"development"

```

Environment type.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|Environment type.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|development|
|*anonymous*|sandbox|
|*anonymous*|production|

<h2 id="tocS_Info">Info</h2>
<!-- backwards compatibility -->
<a id="schemainfo"></a>
<a id="schema_Info"></a>
<a id="tocSinfo"></a>
<a id="tocsinfo"></a>

```json
{
  "serverVersion": "1.0.0"
}

```

Model used for providing technical information about API.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|serverVersion|string|true|none|Current version of API.|

<h2 id="tocS_InfoResponse">InfoResponse</h2>
<!-- backwards compatibility -->
<a id="schemainforesponse"></a>
<a id="schema_InfoResponse"></a>
<a id="tocSinforesponse"></a>
<a id="tocsinforesponse"></a>

```json
{
  "data": {
    "serverVersion": "1.0.0"
  }
}

```

Response model used for providing the information about API.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|data|[Info](#schemainfo)|true|none|Model used for providing technical information about API.|

<h2 id="tocS_LicenseType">LicenseType</h2>
<!-- backwards compatibility -->
<a id="schemalicensetype"></a>
<a id="schema_LicenseType"></a>
<a id="tocSlicensetype"></a>
<a id="tocslicensetype"></a>

```json
"Production"

```

License type.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|License type.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Production|
|*anonymous*|Failover|
|*anonymous*|Sandbox|

<h2 id="tocS_MarkUserMigratedModel">MarkUserMigratedModel</h2>
<!-- backwards compatibility -->
<a id="schemamarkusermigratedmodel"></a>
<a id="schema_MarkUserMigratedModel"></a>
<a id="tocSmarkusermigratedmodel"></a>
<a id="tocsmarkusermigratedmodel"></a>

```json
{
  "userEmail": "simple@example.com"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|userEmail|string|true|none|User email which is used in MyCP to mark user as migrated.|

<h2 id="tocS_ProblemDetails">ProblemDetails</h2>
<!-- backwards compatibility -->
<a id="schemaproblemdetails"></a>
<a id="schema_ProblemDetails"></a>
<a id="tocSproblemdetails"></a>
<a id="tocsproblemdetails"></a>

```json
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string",
  "property1": null,
  "property2": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|**additionalProperties**|any|false|none|none|
|type|string¦null|false|none|none|
|title|string¦null|false|none|none|
|status|integer(int32)¦null|false|none|none|
|detail|string¦null|false|none|none|
|instance|string¦null|false|none|none|

<h2 id="tocS_SubscriptionEnvironmentModel">SubscriptionEnvironmentModel</h2>
<!-- backwards compatibility -->
<a id="schemasubscriptionenvironmentmodel"></a>
<a id="schema_SubscriptionEnvironmentModel"></a>
<a id="tocSsubscriptionenvironmentmodel"></a>
<a id="tocssubscriptionenvironmentmodel"></a>

```json
{
  "id": 494,
  "name": "cp-eee-001",
  "region": "westeurope",
  "type": "development",
  "usedStorage": 1093314335,
  "backOfficeUri": "https://cp-000-000.chili-publish-sandbox.online/cp-000-000/interface.aspx"
}

```

Response model with environment details included in subscription.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|true|none|Environment Id.|
|name|string¦null|false|none|Environment name.|
|region|string¦null|false|none|Environment region.|
|type|[SubscriptionEnvironmentType](#schemasubscriptionenvironmenttype)|false|none|Environment type used in subscription.|
|usedStorage|integer(int64)|true|none|Total environment used storage.|
|backOfficeUri|string(uri)¦null|false|none|Backoffice URL.|

<h2 id="tocS_SubscriptionEnvironmentType">SubscriptionEnvironmentType</h2>
<!-- backwards compatibility -->
<a id="schemasubscriptionenvironmenttype"></a>
<a id="schema_SubscriptionEnvironmentType"></a>
<a id="tocSsubscriptionenvironmenttype"></a>
<a id="tocssubscriptionenvironmenttype"></a>

```json
"development"

```

Environment type used in subscription.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|Environment type used in subscription.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|development|
|*anonymous*|sandbox|
|*anonymous*|production|

<h2 id="tocS_SubscriptionLicenseModel">SubscriptionLicenseModel</h2>
<!-- backwards compatibility -->
<a id="schemasubscriptionlicensemodel"></a>
<a id="schema_SubscriptionLicenseModel"></a>
<a id="tocSsubscriptionlicensemodel"></a>
<a id="tocssubscriptionlicensemodel"></a>

```json
{
  "id": "CPF-2022-0000001",
  "coresTotal": 16,
  "coresUsed": 2,
  "url": "https://chili-publish.com/Licenses/Details/00000000-0000-0000-0000-000000000000",
  "licenseType": "Production"
}

```

Response model with license details included in subscription.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|License serial key|
|coresTotal|integer(int32)¦null|false|none|Max cores amount|
|coresUsed|integer(int32)|true|none|Used cores amount|
|url|string(uri)¦null|false|none|Url to license information|
|licenseType|[LicenseType](#schemalicensetype)|false|none|License type.|

<h2 id="tocS_SubscriptionModel">SubscriptionModel</h2>
<!-- backwards compatibility -->
<a id="schemasubscriptionmodel"></a>
<a id="schema_SubscriptionModel"></a>
<a id="tocSsubscriptionmodel"></a>
<a id="tocssubscriptionmodel"></a>

```json
{
  "id": 1,
  "name": "CHILI (Online)",
  "usedRenders": 1000,
  "maxRenders": 2500,
  "maxStorage": 250000000000,
  "storageUsed": 81959236,
  "environments": [
    {
      "id": 494,
      "name": "cp-eee-001",
      "region": "westeurope",
      "type": "development",
      "usedStorage": 1093314335,
      "backOfficeUri": "https://cp-000-000.chili-publish-sandbox.online/cp-000-000/interface.aspx"
    }
  ],
  "licenses": [
    {
      "id": "CPF-2022-0000001",
      "coresTotal": 16,
      "coresUsed": 2,
      "url": "https://chili-publish.com/Licenses/Details/00000000-0000-0000-0000-000000000000",
      "licenseType": "Production"
    }
  ],
  "startDate": "11/12/2022 12:15:32 AM",
  "endDate": "11/12/2023 12:15:32 PM",
  "subscriptionType": "OnPremises",
  "status": "Inactive",
  "clientName": "CHILI Group",
  "billingClientContact": "simple@example.com",
  "templateDesignerSeatsTotal": 6,
  "templateDesignerSeatsUsed": 4,
  "tenantInformation": {
    "sandboxEnvironmentsTotal": 4,
    "sandboxEnvironmentsUsed": 2,
    "productionEnvironmentsTotal": 4,
    "productionEnvironmentsUsed": 1
  }
}

```

Response model with detailed information about subscription.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|true|none|Subscription Id.|
|name|string¦null|false|none|Subscription name.|
|usedRenders|integer(int64)¦null|false|none|Used renders.|
|maxRenders|integer(int64)¦null|false|none|Max renders available in subscription.|
|maxStorage|integer(int64)¦null|false|none|Max storage available in subscription in bytes.|
|storageUsed|integer(int64)|true|none|Storage used in bytes.|
|environments|[[SubscriptionEnvironmentModel](#schemasubscriptionenvironmentmodel)]|true|none|Environments in subscription.|
|licenses|[[SubscriptionLicenseModel](#schemasubscriptionlicensemodel)]¦null|false|none|Licenses assigned to the subscription.|
|startDate|string¦null|false|none|Subscription start date.|
|endDate|string¦null|false|none|Subscription end date.|
|subscriptionType|[SubscriptionType](#schemasubscriptiontype)|true|none|Subscription type.|
|status|[SubscriptionStatus](#schemasubscriptionstatus)|true|none|Status of user subscription.|
|clientName|string¦null|false|none|Client name which uses the subscription.|
|billingClientContact|string¦null|false|none|Client billing contact information.|
|templateDesignerSeatsTotal|integer(int32)¦null|false|none|Max count of template designer seats.|
|templateDesignerSeatsUsed|integer(int32)¦null|false|none|Using count of template designer seats.|
|tenantInformation|[SubscriptionTenantInformationModel](#schemasubscriptiontenantinformationmodel)|true|none|Response model with subscription tenant information.|

<h2 id="tocS_SubscriptionRendersModel">SubscriptionRendersModel</h2>
<!-- backwards compatibility -->
<a id="schemasubscriptionrendersmodel"></a>
<a id="schema_SubscriptionRendersModel"></a>
<a id="tocSsubscriptionrendersmodel"></a>
<a id="tocssubscriptionrendersmodel"></a>

```json
{
  "date": "2021-11-01T00:00:00",
  "totalRenders": 4680,
  "environments": [
    {
      "name": "cp-itm-000",
      "renders": 4680
    }
  ]
}

```

Response model with subscription render information.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date|string(date-time)|true|none|Renders of environments date.|
|totalRenders|integer(int64)|true|none|Total count of renders for environments.|
|environments|[[EnvironmentRenderInformation](#schemaenvironmentrenderinformation)]|true|none|Environment render details.|

<h2 id="tocS_SubscriptionStatus">SubscriptionStatus</h2>
<!-- backwards compatibility -->
<a id="schemasubscriptionstatus"></a>
<a id="schema_SubscriptionStatus"></a>
<a id="tocSsubscriptionstatus"></a>
<a id="tocssubscriptionstatus"></a>

```json
"Inactive"

```

Status of user subscription.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|Status of user subscription.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Inactive|
|*anonymous*|Active|

<h2 id="tocS_SubscriptionTenantInformationModel">SubscriptionTenantInformationModel</h2>
<!-- backwards compatibility -->
<a id="schemasubscriptiontenantinformationmodel"></a>
<a id="schema_SubscriptionTenantInformationModel"></a>
<a id="tocSsubscriptiontenantinformationmodel"></a>
<a id="tocssubscriptiontenantinformationmodel"></a>

```json
{
  "sandboxEnvironmentsTotal": 4,
  "sandboxEnvironmentsUsed": 2,
  "productionEnvironmentsTotal": 4,
  "productionEnvironmentsUsed": 1
}

```

Response model with subscription tenant information.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sandboxEnvironmentsTotal|integer(int64)¦null|false|none|Total count of sandbox environments allowed in subscription.|
|sandboxEnvironmentsUsed|integer(int64)|true|none|Total count of sandbox environments used in subscription.|
|productionEnvironmentsTotal|integer(int64)¦null|false|none|Total count of production environments allowed in subscription.|
|productionEnvironmentsUsed|integer(int64)|true|none|Total count of production environments used in subscription.|

<h2 id="tocS_SubscriptionType">SubscriptionType</h2>
<!-- backwards compatibility -->
<a id="schemasubscriptiontype"></a>
<a id="schema_SubscriptionType"></a>
<a id="tocSsubscriptiontype"></a>
<a id="tocssubscriptiontype"></a>

```json
"OnPremises"

```

Subscription type.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|Subscription type.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|OnPremises|
|*anonymous*|Saas|

<h2 id="tocS_UpdateUserModel">UpdateUserModel</h2>
<!-- backwards compatibility -->
<a id="schemaupdateusermodel"></a>
<a id="schema_UpdateUserModel"></a>
<a id="tocSupdateusermodel"></a>
<a id="tocsupdateusermodel"></a>

```json
{
  "firstName": "John",
  "lastName": "Doe"
}

```

Request model that is used to update user's first name and last name in GraFx.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|firstName|string|true|none|User first name.|
|lastName|string|true|none|User last name.|

<h2 id="tocS_UserAccessibleSubscriptionsModel">UserAccessibleSubscriptionsModel</h2>
<!-- backwards compatibility -->
<a id="schemauseraccessiblesubscriptionsmodel"></a>
<a id="schema_UserAccessibleSubscriptionsModel"></a>
<a id="tocSuseraccessiblesubscriptionsmodel"></a>
<a id="tocsuseraccessiblesubscriptionsmodel"></a>

```json
{
  "userEmail": "simple@example.com"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|userEmail|string|true|none|User email which is used in MyCP to get accessible subscriptions.|

<h2 id="tocS_UserEmailVerificationStatusModel">UserEmailVerificationStatusModel</h2>
<!-- backwards compatibility -->
<a id="schemauseremailverificationstatusmodel"></a>
<a id="schema_UserEmailVerificationStatusModel"></a>
<a id="tocSuseremailverificationstatusmodel"></a>
<a id="tocsuseremailverificationstatusmodel"></a>

```json
{
  "isEmailVerified": true
}

```

Response model with user email verification status.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|isEmailVerified|boolean|true|none|User email verification status. `true` if user verified its email address.|

<h2 id="tocS_UserModel">UserModel</h2>
<!-- backwards compatibility -->
<a id="schemausermodel"></a>
<a id="schema_UserModel"></a>
<a id="tocSusermodel"></a>
<a id="tocsusermodel"></a>

```json
{
  "id": "auth0|630f8c2b524936fea93c0e75",
  "email": "simple@example.com",
  "firstName": "John",
  "lastName": "Doe",
  "avatar": "https://www.chili-publish.com/",
  "lastSeen": 1668540708,
  "status": "Active"
}

```

Response model with user information.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string¦null|false|none|User Id.|
|email|string¦null|false|none|User email.|
|firstName|string¦null|false|none|User first name.|
|lastName|string¦null|false|none|User last name.|
|avatar|string¦null|false|none|Link to avatar picture.|
|lastSeen|integer(int64)¦null|false|none|Last login datetime in seconds (unit timestamp).|
|status|string¦null|false|none|User activity status.|

