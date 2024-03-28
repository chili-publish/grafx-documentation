# Seciton 15: Implementing Preview Endpoints

This section addresses the issue of missing preview functionality for store interfaces by introducing new server-side code that handles preview requests, based on the file type (project or template).

**Objectives**

- Implement preview endpoint functionality in `server.js`.
- Develop the `getThumbnail` function within `chili.js`.

## 1. Adding the Preview Endpoint

Currently, the `store-front.html` and `store-admin.html` pages cannot load previews because they reference a nonexistent endpoint. To resolve this, add the following code snippet to `server.js`. This snippet creates an endpoint to handle preview requests for different file types.

```js
app.get("/preview/:type/:id", async (context) => {
  const userType = getUserType(context);

  if (userType == "unauth") {
    return context.text("Unauthorized", 401);
  }

  const {type, id} = context.req.param();

  const dangerousToken = await getDangerousToken(db);

  if (type == "project") {
    const previewFile = await getThumbnail({
      baseURL,
      environment,
      projectID: id,
      token: dangerousToken
    });

    return context.body(previewFile);
  }
  
  if (type == "template") {
      const previewFile = await getThumbnail({
        baseURL,
        environment,
        templateID: id,
        token: dangerousToken
      });

      return context.body(previewFile);
  }
  
});
```

This endpoint is unique to the other in that is has two URL parameters. The reason being is the preview URLs in CHILI are specific to the filetype: Tempalte or Project.

The `getThumbnail` function returns a stream which we will pass to the body of our response.

You can go ahead and add to your import from `chili.js` the `getThumbnail` function.

## 2. Downloading Previews

For our `chili.js` file we need to actually create the `getThumbnail function`.

```js
export async function getThumbnail({ projectID, templateID, token, baseURL, environment }) {

  let previewUrl = 
    (templateID == null) ?
      `${baseURL}/grafx/api/v1/environment/${environment}/projects/${projectID}/preview/thumbnail` :
      `${baseURL}/grafx/api/v1/environment/${environment}/templates/${templateID}/preview/thumbnail`;

  try {
    let response = await fetch(previewUrl, {
      method: 'GET',
      headers: {
        'Accept': 'image/png, application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (response.status === 200) {
      return await response.body
    } else if (response.status === 202) {
      const json = await response.json();
      const taskId = json.data.taskId;

      // Poll the taskInfo endpoint until the task is complete
      let taskResponse;
      do {
        // Wait before polling again to prevent excessive requests
        await new Promise(resolve => setTimeout(resolve, 1000)); 

        taskResponse = await fetch(`${baseURL}/grafx/api/v1/environment/${environment}/projects/preview/tasks/${taskId}`, {
          method: 'GET',
          headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${token}`
          }
        });

        if (taskResponse.status !== 200 && taskResponse.status !== 202) {
          throw new Error(`Task polling failed with status: ${taskResponse.status}`);
        }

      } while (taskResponse.status !== 200);

      const taskInfo = await taskResponse.json();
      const downloadUrl = taskInfo.links.download;

      // Download the final image using the download URL
      const downloadResponse = await fetch(downloadUrl, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });

      if (downloadResponse.status !== 200) {
        throw new Error(`Image download failed with status: ${downloadResponse.status}`);
      }

      return await downloadResponse.body
    } else {
      throw new Error(`Unexpected response status: ${response.status}`);
    }
  } catch (error) {
    console.error("Failed to get project thumbnail:", error);
    throw error;
  }
}
```

This new function is a bit long.

When you request a preview thumbnail for a project or template, the server doesn't always have it ready immediately. Sometimes, it needs to generate this thumbnail, which can take a little time. So, instead of giving you the image straight away, the server provides a task ID, which you can use to check back later to see if the image is ready.

This function will confirms that the image is ready to be downloaded. It uses the URL provided by the server to attempt to download the image.

If the image is successfully retrieved, it is returned so it can be shown in a user's browser. If something goes wrong—say, if the server responds with an error instead of the image—the function will throw an error, signaling that the download attempt failed. This error can then be used to troubleshoot what went wrong in the process.