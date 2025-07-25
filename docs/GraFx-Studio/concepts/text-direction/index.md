# Text Direction

GraFx Studio supports both left-to-right (LTR) and right-to-left (RTL) text directions, enabling you to work seamlessly in languages such as English, Dutch, Arabic, ...

## Automatic direction

GraFx Studio applies the Unicode Bidirectional Algorithm to determine whether a run of text is LTR or RTL. No extra UI controls are needed to “switch” direction.
Arabic script, for example, will render RTL automatically.  
  
## Manual alignment

Horizontal alignment (left, center, right) remains a user-driven setting. You can choose left or right alignment independent of text direction via the existing alignment controls.

## Scope of support

- Static text on canvas  
- Text variable values  
- List variable item names  
- Variable prefix & suffix  
- All input fields (text, list variables, prefix/suffix) accept RTL characters, though input is always left-aligned in the editor
- All output formats