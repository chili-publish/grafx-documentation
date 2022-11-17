<!-- Generator: Widdershins v4.0.1 -->

<h1 id="chili-grafx">CHILI GraFx v1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Base URLs:

* <a href="/grafx">/grafx</a>

# Authentication

- HTTP Authentication, scheme: bearer Enter a bearer token (JWT):

<h1 id="chili-grafx-fonts">Fonts</h1>

## get  api v1 environment {environment} fonts

`GET /api/v1/environment/{environment}/fonts`

*Returns all fonts in the environment including subfolders*

Returns all fonts in the environment including subfolders

<h3 id="get--api-v1-environment-{environment}-fonts-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|nextPageToken|query|string|false|Next page token|
|limit|query|integer|false|Amount of resources per-response|
|sortBy|query|string|false|Name of field sort is based|
|sortOrder|query|string|false|Order of resources, ascending of descending|
|folder|query|string|false|Folder in which search should be done (NOTE: forward slashes only, should start with slash)|
|search|query|string|false|Search by name, relativePath or resource ID|

#### Enumerated Values

|Parameter|Value|
|---|---|
|sortBy|name|
|sortBy|id|
|sortBy|relativePath|
|sortOrder|asc|
|sortOrder|desc|

> Example responses

> 200 Response

```json
{
  "pageSize": "1",
  "data": [
    {
      "family": "Arial",
      "style": "Regular",
      "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
      "name": "Resource",
      "relativePath": "Folder",
      "extension": "jpg",
      "type": "0"
    }
  ],
  "links": {
    "nextPage": "string"
  }
}
```

<h3 id="get--api-v1-environment-{environment}-fonts-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[FontsResponse](#schemafontsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|One of arguments is incorrect|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} fonts directory

`GET /api/v1/environment/{environment}/fonts/directory`

*Returns all fonts and directories in the environment*

Returns all fonts and directories in the environment located directly in requested folder not including subfolders (in root when no folder is provided)

<h3 id="get--api-v1-environment-{environment}-fonts-directory-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|nextPageToken|query|string|false|Next page token|
|limit|query|integer|false|Amount of folders per-response|
|sortBy|query|string|false|Name of field sort is based|
|sortOrder|query|string|false|Order of resources, ascending of descending|
|folder|query|string|false|Folder in which search should be done (NOTE: forward slashes only, should start with slash)|
|search|query|string|false|Search by name, relativePath or resource ID|

#### Enumerated Values

|Parameter|Value|
|---|---|
|sortBy|name|
|sortBy|id|
|sortBy|relativePath|
|sortOrder|asc|
|sortOrder|desc|

> Example responses

> 200 Response

```json
{
  "pageSize": "1",
  "data": [
    {
      "family": "Arial",
      "style": "Regular",
      "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
      "name": "Resource",
      "relativePath": "Folder",
      "extension": "jpg",
      "type": "0"
    }
  ],
  "links": {
    "nextPage": "string"
  }
}
```

<h3 id="get--api-v1-environment-{environment}-fonts-directory-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[FontsResponse](#schemafontsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|One of arguments is incorrect|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} fonts {fontId}

`GET /api/v1/environment/{environment}/fonts/{fontId}`

*Returns font by ID in the environment*

Returns font by ID in the environment

<h3 id="get--api-v1-environment-{environment}-fonts-{fontid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|fontId|path|string|true|ID of the font|

> Example responses

> 200 Response

```json
{
  "family": "Arial",
  "style": "Regular",
  "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
  "name": "Resource",
  "relativePath": "Folder",
  "extension": "jpg",
  "type": "0"
}
```

<h3 id="get--api-v1-environment-{environment}-fonts-{fontid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Font](#schemafont)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment or font is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} fonts {fontId} download

`GET /api/v1/environment/{environment}/fonts/{fontId}/download`

*Downloads font by ID in the environment*

Downloads font by ID in the environment

<h3 id="get--api-v1-environment-{environment}-fonts-{fontid}-download-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|fontId|path|string|true|ID of the font|

> Example responses

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": "401",
  "traceId": "00-4c7122268e63dfb01f47bd1a23507588-13f1aab74314c293-00"
}
```

<h3 id="get--api-v1-environment-{environment}-fonts-{fontid}-download-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success, returns file|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment or font is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} fonts {fontId} preview

`GET /api/v1/environment/{environment}/fonts/{fontId}/preview`

*Returns image preview of the font by ID in the environment*

Returns image preview of the font by ID in the environment

<h3 id="get--api-v1-environment-{environment}-fonts-{fontid}-preview-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|fontId|path|string|true|ID of the font|
|previewType|query|string|false|Type of preview|

#### Enumerated Values

|Parameter|Value|
|---|---|
|previewType|highest|
|previewType|medium|
|previewType|thumbnail|

> Example responses

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": "401",
  "traceId": "00-4c7122268e63dfb01f47bd1a23507588-13f1aab74314c293-00"
}
```

