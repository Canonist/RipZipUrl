# RipZipUrl
Downloads all .zip archives from given URL. Enter your download-link catalog into the url-field demonstrated within. Tested only on single layers of links, and downloads being directly behind &lt;a>&lt;/a> tags in href.

This script lets you download all .zip archives in a given download catalog.
Only tested and working on single layer links, i.e. clicking the link starts the download.
If there are undesired downloads on the page with the .zip filetype, they will be downloaded. Edit code as necessary.
If it's broken, it's due to excessive cleaning of the code for aesthetics.
This code depends on libraries.

This script does not contain a sleep timer, it is intended for large archives, where their slow processing slows the script down sufficiently. Please add sleeptimers and pauses if your use case is in a faster environment, to avoid accidents involving denial of service.
