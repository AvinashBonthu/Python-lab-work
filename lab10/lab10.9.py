from Tkinter import *
root=Tk()
Label(root,text="Enter the principle amount").pack()
p=Entry(root)
p.pack()
Label(root,text="Enter the time").pack()
i=Entry(root)
i.pack()
Label(root,text="Enter the rate").pack()
r=Entry(root)
r.pack()
def simpleint():
    a=str(float(p.get())*float(i.get())*float(r.get())/100)
    Label(root,text="Simple interest="+a).pack()
Button(root,text="Calculate",command=simpleint).pack()
root.mainloop()
