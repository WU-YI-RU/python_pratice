@echo off
set PROFILE_DIR=%~dp0chrome-debug-profile
set CHROME="C:\Program Files\Google\Chrome\Application\chrome.exe"

%CHROME% ^
  --remote-debugging-port=9222 ^
  --user-data-dir="%PROFILE_DIR%" ^
  --no-first-run ^
  --no-default-browser-check ^
  "https://admin-demo.nopcommerce.com/login"
  