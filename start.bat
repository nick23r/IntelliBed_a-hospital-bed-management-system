@echo off
echo Hospital Bed Management System Startup
echo ====================================
echo.

REM Check if virtual environment exists, if not create it
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    if %ERRORLEVEL% neq 0 (
        echo Error creating virtual environment!
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install/Update requirements
echo Checking and installing requirements...
python -m pip install --upgrade pip
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo Error installing requirements!
    pause
    exit /b 1
)

echo.
echo Starting application...
echo.

REM Run the application
C:/Users/HP/Downloads/hospital-bed-system/.venv/Scripts/python.exe main.py

REM Keep the window open if there's an error
if %ERRORLEVEL% neq 0 (
    echo.
    echo An error occurred. Press any key to exit...
    pause > nul
)

REM Deactivate virtual environment
call deactivate