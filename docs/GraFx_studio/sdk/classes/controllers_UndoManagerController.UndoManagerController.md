# Class: UndoManagerController

[controllers/UndoManagerController](../modules/controllers_UndoManagerController.md).UndoManagerController

The UndoManagerController is responsible for all communication regarding the Undo-Manager.
Methods inside this controller can be called by `window.SDK.undoManager.{method-name}`

## Table of contents

### Methods

- [redo](controllers_UndoManagerController.UndoManagerController.md#redo)
- [undo](controllers_UndoManagerController.UndoManagerController.md#undo)

## Methods

### redo

▸ **redo**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method redoes the last operation

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/UndoManagerController.ts:33](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/UndoManagerController.ts#L33)

___

### undo

▸ **undo**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method undoes the last operation

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/UndoManagerController.ts:24](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/UndoManagerController.ts#L24)
