# Date Variables

## Create a Date Variable

Under the Automate icon, click Variables, and add a variable with the "+" sign.

![screenshot](num0.png)

Choose "Date" as the Variable Type.

![screenshot-full](create-numbers.gif)

## Set the Variable Name

Double-click the name, or choose "Rename" under the "..." menu.

![screenshot](num2.png)

## Set General Properties

![screenshot-full](num1.png)

### Visible

Defines if the variable will be visible in the [Studio UI](/GraFx-Studio/concepts/template-management/#studio-ui) to the end user.

### Display Format

 * Supported date formats:
 * - Day -> `d`, `dd`
 * - Month -> `M`, `MM`, `MMM`, `MMMM`
 * - Year -> `yy`, `yyyy`
 * - Day of week -> `ccc`, `cccc`
 *
 * Examples for an input date of `10-12-1815`:
 * - Format `dd/MM/yyyy` will display `12/10/1815`
 * - Format `d.M.yy` will display `12.10.15`
 * - Format `d MMM yyyy` will display `12 Oct 1815` for the `en_US` language
 * - Format `MMMM d, yyyy` will display `October 12, 1815` for the `en_US` language
 * - Format `ccc, MMM d, yyyy` will display `Thu, Oct 12, 1815` for the `en_US` language
 * - Format `cccc, MMMM d, yyyy` will display `Thursday, October 12, 1815` for the `en_US` language
 * - Format `cccc, MMMM d, yyyy` will display `donderdag, oktober 12, 1815` for the `nl` language
 *
 * Patterns which output words such as `MM`, `MMM`, `MMMM`, `cc` and `ccc` will
 * differ depending on chosen language (default is `en_US`).
 
 
#### Display Format

qdfqsdf

#### Language

Will display the name of the month or day in the chosen language

Will work for patterns which output words such as `MM`, `MMM`, `MMMM`, `cc` and `ccc`. Default is `en_US`.

## Use in Actions

Different helper functions are available in Actions related to Date variables.

In Actions, you can use JavaScript to address the value and/or properties for date variables.

## Use in the API

Using the API, you can pass data in the form of JSON to populate the variables.

E.g. With the PDF Output endpoint, you can pass 1 set (or a full array) of variables. Dates can be passed as strings or native.

Example to pass 1 set of variables:

``` js
"variables": [
    {
        "var_text": "Single line of text",
        "var_image": "CHILI care soap",
        "var_number1": "45.674",
        "var_number2": 45.674
    }
```
Example to pass multiple sets of variables (for VDP output):

``` js
"variables": [
    {
        "var_text": "Single line of text",
        "var_image": "CHILI care soap",
        "var_number1": "45.674",
        "var_number2": 45.674
    },
    {
        "var_text": "Second line of text",
        "var_image": "CHILI care shampoo",
        "var_number1": "12.345",
        "var_number2": 12.345
    }
]
```

!!! Remark
    Don't pass thousand separators using JSON, only pass the actual numeric value.
