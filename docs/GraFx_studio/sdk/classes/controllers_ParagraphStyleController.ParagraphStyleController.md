[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/ParagraphStyleController](../modules/controllers_ParagraphStyleController.md) / ParagraphStyleController

# Class: ParagraphStyleController

[src/controllers/ParagraphStyleController](../modules/controllers_ParagraphStyleController.md).ParagraphStyleController

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

▸ **createParagraphStyle**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

This method create a new paragraph style

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

the new created paragraph style id

#### Defined in

[src/controllers/ParagraphStyleController.ts:47](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ParagraphStyleController.ts#L47)

___

### duplicateParagraphStyle

▸ **duplicateParagraphStyle**(`paragraphStyleId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

This method duplicates a paragraph style

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `paragraphStyleId` | `string` | The ID of a specific paragraph style |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

the new paragraph style id

#### Defined in

[src/controllers/ParagraphStyleController.ts:57](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ParagraphStyleController.ts#L57)

___

### getParagraphStyleById

▸ **getParagraphStyleById**(`paragraphStyleId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`ParagraphStyle`](../modules/src.md#paragraphstyle)\>\>

This method returns a paragraph style by id

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `paragraphStyleId` | `string` | The ID of a specific paragraph style |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`ParagraphStyle`](../modules/src.md#paragraphstyle)\>\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:36](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ParagraphStyleController.ts#L36)

___

### getParagraphStyles

▸ **getParagraphStyles**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`ParagraphStyle`](../modules/src.md#paragraphstyle)[]\>\>

This method returns the list of paragraph styles

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`ParagraphStyle`](../modules/src.md#paragraphstyle)[]\>\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:26](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ParagraphStyleController.ts#L26)

___

### moveParagraphStyles

▸ **moveParagraphStyles**(`order`, `paragraphStyleIds`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method changes positions of paragraph styles

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `order` | `number` | The position of the paragraph styles |
| `paragraphStyleIds` | `string`[] | The list of paragraph styles ids |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:102](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ParagraphStyleController.ts#L102)

___

### removeParagraphStyle

▸ **removeParagraphStyle**(`id`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method removes a paragraph style

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of a specific paragraph style |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:91](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ParagraphStyleController.ts#L91)

___

### renameParagraphStyle

▸ **renameParagraphStyle**(`id`, `name`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method renames a paragraph style

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of a specific paragraph style |
| `name` | `string` | The new name of the paragraph style |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:81](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ParagraphStyleController.ts#L81)

___

### updateParagraphStyle

▸ **updateParagraphStyle**(`id`, `paragraphStyle`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method updates a paragraph style

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of a specific paragraph style |
| `paragraphStyle` | [`ParagraphStyleUpdate`](../modules/src.md#paragraphstyleupdate) | The new paragraph style properties |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/ParagraphStyleController.ts:68](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ParagraphStyleController.ts#L68)
