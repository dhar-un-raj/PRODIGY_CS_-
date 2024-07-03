# Packet Sniffer Tool

This packet sniffer tool captures and analyzes network packets, displaying relevant information such as source and destination IP addresses, protocols, and payload data. This tool is intended for educational purposes only.

## Features

- Capture and display source and destination IP addresses
- Identify and display network protocols (TCP, UDP, ICMP)
- Display packet payload data

## Prerequisites

- Python 3.x
- Scapy library
- Npcap (for Windows users)

## Installation

1. **Install Scapy:**

    ```sh
    pip install scapy
    ```

2. **Install Npcap (for Windows users):**

    - Download the Npcap installer from the [Npcap download page](https://nmap.org/npcap/).
    - Run the installer and follow the instructions. Ensure that you check the option to install Npcap in "WinPcap API-compatible Mode" if prompted.

## Usage

1. **Clone the repository:**

    ```sh
    git clone https://github.com/dhar-un-raj/packet-sniffer-tool.git
    cd packet-sniffer-tool
    ```

2. **Run the packet sniffer:**

    Ensure you run the script with administrator or root privileges:

    ```sh
    sudo python packet_sniffer.py
    ```

    For Windows, run the script with administrator privileges.

## Ethical Considerations

- **Educational Purposes**: The tool should only be used in a controlled environment, such as a lab setup for learning and testing purposes.
- **Authorization**: Ensure you have permission to capture and analyze network traffic on the network you are monitoring.
- **Privacy**: Be aware of privacy implications and avoid capturing sensitive information unless explicitly permitted.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License

## Acknowledgements

- This project uses the [Scapy](https://scapy.net/) library for packet manipulation.
- Npcap is used for packet capturing on Windows systems.

## Contact

For any inquiries, please contact [dharunraj857@gmail.com].
