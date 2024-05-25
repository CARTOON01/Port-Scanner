import socket
import nmap

def initial_scan(target, port_range):
    open_ports = []
    print(f"Initial scan on {target} for open ports...\n")
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
            print(f"Port {port} is open")
        sock.close()
    if not open_ports:
        print("No open ports found.")
    return open_ports

def detailed_scan(target, open_ports):
    nm = nmap.PortScanner()
    args = '-sC -sV -vv -T4 --min-rate 1750'
    scan_range = ','.join(map(str, open_ports))
    
    print(f"\nDetailed scan on {target} for open ports {scan_range} with arguments {args}...\n")
    nm.scan(target, scan_range, arguments=args)
    
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                port_info = nm[host][proto][port]
                print(f"Port: {port}\tState: {port_info['state']}\tService: {port_info['name']}\tVersion: {port_info.get('version', '')}")

def main():
    target = input("Enter the IP address or URL to scan: ")
    port_range = range(1, 1025)  # default port range from 1 to 1024
    
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
        return

    open_ports = initial_scan(ip, port_range)
    if open_ports:
        detailed_scan(ip, open_ports)

if __name__ == "__main__":
    main()
