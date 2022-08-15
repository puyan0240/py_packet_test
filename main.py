from cgitb import text
import tkinter
from tkinter import ttk
from tkinter import messagebox
from packetClass import *
import time
from common import *

ENTRY_WIDTH=6
ENTRY_WIDTH_IPADDR =16
MAX_PKT_RANDOM =10

start_flag = False

#packetClassクラスのインスタンス
pkt = packetClass()



############################################################
#テストパケット送信メイン関数
############################################################
def send_packet_main():
    #テストパケット送信&ping確認
    ret = pkt.send_packet()
    if ret == "NG":
        #結果出力TEXTに表示
        result_window_ctrl("set", "異常: 応答なし")
    else:    
        #結果出力TEXTに表示
        result_window_ctrl("set", "成功: 応答時間 ["+ret+"]")


############################################################
#テストパケット自動送信関数
############################################################
def send_packet_auto():
    #結果出力TEXTに表示
    result_window_ctrl("set", "全パラメータを最小値でテストパケットを送信...")
    #全パラメータ最大値設定
    pkt.param_all_set_min()
    #テストパケット送信メイン関数
    send_packet_main()

    #結果出力TEXTに表示
    result_window_ctrl("set", "全パラメータを最大値でテストパケットを送信...")
    #全パラメータ最大値設定
    pkt.param_all_set_max()
    #テストパケット送信メイン関数
    send_packet_main()

    #-------------------------------------------------------
    #IPヘッダのパラメータ検査
    #-------------------------------------------------------
    #結果出力TEXTに表示
    result_window_ctrl("set", "IPヘッダのパラメータ検査...")
    count = 0
    err_flag = False

    for key in pkt.max_ip_tbl:
        count += 1
        #パラメータ全クリア
        pkt.param_all_clr()
        #最大値取得
        max = pkt.max_ip_tbl[key]
        #print(key+" max:"+str(max))
        #呼び出す関数名を作成
        func = "pkt.set_"+key

        if key == "ip_ver" or key == "ip_flags" or key == "ip_protocol":    #全て検査
            #結果出力TEXTに表示
            resutl_text = " "+ str(count) + "/"+ str(len(pkt.max_ip_tbl)) + "項目: "
            if key == 'ip_ver':
                param_name = "Version"
                resutl_text += param_name
            elif key == "ip_flags":
                param_name = "フラグ"
                resutl_text += param_name
            elif key == "ip_protocol":
                param_name = "プロトコル"
                resutl_text += param_name
            else:
                resutl_text += "Unkonwn"
            resutl_text += " 全範囲検査"
            result_window_ctrl("set", resutl_text)

            for val in range(max+1):
                #関数名で定義した関数を実行
                eval(func)(str(val))

                #テストパケット送信&ping確認
                ret = pkt.send_packet()
                if ret == "NG":
                    err_flag = True
                    break

        else:   #ランダムで抜き取り検査
            #結果出力TEXTに表示
            resutl_text = " "+ str(count) + "/"+ str(len(pkt.max_ip_tbl)) + "項目: "
            if key == 'ip_ihl':
                param_name = "ヘッダ長"
                resutl_text += param_name
            elif key == "ip_tos":
                param_name = "TOS"
                resutl_text += param_name
            elif key == "ip_tl":
                param_name = "全長"
                resutl_text += param_name
            elif key == "ip_id":
                param_name = "識別番号"
                resutl_text += param_name
            elif key == "ip_foffset":
                param_name = "フラグメントオフセット"
                resutl_text += param_name
            elif key == "ip_ttl":
                param_name = "TTL"
                resutl_text += param_name
            elif key == "ip_chksum":
                param_name = "ヘッダチェックサム"
                resutl_text += param_name
            else:
                resutl_text += "Unkonwn"
            resutl_text += " ランダム検査("+ str(MAX_PKT_RANDOM)+"種類)"
            result_window_ctrl("set", resutl_text)

            #ランダムリスト作成
            random_list = random_ints_nodup(0, max, MAX_PKT_RANDOM)

            for val in random_list:
                #関数名で定義した関数を実行
                eval(func)(str(val))
                #テストパケット送信&ping確認
                ret = pkt.send_packet()
                if ret == "NG":
                    err_flag = True
                    break

        #結果出力TEXTに表示
        if err_flag == False:
            result_window_ctrl("set", "  OK")
        else:
            result_window_ctrl("set", "  #################### エラー検出 ####################")
            result_window_ctrl("set", "    "+param_name+":"+str(val))
            return "NG"

    #-------------------------------------------------------
    #UDPヘッダのパラメータ検査
    #-------------------------------------------------------
    #結果出力TEXTに表示
    result_window_ctrl("set", "UDPヘッダのパラメータ検査...")
    count = 0
    err_flag = False

    for key in pkt.max_udp_tbl:
        #パラメータ全クリア
        pkt.param_all_clr()
        #最大値取得
        max = pkt.max_udp_tbl[key]
        #print(key+" max:"+str(max))
        #呼び出す関数名を作成
        func = "pkt.set_"+key

        #ランダムで抜き取り検査
        if key != "udp_port":
            count += 1
            #結果出力TEXTに表示
            resutl_text = " "+ str(count) + "/"+ str(len(pkt.max_udp_tbl) -1) + "項目: "    #-1はudp_port分
            if key == 'udp_dtl':
                param_name = "データ長"
                resutl_text += param_name
            elif key == "udp_chksum":
                param_name = "チェックサム"
                resutl_text += param_name
            else:
                resutl_text += "Unkonwn"
            resutl_text += " ランダム検査("+ str(MAX_PKT_RANDOM)+"種類)"
            result_window_ctrl("set", resutl_text)

            #ランダムリスト作成
            random_list = random_ints_nodup(0, max, MAX_PKT_RANDOM)

            for val in random_list:
                #関数名で定義した関数を実行
                eval(func)(str(val))
                #テストパケット送信&ping確認
                ret = pkt.send_packet()
                if ret == "NG":
                    err_flag = True
                    break

            #結果出力TEXTに表示
            if err_flag == False:
                result_window_ctrl("set", "  OK")
            else:
                result_window_ctrl("set", "  #################### エラー検出 ####################")
                result_window_ctrl("set", "    "+param_name+":"+str(val))
                return "NG"

    #-------------------------------------------------------
    #UDPヘッダのパラメータ検査
    #-------------------------------------------------------
    #結果出力TEXTに表示
    result_window_ctrl("set", "User DATAを最小値でテストパケットを送信...")
    #パラメータ全クリア
    pkt.param_all_clr()
    #最小のランダム文字列
    pkt.set_user_data(random_str(0))
    #テストパケット送信メイン関数
    send_packet_main()

    #結果出力TEXTに表示
    result_window_ctrl("set", "User DATAを最大値でテストパケットを送信...")
    #パラメータ全クリア
    pkt.param_all_clr()
    #最大のランダム文字列
    pkt.set_user_data(random_str(pkt.get_max_user_data()))
    #テストパケット送信メイン関数
    send_packet_main()


    #結果出力TEXTに表示
    result_window_ctrl("set", "完了")
    return "OK"


