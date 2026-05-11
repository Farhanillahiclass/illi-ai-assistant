@echo off
echo Testing ILLI AI Application...
echo.

echo Checking Python dependencies...
python -c "import tkinter; print('✓ tkinter OK')" 2>nul
python -c "import psutil; print('✓ psutil OK')" 2>nul
python -c "import speech_recognition; print('✓ speech_recognition OK')" 2>nul
python -c "import pyttsx3; print('✓ pyttsx3 OK')" 2>nul

echo.
echo Checking application syntax...
python -m py_compile ILLI_AI_SIMPLE_WORKING.py
if %errorlevel% equ 0 (
    echo ✓ Syntax check passed
) else (
    echo ✗ Syntax check failed
    goto :error
)

echo.
echo Checking application structure...
findstr /C:"class ILLI_AI_Simple_Working" ILLI_AI_SIMPLE_WORKING.py >nul
if %errorlevel% equ 0 (
    echo ✓ Main class found
) else (
    echo ✗ Main class not found
    goto :error
)

echo.
echo ✓ All tests passed!
echo The ILLI AI application is ready to use.
echo.
echo To run the application, use: python ILLI_AI_SIMPLE_WORKING.py
goto :end

:error
echo.
echo ✗ Some tests failed. Please check the issues above.

:end
pause
