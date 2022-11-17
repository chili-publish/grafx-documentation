<h1 id="chili-grafx">CHILI GraFx v1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

# Authentication

- HTTP Authentication, scheme: Bearer Enter a bearer token (JWT):

<h1 id="chili-grafx-environmentroutingmodule">EnvironmentRoutingModule</h1>

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
  "id": 0,
  "name": "string",
  "type": 0,
  "usedStorage": 0,
  "usedStorageDetail": {
    "assets": 0,
    "documents": 0,
    "fonts": 0,
    "cache": 0,
    "backup": 0,
    "other": 0
  },
  "tenantName": "string",
  "region": "string",
  "renders": 0
}
```

<h3 id="get--api-v1-environment-{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns environment information.|[EnvironmentModel](#schemaenvironmentmodel)|
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
|groupBy|query|string|true|Groups render information by: `year`, `month`|

> Example responses

> 200 Response

```json
[
  {
    "date": "2019-08-24T14:15:22Z",
    "totalRenders": 0,
    "renderDetail": [
      {
        "name": "string",
        "renders": 0
      }
    ]
  }
]
```

<h3 id="get--api-v1-environment-{id}-renders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns environment renders information.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If groupBy is missing or invalid.|[ProblemDetails](#schemaproblemdetails)|
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

<h1 id="chili-grafx-inforoutingmodule">InfoRoutingModule</h1>

## get  api v1 info

`GET /api/v1/info`

*Gets information about API.*

> Example responses

> 200 Response

```json
{
  "data": {
    "serverVersion": "string"
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

<h1 id="chili-grafx-rolesroutingmodule">RolesRoutingModule</h1>

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

<h3 id="get--api-v1-roles-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of supported user roles.|Inline|

<h3 id="get--api-v1-roles-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-subscriptionroutingmodule">SubscriptionRoutingModule</h1>

## get  api v1 subscriptions

`GET /api/v1/subscriptions`

*Gets all existing subscriptions.*

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "name": "string",
    "isActive": true
  }
]
```

<h3 id="get--api-v1-subscriptions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of subscriptions.|Inline|

<h3 id="get--api-v1-subscriptions-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[BasicSubscriptionModel](#schemabasicsubscriptionmodel)]|false|none|[Response model with subscription information.]|
|» id|integer(int32)|true|none|Subscription Id.|
|» name|string|true|none|Subscription name.|
|» isActive|boolean|true|none|`True` if subscription is still active.|

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
  "id": 0,
  "name": "string",
  "usedRenders": 0,
  "maxRenders": 0,
  "maxStorage": 0,
  "storageUsed": 0,
  "environments": [
    {
      "id": 0,
      "name": "string",
      "region": "string",
      "type": 0,
      "usedStorage": 0,
      "backOfficeUri": "http://example.com"
    }
  ],
  "licenses": [
    {
      "id": "string",
      "coresTotal": 0,
      "coresUsed": 0,
      "url": "http://example.com",
      "licenseType": 0
    }
  ],
  "startDate": {
    "calendar": {
      "id": "string",
      "name": "string",
      "minYear": 0,
      "maxYear": 0,
      "eras": [
        {
          "name": "string"
        }
      ]
    },
    "year": 0,
    "month": 0,
    "day": 0,
    "dayOfWeek": 0,
    "yearOfEra": 0,
    "era": {
      "name": "string"
    },
    "dayOfYear": 0
  },
  "endDate": {
    "calendar": {
      "id": "string",
      "name": "string",
      "minYear": 0,
      "maxYear": 0,
      "eras": [
        {
          "name": "string"
        }
      ]
    },
    "year": 0,
    "month": 0,
    "day": 0,
    "dayOfWeek": 0,
    "yearOfEra": 0,
    "era": {
      "name": "string"
    },
    "dayOfYear": 0
  },
  "subscriptionType": 0,
  "status": 0,
  "clientName": "string",
  "billingClientContact": "string",
  "templateDesignerSeatsTotal": 0,
  "templateDesignerSeatsUsed": 0,
  "tenantInformation": {
    "sandboxEnvironmentsTotal": 0,
    "sandboxEnvironmentsUsed": 0,
    "productionEnvironmentsTotal": 0,
    "productionEnvironmentsUsed": 0
  }
}
```

<h3 id="get--api-v1-subscription-{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns subscription.|[SubscriptionModel](#schemasubscriptionmodel)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ProblemDetails](#schemaproblemdetails)|

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

<h3 id="get--api-v1-subscription-{subscriptionguid}-{environmentguid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns `True` if environment is under subscription.|boolean|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 subscription {id} renders

