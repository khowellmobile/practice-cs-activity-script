@echo off

:: Change directory to the folder where this batch file is located
cd /d "%~dp0"

:: Activate the virtual environment
call venv\Scripts\activate

:: Run the python script
python "%~dp0practice-cs-window-clicker.py"

:: Keep window on script finish/crash to see any output
pause