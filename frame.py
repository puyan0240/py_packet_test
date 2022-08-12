import tkinter
from tkinter import ttk



start_flag = False

#ラジオボタン押下
def radio_top_click():
    print("ラジオボタン押下:"+str(radio_top_text[radio_top_grp.get()]))


#開始/停止ボタン押下
def btn_top_click():
    global start_flag

    if start_flag == False:
        start_flag = True
        btn_top.config(text='停止', bg='RED')
        #入力規制
        input_ctrl(True)
    else:
        start_flag = False
        btn_top.config(text='開始', bg='GREEN')
        #入力規制解除
        input_ctrl(False)


#入力規制関数
def input_ctrl(inhibit):
    if inhibit == True:
        #TOP
        radio_top_auto.config(state=tkinter.DISABLED)
        radio_top_manual.config(state=tkinter.DISABLED)
        text_top_dstip.config(state=tkinter.DISABLED)
        text_top_dport.config(state=tkinter.DISABLED)
        #IP
        text_ip_ver.config(state=tkinter.DISABLED)
        text_ip_ihl.config(state=tkinter.DISABLED)
        text_ip_tos.config(state=tkinter.DISABLED)
        text_ip_tl.config(state=tkinter.DISABLED)
        text_ip_id.config(state=tkinter.DISABLED)
        text_ip_flags.config(state=tkinter.DISABLED)
        text_ip_foffset.config(state=tkinter.DISABLED)
        text_ip_ttl.config(state=tkinter.DISABLED)
        text_ip_protocol.config(state=tkinter.DISABLED)
        text_ip_chksum.config(state=tkinter.DISABLED)
        text_ip_srcip.config(state=tkinter.DISABLED)
        text_ip_dstip.config(state=tkinter.DISABLED)
        text_ip_opt.config(state=tkinter.DISABLED)
        text_ip_pad.config(state=tkinter.DISABLED)
        #UDP
        text_udp_sport.config(state=tkinter.DISABLED)
        text_udp_dport.config(state=tkinter.DISABLED)
        text_udp_dtl.config(state=tkinter.DISABLED)
        text_udp_chksum.config(state=tkinter.DISABLED)
        #DATA
        text_data_data.config(state=tkinter.DISABLED)
        return
    else:
        #TOP
        radio_top_auto.config(state=tkinter.NORMAL)
        radio_top_manual.config(state=tkinter.NORMAL)
        text_top_dstip.config(state=tkinter.NORMAL)
        text_top_dport.config(state=tkinter.NORMAL)
        #IP
        text_ip_ver.config(state=tkinter.NORMAL)
        text_ip_ihl.config(state=tkinter.NORMAL)
        text_ip_tos.config(state=tkinter.NORMAL)
        text_ip_tl.config(state=tkinter.NORMAL)
        text_ip_id.config(state=tkinter.NORMAL)
        text_ip_flags.config(state=tkinter.NORMAL)
        text_ip_foffset.config(state=tkinter.NORMAL)
        text_ip_ttl.config(state=tkinter.NORMAL)
        text_ip_protocol.config(state=tkinter.NORMAL)
        text_ip_chksum.config(state=tkinter.NORMAL)
        text_ip_srcip.config(state=tkinter.NORMAL)
        text_ip_dstip.config(state=tkinter.NORMAL)
        text_ip_opt.config(state=tkinter.NORMAL)
        text_ip_pad.config(state=tkinter.NORMAL)
        #UDP
        text_udp_sport.config(state=tkinter.NORMAL)
        text_udp_dport.config(state=tkinter.NORMAL)
        text_udp_dtl.config(state=tkinter.NORMAL)
        text_udp_chksum.config(state=tkinter.NORMAL)
        #DATA
        text_data_data.config(state=tkinter.NORMAL)
        return




root = tkinter.Tk()
root.title("Packet Test")
root.geometry("700x700")


###########################################################
#Frame (TOP)
###########################################################
frame_top_base = tkinter.Frame(root)
frame_top_base.pack(fill=tkinter.X, pady=(0,20))

#左側1行目
frame_top_left = tkinter.Frame(frame_top_base)
frame_top_left.pack(side=tkinter.LEFT, padx=10)

frame_top1 = tkinter.Frame(frame_top_left)
frame_top1.pack()

label_top_mode = tkinter.Label(frame_top1, text="動作モード: ", font=('System', 12))
label_top_mode.grid(row=0, column=0, sticky=tkinter.W)

radio_top_text = ['auto', 'manual']
radio_top_grp  = tkinter.IntVar()
radio_top_auto = tkinter.Radiobutton(frame_top1, value=0, variable=radio_top_grp, text=radio_top_text[0], font=('System', 12), command=radio_top_click)
radio_top_auto.grid(row=0, column=1, sticky=tkinter.W)
radio_top_manual = tkinter.Radiobutton(frame_top1, value=1, variable=radio_top_grp, text=radio_top_text[1], font=('System', 12), command=radio_top_click)
radio_top_manual.grid(row=0, column=2, sticky=tkinter.W)


