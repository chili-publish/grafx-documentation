<h1 id="chili-grafx-platform">CHILI GraFx Platform v1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

API allowing integration with the CHILI GraFx Platform.

# Authentication

- HTTP Authentication, scheme: Bearer Enter a bearer token (JWT):

<h1 id="chili-grafx-platform-environments">Environments</h1>

## Gets environment information.

`GET /api/v1/environment/{id}`

<h3 id="gets-environment-information.-parameters">Parameters</h3>

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

<h3 id="gets-environment-information.-responses">Responses</h3>

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

## Get environment renders information.

`GET /api/v1/environment/{id}/renders`

<h3 id="get-environment-renders-information.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|Environment Id.|
|groupBy|query|string|true|Groups render information.|
|startDate|query|string|false|Start date of the range from which to return the renders. Required if `endDate` is provided. Format: yyyy-MM-dd.|
|endDate|query|string|false|End date of the range from which to return the renders. Required if `startDate` is provided. Format: yyyy-MM-dd.|

#### Detailed descriptions

**groupBy**: Groups render information.
                For `year` returns renders for last 12 months and groups renders by each month.
                For `month` returns renders for last 30 days and groups renders by each day.
                These ranges can be overwritten by providing both `startDate` and `endDate` parameters.

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

<h3 id="get-environment-renders-information.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns environment renders information.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If groupBy is missing or one of the params has incorrect format.|[ProblemDetails](#schemaproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If environment with such Id is not found.|[ProblemDetails](#schemaproblemdetails)|

<h3 id="get-environment-renders-information.-responseschema">Response Schema</h3>

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

## Get environments under specified subscription.

`GET /api/v1/environments`

<h3 id="get-environments-under-specified-subscription.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|subscriptionId|query|string(uuid)|true|Specifies ID of the subscription to read environments from.|

> Example responses

> 200 Response

