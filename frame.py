from cProfile import label
import tkinter

root = tkinter.Tk()
root.title("Packet Test")
root.geometry("600x400")

#MAIN Frame
frame_main = tkinter.Frame(root, width=100, bg='dark cyan')
frame_main.pack(side=tkinter.LEFT)

#Control Frame
frame_ctrl = tkinter.Frame(root, bg='BLUE')
frame_ctrl.pack(side=tkinter.RIGHT)

#STATUS Frame
frame_status = tkinter.Frame(root, bg='RED')
frame_status.pack(side=tkinter.BOTTOM)

root.mainloop()