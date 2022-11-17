[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/DocumentController](../modules/controllers_DocumentController.md) / DocumentController

# Class: DocumentController

[src/controllers/DocumentController](../modules/controllers_DocumentController.md).DocumentController

The DocumentController is responsible for all communication regarding the Document.
Methods inside this controller can be called by `window.SDK.document.{method-name}`

## Table of contents

### Methods

- [getCurrentDocumentState](controllers_DocumentController.DocumentController.md#getcurrentdocumentstate)
- [getDownloadLink](controllers_DocumentController.DocumentController.md#getdownloadlink)
- [loadDocument](controllers_DocumentController.DocumentController.md#loaddocument)
- [startPollingOnEndpoint](controllers_DocumentController.DocumentController.md#startpollingonendpoint)

## Methods

### getCurrentDocumentState

▸ **getCurrentDocumentState**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`ChiliDocument`](../interfaces/types_DocumentTypes.ChiliDocument.md)\>\>

This method retrieves the current document state from the editor

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`ChiliDocument`](../interfaces/types_DocumentTypes.ChiliDocument.md)\>\>

The JSON document in the form of a string

#### Defined in

[src/controllers/DocumentController.ts:29](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/DocumentController.ts#L29)

___

### getDownloadLink

▸ **getDownloadLink**(`format`, `layoutId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

This method will call an external api to create a download url
The video will be generated in the dimensions (and resolution) of the layout.
This means that any upscaling (e.g. playing the video full screen on a 4k monitor) will result in interpolation (= quality loss).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `format` | [`DownloadFormats`](../enums/src.DownloadFormats.md) | The format of a downloadable url |
| `layoutId` | `number` | id of layout to be downloaded |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

the download link

#### Defined in

[src/controllers/DocumentController.ts:53](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/DocumentController.ts#L53)

___

### loadDocument

▸ **loadDocument**(`doc`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`unknown`\>\>

This method will load a provided document in the ChiliDocument format

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `doc` | `string` \| [`ChiliDocument`](../interfaces/types_DocumentTypes.ChiliDocument.md) | The document to load in |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`unknown`\>\>

The document loaded inside of the canvas

#### Defined in

[src/controllers/DocumentController.ts:39](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/DocumentController.ts#L39)

___

### startPollingOnEndpoint

▸ **startPollingOnEndpoint**(`endpoint`): `Promise`<`unknown`\>

This method will call an external api endpoint, untill the api endpoint returns a status code 200

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `endpoint` | `string` | api endpoint to start polling on |

#### Returns

`Promise`<`unknown`\>

true when the endpoint call has successfully been resolved

#### Defined in

[src/controllers/DocumentController.ts:143](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/DocumentController.ts#L143)
