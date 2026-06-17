OS Mechanisms & Technical Specifications
Component 4: Smart Hydration & Aid Stations
Team A - Smart-Fun-Run-TeamA-Component4
1. Concurrency and Multithreading
Our backend system is built on a multithreaded architecture using the Flask framework to handle high-frequency data from multiple aid stations simultaneously
.
Mechanism: When the IoT hardware sends bottle stock data (High, Medium, Low, or Empty), the OS creates a separate thread to process the request
.
Implementation: We explicitly track the Thread ID and Process ID (PID) for every transaction [Code].
Significance: This ensures the "Smart Fun Run" event stays responsive. Even if 20 stations send data at the exact same time, the OS schedules these threads to prevent the server from hanging or crashing under load
.
2. Resource Locks and Synchronization (Strict Mutex)
As required for Component 4, we have implemented strict OS mutexes to manage the shared resource of the hydration stock log
.
The Problem (Race Condition): If two threads attempt to write to the hydration_log.xlsx file at the same millisecond, the file could become corrupted, or data could be lost.
Our Solution: We implemented a Mutual Exclusion (Mutex) Lock using threading.Lock() [Code].
Strict Synchronization: By using the with db_lock: statement, we create a Critical Section
. Only one thread is granted the "key" to access the Excel file at a time. All other threads are placed in a waiting state until the lock is released, ensuring absolute data integrity for our water bottle totals
.
3. File Management System
The OS backend serves as a robust file manager for the event’s live data
.
Modular Architecture: To follow industry standards, we separated the logic into server.py (API and Synchronization) and database_handler.py (File I/O operations)
.
Automated Initialization: The system uses os.path.exists to check for the log file at startup. If missing, the OS automatically initializes a new .xlsx file with the required headers [Code].
Persistence and Formatting: We utilize the openpyxl library to append data persistently. Our code includes an Auto-Fit algorithm that dynamically adjusts column widths based on data length, ensuring the logs are instantly readable for human administrators [Code, 26].
4. System-Wide Monitoring and Robustness
To ensure the reliability required for a "competitive" ecosystem, we implemented several monitoring features
:
Process Identification: By logging the Process ID, we allow system administrators to monitor the backend as a stable background process (daemon)
.
Network Tracking: We capture the IP Address of the sender to verify that the data is coming from authorized aid station hardware [Code].
Error Handling: Our use of try...except blocks prevents system-wide failure if a file access error occurs, allowing the server to log the error and continue serving other stations

