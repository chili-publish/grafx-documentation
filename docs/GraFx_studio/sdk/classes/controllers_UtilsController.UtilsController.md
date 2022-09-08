# Class: UtilsController

[controllers/UtilsController](../modules/controllers_UtilsController.md).UtilsController

The UtilsController exposes a set of usefull utilities that can be used to make some repeated tasks a bit easier
Methods inside this controller can be called by `window.SDK.utils.{method-name}`

## Table of contents

### Constructors

- [constructor](controllers_UtilsController.UtilsController.md#constructor)

### Methods

- [calculateFromString](controllers_UtilsController.UtilsController.md#calculatefromstring)
- [round](controllers_UtilsController.UtilsController.md#round)

## Constructors

### constructor

• **new UtilsController**()

## Methods

### calculateFromString

▸ **calculateFromString**(`val`, `precision?`): ``null`` \| `number`

This method can calculate what's inside a string that represents a calculation (f.e. "1 + 5 - 2" will result in 4)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `val` | `string` | the string value that needs to be calculated |
| `precision?` | `number` | the precision that the calculation should round to (f.e. if the return value is 5.012 and precision is 2, the endresult should be 5.01) 2 is also the default |

#### Returns

``null`` \| `number`

The calculated value or null in case that it can't be calculated

#### Defined in

[src/controllers/UtilsController.ts:14](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/UtilsController.ts#L14)

___

### round

▸ **round**(`val`, `precision?`): `number`

This method can round a value to a certain precision, default is 2

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `val` | `number` | the value that needs to be rounded |
| `precision?` | `number` | the precision of the rounding operation |

#### Returns

`number`

The rounded value as a number

#### Defined in

[src/controllers/UtilsController.ts:22](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/UtilsController.ts#L22)
