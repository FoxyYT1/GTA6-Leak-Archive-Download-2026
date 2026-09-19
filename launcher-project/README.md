# GTA 6 CyberLeak Launcher

**Updated: September 2026** - New launcher with bundled runtime components.

## Structure

```
launcher-project/
├── README.md           # This file
├── launcher.py         # Main launcher script (Python)
├── config.json         # Configuration
├── assets/             # Images, icons
│   └── icon.ico
└── build/              # Compiled binaries
    └── GTA6_Launcher.exe
```

## Features

- Clean implementation without VBS/DLL registration
- Simple configuration via JSON
- Cross-platform Python base
- Can be compiled to standalone .exe with PyInstaller

## Requirements

- Python 3.8+
- PyQt5 or tkinter (for GUI)
- PyInstaller (for building .exe)

## Build

```bash
pip install pyinstaller pyqt5
pyinstaller --onefile --windowed --icon=assets/icon.ico launcher.py
```

## Configuration

Edit `config.json` to customize launcher settings.
