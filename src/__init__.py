"""Click Timer - A timer that only advances when you click."""

from src.timer import ClickTimer, TimerConfig, TimerState

try:
    from src.gui import ClickTimerGUI, create_app
    __all__ = ["ClickTimer", "TimerConfig", "TimerState", "ClickTimerGUI", "create_app"]
except ImportError:
    __all__ = ["ClickTimer", "TimerConfig", "TimerState"]

__version__ = "1.0.0"
