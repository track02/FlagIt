#!/bin/bash
python page_builder.py Build_Resources/flags True
cp -R Build_Resources/. ../Chrome_Build
cp -R Pages/. ../Chrome_Build/Pages
cp -R Scripts/. ../Chrome_Build/Scripts
cp -R Chrome_Resources/. ../Chrome_Build
cd ../Chrome_Build
web-ext build
