# CHILI GraFx requirements

Although **CHILI GraFx** runs in the cloud and is accessed through your browser, some corporate IT infrastructures may require configuration.

Below are common requirements to consider.

## Application URLs to whitelist

### Production Application

``` html
*.chiligrafx.com (asterisk will be your environment name)
*.chili-publish.online
api.chiligrafx.com/api/
*.chili-publish-sandbox.online
```

### Applications & URLs CHILI GraFx will call

``` html
region1.google-analytics.com/
api-iam.eu.intercom.io/
```

## Supporting applications

**Support**

``` html
mysupport.chili-publish.com/
```
Will redirect to

``` html
chili-publish.zendesk.com
```

**Training & Certification Portan**

``` html
product.chili-publish.academy
```

**Open source elements of CHILI GraFx**

``` html
github.com/chili-publish
```