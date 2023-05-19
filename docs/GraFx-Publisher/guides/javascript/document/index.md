# JavaScript Document Manipulation Examples

### Get the name of the document
=== "PublisherInterface"
    ```javascript
    await publisher.getObject("document.name");
    ```
=== "editorObject"
    ```javascript
    editorObject.GetObject("document.name");
    ```

### Get the XML of the document currently in the editor
=== "PublisherInterface"
    ```javascript
    await publisher.executeFunction("document", "GetTempXML");
    ```
=== "editorObject"
    ```javascript
    editorObject.ExecuteFunction("document", "GetTempXML");
    ```

### Load a document in to the editor
=== "PublisherInterface"
    ```javascript
    /* publisherDocument can be either a document ID or document XML*/
    const publisherDocument = `document id or xml`;
    await publisher.executeFunction('document','OpenDocumentFromXml', publisherDocument);
    ```
=== "editorObject"
    ```javascript
    /* publisherDocument can be either a document ID or document XML*/
    const publisherDocument = `document id or xml`;
    editor.ExecuteFunction('document','OpenDocumentFromXml', publisherDocument);
    ```

  You can optionally include a Workspace ID and/or View Preferences ID to load with the document
=== "PublisherInterface"
    ```javascript
    const publisherDocument = `document id or xml`;
    const workspaceID = `itemID of Workspace`;
    const viewPreferencesID = `itemID of View Preferences`;
    await publisher.executeFunction('document','OpenDocumentFromXml', publisherDocument, workspaceID, viewPreferencesID);
    ```
=== "editorObject"
    ```javascript
    const publisherDocument = `document id or xml`;
    const workspaceID = `itemID of Workspace`;
    const viewPreferencesID = `itemID of View Preferences`;
    editorObject.ExecuteFunction('document','OpenDocumentFromXml', publisherDocument, workspaceID, viewPreferencesID);
    ```

### Save document
=== "PublisherInterface"
    ```javascript
    await publisher.executeFunction("document", "Save");
    ```
=== "editorObject"
    ```javascript
    editorObject.ExecuteFunction("document", "Save");
    ```

### Rotate document
=== "PublisherInterface"
    ```javascript
    await publisher.setProperty("document.viewPreferences", "rotateView", 180);
    ```
=== "editorObject"
    ```javascript
    editorObject.SetProperty("document.viewPreferences", "rotateView", 180);
    ```

### Freeze undo manager
=== "PublisherInterface"
    ```javascript
    /* If set to true, changes are no longer tracked */
    await publisher.setProperty("doc.undoManager", "holdChanges", true);
    ```
=== "editorObject"
    ```javascript
    /* If set to true, changes are no longer tracked */
    editorObject.SetProperty("doc.undoManager", "holdChanges", true);
    ```

### Get mouse position
=== "PublisherInterface"
    ```javascript
    /* Returns the x, y and current page of the mouse cursor */
    await publisher.executeFunction("document", "GetMousePosition");
    ```
=== "editorObject"
    ```javascript
    /* Returns the x, y and current page of the mouse cursor */
    editorObject.ExecuteFunction("document", "GetMousePosition");
    ```