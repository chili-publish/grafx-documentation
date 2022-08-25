[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [controllers/AnimationController](../modules/controllers_AnimationController.md) / AnimationController

# Class: AnimationController

[controllers/AnimationController](../modules/controllers_AnimationController.md).AnimationController

The AnimationController is responsible for all communication regarding Animations.
Methods inside this controller can be called by `window.SDK.animation.{method-name}`

## Methods

### getAnimationByFrameId

▸ **getAnimationByFrameId**(`frameId`, `layoutId?`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns an animation for a given frame and layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `layoutId?` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/AnimationController.ts:36](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/AnimationController.ts#L36)

___

### getAnimationsByLayoutId

▸ **getAnimationsByLayoutId**(`layoutId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns the animations for a given layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/AnimationController.ts:46](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/AnimationController.ts#L46)

___

### getAnimationsOnSelectedLayout

▸ **getAnimationsOnSelectedLayout**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns all animations on current layout

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/AnimationController.ts:25](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/AnimationController.ts#L25)

___

### pauseAnimation

▸ **pauseAnimation**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method triggers the animation to pause

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/AnimationController.ts:74](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/AnimationController.ts#L74)

___

### playAnimation

▸ **playAnimation**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method triggers the animation to play

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/AnimationController.ts:65](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/AnimationController.ts#L65)

___

### resetAnimation

▸ **resetAnimation**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method resets the layout's animations and animation duration to its initial state

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/AnimationController.ts:113](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/AnimationController.ts#L113)

___

### resetFrameAnimation

▸ **resetFrameAnimation**(`frameId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method resets the animation to its initial state

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The id of a certain frame |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/AnimationController.ts:104](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/AnimationController.ts#L104)

___

### setAnimationDuration

▸ **setAnimationDuration**(`timeInMS`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets the total and maximum duration of the animation

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `timeInMS` | `number` | The time expressed in miliseconds |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/AnimationController.ts:94](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/AnimationController.ts#L94)

___

### setFrameAnimation

▸ **setFrameAnimation**(`animation`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets the animation state for a certain Frame

#### Parameters

| Name | Type |
| :------ | :------ |
| `animation` | [`FrameAnimationPropertiesType`](../modules/index.md#frameanimationpropertiestype) |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/AnimationController.ts:56](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/AnimationController.ts#L56)

___

### setScrubberPosition

▸ **setScrubberPosition**(`timeInMS`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets the animation time to a certain time, expressed in miliseconds

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `timeInMS` | `number` | The time expressed in miliseconds |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/AnimationController.ts:84](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/AnimationController.ts#L84)
