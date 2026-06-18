# OS Mechanisms and Technical Specifications
### **Component 4: Smart Hydration and Aid Stations**
**Team:** `Smart Fun Run TeamA Component4`

## Introduction
Our group was tasked with managing the resource tracking (water bottle stock) for the Smart Fun Run. To ensure the system remains stable and the data stays accurate when multiple aid stations send updates at once, we implemented several core Operating System concepts within our backend.

---

## 1. Handling Concurrency (Multithreading in `server.py`)
For the Smart Fun Run, we expect multiple hydration stations to send stock updates simultaneously. To prevent the server from becoming a bottleneck, we utilized a multithreaded architecture.  

**Implementation:** Each incoming request from the IoT hardware to the `/api/funrun` endpoint is processed by the OS backend in `server.py` within its own dedicated thread. This ensures the server is non-blocking and remains highly available.  

**Tracking:** Our code explicitly captures and logs the Thread ID and Process ID (PID) for every transaction. This allows our team of 6 OS developers to verify that the operating system is multitasking correctly during the event.  

**Purpose:** This prevents *Head of Line Blocking*, where one station's network lag could delay updates from others, maintaining high system responsiveness.

---

## 2. Synchronization and The Mutex Lock (Implemented in `server.py`)
Since all threads attempt to write to a single shared resource, the `hydration_log.xlsx` file, we had to address the risk of Race Conditions. Without synchronization, simultaneous writes would lead to file corruption or server crashes.  

**The Strict Mutex:** We implemented a Mutex Lock (`db_lock`) using the `threading.Lock()` primitive inside `server.py`.  

**The Critical Section:** We used a `with db_lock:` block to wrap the file writing logic. This acts as a gatekeeper: only one thread is granted the lock to access and write to the Excel file at any given moment.  

**Result:** By enforcing this strict synchronization, we guarantee absolute data integrity for bottle counts, ensuring the Smart Hydration system never loses track of resources.

---

## 3. File Management System (`database_handler.py` logic)
The OS backend handles the persistence of live data through a dedicated module to ensure it is stored and formatted correctly for event organizers.  

**Initialization Logic:** In `database_handler.py`, the `inisialisasi_excel()` function uses the `os.path` library to check for the log file's existence at startup. If the file is missing, the script automatically generates a new `.xlsx` file with established headers for tracking: *Date and Masa, Process ID, Thread ID, IP Address, Quantity (Botol), and Status*.  

**Auto Formatting:** To improve data readability, we implemented an Auto Fit algorithm. This logic uses the `openpyxl` library to calculate the character length in each cell and adjusts the Excel column widths dynamically, demonstrating an automated approach to file management.

---

## 4. System Monitoring and Fault Tolerance
We integrated several monitoring and stability features into our core server logic:  

**Identity Tracking:** In `server.py`, we log the IP Address of every incoming request to confirm the data originates from authorized IoT sensor hardware.  

**Robustness:** We wrapped the file operations in `try...except` blocks. If the file system experiences a temporary error (for example, if the file is opened by another program), the server catches the error and stays online rather than crashing. This ensures the system-wide stability required for a live Fun Run environment.
