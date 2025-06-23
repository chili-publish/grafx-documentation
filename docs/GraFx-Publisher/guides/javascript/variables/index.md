# JavaScript Variable Manipulation Examples

This page contains JavaScript snippets for working with variables in Publisher.

### Get all properties of a variable
=== "PublisherInterface"
    ```javascript
    const variableNameOrID = "myVar";
    await publisher.getObject(`document.variables[${variableNameOrID}]`);
    ```
=== "editorObject"
    ```javascript
    const variableNameOrID = "myVar";
    editorObject.GetObject(`document.variables[${variableNameOrID}]`);
    ```

### Set the value of a variable
This will work to set the value of most variables in Publisher. Variables such as the list variable or button bar don't have a "single" value, so this does not apply to them. Please see their specific page for more information.

=== "PublisherInterface"
    ```javascript
    const variableNameOrID = "myVar";
    await publisher.setProperty(`document.variables[${variableNameOrID}]`, "value", "New Value");
    ```
=== "editorObject"
    ```javascript
    const variableNameOrID = "myVar";
    editorObject.SetProperty(`document.variables[${variableNameOrID}]`, "value", "New Value");
    ```


### Create a new variable

This function will create a new variable within the document and return the ID of the variable. Please see the list below for the available `type` parameter options.
=== "PublisherInterface"
    ```javascript
    /**
    @param name - The name for the new variable
    @param type - The dataType for the variable
    **/
    async function createVariable(name, type) {
      const newVarID = (await publisher.executeFunction("document.variables", "Add")).id;
      await publisher.setProperty(`document.variables[${newVarID}]`, "name", name);
      await publisher.setProperty(`document.variables[${newVarID}]`, "dataType", type);
      return newVarID;
    }
    ```
=== "editorObject"
    ```javascript
    /**
    @param name - The name for the new variable
    @param type - The dataType for the variable
    **/
    function createVariable(name, type) {
      const newVarID = editorObject.ExecuteFunction("document.variables", "Add").id;
      editorObject.SetProperty(`document.variables[${newVarID}]`, "name", name);
      editorObject.SetProperty(`document.variables[${newVarID}]`, "dataType", type);
      return newVarID;
    }
    ```

###Variable Types

|Variable Type Name|dataType|
|------------------|--------|
|Short Text | "string"|
|Long Text | "longtext"|
|Formatted Text | "formattedtext"|
|Structured Text | "structuredtext"|
|Calculated Field | "calculated"|
|Image | "image"|
|Number | "number"|
|Checkbox | "checkbox"|
|Date | "date"|
|List | "list"|
|Table | "table"|
|Color | "color"|
|Paragraph Style | "paragraphstyle"|
|Character Style | "characterstyle"|
|Font | "font"|
|Coordinate | "coordinate"|
|Divider | "divider"|
|Button Bar | "buttonbar"|

### Get all variables in document
=== "PublisherInterface"
    ```javascript
    async function getVariables() {
      const varCount = (await publisher.getObject("document.variables.length")) - 1;
      let variables = [];
      for (let i = 0; i < varCount; i++) {
        /* Modify varData to extract whatever property you need*/
        const varData = await publisher.getObject(`document.variables[${i}]`)
        variables.push(varData);
      }
      return variables;
    }
    ```
=== "editorObject"
    ```javascript
    function getVariables() {
      const varCount = editorObject.GetObject("document.variables.length") - 1;
      let variables = [];
      for (let i = 0; i < varCount; i++) {
        /* Modify varData to extract whatever property you need*/
        const varData = editorObject.GetObject(`document.variables[${i}]`)
        variables.push(varData);
      }
      return variables;
    }
    ```


###Force variables in a frame to re-render
=== "PublisherInterface"
    ```javascript
    const frameTagOrID = "myFrame";
    await publisher.setProperty(`document.allFrames[${frameTagOrID}]`, "variablesUpdatedOnce", false);
    ```
=== "editorObject"
    ```javascript
    const frameTagOrID = "myFrame";
    editorObject.SetProperty(`document.allFrames[${frameTagOrID}]`, "variablesUpdatedOnce", false);
    ```

###Save document if all variables have values
=== "PublisherInterface"
    ```javascript
    async function validateAndSave() {
      let valid = true;
      const varCount = (await publisher.getObject('document.variables.count'))-1;

      for (let i = varCount; i >= 0; i--) {
        const variable = await publisher.getObject(`document.variables[${i}]`);
        if (variable.value == "")
          valid = false;
      }

      if (valid) {
        await publisher.executeFunction("document", "Save");
      } else {
        await publisher.alert("Please make sure that all require variables have a value.", "Save Failed");
      }
    }
    ```
=== "editorObject"
    ```javascript
    function validateAndSave() {
      let valid = true;
      const varCount = editorObject.GetObject('document.variables.count')-1;

      for (let i = varCount; i >= 0; i--) {
        const variable = editorObject.GetObject(`document.variables[${i}]`);
        if (variable.value == "")
          valid = false;
      }

      if (valid) {
        editorObject.ExecuteFunction("document", "Save");
      } else {
        editorObject.Alert("Please make sure that all require variables have a value.", "Save Failed");
      }
    }
    ```
