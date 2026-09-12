# ⏱️ Click Timer 🎯

## Basic Details

**Project Name:** Click Timer - Interactive Time Tracker

**Team Name:** GLaDOS

**Team Members:**
Devika Shankar - ASIET
Devabhadra K U- ASIET

---

## Project Description

Click Timer is a fully functional timer application with an intentionally chaotic user interface. The timer only runs when you continuously click a button - stop clicking for 5 seconds and the timer stops! Available in both desktop (Tkinter) and web (Flask) versions.

The concept merges practical timer functionality with deliberately broken UI mechanics, making time-tracking both functional and entertaining.


https://drive.google.com/drive/folders/1IHO64x64mqgG00iAAkcGKRrEddzjFhzn?usp=sharing

---

## The Problem (that doesn't exist)

Most timers are boring and predictable. They just... tick. There's no challenge, no engagement, no reason to keep interacting with them!

---

## The Solution (that nobody asked for)

Introducing the Click Timer - a timer that demands your constant attention! Want to track time? Better keep clicking that button or your timer stops. It's productivity meets chaos. It's a timer that won't leave you alone. It's the timer experience nobody knew they needed!

---

## Technical Details

### Technologies/Components Used

**For Software:**
* **Languages:** Python 3.8+
* **Frameworks:** 
  - Tkinter (Desktop GUI)
  - Flask (Web Framework)
* **Libraries:**
  - time (Timer logic)
  - random (Button chaos)
  - jsonify (API responses)
* **Tools:**
  - VS Code
  - Git & GitHub
  - Python pip

**For Hardware:**
* No hardware required - runs on any computer with Python installed

---

## Implementation

### For Software:

#### Installation

```bash
# Clone the repository
git clone https://github.com/DevikaShankarD/useless_project_temp.git

# Navigate to project
cd timer

# Install dependencies
pip install Flask

# For Tkinter (usually pre-installed)
pip install tk
```

#### Run - Desktop Version (Recommended)

```bash
python main.py
```

#### Run - Web Version

```bash
python app.py
```
Then open: `http://localhost:5000`

---

## Project Documentation

### For Software:

#### Screenshots

![Timer Start](Screenshot showing timer at 00:00.00)
*Screenshot 1: Initial Timer State - Shows the Click Timer interface at startup with timer at 00:00.00, ready to begin*

![Timer Running](Screenshot showing timer running with clicks)
*Screenshot 2: Timer Running - Demonstrates timer actively running with accumulated time and click counter showing progress*

![Timer Stopped](Screenshot showing timer stopped after 5 seconds)
*Screenshot 3: Timer Stopped - Shows timer paused after 5 seconds of inactivity, displaying final time and reset option*

#### Architecture Diagram

![Workflow](Add workflow diagram here)
*Click Timer Architecture: User clicks button → Timer advances continuously → No click for 5 seconds → Timer stops. Pause/Resume/Reset controls available anytime*

---

## How It Works

### Timer Flow

1. **Click Button** → Timer starts and runs continuously
2. **Keep Clicking** → Timer keeps running (every 5 seconds without click stops it)
3. **Stop Clicking** → Timer automatically pauses after 5 seconds
4. **Resume** → Click again or use Resume button to restart
5. **Reset** → Clear everything and start fresh

### Features

- ⏱️ **Continuous Timer** - Runs like a normal timer once started
- 👆 **Click-Dependent** - Requires clicks every 5 seconds to stay running
- 🎯 **Multiple Controls** - Pause, Resume, Reset buttons
- 💥 **Chaotic UI** - Buttons move around during interaction
- 📊 **Stats Display** - Shows clicks and current state
- 🌐 **Dual Versions** - Desktop (Tkinter) and Web (Flask)

---

## Project Demo

### Desktop Version Demo
Click the button repeatedly and watch the timer count up! Stop clicking and it stops after 5 seconds. Simple, chaotic, and effective!

### Web Version Demo
Modern UI with floating buttons - same functionality but in your browser at `localhost:5000`.

---

## Team Contributions

* **Divya Shankar:** Full-stack development including timer logic, Tkinter GUI, Flask web app, Material Design UI, GitHub integration, and project documentation

---

## Installation & Setup (Quick Start)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning repo)

### Step-by-Step Setup

```bash
# 1. Clone repository
git clone https://github.com/DevikaShankarD/useless_project_temp.git
cd timer

# 2. Install dependencies
pip install -e .
pip install Flask

# 3. Run Desktop Version
python main.py

# OR Run Web Version
python app.py
# Then open http://localhost:5000
```

---

## Project Structure
