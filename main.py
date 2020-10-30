from tkinter import *
import urllib.request
import math as m
from tkinter import Tk, StringVar, ttk
###################################################################
root = Tk()
root.title('Hybrid Calculator')
root.geometry("450x360+100+200")
labelfont = ('ariel', 56, 'bold')

widget = Button(None, text="QUIT", bg="black", fg="Red", font=("Arial", 14, "bold"), relief=RAISED,
                justify=CENTER, highlightbackground="black",padx=205,pady=20, command=root.destroy).place(x=0, y=300)
######################################################################################################################
def CurrencyConverter():
    ids = {"US Dollar": 'USD', "Euros": 'EUR', "Indian Rupees": 'INR', "Qatar Doha": 'QAR', "Zimbwabe Harare": 'ZWD',
           "Arab Emirates Dirham": 'AED', "Pound Sterling": 'GBP', "Japanese Yen": 'JPY', "Yuan Renminbi": 'CNY'}

    def convert(amt, frm, to):
        html = urllib.request.urlopen(
            "http://www.exchangerate-api.com/%s/%s/%f?k=a28d653d2d4fd2727003e437" % (frm, to, amt))
        return html.read().decode('utf-8')

    def callback():
        try:
            amt = float(in_field.get())

        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Currency Converter")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    in_select = OptionMenu(mainframe, in_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha", "Zimbwabe Harare",
                           "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3,
                                                                                                           row=1,
                                                                                                           sticky=W)
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=2, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha", "Zimbwabe Harare",
                           "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3,
                                                                                                           row=2,
                                                                                                           sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=3, sticky=E)
##############################################################################################################
def WeightConverter():

    factors = {'kg': 1000, 'hg': 100, 'dg': 10, 'g': 1, 'deg': 0.1, 'cg': 0.01, 'mg': 0.001}
    ids = {"Kilogram": 'kg', "Hectagram": 'hg', "Decagram": 'dg', "Decigram": 'deg', "Kilogram": 'kg', "gram": 'g',
           "centigram": 'cg', "milligram": 'mg'}


    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Weight Converter")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))
    in_select = OptionMenu(mainframe, in_unit, "Kilogram", "Hectagram", "Decagram", "gram", "Decigram", "Centigram",
                           "Milligram").grid(column=3, row=1, sticky=W)

    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=2, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Kilogram", "Hectagram", "Decagram", "gram", "Decigram", "Centigram",
                           "Milligram").grid(column=3, row=2, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=3, sticky=E)
