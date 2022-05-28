import tkinter as tk
import tkinter.font as font
from math import *
"""from sympy import *
from sympy.parsing.sympy_parser import parse_expr"""

root = tk.Tk()
WIDTH=704
HEIGHT=450
screen_x = int(root.winfo_screenwidth())
screen_y = int(root.winfo_screenheight())
posX= (screen_x // 2) - (WIDTH // 2)
posY= (screen_y // 2) - (HEIGHT // 2)
geo = '{}x{}+{}+{}'.format(WIDTH,HEIGHT,posX,posY)
root.geometry(geo)
root.resizable(0,0)
root.title("Calculator")

expression=""
total = 0
equation = tk.StringVar()
convert_unit = 1
a_convert_unit = 1
pixelVirtual = tk.PhotoImage(width=1, height=1)
myFont = font.Font(family="Helvetica", size=13, weight="bold")

#set the expression to ""
def clear():
    global expression
    expression=""
    equation.set(expression)
#adding numbres and operation to the expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
#evaluate the equation after clicking the "equal" button + traiting scientifc notation + get ride of trailing zeros ( 0.00100000 = 0.001 / 5.00 = 5)
def eql():
    global expression
    global total
    try :
        total = eval(expression)
        total = "{:.15f}".format(total)
        total = total.rstrip("0").rstrip(".")
        equation.set(total)
    except:
        equation.set("error")
#delete the last character from the string
def delete():
    global expression
    l = len(expression)
    expression = expression[:l-1]
    equation.set(expression)
def deg():
    global convert_unit
    global a_convert_unit
    convert_unit = pi/180
    a_convert_unit = 180/pi
    btdeg["fg"]="#ff9900"
    btrad["fg"]="#808080"
def rad():
    global convert_unit
    global a_convert_unit
    convert_unit = 1
    a_convert_unit = 1
    btdeg["fg"]="#808080"
    btrad["fg"]="#ff9900"
def fcos(x):
    return cos(x*convert_unit)
def fsin(x):
    if convert_unit==1 and x=="pi":
        return "0"
    else:
        return sin(x*convert_unit)
def ftan(x):
    if convert_unit==1 and x=="pi":
        return "0"
    else:
        return tan(x*convert_unit)
def arccos(x):
    return acos(x)*a_convert_unit
def arcsin(x):
    return asin(x)*a_convert_unit
def arctan(x):
    return atan(x)*a_convert_unit
def ln(x):
    return log(x)
def ans():
    global expression
    x = total[0]
    if x == "-":
        expression = expression + "(" + total + ")"
    else:
        expression = expression + total
    equation.set(expression)
top_frame = tk.Frame(root, width=WIDTH, height=80)
main = tk.Frame(root, width=WIDTH, height=370)
top_frame.pack(side=tk.TOP)
main.pack(side=tk.BOTTOM)

RESULT = tk.Label(top_frame, bg="#666666", fg="white", textvariable=equation, font=("Arial", 25), justify=tk.LEFT).place(width=WIDTH,height=80)
btrad = tk.Button(main, bg="#666666", fg="#ff9900", text="Rad", command= rad, activebackground="#ff9900", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btrad.grid(row=0 , column=0)
btdeg = tk.Button(main, bg="#666666", text="Deg", fg="#808080", command= deg, activebackground="#ff9900", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btdeg.grid(row=0 , column=1)
btsqrt = tk.Button(main, bg="#666666", text="√", fg="white", command=lambda: press("sqrt("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btsqrt.grid(row=0 , column=2)
btopenep = tk.Button(main, bg="#666666", text="(", fg="white", command=lambda: press("("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btopenep.grid(row=0 , column=3)
btclosep = tk.Button(main, bg="#666666", text=")", fg="white", command=lambda: press(")"), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btclosep.grid(row=0 , column=4)
btmod = tk.Button(main, bg="#666666", text="%", fg="white", command=lambda: press("%"), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btmod.grid(row=0 , column=5)
btdel = tk.Button(main, bg="#666666", text="del", fg="white", command= delete ,activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btdel.grid(row=0 , column=6)
btrst = tk.Button(main, bg="#666666", text="C", fg="white", command= clear, activebackground="white", activeforeground="#666666", image=pixelVirtual, font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btrst.grid(row=0 , column=7)
btfct = tk.Button(main, bg="#666666", text="x!", fg="white", command=lambda: press("factorial("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btfct.grid(row=1 , column=0)
btlg = tk.Button(main, bg="#666666", text="log", fg="white", command=lambda: press("log10("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btlg.grid(row=1 , column=1)
btx2 = tk.Button(main, bg="#666666", text="x\u00b2", fg="white", command=lambda: press("**2"), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btx2.grid(row=1 , column=2)
bt7 = tk.Button(main, bg="#4d4d4d", text="7", fg="white", command=lambda: press(7), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt7.grid(row=1 , column=3)
bt8 = tk.Button(main, bg="#4d4d4d", text="8", fg="white", command=lambda: press(8), activebackground="white", activeforeground="#666666", image=pixelVirtual, font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt8.grid(row=1 , column=4)
bt9 = tk.Button(main, bg="#4d4d4d", text="9", fg="white", command=lambda: press(9), activebackground="white", activeforeground="#666666", image=pixelVirtual, font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt9.grid(row=1 , column=5)
btdiv = tk.Button(main, bg="#666666", text="/", fg="white", command=lambda: press('/'), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btdiv.grid(row=1 , column=6)
btexp = tk.Button(main, bg="#666666", text="e", fg="white", command=lambda: press("exp("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btexp.grid(row=1 , column=7)
btln = tk.Button(main, bg="#666666", text="ln", fg="white", command=lambda: press("ln("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btln.grid(row=2 , column=0)
btpower = tk.Button(main, bg="#666666", text="x\u02B0", fg="white", command=lambda: press('**'), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btpower.grid(row=2 , column=1)
btx3 = tk.Button(main, bg="#666666", text="x\u00b3", fg="white", command=lambda: press("**3"), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btx3.grid(row=2 , column=2)
bt4 = tk.Button(main, bg="#4d4d4d", text="4", fg="white", command=lambda: press(4), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt4.grid(row=2 , column=3)
bt5 = tk.Button(main, bg="#4d4d4d", text="5", fg="white", command=lambda: press(5), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt5.grid(row=2 , column=4)
bt6 = tk.Button(main, bg="#4d4d4d", text="6", fg="white", command=lambda: press(6), activebackground="white", activeforeground="#666666", image=pixelVirtual, font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt6.grid(row=2 , column=5)
btmult = tk.Button(main, bg="#666666", text="x", fg="white", command=lambda: press('*'), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btmult.grid(row=2 , column=6)
btpi = tk.Button(main, bg="#666666", text="π", fg="white", command=lambda: press("pi"), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btpi.grid(row=2 , column=7)
btcos = tk.Button(main, bg="#666666", text="cos", fg="white", command=lambda: press("fcos("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btcos.grid(row=3 , column=0)
btsin = tk.Button(main, bg="#666666", text="sin", fg="white", command=lambda: press("fsin("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btsin.grid(row=3 , column=1)
bttan = tk.Button(main, bg="#666666", text="tan", fg="white", command=lambda: press("ftan("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bttan.grid(row=3 , column=2)
bt1 = tk.Button(main, bg="#4d4d4d", text="1", fg="white", command=lambda: press(1), activebackground="white", activeforeground="#666666", image=pixelVirtual, font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt1.grid(row=3 , column=3)
bt2 = tk.Button(main, bg="#4d4d4d", text="2", fg="white", command=lambda: press(2), activebackground="white", activeforeground="#666666", image=pixelVirtual, font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt2.grid(row=3 , column=4)
bt3 = tk.Button(main, bg="#4d4d4d", text="3", fg="white", command=lambda: press(3), activebackground="white", activeforeground="#666666", image=pixelVirtual, font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt3.grid(row=3 , column=5)
btsub = tk.Button(main, bg="#666666", text="-", fg="white", command=lambda: press('-'), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btsub.grid(row=3 , column=6)
bt10pwr= tk.Button(main, bg="#666666", text="10\u02b0", fg="white", command=lambda: press("10**("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt10pwr.grid(row=3 , column=7)
btcos_1 = tk.Button(main, bg="#666666", text="cos-\u00B9", fg="white", command=lambda: press("arccos("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btcos_1.grid(row=4 , column=0)
btsin_1 = tk.Button(main, bg="#666666", text="sin-\u00B9", fg="white", command=lambda: press("arcsin("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btsin_1.grid(row=4 , column=1)
bttan_1 = tk.Button(main, bg="#666666", text="tan-\u00B9", fg="white", command=lambda: press("arctan("), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bttan_1.grid(row=4 , column=2)
bt0 = tk.Button(main, bg="#4d4d4d", text="0", fg="white", command=lambda: press(0) , activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bt0.grid(row=4 , column=3)
btpt = tk.Button(main, bg="#4d4d4d", text=".", fg="white", command=lambda: press("."), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btpt.grid(row=4 , column=4)
bteq = tk.Button(main, bg="#ff9900", fg="black", text="=", command= eql, activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
bteq.grid(row=4 , column=5)
btadd= tk.Button(main, bg="#666666", text="+", fg="white", command=lambda: press("+"), activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btadd.grid(row=4 , column=6)
btans = tk.Button(main, bg="#666666", text="Ans", fg="white", command= ans ,activebackground="white", activeforeground="#666666", image=pixelVirtual , font=myFont, width=80, height=66, compound="c", relief=tk.FLAT)
btans.grid(row=4 ,column=7)
main.mainloop()