# DNS 放大攻击工具

**功能：** 

向 DNS 服务器发送伪造源 IP 的请求包，达到放大攻击的效果。（事实上一般路由器回自动修正源 IP ，导致伪造失败，但在某些情况下是有意义的）

**程序结构：**

`generate_spoof_dns.py`构造伪造的请求数据包

`send_pkt.py`发送伪造的数据包

`main.py`设置攻击目标和参数

**使用方法：**

设置`main.py`中的参数，然后运行`main.py`

**要求：**

Python 3.7 以上版本

[scapy](https://scapy.net/) 2.4 以上版本

[tcpreplay](http://tcpreplay.appneta.com/wiki/installation.html#installation)