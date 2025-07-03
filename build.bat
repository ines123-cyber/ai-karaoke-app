@echo off
echo Cleaning old build files...
rmdir /s /q build
rmdir /s /q dist
del karaoke_app.spec 2>nul

echo Building the karaoke app into an EXE...

REM Make sure we're in the correct folder
cd /d "%~dp0"

REM Use --add-data to bundle ffmpeg folder
pyinstaller --onefile --name karaoke_app --add-data "ffmpeg;ffmpeg" karaoke_app.py

echo.
echo Build complete. Your EXE is in the 'dist' folder.
pause