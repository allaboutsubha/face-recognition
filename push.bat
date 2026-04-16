@echo off
:: এখানে তোমার ডিফল্ট মেসেজটি লিখে রাখো
set "default_msg=Update: Face Recognition System Improvement"

:: ইউজারকে ইনপুট দেওয়ার সুযোগ দেওয়া হচ্ছে, কিছু না লিখলে ডিফল্টটি নিয়ে নেবে
set /p msg="Enter commit message (Press Enter for default): "

if "%msg%"=="" set "msg=%default_msg%"

git add .
git commit -m "%msg%"
git push origin main

echo.
echo ===========================================
echo Commit Done with message: "%msg%"
echo Closing in 1 seconds...
echo ===========================================

timeout /t 1 >nul
exit