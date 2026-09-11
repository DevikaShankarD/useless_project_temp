"""Click-to-keep-running timer that only advances while clicking."""

import time
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional


class TimerState(Enum):
    """Enumeration of timer states."""
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"


@dataclass
class TimerConfig:
    """Configuration for the timer."""
    initial_seconds: int = 0
    click_timeout_seconds: int = 5  # Stop after 5 seconds of no clicks
    max_seconds: int = 3600


class ClickTimer:
    """A timer that runs continuously but only if you keep clicking."""
    
    def __init__(self, config: TimerConfig):
        """Initialize the timer."""
        self.config = config
        self._elapsed_seconds = float(config.initial_seconds)
        self._state = TimerState.IDLE
        self._click_count = 0
        self._callback: Optional[Callable] = None
        self._last_click_time = None
        self._start_time = None
        self._max_seconds = config.max_seconds
        self._is_running = False
    
    def on_click(self) -> None:
        """Handle a click event - keep timer running."""
        current_time = time.time()
        self._last_click_time = current_time
        self._click_count += 1
        
        # Start timer if first click
        if self._state == TimerState.IDLE:
            self._state = TimerState.RUNNING
            self._start_time = current_time
            self._is_running = True
        elif self._state == TimerState.PAUSED:
            # Resume from pause
            self._state = TimerState.RUNNING
            self._start_time = current_time - (self._elapsed_seconds)
            self._is_running = True
        
        self._update_timer()
    
    def pause(self) -> None:
        """Pause the timer."""
        if self._state == TimerState.RUNNING:
            self._state = TimerState.PAUSED
            self._is_running = False
    
    def resume(self) -> None:
        """Resume the timer."""
        if self._state == TimerState.PAUSED:
            self._state = TimerState.RUNNING
            self._start_time = time.time() - self._elapsed_seconds
            self._is_running = True
    
    def reset(self) -> None:
        """Reset the timer."""
        self._elapsed_seconds = 0
        self._state = TimerState.IDLE
        self._click_count = 0
        self._last_click_time = None
        self._start_time = None
        self._is_running = False
        if self._callback:
            self._callback(self.get_display_time())
    
    def set_callback(self, callback: Callable[[str], None]) -> None:
        """Set callback for updates."""
        self._callback = callback
    
    def _update_timer(self) -> None:
        """Update elapsed time based on clicks."""
        if self._state == TimerState.RUNNING and self._start_time:
            self._elapsed_seconds = time.time() - self._start_time
            
            # Cap at max
            if self._elapsed_seconds > self._max_seconds:
                self._elapsed_seconds = self._max_seconds
            
            if self._callback:
                self._callback(self.get_display_time())
    
    def update(self) -> None:
        """Call this regularly to check if timer should stop."""
        if self._state == TimerState.RUNNING and self._last_click_time:
            current_time = time.time()
            time_since_click = current_time - self._last_click_time
            
            # Stop if no click for 5 seconds
            if time_since_click > self.config.click_timeout_seconds:
                self._state = TimerState.PAUSED
                self._is_running = False
                if self._callback:
                    self._callback(self.get_display_time())
            else:
                self._update_timer()
    
    def get_display_time(self) -> str:
        """Get formatted time MM:SS.ms"""
        total_seconds = self._elapsed_seconds
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int((total_seconds % 1) * 100)
        return f"{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
    
    def get_state(self) -> TimerState:
        """Get current state."""
        return self._state
    
    def get_click_count(self) -> int:
        """Get click count."""
        return self._click_count
    
    def is_at_max(self) -> bool:
        """Check if at max."""
        return self._elapsed_seconds >= self._max_seconds