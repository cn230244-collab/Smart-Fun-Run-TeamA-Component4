# OS Mechanisms & Technical Specifications
### **Component 4: Smart Hydration & Aid Stations**
**Team:** `Smart-Fun-Run-TeamA-Component4`

## Introduction
Our group was tasked with managing the resource tracking (water bottle stock) for the Smart Fun Run. To ensure the system remains stable and the data stays accurate when multiple aid stations send updates at once, we implemented several core Operating System concepts within our backend.

---

### 1. Handling Concurrency (Multithreading in `server.py`)
For the Smart Fun Run, we expect multiple hydration stations to send stock updates simultaneously. To prevent the server from becoming a bottleneck, we utilized a multithreaded architecture.

*   **Implementation:** Each incoming request from the IoT hardware to the `/api/funrun` endpoint is processed by the OS backend in **`server.py`** within its own dedicated thread.
*   **Tracking:** Our code explicitly captures and logs the **Thread ID** and **Process ID (PID)** for every transaction. This allows our team of 6 OS developers to verify that the operating system is multitasking correctly during the event.
*   **Purpose:** This ensures that if one station experiences network lag, it does not block the water level updates from other aid stations, maintaining high system responsiveness.

---

### 2. Synchronization & The Mutex Lock (Implemented in `server.py`)
Since all threads attempt to write to a single shared resource—the `hydration_log.xlsx` file—we had to address the risk of **Race Conditions**. Without synchronization, simultaneous writes would lead to file corruption or server crashes.

*   **The Lock:** As required for Component 4, we implemented a **Strict Mutex Lock** (`db_lock`) using `threading.Lock()` inside **`server.py`**.
*   **The Critical Section:** We used a `with db_lock:` block to wrap the file-writing logic. This acts as a gatekeeper: only one thread is granted the "lock" to access and write to the Excel file at any given moment.
*   **Result:** By enforcing this strict synchronization, we guarantee absolute data integrity for bottle counts, ensuring the "Smart Hydration" system never loses track of resources.

---

### 3. File Management System (`database_handler.py`)
The OS backend handles the persistence of live data through a dedicated module to ensure it is stored and formatted correctly for event organizers.

*   **Automation:** In **`database_handler.py`**, we used the `os.path` library to verify the existence of the log file at startup. If the file is missing, the script automatically generates a new `.xlsx` file with established headers for tracking.
*   **Auto-Formatting:** To improve data readability, we implemented an "Auto-Fit" algorithm within the handler. This logic calculates the character length in each cell and adjusts the Excel column widths dynamically, demonstrating an automated approach to file presentation and management.

---

### 4. System Monitoring and Fault Tolerance
We integrated several monitoring and stability features into our core server logic:

*   **Identity Tracking:** In **`server.py`**, we log the **IP Address** of every incoming request to confirm the data originates from authorized IoT sensor hardware.
*   **Robustness:** We wrapped the file operations in `try...except` blocks. If the file system experiences a temporary error (e.g., if the file is opened by another program), the server catches the error and stays online rather than crashing. This ensures the system-wide stability required for a live "Fun Run" environment.
