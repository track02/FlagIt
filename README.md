# FlagIt


A simple browser-addon checklist for flag collectors.


##TODO

Grey out flags that haven't been found, add a tag when generating the
table and use CSS to adjust transparency.

When a flag is clicked change to another tag with no transparency
adjustments. Bind a handler to click events, check for element tag.

Look into using storage.local to store JSON country ISO names/codes and
to keep track of found flags.

Consider using individual pages and displaying flags alphabetically, 
this would allow larger flag images to be used on each page or breaking 
up the page into alphabetical sections.


##Notes/Other

Current flag icons from http://icondrawer.com/free.php.

Polyfill library added for Chrome support: https://github.com/mozilla/webextension-polyfill
