@echo off
title Gmail App Password Setup for ILLI
echo ===============================================
echo     GMAIL APP PASSWORD SETUP FOR ILLI
echo ===============================================
echo.
echo This will help you setup Gmail app password for ILLI email functionality
echo.
echo Step 1: Opening Google Account Security page...
echo This is where you enable 2-factor authentication
echo.
pause
start https://myaccount.google.com/security

echo.
echo Step 2: After enabling 2FA, opening App Passwords page...
echo This is where you generate the app password for ILLI
echo.
pause
start https://myaccount.google.com/apppasswords

echo.
echo SETUP INSTRUCTIONS:
echo ===================
echo 1. Enable 2-Factor Authentication on the first page
echo 2. On App Passwords page:
echo    - Select app: Other (Custom name)
echo    - Select device: Windows Computer
echo    - Name: ILLI Virtual Assistant
echo    - Click GENERATE
echo    - Copy the 16-character password
echo.
echo 3. Update the ILLI script:
echo    - Open: g:/Virtual Assistant/illi_final.py
echo    - Find line: sender_password = "your-app-password"
echo    - Replace "your-app-password" with your generated password
echo.
echo 4. Test email functionality:
echo    - Start ILLI
echo    - Say: "send email to test@gmail.com subject Test message This is a test"
echo.
echo Links for manual access:
echo - Google Security: https://myaccount.google.com/security
echo - App Passwords: https://myaccount.google.com/apppasswords
echo.
echo Would you like to open the ILLI script now to update the password?
echo.
pause
notepad "g:/Virtual Assistant/illi_final.py"

echo.
echo Setup complete! Your ILLI will be able to send emails once you update the password.
echo.
pause
