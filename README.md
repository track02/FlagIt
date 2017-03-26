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

### Updating check arrays

Need to store more information to allow for automated updates when flags are added or taken array.

Update to array of pairs [<Country Name> <0/1>] - loop over all td elements and extract id, pair these up with existing array values and store.

#### Update current script to overwrite old check arrays with check pairs, map td id's to stored check values

#### When a size difference is found, pull out stored pairs from previous version and generate a new set of pairs (mapped to zero), loop over old pairs and copy check value into new set. When finished overwrite the old set with the new set that has been populated. 


## Other

Extension icon from: https://material.io/icons/

Current flag icons from: http://icondrawer.com/free.php.

Polyfill library added for Chrome support: https://github.com/mozilla/webextension-polyfill

web-ext used for build: https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Getting_started_with_web-ext
