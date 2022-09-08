# Class: DocumentController

[controllers/DocumentController](../modules/controllers_DocumentController.md).DocumentController

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

▸ **getCurrentDocumentState**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method retrieves the current document state from the editor

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

The JSON document in the form of a string

#### Defined in

[src/controllers/DocumentController.ts:28](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/DocumentController.ts#L28)

___

### getDownloadLink

▸ **getDownloadLink**(`format`, `layoutId`): `Promise`<{ `data`: ``null`` = null; `error`: ``null`` ; `status`: `any` = response.status; `success`: `boolean` = false } \| { `data`: ``null`` = null; `error`: [`DocumentError`](../modules/index.md#documenterror) ; `status`: `number` ; `success`: `boolean` = false } \| { `data`: ``null`` \| `string` = DOWNLOAD\_URL; `error`: `undefined` ; `status`: `number` = 200; `success`: `boolean` = true }\>

This method will call an external api to create a download url
The video will be generated in the dimensions (and resolution) of the layout.
This means that any upscaling (e.g. playing the video full screen on a 4k monitor) will result in interpolation (= quality loss).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `format` | [`DownloadFormats`](../enums/index.DownloadFormats.md) | The format of a downloadable url |
| `layoutId` | `number` | id of layout to be downloaded |

#### Returns

`Promise`<{ `data`: ``null`` = null; `error`: ``null`` ; `status`: `any` = response.status; `success`: `boolean` = false } \| { `data`: ``null`` = null; `error`: [`DocumentError`](../modules/index.md#documenterror) ; `status`: `number` ; `success`: `boolean` = false } \| { `data`: ``null`` \| `string` = DOWNLOAD\_URL; `error`: `undefined` ; `status`: `number` = 200; `success`: `boolean` = true }\>

the download link

#### Defined in

[src/controllers/DocumentController.ts:51](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/DocumentController.ts#L51)

___

### loadDocument

▸ **loadDocument**(`documentJson`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will load a provided document

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `documentJson` | `string` | The document to load in string format |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

The document loaded inside of the canvas

#### Defined in

[src/controllers/DocumentController.ts:38](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/DocumentController.ts#L38)

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

[src/controllers/DocumentController.ts:127](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/DocumentController.ts#L127)
