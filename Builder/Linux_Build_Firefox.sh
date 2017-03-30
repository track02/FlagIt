#!/bin/bash
python page_builder.py Build_Resources/flags False
cp -R Build_Resources/. ../Firefox_Build
cp -R Pages/. ../Firefox_Build/Pages
cp -R Scripts/. ../Firefox_Build/Scripts
cp -R Firefox_Resources/. ../Firefox_Build
cd ../Firefox_Build
web-ext build
