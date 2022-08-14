from scapy.all import *
from ping3 import ping
import socket
import time

class packetClass():
    OK=0
    ERROR_NO_VALUE=1
    ERROR_RANGE=2
    #ERROR_NO_NUMBER=3

    #最大値テーブル
    max_ip_tbl = {
        "ip_ver":15,
        "ip_ihl":15,
        "ip_tos":255,
        "ip_tl":65535,
        "ip_id":65535,
        "ip_flags":7,
        "ip_foffset":8191,
        "ip_ttl":255,
        "ip_protocol":15,
        "ip_chksum":65535
    }
    max_udp_tbl = {
        "udp_port":65535,
        "udp_dtl":65535,
        "udp_chksum":65535
    }


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
  

    #-------------------------------------------------------
    #Version
    #-------------------------------------------------------
    def set_ip_ver(self, ip_ver):
        if ip_ver != "":
            try:
                val = int(ip_ver)
                if val < 0 or val > self.max_ip_tbl["ip_ver"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_ver = ip_ver
        return self.OK
    
    def clr_ip_ver(self):
        self.ip_ver = ""
    
    def get_max_ip_ver(self):
        return self.max_ip_tbl["ip_ver"]


    #ヘッダ長
    def set_ip_ihl(self, ip_ihl):
        if ip_ihl != "":
            try:
                val = int(ip_ihl)
                if val < 0 or val > self.max_ip_tbl["ip_ihl"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_ihl = ip_ihl
        return self.OK

    def clr_ip_ihl(self):
        self.ip_ihl = ""

    def get_max_ip_ihl(self):
        return self.max_ip_tbl["ip_ihl"]

    #-------------------------------------------------------
    #TOS
    #-------------------------------------------------------
    def set_ip_tos(self, ip_tos):
        if ip_tos != "":
            try:
                val = int(ip_tos)
                if val < 0 or val > self.max_ip_tbl["ip_tos"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_tos = ip_tos
        return self.OK

    def clr_ip_tos(self):
        self.ip_tos = ""

    def get_max_ip_tos(self):
        return self.max_ip_tbl["ip_tos"]

    #-------------------------------------------------------
    #全長
    #-------------------------------------------------------
    def set_ip_tl(self, ip_tl):
        if ip_tl != "":
            try:
                val = int(ip_tl)
                if val < 0 or val > self.max_ip_tbl["ip_tl"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_tl = ip_tl
        return self.OK

    def clr_ip_tl(self):
        self.ip_tl = ""

    def get_max_ip_tl(self):
        return self.max_ip_tbl["ip_tl"]
    
    #-------------------------------------------------------
    #識別番号
    #-------------------------------------------------------
    def set_ip_id(self, ip_id):
        if ip_id != "":
            try:
                val = int(ip_id)
                if val < 0 or val > self.max_ip_tbl["ip_id"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_id = ip_id
        return self.OK
    
    def clr_ip_id(self):
        self.ip_id = ""

    def get_max_ip_id(self):
        return self.max_ip_tbl["ip_id"]
    
    #-------------------------------------------------------
    #フラグ
    #-------------------------------------------------------
    def set_ip_flags(self, ip_flags):
        if ip_flags != "":
            try:
                val = int(ip_flags)
                if val < 0 or val > self.max_ip_tbl["ip_flags"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_flags = ip_flags
        return self.OK
    
    def clr_ip_flags(self):
        self.ip_flags = ""

    def get_max_ip_flags(self):
        return self.max_ip_tbl["ip_flags"]
    
    #-------------------------------------------------------
    #フラグメントオフセット
    #-------------------------------------------------------
    def set_ip_foffset(self, ip_foffset):
        if ip_foffset != "":
            try:
                val = int(ip_foffset)
                if val < 0 or val > self.max_ip_tbl["ip_foffset"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_foffset = ip_foffset
        return self.OK
    
    def clr_ip_foffset(self):
        self.ip_foffset = ""
    
    def get_max_ip_foffset(self):
        return self.max_ip_tbl["ip_foffset"]

    #-------------------------------------------------------
    #TTL
    #-------------------------------------------------------
    def set_ip_ttl(self, ip_ttl):
        if ip_ttl != "":
            try:
                val = int(ip_ttl)
                if val < 0 or val > self.max_ip_tbl["ip_ttl"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_ttl = ip_ttl
        return self.OK

    def clr_ip_ttl(self):
        self.ip_ttl = ""

    def get_max_ip_ttl(self):
        return self.max_ip_tbl["ip_ttl"]

    #-------------------------------------------------------
    #プロトコル
    #-------------------------------------------------------
    def set_ip_protocol(self, ip_protocol):
        if ip_protocol != "":
            try:
                val = int(ip_protocol)
                if val < 0 or val > self.max_ip_tbl["ip_protocol"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_protocol = ip_protocol
        return self.OK

    def clr_ip_protocol(self):
        self.ip_protocol = ""

    def get_max_ip_protocol(self):
        return self.max_ip_tbl["ip_protocol"]

    #-------------------------------------------------------
    #ヘッダチェックサム
    #-------------------------------------------------------
    def set_ip_chksum(self, ip_chksum):
        if ip_chksum != "":
            try:
                val = int(ip_chksum)
                if val < 0 or val > self.max_ip_tbl["ip_chksum"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_chksum = ip_chksum
        return self.OK

    def clr_ip_chksum(self):
        self.ip_chksum = ""

    def get_max_ip_chksum(self):
        return self.max_ip_tbl["ip_chksum"]

    #-------------------------------------------------------
    #送信元IPアドレス
    #-------------------------------------------------------
    def set_ip_srcip(self, ip_srcip):
        return self.OK

    #-------------------------------------------------------
    #送信先IPアドレス
    #-------------------------------------------------------
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

    #-------------------------------------------------------
    #オプション
    #-------------------------------------------------------
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

    def clr_ip_opt(self):
        self.ip_opt = ""

    #-------------------------------------------------------
    #パディング
    #-------------------------------------------------------
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
    
    def clr_ip_pad(self):
        self.ip_pad = ""


    #-------------------------------------------------------
    #送信元ポート番号
    #-------------------------------------------------------
    def set_udp_sport(self, udp_sport):
        if udp_sport != "":
            try:
                val = int(udp_sport)
                #if val < 0 or val > self.MAX_UDP_PORT:
                if val < 0 or val > self.max_udp_tbl["udp_port"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_sport = udp_sport
        return self.OK

    def clr_udp_sport(self):
        self.udp_sport = ""

    def get_max_udp_port(self):
        return self.max_udp_tbl["udp_port"]

    #-------------------------------------------------------
    #送信先ポート番号
    #-------------------------------------------------------
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

    def clr_udp_dport(self):
        self.udp_dport = ""

    #-------------------------------------------------------
    #データ長
    #-------------------------------------------------------
    def set_udp_dtl(self, udp_dtl):
        if udp_dtl != "":
            try:
                val = int(udp_dtl)
                if val < 0 or val > self.max_udp_tbl["udp_dtl"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_dtl = udp_dtl
        return self.OK
    
    def clr_udp_dtl(self):
        self.udp_dtl = ""

    def get_max_udp_dtl(self):
        return self.max_udp_tbl["udp_dtl"]

    #-------------------------------------------------------
    #チェックサム
    #-------------------------------------------------------
    def set_udp_chksum(self, udp_chksum):
        if udp_chksum != "":
            try:
                val = int(udp_chksum)
                if val < 0 or val > self.max_udp_tbl["udp_chksum"]:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_chksum = udp_chksum
        return self.OK
    
    def clr_udp_chksum(self):
        self.udp_chksum = ""

    def get_max_udp_chksum(self):
        return self.max_udp_tbl["udp_chksum"]


    #User DATA
    def set_data(self, data):
        self.data = data
        return self.OK


    ########################################################
    #IPパラメータクリア(IPアドレス以外)一括設定
    ########################################################
    #クリア
    def param_ip_clr(self):
        self.set_ip_ver(4)
        self.clr_ip_ihl()
        self.clr_ip_tos()
        self.clr_ip_tl()
        self.clr_ip_id()
        self.clr_ip_flags()
        self.clr_ip_foffset()
        self.clr_ip_ttl()
        self.clr_ip_protocol()
        self.clr_ip_chksum()
        self.clr_ip_opt()
        self.clr_ip_pad()

    #最大値設定(オプション/パディング除く)
    def param_ip_set_max(self):
        self.set_ip_ver(self.get_max_ip_ver())
        self.set_ip_ihl(self.get_max_ip_ihl())
        self.set_ip_tos(self.get_max_ip_tos())
        self.set_ip_tl(self.get_max_ip_tl())
        self.set_ip_id(self.get_max_ip_id())
        self.set_ip_flags(self.get_max_ip_flags())
        self.set_ip_foffset(self.get_max_ip_foffset())
        self.set_ip_ttl(self.get_max_ip_ttl())
        self.set_ip_protocol(self.get_max_ip_protocol())
        self.set_ip_chksum(self.get_max_ip_chksum())
    
    #最小値設定(オプション/パディング除く)
    def param_ip_set_min(self):
        self.set_ip_ver(0)
        self.set_ip_ihl(0)
        self.set_ip_tos(0)
        self.set_ip_tl(0)
        self.set_ip_id(0)
        self.set_ip_flags(0)
        self.set_ip_foffset(0)
        self.set_ip_ttl(0)
        self.set_ip_protocol(0)
        self.set_ip_chksum(0)


    ########################################################
    #UDPパラメータクリア(ポート番号以外)一括設定
    ########################################################
    #クリア
    def param_udp_clr(self):
        self.clr_udp_dtl()
        self.clr_udp_chksum()
    
    #最大値設定
    def param_udp_set_max(self):
        self.set_udp_dtl(self.get_max_udp_dtl())
        self.set_udp_chksum(self.get_max_udp_chksum())

    #最小値設定
    def param_udp_set_min(self):
        self.set_udp_dtl(self.get_max_udp_dtl())
        self.set_udp_chksum(self.get_max_udp_chksum())


    ########################################################
    #一括設定
    ########################################################
    #クリア
    def param_all_clr(self):
        self.param_ip_clr()
        self.param_udp_clr()

    #最大値設定
    def param_all_set_max(self):
        self.param_all_clr()    #全クリア
        self.param_ip_set_max()
        self.param_udp_set_max()

    #最小値設定
    def param_all_set_min(self):
        self.param_all_clr()    #全クリア
        self.param_ip_set_min()
        self.param_udp_set_min()



    ########################################################
    #テストパケット送信&ping確認
    ########################################################
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
            pkt.show()  #DBG
            send(pkt)   #送信

            #PING検査
            time.sleep(0.01)    #10ms
            return self.ping_test()
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