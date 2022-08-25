[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [index](../modules/index.md) / SDK

# Class: SDK

[index](../modules/index.md).SDK

## Constructors

### constructor

• **new SDK**(`config`)

The SDK should be configured clientside and it exposes all controllers to work with in other applications

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `config` | [`ConfigType`](../modules/index.md#configtype) | The configuration object where the SDK and editor can get configured |

#### Defined in

[src/index.ts:85](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L85)

## Properties

### animation

• **animation**: [`AnimationController`](controllers_AnimationController.AnimationController.md)

#### Defined in

[src/index.ts:69](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L69)

___

### config

• **config**: [`ConfigType`](../modules/index.md#configtype)

#### Defined in

[src/index.ts:59](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L59)

___

### connection

• **connection**: `Connection`<`CallSender`\>

#### Defined in

[src/index.ts:60](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L60)

___

### debug

• **debug**: `DebugController`

#### Defined in

[src/index.ts:75](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L75)

___

### document

• **document**: [`DocumentController`](controllers_DocumentController.DocumentController.md)

#### Defined in

[src/index.ts:70](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L70)

___

### frame

• **frame**: [`FrameController`](controllers_FrameController.FrameController.md)

#### Defined in

[src/index.ts:68](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L68)

___

### layout

• **layout**: [`LayoutController`](controllers_LayoutController.LayoutController.md)

#### Defined in

[src/index.ts:67](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L67)

___

### page

• **page**: `PageController`

#### Defined in

[src/index.ts:74](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L74)

___

### textSelection

• **textSelection**: `TextStyleController`

#### Defined in

[src/index.ts:77](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L77)

___

### tool

• **tool**: [`ToolController`](controllers_ToolController.ToolController.md)

#### Defined in

[src/index.ts:73](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L73)

___

### undoManager

• **undoManager**: `UndoManagerController`

#### Defined in

[src/index.ts:76](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L76)

___

### utils

• **utils**: [`UtilsController`](controllers_UtilsController.UtilsController.md)

#### Defined in

[src/index.ts:72](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L72)

___

### variable

• **variable**: [`VariableController`](controllers_VariableController.VariableController.md)

#### Defined in

[src/index.ts:71](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L71)

## Methods

### loadEditor

▸ **loadEditor**(): `void`

This method will initiate the editor, running this will result in the editor restarting
It will generate an iframe in the document

#### Returns

`void`

#### Defined in

[src/index.ts:111](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L111)

___

### setConnection

▸ **setConnection**(`newConnection`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `newConnection` | `Connection`<`CallSender`\> |

#### Returns

`void`

#### Defined in

[src/index.ts:148](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/index.ts#L148)
