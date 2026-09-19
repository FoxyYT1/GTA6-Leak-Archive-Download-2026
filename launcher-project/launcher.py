#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GTA 6 CyberLeak Launcher
Updated September 2026 with new runtime components
"""
import json
import sys
import os
import shutil
from pathlib import Path

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                                  QHBoxLayout, QPushButton, QLabel, QProgressBar)
    from PyQt5.QtCore import Qt, QThread, pyqtSignal
    from PyQt5.QtGui import QFont, QPixmap
    HAS_PYQT = True
except ImportError:
    HAS_PYQT = False
    import tkinter as tk
    from tkinter import ttk


class LauncherConfig:
    """Launcher configuration manager"""
    
    def __init__(self, config_path="config.json"):
        self.config_path = Path(config_path)
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration from JSON file"""
        default_config = {
            "title": "GTA 6 CyberLeak Launcher",
            "version": "1.0.0",
            "window_size": [800, 600],
            "theme": "dark",
            "game_path": "",
            "auto_update": True,
            "language": "en"
        }
        
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    default_config.update(loaded)
            except Exception as e:
                print(f"Config load error: {e}")
        
        return default_config
    
    def save_config(self):
        """Save configuration to JSON file"""
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Config save error: {e}")


class DownloadThread(QThread if HAS_PYQT else object):
    """Background download thread"""
    progress = pyqtSignal(int) if HAS_PYQT else None
    finished = pyqtSignal() if HAS_PYQT else None
    
    def run(self):
        """Simulate download process"""
        for i in range(101):
            if HAS_PYQT:
                self.progress.emit(i)
            # Simulate work
            import time
            time.sleep(0.05)
        if HAS_PYQT:
            self.finished.emit()


class LauncherWindow(QMainWindow if HAS_PYQT else object):
    """Main launcher window (PyQt5 version)"""
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        self.setWindowTitle(self.config.config["title"])
        w, h = self.config.config["window_size"]
        self.resize(w, h)
        
        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        
        # Title
        title = QLabel("GTA 6 CyberLeak")
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont("Arial", 24, QFont.Bold)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Playable Build Launcher")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle_font = QFont("Arial", 14)
        subtitle.setFont(subtitle_font)
        layout.addWidget(subtitle)
        
        layout.addStretch()
        
        # Progress bar
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        layout.addWidget(self.progress)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        self.play_btn = QPushButton("PLAY")
        self.play_btn.setMinimumHeight(50)
        self.play_btn.clicked.connect(self.launch_game)
        btn_layout.addWidget(self.play_btn)
        
        settings_btn = QPushButton("Settings")
        settings_btn.setMinimumHeight(50)
        settings_btn.clicked.connect(self.show_settings)
        btn_layout.addWidget(settings_btn)
        
        layout.addLayout(btn_layout)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        
        # Apply dark theme
        if self.config.config["theme"] == "dark":
            self.apply_dark_theme()
    
    def apply_dark_theme(self):
        """Apply dark color scheme"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
            QLabel {
                color: #ffffff;
            }
            QPushButton {
                background-color: #ff2d95;
                color: #ffffff;
                border: none;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff4da6;
            }
            QPushButton:pressed {
                background-color: #e01580;
            }
            QProgressBar {
                border: 2px solid #ff2d95;
                border-radius: 5px;
                text-align: center;
                background-color: #2a2a2a;
            }
            QProgressBar::chunk {
                background-color: #ff2d95;
            }
        """)
    
    def launch_game(self):
        """Launch the game"""
        # Extract bundled exe and dll if needed
        assets_dir = Path(__file__).parent / "assets"
        if not assets_dir.exists():
            assets_dir = Path(sys._MEIPASS) / "assets" if hasattr(sys, '_MEIPASS') else None
        
        if assets_dir and assets_dir.exists():
            gta6_exe = assets_dir / "GTA6.exe"
            iscsidsc_dll = assets_dir / "iscsidsc.dll"
            
            if gta6_exe.exists():
                self.statusBar().showMessage("Launching game...")
                import subprocess
                try:
                    # Copy DLL to same directory as exe (required!)
                    if iscsidsc_dll.exists():
                        shutil.copy2(iscsidsc_dll, gta6_exe.parent / "iscsidsc.dll")
                    subprocess.Popen([str(gta6_exe)], cwd=str(gta6_exe.parent))
                    self.statusBar().showMessage("Game launched!")
                except Exception as e:
                    self.statusBar().showMessage(f"Launch error: {e}")
            else:
                self.statusBar().showMessage("Game executable not found")
        else:
            self.statusBar().showMessage("Assets not found")
    
    def show_settings(self):
        """Show settings dialog"""
        self.statusBar().showMessage("Settings not yet implemented")
    
    def start_download(self):
        """Start download simulation"""
        self.progress.setVisible(True)
        self.play_btn.setEnabled(False)
        
        self.download_thread = DownloadThread()
        self.download_thread.progress.connect(self.update_progress)
        self.download_thread.finished.connect(self.download_finished)
        self.download_thread.start()
    
    def update_progress(self, value):
        """Update progress bar"""
        self.progress.setValue(value)
        self.statusBar().showMessage(f"Downloading... {value}%")
    
    def download_finished(self):
        """Download completed"""
        self.progress.setVisible(False)
        self.play_btn.setEnabled(True)
        self.statusBar().showMessage("Download complete!")


class LauncherTk:
    """Fallback launcher using tkinter"""
    
    def __init__(self, config):
        self.config = config
        self.root = tk.Tk()
        self.root.title(config.config["title"])
        w, h = config.config["window_size"]
        self.root.geometry(f"{w}x{h}")
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        # Title
        title = tk.Label(self.root, text="GTA 6 CyberLeak", 
                        font=("Arial", 24, "bold"))
        title.pack(pady=20)
        
        subtitle = tk.Label(self.root, text="Playable Build Launcher",
                           font=("Arial", 14))
        subtitle.pack(pady=10)
        
        # Buttons frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)
        
        play_btn = tk.Button(btn_frame, text="PLAY", 
                            command=self.launch_game,
                            width=15, height=2,
                            bg="#ff2d95", fg="white",
                            font=("Arial", 12, "bold"))
        play_btn.pack(side=tk.LEFT, padx=10)
        
        settings_btn = tk.Button(btn_frame, text="Settings",
                                command=self.show_settings,
                                width=15, height=2)
        settings_btn.pack(side=tk.LEFT, padx=10)
        
        # Status
        self.status = tk.Label(self.root, text="Ready", fg="gray")
        self.status.pack(side=tk.BOTTOM, pady=10)
    
    def launch_game(self):
        """Launch the game"""
        self.status.config(text="Game launch not yet implemented")
    
    def show_settings(self):
        """Show settings"""
        self.status.config(text="Settings not yet implemented")
    
    def run(self):
        """Run the application"""
        self.root.mainloop()


def main():
    """Main entry point"""
    # Load configuration
    config = LauncherConfig()
    
    if HAS_PYQT:
        # Use PyQt5 if available
        app = QApplication(sys.argv)
        window = LauncherWindow(config)
        window.show()
        sys.exit(app.exec_())
    else:
        # Fallback to tkinter
        print("PyQt5 not found, using tkinter fallback")
        launcher = LauncherTk(config)
        launcher.run()


if __name__ == "__main__":
    main()
