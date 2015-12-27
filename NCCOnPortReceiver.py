# -*- coding: utf-8 -*-

'''
File name: NCCOnPortReceiver.py
Description: Network Covert Channel on Port
Python Version: 2.7
'''

import argparse
from scapy.all import *

class NCCOnPortReceiver(object):
    def __init__(self, iface):
        self.sniffer = sniff(iface=iface, filter="tcp", prn=self.parse)


    def parse(self, pkt):
        flag = pkt['TCP'].flags

        if flag == 0x40:    # ECE flag
            c = chr(pkt['TCP'].sport)
            #sys.stdout.write(c)
            sys.stdout.write(pkt.sniffed_on + ": " + pkt.summary() + ": " + c + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Network covert channel communication')
    parser.add_argument('--iface', nargs=1, required=True, help='interface name')
    args = parser.parse_args()

    recv = NCCOnPortReceiver(args.iface)
