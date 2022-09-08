# Class: TextStyleController

[controllers/TextStyleController](../modules/controllers_TextStyleController.md).TextStyleController

The TextStyleController is responsible for all communication regarding text styles.
Methods inside this controller can be called by `window.SDK.textStyle.{method-name}`

## Table of contents

### Methods

- [setTextStyleProperties](controllers_TextStyleController.TextStyleController.md#settextstyleproperties)

## Methods

### setTextStyleProperties

▸ **setTextStyleProperties**(`style`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method updates a selected Text's style properties

#### Parameters

| Name | Type |
| :------ | :------ |
| `style` | [`TextStyleUpdateType`](../modules/index.md#textstyleupdatetype) |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/TextStyleController.ts:24](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/TextStyleController.ts#L24)
