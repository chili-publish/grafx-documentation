[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/TextStyleController](../modules/controllers_TextStyleController.md) / TextStyleController

# Class: TextStyleController

[src/controllers/TextStyleController](../modules/controllers_TextStyleController.md).TextStyleController

The TextStyleController is responsible for all communication regarding text styles.
Methods inside this controller can be called by `window.SDK.textStyle.{method-name}`

## Table of contents

### Methods

- [setTextStyleProperties](controllers_TextStyleController.TextStyleController.md#settextstyleproperties)

## Methods

### setTextStyleProperties

▸ **setTextStyleProperties**(`style`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method updates a selected Text's style properties

#### Parameters

| Name | Type |
| :------ | :------ |
| `style` | [`TextStyleUpdateType`](../modules/src.md#textstyleupdatetype) |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/TextStyleController.ts:25](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/TextStyleController.ts#L25)
