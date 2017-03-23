python page_builder.py Build_Resources\flags False
xcopy Pages\*.* ..\Firefox_Build\Pages
xcopy Scripts\*.* ..\Firefox_Build\Scripts
xcopy Build_Resources ..\Firefox_Build\ /E /Y
xcopy Firefox_Resources ..\Firefox_Build\ /E /Y
cd ..\Firefox_Build\
web-ext 
pause
