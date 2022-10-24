[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/PageController](../modules/controllers_PageController.md) / PageController

# Class: PageController

[src/controllers/PageController](../modules/controllers_PageController.md).PageController

The PageController is responsible for all communication regarding Pages.
Methods inside this controller can be called by `window.SDK.page.{method-name}`

## Table of contents

### Methods

- [getPageById](controllers_PageController.PageController.md#getpagebyid)
- [getPages](controllers_PageController.PageController.md#getpages)

## Methods

### getPageById

▸ **getPageById**(`pageId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Page`\>\>

This method returns a page by its id

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `pageId` | `number` | The ID of a specific page |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Page`\>\>

#### Defined in

[src/controllers/PageController.ts:36](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/PageController.ts#L36)

___

### getPages

▸ **getPages**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Page`[]\>\>

This method returns the list of pages

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Page`[]\>\>

#### Defined in

[src/controllers/PageController.ts:26](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/PageController.ts#L26)
