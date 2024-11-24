import os
from colorama import Fore, init
import time

def banner():
    print(Fore.RED + '''
╔═╗╔═╗╔╦╗╔═╗╔═╗╦  
║ ║╚═╗ ║ ║ ║║ ║║  
╚═╝╚═╝ ╩ ╚═╝╚═╝╩═╝ - TK''')
    print("")
    print(Fore.YELLOW + "1) Ping IP")
    print(Fore.RED + "2) Trace IP Route")
    print(Fore.MAGENTA + "3) Tracert IP")
    print(Fore.BLUE + "4) Remote Shutdown IP")
    print(Fore.GREEN + "5) Matrix")
    print(Fore.YELLOW + "6) Exit")
    print("")
    print("")

def ping():
    os.system('cls')
    ip = input(Fore.BLUE + "Enter IP To Ping: ")
    print(Fore.RED + f"[+] PINGING {ip}...")
    time.sleep(1)
    print(Fore.MAGENTA)
    os.system(f'ping {ip}')
    print("")
    time.sleep(1)
    input(Fore.GREEN + "Press Enter To Continue...")

def geo():
    os.system('cls')
    ip1 = input(Fore.BLUE + "Enter IP To Trace Route: ")
    print(Fore.RED + f"[+] TRACING {ip1}")
    time.sleep(1)
    print(Fore.MAGENTA)
    os.system(f'curl https://ipinfo.io/{ip1}/json')
    print("")
    time.sleep(1)
    print("")
    input(Fore.GREEN + "Press Enter To Continue...")

def trace():
    os.system('cls')
    ip2 = input(Fore.BLUE + "Enter IP To Tracert: ")
    print(Fore.RED + f"[+] SCANNING {ip2}...")
    time.sleep(1)
    print(Fore.MAGENTA)
    os.system(f'tracert {ip2}')
    time.sleep(1)
    input(Fore.GREEN + "Press Enter To Continue...")

def rsip():
    os.system('cls')
    input(Fore.RED + "[+] Press Enter To Open Menu...")
    os.system('shutdown -i')
    time.sleep(1)
    input(Fore.GREEN + "Press Enter To Continue...")

def matrix():
    print(Fore.GREEN)
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')
    os.system('tree')

def choice():
    while True:
        os.system('cls')
        banner()
        choice = input("CHOICE -> ")

        if choice == "1":
            ping()
        elif choice == "2":
            geo()
        elif choice == "3":
            trace()
        elif choice == "4":
            rsip()
        elif choice == "5":
            matrix()
        elif choice == "6":
            os.system('cls')
            print("GOOBYE...")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "[-] Please Enter Valid Option!")
            time.sleep(1)

if __name__ == "__main__":
    choice()