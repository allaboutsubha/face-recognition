@echo off
echo Initializing Git and Pushing to GitHub...
echo "# face-recognition" >> README.md
git init
git add .
git commit -m "initial project setup"
git branch -M main
git remote add origin https://github.com/allaboutsubha/face-recognition.git
git push -u origin main
echo.
echo Setup Complete! Closing in 5 seconds...
timeout /t 5 >nul
exit