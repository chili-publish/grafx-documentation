[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/ToolController](../modules/controllers_ToolController.md) / ToolController

# Class: ToolController

[src/controllers/ToolController](../modules/controllers_ToolController.md).ToolController

The ToolController is responsible for all communication regarding the tools.
Methods inside this controller can be called by `window.SDK.tool.{method-name}`

## Table of contents

### Methods

- [getSelectedTool](controllers_ToolController.ToolController.md#getselectedtool)
- [setHandTool](controllers_ToolController.ToolController.md#sethandtool)
- [setImageFrameTool](controllers_ToolController.ToolController.md#setimageframetool)
- [setSelectTool](controllers_ToolController.ToolController.md#setselecttool)
- [setTextFrameTool](controllers_ToolController.ToolController.md#settextframetool)
- [setZoomTool](controllers_ToolController.ToolController.md#setzoomtool)

## Methods

### getSelectedTool

▸ **getSelectedTool**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`ToolType`](../enums/src.ToolType.md)\>\>

This method returns selected tool

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`ToolType`](../enums/src.ToolType.md)\>\>

#### Defined in

[src/controllers/ToolController.ts:34](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ToolController.ts#L34)

___

### setHandTool

▸ **setHandTool**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets the used tool to a Move tool

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/ToolController.ts:49](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ToolController.ts#L49)

___

### setImageFrameTool

▸ **setImageFrameTool**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets the used tool to a ImageFrame tool

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/ToolController.ts:70](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ToolController.ts#L70)

___

### setSelectTool

▸ **setSelectTool**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets the used tool to a Pointer tool

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/ToolController.ts:42](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ToolController.ts#L42)

___

### setTextFrameTool

▸ **setTextFrameTool**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets the used tool to a TextFrame tool

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/ToolController.ts:63](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ToolController.ts#L63)

___

### setZoomTool

▸ **setZoomTool**(): `Promise`<`void`\>

This method sets the used tool to a Zoom tool

#### Returns

`Promise`<`void`\>

#### Defined in

[src/controllers/ToolController.ts:56](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/ToolController.ts#L56)
