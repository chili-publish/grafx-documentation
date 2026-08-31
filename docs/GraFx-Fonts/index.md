# ![GraFx Fonts logo](/assets/icon-GraFx-Fonts.svg){.applogo-inline} GraFx Fonts

The fonts application for [GraFx Studio](/GraFx-Studio/)

![The GraFx Fonts library as a grid of font cards, each previewing the pangram sentence](dashboard.png){.screenshot-full}

## Fonts for your applications

GraFx Fonts serves Fonts and Font families for GraFx Studio

GraFx Publisher Fonts [serves Fonts for GraFx Publisher](/GraFx-Fonts/concepts/fonts-in-publisher/)

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