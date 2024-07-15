# Date Variables

## Create a Date Variable

Under the Automate icon, click Variables, and add a variable with the "+" sign.

![screenshot](date0.png)

Choose "Date" as the Variable Type.

## Set the Variable Name

Double-click the name, or choose "Rename" under the "..." menu.

![screenshot](date1.png)

## Set General Properties

![screenshot-full](date2.png)

### Visible

Defines if the variable will be visible in the [Studio UI](/GraFx-Studio/concepts/template-management/#studio-ui) to the end user.

### Display Format

A date can be displayed in several formats, depending on the local preferences. You can set a formatting string, how to display the date.

The formatting can be empty, and will then default to "dd/MM/yyyy"

**Format**

Supported date formats

- Day -> `d`, `dd`
- Month -> `M`, `MM`, `MMM`, `MMMM`
- Year -> `yy`, `yyyy`
- Day of week -> `ccc`, `cccc`

[See Github](https://unicode-org.github.io/icu/userguide/format_parse/datetime/) for ICO formatting. (Only the above formats are supported)

Examples for an input date of `10-12-1815`

- Format `dd/MM/yyyy` will display `12/10/1815`
- Format `d.M.yy` will display `12.10.15`
- Format `d MMM yyyy` will display `12 Oct 1815` for the `en_US` language
- Format `MMMM d, yyyy` will display `October 12, 1815` for the `en_US` language
- Format `ccc, MMM d, yyyy` will display `Thu, Oct 12, 1815` for the `en_US` language
- Format `cccc, MMMM d, yyyy` will display `Thursday, October 12, 1815` for the `en_US` language
- Format `cccc, MMMM d, yyyy` will display `donderdag, oktober 12, 1815` for the `nl` language
	
**Language**

Will display the name of the month or day in the chosen language

Will work for patterns which output words such as `MM`, `MMM`, `MMMM`, `cc` and `ccc`. Default is `en_US`.

## Use in Actions

Different helper functions are available in Actions related to Date variables.

In Actions, you can use JavaScript to address the value and/or properties for date variables.

- getDateVariableValue
- setDateVariableValue
- setDateVariableDisplayFormat (see Display Format above)
- setDateVariableLanguage

## Use in the API

Using the API, you can pass data in the form of JSON to populate the variables.

E.g. With the PDF Output endpoint, you can pass 1 set (or a full array) of variables. Dates can be passed as strings.

``` js
	# Format to be used: yyyy-MM-dd
	{
		"var_date": "2024-07-15"
	}
```

Example to pass 1 set of variables:

``` js
"variables": [
    {
        "var_text": "Single line of text",
        "var_image": "CHILI care soap",
        "var_date": "2024-07-15"
    }
```
Example to pass multiple sets of variables (for VDP output):

``` js
"variables": [
    {
        "var_text": "Single line of text",
        "var_image": "CHILI care soap",
        "var_date": "2024-07-15"
    },
    {
        "var_text": "Second line of text",
        "var_image": "CHILI care shampoo",
        "var_date": "2024-07-19"
    }
]
```

!!! Remark
    Only pass a date, no time