###########################################################################################################
def Calculator():
    root = Toplevel()
    root.title("Scientific Calculator")
    root.configure(bg="white")
    mainframe = ttk.Frame(root)
    mainframe.grid(row=0, column=0, columnspan=5)
    e = Entry(mainframe, width=40, relief=RIDGE, fg="White", bg="Black", justify=RIGHT)
    e.grid(ipady=15)
    mainframe2 = ttk.Frame(root)
    mainframe2.grid(row=1, column=0, columnspan=5)

    def click(to_print):
        old = e.get()
        e.delete(0, END)
        e.insert(0, old + to_print)
        return

    def sc(event):
        key = event.widget
        text = key['text']
        no = e.get()
        result = ''
        if text == 'sin':
            result = str(m.sin(float(no)))
        if text == 'cos':
            result = str(m.cos(float(no)))
        if text == 'tan':
            result = str(m.tan(float(no)))
        if text == 'log':
            result = str(m.log10(float(no)))
        if text == '√x':
            result = str(m.sqrt(float(no)))
        if text == 'x!':
            result = str(m.factorial(float(no)))
        if text == '1/x':
            result = str(1 / (float(no)))
        if text == 'e':
            if no == "":
                result = str(m.e)
            else:
                result = str(m.e ** float(no))

        e.delete(0, END)
        e.insert(0, result)

    def clear():
        e.delete(0, END)
        return

    def bksps():
        current = e.get()
        length = len(current) - 1
        e.delete(length, END)

    def evaluate():
        ans = e.get()
        ans = eval(ans)
        e.delete(0, END)
        e.insert(0, ans)

    lg = Button(mainframe2 , text="log", padx=26, pady=10)
    lg.bind("<Button-1>", sc)
    par1st = Button(mainframe2 , text="(", padx=30, pady=10,  command=lambda: click("("))
    par2nd = Button(mainframe2 , text=")", padx=30, pady=10,  command=lambda: click(")"))
    dot = Button(mainframe2 , text=".", padx=32, pady=10,  command=lambda: click("."))

    exp = Button(mainframe2 , text="^", padx=32, pady=10,  command=lambda: click("**"))

    sinb = Button(mainframe2 , text="sin", padx=24, pady=10)
    sinb.bind("<Button-1>", sc)
    cosb = Button(mainframe2 , text="cos", padx=22, pady=10)
    cosb.bind("<Button-1>", sc)
    tanb = Button(mainframe2 , text="tan", padx=23, pady=10)
    tanb.bind("<Button-1>", sc)

    sqrtm = Button(mainframe2 , text="√x", padx=26, pady=10)
    sqrtm.bind("<Button-1>", sc)
    ac = Button(mainframe2 , text="C", padx=29, pady=10,  command=lambda: clear())
    bksp = Button(mainframe2 , text=" ⌫ ", padx=23, pady=10,  command=lambda: bksps())
    mod = Button(mainframe2 , text="mod", padx=19, pady=10,  command=lambda: click("%"))
    div = Button(mainframe2 , text="/", padx=29, pady=10,  command=lambda: click("/"))

    fact = Button(mainframe2 , text="x!", padx=29, pady=10, relief=RAISED)
    fact.bind("<Button-1>", sc)
    seven = Button(mainframe2 , text="7", padx=30, pady=10, command=lambda: click("7"))
    eight = Button(mainframe2 , text="8", padx=29, pady=10, command=lambda: click("8"))
    nine = Button(mainframe2 , text="9", padx=29, pady=10, command=lambda: click("9"))
    mult = Button(mainframe2 , text="*", padx=29, pady=10,  command=lambda: click("*"))

    frac = Button(mainframe2 , text="1/x", padx=25, pady=10, relief=RAISED)
    frac.bind("<Button-1>", sc)
    four = Button(mainframe2 , text="4", padx=30, pady=10,  command=lambda: click("4"))
    five = Button(mainframe2 , text="5", padx=29, pady=10,  command=lambda: click("5"))
    six = Button(mainframe2 , text="6", padx=29, pady=10,  command=lambda: click("6"))
    minus = Button(mainframe2 , text="-", padx=29, pady=10,  command=lambda: click("-"))

    one = Button(mainframe2 , text="1", padx=30, pady=10, command=lambda: click("1"))
    two = Button(mainframe2 , text="2", padx=29, pady=10,  command=lambda: click("2"))
    three = Button(mainframe2 , text="3", padx=29, pady=10,  command=lambda: click("3"))
    plus = Button(mainframe2 , text="+", padx=29, pady=10, command=lambda: click("+"))

    e_b = Button(mainframe2 , text="e", padx=29, pady=10)
    e_b.bind("<Button-1>", sc)
    zero = Button(mainframe2 , text="0", padx=29, pady=10, command=lambda: click("0"))
    equal = Button(mainframe2 , text="=", padx=29, pady=10,  command=lambda: evaluate())

    lg.grid(row=1, column=0)
    e_b.grid(row=1, column=1)
    par1st.grid(row=1, column=2)
    par2nd.grid(row=1, column=3)
    equal.grid(row=1, column=4)

    exp.grid(row=2, column=0)
    tanb.grid(row=2, column=1)
    sinb.grid(row=2, column=2)
    cosb.grid(row=2, column=3)
    mod.grid(row=2, column=4)

    sqrtm.grid(row=3, column=0)
    ac.grid(row=3, column=1)
    zero.grid(row=3, column=2)
    bksp.grid(row=3, column=3)
    div.grid(row=3, column=4)

    fact.grid(row=4, column=0)
    seven.grid(row=4, column=1)
    eight.grid(row=4, column=2)
    nine.grid(row=4, column=3)
    mult.grid(row=4, column=4)

    frac.grid(row=5, column=0)
    four.grid(row=5, column=1)
    five.grid(row=5, column=2)
    six.grid(row=5, column=3)
    minus.grid(row=5, column=4)

    dot.grid(row=6, column=0)
    one.grid(row=6, column=1)
    two.grid(row=6, column=2)
    three.grid(row=6, column=3)
    plus.grid(row=6, column=4)
