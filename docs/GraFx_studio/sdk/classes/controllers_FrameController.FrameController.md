# Class: FrameController

[controllers/FrameController](../modules/controllers_FrameController.md).FrameController

The FrameController is responsible for all communication regarding Frames.
Methods inside this controller can be called by `window.SDK.frame.{method-name}`

## Table of contents

### Methods

- [getFrameById](controllers_FrameController.FrameController.md#getframebyid)
- [getFrameByName](controllers_FrameController.FrameController.md#getframebyname)
- [getFramePropertiesByFrameId](controllers_FrameController.FrameController.md#getframepropertiesbyframeid)
- [getFramePropertiesOnSelectedLayout](controllers_FrameController.FrameController.md#getframepropertiesonselectedlayout)
- [getFrames](controllers_FrameController.FrameController.md#getframes)
- [getFramesByPageId](controllers_FrameController.FrameController.md#getframesbypageid)
- [getFramesProperties](controllers_FrameController.FrameController.md#getframesproperties)
- [getSelectedFrames](controllers_FrameController.FrameController.md#getselectedframes)
- [removeFrame](controllers_FrameController.FrameController.md#removeframe)
- [resetFrame](controllers_FrameController.FrameController.md#resetframe)
- [resetFrameHeight](controllers_FrameController.FrameController.md#resetframeheight)
- [resetFrameRotation](controllers_FrameController.FrameController.md#resetframerotation)
- [resetFrameSize](controllers_FrameController.FrameController.md#resetframesize)
- [resetFrameWidth](controllers_FrameController.FrameController.md#resetframewidth)
- [resetFrameX](controllers_FrameController.FrameController.md#resetframex)
- [resetFrameY](controllers_FrameController.FrameController.md#resetframey)
- [selectFrame](controllers_FrameController.FrameController.md#selectframe)
- [selectMultipleFrames](controllers_FrameController.FrameController.md#selectmultipleframes)
- [setFrameHeight](controllers_FrameController.FrameController.md#setframeheight)
- [setFrameName](controllers_FrameController.FrameController.md#setframename)
- [setFrameRotation](controllers_FrameController.FrameController.md#setframerotation)
- [setFrameVisibility](controllers_FrameController.FrameController.md#setframevisibility)
- [setFrameWidth](controllers_FrameController.FrameController.md#setframewidth)
- [setFrameX](controllers_FrameController.FrameController.md#setframex)
- [setFrameY](controllers_FrameController.FrameController.md#setframey)

## Methods

### getFrameById

▸ **getFrameById**(`id`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns a frame by its id

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `number` | The ID of a specific frame |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:64](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L64)

___

### getFrameByName

▸ **getFrameByName**(`name`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns a frame by its name

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | The name of a specific frame |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:54](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L54)

___

### getFramePropertiesByFrameId

▸ **getFramePropertiesByFrameId**(`frameId`, `layoutId?`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns frame properties for a given frame and layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `layoutId?` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:84](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L84)

___

### getFramePropertiesOnSelectedLayout

▸ **getFramePropertiesOnSelectedLayout**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns all frame properties on current layout

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:73](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L73)

___

### getFrames

▸ **getFrames**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns the list of frames

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:25](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L25)

___

### getFramesByPageId

▸ **getFramesByPageId**(`pageId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns the list of frames by pageId

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `pageId` | `number` | The ID of a specific page |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:44](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L44)

___

### getFramesProperties

▸ **getFramesProperties**(`layoutId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns frame properties for a given layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:94](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L94)

___

### getSelectedFrames

▸ **getSelectedFrames**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns the list of selected frames

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:34](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L34)

___

### removeFrame

▸ **removeFrame**(`frameId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will remove a specific frame using the Id.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to be deleted |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:296](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L296)

___

### resetFrame

▸ **resetFrame**(`frameId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will reset properties of a specific frame to their original values

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:226](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L226)

___

### resetFrameHeight

▸ **resetFrameHeight**(`frameId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will reset the height of a specific frame to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:275](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L275)

___

### resetFrameRotation

▸ **resetFrameRotation**(`frameId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will reset the rotation value of a specific frame to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:255](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L255)

___

### resetFrameSize

▸ **resetFrameSize**(`frameId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will reset the frame size (width and height) to the frame's original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:104](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L104)

___

### resetFrameWidth

▸ **resetFrameWidth**(`frameId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will reset the width of a specific frame to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:265](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L265)

___

### resetFrameX

▸ **resetFrameX**(`frameId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will reset the x value of a specific frame to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:235](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L235)

___

### resetFrameY

▸ **resetFrameY**(`frameId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will reset the y value of a specific frame to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:245](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L245)

___

### selectFrame

▸ **selectFrame**(`frameId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will select a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:114](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L114)

___

### selectMultipleFrames

▸ **selectMultipleFrames**(`frameIds`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will select multipleFrames

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameIds` | `number`[] | An array of all IDs you want to select |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:124](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L124)

___

### setFrameHeight

▸ **setFrameHeight**(`frameId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

This method will set the height of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:135](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L135)

___

### setFrameName

▸ **setFrameName**(`frameId`, `frameName`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will update the name of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `frameName` | `string` | The new name that the frame should receive |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:216](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L216)

___

### setFrameRotation

▸ **setFrameRotation**(`frameId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

This method will set the rotation angle of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:151](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L151)

___

### setFrameVisibility

▸ **setFrameVisibility**(`frameId`, `value`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method will set the visibility property of a specified frame. If set to false the frame will be invisible and vice versa.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get updated |
| `value` | `boolean` | True means the frame gets visible, false means the frame gets invisible |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:286](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L286)

___

### setFrameWidth

▸ **setFrameWidth**(`frameId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

This method will set the width of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:167](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L167)

___

### setFrameX

▸ **setFrameX**(`frameId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

This method will set the x value of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:183](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L183)

___

### setFrameY

▸ **setFrameY**(`frameId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

This method will set the y value of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/FrameController.ts:199](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/FrameController.ts#L199)
