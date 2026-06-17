# OS Mechanisms & Technical Specifications
### **Component 4: Smart Hydration & Aid Stations**
**Team:** `Smart-Fun-Run-TeamA-Component4`

## Introduction
Our group was tasked with managing the resource tracking (water bottle stock) for the Smart Fun Run. To ensure the system remains stable and the data stays accurate when multiple aid stations send updates at once, we implemented several core Operating System concepts within our backend.

---

## 1. Concurrency and Multithreading
Our backend system is designed to handle high-frequency data from multiple aid stations simultaneously by utilizing a **multithreaded architecture**.

*   **Mechanism:** Each incoming request from an IoT sensor to the `/api/funrun` endpoint is processed within a **separate execution thread**.

*   **Implementation:** We track the **Thread ID** and **Process ID (PID)** for every transaction to monitor how the OS manages concurrent tasks.

*   **Significance:** This ensures that the system remains responsive. If multiple runners or stations trigger data updates at once, the OS schedules these threads efficiently to prevent server bottlenecks. 

---

## 2. Resource Locks and Synchronization (Strict Mutex)
As specifically required for **Component 4**, we have implemented **strict OS mutexes** to manage the shared resource of the hydration stock log. 

*   **The Challenge (Race Conditions):** Without protection, two threads writing to the `hydration_log.xlsx` file at the same time would cause file corruption or data loss.

*   **The Solution:** We implemented a **Mutual Exclusion (Mutex) Lock** using `threading.Lock()`.

*   **Strict Synchronization:** By utilizing the `with db_lock:` statement, we define a **Critical Section**. 
    *   Only **one thread** is granted access to the file at a time.
    *   All other threads must wait in a queue until the lock is released.
    *   This guarantees absolute **data integrity** for the water bottle totals.

---

## 3. File Management System
The OS backend provides a robust file management layer to ensure all hydration data is stored and formatted correctly. 

*   **Automated Initialization:** The system uses `os.path.exists` to check for the log file at startup. If it is missing, the OS automatically creates a new `.xlsx` file with the correct headers.

*   **Persistence and Formatting:** We use the `openpyxl` library to append data persistently. 

*   **Dynamic Auto-Fit:** To improve usability, our code includes an algorithm that calculates the maximum length of data in each column and **automatically adjusts the column width**, ensuring the logs are always readable.

---

## 4. System-Wide Monitoring and Robustness
To meet the "Excellent" grade criteria, we integrated system-level monitoring features. 

*   **Process Identification:** Logging the **PID** allows administrators to track the server as a stable background process (daemon) within the OS environment.

*   **Network Security:** We capture the **IP Address** of every incoming request to verify that the data originates from authorized aid station hardware.

*   **Fault Tolerance:** Our implementation of `try...except` blocks ensures that file-level errors (like a locked file) do not crash the entire server, maintaining **system-wide stability**.
