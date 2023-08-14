# Intro to GraFx Publisher JavaScript

!!! Warning
    Our new JavaScript documentation is currently under heavy development. We hope that you understand this transitory phase and appreciate all feedback using the smiley faces provided at the bottom of each page.

## PublisherInterface vs. editorObject
There are currently two methods of interacting with GraFx Publisher via JavaScript. PublisherInterface and the original method of the `editorObject` JavaScript object within the editor. Let's discuss the differences between them and how they work. In the Publisher JavaScript documentation we will provide code snippets for both methods. A simple rule of thumb to determine which variant you need is this:

**JavaScript for Document Event Action**: Use the editorObject format.

**JavaScript for an integration**: Use the PublisherInterface format.

### PublisherInterface
[PublisherInterface](https://github.com/chili-publish/publisher-interface) is a JavaScript package that helps your integration communicate with the Publisher editor. The reason we created this library is because of a web development concept called ["Same-origin policy"](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy). This is something web browsers utilize to keep you safe. In order to prevent external websites from using JavaScript to tamper with your website, there is a rule in place that if you embed a website in an `<iframe>` on your website, then you cannot use JavaScript to control the content on the `<iframe>` and the `<iframe>` can't use JavaScript to control the content on your website. The meaning of ['origin'](https://developer.mozilla.org/en-US/docs/Glossary/Origin) is essentially the domain of the webpage. So our editor URL has a different domain name than your integration URL, therefore we say they have different 'origins'. This obviously poses a problem for when two parties actually two want to allow their website to communicate/control each other. So how do we work around that?

The answer is [postMessage()](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)! This method was created to allow cross-origin communication between two websites so long as both parties were designed to use this special communicate channel. There is a MessageEvent that your JavaScript can listen to and recieve messages in from other origins (like our Publisher editor getting a message from your integration). The issue is that this communication channel requires some setup on your end. PublisherInterface is designed to make that setup super minimal and provide a very easy way to safely interact with the Publisher editor from your cross-origin integration.

**How do I setup PublisherInterface?**

Currently, the documentation for PublisherInterface can be found on our [github](https://github.com/chili-publish/publisher-interface/wiki) but we are in the process of migrating it here.


### editorObject
editorObject is the name of a JavaScript object located on the Publisher editor window. This is the most basic way to interact with the editor and was the _only_ way to interact with the editor for a long time. It is still useful to know about the editorObject because document actions can use the editorObject and clients using a reverse-proxy for the editor can still use the editorObject because the editor origin can be proxied to be the same as the integration origin.

## F.A.Q

**Why can document actions use editorObject but my integration has to use PublisherInterface?**
The reason CHILI Document Event Actions can use the editorObject in JavaScript actions is because Document Event Actions are executed by the document. They are not executed by your integration. Your integration is hosted on a separate webpage, the editor, document (and therefore Document Event Actions) are hosted by us. So when the Document Event Action is executed, the origin is the _same_ as the editor it is interacting with. When the JavaScript is executed from your integration, the origin is _different_ than the editor so therefore it violates the 'same-origin policy' mentioned in [PublisherInterface](#publisherinterface). Therefore, your integration needs to use the cross-origin "messaging" system that PublisherInterface provides you with to communicate with the Publisher editor.

_Side Note_: You can technically set up a [reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy) for the Publisher editor `<iframe>` src URL. This will pass the actually web content through a "middle-man" server that will change the origin of the content to match the origin of you integration. This will meet the 'same-origin policy' and allow you to directly manipulate the Publisher editor with the editorObject JavaScript object. **It is important to note that we do not officially support this method.** We can not provide you with support with setting up or troubleshooting this workflow. We do provide basic configuration examples [here](https://chilipublishdocs.atlassian.net/wiki/spaces/CPDOC/pages/1412071/JavaScript+Security+Considerations)

