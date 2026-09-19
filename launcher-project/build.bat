@echo off
REM Build GTA 6 Launcher to standalone .exe with bundled assets

echo Installing requirements...
pip install pyinstaller pyqt5

echo Building launcher with assets...
pyinstaller --onefile ^
    --windowed ^
    --name "GTA6_Launcher" ^
    --add-data "assets;assets" ^
    launcher.py

echo.
echo Build complete! Check dist/ folder for GTA6_Launcher.exe
echo The launcher includes bundled GTA6.exe and iscsidsc.dll
echo WARNING: DLL name must NOT be changed!
pause
