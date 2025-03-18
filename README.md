**Objective**
The purpose of this project is to continuously monitor a MySQL database and log its status (UP/DOWN). This aligns with **GAMP 5 Category 1 (Infrastructure Software)** and supports Computer System Validation (CSV).

The key goals include:
1. Ensuring real-time monitoring of database availability.
2. Logging the database status accurately for audit and compliance.
3. Validating the system using IQ, OQ, and PQ processes.

**Project Overview**

The Database Monitoring System continuously checks the status of a MySQL database. It logs whether the database is UP (available) or DOWN (unavailable) every minute and stores the results in a CSV file. This project aligns with GAMP 5 Category 1 (Infrastructure Software) for Computer System Validation (CSV).

 **System Requirements**

Operating System: Windows 10/11, Linux (Ubuntu), macOS
Python Version: Python 3.13+
MySQL Server: MySQL 8.0+
Tools: Git for version control
**Step 1: Set Up the Project**
**Create a Project Folder**
fOR Eg;-
cd /c/Dms
mkdir "Real time projects -CSV"
cd "Real time projects -CSV"**
**Set Up a Virtual Environment**
python -m venv dbms_monitor_env
source dbms_monitor_env/Scripts/activate  **(For Windows)**
**Install Required Package**
pip install mysql-connector-python
**Create the Python Script**
Create a file called db_monitor.py and paste the following code:
import mysql.connector
import time
import csv
from datetime import datetime

# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'test_db'
}

def monitor_db():
    while True:
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            if connection.is_connected():
                print("✅ Database is connected!")
                status = "UP"
                connection.close()
        except Exception as e:
            print("❌ Database is NOT connected:", e)
            status = "DOWN"

        # Log Status
        log_status(status)
        time.sleep(60)  # Check every minute

def log_status(status):
    with open('db_monitor_log.csv', mode='a', newline='') as log_file:
        writer = csv.writer(log_file)
        if log_file.tell() == 0:
            writer.writerow(["Time", "Status"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status])

if __name__ == '__main__':
    monitor_db()

**Create the Database**
python db_monitor.py
Note:-You should see: ✅ Database is connected! and logs will be recorded in db_monitor_log.csv.

**Results**
The database monitoring system was successfully validated:

1. **Installation Qualification (IQ)**: Python 3.13 and MySQL were installed and verified.
2. **Operational Qualification (OQ)**: The system accurately detected both database UP and DOWN states.
3. **Performance Qualification (PQ)**: The script operated continuously for 24 hours without failure, ensuring accurate data logging.
