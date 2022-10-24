[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / types/MediaConnectorTypes

# Module: types/MediaConnectorTypes

## Table of contents

### Enumerations

- [MediaDownloadType](../enums/types_MediaConnectorTypes.MediaDownloadType.md)

### Type Aliases

- [Media](types_MediaConnectorTypes.md#media)
- [MediaPage](types_MediaConnectorTypes.md#mediapage)

## Type Aliases

### Media

Ƭ **Media**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `id` | `string` |
| `metaData` | `Map`<`string`, `string`\> |
| `name` | `string` |
| `relativePath` | `string` |
| `type` | [`MediaType`](../enums/src.MediaType.md) |

#### Defined in

[types/MediaConnectorTypes.ts:8](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/MediaConnectorTypes.ts#L8)

___

### MediaPage

Ƭ **MediaPage**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `data` | [`Media`](types_MediaConnectorTypes.md#media)[] |
| `nextPageToken?` | `string` |

#### Defined in

[types/MediaConnectorTypes.ts:16](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/types/MediaConnectorTypes.ts#L16)
