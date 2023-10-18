# Introduction

![applogo](/assets/CHILI_LOGOS_OK-07.svg)

Centralize your licensed fonts in a single location. GraFx Fonts is visually intuitive and easy to use.

![asset](dashboard.png)

## Fonts for your applications

GraFx Fonts serves Fonts and Font families for GraFx Studio

GraFx Publisher Fonts serves Fonts for GraFx Publisher

``` mermaid
erDiagram
  GraFx-Studio ||--|{ GraFx-Fonts : "Has access to"
  GraFx-Publisher ||--|{ GraFx-Publisher-Fonts : "Has access to"
  GraFx-Fonts {
  	handles Font-Families
  }  
  GraFx-Publisher-Fonts {
  	handles Fonts
  }  
```
