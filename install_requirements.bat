@echo off
title Python Library Installer
echo Checking and installing requirements...

:: Pip ব্যবহার করে requirements.txt এর লাইব্রেরিগুলো চেক ও ইনস্টল করা
:: --upgrade দিলে পুরনো ভার্সন থাকলে আপডেট হবে, আর ইনস্টল থাকলে দ্রুত স্কিপ করবে
pip install -r requirements.txt --disable-pip-version-check

echo.
echo ===========================================
echo Setup Complete! Press any key to exit.
echo ===========================================
pause >nul