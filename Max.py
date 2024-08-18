import socket
from colorama import Fore, init


init(autoreset=True)

UDP_IP = "185.107.192.21"
UDP_PORT = 51814
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print(Fore.LIGHTGREEN_EX + "[!] Attack sent successfully!")
except Exception as e:
    print(Fore.RED + "[!] Failed to send attack: %s" % str(e))