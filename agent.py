from detector import detect_bruteforce
from config import LOG_FILE

def load_logs():
    with open(LOG_FILE, "r") as file:
        return file.readlines()

def run_agent():
    print("Cybersecurity Agent Started...\n")
    logs = load_logs()
    detect_bruteforce(logs)
    print("\nMonitoring completed.")

if __name__ == "__main__":
    run_agent()
