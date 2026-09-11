#!/usr/bin/env python3
"""
Click Timer - Main Entry Point

A timer that runs continuously but only keeps running if you keep clicking.
Stop clicking for 5 seconds and the timer stops.

Usage:
    python main.py
"""

import sys
import tkinter as tk
from src.timer import TimerConfig
from src.gui import create_app


def main():
    """Main entry point."""
    # Configure the timer
    config = TimerConfig(
        initial_seconds=0,
        click_timeout_seconds=5,  # Stop after 5 seconds of no clicks
        max_seconds=3600           # Max 1 hour
    )
    
    # Create and run the app
    root, gui = create_app(config)
    
    print("✨ Click Timer Started!")
    print("📋 Click the button to start and keep the timer running.")
    print("⏸️  Stop clicking for 5 seconds and timer stops.")
    print("💥 Button keeps moving - that's intentional!")
    
    try:
        gui.run()
    except KeyboardInterrupt:
        print("\n👋 Click Timer closed.")
        sys.exit(0)


if __name__ == "__main__":
    main()