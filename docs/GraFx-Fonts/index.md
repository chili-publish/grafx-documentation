# Introduction

![applogo](../assets/CHILI_LOGOS_OK-07.svg)

The fonts application for [GraFx Studio](../GraFx-Studio/)

![asset](dashboard.png)

## Fonts for your applications

GraFx Fonts serves Fonts and Font families for GraFx Studio

GraFx Publisher Fonts [serves Fonts for GraFx Publisher](concepts/fonts-in-publisher/)

``` mermaid
erDiagram
  GraFx-Studio ||--|| GraFx-Fonts : "|"
  GraFx-Publisher ||--|| GraFx-Publisher-Fonts : "|"
  GraFx-Fonts {
  	has fonts
  	has Families
  }  
  GraFx-Publisher-Fonts {
  	has fonts
  }  
```