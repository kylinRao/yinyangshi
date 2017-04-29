#@echo off
setlocal enabledelayedexpansion

for /f "delims=  tokens=1" %%i in ('netstat -aon ^| findstr 4723 ') do (
set a=%%i
echo %%a
goto js
)
:js
taskkill /f /pid "!a:~71,5!"
rem pause>nul