#左側2行目
frame_top2 = tkinter.Frame(frame_top_left)
frame_top2.pack()

#送信先IPアドレス
label_top_dstip = tkinter.Label(frame_top2, text="送信先IPアドレス (IPv4):")
label_top_dstip.grid(row=0, column=0, sticky=tkinter.W)
text_top_dstip = tkinter.Entry(frame_top2, width=16)
text_top_dstip.grid(row=0, column=1, sticky=tkinter.W)

#送信先ポート番号
label_top_dport = tkinter.Label(frame_top2, text="送信先ポート番号 (0-65535):")
label_top_dport.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_top_dport = tkinter.Entry(frame_top2, width=6)
text_top_dport.grid(row=0, column=3, sticky=tkinter.W)


#右側
frame_top_right = tkinter.Frame(frame_top_base)
frame_top_right.pack(side=tkinter.RIGHT)

#ボタン
btn_top = tkinter.Button(frame_top_right, text="開始", font=('System', 12), padx=10, bg='GREEN', command=btn_top_click)
btn_top.pack(padx=(10,10))

#境界線
border = ttk.Separator(root, orient="horizontal")
border.pack(fill=tkinter.X)

###########################################################
#Frame (IP)
###########################################################
#IP 1行目--------------------
frame_ip1 = tkinter.Frame(root)
frame_ip1.pack(fill=tkinter.X, padx=10)

#タイトル
title_text = "==================== IP HEADER ===================="
label_ip_title  = tkinter.Label(frame_ip1, text=title_text, font=('System','12','bold'))
label_ip_title.grid(row=0, column=0, columnspan=8, sticky=tkinter.W)

