# Class: SDK

[index](../modules/index.md).SDK

## Table of contents

### Constructors

- [constructor](index.SDK.md#constructor)

### Properties

- [animation](index.SDK.md#animation)
- [colorStyle](index.SDK.md#colorstyle)
- [config](index.SDK.md#config)
- [connection](index.SDK.md#connection)
- [debug](index.SDK.md#debug)
- [document](index.SDK.md#document)
- [frame](index.SDK.md#frame)
- [layout](index.SDK.md#layout)
- [page](index.SDK.md#page)
- [paragraphStyle](index.SDK.md#paragraphstyle)
- [textSelection](index.SDK.md#textselection)
- [tool](index.SDK.md#tool)
- [undoManager](index.SDK.md#undomanager)
- [utils](index.SDK.md#utils)
- [variable](index.SDK.md#variable)

### Methods

- [loadEditor](index.SDK.md#loadeditor)
- [setConnection](index.SDK.md#setconnection)

## Constructors

### constructor

• **new SDK**(`config`)

The SDK should be configured clientside and it exposes all controllers to work with in other applications

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `config` | [`ConfigType`](../modules/index.md#configtype) | The configuration object where the SDK and editor can get configured |

#### Defined in

[src/index.ts:102](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L102)

## Properties

### animation

• **animation**: [`AnimationController`](controllers_AnimationController.AnimationController.md)

#### Defined in

[src/index.ts:84](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L84)

___

### colorStyle

• **colorStyle**: `ColorStyleController`

#### Defined in

[src/index.ts:94](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L94)

___

### config

• **config**: [`ConfigType`](../modules/index.md#configtype)

#### Defined in

[src/index.ts:74](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L74)

___

### connection

• **connection**: `Connection`<`CallSender`\>

#### Defined in

[src/index.ts:75](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L75)

___

### debug

• **debug**: [`DebugController`](controllers_DebugController.DebugController.md)

#### Defined in

[src/index.ts:90](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L90)

___

### document

• **document**: [`DocumentController`](controllers_DocumentController.DocumentController.md)

#### Defined in

[src/index.ts:85](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L85)

___

### frame

• **frame**: [`FrameController`](controllers_FrameController.FrameController.md)

#### Defined in

[src/index.ts:83](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L83)

___

### layout

• **layout**: [`LayoutController`](controllers_LayoutController.LayoutController.md)

#### Defined in

[src/index.ts:82](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L82)

___

### page

• **page**: [`PageController`](controllers_PageController.PageController.md)

#### Defined in

[src/index.ts:89](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L89)

___

### paragraphStyle

• **paragraphStyle**: [`ParagraphStyleController`](controllers_ParagraphStyleController.ParagraphStyleController.md)

#### Defined in

[src/index.ts:93](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L93)

___

### textSelection

• **textSelection**: [`TextStyleController`](controllers_TextStyleController.TextStyleController.md)

#### Defined in

[src/index.ts:92](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L92)

___

### tool

• **tool**: [`ToolController`](controllers_ToolController.ToolController.md)

#### Defined in

[src/index.ts:88](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L88)

___

### undoManager

• **undoManager**: [`UndoManagerController`](controllers_UndoManagerController.UndoManagerController.md)

#### Defined in

[src/index.ts:91](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L91)

___

### utils

• **utils**: [`UtilsController`](controllers_UtilsController.UtilsController.md)

#### Defined in

[src/index.ts:87](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L87)

___

### variable

• **variable**: [`VariableController`](controllers_VariableController.VariableController.md)

#### Defined in

[src/index.ts:86](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L86)

## Methods

### loadEditor

▸ **loadEditor**(): `void`

This method will initiate the editor, running this will result in the editor restarting
It will generate an iframe in the document

#### Returns

`void`

#### Defined in

[src/index.ts:129](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L129)

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

[src/index.ts:170](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/index.ts#L170)
