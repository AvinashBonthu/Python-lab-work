from Tkinter import *
root=Tk()
def infor():
    Label(root,text="Nice Job!").pack()
def info():
    Button(root,text="Click once more",command=infor).pack()
Button(root,text="Click",command=info).pack()
root.mainloop()
