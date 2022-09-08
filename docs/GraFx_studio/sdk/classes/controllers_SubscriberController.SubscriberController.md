# Class: SubscriberController

[controllers/SubscriberController](../modules/controllers_SubscriberController.md).SubscriberController

The SubscriberController is responsible for all listeners which can influence the aplication-state from outside.
Callbacks inside this controller can be set by `window.SDK.subscriber.{method-name}`

## Table of contents

### Methods

- [onAnimationChanged](controllers_SubscriberController.SubscriberController.md#onanimationchanged)
- [onAnimationPlaybackChanged](controllers_SubscriberController.SubscriberController.md#onanimationplaybackchanged)
- [onColorsChanged](controllers_SubscriberController.SubscriberController.md#oncolorschanged)
- [onPageSelectionChanged](controllers_SubscriberController.SubscriberController.md#onpageselectionchanged)
- [onParagraphStylesChanged](controllers_SubscriberController.SubscriberController.md#onparagraphstyleschanged)
- [onSelectedFrameContentChanged](controllers_SubscriberController.SubscriberController.md#onselectedframecontentchanged)
- [onSelectedFrameLayoutChanged](controllers_SubscriberController.SubscriberController.md#onselectedframelayoutchanged)
- [onSelectedLayoutFramesChanged](controllers_SubscriberController.SubscriberController.md#onselectedlayoutframeschanged)
- [onSelectedLayoutPropertiesChanged](controllers_SubscriberController.SubscriberController.md#onselectedlayoutpropertieschanged)
- [onSelectedTextStyleChanged](controllers_SubscriberController.SubscriberController.md#onselectedtextstylechanged)
- [onSelectedToolChanged](controllers_SubscriberController.SubscriberController.md#onselectedtoolchanged)
- [onStateChanged](controllers_SubscriberController.SubscriberController.md#onstatechanged)
- [onUndoStateChanged](controllers_SubscriberController.SubscriberController.md#onundostatechanged)
- [onVariableListChanged](controllers_SubscriberController.SubscriberController.md#onvariablelistchanged)

## Methods

### onAnimationChanged

▸ **onAnimationChanged**(`animation`): `void`

Listener on when a certain animation gets changed

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `animation` | `string` | Stringified array of FrameAnimationType |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:25](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L25)

___

### onAnimationPlaybackChanged

▸ **onAnimationPlaybackChanged**(`animationPlaybackState`): `void`

Listener on the playbackstate of the animation, it contains the current time of the playback (in miliseconds) and a flag that describes if the animation is currently playing

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `animationPlaybackState` | `string` | Stringified array of AnimationPlaybackType |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:34](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L34)

___

### onColorsChanged

▸ **onColorsChanged**(`colors`): `void`

Listener on the state of the currently selected color's styles, if this changes, this listener will get triggered with the updates

#### Parameters

| Name | Type |
| :------ | :------ |
| `colors` | `string` |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:132](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L132)

___

### onPageSelectionChanged

▸ **onPageSelectionChanged**(): `void`

To be implemented, gets triggered when clicking on the pageTitle on the canvas.

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:78](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L78)

___

### onParagraphStylesChanged

▸ **onParagraphStylesChanged**(`paragraphStyles`): `void`

Listener on paragraph styles, if this changes, this listener will get triggered with the updates

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `paragraphStyles` | `string` | Stringified object of paragraph styles |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:141](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L141)

___

### onSelectedFrameContentChanged

▸ **onSelectedFrameContentChanged**(`frame`): `void`

Listener on the state of the currently selected frame, it contains some basic information on the type of frame it is

#### Parameters

| Name | Type |
| :------ | :------ |
| `frame` | `string` |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:61](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L61)

___

### onSelectedFrameLayoutChanged

▸ **onSelectedFrameLayoutChanged**(`frame`): `void`

Listener on the state of the currently selected frame, if this changes, this listener will get triggered with the updates

#### Parameters

| Name | Type |
| :------ | :------ |
| `frame` | `string` |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:52](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L52)

___

### onSelectedLayoutFramesChanged

▸ **onSelectedLayoutFramesChanged**(`frames`): `void`

Listener on the state of the currently selected layout's frames, if this changes, this listener will get triggered with the updates

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frames` | `string` | Stringified object of Frames |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:114](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L114)

___

### onSelectedLayoutPropertiesChanged

▸ **onSelectedLayoutPropertiesChanged**(`properties`): `void`

Listener on the state of the currently selected layout, if its properties are changed, this listener will get triggered with the new properties

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `properties` | `string` | Stringified object of LayoutPropertiesType |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:43](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L43)

___

### onSelectedTextStyleChanged

▸ **onSelectedTextStyleChanged**(`styles`): `void`

Listener on the state of the currently selected text's styles, if this changes, this listener will get triggered with the updates

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `styles` | `string` | Stringified object of styles |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:123](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L123)

___

### onSelectedToolChanged

▸ **onSelectedToolChanged**(`tool`): `void`

Listener on when the tool has changed by the canvas

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `tool` | `string` | The string representation of a certain tool |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:96](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L96)

___

### onStateChanged

▸ **onStateChanged**(`document`): `void`

A listener on the general state of the document, gets triggered everytime a change is done on the document. Use with care, very expensive operation

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `document` | `string` | String value of the document, typed as InitialStateType |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:70](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L70)

___

### onUndoStateChanged

▸ **onUndoStateChanged**(`undoState`): `void`

Listener on state changes

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `undoState` | `string` | Stringified object of UndoState |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:105](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L105)

___

### onVariableListChanged

▸ **onVariableListChanged**(`variablesJson`): `void`

Listener on when variables change

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `variablesJson` | `string` | Stringified array of Variable |

#### Returns

`void`

#### Defined in

[src/controllers/SubscriberController.ts:87](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/SubscriberController.ts#L87)
