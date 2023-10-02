# Introduction

![applogo](https://chilipublishdocs.imgix.net/logos/CHILI_LOGOS-Media-1.svg)

GraFx Media is the central repository to store your assets to be used in your Smart Templates.

GraFx Media uses the same repository for GraFx Publisher and GraFx Studio. This facilitates maintaining brand consistency throughout all your output.

![appscreen](dashboard.png)

## Media for all editors

``` mermaid
erDiagram
  GraFx-Studio ||--|{ GraFx-Media : "Has access to"
  GraFx-Publisher ||--|{ GraFx-Media : "Has access to"
  GraFx-Media {
  	handles Assets
  }  
```