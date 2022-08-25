[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [controllers/VariableController](../modules/controllers_VariableController.md) / VariableController

# Class: VariableController

[controllers/VariableController](../modules/controllers_VariableController.md).VariableController

The VariableController is responsible for all communication regarding the variables.
Methods inside this controller can be called by `window.SDK.variable.{method-name}`

## Methods

### addVariable

▸ **addVariable**(`parentId`, `variableType`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method adds a new variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `parentId` | `string` |
| `variableType` | [`VariableType`](../enums/index.VariableType.md) |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

The new created variable id

#### Defined in

[src/controllers/VariableController.ts:54](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L54)

___

### duplicateVariable

▸ **duplicateVariable**(`variableId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method creates a copy of a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:117](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L117)

___

### getVariableById

▸ **getVariableById**(`variableId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns a variable by id

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `variableId` | `string` | The ID of a specific variable |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:35](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L35)

___

### getVariableByName

▸ **getVariableByName**(`variableName`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns a variable by name

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `variableName` | `string` | The name of a specific variable |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:45](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L45)

___

### getVariables

▸ **getVariables**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns the list of variables

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:25](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L25)

___

### groupVariables

▸ **groupVariables**(`groupName`, `variableIds`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method aggregates the provided variables into a new group

#### Parameters

| Name | Type |
| :------ | :------ |
| `groupName` | `string` |
| `variableIds` | `string`[] |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:126](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L126)

___

### moveVariable

▸ **moveVariable**(`variableId`, `parentId`, `orderIndex`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method moves a variable's position

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `parentId` | `string` |
| `orderIndex` | `number` |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:144](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L144)

___

### moveVariables

▸ **moveVariables**(`movedVariables`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method changes positions of variables

#### Parameters

| Name | Type |
| :------ | :------ |
| `movedVariables` | [`VariableMoves`](../modules/index.md#variablemoves) |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:153](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L153)

___

### removeVariables

▸ **removeVariables**(`variableIds`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method removes a list of variables

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableIds` | `string`[] |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:63](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L63)

___

### setDefaultVariableValue

▸ **setDefaultVariableValue**(`variableId`, `value`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets a new value for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `value` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:99](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L99)

___

### setVariableIsHidden

▸ **setVariableIsHidden**(`variableId`, `isHidden`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets isHidden flag for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `isHidden` | `boolean` |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:162](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L162)

___

### setVariableIsReadonly

▸ **setVariableIsReadonly**(`variableId`, `isReadonly`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets isReadonly flag for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `isReadonly` | `boolean` |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:180](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L180)

___

### setVariableIsRequired

▸ **setVariableIsRequired**(`variableId`, `isRequired`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets isRequired flag for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `isRequired` | `boolean` |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:171](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L171)

___

### setVariableLabel

▸ **setVariableLabel**(`variableId`, `label`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets a new label for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `label` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:81](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L81)

___

### setVariableName

▸ **setVariableName**(`variableId`, `name`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets a new name for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `name` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:72](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L72)

___

### setVariableType

▸ **setVariableType**(`variableId`, `type`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets a new type for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `type` | [`VariableType`](../enums/index.VariableType.md) |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:90](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L90)

___

### setVariableValue

▸ **setVariableValue**(`variableId`, `value`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method sets a new value for a variable

#### Parameters

| Name | Type |
| :------ | :------ |
| `variableId` | `string` |
| `value` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:108](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L108)

___

### ungroupVariable

▸ **ungroupVariable**(`groupId`): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method dissolves the specified group

#### Parameters

| Name | Type |
| :------ | :------ |
| `groupId` | `string` |

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/VariableController.ts:135](https://github.com/chili-publish/editor-sdk/blob/c6e096c/src/controllers/VariableController.ts#L135)
