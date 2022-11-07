[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/MediaConnectorController](../modules/controllers_MediaConnectorController.md) / MediaConnectorController

# Class: MediaConnectorController

[src/controllers/MediaConnectorController](../modules/controllers_MediaConnectorController.md).MediaConnectorController

The MediaConnectorController is responsible for all communication regarding media connectors.
Methods inside this controller can be called by `window.SDK.mediaConnector.{method-name}`

The way CHILI Studio handles different sources of media is called 'MediaConnectors'. A MediaConnectors is an
implementation of a set of capabilities we need to interact with a certain Digital Asset Management system.
In essence a connector is the combination of a Javascript snippet and some metadata. The Javascript snippet
is loaded in the studio engine using a sandboxed Javascript execution engine (QuickJs). This allows us to
execute the media connector both on web using webassembly and on the server side during e.g. animation output
generation.
This controller is an interface to the running connector instance inside the studio engine.

## Table of contents

### Methods

- [copy](controllers_MediaConnectorController.MediaConnectorController.md#copy)
- [download](controllers_MediaConnectorController.MediaConnectorController.md#download)
- [getCapabilities](controllers_MediaConnectorController.MediaConnectorController.md#getcapabilities)
- [getDownloadOptions](controllers_MediaConnectorController.MediaConnectorController.md#getdownloadoptions)
- [getQueryOptions](controllers_MediaConnectorController.MediaConnectorController.md#getqueryoptions)
- [parseDeprecatedMediaType](controllers_MediaConnectorController.MediaConnectorController.md#parsedeprecatedmediatype)
- [query](controllers_MediaConnectorController.MediaConnectorController.md#query)
- [remove](controllers_MediaConnectorController.MediaConnectorController.md#remove)
- [upload](controllers_MediaConnectorController.MediaConnectorController.md#upload)

## Methods

### copy

▸ **copy**(`connectorId`, `mediaId`, `newName`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

Depending on the connector capabilities, copies media identified by `mediaId` to a new media item on the
connector's backend

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectorId` | `string` | unique Id of the media connector |
| `mediaId` | `string` | unique Id of the media to download |
| `newName` | `string` | name of the copied media on the connector's backend |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/MediaConnectorController.ts:100](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/MediaConnectorController.ts#L100)

___

### download

▸ **download**(`connectorId`, `mediaId`, `downloadType`, `context`): `Promise`<`Uint8Array`\>

The combination of a `connectorId` and `mediaId` is typically enough for a media connector to
perform the download of this asset. The `download` endpoint is capable of relaying this information to the
media connector instance running in the editor engine.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectorId` | `string` | unique Id of the media connector |
| `mediaId` | `string` | unique Id of the media to download |
| `downloadType` | [`MediaDownloadType`](../enums/types_MediaConnectorTypes.MediaDownloadType.md) | hint to the media connector about desired quality of the downloaded media |
| `context` | [`MetaData`](../interfaces/src.MetaData.md) | dynamic map of additional options potentially used by the connector |

#### Returns

`Promise`<`Uint8Array`\>

#### Defined in

[src/controllers/MediaConnectorController.ts:57](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/MediaConnectorController.ts#L57)

___

### getCapabilities

▸ **getCapabilities**(`connectorId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`ConnectorCapabilities`\>\>

This method returns what capabilities the selected connector has. It gives an indication what methods can
be used successfully for a certain connector.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectorId` | `string` | unique Id of the media connector |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`ConnectorCapabilities`\>\>

#### Defined in

[src/controllers/MediaConnectorController.ts:138](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/MediaConnectorController.ts#L138)

___

### getDownloadOptions

▸ **getDownloadOptions**(`connectorId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`ConnectorOptions`\>\>

All connectors have a certain set of downloadOptions they allow to be passed in the download context. This
method allows you to discover what options are available for a given connector. If you want to use any of these
options, they need to be passed in the `context` parameter of the `download` api method.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectorId` | `string` | unique Id of the media connector |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`ConnectorOptions`\>\>

#### Defined in

[src/controllers/MediaConnectorController.ts:126](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/MediaConnectorController.ts#L126)

___

### getQueryOptions

▸ **getQueryOptions**(`connectorId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`ConnectorOptions`\>\>

All connectors have a certain set of queryOptions they allow to be passed in the query context. This
method allows you to discover what options are available for a given connector. If you want to use any of these
options, they need to be passed in the `context` parameter of the `query` api method.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectorId` | `string` | unique Id of the media connector |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`ConnectorOptions`\>\>

#### Defined in

[src/controllers/MediaConnectorController.ts:113](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/MediaConnectorController.ts#L113)

___

### parseDeprecatedMediaType

▸ **parseDeprecatedMediaType**(`deprecatedType`): `undefined` \| [`file`](../enums/src.MediaType.md#file) \| [`collection`](../enums/src.MediaType.md#collection)

This method will parse the deprecatedMediaType to the new media type. This method will be removed once the deprecatedMediaType is out of use

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `deprecatedType` | `DeprecatedMediaType` | is 0 or 1 |

#### Returns

`undefined` \| [`file`](../enums/src.MediaType.md#file) \| [`collection`](../enums/src.MediaType.md#collection)

#### Defined in

[src/controllers/MediaConnectorController.ts:149](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/MediaConnectorController.ts#L149)

___

### query

▸ **query**(`connectorId`, `queryOptions`, `context`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`MediaPage`](../modules/types_MediaConnectorTypes.md#mediapage)\>\>

Query a specific MediaConnector for data using both standardized queryOptions and the dynamic
context as parameters. This call returns an array of Media items.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectorId` | `string` | unique Id of the media connector |
| `queryOptions` | [`QueryOptions`](../modules/src.md#queryoptions) | stringified instance of `QueryOptions` |
| `context` | [`MetaData`](../interfaces/src.MetaData.md) | stringified `Map<string, string>` of dynamic options |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`MediaPage`](../modules/types_MediaConnectorTypes.md#mediapage)\>\>

#### Defined in

[src/controllers/MediaConnectorController.ts:41](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/MediaConnectorController.ts#L41)

___

### remove

▸ **remove**(`connectorId`, `mediaId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

Depending on the connector capabilities, removes media identified by `mediaId` from the connector's backend storage

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectorId` | `string` | unique Id of the media connector |
| `mediaId` | `string` | unique Id of the media to download |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/MediaConnectorController.ts:88](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/MediaConnectorController.ts#L88)

___

### upload

▸ **upload**(`connectorId`, `mediaId`, `blob`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

Depending on the connector capabilities, this api method allows you to upload new media to the
connector's backend.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `connectorId` | `string` | unique Id of the media connector |
| `mediaId` | `string` | unique Id of the media to upload |
| `blob` | `Uint8Array` | byte array representation of the media to upload |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/MediaConnectorController.ts:76](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/MediaConnectorController.ts#L76)