```json
[
  {
    "id": 494,
    "guid": "18a3ae5c-3bc5-42eb-b8d8-0307fbbbfea1",
    "name": "CHILI Team",
    "region": "westeurope",
    "type": "development",
    "usedStorage": 1093314335,
    "backOfficeUri": "https://cp-000-000.chili-publish-sandbox.online/cp-000-000/interface.aspx",
    "technicalName": "ch-01"
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

<h3 id="get-environments-under-specified-subscription.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns environments under specified subscription.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If `subscriptionId` is missing or has incorrect format.|[ProblemDetails](#schemaproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If subscription with such ID is not found.|[ProblemDetails](#schemaproblemdetails)|

<h3 id="get-environments-under-specified-subscription.-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[BasicEnvironmentModel](#schemabasicenvironmentmodel)]|false|none|[Response model with the basic information about environment.]|
|» id|integer(int32)|true|none|Environment Id.|
|» guid|string(uuid)|false|none|Environment guid.|
|» name|string¦null|false|none|Environment display name.|
|» region|string¦null|false|none|Environment region.|
|» type|[EnvironmentType](#schemaenvironmenttype)|false|none|Environment type.|
|» usedStorage|integer(int64)|true|none|Total environment used storage.|
|» backOfficeUri|string(uri)¦null|false|none|Backoffice URL.|
|» technicalName|string¦null|false|none|Environment technical name.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|development|
|type|sandbox|
|type|production|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-platform-info">Info</h1>

## Gets information about API.

`GET /api/v1/info`

> Example responses

> 200 Response

```json
{
  "data": {
    "serverVersion": "1.0.0"
  }
}
```

<h3 id="gets-information-about-api.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns information about API.|[InfoResponse](#schemainforesponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## Checks server availability.

`GET /api/ping`

<h3 id="checks-server-availability.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|If server is available.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-platform-subscriptions">Subscriptions</h1>

## Gets all existing subscriptions.

`GET /api/v1/subscriptions`

> Example responses

> 200 Response

```json
[
  {
    "id": 44,
    "guid": "d9aa2149-7f95-4ecc-ab2f-d6d12708f8da",
    "name": "CHILI - OnlineTrial",
    "isActive": true,
    "clientId": "950c78e8-99c0-4681-98b3-a8b2ff11683c",
    "clientName": "CHILI"
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

<h3 id="gets-all-existing-subscriptions.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of subscriptions.|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|

<h3 id="gets-all-existing-subscriptions.-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[BasicSubscriptionModel](#schemabasicsubscriptionmodel)]|false|none|[Response model with subscription information.]|
|» id|integer(int32)|true|none|Subscription Id.|
|» guid|string(uuid)|true|none|Subscription GUID.|
|» name|string|true|none|Subscription name.|
|» isActive|boolean|true|none|`true` if subscription is still active.|
|» clientId|string(uuid)¦null|false|none|Client GUID.|
|» clientName|string¦null|false|none|Client name.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## Gets detailed information about subscription.

`GET /api/v1/subscription/{id}`

<h3 id="gets-detailed-information-about-subscription.-parameters">Parameters</h3>

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

<h3 id="gets-detailed-information-about-subscription.-responses">Responses</h3>

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

## Checks if environment is under subscription.

`GET /api/v1/subscription/{subscriptionGuid}/{environmentGuid}`

<h3 id="checks-if-environment-is-under-subscription.-parameters">Parameters</h3>

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

<h3 id="checks-if-environment-is-under-subscription.-responses">Responses</h3>

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

## Gets environments render information included in subscription.

`GET /api/v1/subscription/{id}/renders`

All environments under that subscription are returned in the specific order by the environment type
(Production, Sandbox, Development) and then by the descending order based on renders amount.

<h3 id="gets-environments-render-information-included-in-subscription.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|Subscription Id.|
|groupBy|query|string|true|Groups render information.|
|top|query|integer(int32)|false|When top parameter is provided, the information for the `top` number of environments with higher number|
|startDate|query|string|false|Start date of the range from which to return the renders. Required if `endDate` is provided. Format: yyyy-MM-dd.|
|endDate|query|string|false|End date of the range from which to return the renders. Required if `startDate` is provided. Format: yyyy-MM-dd.|

#### Detailed descriptions

**groupBy**: Groups render information.
For `year` returns renders for last 12 months and groups renders by each month.
For `month` returns renders for last 30 days and groups renders by each day.
These ranges can be overwritten by providing both `startDate` and `endDate` parameters.

**top**: When top parameter is provided, the information for the `top` number of environments with higher number
of renders is returned and for all the rest of existing environments in the subscription the renders are
concatenated under "Others".

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

<h3 id="gets-environments-render-information-included-in-subscription.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of environments render details.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If groupBy is missing or one of the params has incorrect format.|[ProblemDetails](#schemaproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If subscription with this id is not found for the authenticated user.|[ProblemDetails](#schemaproblemdetails)|

<h3 id="gets-environments-render-information-included-in-subscription.-responseschema">Response Schema</h3>

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

## Gets users that use the subscription.

`GET /api/v1/subscription/{id}/users`

<h3 id="gets-users-that-use-the-subscription.-parameters">Parameters</h3>

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

<h3 id="gets-users-that-use-the-subscription.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of user details.|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|If bearer token is missing.|[ProblemDetails](#schemaproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|If user does not have required role.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If subscription with this id is not found for the authenticated user.|[ProblemDetails](#schemaproblemdetails)|

<h3 id="gets-users-that-use-the-subscription.-responseschema">Response Schema</h3>

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

# Schemas

<h2 id="tocS_BasicEnvironmentModel">BasicEnvironmentModel</h2>
<!-- backwards compatibility -->
<a id="schemabasicenvironmentmodel"></a>
<a id="schema_BasicEnvironmentModel"></a>
<a id="tocSbasicenvironmentmodel"></a>
<a id="tocsbasicenvironmentmodel"></a>

```json
{
  "id": 494,
  "guid": "18a3ae5c-3bc5-42eb-b8d8-0307fbbbfea1",
  "name": "CHILI Team",
  "region": "westeurope",
  "type": "development",
  "usedStorage": 1093314335,
  "backOfficeUri": "https://cp-000-000.chili-publish-sandbox.online/cp-000-000/interface.aspx",
  "technicalName": "ch-01"
}

```

Response model with the basic information about environment.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|true|none|Environment Id.|
|guid|string(uuid)|false|none|Environment guid.|
|name|string¦null|false|none|Environment display name.|
|region|string¦null|false|none|Environment region.|
|type|[EnvironmentType](#schemaenvironmenttype)|false|none|Environment type.|
|usedStorage|integer(int64)|true|none|Total environment used storage.|
|backOfficeUri|string(uri)¦null|false|none|Backoffice URL.|
|technicalName|string¦null|false|none|Environment technical name.|

<h2 id="tocS_BasicSubscriptionModel">BasicSubscriptionModel</h2>
<!-- backwards compatibility -->
<a id="schemabasicsubscriptionmodel"></a>
<a id="schema_BasicSubscriptionModel"></a>
<a id="tocSbasicsubscriptionmodel"></a>
<a id="tocsbasicsubscriptionmodel"></a>

```json
{
  "id": 44,
  "guid": "d9aa2149-7f95-4ecc-ab2f-d6d12708f8da",
  "name": "CHILI - OnlineTrial",
  "isActive": true,
  "clientId": "950c78e8-99c0-4681-98b3-a8b2ff11683c",
  "clientName": "CHILI"
}

```

Response model with subscription information.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|true|none|Subscription Id.|
|guid|string(uuid)|true|none|Subscription GUID.|
|name|string|true|none|Subscription name.|
|isActive|boolean|true|none|`true` if subscription is still active.|
|clientId|string(uuid)¦null|false|none|Client GUID.|
|clientName|string¦null|false|none|Client name.|

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

