# Section 14: Order Handling

This section provides a detailed guide on handling and managing orders within our example project.

**Objectives**
- Understand the process of order handling in the project.
- Implement the order checking and completion functionalities.
- Test the order processing workflow.

## 1. Handling Orders

In a live environment, order processing would typically involve a separate service responsible for file downloads and subsequent delivery to a Digital Asset Management (DAM) system or printer. For the sake of simplicity in our demonstration, we will periodically check the completion status of orders using a timed loop.

Insert the following snippet into your `server.js` file:

```js
// Check orders every 1 minute to see if any are complete and download them. 
setInterval(async ()=>{

  console.log("Checking orders");

  const orders = db.getOrders();

  const token = await getDangerousToken(db);

  for (const order of orders) {

    db.removeOrder(order.taskID);
    const result = await orderDone({taskID: order.taskID, baseURL, environment, token});

    if (typeof result == "string") {
      console.log("Failed Task:" + result);
    }

    if (result == false) {
      db.addOrder(order.taskID);
    }
  }
}, 60000);
```
This code will:
- Remove the order from the database.
- Invoke the `orderDone` function to check if the task is complete.
    - If `true`, the task is done and `orderDone` will download the file.
    - If `false`, the task is not done, and will be readded to the database.
    - If a string, the task failed, and we throw and error. 

!!! note

    In a production application, it is a good idea to handle failed tasks by logging the error message, taskID, projectID, and any other info that would be useful in the investigation.

## 2. Order Completion Verification

In the `chili.js` file, define a new function `orderDone` as shown:

```js
export async function orderDone({ taskID, token, baseURL, environment}) {
  const taskUrl = `${baseURL}/grafx/api/v1/environment/${environment}/output/tasks/${taskID}`;

  try {
    const response = await fetch(taskUrl, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (response.status === 200) {
      const jsonResponse = await response.json();
      const downloadLink = jsonResponse.links.download;
      const ordersDir = "./orders/";
      const filePath = `${ordersDir}${taskID}.png`;

      // Download and save the file
      const downloadResponse = await fetch(downloadLink, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        }
      );
      const fileStream = fs.createWriteStream(filePath);
      await await pipeline(downloadResponse.body, fileStream);

      return true;
    } else if (response.status === 204) {
      return false;
    } else {
      if (response.status == 500) {
        return `Error: Task failed ${await response.text()}`;
      }
      else {
        return `Error: Received unexpected status code ${response.status}`;
      }
    }
  } catch (error) {
    console.error("Failed to process order:", error);
    return `Error: ${error.message}`;
  }
}
```

This function performs the following actions:
- Calls an API endpoint to check the task status using `taskID`.
- On task completion, downloads the file and saves it to the `orders` directory.
- Handles various HTTP response scenarios, returning a boolean or error message.

By the way, make sure you add a `orders` folder to avoid filesystem errors when writing the completed task.

```sh
mkdir orders
```

Also don't forget to import `orderDone` into `server.js`.

## 3. Test

To verify the functionality of your order processing:

1. Restart the server by running `node server.js`.
2. Ensure `database.json` contains several orders. If not, populate it by simulating order creation in your workflow.
3. Adjust the checking interval in `server.js` if you prefer not to wait one minute between checks.
4. Observe the "Checking orders" log in the console to confirm operation, and then locate the downloaded order files in the `orders` directory.

