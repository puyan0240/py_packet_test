import pkgutil
from telnetlib import IP
from scapy.all import *

target = '192.168.0.21'

#pkt = IP()/UDP()/Raw()

pkt = IP()

#IP Header
pkt.dst = '192.168.0.21'
#pkt.id = 99

#pkt.show()

pkt2 = UDP()

#UDP Header
pkt2.sport = 40000
pkt2.dport = 555
pkt2.len=123
#User Data


pkt3 = Raw()
pkt3.load = "1234".encode()


#Packet Show Command
#pkt2.show()

pkt = pkt/pkt2/pkt3
pkt.show()

#Packet Send Command
send(pkt)

#sr1(pkt)