<h3 id="get--api-v1-environment-{environment}-fonts-{fontid}-preview-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success, returns file|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment, font or preview is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} fonts {fontId} preview {previewType}

`GET /api/v1/environment/{environment}/fonts/{fontId}/preview/{previewType}`

*Returns image preview of the font by ID in the environment*

Returns image preview of the font by ID in the environment

<h3 id="get--api-v1-environment-{environment}-fonts-{fontid}-preview-{previewtype}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|fontId|path|string|true|ID of the font|
|previewType|path|string|true|Type of preview|

#### Enumerated Values

|Parameter|Value|
|---|---|
|previewType|highest|
|previewType|medium|
|previewType|thumbnail|

> Example responses

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": "401",
  "traceId": "00-4c7122268e63dfb01f47bd1a23507588-13f1aab74314c293-00"
}
```

<h3 id="get--api-v1-environment-{environment}-fonts-{fontid}-preview-{previewtype}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success, returns file|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment, font or preview is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-media">Media</h1>

## get  api v1 environment {environment} media

`GET /api/v1/environment/{environment}/media`

*Returns all media in the environment including subfolders*

Returns all media in the environment including subfolders

<h3 id="get--api-v1-environment-{environment}-media-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|nextPageToken|query|string|false|Next page token|
|limit|query|integer|false|Amount of resources per-response|
|sortBy|query|string|false|Name of field sort is based|
|sortOrder|query|string|false|Order of resources, ascending of descending|
|folder|query|string|false|Folder in which search should be done (NOTE: forward slashes only, should start with slash)|
|search|query|string|false|Search by name, relativePath or resource ID|

#### Enumerated Values

|Parameter|Value|
|---|---|
|sortBy|name|
|sortBy|id|
|sortBy|relativePath|
|sortOrder|asc|
|sortOrder|desc|

> Example responses

> 200 Response

```json
{
  "pageSize": "1",
  "data": [
    {
      "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
      "name": "Resource",
      "relativePath": "Folder",
      "extension": "jpg",
      "type": "0"
    }
  ],
  "links": {
    "nextPage": "string"
  }
}
```

<h3 id="get--api-v1-environment-{environment}-media-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[MediasResponse](#schemamediasresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|One of arguments is incorrect|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} media directory

`GET /api/v1/environment/{environment}/media/directory`

*Returns all media and directories in the environment*

Returns all media and directories in the environment located directly in requested folder not including subfolders (in root when no folder is provided)

<h3 id="get--api-v1-environment-{environment}-media-directory-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|nextPageToken|query|string|false|Next page token|
|limit|query|integer|false|Amount of folders per-response|
|sortBy|query|string|false|Name of field sort is based|
|sortOrder|query|string|false|Order of resources, ascending of descending|
|folder|query|string|false|Folder in which search should be done (NOTE: forward slashes only, should start with slash)|
|search|query|string|false|Search by name, relativePath or resource ID|

#### Enumerated Values

|Parameter|Value|
|---|---|
|sortBy|name|
|sortBy|id|
|sortBy|relativePath|
|sortOrder|asc|
|sortOrder|desc|

> Example responses

> 200 Response

```json
{
  "pageSize": "1",
  "data": [
    {
      "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
      "name": "Resource",
      "relativePath": "Folder",
      "extension": "jpg",
      "type": "0"
    }
  ],
  "links": {
    "nextPage": "string"
  }
}
```

<h3 id="get--api-v1-environment-{environment}-media-directory-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[MediasResponse](#schemamediasresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|One of arguments is incorrect|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} media {mediaId}

`GET /api/v1/environment/{environment}/media/{mediaId}`

*Returns media by ID in the environment*

Returns media by ID in the environment

<h3 id="get--api-v1-environment-{environment}-media-{mediaid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|mediaId|path|string|true|ID of the media|

> Example responses

> 200 Response

```json
{
  "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
  "name": "Resource",
  "relativePath": "Folder",
  "extension": "jpg",
  "type": "0"
}
```

<h3 id="get--api-v1-environment-{environment}-media-{mediaid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Media](#schemamedia)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment or media is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} media {mediaId} download

`GET /api/v1/environment/{environment}/media/{mediaId}/download`

*Downloads media by ID in the environment*

Downloads media by ID in the environment

<h3 id="get--api-v1-environment-{environment}-media-{mediaid}-download-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|mediaId|path|string|true|ID of the media|

> Example responses

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": "401",
  "traceId": "00-4c7122268e63dfb01f47bd1a23507588-13f1aab74314c293-00"
}
```

