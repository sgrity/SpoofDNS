#!/usr/bin/python3
# -*- coding: utf-8 -*-

from scapy.all import *
import generate_spoof_dns


def start_send_spoof_pkt(src_ip, dst_ip, query_type, packet_number, send_pkt_speed=999999,
                         domain='test.com', ttl_length=128, DNS_RD=1, dns_port=53):

    # 发送所有的测试用数据包
    print('sending packets...')
    send_pkts(src_ip, dst_ip, query_type, packet_number, send_pkt_speed,
              DNS_RD, ttl_length, dns_port, domain)
    print('sending packets finish...')

    return


def send_pkts(src_ip, dst_ip, query_type, packet_number, send_pkt_speed, DNS_RD, ttl_length, dns_port, domain):
    pkts = generate_spoof_dns.generate_pkts(
        src_ip, dst_ip, query_type, packet_number, DNS_RD, ttl_length, dns_port, domain)
    
    sendpfast(pkts, mbps=send_pkt_speed, file_cache=True)

    return