############################################################
#ラジオボタン押下
############################################################
def radio_top_click():
    #print("ラジオボタン押下:"+str(radio_top_text[radio_top_grp.get()]))
    manual_entry_ctrl() #手動Frame入力規制/解除


############################################################
#開始/停止ボタン押下
############################################################
def btn_top_click():
    global start_flag

    if start_flag == False: #停止->開始状態へ

        #結果出力TEXTをクリアする
        result_window_ctrl("clr", "")
        #結果出力TEXTに表示
        result_window_ctrl("set", "開始")

        #エントリー内容を反映させる(※戻り値はエラー文字列)
        ret = entry_data_input()
        if ret == "OK":
            #結果出力TEXTに表示
            result_text = "送信先IPアドレス: "+pkt.get_ip_dstip()
            result_window_ctrl("set", result_text)
        else:
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


        if radio_top_text[radio_top_grp.get()] == "manual":
            #結果出力TEXTに表示
            result_window_ctrl("set", "テストパケット送信...")
            #テストパケット送信メイン関数
            send_packet_main()
        else:
            #テストパケット自動送信関数
            send_packet_auto()

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


############################################################
#エントリー内容を反映させる関数(※戻り値はエラー文字列)
############################################################
def entry_data_input():

    #-------------------------------------------------------
    #Frame (TOP)
    #-------------------------------------------------------
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
        return "送信先ポート番号の範囲が不正です(0-"+str(pkt.get_max_udp_port())+")"

    if radio_top_text[radio_top_grp.get()] == "manual":
        #---------------------------------------------------
        #Frame (IP)
        #---------------------------------------------------
        #Version
        if pkt.set_ip_ver(text_ip_ver.get()) == pkt.ERROR_RANGE:
            return "versionの範囲が不正です(0-"+str(pkt.get_max_ip_ver())+")"
        #ヘッダ長
        if pkt.set_ip_ihl(text_ip_ihl.get()) == pkt.ERROR_RANGE:
            return "ヘッダ長の範囲が不正です(0-"+str(pkt.get_max_ip_ihl())+")"
        #TOS
        if pkt.set_ip_tos(text_ip_tos.get()) == pkt.ERROR_RANGE:
            return "TOSの範囲が不正です(0-"+str(pkt.get_max_ip_tos())+")"
        #全長
        if pkt.set_ip_tl(text_ip_tl.get()) == pkt.ERROR_RANGE:
            return "全長の範囲が不正です(0-"+str(pkt.get_max_ip_tl())+")"
        #識別番号
        if pkt.set_ip_id(text_ip_id.get()) == pkt.ERROR_RANGE:
            return "識別番号の範囲が不正です(0-"+str(pkt.get_max_ip_id())+")"
        #フラグ
        if pkt.set_ip_flags(text_ip_flags.get()) == pkt.ERROR_RANGE:
            return "フラグの範囲が不正です(0-"+str(pkt.get_max_ip_flags())+")"
        #フラグメントオフセット
        if pkt.set_ip_foffset(text_ip_foffset.get()) == pkt.ERROR_RANGE:
            return "フラグメントオフセットの範囲が不正です(0-"+str(pkt.get_max_ip_foffset())+")"
        #TTL
        if pkt.set_ip_ttl(text_ip_ttl.get()) == pkt.ERROR_RANGE:
            return "TTLの範囲が不正です(0-"+str(pkt.get_max_ip_ttl())+")"
        #プロトコル
        if pkt.set_ip_protocol(text_ip_protocol.get()) == pkt.ERROR_RANGE:
            return "プロトコルの範囲が不正です(0-"+str(pkt.get_max_ip_protocol())+")"
        #ヘッダチェックサム
        if pkt.set_ip_chksum(text_ip_chksum.get()) == pkt.ERROR_RANGE:
            return "ヘッダチェックサムの範囲が不正です(0-"+str(pkt.get_max_ip_chksum())+")"
        #送信元IPアドレス
        if pkt.set_ip_srcip(text_ip_srcip.get()) == pkt.ERROR_RANGE:
            return "送信元IPアドレスの範囲が不正です(0-XXXXX)"
        #オプション
        if pkt.set_ip_opt(text_ip_opt.get()) == pkt.ERROR_RANGE:
            return "オプションの範囲が不正です(0-)"
        #パディング
        if pkt.set_ip_pad(text_ip_pad.get()) == pkt.ERROR_RANGE:
            return "パディングの範囲が不正です(0-)"

        #---------------------------------------------------
        #Frame (UDP)
        #---------------------------------------------------
        #送信元ポート番号
        if pkt.set_udp_sport(text_udp_sport.get()) == pkt.ERROR_RANGE:
            return "送信元ポート番号の範囲が不正です(0-"+str(pkt.get_max_udp_port())+")"
        #データ長
        if pkt.set_udp_dtl(text_udp_dtl.get()) == pkt.ERROR_RANGE:
            return "データ長の範囲が不正です(0-"+str(pkt.get_max_udp_dtl())+")"
        #チェックサム
        if pkt.set_udp_chksum(text_udp_chksum.get()) == pkt.ERROR_RANGE:
            return "チェックサムの範囲が不正です(0-"+str(pkt.get_max_udp_chksum())+")"

        #---------------------------------------------------
        #Frame (User DATA)
        #---------------------------------------------------
        pkt.set_user_data(text_user_data.get())

    return "OK"


