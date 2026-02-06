from collections import defaultdict
from logger import log_alert
from config import FAILED_LOGIN_THRESHOLD

def detect_bruteforce(log_lines):
    ip_counter = defaultdict(int)

    for line in log_lines:
        if "FAILED_LOGIN" in line:
            ip = line.split()[0]
            ip_counter[ip] += 1

            if ip_counter[ip] == FAILED_LOGIN_THRESHOLD:
                log_alert(f"Possible brute-force attack from IP {ip}")