<h3 id="get--api-v1-environment-{environment}-media-{mediaid}-download-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success, returns file|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment or media is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} media {mediaId} preview

`GET /api/v1/environment/{environment}/media/{mediaId}/preview`

*Returns image preview of the media by ID in the environment*

Returns image preview of the media by ID in the environment

<h3 id="get--api-v1-environment-{environment}-media-{mediaid}-preview-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|mediaId|path|string|true|ID of the media|
|previewType|query|string|false|Type of preview|

#### Enumerated Values

|Parameter|Value|
|---|---|
|previewType|highest|
|previewType|medium|
|previewType|thumbnail|

> Example responses

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": "401",
  "traceId": "00-4c7122268e63dfb01f47bd1a23507588-13f1aab74314c293-00"
}
```

<h3 id="get--api-v1-environment-{environment}-media-{mediaid}-preview-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success, returns file|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment, media or preview is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} media {mediaId} preview {previewType}

`GET /api/v1/environment/{environment}/media/{mediaId}/preview/{previewType}`

*Returns image preview of the media by ID in the environment*

Returns image preview of the media by ID in the environment

<h3 id="get--api-v1-environment-{environment}-media-{mediaid}-preview-{previewtype}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|mediaId|path|string|true|ID of the media|
|previewType|path|string|true|Type of preview|

#### Enumerated Values

|Parameter|Value|
|---|---|
|previewType|highest|
|previewType|medium|
|previewType|thumbnail|

> Example responses

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": "401",
  "traceId": "00-4c7122268e63dfb01f47bd1a23507588-13f1aab74314c293-00"
}
```

<h3 id="get--api-v1-environment-{environment}-media-{mediaid}-preview-{previewtype}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success, returns file|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment, media or preview is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-templates">Templates</h1>

## get  api v1 environment {environment} templates

`GET /api/v1/environment/{environment}/templates`

*Returns all templates in the environment including subfolders*

Returns all templates in the environment including subfolders

<h3 id="get--api-v1-environment-{environment}-templates-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|nextPageToken|query|string|false|Next page token|
|limit|query|integer|false|Amount of resources per-response|
|sortBy|query|string|false|Name of field sort is based|
|sortOrder|query|string|false|Order of resources, ascending of descending|
|folder|query|string|false|Folder in which search should be done (NOTE: forward slashes only, should start with slash)|
|search|query|string|false|Search by name, relativePath or resource ID|

#### Enumerated Values

|Parameter|Value|
|---|---|
|sortBy|name|
|sortBy|id|
|sortBy|relativePath|
|sortOrder|asc|
|sortOrder|desc|

> Example responses

> 200 Response

```json
{
  "pageSize": "1",
  "data": [
    {
      "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
      "name": "Resource",
      "relativePath": "Folder",
      "extension": "jpg",
      "type": "0"
    }
  ],
  "links": {
    "nextPage": "string"
  }
}
```

