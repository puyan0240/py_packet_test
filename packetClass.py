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
        self.udp_spor = ""
        self.udp_dport = ""
        self.udp_dtl = ""
        self.udp_chksum = ""
        #DATA
        self.data = ""

    def set_ip_dstip(self, ip_dstip):
        if ip_dstip == "":
            return self.ERROR_NO_VALUE
        self.ip_dstip = ip_dstip
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