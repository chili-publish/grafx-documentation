# Section 2: Creating Store Pages

To set up the template store, we'll need the following 7 pages:

| Page   | Reason    |
|--------------- | --------------- |
| login.html   | Login as a user or admin |
| store-front.html   | For showing all the templates that a user can customize and then order   |
| editor.html | For opening a project in an editor |
| store-admin.html| A special admmin page for publishing and removing templates in our store |

!!! note

    We're using the same terminology as GraFx Studio for simplicity.

Run the following commands in your terminal to create the pages:

=== "Linux/macOS"
    ```SH
    mkdir public && touch public/login.html public/store-front.html public/editor.html public/store-admin.html
    ```
=== "Windows (PowerShell)"
    ```PowerShell
    mkdir public; ni public/login.html, public/store-front.html, public/editor.html, public/store-admin.html -ItemType File
    ```

These HTML files are empty for now but will be populated shortly in the follwing sections.

