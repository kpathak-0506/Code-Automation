from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import messagebox as mb
root = Tk()
root.geometry("1300x1300")
root.title("Code Automation")
tabControl = ttk.Notebook(root)
root.counter = 0

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Design')
tabControl.add(tab2, text='Code')
tabControl.add(tab3, text='Preview')
tabControl.pack(expand=1, fill="both")

lab=Label(tab1,text="Code Automation",font=("arial",14,"bold"),width=20)
lab.place(x=0,y=10)

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


def destroy(event):
    widget = event.widget
    widget.destroy()

def hover(event):
    widget = event.widget



# FRAMES-------------------------------------------------------------------------------------------------------------------------
Frame1 = Frame(tab1, bg="light gray", bd=20, width=180, height=1300)
Frame1.grid(row=0, column=0)
Frame2 = Frame(tab1, bg="white", bd=20, width=800, height=1300)
Frame2.grid(row=0, column=1)
Frame3 = Frame(tab1, bg="light gray", width=320, height=1300)
Frame3.grid(row=0, column=2)
lab=Label(Frame2,text="Code Automation",font=("arial",20,"bold"),width=20,bg="white")
lab.place(x=200,y=0)
# FRAME 3-------------------------------------------------------------------------------------------------------------------------
width_frame = LabelFrame(tab1, text="Width")
width_frame.place(x=1010, y=100)
height_frame = LabelFrame(tab1, text="Height")
height_frame.place(x=1010, y=170)
width_slider = ttk.Scale(width_frame, from_=10, to=500, orient=HORIZONTAL, length=200)
width_slider.pack(padx=10, pady=10)
height_slider = ttk.Scale(height_frame, from_=0, to=50, orient=HORIZONTAL, length=200)
height_slider.pack(padx=10, pady=10)

label_name = Label(tab1, text="Label Name :", font=("arial", 10), bg="light gray")
label_name.place(x=1020, y=305)
e1 = Entry(tab1, width=10)
e1.place(x=1120, y=310)

bcol = Label(tab1, text="Bg Colour :", font=("arial", 10), bg="light gray")
bcol.place(x=1020, y=275)
e2 = Entry(tab1, width=10)
e2.place(x=1120, y=280)

fcol = Label(tab1, text="Font Colour :", font=("arial", 10), bg="light gray")
fcol.place(x=1020, y=335)
e3 = Entry(tab1, width=10)
e3.place(x=1120, y=340)

configfile = Text(tab2, width=200, height=40)
configfile.pack()
class entry:

    def __init__(self, master):
        self.myentry = Entry(master, bg="white", width=10)
        self.myentry.place(x=500, y=600)
        self.button = Button(tab1, text="OK", width=5, bg="gray",
                             command=lambda: (self.width(), self.create_page(),self.colour()))
        self.button.place(x=1000, y=400)
        self.myentry.bind("<Button-1>", drag_start)
        self.myentry.bind("<B1-Motion>", drag_motion)
        self.myentry.bind("<Button-3>", destroy)
        self.myentry.bind("<Double-Button-1>",hover)

    def width(self):
        self.myentry.config(width=int(width_slider.get()))
        self.wid = Label(Frame3, text=int(width_slider.get()), width=10, font=("arial", 10))
        self.wid.place(x=1200, y=100)

    def colour(self):
        self.myentry.config(bg=e2.get())

    def create_page(self):
        global l1
        configfile.insert(INSERT, str("<input type= text\t id=" + str(e2.get()) + "\t STYLE= 'font-family: Verdana; font-weight: bold;background-color: "+str(e2.get()) + "; size=" + str(int(width_slider.get())) + "'>\n"))
        l1=[]
        l1.append("<input type= text\t id=" + str(e2.get()) + "\t STYLE= 'font-family: Verdana; font-weight: bold;background-color: "+str(e2.get()) + "; width:" + str(int(width_slider.get())) + "px'>\n")