#Version
label_ip_ver = tkinter.Label(frame_ip1, text="version (0-15):")
label_ip_ver.grid(row=1, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_ver = tkinter.Entry(frame_ip1, width=4)
text_ip_ver.insert(tkinter.END, "4")
text_ip_ver.grid(row=1, column=1, sticky=tkinter.W)

#ヘッダ長
label_ip_ihl = tkinter.Label(frame_ip1, text="ヘッダ長 (空白->自動 | 0-15):")
label_ip_ihl.grid(row=1, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_ihl = tkinter.Entry(frame_ip1, width=4)
text_ip_ihl.grid(row=1, column=3, sticky=tkinter.W)

#サービスタイプ
label_ip_tos = tkinter.Label(frame_ip1, text="ToS (空白->自動 | 0-127):")
label_ip_tos.grid(row=1, column=4, sticky=tkinter.W, padx=(5,0))
text_ip_tos = tkinter.Entry(frame_ip1, width=4)
text_ip_tos.grid(row=1, column=5, sticky=tkinter.W)

#全長
label_ip_tl = tkinter.Label(frame_ip1, text="全長 (空白->自動 | 0-65535):")
label_ip_tl.grid(row=1, column=6, sticky=tkinter.W, padx=(5,0))
text_ip_tl = tkinter.Entry(frame_ip1, width=6)
text_ip_tl.grid(row=1, column=7, sticky=tkinter.W)


#IP 2行目--------------------
frame_ip2 = tkinter.Frame(root)
frame_ip2.pack(fill=tkinter.X, padx=10)

#識別番号
label_ip_id = tkinter.Label(frame_ip2, text="識別番号 (空白->自動 | 0-65535):")
label_ip_id.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_id = tkinter.Entry(frame_ip2, width=6)
text_ip_id.grid(row=0, column=1, sticky=tkinter.W)

#フラグ
label_ip_flags = tkinter.Label(frame_ip2, text="フラグ (空白->自動 | 0-7):")
label_ip_flags.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_flags = tkinter.Entry(frame_ip2, width=6)
text_ip_flags.grid(row=0, column=3, sticky=tkinter.W)

#フラグメントオフセット
label_ip_foffset = tkinter.Label(frame_ip2, text="フラグメントオフセット (空白->自動 | 0-8191):")
label_ip_foffset.grid(row=0, column=4, sticky=tkinter.W, padx=(5,0))
text_ip_foffset = tkinter.Entry(frame_ip2, width=6)
text_ip_foffset.grid(row=0, column=5, sticky=tkinter.W)


#IP 3行目--------------------
frame_ip3 = tkinter.Frame(root)
frame_ip3.pack(fill=tkinter.X, padx=10)

#TTL
label_ip_ttl = tkinter.Label(frame_ip3, text="TTL (空白->自動 | 0-255):")
label_ip_ttl.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_ttl = tkinter.Entry(frame_ip3, width=6)
text_ip_ttl.grid(row=0, column=1, sticky=tkinter.W)

#プロトコル
label_ip_protocol = tkinter.Label(frame_ip3, text="プロトコル (空白->自動 | 0-15):")
label_ip_protocol.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_protocol = tkinter.Entry(frame_ip3, width=6)
text_ip_protocol.grid(row=0, column=3, sticky=tkinter.W)

#ヘッダチェックサム
label_ip_chksum = tkinter.Label(frame_ip3, text="ヘッダチェックサム (空白->自動 | 0-65535):")
label_ip_chksum.grid(row=0, column=4, sticky=tkinter.W, padx=(5,0))
text_ip_chksum = tkinter.Entry(frame_ip3, width=6)
text_ip_chksum.grid(row=0, column=5, sticky=tkinter.W)


#IP 4行目--------------------
frame_ip4 = tkinter.Frame(root)
frame_ip4.pack(fill=tkinter.X, padx=10)

#送信元IPアドレス
label_ip_srcip = tkinter.Label(frame_ip4, text="送信元IPアドレス (空白->自動 | IPv4):")
label_ip_srcip.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_srcip = tkinter.Entry(frame_ip4, width=16)
text_ip_srcip.grid(row=0, column=1, sticky=tkinter.W)

#送信先IPアドレス
label_ip_dstip = tkinter.Label(frame_ip4, text="送信先IPアドレス (空白->自動 | IPv4):")
label_ip_dstip.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_dstip = tkinter.Entry(frame_ip4, width=16)
text_ip_dstip.grid(row=0, column=3, sticky=tkinter.W)


#IP 5行目--------------------
frame_ip5 = tkinter.Frame(root)
frame_ip5.pack(fill=tkinter.X, padx=10)

#オプション
label_ip_opt = tkinter.Label(frame_ip5, text="オプション:")
label_ip_opt.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_opt = tkinter.Entry(frame_ip5, width=16)
text_ip_opt.grid(row=0, column=1, sticky=tkinter.W)

#パディング
label_ip_pad = tkinter.Label(frame_ip5, text="パディング:(空白->自動 | 0-)")
label_ip_pad.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_pad = tkinter.Entry(frame_ip5, width=16)
text_ip_pad.grid(row=0, column=3, sticky=tkinter.W)


###########################################################
#Frame (UDP)
###########################################################
#UDP: 1行目--------------------
frame_udp1 = tkinter.Frame(root)
frame_udp1.pack(fill=tkinter.X, padx=10)

#タイトル
title_text = "\n==================== UDP HEADER ===================="
label_udp_title  = tkinter.Label(frame_udp1, text=title_text, font=('System', '12', 'bold'))
label_udp_title.grid(row=0, column=0, columnspan=8, sticky=tkinter.W)

#送信元ポート番号
label_udp_sport = tkinter.Label(frame_udp1, text="送信元ポート番号 (空白->自動 | 0-65535):")
label_udp_sport.grid(row=1, column=0, sticky=tkinter.W, padx=(5,0))
text_udp_sport = tkinter.Entry(frame_udp1, width=6)
text_udp_sport.grid(row=1, column=1, sticky=tkinter.W)

#送信先ポート番号
label_udp_dport = tkinter.Label(frame_udp1, text="送信先ポート番号 (0-65535):")
label_udp_dport.grid(row=1, column=2, sticky=tkinter.W, padx=(5,0))
text_udp_dport = tkinter.Entry(frame_udp1, width=6)
text_udp_dport.grid(row=1, column=3, sticky=tkinter.W)

#UDP: 2行目--------------------
frame_udp2 = tkinter.Frame(root)
frame_udp2.pack(fill=tkinter.X, padx=10)

#データ長
label_udp_dtl = tkinter.Label(frame_udp2, text="データ長 (空白->自動 | 0-65535):")
label_udp_dtl.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_udp_dtl = tkinter.Entry(frame_udp2, width=6)
text_udp_dtl.grid(row=0, column=1, sticky=tkinter.W)

#チェックサム
label_udp_chksum = tkinter.Label(frame_udp2, text="チェックサム (空白->自動 | 0-65535):")
label_udp_chksum.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_udp_chksum = tkinter.Entry(frame_udp2, width=6)
text_udp_chksum.grid(row=0, column=3, sticky=tkinter.W)


###########################################################
#Frame (DATA)
###########################################################
frame_data = tkinter.Frame(root)
frame_data.pack(fill=tkinter.X, padx=10)

#タイトル
title_text = "\n==================== User DATA ===================="
label_data_title  = tkinter.Label(frame_data, text=title_text, font=('System', '12', 'bold'))
label_data_title.grid(row=0, column=0, columnspan=8, sticky=tkinter.W)

#データ
label_data_data = tkinter.Label(frame_data, text="データ")
label_data_data.grid(row=1, column=0, sticky=tkinter.W, padx=(5,0))
text_data_data = tkinter.Entry(frame_data, width=100)
text_data_data.insert(tkinter.END, "TEST")
text_data_data.grid(row=1, column=1, sticky=tkinter.W)




###########################################################
#Frame (STATUS)
###########################################################
frame_status = tkinter.Frame(root, relief=tkinter.SOLID, bd=1)
frame_status.pack(fill=tkinter.X)

root.mainloop()