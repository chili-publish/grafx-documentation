[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src](../modules/src.md) / EditorResponse

# Interface: EditorResponse<T\>

[src](../modules/src.md).EditorResponse

## Type parameters

| Name |
| :------ |
| `T` |

## Table of contents

### Properties

- [data](src.EditorResponse.md#data)
- [error](src.EditorResponse.md#error)
- [parsedData](src.EditorResponse.md#parseddata)
- [status](src.EditorResponse.md#status)
- [success](src.EditorResponse.md#success)

## Properties

### data

• `Optional` **data**: ``null`` \| `string`

#### Defined in

[types/CommonTypes.ts:39](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/CommonTypes.ts#L39)

___

### error

• `Optional` **error**: ``null`` \| `string` \| { `code`: `number` ; `error`: `Record`<`string`, `unknown`\>  }

#### Defined in

[types/CommonTypes.ts:40](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/CommonTypes.ts#L40)

___

### parsedData

• **parsedData**: ``null`` \| `T`

#### Defined in

[types/CommonTypes.ts:41](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/CommonTypes.ts#L41)

___

### status

• **status**: `number`

#### Defined in

[types/CommonTypes.ts:38](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/CommonTypes.ts#L38)

___

### success

• **success**: `boolean`

#### Defined in

[types/CommonTypes.ts:37](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/CommonTypes.ts#L37)
