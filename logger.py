from datetime import datetime

def log_alert(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[ALERT] {time} - {message}")
