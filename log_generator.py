import requests
import time
import random
URL = "http://127.0.0.1:8000/logs"
levels = ["INFO", "WARNING", "ERROR"]
messages = [
    "User logged in",
    "Database connection lost",
    "File uploaded",
    "Memory usage high",
    "Payment failed",
    "Server restarted"
]
while True:
    log = {
        "level": random.choice(levels),
        "message": random.choice(messages)
    }

    try:
        res = requests.post(URL, json=log)
        print("Sent:", log)
    except Exception as e:
        print("Error:", e)

    time.sleep(2)  # send every 2 seconds
