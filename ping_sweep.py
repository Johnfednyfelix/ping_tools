from scapy.all import *
import ipaddress

subnet = ipaddress.IPv4Network("192.168.1.0/24")

for ip in subnet.hosts():
    pkt = IP(dst=str(ip))/ICMP()
    res = sr1(pkt, timeout=1, verbose=0)
    if res:
        print(f"{ip} is UP")
