import socket
import sys
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def port_scanning(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5) #timeout speed to be set here
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    service_name = socket.getservbyport(port)
                except:
                    service_name = "unidentified"

                try:
                    banner = s.recv(1024).decode().strip()
                    banner_info = f" | Banner: {banner}"
                except:
                    banner_info = ""
                print(f"Port {port:5}: OPEN ({service_name}){banner_info}")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    target_input = input ("Enter the host address:")
        

    try:
        target = socket.gethostbyname(target_input)
    except socket.gaierror:
        print ("\n[!] Error: Hostname could not be resolved.")
        return
    
    #port range input
    print("\nSelect scan type:")
    print("1. Common Ports (21 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080)")
    print("2. Custom Range (eg., 1-500)")

    choice = input("Enter choice (1 or 2): ")

    ports_to_scan = []
    if choice == "1":
        ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    else:
        start_p = int(input("Enter starting port: "))
        end_p = int(input("Enter ending port: "))
        ports_to_scan = range(start_p, end_p +1)

    print("-" * 50)
    print(f"scanning target: {target}")
    print(f"started at: {datetime.now()}")
    print("-" * 50)


    #thread executor
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports_to_scan:
            executor.submit(port_scanning, target, port)

    print ("-" * 50)
    print(f"Scan completed at: {datetime.now()}")


if __name__ == "__main__":
    main()
