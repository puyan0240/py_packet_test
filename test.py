import pkgutil
from telnetlib import IP
from scapy.all import *

target = '192.168.0.21'

#pkt = IP(dst=target)/ICMP()

pkt = IP()/UDP()
pkt.dst = '192.168.0.21'
pkt.id = 99
pkt.show()

pkt.dport = 555

send(pkt)

#sr1(pkt)