#!/usr/bin/python3
# -*- coding: utf-8 -*-

from scapy.all import *


'''
请求类型：ANY qtype='ANY'
默认为DNS_RD=1递归请求
'''


def generate_pkts(src_ip, dst_ip, query_type, packet_number, DNS_RD, ttl_length, dns_port, domain):
    if query_type == 'ANY':
        pkts = generate_any_type_dns_packets(src_ip, dst_ip, ttl_length=ttl_length,
                                             DNS_RD=DNS_RD, packet_number=packet_number,  dns_port=dns_port, domain=domain)
    elif query_type == 'A':
        pkts = generate_a_type_dns_packets(src_ip, dst_ip, ttl_length=ttl_length,
                                           DNS_RD=DNS_RD, packet_number=packet_number,  dns_port=dns_port, domain=domain)
    return pkts


def generate_any_type_dns_packets(src_ip, dst_ip, DNS_RD=1, ttl_length=128, packet_number=30, dns_port=53, domain='test.com'):
    pkt_list = []
    for il in range(packet_number):
        newp = Ether()/IP(src=src_ip, dst=dst_ip, ttl=ttl_length)/UDP(sport=30000+il, dport=dns_port) / \
            DNS(id=100+il*5, rd=DNS_RD, qd=DNSQR(qname=domain, qtype=255))
        print(src_ip)
        pkt_list.append(newp)
    return pkt_list


'''
请求类型：A qtype=1（默认）
默认为DNS_RD=1递归请求
'''


def generate_a_type_dns_packets(src_ip, dst_ip, DNS_RD=1, ttl_length=128, packet_number=30, dns_port=53, domain='test.com'):
    pkt_list = []
    for il in range(packet_number):
        newp = Ether()/IP(src=src_ip, dst=dst_ip, ttl=ttl_length)/UDP(sport=30000+il,
                                                                      dport=dns_port)/DNS(id=100+il*5, rd=DNS_RD, qd=DNSQR(qname=domain))
        pkt_list.append(newp)
    return pkt_list
