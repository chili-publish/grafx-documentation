[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src](../modules/src.md) / SDK

# Class: SDK

[src](../modules/src.md).SDK

## Table of contents

### Constructors

- [constructor](SDK.md#constructor)

### Properties

- [animation](SDK.md#animation)
- [colorStyle](SDK.md#colorstyle)
- [config](SDK.md#config)
- [configuration](SDK.md#configuration)
- [connection](SDK.md#connection)
- [connector](SDK.md#connector)
- [debug](SDK.md#debug)
- [document](SDK.md#document)
- [fontConnector](SDK.md#fontconnector)
- [frame](SDK.md#frame)
- [layout](SDK.md#layout)
- [mediaConnector](SDK.md#mediaconnector)
- [page](SDK.md#page)
- [paragraphStyle](SDK.md#paragraphstyle)
- [textSelection](SDK.md#textselection)
- [tool](SDK.md#tool)
- [undoManager](SDK.md#undomanager)
- [utils](SDK.md#utils)
- [variable](SDK.md#variable)

### Methods

- [loadEditor](SDK.md#loadeditor)
- [setConnection](SDK.md#setconnection)

## Constructors

### constructor

• **new SDK**(`config`)

The SDK should be configured clientside and it exposes all controllers to work with in other applications

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `config` | [`ConfigType`](../modules/src.md#configtype) | The configuration object where the SDK and editor can get configured |

#### Defined in

[src/index.ts:129](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L129)

## Properties

### animation

• **animation**: [`AnimationController`](controllers_AnimationController.AnimationController.md)

#### Defined in

[src/index.ts:110](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L110)

___

### colorStyle

• **colorStyle**: `ColorStyleController`

#### Defined in

[src/index.ts:121](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L121)

___

### config

• **config**: [`ConfigType`](../modules/src.md#configtype)

#### Defined in

[src/index.ts:97](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L97)

___

### configuration

• **configuration**: `ConfigurationController`

#### Defined in

[src/index.ts:112](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L112)

___

### connection

• **connection**: `Connection`<`CallSender`\>

#### Defined in

[src/index.ts:98](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L98)

___

### connector

• **connector**: `ConnectorController`

#### Defined in

[src/index.ts:107](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L107)

___

### debug

• **debug**: [`DebugController`](controllers_DebugController.DebugController.md)

#### Defined in

[src/index.ts:117](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L117)

___

### document

• **document**: [`DocumentController`](controllers_DocumentController.DocumentController.md)

#### Defined in

[src/index.ts:111](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L111)

___

### fontConnector

• **fontConnector**: `FontConnectorController`

#### Defined in

[src/index.ts:109](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L109)

___

### frame

• **frame**: [`FrameController`](controllers_FrameController.FrameController.md)

#### Defined in

[src/index.ts:106](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L106)

___

### layout

• **layout**: [`LayoutController`](controllers_LayoutController.LayoutController.md)

#### Defined in

[src/index.ts:105](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L105)

___

### mediaConnector

• **mediaConnector**: [`MediaConnectorController`](controllers_MediaConnectorController.MediaConnectorController.md)

#### Defined in

[src/index.ts:108](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L108)

___

### page

• **page**: [`PageController`](controllers_PageController.PageController.md)

#### Defined in

[src/index.ts:116](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L116)

___

### paragraphStyle

• **paragraphStyle**: [`ParagraphStyleController`](controllers_ParagraphStyleController.ParagraphStyleController.md)

#### Defined in

[src/index.ts:120](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L120)

___

### textSelection

• **textSelection**: [`TextStyleController`](controllers_TextStyleController.TextStyleController.md)

#### Defined in

[src/index.ts:119](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L119)

___

### tool

• **tool**: [`ToolController`](controllers_ToolController.ToolController.md)

#### Defined in

[src/index.ts:115](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L115)

___

### undoManager

• **undoManager**: [`UndoManagerController`](controllers_UndoManagerController.UndoManagerController.md)

#### Defined in

[src/index.ts:118](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L118)

___

### utils

• **utils**: [`UtilsController`](controllers_UtilsController.UtilsController.md)

#### Defined in

[src/index.ts:114](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L114)

___

### variable

• **variable**: [`VariableController`](controllers_VariableController.VariableController.md)

#### Defined in

[src/index.ts:113](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L113)

## Methods

### loadEditor

▸ **loadEditor**(): `void`

This method will initiate the editor, running this will result in the editor restarting
It will generate an iframe in the document

#### Returns

`void`

#### Defined in

[src/index.ts:160](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L160)

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

[src/index.ts:212](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/index.ts#L212)
