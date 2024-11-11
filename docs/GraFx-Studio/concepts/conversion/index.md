# Conversion of Desktop files

## Intro

Imagine the scenario where you have a design created in a Desktop application. This file should be the basis for your Smart Template.

AN easy design could be recreated in GraFx Studio, for a more complex file it would be handy to have a conversion from your existing file to GraFx Studio.

That is wat a conversion does.

## Intermediate File Format

To accomodate several application, we designed the process to enable Desktop applications to export to an Intermediate File Format.

Once in GraFx Studio, you can import the file you (or a plugin) created into GraFx Studio.

## Process

### Export with plugin

For these applications, we created plugins to export to the Intermediate File Format.

The plugin will create a zip file, with the Intermediate File, and all relevant assets.

### Import on CHILI GraFx

Once in GraFx Studio, you can import the exported (zip) file.

![screenshot](plugin1.png)

## Limitations

Due to the nature of each desktop applications, not all features are supported.

It's best to check the features you need, and adjust where necessary.

Where possible, the plugin will create a flattened asset in the highest resolution, to get as close as possible.