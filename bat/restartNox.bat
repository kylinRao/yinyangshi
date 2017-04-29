@echo off
setlocal enabledelayedexpansion

for /f  %%i in ('tasklist ^| findstr Nox ') do (

set a=%%i
echo "this is a"
echo %a%
goto js


)
:js
taskkill /f /pid %a%
L:\yeshen\Nox\bin\Nox.exe
rem pause>nul
