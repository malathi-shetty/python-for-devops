import psutil
import time
from datetime import datetime

def write_log(message):
    with open("system_health.log", "a") as file:
        file.write(message + "\n")

print("SYSTEM MONITORING STARTED")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # -------------------------
        # INFO LOG (always)
        # -------------------------
        info_msg = f"{timestamp} [INFO] CPU={cpu}% MEMORY={memory}%"
        print(info_msg)
        write_log(info_msg)

        # -------------------------
        # ALERT LOGS
        # -------------------------
        if cpu > 80:
            alert_msg = f"{timestamp} [ALERT] CPU HIGH: {cpu}%"
            print(alert_msg)
            write_log(alert_msg)

        if memory > 80:
            alert_msg = f"{timestamp} [ALERT] MEMORY HIGH: {memory}%"
            print(alert_msg)
            write_log(alert_msg)

        time.sleep(5)

except KeyboardInterrupt:
    print("\nSCRIPT STOPPED MANUALLY (CTRL + C)")

    end_msg = f"{datetime.now()} [SYSTEM] Monitoring stopped by user"
    write_log(end_msg)

print("SCRIPT ENDED")