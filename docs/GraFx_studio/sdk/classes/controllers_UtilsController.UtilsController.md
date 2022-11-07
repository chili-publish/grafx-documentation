[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/UtilsController](../modules/controllers_UtilsController.md) / UtilsController

# Class: UtilsController

[src/controllers/UtilsController](../modules/controllers_UtilsController.md).UtilsController

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

▸ **calculateFromString**(`val`, `precision?`): [`EditorResponse`](../interfaces/src.EditorResponse.md)<`number`\>

This method can calculate what's inside a string that represents a calculation (f.e. "1 + 5 - 2" will result in 4)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `val` | `string` | the string value that needs to be calculated |
| `precision?` | `number` | the precision that the calculation should round to (f.e. if the return value is 5.012 and precision is 2, the endresult should be 5.01) 2 is also the default |

#### Returns

[`EditorResponse`](../interfaces/src.EditorResponse.md)<`number`\>

The calculated value or null in case that it can't be calculated

#### Defined in

[src/controllers/UtilsController.ts:15](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/UtilsController.ts#L15)

___

### round

▸ **round**(`val`, `precision?`): [`EditorResponse`](../interfaces/src.EditorResponse.md)<`number`\>

This method can round a value to a certain precision, default is 2

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `val` | `number` | the value that needs to be rounded |
| `precision?` | `number` | the precision of the rounding operation |

#### Returns

[`EditorResponse`](../interfaces/src.EditorResponse.md)<`number`\>

The rounded value as a number

#### Defined in

[src/controllers/UtilsController.ts:29](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/UtilsController.ts#L29)
