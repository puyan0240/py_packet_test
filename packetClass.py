from scapy.all import *
from ping3 import ping
import socket

class packetClass():
    OK=0
    ERROR_NO_VALUE=1
    ERROR_RANGE=2
    #ERROR_NO_NUMBER=3

    #範囲
    MAX_IP_VER=15
    MAX_IP_IHL=15
    MAX_IP_TOS=127
    MAX_IP_TL=65535
    MAX_IP_ID=65535
    MAX_IP_FLAGS=7
    MAX_IP_FOFFSET=8191
    MAX_IP_TTL=255
    MAX_IP_PROTOCOL=15
    MAX_IP_CHKSUM=65535
    MAX_UDP_PORT=65535
    MAX_UDP_DTL=65535
    MAX_UDP_CHKSUM=65535



    def __init__(self):
        #IP
        self.ip_ver = ""
        self.ip_ihl = ""
        self.ip_tos = ""
        self.ip_tl  = ""
        self.ip_id  = ""
        self.ip_flags = ""
        self.ip_foffset = ""
        self.ip_ttl = ""
        self.ip_protocol = ""
        self.ip_chksum = ""
        self.ip_srcip = ""
        self.ip_dstip = ""
        self.ip_opt = ""
        self.ip_pad = ""
        #UDP
        self.udp_sport = ""
        self.udp_dport = ""
        self.udp_dtl = ""
        self.udp_chksum = ""
        #DATA
        self.data = ""
  
    
    def set_ip_ver(self, ip_ver):
        if ip_ver != "":
            try:
                val = int(ip_ver)
                if val < 0 or val > self.MAX_IP_VER:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_ver = ip_ver
        return self.OK
    
    def get_max_ip_ver(self):
        return self.MAX_IP_VER

    def set_ip_ihl(self, ip_ihl):
        if ip_ihl != "":
            try:
                val = int(ip_ihl)
                if val < 0 or val > self.MAX_IP_IHL:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_ihl = ip_ihl
        return self.OK

    def get_max_ip_ihl(self):
        return self.MAX_IP_IHL

    def set_ip_tos(self, ip_tos):
        if ip_tos != "":
            try:
                val = int(ip_tos)
                if val < 0 or val > self.MAX_IP_TOS:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_tos = ip_tos
        return self.OK

    def get_max_ip_tos(self):
        return self.MAX_IP_TOS

    def set_ip_tl(self, ip_tl):
        if ip_tl != "":
            try:
                val = int(ip_tl)
                if val < 0 or val > self.MAX_IP_TL:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_tl = ip_tl
        return self.OK

    def get_max_ip_tl(self):
        return self.MAX_IP_TL
    
    def set_ip_id(self, ip_id):
        if ip_id != "":
            try:
                val = int(ip_id)
                if val < 0 or val > self.MAX_IP_ID:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_id = ip_id
        return self.OK
    
    def get_max_ip_id(self):
        return self.MAX_IP_ID
    
    def set_ip_flags(self, ip_flags):
        if ip_flags != "":
            try:
                val = int(ip_flags)
                if val < 0 or val > self.MAX_IP_FLAGS:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_flags = ip_flags
        return self.OK
    
    def get_max_ip_flags(self):
        return self.MAX_IP_FLAGS
    
    def set_ip_foffset(self, ip_foffset):
        if ip_foffset != "":
            try:
                val = int(ip_foffset)
                if val < 0 or val > self.MAX_IP_FOFFSET:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_foffset = ip_foffset
        return self.OK
    
    def get_max_ip_foffset(self):
        return self.MAX_IP_FOFFSET

    def set_ip_ttl(self, ip_ttl):
        if ip_ttl != "":
            try:
                val = int(ip_ttl)
                if val < 0 or val > self.MAX_IP_TTL:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_ttl = ip_ttl
        return self.OK
    
    def get_max_ip_ttl(self):
        return self.MAX_IP_TTL

    def set_ip_protocol(self, ip_protocol):
        if ip_protocol != "":
            try:
                val = int(ip_protocol)
                if val < 0 or val > self.MAX_IP_PROTOCOL:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_protocol = ip_protocol
        return self.OK

    def get_max_ip_protocol(self):
        return self.MAX_IP_PROTOCOL

    def set_ip_chksum(self, ip_chksum):
        if ip_chksum != "":
            try:
                val = int(ip_chksum)
                if val < 0 or val > self.MAX_IP_CHKSUM:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_chksum = ip_chksum
        return self.OK

    def get_max_ip_chksum(self):
        return self.MAX_IP_CHKSUM

    def set_ip_srcip(self, ip_srcip):
        return self.OK

    def set_ip_dstip(self, ip_dstip):
        if ip_dstip == "":
            return self.ERROR_NO_VALUE
        #DNS解決する
        try:
            ip_dstip = socket.gethostbyname(ip_dstip) #DNS解決
        except Exception as e:
            #print("dns err"+str(e))
            return self.ERROR_RANGE
        self.ip_dstip = ip_dstip
        return self.OK

    def get_ip_dstip(self):
        return self.ip_dstip

    def set_ip_opt(self, ip_opt):
        if ip_opt != "":
            try:
                val = int(ip_opt)
                if val < 0:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_opt = ip_opt
        return self.OK
    
    def set_ip_pad(self, ip_pad):
        if ip_pad != "":
            try:
                val = int(ip_pad)
                if val < 0:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_pad = ip_pad
        return self.OK
    
    def set_udp_sport(self, udp_sport):
        if udp_sport != "":
            try:
                val = int(udp_sport)
                if val < 0 or val > self.MAX_UDP_PORT:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_sport = udp_sport
        return self.OK

    def get_max_udp_port(self):
        return self.MAX_UDP_PORT

    def set_udp_dport(self, dport):
        if dport == "":
            return self.ERROR_NO_VALUE
        else:
            try:
                val = int(dport)
                if val < 0 or val > self.MAX_UDP_PORT:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_dport = dport
        return self.OK

    def set_udp_dtl(self, udp_dtl):
        if udp_dtl != "":
            try:
                val = int(udp_dtl)
                if val < 0 or val > self.MAX_UDP_DTL:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_dtl = udp_dtl
        return self.OK
    
    def get_max_udp_dtl(self):
        return self.MAX_UDP_DTL

    def set_udp_chksum(self, udp_chksum):
        if udp_chksum != "":
            try:
                val = int(udp_chksum)
                if val < 0 or val > self.MAX_IP_CHKSUM:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_chksum = udp_chksum
        return self.OK
    
    def get_max_udp_chksum(self):
        return self.MAX_UDP_CHKSUM

    def set_data(self, data):
        self.data = data
        return self.OK


    #個別パケット送信
    def send_packet(self):
        pkt_ip  = IP()
        pkt_udp = UDP()
        pkt_raw = Raw()

        #----------------------------------------------------
        #必須パラメータ
        #----------------------------------------------------
        #送信元IPアドレス
        pkt_ip.dst = self.ip_dstip

        #送信元ポート番号
        if self.udp_sport == "":
            val = 12345
        else:
            val = int(self.udp_sport)
        pkt_udp.sport = val

        #送信先ポート番号
        pkt_udp.dport = int(self.udp_dport)


        #----------------------------------------------------
        #カスタムパラメータ(IP)
        #----------------------------------------------------
        #Version
        if self.ip_ver != "":
            pkt_ip.version = int(self.ip_ver)
        #ヘッダ長
        if self.ip_ihl != "":
            pkt_ip.ihl = int(self.ip_ihl)
        #TOS
        if self.ip_tos != "":
            pkt_ip.tos = int(self.ip_tos)
        #全長
        if self.ip_tl != "":
            pkt_ip.len = int(self.ip_tl)
        #識別番号
        if self.ip_id != "":
            pkt_ip.id = int(self.ip_id)
        #フラグ
        if self.ip_flags != "":
            pkt_ip.flags = int(self.ip_flags)
        #フラグメントオフセット
        if self.ip_foffset != "":
            pkt_ip.frag = int(self.ip_foffset)
        #TTL
        if self.ip_ttl != "":
            pkt_ip.ttl = int(self.ip_ttl)
        #プロトコル
        if self.ip_protocol != "":
            pkt_ip.proto = int(self.ip_protocol)
        #ヘッダチェックサム
        if self.ip_chksum != "":
            pkt_ip.chksum = int(self.ip_chksum)
        #オプション
        if self.ip_opt != "":
            pkt_ip.option = int(self.ip_opt)


        #----------------------------------------------------
        #カスタムパラメータ(UDP)
        #----------------------------------------------------
        #データ長
        if self.udp_dtl != "":
            pkt_udp.len = int(self.udp_dtl)
        #チェックサム
        if self.udp_chksum != "":
            pkt_udp.chksum = int(self.udp_chksum)

        #----------------------------------------------------
        #カスタムパラメータ(User DATA)
        #----------------------------------------------------
        #User DATA
        if self.data != "":
            pkt_raw.load = self.data.encode()


        #パケット組み立て
        pkt = pkt_ip/pkt_udp/pkt_raw

        #パケット送信
        try:
            #pkt.show()  #DBG
            send(pkt)   #送信
            return "OK"
        except Exception as e:
            #print("send err:"+str(e))
            return "NG"


    #PING検査
    def ping_test(self):
        #print(self.ip_dstip)

        try:
            #PING(ms単位で)
            ret = ping(self.ip_dstip, unit="ms")
            return str(int(ret))+"ms"
        except Exception as e:
            #print("ping err:"+str(e))
            return "NG"