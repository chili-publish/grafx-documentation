[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / src

# Module: src

## Table of contents

### References

- [DocumentError](src.md#documenterror)
- [Media](src.md#media)
- [MediaDownloadType](src.md#mediadownloadtype)
- [MediaPage](src.md#mediapage)
- [default](src.md#default)

### Enumerations

- [Alignment](../enums/src.Alignment.md)
- [BasicAnimationsEmphasisStyles](../enums/src.BasicAnimationsEmphasisStyles.md)
- [BlendMode](../enums/src.BlendMode.md)
- [BlendModes](../enums/src.BlendModes.md)
- [Case](../enums/src.Case.md)
- [ColorType](../enums/src.ColorType.md)
- [ColorUsageType](../enums/src.ColorUsageType.md)
- [DownloadFormats](../enums/src.DownloadFormats.md)
- [EaseTypes](../enums/src.EaseTypes.md)
- [FitMode](../enums/src.FitMode.md)
- [FlowDirection](../enums/src.FlowDirection.md)
- [FontWeights](../enums/src.FontWeights.md)
- [FrameProperyNames](../enums/src.FrameProperyNames.md)
- [FrameTypeEnum](../enums/src.FrameTypeEnum.md)
- [LayoutProperyNames](../enums/src.LayoutProperyNames.md)
- [LayoutType](../enums/src.LayoutType.md)
- [MediaType](../enums/src.MediaType.md)
- [Scripting](../enums/src.Scripting.md)
- [SelectedTextStyleSections](../enums/src.SelectedTextStyleSections.md)
- [SelectedTextStyles](../enums/src.SelectedTextStyles.md)
- [ShakeDirections](../enums/src.ShakeDirections.md)
- [SlideDirections](../enums/src.SlideDirections.md)
- [TextDirection](../enums/src.TextDirection.md)
- [TextPosition](../enums/src.TextPosition.md)
- [ToolType](../enums/src.ToolType.md)
- [TweenTypes](../enums/src.TweenTypes.md)
- [VariableType](../enums/src.VariableType.md)
- [VerticalAlign](../enums/src.VerticalAlign.md)
- [WellKnownConfigurationKeys](../enums/src.WellKnownConfigurationKeys.md)

### Classes

- [SDK](../classes/SDK.md)

### Interfaces

- [AppearanceProperties](../interfaces/src.AppearanceProperties.md)
- [EditorResponse](../interfaces/src.EditorResponse.md)
- [MetaData](../interfaces/src.MetaData.md)
- [SelectedLayoutFrame](../interfaces/src.SelectedLayoutFrame.md)
- [TextProperties](../interfaces/src.TextProperties.md)
- [TextStyle](../interfaces/src.TextStyle.md)
- [UpdateStyleType](../interfaces/src.UpdateStyleType.md)

### Type Aliases

- [AnimationPlaybackType](src.md#animationplaybacktype)
- [BasicAnimationsType](src.md#basicanimationstype)
- [CharacterStyle](src.md#characterstyle)
- [Color](src.md#color)
- [ColorUpdate](src.md#colorupdate)
- [ColorUsage](src.md#colorusage)
- [ColorUsageUpdate](src.md#colorusageupdate)
- [ConfigType](src.md#configtype)
- [DocumentColor](src.md#documentcolor)
- [EaseTweenCombinationType](src.md#easetweencombinationtype)
- [Font](src.md#font)
- [Frame](src.md#frame)
- [FrameAnimationPropertiesType](src.md#frameanimationpropertiestype)
- [FrameAnimationType](src.md#frameanimationtype)
- [FrameLayoutType](src.md#framelayouttype)
- [FrameProperties](src.md#frameproperties)
- [FrameType](src.md#frametype)
- [ImageFrame](src.md#imageframe)
- [InitialStateType](src.md#initialstatetype)
- [LayoutPropertiesType](src.md#layoutpropertiestype)
- [LayoutWithFrameProperties](src.md#layoutwithframeproperties)
- [PageType](src.md#pagetype)
- [ParagraphStyle](src.md#paragraphstyle)
- [ParagraphStyleUpdate](src.md#paragraphstyleupdate)
- [QueryOptions](src.md#queryoptions)
- [TextFrame](src.md#textframe)
- [TextStyleUpdateType](src.md#textstyleupdatetype)
- [Variable](src.md#variable)
- [VariableMoves](src.md#variablemoves)

## References

### DocumentError

Re-exports [DocumentError](types_DocumentTypes.md#documenterror)

___

### Media

Re-exports [Media](types_MediaConnectorTypes.md#media)

___

### MediaDownloadType

Re-exports [MediaDownloadType](../enums/types_MediaConnectorTypes.MediaDownloadType.md)

___

### MediaPage

Re-exports [MediaPage](types_MediaConnectorTypes.md#mediapage)

___

### default

Renames and re-exports [SDK](../classes/SDK.md)

## Type Aliases

### AnimationPlaybackType

Ƭ **AnimationPlaybackType**: { `animationIsPlaying`: `boolean` ; `currentAnimationTimeMs`: `number`  } \| ``null``

#### Defined in

[types/AnimationTypes.ts:119](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/AnimationTypes.ts#L119)

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

[types/AnimationTypes.ts:101](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/AnimationTypes.ts#L101)

___

### CharacterStyle

Ƭ **CharacterStyle**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `baselineShiftValue?` | `string` |
| `color` | [`ColorUsage`](src.md#colorusage) |
| `fontKey?` | `string` |
| `fontSize?` | `number` |
| `fontStyle?` | `string` |
| `id` | `string` |
| `kerningOn` | `boolean` |
| `lineHeight?` | `number` |
| `lineThrough` | `boolean` |
| `name` | `string` |
| `subSuperScript?` | [`Scripting`](../enums/src.Scripting.md) |
| `textIndent?` | `string` |
| `textOverprint?` | `boolean` |
| `trackingLeft?` | `string` |
| `trackingRight?` | `string` |
| `typographicCase?` | [`Case`](../enums/src.Case.md) |
| `underline` | `boolean` |

#### Defined in

[types/CharacterStyleTypes.ts:4](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/CharacterStyleTypes.ts#L4)

___

### Color

Ƭ **Color**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `b` | `number` |
| `colorType` | [`ColorType`](../enums/src.ColorType.md) |
| `displayValue?` | `string` |
| `g` | `number` |
| `r` | `number` |

#### Defined in

[types/ColorStyleTypes.ts:23](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/ColorStyleTypes.ts#L23)

___

### ColorUpdate

Ƭ **ColorUpdate**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `b` | `number` |
| `colorType` | [`ColorType`](../enums/src.ColorType.md) |
| `g` | `number` |
| `r` | `number` |

#### Defined in

[types/ColorStyleTypes.ts:16](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/ColorStyleTypes.ts#L16)

___

### ColorUsage

Ƭ **ColorUsage**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `color` | [`Color`](src.md#color) |
| `opacity?` | `number` |
| `usageType` | [`ColorUsageType`](../enums/src.ColorUsageType.md) |

#### Defined in

[types/ParagraphStyleTypes.ts:9](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/ParagraphStyleTypes.ts#L9)

___

### ColorUsageUpdate

Ƭ **ColorUsageUpdate**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `color` | [`ColorUpdate`](src.md#colorupdate) |
| `usageType` | [`ColorUsageType`](../enums/src.ColorUsageType.md) |

#### Defined in

[types/ParagraphStyleTypes.ts:4](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/ParagraphStyleTypes.ts#L4)

___

### ConfigType

Ƭ **ConfigType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `chiliEnvironmentUrl?` | `string` |
| `editorId?` | `string` |
| `editorLink?` | `string` |
| `onCharacterStylesChanged?` | (`characterStyles`: [`CharacterStyle`](src.md#characterstyle)[]) => `void` |
| `onColorsChanged?` | (`colors`: [`DocumentColor`](src.md#documentcolor)[]) => `void` |
| `onFontsChanged?` | (`fonts`: [`Font`](src.md#font)[]) => `void` |
| `onFrameAnimationsChanged?` | (`animationState`: [`FrameAnimationType`](src.md#frameanimationtype)[]) => `void` |
| `onPageSelectionChanged?` | () => `void` |
| `onParagraphStylesChanged?` | (`paragraphStyles`: [`ParagraphStyle`](src.md#paragraphstyle)[]) => `void` |
| `onScrubberPositionChanged?` | (`state`: [`AnimationPlaybackType`](src.md#animationplaybacktype)) => `void` |
| `onSelectedFrameContentChanged?` | (`state`: [`Frame`](src.md#frame)) => `void` |
| `onSelectedFrameLayoutChanged?` | (`state`: [`FrameLayoutType`](src.md#framelayouttype)) => `void` |
| `onSelectedLayoutFramesChanged?` | (`frames`: [`SelectedLayoutFrame`](../interfaces/src.SelectedLayoutFrame.md)[]) => `void` |
| `onSelectedLayoutPropertiesChanged?` | (`state`: [`LayoutPropertiesType`](src.md#layoutpropertiestype)) => `void` |
| `onSelectedTextStyleChanged?` | (`styles`: `any`) => `void` |
| `onSelectedToolChanged?` | (`tool`: [`ToolType`](../enums/src.ToolType.md)) => `void` |
| `onStateChanged?` | (`state`: [`InitialStateType`](src.md#initialstatetype)) => `void` |
| `onUndoStackStateChanged?` | (`undoStackState`: [`UndoState`](types_DocumentTypes.md#undostate)) => `void` |
| `onVariableListChanged?` | (`variableList`: [`Variable`](src.md#variable)[]) => `void` |

#### Defined in

[types/CommonTypes.ts:14](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/CommonTypes.ts#L14)

___

### DocumentColor

Ƭ **DocumentColor**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `color` | [`Color`](src.md#color) |
| `id` | `string` |
| `name` | `string` |

#### Defined in

[types/ColorStyleTypes.ts:31](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/ColorStyleTypes.ts#L31)

___

### EaseTweenCombinationType

Ƭ **EaseTweenCombinationType**: \`${EaseTypes}${TweenTypes}\` \| ``"noEase"``

#### Defined in

[types/AnimationTypes.ts:49](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/AnimationTypes.ts#L49)

___

### Font

Ƭ **Font**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `connectorId` | `string` |
| `fontFamily` | `string` |
| `fontId` | `string` |
| `fontStyle` | `string` |
| `id` | `string` |
| `name` | `string` |

#### Defined in

[types/FontTypes.ts:1](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/FontTypes.ts#L1)

___

### Frame

Ƭ **Frame**: [`TextFrame`](src.md#textframe) \| [`ImageFrame`](src.md#imageframe)

#### Defined in

[types/FrameTypes.ts:27](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/FrameTypes.ts#L27)

___

### FrameAnimationPropertiesType

Ƭ **FrameAnimationPropertiesType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `advancedAnimations?` | `unknown` |
| `basicAnimations` | [`BasicAnimationsType`](src.md#basicanimationstype) |
| `frameId` | `number` |
| `from` | `number` |
| `to` | `number` |

#### Defined in

[types/AnimationTypes.ts:107](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/AnimationTypes.ts#L107)

___

### FrameAnimationType

Ƭ **FrameAnimationType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `animation` | [`FrameAnimationPropertiesType`](src.md#frameanimationpropertiestype) |
| `isOverride` | `boolean` |

#### Defined in

[types/AnimationTypes.ts:114](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/AnimationTypes.ts#L114)

___

### FrameLayoutType

Ƭ **FrameLayoutType**: { `fitMode`: `PropertyState`<[`FitMode`](../enums/src.FitMode.md)\> ; `frameId`: `number` ; `height`: `PropertyState`<`number`\> ; `included`: `PropertyState`<`boolean`\> ; `layoutId`: `number` ; `rotationDegrees`: `PropertyState`<`number`\> ; `scaleX`: `PropertyState`<`number`\> ; `scaleY`: `PropertyState`<`number`\> ; `width`: `PropertyState`<`number`\> ; `x`: `PropertyState`<`number`\> ; `y`: `PropertyState`<`number`\>  } \| ``null``

#### Defined in

[types/FrameTypes.ts:4](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/FrameTypes.ts#L4)

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

[types/LayoutTypes.ts:12](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/LayoutTypes.ts#L12)

___

### FrameType

Ƭ **FrameType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `blendMode` | `string` |
| `frameId` | `number` |
| `frameName` | `string` |
| `frameType` | [`FrameTypeEnum`](../enums/src.FrameTypeEnum.md) |
| `imageUrl` | `string` |

#### Defined in

[types/FrameTypes.ts:19](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/FrameTypes.ts#L19)

___

### ImageFrame

Ƭ **ImageFrame**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `blendMode` | [`BlendMode`](../enums/src.BlendMode.md) |
| `frameId` | `number` |
| `frameName` | `string` |
| `frameType` | [`image`](../enums/src.FrameTypeEnum.md#image) |
| `src` | `string` |

#### Defined in

[types/FrameTypes.ts:29](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/FrameTypes.ts#L29)

___

### InitialStateType

Ƭ **InitialStateType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `layouts` | [`LayoutWithFrameProperties`](src.md#layoutwithframeproperties)[] |
| `pages` | [`PageType`](src.md#pagetype)[] |
| `selectedLayoutId` | `number` |
| `variables` | [`Variable`](src.md#variable)[] |

#### Defined in

[types/CommonTypes.ts:60](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/CommonTypes.ts#L60)

___

### LayoutPropertiesType

Ƭ **LayoutPropertiesType**: { `[key: string]`: `number` \| `string` \| `Record`<`string`, `unknown`\>; `height`: { `isOverride`: `boolean` ; `value`: `number`  } ; `layoutId`: `number` ; `timelineLengthMs`: { `isOverride`: `boolean` ; `value`: `number`  } ; `width`: { `isOverride`: `boolean` ; `value`: `number`  }  } \| ``null``

#### Defined in

[types/LayoutTypes.ts:3](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/LayoutTypes.ts#L3)

___

### LayoutWithFrameProperties

Ƭ **LayoutWithFrameProperties**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `childLayouts` | `number`[] |
| `children?` | [`LayoutWithFrameProperties`](src.md#layoutwithframeproperties)[] |
| `frameProperties` | [`FrameProperties`](src.md#frameproperties)[] |
| `height` | `number` \| ``null`` |
| `layoutId` | `number` |
| `layoutName` | `string` |
| `layoutType` | [`LayoutType`](../enums/src.LayoutType.md) |
| `parentLayoutId?` | `number` |
| `timelineLengthMs?` | `number` |
| `width` | `number` \| ``null`` |

#### Defined in

[types/LayoutTypes.ts:25](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/LayoutTypes.ts#L25)

___

### PageType

Ƭ **PageType**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `frames` | [`FrameType`](src.md#frametype)[] |
| `height` | `number` \| ``null`` |
| `pageId` | `number` |
| `pageNumber` | `number` |
| `width` | `number` \| ``null`` |

#### Defined in

[types/CommonTypes.ts:52](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/CommonTypes.ts#L52)

___

### ParagraphStyle

Ƭ **ParagraphStyle**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `alignToBaseLine` | `boolean` |
| `baselineShiftValue` | `string` |
| `color` | [`ColorUsage`](src.md#colorusage) |
| `fontKey` | `string` |
| `fontSize` | `number` |
| `fontStyle` | `string` |
| `id` | `string` |
| `kerningOn` | `boolean` |
| `lineHeight` | `number` |
| `lineThrough` | `boolean` |
| `name` | `string` |
| `paragraphEndIndent` | `string` |
| `paragraphSpaceAfter` | `string` |
| `paragraphSpaceBefore` | `string` |
| `paragraphStartIndent` | `string` |
| `subSuperScript` | [`Scripting`](../enums/src.Scripting.md) |
| `textAlign` | [`Alignment`](../enums/src.Alignment.md) |
| `textAlignLast` | [`Alignment`](../enums/src.Alignment.md) |
| `textIndent` | `string` |
| `textOverprint` | `boolean` |
| `trackingLeft` | `string` |
| `trackingRight` | `string` |
| `typographicCase` | [`Case`](../enums/src.Case.md) |
| `underline` | `boolean` |

#### Defined in

[types/ParagraphStyleTypes.ts:20](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/ParagraphStyleTypes.ts#L20)

___

### ParagraphStyleUpdate

Ƭ **ParagraphStyleUpdate**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `alignToBaseLine` | { `value`: `boolean`  } |
| `alignToBaseLine.value` | `boolean` |
| `baselineShiftValue` | { `value`: `string`  } |
| `baselineShiftValue.value` | `string` |
| `color` | { `value`: [`ColorUsageUpdate`](src.md#colorusageupdate)  } |
| `color.value` | [`ColorUsageUpdate`](src.md#colorusageupdate) |
| `fontSize` | { `value`: `number`  } |
| `fontSize.value` | `number` |
| `kerningOn` | { `value`: `boolean`  } |
| `kerningOn.value` | `boolean` |
| `lineHeight` | { `value`: `number`  } |
| `lineHeight.value` | `number` |
| `lineThrough` | { `value`: `boolean`  } |
| `lineThrough.value` | `boolean` |
| `subSuperScript` | { `value`: [`Scripting`](../enums/src.Scripting.md)  } |
| `subSuperScript.value` | [`Scripting`](../enums/src.Scripting.md) |
| `textAlign` | { `value`: [`Alignment`](../enums/src.Alignment.md)  } |
| `textAlign.value` | [`Alignment`](../enums/src.Alignment.md) |
| `textAlignLast` | { `value`: [`Alignment`](../enums/src.Alignment.md)  } |
| `textAlignLast.value` | [`Alignment`](../enums/src.Alignment.md) |
| `textIndent` | { `value`: `string`  } |
| `textIndent.value` | `string` |
| `textOverprint` | { `value`: `boolean`  } |
| `textOverprint.value` | `boolean` |
| `trackingLeft` | { `value`: `string`  } |
| `trackingLeft.value` | `string` |
| `trackingRight` | { `value`: `string`  } |
| `trackingRight.value` | `string` |
| `typographicCase` | { `value`: [`Case`](../enums/src.Case.md)  } |
| `typographicCase.value` | [`Case`](../enums/src.Case.md) |
| `underline` | { `value`: `boolean`  } |
| `underline.value` | `boolean` |

#### Defined in

[types/ParagraphStyleTypes.ts:49](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/ParagraphStyleTypes.ts#L49)

___

### QueryOptions

Ƭ **QueryOptions**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `collection?` | `string` \| ``null`` |
| `filter?` | `string`[] \| ``null`` |
| `pageSize?` | `number` \| ``null`` |
| `pageToken?` | `string` \| ``null`` |
| `sortBy?` | `SortBy` \| ``null`` |
| `sortOrder?` | `SortOrder` \| ``null`` |

#### Defined in

[types/ConnectorTypes.ts:22](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/ConnectorTypes.ts#L22)

___

### TextFrame

Ƭ **TextFrame**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `blendMode` | [`BlendMode`](../enums/src.BlendMode.md) |
| `columnGap` | `number` |
| `flowDirection` | [`FlowDirection`](../enums/src.FlowDirection.md) |
| `frameId` | `number` |
| `frameName` | `string` |
| `frameType` | [`text`](../enums/src.FrameTypeEnum.md#text) |
| `hasClippingPath` | `boolean` |
| `numberOfColumn` | `number` |
| `paddingBottom` | `number` |
| `paddingLeft` | `number` |
| `paddingRight` | `number` |
| `paddingTop` | `number` |
| `textContent` | `string` |
| `textDirection` | [`TextDirection`](../enums/src.TextDirection.md) |
| `textStroke` | `boolean` |
| `textStrokeColor` | `number` |
| `textStrokeWeight` | `number` |
| `verticalAlign` | [`VerticalAlign`](../enums/src.VerticalAlign.md) |

#### Defined in

[types/FrameTypes.ts:36](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/FrameTypes.ts#L36)

___

### TextStyleUpdateType

Ƭ **TextStyleUpdateType**: { [key in keyof typeof SelectedTextStyles]?: Object }

#### Defined in

[types/TextStyleTypes.ts:53](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/TextStyleTypes.ts#L53)

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
| `type` | [`VariableType`](../enums/src.VariableType.md) |
| `value?` | `string` |

#### Defined in

[types/VariableTypes.ts:5](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/VariableTypes.ts#L5)

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

[types/VariableTypes.ts:19](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/VariableTypes.ts#L19)
