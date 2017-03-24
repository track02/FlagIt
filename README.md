# FlagIt

A simple web extension checklist for flag collectors.


## Building

Run the firefox/chrome build scripts located inside the Builder folder, this will create a new directory with the needed files and package the contents, web-ext is required. Windows only at the moment

## Installation

### Firefox 

Add to firefox from Mozilla's add-on site: https://addons.mozilla.org/en-GB/firefox/addon/flag_it/?src=ss

New versions will be downloaded automatically as add-on updates.

### Chromium

Note: This release is outdated and does not include regional flags.

Use the .crx file in the Chromium folder and drag onto browser addons page.


## TODO

Optimisations:
- boolean array over int array
- loading images from external source (e.g. this github page) instead of bundling with addon
- further image compression, extracting only when needed
- world map with toggling countries


## Other

Extension icon from: https://material.io/icons/

Current flag icons from: http://icondrawer.com/free.php.

Polyfill library added for Chrome support: https://github.com/mozilla/webextension-polyfill

web-ext used for build: https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Getting_started_with_web-ext