###########################################################################################################
def LengthConverter():
    factors = {'nmi': 1852, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1, 'cm': 0.01,
               'mm': 0.001}
    ids = {"Nautical Miles": 'nmi', "Miles": 'mi', "Yards": 'yd', "Feet": 'ft', "Inches": 'inch', "Kilometers": 'km',
           "meters": 'm', "centimeters": 'cm', "millileters": 'mm'}

    def convert(amt, frm, to):
        if frm != 'm':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Length Converter")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))
    in_select = OptionMenu(mainframe, in_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers",
                           "meters", "centimeters", "millileters").grid(column=3, row=1, sticky=W)

    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=2, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers",
                           "meters", "centimeters", "millileters").grid(column=3, row=2, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=3, sticky=E)
#####################################################################################################################
def TemperatureConverter():
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()

        if celTempVar.get() != 0.0:
            celToFah = (celTemp * 9 / 5 + 32)
            fahTempVar.set(celToFah)

        elif fahTempVar.get() != 0.0:
            fahToCel = ((fahTemp - 32) * (5 / 9))
            celTempVar.set(fahToCel)

    def reset():
        top = Toplevel(padx=50, pady=50)
        top.grid()
        message = Label(top, text="Reset Complete")
        button = Button(top, text="OK", command=top.destroy)

        message.grid(row=0, padx=5, pady=5)
        button.grid(row=1, ipadx=10, ipady=10, padx=5, pady=5)

        fahTempVar.set(int(0))
        celTempVar.set(int(0))

    top = Toplevel()
    top.title("Temperature Converter")
    celTempVar = IntVar()
    celTempVar.set(int(0))
    fahTempVar = IntVar()
    fahTempVar.set(int(0))

    celLabel = Label(top, text="Celcius: ", font=("Arial", 16), fg="black")
    celLabel.grid(row=2, column=2, pady=10, sticky=NW)

    fahLabel = Label(top, text="Fahrenheit: ", font=("Arial", 16), fg="black")
    fahLabel.grid(row=3, column=2, pady=10, sticky=NW)

    celEntry = Entry(top, width=10, bd=2, textvariable=celTempVar)
    celEntry.grid(row=2, column=2, pady=10, padx=125)

    fahEntry = Entry(top, width=10, bd=2, textvariable=fahTempVar)
    fahEntry.grid(row=3, column=2, pady=10, padx=125)

    convertButton = Button(top, text="Convert", font=("Arial", 8, "bold"), bd=5, justify=CENTER,command=convert)
    convertButton.grid(row=4, column=2, ipady=8, ipadx=12, pady=10, padx=55)

    resetButton = Button(top, text="Reset", font=("Arial", 8, "bold"), bd=5, justify=CENTER,command=reset)
    resetButton.grid(row=5, column=2, ipady=8, ipadx=12, pady=10 )
####################################################################################################

widget = Button(root, text="Temperature converter", bg="grey", fg="white", font=("Arial", 14, "bold"), relief=RAISED,
                bd=5, justify=CENTER, highlightbackground="black",padx=145,pady=20,command=TemperatureConverter).place(x=0, y=60)
widget = Button(root, text="Length Converter", bg="grey", fg="white", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="black",padx=163,pady=20, command=LengthConverter).place(x=0, y=120)
widget = Button(root, text="Calculator", bg="grey", fg="white", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
               justify=CENTER, highlightbackground="black",padx=187,pady=20, command=Calculator).place(x=0, y=180)
widget = Button(root, text="Currency converter", bg="grey", fg="white", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="black",padx=156,pady=20, command=CurrencyConverter).place(x=0, y=0)
widget = Button(root, text="Weight Converter", bg="grey", fg="white", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="black",padx=163,pady=20, command=WeightConverter).place(x=0, y=240)

root.mainloop()
