from scapy.all import *

class packetClass():
    OK=0
    ERROR_NO_VALUE=1
    ERROR_RANGE=2
    #ERROR_NO_NUMBER=3

    def __init__(self):
        print("init")
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
                if val < 0 or val > 15:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_ver = ip_ver
        return self.OK
    
    def set_ip_ihl(self, ip_ihl):
        if ip_ihl != "":
            try:
                val = int(ip_ihl)
                if val < 0 or val > 15:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_ihl = ip_ihl
        return self.OK
    
    def set_ip_tos(self, ip_tos):
        if ip_tos != "":
            try:
                val = int(ip_tos)
                if val < 0 or val > 127:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_tos = ip_tos
        return self.OK
    
    def set_ip_tl(self, ip_tl):
        if ip_tl != "":
            try:
                val = int(ip_tl)
                if val < 0 or val > 65535:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_tl = ip_tl
        return self.OK
    
    def set_ip_id(self, ip_id):
        if ip_id != "":
            try:
                val = int(ip_id)
                if val < 0 or val > 65535:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_id = ip_id
        return self.OK
    
    def set_ip_flags(self, ip_flags):
        if ip_flags != "":
            try:
                val = int(ip_flags)
                if val < 0 or val > 7:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_flags = ip_flags
        return self.OK
    
    def set_ip_foffset(self, ip_foffset):
        if ip_foffset != "":
            try:
                val = int(ip_foffset)
                if val < 0 or val > 8191:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_foffset = ip_foffset
        return self.OK
    
    def set_ip_ttl(self, ip_ttl):
        if ip_ttl != "":
            try:
                val = int(ip_ttl)
                if val < 0 or val > 255:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_ttl = ip_ttl
        return self.OK
    
    def set_ip_protocol(self, ip_protocol):
        if ip_protocol != "":
            try:
                val = int(ip_protocol)
                if val < 0 or val > 15:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_protocol = ip_protocol
        return self.OK

    def set_ip_chksum(self, ip_chksum):
        if ip_chksum != "":
            try:
                val = int(ip_chksum)
                if val < 0 or val > 65535:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.ip_chksum = ip_chksum
        return self.OK

    def set_ip_srcip(self, ip_srcip):
        return self.OK

    def set_ip_dstip(self, ip_dstip):
        if ip_dstip == "":
            return self.ERROR_NO_VALUE
        self.ip_dstip = ip_dstip
        return self.OK

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
                if val < 0 or val > 65535:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_sport = udp_sport
        return self.OK

    def set_udp_dport(self, dport):
        if dport == "":
            return self.ERROR_NO_VALUE
        else:
            try:
                val = int(dport)
                if val < 0 or val > 65535:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_dport = dport
        return self.OK

    def set_udp_dtl(self, udp_dtl):
        if udp_dtl != "":
            try:
                val = int(udp_dtl)
                if val < 0 or val > 65535:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_dtl = udp_dtl
        return self.OK

    def set_udp_chksum(self, udp_chksum):
        if udp_chksum != "":
            try:
                val = int(udp_chksum)
                if val < 0 or val > 65535:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_RANGE
        self.udp_chksum = udp_chksum
        return self.OK
    
    def set_data(self, data):
        self.data = data
        return self.OK


    #個別パケット送信
    def send_packet(self):
        pkt = IP()/UDP()/Raw()

        #----------------------------------------------------
        #必須パラメータ
        #----------------------------------------------------
        #送信元IPアドレス
        pkt.dst = self.ip_dstip

        #送信元ポート番号
        if self.udp_sport == "":
            val = 12345
        else:
            val = int(self.udp_sport)
        pkt.sport = val

        #送信先ポート番号
        pkt.dport = int(self.udp_dport)


        #----------------------------------------------------
        #カスタムパラメータ(IP)
        #----------------------------------------------------
        #Version
        if self.ip_ver != "":
            pkt.version = int(self.ip_ver)
        #ヘッダ長
        if self.ip_ihl != "":
            pkt.ihl = int(self.ip_ihl)
        #TOS
        if self.ip_tos != "":
            pkt.tos = int(self.ip_tos)
        #全長
        if self.ip_tl != "":
            pkt.len = int(self.ip_tl)
        #識別番号
        if self.ip_id != "":
            pkt.id = int(self.ip_id)
        #フラグ
        if self.ip_flags != "":
            pkt.flags = int(self.ip_flags)
        #フラグメントオフセット
        if self.ip_foffset != "":
            pkt.frag = int(self.ip_foffset)
        #TTL
        if self.ip_ttl != "":
            pkt.ttl = int(self.ip_ttl)
        #プロトコル
        if self.ip_protocol != "":
            pkt.proto = int(self.ip_protocol)
        #ヘッダチェックサム
        if self.ip_chksum != "":
            pkt.chksum = int(self.ip_chksum)
        #オプション
        if self.ip_opt != "":
            pkt.option = int(self.ip_opt)



        #User DATA
        if self.data != "":
            pkt.load = self.data.encode()

        pkt.show()

        #パケット送信
        try:
            send(pkt)
        except Exception as e:
            print(e)

        return