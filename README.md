# FlagIt

A simple web extension checklist for flag collectors.


## Building

Run the firefox/chrome build scripts located inside the Builder folder, this will create a new directory with the needed files and package the contents, web-ext is required.

## Installation

### Firefox 

Add to firefox from Mozilla's add-on site: https://addons.mozilla.org/en-GB/firefox/addon/flag_it/?src=ss

New versions will be downloaded automatically as add-on updates. Currently V0.39

### Chromium

Only available via repo - download and load the Chrome Build folder as an addon


## TODO
- Investigate chrome packaging process - stripping polyfill?
- loading images from external source (e.g. this github page) instead of bundling with addon
- world map with toggling countries


## Other

Extension icon from: https://material.io/icons/

Current flag icons from: http://icondrawer.com/free.php.

Polyfill library added for Chrome support: https://github.com/mozilla/webextension-polyfill

web-ext used for automating build: https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Getting_started_with_web-ext