############################################################
#手動Frame入力規制/解除関数
############################################################
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
        #User DATA
        text_user_data.config(state=tkinter.DISABLED)
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
        #User DATA
        text_user_data.config(state=tkinter.NORMAL)
        return


############################################################
#結果出力TEXTの表示制御
############################################################
def result_window_ctrl(cmd, msg):
    text_result.config(state=tkinter.NORMAL)    #書き込み許可

    if cmd == "clr":
        text_result.delete("1.0", tkinter.END)  #表示クリア
    elif cmd == "set":
        text_result.insert(tkinter.END, msg+"\n")    #追加書き込み(改行コード付き)
        text_result.see(tkinter.END)            #最終行を表示するため自動スクロール
    text_result.update()    #TEXT更新

    text_result.config(state=tkinter.DISABLED)  #書き込み禁止



root = tkinter.Tk()
root.title("Packet Test")
root.geometry("600x700")


#-----------------------------------------------------------
#Frame (TOP)
#-----------------------------------------------------------
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
label_text = "送信先ポート番号 (0-"+str(pkt.get_max_udp_port())+"):"
label_top_dport = tkinter.Label(frame_top2, text=label_text)
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

#-----------------------------------------------------------
#Frame (IP)
#-----------------------------------------------------------
#IP 1行目--------------------
frame_ip1 = tkinter.Frame(root)
frame_ip1.pack(fill=tkinter.X, padx=10)

