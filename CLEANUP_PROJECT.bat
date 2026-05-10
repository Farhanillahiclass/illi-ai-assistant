@echo off
title ILLI Project Cleanup
echo ===============================================
echo         ILLI PROJECT CLEANUP SCRIPT
echo ===============================================
echo.
echo This will delete all unnecessary files
echo and keep only working versions
echo.
echo Press any key to continue or Ctrl+C to cancel...
pause >nul
echo.

echo Deleting old ILLI versions...
for %%f in (illi_advanced.py illi_comprehensive.py illi_conversational.py illi_dashboard.py illi_dashboard_futuristic.py illi_enhanced.py illi_fast.py illi_file_manager.py illi_final.py illi_fixed.py illi_running_apps.py illi_talking.py illi_text.py illi_ultimate.py illi_ultimate_fixed.py illi_ultra.py illi_universal.py illi_universal_fixed.py illi_working.py illi_working_final.py) do (
    if exist "%%f" (
        echo Deleting %%f
        del "%%f"
    )
)

echo.
echo Deleting all JARVIS versions...
for %%f in (jarvis_final.py jarvis_final_working.py jarvis_modular.py jarvis_perfect.py jarvis_working.py) do (
    if exist "%%f" (
        echo Deleting %%f
        del "%%f"
    )
)

echo.
echo Deleting old batch files...
for %%f in (START_ILLI_COMPREHENSIVE.bat START_ILLI_CONVERSATIONAL.bat START_ILLI_DASHBOARD_FUTURISTIC.bat START_ILLI_ENHANCED.bat START_ILLI_FAST.bat START_ILLI_FILE_MANAGER.bat START_ILLI_FINAL.bat START_ILLI_FIXED.bat START_ILLI_RUNNING_APPS.bat START_ILLI_TALKING.bat START_ILLI_TEXT.bat START_ILLI_ULTIMATE.bat START_ILLI_ULTIMATE_FIXED.bat START_ILLI_ULTRA.bat START_ILLI_UNIVERSAL.bat START_ILLI_UNIVERSAL_FIXED.bat START_ILLI_WORKING.bat START_ILLI_WORKING_FINAL.bat START_JARVIS_FINAL.bat START_JARVIS_FINAL_WORKING.bat START_JARVIS_MODULAR.bat START_JARVIS_PERFECT.bat START_JARVIS_WORKING.bat) do (
    if exist "%%f" (
        echo Deleting %%f
        del "%%f"
    )
)

echo.
echo Cleaning Python cache files...
for /d %%d in (__pycache__) do (
    if exist "%%d" (
        echo Deleting %%d
        rmdir /s /q "%%d"
    )
)
del /q *.pyc 2>nul

echo.
echo Cleanup completed!
echo.
echo Files remaining:
echo - illi.py (Original)
echo - illi_working_simple.py (Working version)
echo - illi_dashboard_simple.py (Dashboard)
echo - START_ILLI.bat (Original launcher)
echo - START_ILLI_WORKING_SIMPLE.bat (Working launcher)
echo - START_ILLI_DASHBOARD_SIMPLE.bat (Dashboard launcher)
echo - README.md (Documentation)
echo - PROJECT_STRUCTURE.txt (Project info)
echo - EMAIL_SETUP_GUIDE.txt (Email setup)
echo - QUICK_EMAIL_SETUP.bat (Email setup)
echo - PROJECT_CLEANUP_SUMMARY.txt (Cleanup summary)
echo.
echo Press any key to exit...
pause >nul