<h3 id="get--api-v1-environment-{environment}-templates-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[TemplatesResponse](#schematemplatesresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|One of arguments is incorrect|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|
|410|[Gone](https://tools.ietf.org/html/rfc7231#section-6.5.9)|Next page token argument is not valid due to removed resource. Please reload previous page to get actual link to the next page|[GoneProblemDetails](#schemagoneproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post  api v1 environment {environment} templates

`POST /api/v1/environment/{environment}/templates`

*Creates a new template in the environment*

Creates a new template in the environment, takes template JSON from request body

> Body parameter

```json
"Template JSON"
```

<h3 id="post--api-v1-environment-{environment}-templates-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|name|query|string|true|Name of template|
|folderPath|query|string|true|Folder to place created template  (NOTE: forward slashes only, should start with slash)|
|body|body|any|false|Template JSON|

> Example responses

> 201 Response

```json
{
  "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
  "name": "Resource",
  "relativePath": "Folder",
  "extension": "jpg",
  "type": "0"
}
```

<h3 id="post--api-v1-environment-{environment}-templates-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Success|[Template](#schematemplate)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|One of arguments is incorrect|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Template cannot be read from request body as json|[IncorrectJsonProblemDetails](#schemaincorrectjsonproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} templates directory

`GET /api/v1/environment/{environment}/templates/directory`

*Returns all templates and directories in the environment*

Returns all templates and directories in the environment located directly in requested folder not including subfolders (in root when no folder is provided)

<h3 id="get--api-v1-environment-{environment}-templates-directory-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|nextPageToken|query|string|false|Next page token|
|limit|query|integer|false|Amount of folders per-response|
|sortBy|query|string|false|Name of field sort is based|
|sortOrder|query|string|false|Order of resources, ascending of descending|
|folder|query|string|false|Folder in which search should be done (NOTE: forward slashes only, should start with slash)|
|search|query|string|false|Search by name, relativePath or resource ID|

#### Enumerated Values

|Parameter|Value|
|---|---|
|sortBy|name|
|sortBy|id|
|sortBy|relativePath|
|sortOrder|asc|
|sortOrder|desc|

> Example responses

> 200 Response

```json
{
  "pageSize": "1",
  "data": [
    {
      "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
      "name": "Resource",
      "relativePath": "Folder",
      "extension": "jpg",
      "type": "0"
    }
  ],
  "links": {
    "nextPage": "string"
  }
}
```

<h3 id="get--api-v1-environment-{environment}-templates-directory-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[TemplatesResponse](#schematemplatesresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|One of arguments is incorrect|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} templates {templateId}

`GET /api/v1/environment/{environment}/templates/{templateId}`

*Returns template by ID in the environment*

Returns template by ID in the environment

<h3 id="get--api-v1-environment-{environment}-templates-{templateid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|templateId|path|string|true|ID of the template|

> Example responses

> 200 Response

```json
{
  "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
  "name": "Resource",
  "relativePath": "Folder",
  "extension": "jpg",
  "type": "0"
}
```

<h3 id="get--api-v1-environment-{environment}-templates-{templateid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Template](#schematemplate)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment or template is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## put  api v1 environment {environment} templates {templateId}

`PUT /api/v1/environment/{environment}/templates/{templateId}`

*Updates template by ID in the environment*

Updates template metadata (name and/or relative path) or body in the environment. Simultaneous update of body and metadata is not allowed

> Body parameter

```json
"Template JSON"
```

<h3 id="put--api-v1-environment-{environment}-templates-{templateid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|templateId|path|string|true|ID of the template|
|name|query|string|false|Name of the template|
|folderPath|query|string|false|Folder to move updated template (NOTE: forward slashes only, should start with slash)|
|body|body|any|false|Template JSON|

> Example responses

> 200 Response

```json
{
  "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
  "name": "Resource",
  "relativePath": "Folder",
  "extension": "jpg",
  "type": "0"
}
```

<h3 id="put--api-v1-environment-{environment}-templates-{templateid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Template](#schematemplate)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|One of arguments is incorrect or request contains both template body and metadata|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment or template is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Template cannot be read from request body as json|[IncorrectJsonProblemDetails](#schemaincorrectjsonproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## delete  api v1 environment {environment} templates {templateId}

`DELETE /api/v1/environment/{environment}/templates/{templateId}`

*Deletes template by ID in the environment*

Deletes template by ID in the environment

<h3 id="delete--api-v1-environment-{environment}-templates-{templateid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|templateId|path|string|true|ID of the template|

> Example responses

> 200 Response

```json
{
  "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
  "name": "Resource",
  "relativePath": "Folder",
  "extension": "jpg",
  "type": "0"
}
```

<h3 id="delete--api-v1-environment-{environment}-templates-{templateid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Template](#schematemplate)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment or template is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} templates {templateId} download

`GET /api/v1/environment/{environment}/templates/{templateId}/download`

*Downloads template by ID in the environment*

Downloads template by ID in the environment

<h3 id="get--api-v1-environment-{environment}-templates-{templateid}-download-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|templateId|path|string|true|ID of the template|

> Example responses

> 401 Response

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": "401",
  "traceId": "00-4c7122268e63dfb01f47bd1a23507588-13f1aab74314c293-00"
}
```

<h3 id="get--api-v1-environment-{environment}-templates-{templateid}-download-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success, returns file|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment or template is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} templates {templateId} preview

`GET /api/v1/environment/{environment}/templates/{templateId}/preview`

*Returns image preview of the template by ID in the environment*

Returns image preview of the template by ID in the environment, or starts new preview generation task and returns it's ID

<h3 id="get--api-v1-environment-{environment}-templates-{templateid}-preview-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|templateId|path|string|true|ID of the template|
|previewType|query|string|false|Type of preview|

#### Enumerated Values

|Parameter|Value|
|---|---|
|previewType|highest|
|previewType|medium|
|previewType|thumbnail|

> Example responses

> 202 Response

```json
{
  "data": {
    "taskId": "a19ddb23-c4db-494f-aa38-129ddc319b99"
  },
  "links": {
    "taskInfo": "string"
  }
}
```

<h3 id="get--api-v1-environment-{environment}-templates-{templateid}-preview-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success, returns file|None|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Existing preview was not found, starting a new task|[OutputTaskStartResponse](#schemaoutputtaskstartresponse)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment, template, or preview is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} templates {templateId} preview {previewType}

`GET /api/v1/environment/{environment}/templates/{templateId}/preview/{previewType}`

*Returns image preview of the template by ID in the environment*

Returns image preview of the template by ID in the environment, or starts new preview generation task and returns it's ID

<h3 id="get--api-v1-environment-{environment}-templates-{templateid}-preview-{previewtype}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|templateId|path|string|true|ID of the template|
|previewType|path|string|true|Type of preview|

#### Enumerated Values

|Parameter|Value|
|---|---|
|previewType|highest|
|previewType|medium|
|previewType|thumbnail|

> Example responses

> 202 Response

```json
{
  "data": {
    "taskId": "a19ddb23-c4db-494f-aa38-129ddc319b99"
  },
  "links": {
    "taskInfo": "string"
  }
}
```

<h3 id="get--api-v1-environment-{environment}-templates-{templateid}-preview-{previewtype}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success, returns file|None|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Existing preview was not found, starting a new task|[OutputTaskStartResponse](#schemaoutputtaskstartresponse)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment, template or preview is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} templates preview tasks {taskId}

`GET /api/v1/environment/{environment}/templates/preview/tasks/{taskId}`

*Returns preview generation task status*

Returns preview generation task status

<h3 id="get--api-v1-environment-{environment}-templates-preview-tasks-{taskid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|taskId|path|string|true|ID of the task|

> Example responses

> 200 Response

```json
{
  "data": {
    "taskId": "a19ddb23-c4db-494f-aa38-129ddc319b99"
  },
  "links": {
    "download": "string"
  }
}
```

<h3 id="get--api-v1-environment-{environment}-templates-preview-tasks-{taskid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Task is finished|[OutputTaskFinishedResponse](#schemaoutputtaskfinishedresponse)|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Task is not yet finished|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Task not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Task failed|[TaskFailedProblemDetails](#schemataskfailedproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-output">Output</h1>

## post  api v1 environment {environment} output animation

`POST /api/v1/environment/{environment}/output/animation`

*Starts animated output task*

Starts animated output task, takes template either by id or from request body

> Body parameter

```json
"Template JSON"
```

<h3 id="post--api-v1-environment-{environment}-output-animation-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|templateId|query|string|false|ID of the template|
|layoutToExport|query|string|false|Index of template layout to export|
|outputType|query|string|false|Format of the output|
|fps|query|integer|false|Framerate of the animated output (NOTE: for GIF output FPS should not exceed 50)|
|pixelRatio|query|number|false|Pixel ratio of the animated output|
|body|body|any|false|Template JSON|

#### Enumerated Values

|Parameter|Value|
|---|---|
|outputType|mp4|
|outputType|gif|

> Example responses

> 200 Response

```json
{
  "data": {
    "taskId": "a19ddb23-c4db-494f-aa38-129ddc319b99"
  },
  "links": {
    "taskInfo": "string"
  }
}
```

<h3 id="post--api-v1-environment-{environment}-output-animation-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[OutputTaskStartResponse](#schemaoutputtaskstartresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Template is not provided, or provided both by ID and body, or one of the arguments exceeds limits|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment or template is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Template cannot be read from request body as json|[IncorrectJsonProblemDetails](#schemaincorrectjsonproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## post  api v1 environment {environment} output image

`POST /api/v1/environment/{environment}/output/image`

*Starts image output task*

Starts image output task, takes template either by id or from request body

> Body parameter

```json
"Template JSON"
```

<h3 id="post--api-v1-environment-{environment}-output-image-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|templateId|query|string|false|ID of the template|
|layoutToExport|query|string|false|Index of template layout to export|
|outputType|query|string|false|Format of the output|
|pixelRatio|query|number|false|Pixel ratio of the image output|
|body|body|any|false|Template JSON|

#### Enumerated Values

|Parameter|Value|
|---|---|
|outputType|png|
|outputType|jpg|

> Example responses

> 200 Response

```json
{
  "data": {
    "taskId": "a19ddb23-c4db-494f-aa38-129ddc319b99"
  },
  "links": {
    "taskInfo": "string"
  }
}
```

<h3 id="post--api-v1-environment-{environment}-output-image-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[OutputTaskStartResponse](#schemaoutputtaskstartresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Template is not provided, or provided both by ID and body, or one of the arguments exceeds limits|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Environment or template is not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Template cannot be read from request body as json|[IncorrectJsonProblemDetails](#schemaincorrectjsonproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} output tasks {taskId}

`GET /api/v1/environment/{environment}/output/tasks/{taskId}`

*Returns task status*

Returns task status

<h3 id="get--api-v1-environment-{environment}-output-tasks-{taskid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|taskId|path|string|true|ID of the task|

> Example responses

> 200 Response

```json
{
  "data": {
    "taskId": "a19ddb23-c4db-494f-aa38-129ddc319b99"
  },
  "links": {
    "download": "string"
  }
}
```

<h3 id="get--api-v1-environment-{environment}-output-tasks-{taskid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Task is finished|[OutputTaskFinishedResponse](#schemaoutputtaskfinishedresponse)|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Task is not yet finished|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Task not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Task failed|[TaskFailedProblemDetails](#schemataskfailedproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 environment {environment} output tasks {taskId} download

`GET /api/v1/environment/{environment}/output/tasks/{taskId}/download`

*Returns task output*

Returns task output

<h3 id="get--api-v1-environment-{environment}-output-tasks-{taskid}-download-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|environment|path|string|true|Name of the environment|
|taskId|path|string|true|ID of the task|

> Example responses

> 400 Response

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.3",
  "title": "Bad Request",
  "status": "400",
  "detail": "Sorting options should not be provided when Next Page Token is provided"
}
```