#タイトル
title_text = "==================== IP HEADER ===================="
label_ip_title  = tkinter.Label(frame_ip1, text=title_text, font=('System','12','bold'))
label_ip_title.grid(row=0, column=0, columnspan=8, sticky=tkinter.W)

#Version
label_text = "version (0-"+str(pkt.get_max_ip_ver())+"):"
label_ip_ver = tkinter.Label(frame_ip1, text=label_text)
label_ip_ver.grid(row=1, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_ver = tkinter.Entry(frame_ip1, width=ENTRY_WIDTH)
text_ip_ver.insert(tkinter.END, "4")
text_ip_ver.grid(row=1, column=1, sticky=tkinter.W)

#ヘッダ長
label_text = "ヘッダ長 (0-"+str(pkt.get_max_ip_ihl())+"):"
label_ip_ihl = tkinter.Label(frame_ip1, text=label_text)
label_ip_ihl.grid(row=1, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_ihl = tkinter.Entry(frame_ip1, width=ENTRY_WIDTH)
text_ip_ihl.grid(row=1, column=3, sticky=tkinter.W)

#サービスタイプ
label_text = "ToS (0-"+str(pkt.get_max_ip_tos())+"):"
label_ip_tos = tkinter.Label(frame_ip1, text=label_text)
label_ip_tos.grid(row=1, column=4, sticky=tkinter.W, padx=(5,0))
text_ip_tos = tkinter.Entry(frame_ip1, width=ENTRY_WIDTH)
text_ip_tos.grid(row=1, column=5, sticky=tkinter.W)

#全長
label_text = "全長 (0-"+str(pkt.get_max_ip_tl())+"):"
label_ip_tl = tkinter.Label(frame_ip1, text=label_text)
label_ip_tl.grid(row=1, column=6, sticky=tkinter.W, padx=(5,0))
text_ip_tl = tkinter.Entry(frame_ip1, width=ENTRY_WIDTH)
text_ip_tl.grid(row=1, column=7, sticky=tkinter.W)


#IP 2行目--------------------
frame_ip2 = tkinter.Frame(root)
frame_ip2.pack(fill=tkinter.X, padx=10)

#識別番号
label_text = "識別番号 (0-"+str(pkt.get_max_ip_id())+"):"
label_ip_id = tkinter.Label(frame_ip2, text=label_text)
label_ip_id.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_id = tkinter.Entry(frame_ip2, width=ENTRY_WIDTH)
text_ip_id.grid(row=0, column=1, sticky=tkinter.W)

#フラグ
label_text = "フラグ (0-"+str(pkt.get_max_ip_flags())+"):"
label_ip_flags = tkinter.Label(frame_ip2, text=label_text)
label_ip_flags.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_flags = tkinter.Entry(frame_ip2, width=ENTRY_WIDTH)
text_ip_flags.grid(row=0, column=3, sticky=tkinter.W)

#フラグメントオフセット
label_text = "フラグメントオフセット (0-"+str(pkt.get_max_ip_foffset())+"):"
label_ip_foffset = tkinter.Label(frame_ip2, text=label_text)
label_ip_foffset.grid(row=0, column=4, sticky=tkinter.W, padx=(5,0))
text_ip_foffset = tkinter.Entry(frame_ip2, width=ENTRY_WIDTH)
text_ip_foffset.grid(row=0, column=5, sticky=tkinter.W)


#IP 3行目--------------------
frame_ip3 = tkinter.Frame(root)
frame_ip3.pack(fill=tkinter.X, padx=10)

#TTL
label_text = "TTL (0-"+str(pkt.get_max_ip_ttl())+"):"
label_ip_ttl = tkinter.Label(frame_ip3, text=label_text)
label_ip_ttl.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_ip_ttl = tkinter.Entry(frame_ip3, width=ENTRY_WIDTH)
text_ip_ttl.grid(row=0, column=1, sticky=tkinter.W)

#プロトコル
label_text = "プロトコル (0-"+str(pkt.get_max_ip_protocol())+"):"
label_ip_protocol = tkinter.Label(frame_ip3, text=label_text)
label_ip_protocol.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_ip_protocol = tkinter.Entry(frame_ip3, width=ENTRY_WIDTH)
text_ip_protocol.grid(row=0, column=3, sticky=tkinter.W)

#ヘッダチェックサム
label_text = "ヘッダチェックサム (0-"+str(pkt.get_max_ip_chksum())+"):"
label_ip_chksum = tkinter.Label(frame_ip3, text=label_text)
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


#-----------------------------------------------------------
#Frame (UDP)
#-----------------------------------------------------------
#UDP: 1行目--------------------
frame_udp1 = tkinter.Frame(root)
frame_udp1.pack(fill=tkinter.X, padx=10)

#タイトル
title_text = "\n==================== UDP HEADER ===================="
label_udp_title  = tkinter.Label(frame_udp1, text=title_text, font=('System', '12', 'bold'))
label_udp_title.grid(row=0, column=0, columnspan=8, sticky=tkinter.W)

#送信元ポート番号
label_text = "送信元ポート番号 (0-"+str(pkt.get_max_udp_port())+"):"
label_udp_sport = tkinter.Label(frame_udp1, text=label_text)
label_udp_sport.grid(row=1, column=0, sticky=tkinter.W, padx=(5,0))
text_udp_sport = tkinter.Entry(frame_udp1, width=ENTRY_WIDTH)
text_udp_sport.insert(tkinter.END, "12345")
text_udp_sport.grid(row=1, column=1, sticky=tkinter.W)

#送信先ポート番号
label_text = "送信先ポート番号 (0-"+str(pkt.get_max_udp_port())+"):"
label_udp_dport = tkinter.Label(frame_udp1, text=label_text)
label_udp_dport.grid(row=1, column=2, sticky=tkinter.W, padx=(5,0))
text_udp_dport = tkinter.Entry(frame_udp1, width=ENTRY_WIDTH, state=tkinter.DISABLED)
text_udp_dport.grid(row=1, column=3, sticky=tkinter.W)

#UDP: 2行目--------------------
frame_udp2 = tkinter.Frame(root)
frame_udp2.pack(fill=tkinter.X, padx=10)

#データ長
label_text = "データ長 (0-"+str(pkt.get_max_udp_dtl())+"):"
label_udp_dtl = tkinter.Label(frame_udp2, text=label_text)
label_udp_dtl.grid(row=0, column=0, sticky=tkinter.W, padx=(5,0))
text_udp_dtl = tkinter.Entry(frame_udp2, width=ENTRY_WIDTH)
text_udp_dtl.grid(row=0, column=1, sticky=tkinter.W)

#チェックサム
label_text = "チェックサム (0-"+str(pkt.get_max_udp_chksum())+"):"
label_udp_chksum = tkinter.Label(frame_udp2, text=label_text)
label_udp_chksum.grid(row=0, column=2, sticky=tkinter.W, padx=(5,0))
text_udp_chksum = tkinter.Entry(frame_udp2, width=ENTRY_WIDTH)
text_udp_chksum.grid(row=0, column=3, sticky=tkinter.W)


#-----------------------------------------------------------
#Frame (User DATA)
#-----------------------------------------------------------
frame_user_data = tkinter.Frame(root)
frame_user_data.pack(fill=tkinter.X, padx=10)

#タイトル
title_text = "\n==================== User DATA ===================="
label_user_data_title  = tkinter.Label(frame_user_data, text=title_text, font=('System', '12', 'bold'))
label_user_data_title.grid(row=0, column=0, columnspan=8, sticky=tkinter.W)

#データ
label_user_data = tkinter.Label(frame_user_data, text="データ")
label_user_data.grid(row=1, column=0, sticky=tkinter.W, padx=(5,0))
text_user_data = tkinter.Entry(frame_user_data, width=80)
text_user_data.insert(tkinter.END, "TEST")
text_user_data.grid(row=1, column=1, sticky=tkinter.W)


#-----------------------------------------------------------
#Frame (RESULT)
#-----------------------------------------------------------
frame_result = tkinter.Frame(root)
frame_result.pack(fill=tkinter.X, pady=(60,10))

#結果出力用TEXT
text_result = tkinter.Text(frame_result,height=20, bg="WHITE", relief=tkinter.SOLID, bd=1)
text_result.config(state=tkinter.DISABLED)  #書き込み禁止
text_result.pack(side=tkinter.LEFT, padx=20)


manual_entry_ctrl() #手動Frame入力規制/解除

root.mainloop()