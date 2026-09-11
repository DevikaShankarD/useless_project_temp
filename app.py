#!/usr/bin/env python3
"""Flask web app for Click Timer with Material Design."""

from flask import Flask, render_template, jsonify, request
from datetime import datetime
import time

app = Flask(__name__)

# Timer state
timer_state = {
    'elapsed': 0.0,
    'running': False,
    'paused': False,
    'clicks': 0,
    'last_click_time': None,
    'start_time': None,
    'timeout_seconds': 5,
    'max_seconds': 3600
}


@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')


@app.route('/api/click', methods=['POST'])
def click():
    """Handle a click event."""
    current_time = time.time()
    timer_state['last_click_time'] = current_time
    timer_state['clicks'] += 1
    
    # Start timer on first click
    if not timer_state['running']:
        timer_state['running'] = True
        timer_state['paused'] = False
        timer_state['start_time'] = current_time
    
    return jsonify({
        'elapsed': timer_state['elapsed'],
        'clicks': timer_state['clicks'],
        'running': timer_state['running'],
        'status': 'running'
    })


@app.route('/api/pause', methods=['POST'])
def pause():
    """Pause the timer."""
    timer_state['paused'] = True
    timer_state['running'] = False
    return jsonify({'status': 'paused'})


@app.route('/api/resume', methods=['POST'])
def resume():
    """Resume the timer."""
    timer_state['paused'] = False
    timer_state['running'] = True
    timer_state['last_click_time'] = time.time()
    return jsonify({'status': 'running'})


@app.route('/api/reset', methods=['POST'])
def reset():
    """Reset the timer."""
    timer_state['elapsed'] = 0.0
    timer_state['running'] = False
    timer_state['paused'] = False
    timer_state['clicks'] = 0
    timer_state['last_click_time'] = None
    timer_state['start_time'] = None
    return jsonify({'status': 'reset', 'elapsed': 0, 'clicks': 0})


@app.route('/api/status', methods=['GET'])
def status():
    """Get current timer status."""
    current_time = time.time()
    
    # Update elapsed time if running
    if timer_state['running'] and timer_state['start_time']:
        timer_state['elapsed'] = current_time - timer_state['start_time']
        
        # Check if should stop (no click for 5 seconds)
        if timer_state['last_click_time']:
            time_since_click = current_time - timer_state['last_click_time']
            if time_since_click > timer_state['timeout_seconds']:
                timer_state['running'] = False
        
        # Cap at max
        if timer_state['elapsed'] > timer_state['max_seconds']:
            timer_state['elapsed'] = timer_state['max_seconds']
    
    return jsonify({
        'elapsed': timer_state['elapsed'],
        'clicks': timer_state['clicks'],
        'running': timer_state['running'],
        'paused': timer_state['paused']
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)