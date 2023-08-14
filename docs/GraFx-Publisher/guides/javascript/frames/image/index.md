# Image frame manipulation examples

### Update an image frame
If you want to update an image frame to another image within your CHILI DAM, it is easier to link the image frame to a variable image and then [update the image variable value](../../variables/image/index.md). This method requires you having the full asset definition XML, the variable method only requires the item ID of the asset.

=== "PublisherInterface"
    ```javascript
    const frameTagOrID = "myImageFrame";
    const assetDefinitionXML = `SAVE ASSET XML OR FETCH WITH ResourceItemGetDefinitionXML`;
    await publisher.executeFunction(`document.allFrames[${frameTagOrID}]`, 'LoadContentFromXmlString', assetDefinitionXML);
    ```
=== "editorObject"
    ```javascript
    const frameTagOrID = "myImageFrame";
    const assetDefinitionXML = `SAVE ASSET XML OR FETCH WITH ResourceItemGetDefinitionXML`;
    editorObject.ExecuteFunction(`document.allFrames[${frameTagOrID}]`, 'LoadContentFromXmlString', assetDefinitionXML);
    ```

### Change fit mode of image
Fit modes include: "frame", "stretch", "manual", "proportional", "proportional_outside", "orig_size", and "smart_fit"
=== "PublisherInterface"
    ```javascript
    const frameTagOrID = "myImageFrame";
    await publisher.setProperty(`document.allFrames[${frameTagOrID}]`, "fitMode", "proportional_outside");
    ```
=== "editorObject"
    ```javascript
    const frameTagOrID = "myImageFrame";
    editorObject.SetProperty(`document.allFrames[${frameTagOrID}]`, "fitMode", "proportional_outside");
    ```

### Cropping Properties
=== "PublisherInterface"
    ```javascript
    /* Set the current frame to manual cropping so the values can be updated */
    await publisher.setProperty("document.selectedFrame", "fitMode", "manual");

    /* Set the value of the image cropped width and height */
    await publisher.setProperty("document.selectedFrame", "clipWidth", "34 mm");
    await publisher.setProperty("document.selectedFrame", "clipHeight", "35 mm");

    /* Set the position of the image in the frame */
    await publisher.setProperty("document.selectedFrame", "imgX", "34 mm");
    await publisher.setProperty("document.selectedFrame", "imgY", "35 mm");

    /* Set the scale of the image inside the frame */
    await publisher.setProperty("document.selectedFrame", "scaleX", "150");
    await publisher.setProperty("document.selectedFrame", "scaleY", "150");
    ```
=== "editorObject"
    ```javascript
    /* Set the current frame to manual cropping so the values can be updated */
    editor.SetProperty("document.selectedFrame", "fitMode", "manual");

    /* Set the value of the image cropped width and height */
    editor.SetProperty("document.selectedFrame", "clipWidth", "34 mm");
    editor.SetProperty("document.selectedFrame", "clipHeight", "35 mm");

    /* Set the position of the image in the frame */
    editor.SetProperty("document.selectedFrame", "imgX", "34 mm");
    editor.SetProperty("document.selectedFrame", "imgY", "35 mm");

    /* Set the scale of the image inside the frame */
    editor.SetProperty("document.selectedFrame", "scaleX", "150");
    editor.SetProperty("document.selectedFrame", "scaleY", "150");
    ```

### Clear image
=== "PublisherInterface"
    ```javascript
    const frameTagOrID = "myImageFrame";
    await publisher.executeFunction(`document.allFrames[${frameTagOrID}]`, "ClearContent");
    ```
=== "editorObject"
    ```javascript
    const frameTagOrID = "myImageFrame";
    editorObject.ExecuteFunction(`document.allFrames[${frameTagOrID}]`, "ClearContent");
    ```