<h3 id="get--api-v1-environment-{environment}-output-tasks-{taskid}-download-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success, returns file|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Task does not contain output|[BadRequestProblemDetails](#schemabadrequestproblemdetails)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[UnauthorizedProblemDetails](#schemaunauthorizedproblemdetails)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ForbiddenProblemDetails](#schemaforbiddenproblemdetails)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Task not found|[NotFoundProblemDetails](#schemanotfoundproblemdetails)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-health">Health</h1>

## get  api ping

`GET /api/ping`

*Returns empty response to check availability*

Returns empty response to check availability

<h3 id="get--api-ping-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

## get  api v1 ping

`GET /api/v1/ping`

*Returns empty response to check availability*

Returns empty response to check availability

<h3 id="get--api-v1-ping-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

<h1 id="chili-grafx-info">Info</h1>

## get  api v1 info

`GET /api/v1/info`

*Returns server info*

Returns server info

> Example responses

> 200 Response

```json
{
  "data": {
    "serverVersion": "1.0.0",
    "serverBaseDir": "/chili_data"
  },
  "links": {}
}
```

<h3 id="get--api-v1-info-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[InfoResponse](#schemainforesponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Bearer
</aside>

# Schemas

<h2 id="tocS_BaseModel">BaseModel</h2>
<!-- backwards compatibility -->
<a id="schemabasemodel"></a>
<a id="schema_BaseModel"></a>
<a id="tocSbasemodel"></a>
<a id="tocsbasemodel"></a>

