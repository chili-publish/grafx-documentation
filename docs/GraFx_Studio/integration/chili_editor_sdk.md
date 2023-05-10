# CHILI Editor SDK (from npm)

Now we’ve set up the structure, we can start building the integration.
To start we add the Editor SDK as a dependency to our project.

```
npm install --save @chili-publish/studio-sdk
```

!!! note
    Mind, we did NOT add **--save-dev** but only **--save**, since the SDK will be included in the final build as dependency.

See also [Editor SDK on Github](https://github.com/chili-publish/studio-sdk){target=_blank} for more information

## Integration documentation

The integration documentation regarding all available calls, are available in our github repository page.
Just go visit [this page](https://chili-publish.github.io/studio-sdk/), and you'll find a ton of information on available methods, listeners and types.