[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/AnimationController](../modules/controllers_AnimationController.md) / AnimationController

# Class: AnimationController

[src/controllers/AnimationController](../modules/controllers_AnimationController.md).AnimationController

The AnimationController is responsible for all communication regarding Animations.
Methods inside this controller can be called by `window.SDK.animation.{method-name}`

## Table of contents

### Methods

- [getAnimationByFrameId](controllers_AnimationController.AnimationController.md#getanimationbyframeid)
- [getAnimationsByLayoutId](controllers_AnimationController.AnimationController.md#getanimationsbylayoutid)
- [getAnimationsOnSelectedLayout](controllers_AnimationController.AnimationController.md#getanimationsonselectedlayout)
- [pauseAnimation](controllers_AnimationController.AnimationController.md#pauseanimation)
- [playAnimation](controllers_AnimationController.AnimationController.md#playanimation)
- [resetAnimation](controllers_AnimationController.AnimationController.md#resetanimation)
- [resetFrameAnimation](controllers_AnimationController.AnimationController.md#resetframeanimation)
- [setAnimationDuration](controllers_AnimationController.AnimationController.md#setanimationduration)
- [setFrameAnimation](controllers_AnimationController.AnimationController.md#setframeanimation)
- [setScrubberPosition](controllers_AnimationController.AnimationController.md#setscrubberposition)

## Methods

### getAnimationByFrameId

▸ **getAnimationByFrameId**(`frameId`, `layoutId?`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameAnimationPropertiesType`](../modules/src.md#frameanimationpropertiestype)\>\>

This method returns an animation for a given frame and layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The ID of a specific frame |
| `layoutId?` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameAnimationPropertiesType`](../modules/src.md#frameanimationpropertiestype)\>\>

#### Defined in

[src/controllers/AnimationController.ts:39](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/AnimationController.ts#L39)

___

### getAnimationsByLayoutId

▸ **getAnimationsByLayoutId**(`layoutId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameAnimationPropertiesType`](../modules/src.md#frameanimationpropertiestype)\>\>

This method returns the animations for a given layout

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `layoutId` | `number` | The ID of a specific layout |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameAnimationPropertiesType`](../modules/src.md#frameanimationpropertiestype)\>\>

#### Defined in

[src/controllers/AnimationController.ts:51](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/AnimationController.ts#L51)

___

### getAnimationsOnSelectedLayout

▸ **getAnimationsOnSelectedLayout**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameAnimationPropertiesType`](../modules/src.md#frameanimationpropertiestype)[]\>\>

This method returns all animations on current layout

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameAnimationPropertiesType`](../modules/src.md#frameanimationpropertiestype)[]\>\>

#### Defined in

[src/controllers/AnimationController.ts:26](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/AnimationController.ts#L26)

___

### pauseAnimation

▸ **pauseAnimation**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method triggers the animation to pause

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/AnimationController.ts:85](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/AnimationController.ts#L85)

___

### playAnimation

▸ **playAnimation**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method triggers the animation to play

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/AnimationController.ts:76](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/AnimationController.ts#L76)

___

### resetAnimation

▸ **resetAnimation**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`unknown`\>\>

This method resets the layout's animations and animation duration to its initial state

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`unknown`\>\>

#### Defined in

[src/controllers/AnimationController.ts:124](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/AnimationController.ts#L124)

___

### resetFrameAnimation

▸ **resetFrameAnimation**(`frameId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`unknown`\>\>

This method resets the animation to its initial state

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frameId` | `number` | The id of a certain frame |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`unknown`\>\>

#### Defined in

[src/controllers/AnimationController.ts:115](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/AnimationController.ts#L115)

___

### setAnimationDuration

▸ **setAnimationDuration**(`timeInMS`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets the total and maximum duration of the animation

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `timeInMS` | `number` | The time expressed in miliseconds |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/AnimationController.ts:105](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/AnimationController.ts#L105)

___

### setFrameAnimation

▸ **setFrameAnimation**(`animation`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameAnimationPropertiesType`](../modules/src.md#frameanimationpropertiestype)\>\>

This method sets the animation state for a certain Frame

#### Parameters

| Name | Type |
| :------ | :------ |
| `animation` | [`FrameAnimationPropertiesType`](../modules/src.md#frameanimationpropertiestype) |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`FrameAnimationPropertiesType`](../modules/src.md#frameanimationpropertiestype)\>\>

#### Defined in

[src/controllers/AnimationController.ts:63](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/AnimationController.ts#L63)

___

### setScrubberPosition

▸ **setScrubberPosition**(`timeInMS`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`unknown`\>\>

This method sets the animation time to a certain time, expressed in miliseconds

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `timeInMS` | `number` | The time expressed in miliseconds |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`unknown`\>\>

#### Defined in

[src/controllers/AnimationController.ts:95](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/AnimationController.ts#L95)
