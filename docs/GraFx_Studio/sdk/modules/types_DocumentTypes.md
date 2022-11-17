[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / types/DocumentTypes

# Module: types/DocumentTypes

## Table of contents

### Enumerations

- [FramePropertiesType](../enums/types_DocumentTypes.FramePropertiesType.md)
- [ImageFrameSourceType](../enums/types_DocumentTypes.ImageFrameSourceType.md)

### Interfaces

- [AssetProviderImageFrameSource](../interfaces/types_DocumentTypes.AssetProviderImageFrameSource.md)
- [BasicAnimations](../interfaces/types_DocumentTypes.BasicAnimations.md)
- [ChildLayout](../interfaces/types_DocumentTypes.ChildLayout.md)
- [ChiliDocument](../interfaces/types_DocumentTypes.ChiliDocument.md)
- [DocumentCharacterStyle](../interfaces/types_DocumentTypes.DocumentCharacterStyle.md)
- [DocumentFrame](../interfaces/types_DocumentTypes.DocumentFrame.md)
- [DocumentPage](../interfaces/types_DocumentTypes.DocumentPage.md)
- [DocumentStyleKit](../interfaces/types_DocumentTypes.DocumentStyleKit.md)
- [DocumentVariable](../interfaces/types_DocumentTypes.DocumentVariable.md)
- [FrameAnimation](../interfaces/types_DocumentTypes.FrameAnimation.md)
- [FrameProperty](../interfaces/types_DocumentTypes.FrameProperty.md)
- [ImageFrame](../interfaces/types_DocumentTypes.ImageFrame.md)
- [ImageFrameSource](../interfaces/types_DocumentTypes.ImageFrameSource.md)
- [Layout](../interfaces/types_DocumentTypes.Layout.md)
- [TextFrame](../interfaces/types_DocumentTypes.TextFrame.md)
- [TopFrameProperty](../interfaces/types_DocumentTypes.TopFrameProperty.md)
- [TopLayout](../interfaces/types_DocumentTypes.TopLayout.md)
- [UrlImageFrameSource](../interfaces/types_DocumentTypes.UrlImageFrameSource.md)
- [VariableImageFrameSource](../interfaces/types_DocumentTypes.VariableImageFrameSource.md)

### Type Aliases

- [ChildFrameProperty](types_DocumentTypes.md#childframeproperty)
- [DocumentError](types_DocumentTypes.md#documenterror)
- [DocumentParagraphStyle](types_DocumentTypes.md#documentparagraphstyle)
- [OperationName](types_DocumentTypes.md#operationname)
- [UndoState](types_DocumentTypes.md#undostate)

## Type Aliases

### ChildFrameProperty

Ƭ **ChildFrameProperty**: [`FrameProperty`](../interfaces/types_DocumentTypes.FrameProperty.md)

#### Defined in

[types/DocumentTypes.ts:131](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/DocumentTypes.ts#L131)

___

### DocumentError

Ƭ **DocumentError**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `code` | `number` |
| `error` | `Record`<`string`, `unknown`\> |

#### Defined in

[types/DocumentTypes.ts:9](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/DocumentTypes.ts#L9)

___

### DocumentParagraphStyle

Ƭ **DocumentParagraphStyle**: [`ParagraphStyle`](src.md#paragraphstyle)

#### Defined in

[types/DocumentTypes.ts:183](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/DocumentTypes.ts#L183)

___

### OperationName

Ƭ **OperationName**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `name` | `string` |
| `translationKey` | `number` |

#### Defined in

[types/DocumentTypes.ts:18](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/DocumentTypes.ts#L18)

___

### UndoState

Ƭ **UndoState**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `canRedo` | `boolean` |
| `canUndo` | `boolean` |
| `redoItemName` | [`OperationName`](types_DocumentTypes.md#operationname) |
| `undoItemName` | [`OperationName`](types_DocumentTypes.md#operationname) |

#### Defined in

[types/DocumentTypes.ts:11](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/DocumentTypes.ts#L11)
