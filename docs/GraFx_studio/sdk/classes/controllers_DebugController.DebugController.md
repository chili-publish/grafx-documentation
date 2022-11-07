[@chili-publish/editor-sdk](../README.md) / [Modules](../modules.md) / [src/controllers/DebugController](../modules/controllers_DebugController.md) / DebugController

# Class: DebugController

[src/controllers/DebugController](../modules/controllers_DebugController.md).DebugController

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

▸ **disableDebug**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method disables the debugging

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/DebugController.ts:53](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/DebugController.ts#L53)

___

### enableDebug

▸ **enableDebug**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method enables the debugging

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/DebugController.ts:44](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/DebugController.ts#L44)

___

### getLogs

▸ **getLogs**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`DebugData`[]\>\>

This method returns all debug logs

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<`DebugData`[]\>\>

#### Defined in

[src/controllers/DebugController.ts:26](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/DebugController.ts#L26)

___

### toggleDebugPanel

▸ **toggleDebugPanel**(): `Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

This method toggles the showcase of debug panel

#### Returns

`Promise`<[`EditorResponse`](../interfaces/src.EditorResponse.md)<``null``\>\>

#### Defined in

[src/controllers/DebugController.ts:35](https://github.com/chili-publish/editor-sdk/blob/bc89ed1/src/controllers/DebugController.ts#L35)
