from cgitb import text
import tkinter
from tkinter import ttk
from tkinter import messagebox
import packetClass

ENTRY_WIDTH=6
ENTRY_WIDTH_IPADDR =16

start_flag = False

#packetClassクラスのインスタンス
pkt = packetClass.packetClass()


#ラジオボタン押下
def radio_top_click():
    #print("ラジオボタン押下:"+str(radio_top_text[radio_top_grp.get()]))
    manual_entry_ctrl() #手動Frame入力規制/解除


#開始/停止ボタン押下
def btn_top_click():
    global start_flag

    if start_flag == False: #停止->開始状態へ

        #結果出力TEXTをクリアする
        result_window_ctrl("clr", "")
        #結果出力TEXTに表示
        result_text = "開始"
        result_window_ctrl("set", result_text)

        #エントリー内容を反映させる(※戻り値はエラー文字列)
        ret = entry_data_input()
        if ret != "OK":
            #結果出力TEXTに表示
            result_text = "中止: ["+ret+"]"
            result_window_ctrl("set", result_text)
            #ポップアップ
            messagebox.showerror("エラー", ret)
            return  #NG

        #送信先IPアドレスとポート番号の入力値を手動Frameにも反映する
        text_ip_dstip.config(state=tkinter.NORMAL)
        text_ip_dstip.insert(tkinter.END, text_top_dstip.get())
        text_ip_dstip.config(state=tkinter.DISABLED)
        text_udp_dport.config(state=tkinter.NORMAL)
        text_udp_dport.insert(tkinter.END, text_top_dport.get())
        text_udp_dport.config(state=tkinter.DISABLED)

        start_flag = True
        btn_top.config(text='停止', bg='RED')
        #入力規制(TOP)
        radio_top_auto.config(state=tkinter.DISABLED)
        radio_top_manual.config(state=tkinter.DISABLED)
        text_top_dstip.config(state=tkinter.DISABLED)
        text_top_dport.config(state=tkinter.DISABLED)

        #個別パケット送信
        if radio_top_text[radio_top_grp.get()] == "manual":
            retval = pkt.send_packet()

            #結果出力TEXTに表示
            result_text = "終了: ["+ret+"]"
            result_window_ctrl("set", result_text)

            btn_top_click() #送信が終了したので停止状態へ戻す

    else:   #開始->停止状態へ
        #手動Frameの送信先IPアドレスとポート番号をクリア
        text_ip_dstip.config(state=tkinter.NORMAL)
        text_ip_dstip.delete(0, tkinter.END)    #Entryクリア
        text_ip_dstip.config(state=tkinter.DISABLED)
        text_udp_dport.config(state=tkinter.NORMAL)
        text_udp_dport.delete(0, tkinter.END)   #Entryクリア
        text_udp_dport.config(state=tkinter.DISABLED)

        start_flag = False
        btn_top.config(text='開始', bg='GREEN')
        #入力規制解除(TOP)
        radio_top_auto.config(state=tkinter.NORMAL)
        radio_top_manual.config(state=tkinter.NORMAL)
        text_top_dstip.config(state=tkinter.NORMAL)
        text_top_dport.config(state=tkinter.NORMAL)

    manual_entry_ctrl() #手動Frame入力規制/解除


