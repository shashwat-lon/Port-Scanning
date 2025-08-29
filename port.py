import socket

def scan_ports(target, start_port, end_port):
    print(f"\n Scanning host: {target}")
    print(f"Ports: {start_port} - {end_port}\n")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)  # timeout for connection
            result = sock.connect_ex((target, port))  # 0 means open
            if result == 0:
                print(f" Port {port} is OPEN")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# --- Example Run ---
if __name__ == "__main__":
    target_host = input("Enter target host (e.g., 127.0.0.1 or example.com): ")
    start_p = int(input("Enter start port: "))
    end_p = int(input("Enter end port: "))
    
    scan_ports(target_host, start_p, end_p)
