@echo off
git pull origin main
echo.
echo Updated! Closing in 3 seconds...
timeout /t 3 >nul
exit