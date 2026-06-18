# Smart-Fun-Run-TeamA-Component4: Smart Hydration & Aid Stations

**Smart Hydration & Aid Stations** is an integrated platform designed to **optimize** event resource management through real-time inventory tracking. **IoT sensors** programmed in **C++** monitor water bottle stock levels and instantly transmit status updates to a robust **Python-based OS backend**. To maintain 100% data integrity during the "Smart Fun Run," the server utilizes **multithreading** to process concurrent updates from multiple stations and **strict mutex synchronization** to prevent race conditions within the shared Excel database. This professional-grade system ensures organizers have access to **automatically formatted, live-updating logs**, enabling seamless aid station operations and efficient resource management throughout the entire event.

---

## 👥 Team Members

| Name | Matric Number | Role |
| :--- | :--- | :--- |
| **MUHAMMAD AIDIL BIN SUHAIMI** | CN230086 | IoT Developer |
| **HAQEEMY A'IMULLAH BIN NAZRI** | CN230029 | IoT Developer |
| **MUHAMMAD HILMAN BIN KAMARUDIN** | CN230050 | IoT Developer |
| **SITI NURFATIHAH BINTI ROLIE** | CN240193 | OS Developer |
| **NURIN SYAHMINA BINTI MOHD AFIZAN** | CN240359 | OS Developer |
| **NIK NUR SABRINA BINTI PAIMAN** | CN240147 | OS Developer |
| **AMIRAH EZZATI** | CN240451 | OS Developer |
| **AHMAD SHAHEER KHUSAIRI BIN MOHD AMBRIM** | CN230434 | OS Developer |
| **HAZIQ HAKIMI BIN HUSHAIMI** | CN230244 | OS Developer |

---

## 🚀 Key Features

*   **Concurrent Resource Management:** Multithreaded Python server capable of handling simultaneous updates from multiple hydration stations without blocking.
*   **Strict Mutex Synchronization:** Implements a robust `threading.Lock()` mechanism to protect the database from race conditions during concurrent writes.
*   **Automated Data Persistence:** A custom backend "Librarian" system that automatically initializes the log and applies an **Auto-Fit algorithm** for real-time Excel formatting.
*   **Live Inventory Tracking:** Physical IoT nodes provide instant status levels (High, Medium, Low, Empty) for proactive event coordination.

---

## 🛠️ Technology Stack

*   **IoT (Edge):** C++, Arduino, JSON-standardized payloads.
*   **OS (Backend):** Python 3.x, Flask (API Framework).
*   **Data Engine:** Openpyxl for Excel management and persistent logging.
*   **OS Mechanisms:** Multithreading, Process ID (PID) tracking, and Mutex/Resource Locking.

---

## 📋 Quick Start Guide

1.  **Hardware Deployment:** Power on the IoT sensor node and ensure it is connected to the event local network.
2.  **Server Activation:** Navigate to the `src_os` directory and execute:
    ```bash
    python serverdata.py
    ```
3.  **Live Monitoring:** Open the `media/hydration_log.xlsx` file. The backend will automatically create and format the log upon receiving the first data packet.
4.  **System Verification:** Observe the server terminal to track incoming **Thread IDs** and **Process IDs** to confirm concurrent operation.

---

## 📂 Folder Structure

*   [**`docs/`**](docs/) - System architecture diagrams, hardware setup guides, and detailed OS mechanism reports.
*   [**`src_iot/`**](src_iot/) - C++ source code for microcontrollers and standardized JSON payload definitions.
*   [**`src_os/`**](src_os/) - Multithreaded server logic and automated Excel database handler scripts.
*   [**`media/`**](media/) - High-quality photos and video demonstrations of the integrated prototype.

---

## 📜 OS Technical Specifications

This system serves as a practical implementation of core Operating System concepts as required by the project rubrics:
*   **Synchronization:** Guaranteed data integrity through strict mutex locks on shared resources to prevent race conditions.
*   **Concurrency:** High-availability server design utilizing independent execution threads to handle multiple incoming station requests. 
*   **File Management:** Systematic I/O handling for long-term data persistence and automated retrieval in an Excel environment. 

