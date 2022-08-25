[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / index

# Module: index

## Enumerations

- [Alignment](../enums/index.Alignment.md)
- [BasicAnimationsEmphasisStyles](../enums/index.BasicAnimationsEmphasisStyles.md)
- [BlendMode](../enums/index.BlendMode.md)
- [BlendModes](../enums/index.BlendModes.md)
- [Case](../enums/index.Case.md)
- [DownloadFormats](../enums/index.DownloadFormats.md)
- [EaseTypes](../enums/index.EaseTypes.md)
- [FlowDirection](../enums/index.FlowDirection.md)
- [FontWeights](../enums/index.FontWeights.md)
- [FrameProperyNames](../enums/index.FrameProperyNames.md)
- [FrameTypeEnum](../enums/index.FrameTypeEnum.md)
- [LayoutProperyNames](../enums/index.LayoutProperyNames.md)
- [LayoutType](../enums/index.LayoutType.md)
- [Scripting](../enums/index.Scripting.md)
- [SelectedTextStyleSections](../enums/index.SelectedTextStyleSections.md)
- [SelectedTextStyles](../enums/index.SelectedTextStyles.md)
- [ShakeDirections](../enums/index.ShakeDirections.md)
- [SlideDirections](../enums/index.SlideDirections.md)
- [TextDirection](../enums/index.TextDirection.md)
- [TextPosition](../enums/index.TextPosition.md)
- [ToolType](../enums/index.ToolType.md)
- [TweenTypes](../enums/index.TweenTypes.md)
- [VariableType](../enums/index.VariableType.md)
- [VerticalAlign](../enums/index.VerticalAlign.md)

## Classes

- [SDK](../classes/index.SDK.md)

## Interfaces

- [AppearanceProperties](../interfaces/index.AppearanceProperties.md)
- [SelectedLayoutFrame](../interfaces/index.SelectedLayoutFrame.md)
- [TextProperties](../interfaces/index.TextProperties.md)
- [TextStyle](../interfaces/index.TextStyle.md)
- [UpdateStyleType](../interfaces/index.UpdateStyleType.md)

## References

### default

Renames and re-exports [SDK](../classes/index.SDK.md)

## Type Aliases

### AnimationPlaybackType

Ƭ **AnimationPlaybackType**: { `animationIsPlaying`: `boolean` ; `currentAnimationTimeMs`: `number`  } \| ``null``

#### Defined in

[types/AnimationTypes.ts:119](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/AnimationTypes.ts#L119)

___

### BasicAnimationsType

Ƭ **BasicAnimationsType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `emphasis?` | `BasicAnimationsEmphasisType` |
| `intro?` | `BasicAnimationsIntroType` |
| `outro?` | `BasicAnimationsOutroType` |

#### Defined in

[types/AnimationTypes.ts:101](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/AnimationTypes.ts#L101)

___

### ConfigType

Ƭ **ConfigType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `editorId?` | `string` |
| `editorLink` | `string` |
| `onFrameAnimationsChanged?` | (`animationState`: [`FrameAnimationType`](index.md#frameanimationtype)[]) => `void` |
| `onPageSelectionChanged?` | () => `void` |
| `onScrubberPositionChanged?` | (`state`: [`AnimationPlaybackType`](index.md#animationplaybacktype)) => `void` |
| `onSelectedFrameContentChanged?` | (`state`: [`FrameType`](index.md#frametype)) => `void` |
| `onSelectedFrameLayoutChanged?` | (`state`: [`FrameLayoutType`](index.md#framelayouttype)) => `void` |
| `onSelectedLayoutFramesChanged?` | (`frames`: [`SelectedLayoutFrame`](../interfaces/index.SelectedLayoutFrame.md)[]) => `void` |
| `onSelectedLayoutPropertiesChanged?` | (`state`: [`LayoutPropertiesType`](index.md#layoutpropertiestype)) => `void` |
| `onSelectedTextStyleChanged?` | (`styles`: `any`) => `void` |
| `onSelectedToolChanged?` | (`tool`: [`ToolType`](../enums/index.ToolType.md)) => `void` |
| `onStateChanged?` | (`state`: [`InitialStateType`](index.md#initialstatetype)) => `void` |
| `onUndoStackStateChanged?` | (`undoStackState`: `UndoState`) => `void` |
| `onVariableListChanged?` | (`variableList`: [`Variable`](index.md#variable)[]) => `void` |

#### Defined in

[types/CommonTypes.ts:10](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/CommonTypes.ts#L10)

___

### DocumentError

Ƭ **DocumentError**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `code` | `number` |
| `error` | `Record`<`string`, `unknown`\> |

#### Defined in

[types/DocumentTypes.ts:1](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/DocumentTypes.ts#L1)

___

### EaseTweenCombinationType

Ƭ **EaseTweenCombinationType**: \`${EaseTypes}${TweenTypes}\` \| ``"noEase"``

#### Defined in

[types/AnimationTypes.ts:49](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/AnimationTypes.ts#L49)

___

### EditorResponse

Ƭ **EditorResponse**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `data?` | `string` |
| `error?` | `string` |
| `status` | `number` |
| `success` | `boolean` |

#### Defined in

[types/CommonTypes.ts:27](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/CommonTypes.ts#L27)

___

### Frame

Ƭ **Frame**: [`TextFrame`](index.md#textframe) \| [`ImageFrame`](index.md#imageframe)

#### Defined in

[types/FrameTypes.ts:27](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/FrameTypes.ts#L27)

___

### FrameAnimationPropertiesType

Ƭ **FrameAnimationPropertiesType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `advancedAnimations?` | `unknown` |
| `basicAnimations` | [`BasicAnimationsType`](index.md#basicanimationstype) |
| `frameId` | `number` |
| `from` | `number` |
| `to` | `number` |

#### Defined in

[types/AnimationTypes.ts:107](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/AnimationTypes.ts#L107)

___

### FrameAnimationType

Ƭ **FrameAnimationType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `animation` | [`FrameAnimationPropertiesType`](index.md#frameanimationpropertiestype) |
| `isOverride` | `boolean` |

#### Defined in

[types/AnimationTypes.ts:114](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/AnimationTypes.ts#L114)

___

### FrameLayoutType

Ƭ **FrameLayoutType**: { `frameId`: `number` ; `height`: `PropertyState`<`number`\> ; `included`: `PropertyState`<`boolean`\> ; `layoutId`: `number` ; `rotationDegrees`: `PropertyState`<`number`\> ; `scaleX`: `PropertyState`<`number`\> ; `scaleY`: `PropertyState`<`number`\> ; `width`: `PropertyState`<`number`\> ; `x`: `PropertyState`<`number`\> ; `y`: `PropertyState`<`number`\>  } \| ``null``

#### Defined in

[types/FrameTypes.ts:4](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/FrameTypes.ts#L4)

___

### FrameProperties

Ƭ **FrameProperties**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `frameId` | `number` |
| `framePropertiesType` | `string` |
| `height` | `number` \| ``null`` |
| `included` | `boolean` \| ``null`` |
| `rotationDegrees` | `number` \| ``null`` |
| `scaleX` | `number` \| ``null`` |
| `scaleY` | `number` \| ``null`` |
| `width` | `number` \| ``null`` |
| `x` | `number` \| ``null`` |
| `y` | `number` \| ``null`` |

#### Defined in

[types/LayoutTypes.ts:12](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/LayoutTypes.ts#L12)

___

### FrameType

Ƭ **FrameType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `blendMode` | `string` |
| `frameId` | `number` |
| `frameName` | `string` |
| `frameType` | ``"image"`` |
| `imageUrl` | `string` |

#### Defined in

[types/FrameTypes.ts:19](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/FrameTypes.ts#L19)

___

### ImageFrame

Ƭ **ImageFrame**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `blendMode` | [`BlendMode`](../enums/index.BlendMode.md) |
| `frameId` | `number` |
| `frameName` | `string` |
| `frameType` | [`image`](../enums/index.FrameTypeEnum.md#image) |
| `src` | `string` |

#### Defined in

[types/FrameTypes.ts:29](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/FrameTypes.ts#L29)

___

### InitialStateType

Ƭ **InitialStateType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `layouts` | [`LayoutWithFrameProperties`](index.md#layoutwithframeproperties)[] |
| `pages` | [`PageType`](index.md#pagetype)[] |
| `selectedLayoutId` | `number` |
| `variables` | [`Variable`](index.md#variable)[] |

#### Defined in

[types/CommonTypes.ts:45](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/CommonTypes.ts#L45)

___

### LayoutPropertiesType

Ƭ **LayoutPropertiesType**: { `[key: string]`: `number` \| `string` \| `Record`<`string`, `unknown`\>; `height`: { `isOverride`: `boolean` ; `value`: `number`  } ; `layoutId`: `number` ; `timelineLengthMs`: { `isOverride`: `boolean` ; `value`: `number`  } ; `width`: { `isOverride`: `boolean` ; `value`: `number`  }  } \| ``null``

#### Defined in

[types/LayoutTypes.ts:3](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/LayoutTypes.ts#L3)

___

### LayoutWithFrameProperties

Ƭ **LayoutWithFrameProperties**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `childLayouts` | `number`[] |
| `children?` | [`LayoutWithFrameProperties`](index.md#layoutwithframeproperties)[] |
| `frameProperties` | [`FrameProperties`](index.md#frameproperties)[] |
| `height` | `number` \| ``null`` |
| `layoutId` | `number` |
| `layoutName` | `string` |
| `layoutType` | [`LayoutType`](../enums/index.LayoutType.md) |
| `parentLayoutId?` | `number` |
| `timelineLengthMs?` | `number` |
| `width` | `number` \| ``null`` |

#### Defined in

[types/LayoutTypes.ts:25](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/LayoutTypes.ts#L25)

___

### PageType

Ƭ **PageType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `frames` | [`FrameType`](index.md#frametype)[] |
| `height` | `number` \| ``null`` |
| `pageId` | `number` |
| `pageNumber` | `number` |
| `width` | `number` \| ``null`` |

#### Defined in

[types/CommonTypes.ts:37](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/CommonTypes.ts#L37)

___

### TextFrame

Ƭ **TextFrame**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `blendMode` | [`BlendMode`](../enums/index.BlendMode.md) |
| `columnGap` | `number` |
| `flowDirection` | [`FlowDirection`](../enums/index.FlowDirection.md) |
| `frameId` | `number` |
| `frameName` | `string` |
| `frameType` | [`text`](../enums/index.FrameTypeEnum.md#text) |
| `hasClippingPath` | `boolean` |
| `numberOfColumn` | `number` |
| `paddingBottom` | `number` |
| `paddingLeft` | `number` |
| `paddingRight` | `number` |
| `paddingTop` | `number` |
| `textContent` | `string` |
| `textDirection` | [`TextDirection`](../enums/index.TextDirection.md) |
| `textStroke` | `boolean` |
| `textStrokeColor` | `number` |
| `textStrokeWeight` | `number` |
| `verticalAlign` | [`VerticalAlign`](../enums/index.VerticalAlign.md) |

#### Defined in

[types/FrameTypes.ts:36](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/FrameTypes.ts#L36)

___

### TextStyleUpdateType

Ƭ **TextStyleUpdateType**: { [key in keyof typeof SelectedTextStyles]?: Object }

#### Defined in

[types/TextStyleTypes.ts:49](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/TextStyleTypes.ts#L49)

___

### Variable

Ƭ **Variable**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `defaultValue?` | `string` |
| `id` | `string` |
| `isHidden?` | `boolean` |
| `isReadonly?` | `boolean` |
| `isRequired?` | `boolean` |
| `label?` | `string` |
| `name?` | `string` |
| `occurrences?` | `number` |
| `parentId?` | `string` |
| `type` | [`VariableType`](../enums/index.VariableType.md) |
| `value?` | `string` |

#### Defined in

[types/VariableTypes.ts:5](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/VariableTypes.ts#L5)

___

### VariableMoves

Ƭ **VariableMoves**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `moves` | `string`[] |
| `order` | `number` |
| `parent` | `string` |

#### Defined in

[types/VariableTypes.ts:19](https://github.com/chili-publish/editor-sdk/blob/c6e096c/types/VariableTypes.ts#L19)
