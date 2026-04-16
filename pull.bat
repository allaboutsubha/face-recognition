@echo off
:: প্রথমে চেক করবে এই ফোল্ডারে গিট সেটআপ আছে কি না, না থাকলে সেট করবে
if not exist .git (
    echo Initializing Git and setting remote...
    git init
    git remote add origin https://github.com/allaboutsubha/face-recognition.git
)

echo Pulling latest code from GitHub...
git pull origin main

echo.
echo Updated! Closing in 5 seconds...
timeout /t 5 >nul
exit