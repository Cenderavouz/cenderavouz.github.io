@ECHO OFF

pushd %~dp0

REM Command file for moving build\html to root

for /d %%i in ("..\*") do if /i not "%%~nxi"=="docs" if /i not "%%~nxi"==".git" @RD /s /q "%%i"
mkdir ..\temp
move ..\.gitignore ..\temp >nul
move ..\README.rst ..\temp >nul
del /q ..\*.*
move ..\temp\* ..\ >nul
rmdir ..\temp
xcopy build\html\* ..\ /s /q /e