#エントリー内容を反映させる関数(※戻り値はエラー文字列)
def entry_data_input():
    ###########################################################
    #Frame (TOP)
    ###########################################################
    #送信先IPアドレス
    retval = pkt.set_ip_dstip(text_top_dstip.get())
    if retval == pkt.ERROR_NO_VALUE:
        return "送信先IPアドレスを入力してください"
    elif retval == pkt.ERROR_RANGE:
        return "送信先IPアドレスが不正です(DNS解決できません)。"

    #送信先ポート番号の入力確認
    ret = pkt.set_udp_dport(text_top_dport.get())
    if ret == pkt.ERROR_NO_VALUE:
        return "送信先ポート番号を入力してください"
    elif ret == pkt.ERROR_RANGE:
        return "送信先ポート番号の範囲が不正です(0-65535)"

    if radio_top_text[radio_top_grp.get()] == "manual":
        ###########################################################
        #Frame (IP)
        ###########################################################
        #Version
        if pkt.set_ip_ver(text_ip_ver.get()) == pkt.ERROR_RANGE:
            return "versionの範囲が不正です(0-15)"
        #ヘッダ長
        if pkt.set_ip_ihl(text_ip_ihl.get()) == pkt.ERROR_RANGE:
            return "ヘッダ長の範囲が不正です(0-15)"
        #TOS
        if pkt.set_ip_tos(text_ip_tos.get()) == pkt.ERROR_RANGE:
            return "TOSの範囲が不正です(0-127)"
        #全長
        if pkt.set_ip_tl(text_ip_tl.get()) == pkt.ERROR_RANGE:
            return "全長の範囲が不正です(0-65535)"
        #識別番号
        if pkt.set_ip_id(text_ip_id.get()) == pkt.ERROR_RANGE:
            return "識別番号の範囲が不正です(0-65535)"
        #フラグ
        if pkt.set_ip_flags(text_ip_flags.get()) == pkt.ERROR_RANGE:
            return "フラグの範囲が不正です(0-7)"
        #フラグメントオフセット
        if pkt.set_ip_foffset(text_ip_foffset.get()) == pkt.ERROR_RANGE:
            return "フラグメントオフセットの範囲が不正です(0-8191)"
        #TTL
        if pkt.set_ip_ttl(text_ip_ttl.get()) == pkt.ERROR_RANGE:
            return "TTLの範囲が不正です(0-255)"
        #プロトコル
        if pkt.set_ip_protocol(text_ip_protocol.get()) == pkt.ERROR_RANGE:
            return "プロトコルの範囲が不正です(0-15)"
        #ヘッダチェックサム
        if pkt.set_ip_chksum(text_ip_chksum.get()) == pkt.ERROR_RANGE:
            return "ヘッダチェックサムの範囲が不正です(0-65535)"
        #送信元IPアドレス
        if pkt.set_ip_srcip(text_ip_srcip.get()) == pkt.ERROR_RANGE:
            return "送信元IPアドレスの範囲が不正です(0-XXXXX)"
        #オプション
        if pkt.set_ip_opt(text_ip_opt.get()) == pkt.ERROR_RANGE:
            return "オプションの範囲が不正です(0-)"
        #パディング
        if pkt.set_ip_pad(text_ip_pad.get()) == pkt.ERROR_RANGE:
            return "パディングの範囲が不正です(0-)"

        ###########################################################
        #Frame (UDP)
        ###########################################################
        #送信元ポート番号
        if pkt.set_udp_sport(text_udp_sport.get()) == pkt.ERROR_RANGE:
            return "送信元ポート番号の範囲が不正です(0-65535)"
        #データ長
        if pkt.set_udp_dtl(text_udp_dtl.get()) == pkt.ERROR_RANGE:
            return "データ長の範囲が不正です(0-65535)"
        #チェックサム
        if pkt.set_udp_chksum(text_udp_chksum.get()) == pkt.ERROR_RANGE:
            return "チェックサムの範囲が不正です(0-65535)"

        ###########################################################
        #Frame (User DATA)
        ###########################################################
        pkt.set_data(text_data_data.get())


    return "OK"

#手動Frame入力規制/解除関数
def manual_entry_ctrl():
    if radio_top_text[radio_top_grp.get()] == 'auto' or start_flag == True:
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
        #text_ip_dstip.config(state=tkinter.NORMAL)
        text_ip_opt.config(state=tkinter.NORMAL)
        text_ip_pad.config(state=tkinter.NORMAL)
        #UDP
        text_udp_sport.config(state=tkinter.NORMAL)
        #text_udp_dport.config(state=tkinter.NORMAL)
        text_udp_dtl.config(state=tkinter.NORMAL)
        text_udp_chksum.config(state=tkinter.NORMAL)
        #DATA
        text_data_data.config(state=tkinter.NORMAL)
        return


