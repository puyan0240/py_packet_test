import tkinter


start_flag = False


def radio_top_click():
    print(radio_top_text[radio_top_val.get()])

def btn_top_click():
    if start_flag == False:
        btn_top.config(text='停止', bg='RED')
    else:
        btn_top.config(text='開始', bg='GREEN')
    print("aaaa")
    print(radio_top_text[radio_top_val.get()])



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
for i in range(len(radio_top_text)):
    radio_top = tkinter.Radiobutton(frame_top, value=i, variable=radio_top_val, text=radio_top_text[i], font=('System', 12), command=radio_top_click)
    radio_top.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=5)

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