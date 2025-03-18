import mysql.connector  # Connect to MySQL
import time  # Keep track of time
import csv  # Write logs to a CSV file

# Step 1: Database Information (Update this!)
DB_CONFIG = {
    "host": "localhost",      # Your MySQL host (use 'localhost' if local)
    "user": "root",           # Your MySQL username
    "password": "root", # Your MySQL password
    "database": "test_db"     # Replace with your database name
}

# Step 2: Connect to the Database
def connect_to_db():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("✅ Database is connected!")
        return connection
    except Exception as e:
        print("❌ Database is NOT connected:", e)
        return None

# Step 3: Monitor and Save Logs
def monitor_db():
    with open("db_monitor_log.csv", mode="a", newline="") as log_file:
        writer = csv.writer(log_file)
        writer.writerow(["Time", "Status"])

        while True:
            connection = connect_to_db()
            status = "UP" if connection else "DOWN"

            # Save the status to CSV
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), status])

            # Close the database connection if it's open
            if connection:
                connection.close()

            print(f"Status: {status}")
            time.sleep(60)  # Wait for 1 minute before checking again

# Step 4: Start Monitoring
monitor_db()
