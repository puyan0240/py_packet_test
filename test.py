import pkgutil
from telnetlib import IP
from scapy.all import *

target = '192.168.0.21'

pkt = IP()/UDP()/Raw()

#IP Header
pkt.dst = '192.168.0.21'
#pkt.id = 99

#UDP Header
pkt.sport = 40000
pkt.dport = 555

#User Data
pkt.load = "1234".encode()


#Packet Show Command
pkt.show()

#Packet Send Command
send(pkt)

#sr1(pkt)