class label:

    def __init__(self, master):
        self.mylabel = Label(master, text="type here",bg="white", width=10, height=1, font=("arial",10))
        self.mylabel.place(x=500, y=600)
        self.button = Button(tab1, text="OK", width=5, bg="gray",
                             command=lambda: (self.text(), self.create_page()))
        self.button.place(x=1000, y=400)
        self.mylabel.bind("<Button-1>", drag_start)
        self.mylabel.bind("<B1-Motion>", drag_motion)
        self.mylabel.bind("<Button-3>", destroy)

    def text(self):
        self.mylabel.config(text=e1.get())

    def create_page(self):
        global l2
        configfile.insert(INSERT, str( "<label for="+str(e2.get())+">"+str(e1.get())+":</label>\n"))
        l2=[]
        l2.append("<label for="+str(e2.get())+">"+str(e1.get())+":</label>\n")

class textbox:

    def __init__(self, master):
        self.mytext = Text(master, bg="white", width=10, height=2, font=("arial",14))
        self.mytext.place(x=500, y=600)
        self.button = Button(tab1, text="OK", width=5, bg="gray",
                             command=lambda: (self.width(),self.colour(),self.fcolour(),self.create_page(),self.height()))
        self.button.place(x=1000, y=400)
        self.mytext.bind("<Button-1>", drag_start)
        self.mytext.bind("<B1-Motion>", drag_motion)
        self.mytext.bind("<Button-3>", destroy)

    def width(self):
        self.mytext.config(width=int(width_slider.get()))
        self.wid = Label(tab1, text=int(width_slider.get()), width=5, font=("arial", 10),bg="white")
        self.wid.place(x=1250, y=120)

    def height(self):
        self.mytext.config(height=int(height_slider.get()))
        self.hid = Label(tab1, text=int(height_slider.get()), width=5, font=("arial", 10),bg="white")
        self.hid.place(x=1250, y=190)

    def colour(self):
        self.mytext.config(bg=e2.get())

    def fcolour(self):
        self.mytext.config(fg=e3.get())


    def create_page(self):
        global l3
        configfile.insert(INSERT, str("<textarea  name="+str(e2.get())+" rows="+str(int(height_slider.get()))+ " cols="+str(int(width_slider.get()))+" style='background-color:"+str(e2.get())+"; color:"+str(e3.get())+";'></textarea>\n"))
        l3=[]
        l3.append("<textarea  name="+str(e2.get())+" rows=3 style='background-color:"+str(e2.get())+"; color:"+str(e3.get())+"; cols=20; width:"+str(int(width_slider.get()))+"px height:"+str(int(height_slider.get()))+"px'></textarea>\n")

class checkbox:

    def __init__(self, master):
        CheckVar1=IntVar()
        self.mycheck = Checkbutton(master, text = "Option", variable = CheckVar1,onvalue = 1, offvalue = 0)
        self.mycheck.place(x=500, y=600)
        self.button = Button(tab1, text="OK", width=5, bg="gray",
                             command=lambda: (self.text(), self.create_page(),))
        self.button.place(x=1000, y=400)
        self.mycheck.bind("<Button-1>", drag_start)
        self.mycheck.bind("<B1-Motion>", drag_motion)
        self.mycheck.bind("<Button-3>", destroy)

    def text(self):
        self.mycheck.config(text=e1.get())

    def create_page(self):
        global l4
        configfile.insert(INSERT, str("<input type="'checkbox'" name="+str(e1.get())+"> "+str(e1.get())+"\n" ))
        l4=[]
        l4.append("<input type="'checkbox'" name="+str(e1.get())+"> "+str(e1.get())+"\n")

