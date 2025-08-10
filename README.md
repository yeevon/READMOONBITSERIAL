# 🌙 ReadMoonbitSerial

A mini-robotics project to read real-time sensor data (light and temperature) from a BBC Micro:bit using USB serial and log it to CSV using Python.

> Optional enhancements now include **live plotting** while logging (added today) and a future C++ port.

## Project Overview

### Goal

Capture and log Micro:bit sensor data on Ubuntu using a Python script.

This project focuses on:

- Embedded sensor reading
- Serial communication
- Logging data for analysis
- Clean code structure and repo hygiene

**Default behavior:** CSV logging only (no UI).  
**Optional (added today):** live plotting during capture.

---

## Project Structure

```ini
ReadMoonbitSerial/
├── Documentation/          # Project notes, recordings, and planning docs
│   ├── LDR measurement recording.mp4
│   ├── Learned Unix commands.odt
│   └── Project Instructions.odt
├── logs/                   # Logged data & optional snapshots
│   ├── Microbit Read Out.csv
│   └── final_graph.png         # saved on exit if live plotting is enabled
├── makecode/               # Micro:bit .hex for serial output
│   └── microbit-Reads-on-board-temp-and-light.hex
├── python/                 # Python scripts and venv
│   ├── read_serial.py          # serial read + CSV logging (+ optional live plot)
│   ├── graph_data.py           # live plotting helper (added today)
│   └── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Setup and Usage

### 1) Flash the Micro:bit

Use MakeCode or any Micro:bit editor to upload the .hex file in makecode/.

Device serial output format:

```makefile
Light:1020, Temp:27
```

(The Python script appends an ISO TimeStamp when logging.)

### 2) Python environment

From python/:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

requirements.txt contains:

```text
pyserial
pandas
matplotlib  # optional, only needed for live plotting
```

### 3) Run the Script

```bash
python read_serial.py
```

- Device path defaults to /dev/ttyACM0.
- Continuous capture until you disconnect the Micro:bit or press Ctrl+C.

#### CSV output

```mathematica
../logs/Microbit Read Out.csv
```

## Headless vs live window

- By default (non-GUI/Agg backend), no window opens — CSV logging still works.
- To show a live plot window (optional):
  - Install a GUI backend (one option):

```bash
sudo apt-get install -y python3-tk
```

- Run with an interactive backend:

```bash
MPLBACKEND=TkAgg python read_serial.py
```
  
- A snapshot of the final plot is saved to ../logs/final_graph.png on exit.

---

### Code Summary

- Reads Micro:bit serial (/dev/ttyACM0) via pyserial
- Parses Light and Temp, appends ISO TimeStamp
- Continuous capture; writes a CSV on exit
- Optional: live plots Light & Temp (two subplots) during capture and saves final_graph.png at shutdown

---

### ✅ Completed Milestones

- Part 1 – Detect Micro:bit on serial (dmesg, /sys/class/tty)
- Part 2 – Flash Micro:bit to output serial data
- Part 3 – Python script to read and clean serial data
- Part 4 – Organized repo structure
- Part 5 – CSV logging using pandas
- Part 6 – Basic Matplotlib plotting (CSV snapshot & optional live plot) ✔️ (added today)

---

### 🚧 Future Work

- Live plotting polish (FPS throttle, history cap, clean headless switch)
- Port serial reader to C++ (POSIX serial I/O)
- CLI flags (port, baud, log path, headless/GUI)
- Visual dashboard (Unity or simple web app)
- Update micro:bit demo video with final script
- Echo data back to Micro:bit over USB for a round-trip demo

---

## 🎥 Demo

[Watch the demo video of microbit](https://youtube.com/shorts/u0WQgC-p3ss?feature=share)