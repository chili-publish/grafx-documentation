# CHILI GraFx Product documentation

<video width="690" height="388" autoplay="true" loop="true" muted="true">
  <source src="/assets/CHILI GraFx Animated video 720.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Latest updates

<div class="grid cards" markdown>

-   :material-clock-fast: **Release Notes**


    ---
  
    **Jul 22, 2026**: GraFx Studio: Convert RGB Colors to CMYK in PDF Output

    ![rn_icon](/assets/icon-GraFx-Studio.svg)

    PDF output settings can now convert RGB content to the target CMYK profile as a complementary step to CMYK conversion — with an RGB source profile dropdown for unmanaged colors, in the UI and via `postProcessing.colorTransformation` in the Environment API.

    [:octicons-arrow-right-24: Full Release Note](/release-notes/2026/07/22/grafx-studio-convert-rgb-colors-to-cmyk-in-pdf-output/)

    ---

    **Jul 15, 2026**: Upcoming Change: Superscript and Subscript Rendering in GraFx Studio

    ![rn_icon](/assets/icon-CHILI-GraFx.svg)

    From GraFx Studio 1.46.0, superscript and subscript text follows the metrics built into each font instead of a single fixed style — review templates that use this formatting before adopting the new version.

    [:octicons-arrow-right-24: Full Release Note](/release-notes/2026/07/15/upcoming-change-superscript-and-subscript-rendering-in-grafx-studio/)

    ---

    **Jul 14, 2026**: CHILI GraFx: Brand Kit Themes

    ![rn_icon](/assets/icon-GraFx-Brandkits.svg)

    One Brand Kit, multiple variations: themes inherit from the default theme and override only what differs — a sub-brand accent color or a CMYK print palette. Manage themes in GraFx Brand Kits, switch them in the Studio workspace, or programmatically via Actions and the SDK.

    [:octicons-arrow-right-24: Full Release Note](/release-notes/2026/07/14/chili-grafx-brand-kit-themes/)

    ---

    **Jul 10, 2026**: CHILI GraFx Environment API: Large output requests fix

    ![rn_icon](/assets/icon-CHILI-GraFx.svg)

    Output requests for large documents no longer fail with `413` errors — the 10MB size limit now applies only to the `variables` property instead of the entire request body.

    [:octicons-arrow-right-24: Full Release Note](/release-notes/2026/07/10/chili-grafx-environment-api-large-output-requests-fix/)

    ---

    **Jun 24, 2026**: CHILI GraFx Environment API: Exclude headers from connector proxy requests

    ![rn_icon](/assets/icon-CHILI-GraFx.svg)

    Connector proxy requests can now drop specific headers via the new `X-GraFx-Proxy-Exclude-Headers` header — so the connector's `Authorization` header isn't forwarded to pre-signed CDN URLs that already carry their own auth.

    [:octicons-arrow-right-24: Full Release Note](/release-notes/2026/06/24/chili-grafx-environment-api-exclude-headers-from-connector-proxy-requests/)

    ---

    **Jun 23, 2026**: GraFx Studio: Improved Smart Crop and More

    ![rn_icon](/assets/icon-GraFx-Studio.svg)

    GraFx Studio's AI-powered Smart Crop gets a major upgrade: a more predictable algorithm with guaranteed framing, a new Subject alignment setting, automatic versioning with a one-click upgrade, and five live previews — plus variable-mapping, connector, and text improvements.

    [:octicons-arrow-right-24: Full Release Note](/release-notes/2026/06/23/grafx-studio-improved-smart-crop-and-more/)

    ---

    **See All Release Notes**

    [:octicons-arrow-right-24: Show all release notes](/release-notes/)

</div>
## The Platform & Applications

<div class="grid cards" markdown>

-   ![tinyapplogo](/assets/CHILI_LOGOS_OK-02.svg) __CHILI GraFx__

    ---

    **CHILI GraFx** platform centralizes your account information, users, resources and documents.

    [:octicons-arrow-right-24: Getting started](/CHILI-GraFx/admin/)

-   ![tinyapplogo](/assets/CHILI_LOGOS_OK-10.svg) __GraFx Studio__

    ---

    **GraFx Studio** is the multichannel Smart Template editor for (animated) digital and print output.

    [:octicons-arrow-right-24: Make your first Smart Template](/GraFx-Studio/guides/hello-world/)

-   ![tinyapplogo](/assets/CHILI_LOGOS_OK-21.svg) __GraFx Publisher__

    ---

    Enter the 'phygital' age of marketing by producing high-quality print and static digital output with **GraFx Publisher**.
    
    [:octicons-arrow-right-24: Make your first Smart Template](/GraFx-Publisher/guides/hello-world/)

-   ![tinyapplogo](/assets/CHILI_LOGOS_OK-12.svg) __GraFx Media__

    ---

    **GraFx Media** is the central repository to store your assets to be used in your Smart Templates.
    
    [:octicons-arrow-right-24: Upload your media](/GraFx-Media/guides/upload-media/)

-   ![tinyapplogo](/assets/CHILI_LOGOS_OK-08.svg) __GraFx Fonts__

    ---

    **GraFx Fonts** serves Fonts and Font families for GraFx Studio
    
    [:octicons-arrow-right-24: Upload your fonts](/GraFx-Fonts/guides/upload-fonts/)

-   :octicons-git-branch-24: __Developer Center__

    ---

    **Integrate** powerful GraFx Applications in your web application.
    
    [:octicons-arrow-right-24: Start Integrating](/GraFx-Developers/)

</div>

## More Resources

<div class="grid cards" markdown>

-   :octicons-mortar-board-24: __Academy__

    ---

    The online learning platform where you can follow self-paced training.

    [:octicons-link-external-24: Get Certified](https://product.chili-publish.academy/)

-   :octicons-video-24: __Youtube__

    ---

    Get inspired by fun and interactive videos.

    [:octicons-link-external-24: Watch](https://www.youtube.com/@chilipublish/featured)

-   :octicons-browser-24: __Demo__

    ---

    Try out concepts before you implement them.

    [:octicons-link-external-24: Discover it yourself](https://www.chili-publish.com/request-a-demo/)

-   :octicons-people-24: __Support__

    ---

    Ask our award winning support staff.

    [:octicons-link-external-24: Support Portal](https://mysupport.chili-publish.com/)

</div>

---

![svg_icon](/assets/CHILI_LOGOS_OK-01.svg)

All information on this portal is documentation on the products and services of [CHILI publish](https://www.chili-publish.com/contact-sales/).

CHILI publish NV<br/>
Korte Keppestraat 9, bus 11<br/>
9320 Aalst, Belgium

[chili-publish.com](https://www.chili-publish.com/){target="_blank"}