class radiobox:

    def __init__(self, master):
        var=IntVar()
        self.myradio = Radiobutton(master, text="Option 1", variable=var, value=1)
        self.myradio.place(x=500, y=600)
        self.button = Button(tab1, text="OK", width=5, bg="gray",
                             command=lambda: (self.text(), self.create_page()))
        self.button.place(x=1000, y=400)
        self.myradio.bind("<Button-1>", drag_start)
        self.myradio.bind("<B1-Motion>", drag_motion)
        self.myradio.bind("<Button-3>", destroy)

    def text(self):
        self.myradio.config(text=e1.get())

    def create_page(self):
        global l5
        configfile.insert(INSERT, str("<input type="'radio'" name="+str(e1.get())+"> "+str(e1.get())+ "\n"))
        l5=[]
        l5.append("<input type="'radio'" name="+str(e1.get())+"> "+str(e1.get())+ "\n")

class buttonbox:

    def __init__(self, master):
        self.mybutton = Button(master, text ="Name", font=("arial",10),width=5, bg="gray",fg="black")
        self.mybutton.place(x=500, y=600)
        self.button = Button(tab1, text="OK", width=5, bg="gray",
                             command=lambda: (self.width(), self.create_page(),self.colour(),self.fcolour(),self.height(),self.text()))
        self.button.place(x=1000, y=400)
        self.mybutton.bind("<Button-1>", drag_start)
        self.mybutton.bind("<B1-Motion>", drag_motion)
        self.mybutton.bind("<Button-3>", destroy)

    def width(self):
        self.mybutton.config(width=int(width_slider.get()))
        self.wid = Label(Frame3, text=int(width_slider.get()), width=10, font=("arial", 10))
        self.wid.place(x=1200, y=100)

    def height(self):
        self.mybutton.config(height=int(height_slider.get()))
        self.hid = Label(Frame3, text=int(height_slider.get()), width=10, font=("arial", 10))
        self.hid.place(x=1200, y=100)

    def colour(self):
        self.mybutton.config(bg=e2.get())

    def fcolour(self):
        self.mybutton.config(fg=e3.get())

    def text(self):
        self.mybutton.config(text=e1.get())

    def create_page(self):
        global l6
        configfile.insert(INSERT, str("<input type='Submit' value="+str(e1.get())+" style='background-color:"+str(e2.get())+";padding: 10px 24px; color:"+str(e3.get())+";  width:"+str(int(width_slider.get()))+"px height:"+str(int(height_slider.get()))+"px'>\n"))
        l6=[]
        l6.append("<input type='Submit' value="+str(e1.get())+" style='background-color:"+str(e2.get())+";padding: 10px 24px; color:"+str(e3.get())+";  width:"+str(int(width_slider.get()))+"px height:"+str(int(height_slider.get()))+"px'>\n")

class header1:

    def __init__(self, master):
        self.mylabel = Label(master, text="Heading",bg="white", width=10, height=2, font=("arial",17),fg="black")
        self.mylabel.place(x=500, y=600)
        self.button = Button(tab1, text="OK", width=5, bg="gray",
                             command=lambda: (self.text(), self.create_page(),self.fcolour(),self.width(),self.height()))
        self.button.place(x=1000, y=400)
        self.mylabel.bind("<Button-1>", drag_start)
        self.mylabel.bind("<B1-Motion>", drag_motion)
        self.mylabel.bind("<Button-3>", destroy)

    def fcolour(self):
        self.mylabel.config(fg=e3.get())

    def colour(self):
        self.mylabel.config(bg=e2.get())
    def text(self):
        self.mylabel.config(text=e1.get())

    def width(self):
        self.mylabel.config(width=int(width_slider.get()))
        self.wid = Label(Frame3, text=int(width_slider.get()), width=10, font=("arial", 10))
        self.wid.place(x=1200, y=100)

    def height(self):
        self.mylabel.config(height=int(height_slider.get()))
        self.hid = Label(Frame3, text=int(height_slider.get()), width=10, font=("arial", 10))
        self.hid.place(x=1200, y=100)

    def create_page(self):
        global l7
        configfile.insert(INSERT, str("<h1 style='background-color:"+str(e2.get())+";color:"+str(e3.get())+";text-align:center'>"+str(e1.get())+"</h1>\n"))
        l7=[]
        l7.append("<h1 style='background-color:"+str(e2.get())+";color:"+str(e3.get())+";text-align:center'>"+str(e1.get())+"</h1>\n")

