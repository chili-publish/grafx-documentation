# Class: ParagraphStyleController

[controllers/ParagraphStyleController](../modules/controllers_ParagraphStyleController.md).ParagraphStyleController

The ParagraphStyleController is responsible for all communication regarding paragraph styles.
Methods inside this controller can be called by `window.SDK.paragraphStyle.{method-name}`

## Table of contents

### Methods

- [createParagraphStyle](controllers_ParagraphStyleController.ParagraphStyleController.md#createparagraphstyle)
- [duplicateParagraphStyle](controllers_ParagraphStyleController.ParagraphStyleController.md#duplicateparagraphstyle)
- [getParagraphStyleById](controllers_ParagraphStyleController.ParagraphStyleController.md#getparagraphstylebyid)
- [getParagraphStyles](controllers_ParagraphStyleController.ParagraphStyleController.md#getparagraphstyles)
- [moveParagraphStyles](controllers_ParagraphStyleController.ParagraphStyleController.md#moveparagraphstyles)
- [removeParagraphStyle](controllers_ParagraphStyleController.ParagraphStyleController.md#removeparagraphstyle)
- [renameParagraphStyle](controllers_ParagraphStyleController.ParagraphStyleController.md#renameparagraphstyle)
- [updateParagraphStyle](controllers_ParagraphStyleController.ParagraphStyleController.md#updateparagraphstyle)

## Methods

### createParagraphStyle

▸ **createParagraphStyle**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method create a new paragraph style

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

the new created paragraph style id

#### Defined in

[src/controllers/ParagraphStyleController.ts:44](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ParagraphStyleController.ts#L44)

___

### duplicateParagraphStyle

▸ **duplicateParagraphStyle**(`paragraphStyleId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method duplicates a paragraph style

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `paragraphStyleId` | `string` | The ID of a specific paragraph style |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

the new paragraph style id

#### Defined in

[src/controllers/ParagraphStyleController.ts:54](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ParagraphStyleController.ts#L54)

___

### getParagraphStyleById

▸ **getParagraphStyleById**(`paragraphStyleId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns a paragraph style by id

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `paragraphStyleId` | `string` | The ID of a specific paragraph style |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:35](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ParagraphStyleController.ts#L35)

___

### getParagraphStyles

▸ **getParagraphStyles**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns the list of paragraph styles

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:25](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ParagraphStyleController.ts#L25)

___

### moveParagraphStyles

▸ **moveParagraphStyles**(`order`, `paragraphStyleIds`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method changes positions of paragraph styles

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `order` | `number` | The position of the paragraph styles |
| `paragraphStyleIds` | `string`[] | The list of paragraph styles ids |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:97](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ParagraphStyleController.ts#L97)

___

### removeParagraphStyle

▸ **removeParagraphStyle**(`id`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method removes a paragraph style

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of a specific paragraph style |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:86](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ParagraphStyleController.ts#L86)

___

### renameParagraphStyle

▸ **renameParagraphStyle**(`id`, `name`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method renames a paragraph style

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of a specific paragraph style |
| `name` | `string` | The new name of the paragraph style |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:76](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ParagraphStyleController.ts#L76)

___

### updateParagraphStyle

▸ **updateParagraphStyle**(`id`, `paragraphStyle`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method updates a paragraph style

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of a specific paragraph style |
| `paragraphStyle` | [`ParagraphStyleUpdate`](../modules/index.md#paragraphstyleupdate) | The new paragraph style properties |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:65](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ParagraphStyleController.ts#L65)
