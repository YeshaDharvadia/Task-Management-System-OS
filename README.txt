# Task Management System — Operating Systems Project

 Developers:
- **Yesha Dharvadia**
- **Antara Patel**

---

📌 Project Overview
This project is a simple **Task Management System** built using Python (Tkinter + psutil).
It demonstrates key **Operating System concepts** such as:

✅ Process Management  
✅ CPU Scheduling  
✅ Memory Monitoring  
✅ System Resource Management  
✅ File Handling (Logging System Events)

The application works like a **mini Task Manager**, showing real-time system status.

---

## 🧠 Operating System Concepts Used

| OS Concept | How this project uses it |
|----------------|-------------------------------|
| **Process Management** | Counts and displays active processes using `psutil.pids()` |
| **CPU Scheduling** | Shows CPU usage %, proving CPU sharing among processes |
| **Memory Management** | Shows RAM usage using `psutil.virtual_memory()` |
| **Concurrency / Multitasking** | Multiple tasks and system processes running simultaneously |
| **Logging & File Handling** | Logs daily resource status into a text file (`system_log.txt`) |

---

🖥️ Features
- Count **Active Processes**
- Display **CPU Usage (%)**
- Display **RAM Usage (%)**
- Refresh button for real-time monitoring
- Log writing for system history

---

🛠️ Requirements
Install required Python package:

```sh
pip install psutil