class para:

    def __init__(self, master):
        self.mylabel = Label(master, text="type ....",bg="white", width=40, height=1, font=("arial",10),fg="black")
        self.mylabel.place(x=500, y=600)
        self.button = Button(tab1, text="OK", width=5, bg="gray",command=lambda: (self.text(), self.colour(),self.create_page()))
        self.button.place(x=1000, y=400)
        self.mylabel.bind("<Button-1>", drag_start)
        self.mylabel.bind("<B1-Motion>", drag_motion)
        self.mylabel.bind("<Button-3>", destroy)

    def text(self):
        self.mylabel.config(text=e1.get())
    def colour(self):
        self.mylabel.config(fg=e3.get())

    def create_page(self):
        global l8
        configfile.insert(INSERT, str("<div style='color:"+str(e3.get())+"; text-align:center;'>"+str(e1.get())+"</div>\n"))
        l8=[]
        l8.append("<div style='color:"+str(e3.get())+"; text-align:center;'>"+str(e1.get())+"</div>\n")

class header2:

    def __init__(self, master):
        self.mylabel = Label(master, text="Heading",bg="white", width=10, height=2, font=("arial",13),fg="black")
        self.mylabel.place(x=500, y=600)
        self.button = Button(tab1, text="OK", width=5, bg="gray",
                             command=lambda: (self.text(), self.create_page(),self.fcolour(),self.width(),self.height()))
        self.button.place(x=1000, y=400)
        self.mylabel.bind("<Button-1>", drag_start)
        self.mylabel.bind("<B1-Motion>", drag_motion)
        self.mylabel.bind("<Button-3>", destroy)

    def fcolour(self):
        self.mylabel.config(fg=e3.get())

    def colour(self):
        self.mylabel.config(bg=e2.get())
    def text(self):
        self.mylabel.config(text=e1.get())

    def width(self):
        self.mylabel.config(width=int(width_slider.get()))
        self.wid = Label(Frame3, text=int(width_slider.get()), width=10, font=("arial", 10))
        self.wid.place(x=1200, y=100)

    def height(self):
        self.mylabel.config(height=int(height_slider.get()))
        self.hid = Label(Frame3, text=int(height_slider.get()), width=10, font=("arial", 10))
        self.hid.place(x=1200, y=100)

    def create_page(self):
        global l9
        configfile.insert(INSERT, str("<h2 style='background-color:"+str(e2.get())+";color:"+str(e3.get())+";text-align:center'>"+str(e1.get())+"</h2>\n"))
        l9=[]
        l9.append("<h2 style='background-color:"+str(e2.get())+";color:"+str(e3.get())+";text-align:center'>"+str(e1.get())+"</h2>\n")

class breaker:
    def __init__(self):
       global l10
       configfile.insert(INSERT, str("<br>"))
       l10=[]
       l10.append("<br>\n")

class unorderedlist:
    def __init__(self,master):
        self.mylabel = Label(master, text="Type", bg="white", width=10, font=("arial", 10), fg="black")
        self.mylabel.place(x=500, y=600)
        self.button = Button(tab1, text="OK", width=5, bg="gray",command=lambda: ( self.text(), self.fcolour(),self.create_page()))
        self.button.place(x=1000, y=400)
        self.mylabel.bind("<Button-1>", drag_start)
        self.mylabel.bind("<B1-Motion>", drag_motion)
        self.mylabel.bind("<Button-3>", destroy)
    def fcolour(self):
        self.mylabel.config(fg=e3.get())
    def text(self):
        self.mylabel.config(text=e1.get())

    def create_page(self):
        global l11
        configfile.insert(INSERT, str("<li style='color:"+str(e3.get())+"'>"+str(e1.get())+"\n"))
        l11 = []
        l11.append("<li style='color:"+str(e3.get())+"'>"+str(e1.get())+"\n")
