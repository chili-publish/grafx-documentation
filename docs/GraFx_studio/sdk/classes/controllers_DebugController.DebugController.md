# Class: DebugController

[controllers/DebugController](../modules/controllers_DebugController.md).DebugController

The DebugController is responsible for all communication regarding Debugging.
Methods inside this controller can be called by `window.SDK.debug.{method-name}`

## Table of contents

### Methods

- [disableDebug](controllers_DebugController.DebugController.md#disabledebug)
- [enableDebug](controllers_DebugController.DebugController.md#enabledebug)
- [getLogs](controllers_DebugController.DebugController.md#getlogs)
- [toggleDebugPanel](controllers_DebugController.DebugController.md#toggledebugpanel)

## Methods

### disableDebug

▸ **disableDebug**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method disables the debugging

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/DebugController.ts:51](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/DebugController.ts#L51)

___

### enableDebug

▸ **enableDebug**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method enables the debugging

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/DebugController.ts:42](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/DebugController.ts#L42)

___

### getLogs

▸ **getLogs**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method returns all debug logs

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/DebugController.ts:24](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/DebugController.ts#L24)

___

### toggleDebugPanel

▸ **toggleDebugPanel**(): `Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

This method toggles the showcase of debug panel

#### Returns

`Promise`<[`EditorResponse`](../modules/index.md#editorresponse)\>

#### Defined in

[src/controllers/DebugController.ts:33](https://github.com/chili-publish/editor-sdk/blob/6abb55e/src/controllers/DebugController.ts#L33)
