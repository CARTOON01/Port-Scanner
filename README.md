# Advanced Port Scanner

This is a Python-based port scanner that performs an initial scan to identify open ports on a given IP address or URL. Once the open ports are identified, it conducts a detailed scan to gather additional information about the services running on those ports using the `nmap` tool.

## Features

- **Initial Port Scan**: Scans a range of ports (default 1-1024) to identify which ports are open.
- **Detailed Port Scan**: Performs a detailed scan on the open ports to retrieve service and version information.
- **User Input**: Prompts the user to input the target IP address or URL and the ports to scan.

## Requirements

- Python 3.x
- `nmap` installed on your system. You can install it using a package manager:

  ```bash
    sudo apt-get install nmap  # for Debian-based systems

    python-nmap library. You can install it using pip:

    sh

    pip install python-nmap
  ```

## Usage

    Clone the repository or download the script:

    sh

    git clone <https://github.com/CARTOON01/Port-Scanner.git>

    cd Port-Scanner

    Run the script:

    sh

    ``` bash
        python advanced_port_scanner.py

        Enter the IP address or URL and the ports to scan when prompted.

    ```

## Example

sh

```bash
$ python advanced_port_scanner.py
Enter the IP address or URL to scan: 10.10.10.4
Enter the ports to scan (comma-separated): 21,22,139,445,3632

Initial scan on 10.10.10.4 for open ports...

Port 21 is open
Port 22 is open
Port 139 is open
Port 445 is open
Port 3632 is open

Detailed scan on 10.10.10.4 for open ports 21,22,139,445,3632 with arguments -sC -sV -vv -T4 --min-rate 1750...

Host: 10.10.10.4 ()
State: up
Protocol: tcp
Port: 21	State: open	Service: ftp	Version: vsftpd 3.0.2
Port: 22	State: open	Service: ssh	Version: OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
Port: 139	State: open	Service: netbios-ssn	Version: Samba smbd 4.7.6-Ubuntu
Port: 445	State: open	Service: microsoft-ds	Version: Windows 7 Professional 7601 Service Pack 1
Port: 3632	State: open	Service: distccd	Version: distccd v1 (GNU/Linux 8.3.0)
```

## Code Structure

    initial_scan(target, port_range):
        Performs a basic scan over a range of ports to determine which ports are open using the socket library.
        Returns a list of open ports.

    detailed_scan(target, open_ports):
        Performs a detailed scan on the open ports using the python-nmap library.
        Prints detailed information about each open port, including state, service name, and version.

    main():
        Prompts the user to input the target IP address or URL and the ports to scan.
        Calls initial_scan to find open ports.
        If open ports are found, calls detailed_scan to perform a detailed analysis.

## Notes

    Ensure you have the necessary permissions to run the scans.
    The script uses a default port range of 1-1024 for the initial scan. You can modify this range as needed.