class back:
    def __init__(self):
       mb.showinfo("Message", "Type your colour BG section")
       global l12

       self.button = Button(tab1, text="OK", width=5, bg="gray",command=self.insert)
       self.button.place(x=1000, y=400)
    def insert(self):

          l12=[]
          l12.append("<body style='color:"+str(e2.get())+">\n")
          f = open("final.html", "r")
          contents = f.readlines()
          f.close()
          contents.insert(6, str("<body style='background-color:"+str(e2.get())+"'>\n"))

          f = open("final.html", "w")
          contents = "".join(contents)
          f.write(contents)
          f.close()

def button0():
    a = entry(Frame2)
def button1():
    z = label(Frame2)
def button2():
    y = textbox(Frame2)
def button3():
    x = checkbox(Frame2)
def button4():
    x = radiobox(Frame2)
def button5():
    w = buttonbox(Frame2)
def button6():
    v = header1(Frame2)
def button7():
    s = header2(Frame2)
def button8():
    u = para(Frame2)
def button9():
    r=breaker()
def button10():
    q=unorderedlist(Frame2)
def button11():
    p=back()
def done():
    result=configfile.get("1.0", "end")
    f = open("final.html", "r")
    contents = f.readlines()
    f.close()
    contents.insert(7, result)

    f = open("final.html", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

    file = open("final.html", "r")
    c = file.read()

    configfile.insert(INSERT, "------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    configfile.insert(INSERT,"-------------------------------------------------------------------------Final Code--------------------------------------------------------------------------------\n")
    configfile.insert(INSERT,str(c))

# FRAME 2--------------------------------------------------------------------------------------------------------------------
b1 = Button(tab1, text="Entry Box", width=20, height=2, font=("arial", 10), command=button0)
b1.place(x=0, y=70)
b2=Button(tab1,text="Label",width=20,height=2,font=("arial",10),command=button1)
b2.place(x=0,y=120)
b3=Button(tab1,text="Text Box",width=20,height=2,font=("arial",10),command=button2)
b3.place(x=0,y=170)
b4=Button(tab1,text="Check Box",width=20,height=2,font=("arial",10),command=button3)
b4.place(x=0,y=220)
b5=Button(tab1,text="Radio Button",width=20,height=2,font=("arial",10),command=button4)
b5.place(x=0,y=270)
b6=Button(tab1,text="Button",width=20,height=2,font=("arial",10),command=button5)
b6.place(x=0,y=320)
b7=Button(tab1,text="Heading 1",width=20,height=2,font=("arial",10),command=button6)
b7.place(x=0,y=370)
b8=Button(tab1,text="Heading 2",width=20,height=2,font=("arial",10),command=button7)
b8.place(x=0,y=420)
b9=Button(tab1,text="Paragraph",width=20,height=2,font=("arial",10),command=button8)
b9.place(x=0,y=470)
b10=Button(tab1,text="Breaker<br>",width=20,height=2,font=("arial",10),bg="yellow",command=button9)
b10.place(x=0,y=620)
b11=Button(tab1,text="Unordered List",width=20,height=2,font=("arial",10),command=button10)
b11.place(x=0,y=520)
b12=Button(tab1,text="Background Colour",width=20,height=2,font=("arial",10),command=button11)
b12.place(x=0,y=570)
donebtn=Button(tab1,text="Done",width=10,height=1,font=("arial",10,"bold"),bg="green",command=done)
donebtn.place(x=530,y=630)

def openn():
    filename = "final.html"
    webbrowser.open_new_tab(filename)
pre=Label(tab3,text="See your Output Here",fg="black",font=("arial",20),width=20,height=3)
pre.place(x=480,y=200)
preview=Button(tab3,text="Show my Output",bg="green",fg="black",font=("arial",12),width=20,height=1,command=openn)
preview.place(x=550,y=300)
root.resizable(0, 0)
root.mainloop()
