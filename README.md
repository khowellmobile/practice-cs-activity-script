Practice CS Window Clicker

This script keeps a window with a title containing "Practice CS" active by clicking near the top-center of that window every 900 seconds (15 minutes).

Current behavior:
- Looks for the first window whose title contains "Practice CS"
- Restores the window if it is minimized, clicks it, then minimizes it again if needed
- Restores the mouse cursor to its original position after clicking
- Skips the click if the mouse has not moved since the last check

Files:
- practice-cs-window-clicker.py: main script
- run-practice-cs-window-clicker.bat: activates the local venv and runs the script

Requirements:
- Windows
- A virtual environment at venv\
- Installed Python packages used by the script