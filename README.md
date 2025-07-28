# 🌙 ReadMoonbitSerial
A mini-robotics project to read real-time sensor data (light and temperature) from a BBC Micro:bit using USB serial and log it to CSV using Python.
-----------------
Optional future enhancements include real-time graphing and a C++ port for embedded development practice.

## Project Overview
### Goal:
Capture and log Micro:bit sensor data using a Python script on Ubuntu.

This is part of a personal robotics micro-project milestone focused on:

- Embedded sensor reading
- Serial communication
- Logging data for analysis
- Clean code structure and repo hygiene

## Project Structure
```graphql
ReadMoonbitSerial/
├── Documentation/          # Project notes, recordings, and planning docs
│   ├── LDR measurement recording.mp4
│   ├── Learned Unix commands.odt
│   └── Project Instructions.odt
├── logs/                   # Logged sensor data
│   └── Microbit Read Out.csv
├── makecode/               # Microbit .hex file for serial output
│   └── microbit-Reads-on-board-temp-and-light.hex
├── python/                 # Python script and venv
│   ├── read_serial.py
│   └── requirements.txt
├── .gitignore
└── README.md
```
-----------------------

## 🛠️ Setup and Usage
### 1. Flash the Micro:bit
Use MakeCode or any Micro:bit editor to upload the .hex file in makecode/.
The code reads:
- Onboard temperature
- External light level from LDR (connected via voltage divider)

#### Serial output format:
```makefile
Light:1020, Temp:27
```

### 2. Python Script
The Python script reads 10 lines of data from the micro:bit serial port and saves it as CSV.

#### Prerequisites
Make sure you're in the python/ folder and have Python 3 + pip:

```bash
    cd python/
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
 ```
 requirements.txt contains:

```nginx
pyserial
pandas
```
---------------------------

### Run the Script
```bash
    python read_serial.py
```

Make sure your Micro:bit is connected and accessible via /dev/ttyACM0.

Output is saved to:
```mathematica
../logs/Microbit Read Out.csv
```
----------------------------

### Code Summary
- Uses pyserial to read /dev/ttyACM0
- Collects 10 sensor rows
- Adds timestamps to each reading
- Saves to CSV via pandas
-------------------------

## Completed Milestones
 - Part 1 – Detect Micro:bit on serial port using Linux tools (dmesg, /sys/class/tty)
 - Part 2 – Flash Micro:bit with MakeCode to output serial data
 - Part 3 – Python script to read and clean serial data
 - Part 4 – Organized repo structure
 - Part 5 – CSV logging using pandas

-----------------

## 🚧 Future Work
- Live data plotting using `matplotlib` 
- Add CLI interface or GUI panel for logging control
- Port script to C++ (POSIX serial I/O)
- Visual dashboard using Unity or web app 
- Update micro:bit video with proper script and demonstration
- Add demo of USB serial output from Micro:bit to terminal
- Add support for --duration or --mode CLI flags to toggle logging/streaming
- Export `matplotlib` plots as PNG images for Unity/Web use
- Use rotating CSV logs or timestamped output files
- Add replay mode to simulate live streaming from past logs
- Optional: stream real-time data to a Flask server or WebSocket for remote dashboards

## 🎥 Demo
[Watch the demo video of microbit](https://youtube.com/shorts/u0WQgC-p3ss?feature=share)
