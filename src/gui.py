"""GUI for the click timer with continuous running."""

import tkinter as tk
import random
from typing import Optional
from src.timer import ClickTimer, TimerConfig


class ClickTimerGUI:
    """GUI for timer that runs continuously but needs constant clicks."""
    
    def __init__(self, root: tk.Tk, timer_config: Optional[TimerConfig] = None):
        """Initialize the GUI."""
        self.root = root
        self.root.title("Click Timer - Keep Clicking to Keep Time Running!")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        self.bg_color = "#1a1a2e"
        self.fg_color = "#00d4ff"
        self.accent_color = "#ff006e"
        self.root.configure(bg=self.bg_color)
        
        self.timer = ClickTimer(timer_config or TimerConfig())
        self.timer.set_callback(self._update_display)
        
        self.chaos_enabled = True
        
        self._create_widgets()
        
        # Start continuous update loop
        self._continuous_update()
    
    def _create_widgets(self) -> None:
        """Create GUI widgets."""
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="⏱️  CLICK TIMER  ⏱️",
            font=("Arial", 28, "bold"),
            fg=self.fg_color,
            bg=self.bg_color
        )
        title_label.pack()
        
        display_frame = tk.Frame(self.root, bg=self.bg_color)
        display_frame.pack(pady=20)
        
        self.time_label = tk.Label(
            display_frame,
            text="00:00.00",
            font=("Courier New", 72, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        )
        self.time_label.pack()
        
        stats_frame = tk.Frame(self.root, bg=self.bg_color)
        stats_frame.pack(pady=10)
        
        self.stats_label = tk.Label(
            stats_frame,
            text="Clicks: 0 | State: IDLE | Keep Clicking!",
            font=("Arial", 12),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.stats_label.pack()
        
        self.buttons_frame = tk.Frame(self.root, bg=self.bg_color)
        self.buttons_frame.pack(pady=30, fill=tk.BOTH, expand=True, padx=20)
        
        self.click_button = self._create_button(
            "CLICK TO\nKEEP TIME\nRUNNING!",
            self.timer.on_click,
            width=15,
            height=4,
            color=self.accent_color
        )
        
        self.pause_button = self._create_button(
            "Pause",
            self.timer.pause,
            width=10,
            height=2
        )
        
        self.resume_button = self._create_button(
            "Resume",
            self.timer.resume,
            width=10,
            height=2
        )
        
        self.reset_button = self._create_button(
            "RESET",
            self.timer.reset,
            width=10,
            height=2,
            color="#ff4757"
        )
        
        info_frame = tk.Frame(self.root, bg=self.bg_color)
        info_frame.pack(pady=10, fill=tk.X, padx=20)
        
        self.info_label = tk.Label(
            info_frame,
            text="⚡ Timer runs continuously! Stop clicking for 5 seconds and it stops.",
            font=("Arial", 10, "italic"),
            fg="#888888",
            bg=self.bg_color,
            wraplength=500
        )
        self.info_label.pack()
    
    def _create_button(self, text: str, command, width: int = 12, height: int = 2, color: str = None) -> tk.Button:
        """Create a styled button."""
        color = color or self.fg_color
        
        button = tk.Button(
            self.buttons_frame,
            text=text,
            command=command,
            width=width,
            height=height,
            font=("Arial", 10, "bold"),
            bg=color,
            fg=self.bg_color,
            activebackground=color,
            activeforeground=self.bg_color,
            relief=tk.RAISED,
            bd=3,
            cursor="hand2"
        )
        
        button.place(
            x=random.randint(0, max(1, self.buttons_frame.winfo_width() - 100)),
            y=random.randint(0, max(1, self.buttons_frame.winfo_height() - 80))
        )
        
        button.bind("<Enter>", lambda e: self._jitter_button(e.widget))
        
        return button
    
    def _jitter_button(self, button: tk.Button) -> None:
        """Move button when hovered - SUPER FAST version."""
        if self.chaos_enabled:
            current_x = button.winfo_x() if button.winfo_x() > 0 else 50
            current_y = button.winfo_y() if button.winfo_y() > 0 else 50
            
            x = current_x + random.randint(-250, 250)
            y = current_y + random.randint(-250, 250)
            
            x = max(0, min(x, self.buttons_frame.winfo_width() - 100))
            y = max(0, min(y, self.buttons_frame.winfo_height() - 80))
            
            button.place(x=x, y=y)
    
    def _update_display(self, time_str: str) -> None:
        """Update the time display."""
        self.time_label.config(text=time_str)
        self.stats_label.config(
            text=f"Clicks: {self.timer.get_click_count()} | "
                 f"State: {self.timer.get_state().value.upper()}"
        )
        
        if self.timer.is_at_max():
            self.time_label.config(fg="#ff4757")
            self.info_label.config(text="⚠️  MAX TIME REACHED! Reset to continue.")
        else:
            self.time_label.config(fg=self.accent_color)
    
    def _continuous_update(self) -> None:
        """Continuously update timer and check if it should stop."""
        self.timer.update()
        # Update display every 50ms
        self.root.after(50, self._continuous_update)
    
    def run(self) -> None:
        """Start the GUI event loop."""
        self.root.mainloop()


def create_app(timer_config: Optional[TimerConfig] = None) -> tuple:
    """Factory function to create and return the app."""
    root = tk.Tk()
    gui = ClickTimerGUI(root, timer_config)
    return root, gui