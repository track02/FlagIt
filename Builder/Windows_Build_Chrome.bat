python page_builder.py Build_Resources\flags True
xcopy Pages\*.* ..\Chrome_Build\Pages
xcopy Scripts\*.* ..\Chrome_Build\Scripts
xcopy Build_Resources ..\Chrome_Build\ /E /y
xcopy Chrome_Resources ..\Chrome_Build\ /E /y
cd ..\Chrome_Build\
web-ext build
pause
