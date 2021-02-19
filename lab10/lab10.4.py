from Tkinter import *
root=Tk()
def event():
    Label(root,text="Welcome....\n").pack()
Button(root,text="Go",command=event).pack()
root.mainloop()