`GET /api/v1/subscription/{id}/renders`

*Gets environments render information included in subscription.*

<h3 id="get--api-v1-subscription-{id}-renders-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|Subscription Id.|
|groupBy|query|string|true|Groups render information by: `year`, `month`|
|top|query|integer(int32)|true|Returns first `top` environments with renders.|

> Example responses

> 200 Response

```json
[
  {
    "date": "2019-08-24T14:15:22Z",
    "totalRenders": 0,
    "environments": [
      {
        "name": "string",
        "renders": 0
      }
    ]
  }
]
```

<h3 id="get--api-v1-subscription-{id}-renders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of environments render details.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If groupBy is missing or invalid.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ProblemDetails](#schemaproblemdetails)|

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
    "id": "string",
    "email": "string",
    "firstName": "string",
    "lastName": "string",
    "avatar": "string",
    "lastSeen": 0,
    "status": "string"
  }
]
```

<h3 id="get--api-v1-subscription-{id}-users-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns array of user details.|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|If subscription with that Id is not found.|[ProblemDetails](#schemaproblemdetails)|

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

<h1 id="chili-grafx-usermanagementroutingmodule">UserManagementRoutingModule</h1>

## post  api v1 users manage add

`POST /api/v1/users/manage/add`

*Adds new user in GraFx.*

> Body parameter

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "subscriptionIds": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "customerGuid": "d7cc35b4-123a-43e1-9482-fdc8ca6dcf4f"
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
  "userId": "string"
}
```

<h3 id="post--api-v1-users-manage-add-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns ID of successfully created user|[CreateUserResultModel](#schemacreateuserresultmodel)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If one of the following params is missing: signature, email, firstName, lastName.|[ProblemDetails](#schemaproblemdetails)|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|If user with the same email already exists.|[ProblemDetails](#schemaproblemdetails)|

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
  "firstName": "string",
  "lastName": "string"
}
```

<h3 id="put--api-v1-users-{userid}-manage-update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|userId|path|string|true|UserId in GraFx.|
|body|body|[UpdateUserModel](#schemaupdateusermodel)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="put--api-v1-users-{userid}-manage-update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|If user has been successfully updated.|[Void](#schemavoid)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If one of the following params is missing: firstName, lastName|[ProblemDetails](#schemaproblemdetails)|
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
|signature|header|string|false|Signature used to verify that the request called by an authorized party.|

> Example responses

> 200 Response

```json
{
  "isEmailVerified": true
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
  "userEmail": "string"
}
```

<h3 id="put--api-v1-users-manage-migrate-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|signature|header|string|false|Signature used to verify that the request called by an authorized party.|
|body|body|[MarkUserMigratedModel](#schemamarkusermigratedmodel)|false|none|

> Example responses

> 400 Response

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

<h3 id="put--api-v1-users-manage-migrate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|If user successfully marked as migrated.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|If one of the following params is missing: signature, userEmail.|[ProblemDetails](#schemaproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ProblemDetails](#schemaproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|If user cannot be marked as migrated due to internal failure.|[ProblemDetails](#schemaproblemdetails)|

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
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "subscriptionIds": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "customerGuid": "d7cc35b4-123a-43e1-9482-fdc8ca6dcf4f"
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
  "id": 0,
  "name": "string",
  "isActive": true
}

```

Response model with subscription information.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|true|none|Subscription Id.|
|name|string|true|none|Subscription name.|
|isActive|boolean|true|none|`True` if subscription is still active.|

<h2 id="tocS_CalendarSystem">CalendarSystem</h2>
<!-- backwards compatibility -->
<a id="schemacalendarsystem"></a>
<a id="schema_CalendarSystem"></a>
<a id="tocScalendarsystem"></a>
<a id="tocscalendarsystem"></a>

