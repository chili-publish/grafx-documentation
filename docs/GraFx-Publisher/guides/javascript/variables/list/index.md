#List Variable Manipulation Examples
These JavaScript snippets are more specific to the `List` variable type.

### Get the name of the currently selected item
=== "PublisherInterface"
    ```javascript
    const variableNameOrID = "myVar";
    await publisher.getObject(`document.variables[${variableNameOrID}].selectedItemName`);
    ```
=== "editorObject"
    ```javascript
    const variableNameOrID = "myVar";
    editorObject.GetObject(`document.variables[${variableNameOrID}].selectedItemName`);
    ```

### Set the currently selected item
=== "PublisherInterface"
    ```javascript
    const variableNameOrID = "myVar";
    await publisher.setProperty(`document.variables[${variableNameOrID}]`, "value", "Selection Name");
    ```
=== "editorObject"
    ```javascript
    const variableNameOrID = "myVar";
    editorObject.SetProperty(`document.variables[${variableNameOrID}]`, "value", "Selection Name");
    ```

### Create options for list variable
This function takes a list variable reference and a JavaScript array of values to add to that list variable.
=== "PublisherInterface"
    ```javascript
    /**
      @param listVariable - The name or ID of a list variable
      @param values - An array of values to be inserted to the list variable
    **/
    async function setListValues(listVariable, values) {
      for (val of values) {
        const rowID = (await publisher.executeFunction(`document.variables[${listVariable}].listItems`, "Add")).id;
        await publisher.setProperty(`document.variables[${listVariable}].listItems[${rowID}]`, "name", val);
        await publisher.setProperty(`document.variables[${listVariable}].listItems[${rowID}]`, "value", val);
      }
    }
    ```
=== "editorObject"
    ```javascript
    /**
      @param listVariable - The name or ID of a list variable
      @param values - An array of values to be inserted to the list variable
    **/
    function setListValues(listVariable, values) {
      for (val of values) {
        const rowID = editorObject.ExecuteFunction(`document.variables[${listVariable}].listItems`, "Add").id;
        editorObject.SetProperty(`document.variables[${listVariable}].listItems[${rowID}]`, "name", val);
        editorObject.SetProperty(`document.variables[${listVariable}].listItems[${rowID}]`, "value", val);
      }
    }
    ```

### Get the currently selected items for a multi-select list
=== "PublisherInterface"
    ```javascript
    async function getSelectedItems(listVariable) {
      let selected = [];
      const listLength = await publisher.getObject(`document.variables[${listVariable}].listItems.count`);
      for (let i = 0; i < listLength; i++) {
        const item = await publisher.getObject(`document.variables[${listVariable}].listItems[${i}]`);
        if (item.isSelected == 'true')
          selected.push(item.name);
      }
      return selected;
    }
    ```
=== "editorObject"
    ```javascript
    function getSelectedItems(listVariable) {
      let selected = [];
      const listLength = editorObject.GetObject(`document.variables[${listVariable}].listItems.count`);
      for (let i = 0; i < listLength; i++) {
        const item = editorObject.GetObject(`document.variables[${listVariable}].listItems[${i}]`);
        if (item.isSelected == 'true')
          selected.push(item.name);
      }
      return selected;
    }
    ```

### Select list items based on array
=== "PublisherInterface"
    ```javascript
    /**
      @param listVariable - The name or ID of a list variable
      @param items - A list of item names to select
    **/
    async function selectListItems(listVariable, items) {
      const listLength = await publisher.getObject(`document.variables[${listVariable}].listItems.count`);
      for (let i = 0; i < listLength; i++) {
        if (items.includes((await publisher.getObject(`document.variables[${listVariable}].listItems[${i}].value`))))
          await publisher.setProperty(`document.variables[${listVariable}].listItems[${i}]`, "isSelected", "true");
      }
    }
    ```
=== "editorObject"
    ```javascript
    /**
      @param listVariable - The name or ID of a list variable
      @param items - A list of item names to select
    **/
    function selectListItems(listVariable, items) {
      const listLength = editorObject.GetObject(`document.variables[${listVariable}].listItems.count`);
      for (let i = 0; i < listLength; i++) {
        if (items.includes(editorObject.GetObject(`document.variables[${listVariable}].listItems[${i}].value`)))
        editorObject.SetProperty(`document.variables[${listVariable}].listItems[${i}]`, "isSelected", "true");
      }
    }
    ```




