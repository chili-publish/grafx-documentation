[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/VariableController](../modules/controllers_VariableController.md) / VariableController

# Class: VariableController

[src/controllers/VariableController](../modules/controllers_VariableController.md).VariableController

The VariableController is responsible for all communication regarding the variables.
Methods inside this controller can be called by `window.SDK.variable.{method-name}`

## Table of contents

### Methods

- [addVariable](controllers_VariableController.VariableController.md#addvariable)
- [duplicateVariable](controllers_VariableController.VariableController.md#duplicatevariable)
- [getVariableById](controllers_VariableController.VariableController.md#getvariablebyid)
- [getVariableByName](controllers_VariableController.VariableController.md#getvariablebyname)
- [getVariables](controllers_VariableController.VariableController.md#getvariables)
- [groupVariables](controllers_VariableController.VariableController.md#groupvariables)
- [moveVariable](controllers_VariableController.VariableController.md#movevariable)
- [moveVariables](controllers_VariableController.VariableController.md#movevariables)
- [removeVariables](controllers_VariableController.VariableController.md#removevariables)
- [setDefaultVariableValue](controllers_VariableController.VariableController.md#setdefaultvariablevalue)
- [setVariableIsHidden](controllers_VariableController.VariableController.md#setvariableishidden)
- [setVariableIsReadonly](controllers_VariableController.VariableController.md#setvariableisreadonly)
- [setVariableIsRequired](controllers_VariableController.VariableController.md#setvariableisrequired)
- [setVariableLabel](controllers_VariableController.VariableController.md#setvariablelabel)
- [setVariableName](controllers_VariableController.VariableController.md#setvariablename)
- [setVariableType](controllers_VariableController.VariableController.md#setvariabletype)
- [setVariableValue](controllers_VariableController.VariableController.md#setvariablevalue)
- [ungroupVariable](controllers_VariableController.VariableController.md#ungroupvariable)

## Methods

### addVariable

▸ **addVariable**(`parentId`, `variableType`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

This method adds a new variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `parentId` | `string` |
| `variableType` | [`VariableType`](../enums/src.VariableType.md) |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

The new created variable id

#### Defined in

[src/controllers/VariableController.ts:55](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L55)

___

### duplicateVariable

▸ **duplicateVariable**(`variableId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

This method creates a copy of a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

#### Defined in

[src/controllers/VariableController.ts:118](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L118)

___

### getVariableById

▸ **getVariableById**(`variableId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`Variable`](../modules/src.md#variable)\>\>

This method returns a variable by id

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `variableId` | `string` | The ID of a specific variable |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`Variable`](../modules/src.md#variable)\>\>

#### Defined in

[src/controllers/VariableController.ts:36](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L36)

___

### getVariableByName

▸ **getVariableByName**(`variableName`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`Variable`](../modules/src.md#variable)\>\>

This method returns a variable by name

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `variableName` | `string` | The name of a specific variable |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`Variable`](../modules/src.md#variable)\>\>

#### Defined in

[src/controllers/VariableController.ts:46](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L46)

___

### getVariables

▸ **getVariables**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`Variable`](../modules/src.md#variable)[]\>\>

This method returns the list of variables

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<[`Variable`](../modules/src.md#variable)[]\>\>

#### Defined in

[src/controllers/VariableController.ts:26](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L26)

___

### groupVariables

▸ **groupVariables**(`groupName`, `variableIds`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

This method aggregates the provided variables into a new group

#### Parameters

| Name | Type |
| :------ | :------ |
| `groupName` | `string` |
| `variableIds` | `string`[] |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`string`\>\>

#### Defined in

[src/controllers/VariableController.ts:127](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L127)

___

### moveVariable

▸ **moveVariable**(`variableId`, `parentId`, `orderIndex`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method moves a variable's position

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `parentId` | `string` |
| `orderIndex` | `number` |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:145](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L145)

___

### moveVariables

▸ **moveVariables**(`movedVariables`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method changes positions of variables

#### Parameters

| Name | Type |
| :------ | :------ |
| `movedVariables` | [`VariableMoves`](../modules/src.md#variablemoves) |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:154](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L154)

___

### removeVariables

▸ **removeVariables**(`variableIds`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method removes a list of variables

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableIds` | `string`[] |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:64](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L64)

___

### setDefaultVariableValue

▸ **setDefaultVariableValue**(`variableId`, `value`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets a new value for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `value` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:100](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L100)

___

### setVariableIsHidden

▸ **setVariableIsHidden**(`variableId`, `isHidden`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets isHidden flag for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `isHidden` | `boolean` |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:165](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L165)

___

### setVariableIsReadonly

▸ **setVariableIsReadonly**(`variableId`, `isReadonly`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets isReadonly flag for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `isReadonly` | `boolean` |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:183](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L183)

___

### setVariableIsRequired

▸ **setVariableIsRequired**(`variableId`, `isRequired`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets isRequired flag for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `isRequired` | `boolean` |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:174](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L174)

___

### setVariableLabel

▸ **setVariableLabel**(`variableId`, `label`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets a new label for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `label` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:82](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L82)

___

### setVariableName

▸ **setVariableName**(`variableId`, `name`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets a new name for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `name` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:73](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L73)

___

### setVariableType

▸ **setVariableType**(`variableId`, `type`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets a new type for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `type` | [`VariableType`](../enums/src.VariableType.md) |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:91](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L91)

___

### setVariableValue

▸ **setVariableValue**(`variableId`, `value`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method sets a new value for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `value` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:109](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L109)

___

### ungroupVariable

▸ **ungroupVariable**(`groupId`): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method dissolves the specified group

#### Parameters

| Name | Type |
| :------ | :------ |
| `groupId` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/VariableController.ts:136](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/VariableController.ts#L136)
