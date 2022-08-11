import tkinter


start_flag = False

#ラジオボタン押下
def radio_top_click():
    print("ラジオボタン押下:"+str(radio_top_text[radio_top_val.get()]))


#開始/停止ボタン押下
def btn_top_click():
    global start_flag

    if start_flag == False:
        start_flag = True
        btn_top.config(text='停止', bg='RED')

        #ラジオボタン規制
        radio_top_auto.config(state=tkinter.DISABLED)
        radio_top_manual.config(state=tkinter.DISABLED)
    else:
        start_flag = False
        btn_top.config(text='開始', bg='GREEN')

        #ラジオボタン規制解除
        radio_top_auto.config(state=tkinter.NORMAL)
        radio_top_auto.config(state=tkinter.NORMAL)




root = tkinter.Tk()
root.title("Packet Test")
root.geometry("800x400")


###########################################################
#TOP Frame
###########################################################
frame_top = tkinter.Frame(root,bg='WHITE', relief=tkinter.SOLID, bd=1,width=500)
frame_top.pack(fill=tkinter.X)

#部品配置
label_top_mode  = tkinter.Label(frame_top, padx=20, text="動作モード: ", font=('System', 12))
label_top_mode.pack(side=tkinter.LEFT, anchor=tkinter.W, fill=tkinter.X)

radio_top_text = ['auto', 'manual']
radio_top_val  = tkinter.IntVar()
radio_top_auto = tkinter.Radiobutton(frame_top, value=0, variable=radio_top_val, text=radio_top_text[0], font=('System', 12), command=radio_top_click)
radio_top_auto.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=5)
radio_top_manual = tkinter.Radiobutton(frame_top, value=1, variable=radio_top_val, text=radio_top_text[1], font=('System', 12), command=radio_top_click)
radio_top_manual.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=5)

btn_top = tkinter.Button(frame_top, text="開始", font=('System', 12), padx=10, bg='GREEN', command=btn_top_click)
btn_top.pack(side=tkinter.RIGHT, padx=10)




###########################################################
#MAIN Frame
###########################################################
frame_main = tkinter.Frame(root, width=100, bg='dark cyan')
frame_main.pack(fill=tkinter.X)


###########################################################
#STATUS Frame
###########################################################
frame_status = tkinter.Frame(root, bg='RED')
frame_status.pack(fill=tkinter.X)

root.mainloop()