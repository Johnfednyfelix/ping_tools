from scapy.all import *

ip = "192.168.1.248"
pkt = IP(dst=ip)/ICMP()
res = sr1(pkt, timeout=2, verbose=0)

if res:
    print(f"{ip} reachable. TTL={res.ttl}")
else:
    print(f"{ip} unreachable.")
