# JavaScript Color Manipulation Examples

### Add a color to the document
=== "PublisherInterface"
    ```javascript
    await publisher.executeFunction("document.colors", "Add");
    ```
=== "editorObject"
    ```javascript
    editorObject.ExecuteFunction("document.colors", "Add");
    ```

### Set a color property
Example properties: `c`, `m`, `y`, `k`, or `r`, `g`, `b`.
=== "PublisherInterface"
    ```javascript
    const colorName = "myColor";
    await publisher.setProperty(`document.colors[${colorName}]`, "k", 75);
    ```
=== "editorObject"
    ```javascript
    const colorName = "myColor";
    editorObject.SetProperty(`document.colors[${colorName}]`, "k", 75);
    ```


