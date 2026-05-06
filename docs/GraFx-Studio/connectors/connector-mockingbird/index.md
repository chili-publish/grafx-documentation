# Mockingbird Media Connector


!!! info "Mockingbird"

	![Mockingbird](Mockingbird.svg){.connector_icon}

	A connector that sings back any media you ask for, but never leaves the cage. Unless you open it.

:fontawesome-regular-square: Built-in  
:fontawesome-regular-square: Built by CHILI publish  
:fontawesome-regular-square-check: Third Party

[See Connector types](/GraFx-Studio/concepts/connectors/#types-of-connectors)

Mockingbird is a media connector that provides a catalogue of 100 placeholder images for testing and prototyping GraFx Studio templates before a real media source is available. It can run in two modes: **offline** (default), where no external service, credentials, or network access are required, and **remote**, where each asset is fetched from [picsum.photos](https://picsum.photos).

## Installation

[See installation through Connector Hub](/GraFx-Studio/guides/connector-hub/)

## Modes

Mockingbird operates in one of two modes, controlled by an environment (runtime) option.

### Offline mode (default)

Each asset returns a pre-encoded 1×1 colored PNG placeholder — no network access is needed. Frame dimensions are set correctly per asset using the realistic values returned by the connector's detail endpoint, so layout and cropping behaviour is representative.

### Remote mode

Each asset fetches a deterministic photo from [picsum.photos](https://picsum.photos), using the asset ID as a seed. The same asset always returns the same image, making remote mode reproducible across sessions. Requires outbound network access to `picsum.photos`.

## Configuration

Once installed, open the connector in your **Connector overview** and go to **Configuration**.

The only option is **Use remote images** (runtime option, text): set to `"true"` to enable remote mode. Any other value (including empty) uses offline mode.
