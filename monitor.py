import psutil
import os
import csv
import datetime
import time
LOG_FILE = "logs/system_usage.csv"
os.makedirs("logs", exist_ok=True)
if not os.path.exists(LOG_FILE): 
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "cpu", "memory"])
def log_metrics():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    with open(LOG_FILE, "a", newline="") as f: 
        writer = csv.writer(f)
        writer.writerow([timestamp, cpu, memory])
if __name__ == "__main__":
    while True:
        log_metrics()
        time.sleep(5)