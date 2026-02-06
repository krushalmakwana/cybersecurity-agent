def cybersecurity_bot():
    print("Cybersecurity Agent is running...")
    print("Ask me a cybersecurity question.")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("You: ").lower()

        if question == "exit":
            print("Agent stopped.")
            break

        elif "phishing" in question:
            print("Agent: Phishing is a cyber attack where attackers trick users into revealing sensitive information.")

        elif "malware" in question:
            print("Agent: Malware is malicious software designed to damage or gain unauthorized access to systems.")

        elif "firewall" in question:
            print("Agent: A firewall is a security system that monitors and controls incoming and outgoing network traffic.")

        elif "brute force" in question:
            print("Agent: Brute force attack attempts to guess passwords by trying many combinations.")

        elif "vpn" in question:
            print("Agent: VPN creates a secure encrypted connection over the internet.")

        else:
            print("Agent: Sorry, I don't know the answer yet.")

if __name__ == "__main__":
    cybersecurity_bot()
