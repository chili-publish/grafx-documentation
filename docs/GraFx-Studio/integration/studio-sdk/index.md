# GraFx Studio SDK (from npm)

Now we've set up the structure, we can start building the integration.
To start we add the Studio SDK as a dependency to our project.

```
npm install --save @chili-publish/studio-sdk
```

!!! note
    Mind, we did NOT add **--save-dev** but only **--save**, since the SDK will be included in the final build as dependency.

See also [Studio SDK on Github](https://github.com/chili-publish/studio-sdk){target=_blank} for more information