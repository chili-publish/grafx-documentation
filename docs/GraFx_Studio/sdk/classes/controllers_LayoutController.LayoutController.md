[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/LayoutController](../modules/controllers_LayoutController.md) / LayoutController

# Class: LayoutController

[src/controllers/LayoutController](../modules/controllers_LayoutController.md).LayoutController

The LayoutController is responsible for all communication regarding Layouts.
Methods inside this controller can be called by `window.SDK.layout.{method-name}`

## Table of contents

### Methods

- [addLayout](controllers_LayoutController.LayoutController.md#addlayout)
- [duplicateLayout](controllers_LayoutController.LayoutController.md#duplicatelayout)
- [getLayoutById](controllers_LayoutController.LayoutController.md#getlayoutbyid)
- [getLayoutByName](controllers_LayoutController.LayoutController.md#getlayoutbyname)
- [getLayouts](controllers_LayoutController.LayoutController.md#getlayouts)
- [getSelectedLayout](controllers_LayoutController.LayoutController.md#getselectedlayout)
- [removeLayout](controllers_LayoutController.LayoutController.md#removelayout)
- [resetLayout](controllers_LayoutController.LayoutController.md#resetlayout)
- [resetLayoutHeight](controllers_LayoutController.LayoutController.md#resetlayoutheight)
- [resetLayoutWidth](controllers_LayoutController.LayoutController.md#resetlayoutwidth)
- [selectLayout](controllers_LayoutController.LayoutController.md#selectlayout)
- [setLayoutHeight](controllers_LayoutController.LayoutController.md#setlayoutheight)
- [setLayoutName](controllers_LayoutController.LayoutController.md#setlayoutname)
- [setLayoutWidth](controllers_LayoutController.LayoutController.md#setlayoutwidth)

## Methods

### addLayout

▸ **addLayout**(`parentId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`number`\>\>

This method will add a new child layout (a new layout is always child of a root / parentlayout)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `parentId` | `number` | The ID of a specific layout, being the parent |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`number`\>\>

#### Defined in

[src/controllers/LayoutController.ts:76](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L76)

___

### duplicateLayout

▸ **duplicateLayout**(`layoutId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`number`\>\>

This method will duplicate a specific layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`number`\>\>

#### Defined in

[src/controllers/LayoutController.ts:107](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L107)

___

### getLayoutById

▸ **getLayoutById**(`id`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Layout`\>\>

This method returns a layout by its id

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Layout`\>\>

#### Defined in

[src/controllers/LayoutController.ts:37](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L37)

___

### getLayoutByName

▸ **getLayoutByName**(`name`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Layout`\>\>

This method returns a layout by its name

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | The name of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Layout`\>\>

#### Defined in

[src/controllers/LayoutController.ts:47](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L47)

___

### getLayouts

▸ **getLayouts**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Layout`[]\>\>

This method returns the list of layouts

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Layout`[]\>\>

#### Defined in

[src/controllers/LayoutController.ts:27](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L27)

___

### getSelectedLayout

▸ **getSelectedLayout**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Layout`\>\>

This method returns the selected layout

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`Layout`\>\>

#### Defined in

[src/controllers/LayoutController.ts:56](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L56)

___

### removeLayout

▸ **removeLayout**(`layoutId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will remove a specific layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/LayoutController.ts:66](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L66)

___

### resetLayout

▸ **resetLayout**(`layoutId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will reset a specific layout to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/LayoutController.ts:117](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L117)

___

### resetLayoutHeight

▸ **resetLayoutHeight**(`layoutId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will reset the height of a specific layout to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/LayoutController.ts:162](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L162)

___

### resetLayoutWidth

▸ **resetLayoutWidth**(`layoutId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will reset the width of a specific layout to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/LayoutController.ts:172](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L172)

___

### selectLayout

▸ **selectLayout**(`layoutId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will select a specific layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/LayoutController.ts:97](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L97)

___

### setLayoutHeight

▸ **setLayoutHeight**(`layoutId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will set the height of the layout to a specific value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/LayoutController.ts:128](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L128)

___

### setLayoutName

▸ **setLayoutName**(`layoutId`, `layoutName`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will update the name of a specific layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |
| `layoutName` | `string` | The new name that the layout should receive |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/LayoutController.ts:87](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L87)

___

### setLayoutWidth

▸ **setLayoutWidth**(`layoutId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will set the width of the layout to a specific value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/LayoutController.ts:145](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/LayoutController.ts#L145)
