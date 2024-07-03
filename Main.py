from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if TCP in packet:
            proto = "TCP"
            payload = bytes(packet[TCP].payload)
        elif UDP in packet:
            proto = "UDP"
            payload = bytes(packet[UDP].payload)
        elif ICMP in packet:
            proto = "ICMP"
            payload = bytes(packet[ICMP].payload)
        else:
            proto = str(protocol)
            payload = bytes(packet[IP].payload)
        
        print(f"IP Src: {ip_src} -> IP Dst: {ip_dst} | Protocol: {proto} | Payload: {payload[:20]}")  # Limiting payload to first 20 bytes for brevity

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
