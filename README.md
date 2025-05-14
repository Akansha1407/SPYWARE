🛡️ SPYWARE

This Python project demonstrates multiple techniques used in ethical hacking and system monitoring. It captures keystrokes, extracts system and clipboard information, retrieves browser history, and takes screenshots — all stored in local files for analysis and learning.

> 🚨 **This tool is created strictly for educational and ethical learning purposes. Do not use it on any device without explicit permission.**

---
 📌 Features

1. 🔤 Keystroke Logging
- Captures all keyboard inputs using `pynput`
- Stores keystrokes in a local text file

2. 💻 System Information
- Collects:
  - OS Name, Version
  - Machine Name
  - IP Address
  - Processor Info
- Stores output in an Excel file using `pandas`

3. 📋 Clipboard Data
- Extracts current clipboard contents
- Saves to a text file
- Uses `win32clipboard` (Windows only)

4. 🌐 Chrome Browser History
- Retrieves Google Chrome browsing history
- Parses and formats it using `sqlite3` and `pandas`
- Saves it to an Excel file

5. 🖼️ Screenshot Capture
- Takes a full screenshot of the current screen
- Saves it as a `.png` file using `Pillow`


🧰 Required Libraries
pynput: For capturing keystrokes.

pandas: For handling and saving data (system info, browser history).

platform: For retrieving system information.

socket: For retrieving IP address.

win32clipboard: For reading clipboard contents (Windows-only).

sqlite3: For retrieving Google Chrome browsing history.

Pillow: For taking screenshots.

imagegrab: For capturing screenshots (part of Pillow).




---
