import pkgutil
from scapy.all import *

target = '192.168.0.21'

pkt = IP(dst=target)/ICMP()
pkt.show()

sr1(pkt)