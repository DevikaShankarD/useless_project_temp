#!/usr/bin/env python3
"""Manual test script - run without pytest."""

import sys
sys.path.insert(0, '.')

from src.timer import ClickTimer, TimerConfig, TimerState

def test_timer():
    """Run manual tests on the timer."""
    print("🧪 Click Timer - Manual Test Suite\n")
    print("=" * 50)
    
    print("\n✓ Test 1: Timer Initialization")
    config = TimerConfig(initial_seconds=0, increment_ms=100, max_seconds=3600)
    timer = ClickTimer(config)
    assert timer.get_elapsed_ms() == 0
    assert timer.get_state() == TimerState.IDLE
    print(f"   - Display: {timer.get_display_time()}")
    
    print("\n✓ Test 2: Click Advances Timer")
    timer.on_click()
    assert timer.get_elapsed_ms() == 100
    print(f"   - After 1 click: {timer.get_display_time()}")
    
    print("\n✓ Test 3: Multiple Clicks")
    for _ in range(9):
        timer.on_click()
    print(f"   - After 10 clicks: {timer.get_display_time()}")
    
    print("\n✓ Test 4: Reset")
    timer.reset()
    assert timer.get_elapsed_ms() == 0
    print(f"   - After reset: {timer.get_display_time()}")
    
    print("\n" + "=" * 50)
    print("✅ All tests passed!\n")
    print("🎉 Ready to run: python main.py\n")

if __name__ == "__main__":
    try:
        test_timer()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)