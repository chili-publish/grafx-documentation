# Class: ToolController

[controllers/ToolController](../modules/controllers_ToolController.md).ToolController

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

▸ **getSelectedTool**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns selected tool

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/ToolController.ts:33](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ToolController.ts#L33)

___

### setHandTool

▸ **setHandTool**(): `Promise`<`void`\>

This method sets the used tool to a Move tool

#### Returns

`Promise`<`void`\>

#### Defined in

[src/controllers/ToolController.ts:48](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ToolController.ts#L48)

___

### setImageFrameTool

▸ **setImageFrameTool**(): `Promise`<`void`\>

This method sets the used tool to a ImageFrame tool

#### Returns

`Promise`<`void`\>

#### Defined in

[src/controllers/ToolController.ts:69](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ToolController.ts#L69)

___

### setSelectTool

▸ **setSelectTool**(): `Promise`<`void`\>

This method sets the used tool to a Pointer tool

#### Returns

`Promise`<`void`\>

#### Defined in

[src/controllers/ToolController.ts:41](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ToolController.ts#L41)

___

### setTextFrameTool

▸ **setTextFrameTool**(): `Promise`<`void`\>

This method sets the used tool to a TextFrame tool

#### Returns

`Promise`<`void`\>

#### Defined in

[src/controllers/ToolController.ts:62](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ToolController.ts#L62)

___

### setZoomTool

▸ **setZoomTool**(): `Promise`<`void`\>

This method sets the used tool to a Zoom tool

#### Returns

`Promise`<`void`\>

#### Defined in

[src/controllers/ToolController.ts:55](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/ToolController.ts#L55)
