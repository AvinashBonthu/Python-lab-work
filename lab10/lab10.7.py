from Tkinter import *
root=Tk()
Label(root,text="Enter the first number").pack()
e1=Entry(root)
e1.pack()
Label(root,text="Enter the second number").pack()
e2=Entry(root)
e2.pack()
def add():
    Label(root,text="The sum="+str(int(e1.get())+int(e2.get()))).pack()
Button(root,text="Sum",command=add).pack()
def sub():
    Label(root,text="The Difference="+str(int(e1.get())-int(e2.get()))).pack()
Button(root,text="Diff",command=sub).pack()
def mul():
    Label(root,text="The Multiplication="+str(int(e1.get())*int(e2.get()))).pack()
Button(root,text="Multiply",command=mul).pack()
def div():
    if int(e2.get())!=0:
        c=float(e1.get())/float(e2.get())
        Label(root,text="The division="+str(c)).pack()
    else:
        Label(root,text="The division is not defined").pack()
Button(root,text="Div",command=div).pack()
def rem():
    Label(root,text="The remainder="+str(int(e1.get())%int(e2.get()))).pack()
Button(root,text="Rem",command=rem).pack()
root.mainloop()
