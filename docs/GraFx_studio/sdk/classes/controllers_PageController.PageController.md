# Class: PageController

[controllers/PageController](../modules/controllers_PageController.md).PageController

The PageController is responsible for all communication regarding Pages.
Methods inside this controller can be called by `window.SDK.page.{method-name}`

## Table of contents

### Methods

- [getPageById](controllers_PageController.PageController.md#getpagebyid)
- [getPages](controllers_PageController.PageController.md#getpages)

## Methods

### getPageById

▸ **getPageById**(`pageId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns a page by its id

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `pageId` | `number` | The ID of a specific page |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/PageController.ts:34](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/PageController.ts#L34)

___

### getPages

▸ **getPages**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns the list of pages

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/PageController.ts:24](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/PageController.ts#L24)
