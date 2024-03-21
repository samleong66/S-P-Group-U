from scapy.all import *

send(IP(dst="10.211.55.3")/fuzz(UDP()),loop=1)