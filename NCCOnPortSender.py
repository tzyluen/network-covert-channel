# -*- coding: utf-8 -*-

'''
File name: NCCOnPortSender.py
Description: Network Covert Channel on Port
Python Version: 2.7
'''

import argparse
import sys 
from scapy.all import *

class NCCOnPortSender(object):
    def __init__(self, iface):
        self.iface = iface


    def pack(self, char, dest_ip):
        payload = ord(char)
        # the TCP layer source port becomes the hidden data payload
        pkt = IP(dst=dest_ip)/TCP(sport=payload, dport=RandNum(0, 65535), flags="E")
        pkt.show2()
        return pkt 
      

    def broadcast(self, ip_list, message):
        print "Broadcast data: " + message
        for char in message:
            for ip in ip_list:
                new_pkt = self.pack(char, ip)
                send(new_pkt, verbose=False)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Network covert channel communication')
    #parser.add_argument('--src', nargs='?', required=True, help='source IP address and port')
    parser.add_argument('--iface', nargs=1, required=True, help='interface name')
    parser.add_argument('--dst', nargs='+', required=True, help='destination IP address list')
    parser.add_argument('--msg', nargs='?', required=True, help='secret message')
    args = parser.parse_args()

    ip_list = args.dst
    secret_msg = args.msg
    iface = args.iface

    sender = NCCOnPortSender(iface)
    sender.broadcast(ip_list, secret_msg)