```json
{
  "id": "string",
  "name": "string",
  "minYear": 0,
  "maxYear": 0,
  "eras": [
    {
      "name": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string¦null|false|read-only|none|
|name|string¦null|false|read-only|none|
|minYear|integer(int32)|false|read-only|none|
|maxYear|integer(int32)|false|read-only|none|
|eras|[[Era](#schemaera)]¦null|false|read-only|none|

<h2 id="tocS_CreateUserResultModel">CreateUserResultModel</h2>
<!-- backwards compatibility -->
<a id="schemacreateuserresultmodel"></a>
<a id="schema_CreateUserResultModel"></a>
<a id="tocScreateuserresultmodel"></a>
<a id="tocscreateuserresultmodel"></a>

```json
{
  "userId": "string"
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
  "id": 0,
  "name": "string",
  "type": 0,
  "usedStorage": 0,
  "usedStorageDetail": {
    "assets": 0,
    "documents": 0,
    "fonts": 0,
    "cache": 0,
    "backup": 0,
    "other": 0
  },
  "tenantName": "string",
  "region": "string",
  "renders": 0
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
  "name": "string",
  "renders": 0
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
  "name": "string",
  "renders": 0
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
  "date": "2019-08-24T14:15:22Z",
  "totalRenders": 0,
  "renderDetail": [
    {
      "name": "string",
      "renders": 0
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
  "assets": 0,
  "documents": 0,
  "fonts": 0,
  "cache": 0,
  "backup": 0,
  "other": 0
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
0

```

Environment type.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|integer(int32)|false|none|Environment type.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|0|
|*anonymous*|1|

<h2 id="tocS_Era">Era</h2>
<!-- backwards compatibility -->
<a id="schemaera"></a>
<a id="schema_Era"></a>
<a id="tocSera"></a>
<a id="tocsera"></a>

```json
{
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string¦null|false|read-only|none|

<h2 id="tocS_Info">Info</h2>
<!-- backwards compatibility -->
<a id="schemainfo"></a>
<a id="schema_Info"></a>
<a id="tocSinfo"></a>
<a id="tocsinfo"></a>

```json
{
  "serverVersion": "string"
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
    "serverVersion": "string"
  }
}

```

Response model used for providing the information about API.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|data|[Info](#schemainfo)|true|none|Model used for providing technical information about API.|

<h2 id="tocS_IsoDayOfWeek">IsoDayOfWeek</h2>
<!-- backwards compatibility -->
<a id="schemaisodayofweek"></a>
<a id="schema_IsoDayOfWeek"></a>
<a id="tocSisodayofweek"></a>
<a id="tocsisodayofweek"></a>

```json
0

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|integer(int32)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|0|
|*anonymous*|1|
|*anonymous*|2|
|*anonymous*|3|
|*anonymous*|4|
|*anonymous*|5|
|*anonymous*|6|
|*anonymous*|7|

<h2 id="tocS_LicenseType">LicenseType</h2>
<!-- backwards compatibility -->
<a id="schemalicensetype"></a>
<a id="schema_LicenseType"></a>
<a id="tocSlicensetype"></a>
<a id="tocslicensetype"></a>

```json
0

```

License type.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|integer(int32)|false|none|License type.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|0|
|*anonymous*|1|
|*anonymous*|2|

<h2 id="tocS_LocalDate">LocalDate</h2>
<!-- backwards compatibility -->
<a id="schemalocaldate"></a>
<a id="schema_LocalDate"></a>
<a id="tocSlocaldate"></a>
<a id="tocslocaldate"></a>

```json
{
  "calendar": {
    "id": "string",
    "name": "string",
    "minYear": 0,
    "maxYear": 0,
    "eras": [
      {
        "name": "string"
      }
    ]
  },
  "year": 0,
  "month": 0,
  "day": 0,
  "dayOfWeek": 0,
  "yearOfEra": 0,
  "era": {
    "name": "string"
  },
  "dayOfYear": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|calendar|[CalendarSystem](#schemacalendarsystem)|false|none|none|
|year|integer(int32)|false|none|none|
|month|integer(int32)|false|none|none|
|day|integer(int32)|false|none|none|
|dayOfWeek|[IsoDayOfWeek](#schemaisodayofweek)|false|none|none|
|yearOfEra|integer(int32)|false|read-only|none|
|era|[Era](#schemaera)|false|none|none|
|dayOfYear|integer(int32)|false|read-only|none|

<h2 id="tocS_MarkUserMigratedModel">MarkUserMigratedModel</h2>
<!-- backwards compatibility -->
<a id="schemamarkusermigratedmodel"></a>
<a id="schema_MarkUserMigratedModel"></a>
<a id="tocSmarkusermigratedmodel"></a>
<a id="tocsmarkusermigratedmodel"></a>

```json
{
  "userEmail": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|userEmail|string¦null|false|none|User email which is used in MyCP to mark user as migrated.|

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
  "id": 0,
  "name": "string",
  "region": "string",
  "type": 0,
  "usedStorage": 0,
  "backOfficeUri": "http://example.com"
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
0

```

Environment type used in subscription.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|integer(int32)|false|none|Environment type used in subscription.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|0|
|*anonymous*|1|

<h2 id="tocS_SubscriptionLicenseModel">SubscriptionLicenseModel</h2>
<!-- backwards compatibility -->
<a id="schemasubscriptionlicensemodel"></a>
<a id="schema_SubscriptionLicenseModel"></a>
<a id="tocSsubscriptionlicensemodel"></a>
<a id="tocssubscriptionlicensemodel"></a>

```json
{
  "id": "string",
  "coresTotal": 0,
  "coresUsed": 0,
  "url": "http://example.com",
  "licenseType": 0
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
  "id": 0,
  "name": "string",
  "usedRenders": 0,
  "maxRenders": 0,
  "maxStorage": 0,
  "storageUsed": 0,
  "environments": [
    {
      "id": 0,
      "name": "string",
      "region": "string",
      "type": 0,
      "usedStorage": 0,
      "backOfficeUri": "http://example.com"
    }
  ],
  "licenses": [
    {
      "id": "string",
      "coresTotal": 0,
      "coresUsed": 0,
      "url": "http://example.com",
      "licenseType": 0
    }
  ],
  "startDate": {
    "calendar": {
      "id": "string",
      "name": "string",
      "minYear": 0,
      "maxYear": 0,
      "eras": [
        {
          "name": "string"
        }
      ]
    },
    "year": 0,
    "month": 0,
    "day": 0,
    "dayOfWeek": 0,
    "yearOfEra": 0,
    "era": {
      "name": "string"
    },
    "dayOfYear": 0
  },
  "endDate": {
    "calendar": {
      "id": "string",
      "name": "string",
      "minYear": 0,
      "maxYear": 0,
      "eras": [
        {
          "name": "string"
        }
      ]
    },
    "year": 0,
    "month": 0,
    "day": 0,
    "dayOfWeek": 0,
    "yearOfEra": 0,
    "era": {
      "name": "string"
    },
    "dayOfYear": 0
  },
  "subscriptionType": 0,
  "status": 0,
  "clientName": "string",
  "billingClientContact": "string",
  "templateDesignerSeatsTotal": 0,
  "templateDesignerSeatsUsed": 0,
  "tenantInformation": {
    "sandboxEnvironmentsTotal": 0,
    "sandboxEnvironmentsUsed": 0,
    "productionEnvironmentsTotal": 0,
    "productionEnvironmentsUsed": 0
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
|startDate|[LocalDate](#schemalocaldate)|false|none|none|
|endDate|[LocalDate](#schemalocaldate)|false|none|none|
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
  "date": "2019-08-24T14:15:22Z",
  "totalRenders": 0,
  "environments": [
    {
      "name": "string",
      "renders": 0
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
0

```

Status of user subscription.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|integer(int32)|false|none|Status of user subscription.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|0|
|*anonymous*|1|

<h2 id="tocS_SubscriptionTenantInformationModel">SubscriptionTenantInformationModel</h2>
<!-- backwards compatibility -->
<a id="schemasubscriptiontenantinformationmodel"></a>
<a id="schema_SubscriptionTenantInformationModel"></a>
<a id="tocSsubscriptiontenantinformationmodel"></a>
<a id="tocssubscriptiontenantinformationmodel"></a>

```json
{
  "sandboxEnvironmentsTotal": 0,
  "sandboxEnvironmentsUsed": 0,
  "productionEnvironmentsTotal": 0,
  "productionEnvironmentsUsed": 0
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
0

```

Subscription type.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|integer(int32)|false|none|Subscription type.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|0|
|*anonymous*|1|

<h2 id="tocS_UpdateUserModel">UpdateUserModel</h2>
<!-- backwards compatibility -->
<a id="schemaupdateusermodel"></a>
<a id="schema_UpdateUserModel"></a>
<a id="tocSupdateusermodel"></a>
<a id="tocsupdateusermodel"></a>

```json
{
  "firstName": "string",
  "lastName": "string"
}

```

Request model that is used to update user's first name and last name in GraFx.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|firstName|string|true|none|User first name.|
|lastName|string|true|none|User last name.|

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
|isEmailVerified|boolean|true|none|User email verification status. `True` if user verified its email address.|

<h2 id="tocS_UserModel">UserModel</h2>
<!-- backwards compatibility -->
<a id="schemausermodel"></a>
<a id="schema_UserModel"></a>
<a id="tocSusermodel"></a>
<a id="tocsusermodel"></a>

```json
{
  "id": "string",
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "avatar": "string",
  "lastSeen": 0,
  "status": "string"
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

<h2 id="tocS_Void">Void</h2>
<!-- backwards compatibility -->
<a id="schemavoid"></a>
<a id="schema_Void"></a>
<a id="tocSvoid"></a>
<a id="tocsvoid"></a>

```json
{}

```

### Properties

*None*

