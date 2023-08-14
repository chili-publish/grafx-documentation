# JavaScript Frame Manipulation Examples

### Add a frame to the document
To see a list of frame types, [please see Frame Types](types/index.md)
=== "PublisherInterface"
    ```javascript
    const addFrame = async (page, type, x, y, width, height) => {
      const frame = await publisher.executeFunction(`document.pages[${page}].frames`, "Add", type, x, y, width, height);
      return frame.id;
    }

    /* Example Usage (makes sure this is used in an async function) */
    const newFrame = await addFrame(0, "text", "10 mm", "10 mm", "100 mm", "50 mm");
    ```
=== "editorObject"
    ```javascript
    const addFrame = (page, type, x, y, width, height) => {
      const frame = editorObject.ExecuteFunction(`document.pages[${page}].frames`, "Add", type, x, y, width, height);
      return frame.id;
    }

    /* Example Usage */
    const newFrame = addFrame(0, "text", "10 mm", "10 mm", "100 mm", "50 mm");
    ```