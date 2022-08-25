[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [controllers/LayoutController](../modules/controllers_LayoutController.md) / LayoutController

# Class: LayoutController

[controllers/LayoutController](../modules/controllers_LayoutController.md).LayoutController

The LayoutController is responsible for all communication regarding Layouts.
Methods inside this controller can be called by `window.SDK.layout.{method-name}`

## Methods

### addLayout

▸ **addLayout**(`parentId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will add a new child layout (a new layout is always child of a root / parentlayout)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `parentId` | `number` | The ID of a specific layout, being the parent |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:74](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L74)

___

### duplicateLayout

▸ **duplicateLayout**(`layoutId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will duplicate a specific layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:105](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L105)

___

### getLayoutById

▸ **getLayoutById**(`id`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns a layout by its id

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:35](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L35)

___

### getLayoutByName

▸ **getLayoutByName**(`name`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns a layout by its name

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | The name of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:45](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L45)

___

### getLayouts

▸ **getLayouts**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns the list of layouts

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:25](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L25)

___

### getSelectedLayout

▸ **getSelectedLayout**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns the selected layout

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:54](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L54)

___

### removeLayout

▸ **removeLayout**(`layoutId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will remove a specific layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:64](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L64)

___

### resetLayout

▸ **resetLayout**(`layoutId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will reset a specific layout to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:115](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L115)

___

### resetLayoutHeight

▸ **resetLayoutHeight**(`layoutId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will reset the height of a specific layout to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:156](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L156)

___

### resetLayoutWidth

▸ **resetLayoutWidth**(`layoutId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will reset the width of a specific layout to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:166](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L166)

___

### selectLayout

▸ **selectLayout**(`layoutId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will select a specific layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:95](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L95)

___

### setLayoutHeight

▸ **setLayoutHeight**(`layoutId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

This method will set the height of the layout to a specific value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:126](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L126)

___

### setLayoutName

▸ **setLayoutName**(`layoutId`, `layoutName`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will update the name of a specific layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |
| `layoutName` | `string` | The new name that the layout should receive |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:85](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L85)

___

### setLayoutWidth

▸ **setLayoutWidth**(`layoutId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

This method will set the width of the layout to a specific value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/LayoutController.ts:141](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/LayoutController.ts#L141)