```json
{
  "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
  "name": "Resource",
  "relativePath": "Folder",
  "extension": "jpg",
  "type": "0"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|ID of the resource|
|name|string|false|none|Name of the resource|
|relativePath|string|false|none|Relative path of the resource|
|extension|string¦null|false|none|Extension of the resource|
|type|integer|false|none|Type of the resource, 0 - Item, 1 - Directory|

#### Enumerated Values

|Property|Value|
|---|---|
|type|0|
|type|1|

<h2 id="tocS_Font">Font</h2>
<!-- backwards compatibility -->
<a id="schemafont"></a>
<a id="schema_Font"></a>
<a id="tocSfont"></a>
<a id="tocsfont"></a>

```json
{
  "family": "Arial",
  "style": "Regular",
  "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
  "name": "Resource",
  "relativePath": "Folder",
  "extension": "jpg",
  "type": "0"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|family|string|false|none|Font family|
|style|string|false|none|Font style|

<h2 id="tocS_Media">Media</h2>
<!-- backwards compatibility -->
<a id="schemamedia"></a>
<a id="schema_Media"></a>
<a id="tocSmedia"></a>
<a id="tocsmedia"></a>

```json
{
  "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
  "name": "Resource",
  "relativePath": "Folder",
  "extension": "jpg",
  "type": "0"
}

```

### Properties

*None*

<h2 id="tocS_Template">Template</h2>
<!-- backwards compatibility -->
<a id="schematemplate"></a>
<a id="schema_Template"></a>
<a id="tocStemplate"></a>
<a id="tocstemplate"></a>

```json
{
  "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
  "name": "Resource",
  "relativePath": "Folder",
  "extension": "jpg",
  "type": "0"
}

```

### Properties

*None*

<h2 id="tocS_MediasResponse">MediasResponse</h2>
<!-- backwards compatibility -->
<a id="schemamediasresponse"></a>
<a id="schema_MediasResponse"></a>
<a id="tocSmediasresponse"></a>
<a id="tocsmediasresponse"></a>

```json
{
  "pageSize": "1",
  "data": [
    {
      "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
      "name": "Resource",
      "relativePath": "Folder",
      "extension": "jpg",
      "type": "0"
    }
  ],
  "links": {
    "nextPage": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pageSize|integer|false|none|Count of medias at this page|
|data|[[Media](#schemamedia)]|false|none|Array of medias|
|links|object¦null|false|none|none|
|» nextPage|string|false|none|Link to the next page|

<h2 id="tocS_FontsResponse">FontsResponse</h2>
<!-- backwards compatibility -->
<a id="schemafontsresponse"></a>
<a id="schema_FontsResponse"></a>
<a id="tocSfontsresponse"></a>
<a id="tocsfontsresponse"></a>

```json
{
  "pageSize": "1",
  "data": [
    {
      "family": "Arial",
      "style": "Regular",
      "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
      "name": "Resource",
      "relativePath": "Folder",
      "extension": "jpg",
      "type": "0"
    }
  ],
  "links": {
    "nextPage": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pageSize|integer|false|none|Count of fonts at this page|
|data|[[Font](#schemafont)]|false|none|Array of fonts|
|links|object¦null|false|none|none|
|» nextPage|string|false|none|Link to the next page|

<h2 id="tocS_TemplatesResponse">TemplatesResponse</h2>
<!-- backwards compatibility -->
<a id="schematemplatesresponse"></a>
<a id="schema_TemplatesResponse"></a>
<a id="tocStemplatesresponse"></a>
<a id="tocstemplatesresponse"></a>

```json
{
  "pageSize": "1",
  "data": [
    {
      "id": "67838f82-09d6-48ad-baeb-1d7dad676c9d",
      "name": "Resource",
      "relativePath": "Folder",
      "extension": "jpg",
      "type": "0"
    }
  ],
  "links": {
    "nextPage": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pageSize|integer|false|none|Count of templates at this page|
|data|[[Template](#schematemplate)]|false|none|Array of templates|
|links|object¦null|false|none|none|
|» nextPage|string|false|none|Link to the next page|

<h2 id="tocS_UnauthorizedProblemDetails">UnauthorizedProblemDetails</h2>
<!-- backwards compatibility -->
<a id="schemaunauthorizedproblemdetails"></a>
<a id="schema_UnauthorizedProblemDetails"></a>
<a id="tocSunauthorizedproblemdetails"></a>
<a id="tocsunauthorizedproblemdetails"></a>

```json
{
  "type": "https://httpstatuses.io/401",
  "title": "Unauthorized",
  "status": "401",
  "traceId": "00-4c7122268e63dfb01f47bd1a23507588-13f1aab74314c293-00"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|false|none|none|
|title|string|false|none|none|
|status|integer|false|none|none|
|traceId|string|false|none|none|

<h2 id="tocS_ForbiddenProblemDetails">ForbiddenProblemDetails</h2>
<!-- backwards compatibility -->
<a id="schemaforbiddenproblemdetails"></a>
<a id="schema_ForbiddenProblemDetails"></a>
<a id="tocSforbiddenproblemdetails"></a>
<a id="tocsforbiddenproblemdetails"></a>

```json
{
  "type": "https://httpstatuses.io/403",
  "title": "Forbidden",
  "status": "403",
  "traceId": "00-4c7122268e63dfb01f47bd1a23507588-13f1aab74314c293-00"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|false|none|none|
|title|string|false|none|none|
|status|integer|false|none|none|
|traceId|string|false|none|none|

<h2 id="tocS_BadRequestProblemDetails">BadRequestProblemDetails</h2>
<!-- backwards compatibility -->
<a id="schemabadrequestproblemdetails"></a>
<a id="schema_BadRequestProblemDetails"></a>
<a id="tocSbadrequestproblemdetails"></a>
<a id="tocsbadrequestproblemdetails"></a>

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.3",
  "title": "Bad Request",
  "status": "400",
  "detail": "Sorting options should not be provided when Next Page Token is provided"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|false|none|none|
|title|string|false|none|none|
|status|integer|false|none|none|
|detail|integer|false|none|none|

<h2 id="tocS_NotFoundProblemDetails">NotFoundProblemDetails</h2>
<!-- backwards compatibility -->
<a id="schemanotfoundproblemdetails"></a>
<a id="schema_NotFoundProblemDetails"></a>
<a id="tocSnotfoundproblemdetails"></a>
<a id="tocsnotfoundproblemdetails"></a>

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": "404",
  "detail": "Environment 'environment' is not found"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|false|none|none|
|title|string|false|none|none|
|status|integer|false|none|none|
|detail|integer|false|none|none|

<h2 id="tocS_GoneProblemDetails">GoneProblemDetails</h2>
<!-- backwards compatibility -->
<a id="schemagoneproblemdetails"></a>
<a id="schema_GoneProblemDetails"></a>
<a id="tocSgoneproblemdetails"></a>
<a id="tocsgoneproblemdetails"></a>

```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.9",
  "title": "Gone",
  "status": "410",
  "detail": "Gone"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|false|none|none|
|title|string|false|none|none|
|status|integer|false|none|none|
|detail|integer|false|none|none|

<h2 id="tocS_TaskFailedProblemDetails">TaskFailedProblemDetails</h2>
<!-- backwards compatibility -->
<a id="schemataskfailedproblemdetails"></a>
<a id="schema_TaskFailedProblemDetails"></a>
<a id="tocStaskfailedproblemdetails"></a>
<a id="tocstaskfailedproblemdetails"></a>

```json
{
  "type": "CHILI.GraFx.EditorSdk.Wrapper.Internal.Wrappers.Editor.Internal.RenderingNotStartedCorrectlyException",
  "title": "Rendering context couldn't be read within 10 seconds.",
  "status": "500",
  "detail": "Exception details"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|false|none|none|
|title|string|false|none|none|
|status|integer|false|none|none|
|detail|integer|false|none|none|

<h2 id="tocS_IncorrectJsonProblemDetails">IncorrectJsonProblemDetails</h2>
<!-- backwards compatibility -->
<a id="schemaincorrectjsonproblemdetails"></a>
<a id="schema_IncorrectJsonProblemDetails"></a>
<a id="tocSincorrectjsonproblemdetails"></a>
<a id="tocsincorrectjsonproblemdetails"></a>

```json
{
  "type": "https://httpstatuses.io/500",
  "title": "Internal Server Error",
  "status": "500",
  "detail": "Failed to read parameter \"JsonObject templateJson\" from the request body as JSON.",
  "exceptionDetails": "Details of the exception"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|false|none|none|
|title|string|false|none|none|
|status|integer|false|none|none|
|detail|string|false|none|none|
|exceptionDetails|string|false|none|none|

<h2 id="tocS_Info">Info</h2>
<!-- backwards compatibility -->
<a id="schemainfo"></a>
<a id="schema_Info"></a>
<a id="tocSinfo"></a>
<a id="tocsinfo"></a>

```json
{
  "serverVersion": "1.0.0",
  "serverBaseDir": "/chili_data"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|serverVersion|string|false|none|none|
|serverBaseDir|string|false|none|none|

<h2 id="tocS_InfoResponse">InfoResponse</h2>
<!-- backwards compatibility -->
<a id="schemainforesponse"></a>
<a id="schema_InfoResponse"></a>
<a id="tocSinforesponse"></a>
<a id="tocsinforesponse"></a>

```json
{
  "data": {
    "serverVersion": "1.0.0",
    "serverBaseDir": "/chili_data"
  },
  "links": {}
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|data|[Info](#schemainfo)|false|none|none|
|links|object¦null|false|none|none|

<h2 id="tocS_TaskInfo">TaskInfo</h2>
<!-- backwards compatibility -->
<a id="schemataskinfo"></a>
<a id="schema_TaskInfo"></a>
<a id="tocStaskinfo"></a>
<a id="tocstaskinfo"></a>

```json
{
  "taskId": "a19ddb23-c4db-494f-aa38-129ddc319b99"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|taskId|any|false|none|ID of started task|

<h2 id="tocS_OutputTaskStartResponse">OutputTaskStartResponse</h2>
<!-- backwards compatibility -->
<a id="schemaoutputtaskstartresponse"></a>
<a id="schema_OutputTaskStartResponse"></a>
<a id="tocSoutputtaskstartresponse"></a>
<a id="tocsoutputtaskstartresponse"></a>

```json
{
  "data": {
    "taskId": "a19ddb23-c4db-494f-aa38-129ddc319b99"
  },
  "links": {
    "taskInfo": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|data|[TaskInfo](#schemataskinfo)|false|none|none|
|links|object|false|none|none|
|» taskInfo|string|false|none|Link to the task status|

<h2 id="tocS_OutputTaskFinishedResponse">OutputTaskFinishedResponse</h2>
<!-- backwards compatibility -->
<a id="schemaoutputtaskfinishedresponse"></a>
<a id="schema_OutputTaskFinishedResponse"></a>
<a id="tocSoutputtaskfinishedresponse"></a>
<a id="tocsoutputtaskfinishedresponse"></a>

```json
{
  "data": {
    "taskId": "a19ddb23-c4db-494f-aa38-129ddc319b99"
  },
  "links": {
    "download": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|data|[TaskInfo](#schemataskinfo)|false|none|none|
|links|object|false|none|none|
|» download|string|false|none|Link to download task result|