#結果出力TEXTの表示制御
def result_window_ctrl(cmd, msg):
    text_result.config(state=tkinter.NORMAL)    #書き込み許可

    if cmd == "clr":
        text_result.delete("1.0", tkinter.END)  #表示クリア
    elif cmd == "set":
        text_result.insert(tkinter.END, msg+"\n")    #追加書き込み(改行コード付き)

    text_result.config(state=tkinter.DISABLED)  #書き込み禁止



root = tkinter.Tk()
root.title("Packet Test")
root.geometry("600x700")


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
text_top_dstip = tkinter.Entry(frame_top2, width=ENTRY_WIDTH_IPADDR)
text_top_dstip.grid(row=0, column=1, sticky=tkinter.W)

#送信先ポート番号
label_top_dport = tkinter.Label(frame_top2, text="送信先ポート番号 (0-65535):")
label_top_dport.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_top_dport = tkinter.Entry(frame_top2, width=ENTRY_WIDTH)
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
text_ip_ver = tkinter.Entry(frame_ip1, width=ENTRY_WIDTH)
text_ip_ver.insert(tkinter.END, "4")
text_ip_ver.grid(row=1, column=1, sticky=tkinter.W)

#ヘッダ長
label_ip_ihl = tkinter.Label(frame_ip1, text="ヘッダ長 (0-15):")
label_ip_ihl.grid(row=1, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_ihl = tkinter.Entry(frame_ip1, width=ENTRY_WIDTH)
text_ip_ihl.grid(row=1, column=3, sticky=tkinter.W)

#サービスタイプ
label_ip_tos = tkinter.Label(frame_ip1, text="ToS (0-127):")
label_ip_tos.grid(row=1, column=4, sticky=tkinter.W, padx=(5,0))
text_ip_tos = tkinter.Entry(frame_ip1, width=ENTRY_WIDTH)
text_ip_tos.grid(row=1, column=5, sticky=tkinter.W)

#全長
label_ip_tl = tkinter.Label(frame_ip1, text="全長 (0-65535):")
label_ip_tl.grid(row=1, column=6, sticky=tkinter.W, padx=(5,0))
text_ip_tl = tkinter.Entry(frame_ip1, width=ENTRY_WIDTH)
text_ip_tl.grid(row=1, column=7, sticky=tkinter.W)


#IP 2行目--------------------
frame_ip2 = tkinter.Frame(root)
frame_ip2.pack(fill=tkinter.X, padx=10)

#識別番号
label_ip_id = tkinter.Label(frame_ip2, text="識別番号 (0-65535):")
label_ip_id.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_id = tkinter.Entry(frame_ip2, width=ENTRY_WIDTH)
text_ip_id.grid(row=0, column=1, sticky=tkinter.W)

#フラグ
label_ip_flags = tkinter.Label(frame_ip2, text="フラグ (0-7):")
label_ip_flags.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_flags = tkinter.Entry(frame_ip2, width=ENTRY_WIDTH)
text_ip_flags.grid(row=0, column=3, sticky=tkinter.W)

#フラグメントオフセット
label_ip_foffset = tkinter.Label(frame_ip2, text="フラグメントオフセット (0-8191):")
label_ip_foffset.grid(row=0, column=4, sticky=tkinter.W, padx=(5,0))
text_ip_foffset = tkinter.Entry(frame_ip2, width=ENTRY_WIDTH)
text_ip_foffset.grid(row=0, column=5, sticky=tkinter.W)


#IP 3行目--------------------
frame_ip3 = tkinter.Frame(root)
frame_ip3.pack(fill=tkinter.X, padx=10)

#TTL
label_ip_ttl = tkinter.Label(frame_ip3, text="TTL (0-255):")
label_ip_ttl.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_ttl = tkinter.Entry(frame_ip3, width=ENTRY_WIDTH)
text_ip_ttl.grid(row=0, column=1, sticky=tkinter.W)

#プロトコル
label_ip_protocol = tkinter.Label(frame_ip3, text="プロトコル (0-15):")
label_ip_protocol.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_protocol = tkinter.Entry(frame_ip3, width=ENTRY_WIDTH)
text_ip_protocol.grid(row=0, column=3, sticky=tkinter.W)

#ヘッダチェックサム
label_ip_chksum = tkinter.Label(frame_ip3, text="ヘッダチェックサム (0-65535):")
label_ip_chksum.grid(row=0, column=4, sticky=tkinter.W, padx=(5,0))
text_ip_chksum = tkinter.Entry(frame_ip3, width=ENTRY_WIDTH)
text_ip_chksum.grid(row=0, column=5, sticky=tkinter.W)


#IP 4行目--------------------
frame_ip4 = tkinter.Frame(root)
frame_ip4.pack(fill=tkinter.X, padx=10)

#送信元IPアドレス
label_ip_srcip = tkinter.Label(frame_ip4, text="送信元IPアドレス (IPv4):")
label_ip_srcip.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_srcip = tkinter.Entry(frame_ip4, width=ENTRY_WIDTH_IPADDR)
text_ip_srcip.grid(row=0, column=1, sticky=tkinter.W)

#送信先IPアドレス
label_ip_dstip = tkinter.Label(frame_ip4, text="送信先IPアドレス (IPv4):")
label_ip_dstip.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_dstip = tkinter.Entry(frame_ip4, width=ENTRY_WIDTH_IPADDR, state=tkinter.DISABLED)
text_ip_dstip.grid(row=0, column=3, sticky=tkinter.W)


#IP 5行目--------------------
frame_ip5 = tkinter.Frame(root)
frame_ip5.pack(fill=tkinter.X, padx=10)

#オプション
label_ip_opt = tkinter.Label(frame_ip5, text="オプション:")
label_ip_opt.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_opt = tkinter.Entry(frame_ip5, width=ENTRY_WIDTH_IPADDR)
text_ip_opt.grid(row=0, column=1, sticky=tkinter.W)

#パディング
label_ip_pad = tkinter.Label(frame_ip5, text="パディング:(0-)")
label_ip_pad.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_pad = tkinter.Entry(frame_ip5, width=ENTRY_WIDTH_IPADDR)
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
label_udp_sport = tkinter.Label(frame_udp1, text="送信元ポート番号 (0-65535):")
label_udp_sport.grid(row=1, column=0, sticky=tkinter.W, padx=(5,0))
text_udp_sport = tkinter.Entry(frame_udp1, width=ENTRY_WIDTH)
text_udp_sport.insert(tkinter.END, "12345")
text_udp_sport.grid(row=1, column=1, sticky=tkinter.W)

#送信先ポート番号
label_udp_dport = tkinter.Label(frame_udp1, text="送信先ポート番号 (0-65535):")
label_udp_dport.grid(row=1, column=2, sticky=tkinter.W, padx=(5,0))
text_udp_dport = tkinter.Entry(frame_udp1, width=ENTRY_WIDTH, state=tkinter.DISABLED)
text_udp_dport.grid(row=1, column=3, sticky=tkinter.W)

#UDP: 2行目--------------------
frame_udp2 = tkinter.Frame(root)
frame_udp2.pack(fill=tkinter.X, padx=10)

#データ長
label_udp_dtl = tkinter.Label(frame_udp2, text="データ長 (0-65535):")
label_udp_dtl.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_udp_dtl = tkinter.Entry(frame_udp2, width=ENTRY_WIDTH)
text_udp_dtl.grid(row=0, column=1, sticky=tkinter.W)

#チェックサム
label_udp_chksum = tkinter.Label(frame_udp2, text="チェックサム (0-65535):")
label_udp_chksum.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_udp_chksum = tkinter.Entry(frame_udp2, width=ENTRY_WIDTH)
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
text_data_data = tkinter.Entry(frame_data, width=80)
text_data_data.insert(tkinter.END, "TEST")
text_data_data.grid(row=1, column=1, sticky=tkinter.W)




###########################################################
#Frame (RESULT)
###########################################################
frame_result = tkinter.Frame(root)
frame_result.pack(fill=tkinter.X, pady=(60,10))

#結果出力用TEXT
text_result = tkinter.Text(frame_result,height=20, bg="WHITE", relief=tkinter.SOLID, bd=1)
text_result.config(state=tkinter.DISABLED)  #書き込み禁止
text_result.pack(side=tkinter.LEFT, padx=20)


manual_entry_ctrl() #手動Frame入力規制/解除

root.mainloop()