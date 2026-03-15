from datetime import datetime
import os
import json

def log(message):

    time = datetime.now().strftime("%H:%M:%S")

    os.makedirs("Logs", exist_ok=True)  # ensures folder exists

    file = "Logs/logs.json"

    log_data = {
        "time": time,
        "message": message
    } 

    try:
        with open(file, "r") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    # Add new log
    logs.append(log_data)

    # Rewrite file with updated list
    with open(file, "w") as f:
        json.dump(logs, f, indent=4)