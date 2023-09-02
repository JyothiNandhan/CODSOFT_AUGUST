from tkinter import*
win=Tk()
def Button_Click(num):
    global var
    var=var+str(num)
    data.set(var)

def Button_Equal():
    global var
    Res=str(eval(var))
    data.set(Res)



def Button_Cancel():
    global var
    var=""
    data.set(var)


win.geometry("375x230")
data=StringVar()
var=""
text=Entry(win, width="25",textvariable=data,relief=RAISED,font=("Arial",20,"bold"),highlightbackground="black",highlightthickness="2",bd=5)
text.grid(row=1,columnspan=4)
frame=Frame(win)
frame.place(x=10,y=50)
b1=Button(frame,text="7",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click(7))
b2=Button(frame,text="8",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click(8))
b3=Button(frame,text="9",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click(9))
b4=Button(frame,text="4",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click(4))
b5=Button(frame,text="5",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click(5))
b6=Button(frame,text="6",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click(6))
b7=Button(frame,text="1",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click(1))
b8=Button(frame,text="2",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click(2))
b9=Button(frame,text="3",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click(3))
b10=Button(frame,text="+",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click("+"))
b11=Button(frame,text="-",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click("-"))
b12=Button(frame,text="*",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click("*"))
b13=Button(frame,text="/",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click("/"))
b14=Button(frame,text="=",width="10",height="2",bg="orange",fg="black",activebackground="orange",activeforeground="blue"
    ,relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Equal())
b15=Button(frame,text="c",width="10",height="2",bg="orange",fg="white",activebackground="white",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Cancel())
b16=Button(frame,text=".",width="10",height="2",bg="black",fg="white",activebackground="orange",activeforeground="blue",
    relief=RAISED,font=("arial",10,"bold"),command=lambda:Button_Click("."))
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=4,column=0)
b5.grid(row=4,column=1)
b6.grid(row=4,column=2)
b7.grid(row=5,column=0)
b8.grid(row=5,column=1)
b9.grid(row=5,column=2)
b10.grid(row=3,column=3)
b11.grid(row=4,column=3)
b12.grid(row=5,column=3)
b13.grid(row=6,column=0)
b15.grid(row=6,column=1)
b16.grid(row=6,column=2)
b14.grid(row=6,column=3)


win.mainloop()