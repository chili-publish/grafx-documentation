[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/UndoManagerController](../modules/controllers_UndoManagerController.md) / UndoManagerController

# Class: UndoManagerController

[src/controllers/UndoManagerController](../modules/controllers_UndoManagerController.md).UndoManagerController

The UndoManagerController is responsible for all communication regarding the Undo-Manager.
Methods inside this controller can be called by `window.SDK.undoManager.{method-name}`

## Table of contents

### Methods

- [redo](controllers_UndoManagerController.UndoManagerController.md#redo)
- [undo](controllers_UndoManagerController.UndoManagerController.md#undo)

## Methods

### redo

▸ **redo**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method redoes the last operation

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/UndoManagerController.ts:34](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/UndoManagerController.ts#L34)

___

### undo

▸ **undo**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method undoes the last operation

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/UndoManagerController.ts:25](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/UndoManagerController.ts#L25)
