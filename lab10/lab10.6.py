from Tkinter import *
root=Tk()
Label(root,text="Enter your first name").pack()
e1=Entry(root)
e1.pack()
Label(root,text="Enter your last name").pack()
e2=Entry(root)
e2.pack()
def info():
    Label(root,text=e1.get()+"...Welcome to Python").pack()
Button(root,text="Go",command=info).pack()
root.mainloop()
