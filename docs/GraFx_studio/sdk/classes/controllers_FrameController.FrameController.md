[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/FrameController](../modules/controllers_FrameController.md) / FrameController

# Class: FrameController

[src/controllers/FrameController](../modules/controllers_FrameController.md).FrameController

The FrameController is responsible for all communication regarding Frames.
Methods inside this controller can be called by `window.SDK.frame.{method-name}`

## Table of contents

### Methods

- [addFrame](controllers_FrameController.FrameController.md#addframe)
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
- [setImageFrameFitMode](controllers_FrameController.FrameController.md#setimageframefitmode)
- [setImageFromConnector](controllers_FrameController.FrameController.md#setimagefromconnector)
- [setVerticalAlignment](controllers_FrameController.FrameController.md#setverticalalignment)

## Methods

### addFrame

▸ **addFrame**(`frameType`, `x`, `y`, `width`, `height`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`number`\>\>

This method will add a new frame of 'frameType' to the template positioned on the requested
coordinates.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameType` | [`FrameTypeEnum`](../enums/src.FrameTypeEnum.md) | The type of frame to create |
| `x` | `number` | X coordinate of the new frame within the template |
| `y` | `number` | Y coordinate of the new frame within the template |
| `width` | `number` | Width of the new frame within the template |
| `height` | `number` | Height of the new frame within the template |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`number`\>\>

The newly created frame's ID

#### Defined in

[src/controllers/FrameController.ts:326](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L326)

___

### getFrameById

▸ **getFrameById**(`id`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameType`](../modules/src.md#frametype)\>\>

This method returns a frame by its id

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `number` | The ID of a specific frame |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameType`](../modules/src.md#frametype)\>\>

#### Defined in

[src/controllers/FrameController.ts:66](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L66)

___

### getFrameByName

▸ **getFrameByName**(`name`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameType`](../modules/src.md#frametype)\>\>

This method returns a frame by its name

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | The name of a specific frame |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameType`](../modules/src.md#frametype)\>\>

#### Defined in

[src/controllers/FrameController.ts:56](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L56)

___

### getFramePropertiesByFrameId

▸ **getFramePropertiesByFrameId**(`frameId`, `layoutId?`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameLayoutType`](../modules/src.md#framelayouttype)\>\>

This method returns frame properties for a given frame and layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `layoutId?` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameLayoutType`](../modules/src.md#framelayouttype)\>\>

#### Defined in

[src/controllers/FrameController.ts:88](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L88)

___

### getFramePropertiesOnSelectedLayout

▸ **getFramePropertiesOnSelectedLayout**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameLayoutType`](../modules/src.md#framelayouttype)[]\>\>

This method returns all frame properties on current layout

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameLayoutType`](../modules/src.md#framelayouttype)[]\>\>

#### Defined in

[src/controllers/FrameController.ts:75](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L75)

___

### getFrames

▸ **getFrames**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameType`](../modules/src.md#frametype)[]\>\>

This method returns the list of frames

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameType`](../modules/src.md#frametype)[]\>\>

#### Defined in

[src/controllers/FrameController.ts:27](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L27)

___

### getFramesByPageId

▸ **getFramesByPageId**(`pageId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameType`](../modules/src.md#frametype)[]\>\>

This method returns the list of frames by pageId

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `pageId` | `number` | The ID of a specific page |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameType`](../modules/src.md#frametype)[]\>\>

#### Defined in

[src/controllers/FrameController.ts:46](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L46)

___

### getFramesProperties

▸ **getFramesProperties**(`layoutId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameLayoutType`](../modules/src.md#framelayouttype)[]\>\>

This method returns frame properties for a given layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameLayoutType`](../modules/src.md#framelayouttype)[]\>\>

#### Defined in

[src/controllers/FrameController.ts:100](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L100)

___

### getSelectedFrames

▸ **getSelectedFrames**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameType`](../modules/src.md#frametype)[]\>\>

This method returns the list of selected frames

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameType`](../modules/src.md#frametype)[]\>\>

#### Defined in

[src/controllers/FrameController.ts:36](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L36)

___

### removeFrame

▸ **removeFrame**(`frameId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will remove a specific frame using the Id.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to be deleted |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:312](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L312)

___

### resetFrame

▸ **resetFrame**(`frameId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will reset properties of a specific frame to their original values

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:242](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L242)

___

### resetFrameHeight

▸ **resetFrameHeight**(`frameId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will reset the height of a specific frame to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:291](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L291)

___

### resetFrameRotation

▸ **resetFrameRotation**(`frameId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will reset the rotation value of a specific frame to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:271](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L271)

___

### resetFrameSize

▸ **resetFrameSize**(`frameId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will reset the frame size (width and height) to the frame's original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:110](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L110)

___

### resetFrameWidth

▸ **resetFrameWidth**(`frameId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will reset the width of a specific frame to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:281](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L281)

___

### resetFrameX

▸ **resetFrameX**(`frameId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will reset the x value of a specific frame to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:251](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L251)

___

### resetFrameY

▸ **resetFrameY**(`frameId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will reset the y value of a specific frame to its original value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get reset |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:261](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L261)

___

### selectFrame

▸ **selectFrame**(`frameId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will select a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:120](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L120)

___

### selectMultipleFrames

▸ **selectMultipleFrames**(`frameIds`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will select multipleFrames

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameIds` | `number`[] | An array of all IDs you want to select |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:130](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L130)

___

### setFrameHeight

▸ **setFrameHeight**(`frameId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will set the height of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:141](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L141)

___

### setFrameName

▸ **setFrameName**(`frameId`, `frameName`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will update the name of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `frameName` | `string` | The new name that the frame should receive |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:232](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L232)

___

### setFrameRotation

▸ **setFrameRotation**(`frameId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will set the rotation angle of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:159](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L159)

___

### setFrameVisibility

▸ **setFrameVisibility**(`frameId`, `value`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will set the visibility property of a specified frame. If set to false the frame will be invisible and vice versa.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get updated |
| `value` | `boolean` | True means the frame gets visible, false means the frame gets invisible |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:302](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L302)

___

### setFrameWidth

▸ **setFrameWidth**(`frameId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will set the width of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:177](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L177)

___

### setFrameX

▸ **setFrameX**(`frameId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will set the x value of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:195](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L195)

___

### setFrameY

▸ **setFrameY**(`frameId`, `value`): `Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will set the y value of a specific frame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `value` | `string` | The string value that will be calculated (f.e. 1+1 will result in 2) The notation is in pixels |

#### Returns

`Promise`<``null`` \| [`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:213](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L213)

___

### setImageFrameFitMode

▸ **setImageFrameFitMode**(`imageFrameId`, `fitMode`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will set the fitMode property of a specified image frame.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `imageFrameId` | `number` | The ID of the imageFrame that needs to get updated. |
| `fitMode` | [`FitMode`](../enums/src.FitMode.md) | The new fitMode that you want to set to the imageFrame. |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:351](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L351)

___

### setImageFromConnector

▸ **setImageFromConnector**(`imageFrameId`, `connectorId`, `resourceId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will assign an image from a mediaConnector to the correct imageFrame

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `imageFrameId` | `number` | The ID of the imageFrame where an image needs to be assigned to |
| `connectorId` | `string` | Unique Id of the media connector |
| `resourceId` | `string` | Unique Id of the asset that you want to assign to the imageFrame |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:338](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L338)

___

### setVerticalAlignment

▸ **setVerticalAlignment**(`frameId`, `verticalAlign`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method will set the vertical alignment property of a specified frame.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of the frame that needs to get updated |
| `verticalAlign` | [`VerticalAlign`](../enums/src.VerticalAlign.md) | The new vertical alignment to be set to the frame. |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/FrameController.ts:362](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/FrameController.ts#L362)
