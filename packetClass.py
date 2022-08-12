class packetClass():
    OK=0
    ERROR_NO_VALUE=1
    ERROR_RANGE=2
    ERROR_NO_NUMBER=3

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
            return -1
        self.ip_dstip = ip_dstip
        return self.OK
    
    def set_udp_dport(self, dport):
        if dport == "":
            return self.ERROR_NO_VALUE
        else:
            try:
                port = int(dport)
                if port < 0 or port > 65535:
                    return self.ERROR_RANGE
            except:
                return self.ERROR_NO_NUMBER
        self.udp_dport = dport
    