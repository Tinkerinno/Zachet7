from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

root = Tk()
root.title("Задача №7")
root.geometry('400x250')

label = Label(root, text="Добро пожаловать в приложение для доставки.") 
label.pack(ipadx=60, ipady=15) 

summa = float()
f = 150
p = 100
ga = 75
g = 50

check1 = IntVar() 
check2 = IntVar() 
check3 = IntVar() 
check4 = IntVar()

Weight = Entry(root, width=10)
Weight.place(x=90, y=62.5)
Weight.insert(0, "0")
label = Label(root, text="Вес (кг):")
label.place(x=5, y=60)

Length = Entry(root, width=10)
Length.place(x=90, y=85.5)
Length.insert(0, "0")
label = Label(root, text="Длина (см):")
label.place(x=5, y=83)

Width = Entry(root, width=10)
Width.place(x=90, y=108.5)
Width.insert(0, "0")
label = Label(root, text="Ширина (см):")
label.place(x=5, y=106)

label = Label(root, text="Расстояние (км):")
label.place(x=215, y=35)	

flykm = Entry(width=10, state = NORMAL)
flykm.place(x=225, y=58.5)
flykm.insert(0, "0")

def flyk(*args):
    if check1.get() == 1:
        flykm.configure(state = NORMAL)
    else:
        flykm.configure(state = DISABLED)

fly = Checkbutton(root, text = "Самолёт", variable = check1, command = flyk) 
fly.place(x=300, y=58.5)

trainkm = Entry(width=10, text="0", state = NORMAL)
trainkm.place(x=225, y=80)
trainkm.insert(0, "0")

def traink(*args):
    if check2.get() == 1:
        trainkm.configure(state = NORMAL)
    else:
        trainkm.configure(state = DISABLED)

train = Checkbutton(root, text = "Поезд", variable = check2, command = traink) 
train.place(x=300, y=80)

gruzautokm = Entry(width=10, state = NORMAL)
gruzautokm.place(x=225, y=100)
gruzautokm.insert(0, "0")

def gruzautok(*args):
    if check3.get() == 1:
        gruzautokm.configure(state = NORMAL)
    else:
        gruzautokm.configure(state = DISABLED)

gruzauto = Checkbutton(root, text = "Грузовой автомобиль", variable = check3, command = gruzautok) 
gruzauto.place(x=300, y=100)

gazelkm = Entry(width=10, state = NORMAL)
gazelkm.place(x=225, y=120)
gazelkm.insert(0, "0")

def gazelk(*args):
    if check4.get() == 1:
        gazelkm.configure(state = NORMAL)
    else:
        gazelkm.configure(state = DISABLED)

gazel = Checkbutton(root, text = "Газель (только малогабаритный груз)", variable = check4, command = gazelk)
gazel.place(x=300, y=120)	

otvet = Entry(width=10, state = DISABLED)
otvet.place(x=150, y=165)

def Sum(*args):
    if float(Weight.get()) <= 0 or float(Length.get()) <= 0 or float(Width.get()) <= 0:
        showerror(title="Ошибка!", message="Не пишите отрицательные числа или ноль!")
    elif float(flykm.get()) < 0 or float(trainkm.get()) < 0 or float(gruzautokm.get()) < 0 or float(gazelkm.get()) < 0:
        showerror(title="Ошибка!", message="Не пишите отрицательные числа!")
    elif 0 < float(Weight.get()) <= 10000 and 0 < float(Length.get()) <= 100 and 0 < float(Width.get()) <= 100:
        if check1.get() == 1:
            fl = float(flykm.get())
            if check2.get() == 1:
                tr = float(trainkm.get())
                if check3.get() == 1:
                    gr = float(gruzautokm.get())
                    if check4.get() == 1:
                        gaz = float(gazelkm.get())
                        summa = 0.5 * (fl + tr + gr + gaz) + f + p + ga + g
                    else:
                        summa = 0.5 * (fl + tr + gr) + f + p + ga
                elif check4.get() == 1:
                    gaz = float(gazelkm.get())
                    summa = 0.5 * (fl + tr + gaz) + f + ga + g
                else:
                    summa = 0.5 * (fl + tr) + f + p
            elif check3.get() == 1:
                gr = float(gruzautokm.get())
                if check4.get() == 1:
                    summa = 0.5 * (fl + gr + gaz) + f + ga + g
                else:
                    summa = 0.5 * (fl + gr) + f + ga
            else:
                summa = 0.5 * fl  + f
        elif check2.get() == 1:
            tr = float(trainkm.get())
            if check3.get() == 1:
                gr = float(gruzautokm.get())
                if check4.get() == 1:
                    gaz = float(gazelkm.get())
                    summa = 0.5 * (tr + gr + gaz) + p + ga + g
                else:
                    summa = 0.5 * (tr + gr) + p + ga
            elif check4.get() == 1:
                gaz = float(gazelkm.get())
                summa = 0.5 * (tr + gaz) + p + g
            else:
                summa = 0.5 * (tr) + p
        elif check3.get() == 1:
            gr = float(gruzautokm.get())
            if check4.get() == 1:
                gaz = float(gazelkm.get())
                summa = 0.5 * (gr + gaz) + ga + g
            else:
                summa = 0.5 * (gr) + p + ga
        elif check4.get() == 1:
            gaz = float(gazelkm.get())
            summa = 0.5 * gaz + g
        else:
            otvet = Entry(width=10, state = DISABLED)
            otvet.place(x=150, y=165)
    else:
        if check1.get() == 1:
            if check2.get() == 1:
                if check3.get() == 1:
                    gr = float(gruzautokm.get())
                    fl = float(flykm.get())
                    tr = float(trainkm.get())
                    summa = 0.75 * (fl + tr + gr) + f + p + ga
                else:
                    tr = float(trainkm.get())
                    fl = float(flykm.get())
                    summa = 0.75 * (fl + tr) + f + p
            elif check3.get() == 1:
                fl = float(flykm.get())
                gr = float(gruzautokm.get())
                summa = 0.75 * (fl + gr) + f + ga
            else:
                fl = float(flykm.get())
                summa = 0.75 * fl + f
        elif check2.get() == 1:
            tr = float(trainkm.get())
            if check3.get() == 1:
                gr = float(gruzautokm.get())
                summa = 0.75 * (tr + gr) + p + ga
            else:
                summa = 0.75 * tr + p
        elif check3.get() == 1:
            gr = float(gruzautokm.get())
            summa = 0.75 * gr + ga
        else:
            gr = float(gruzautokm.get())
            summa = 0.75 * (gr) + p + ga
            
    otvetk = StringVar(value=summa)
    otvet = Entry(width=10, textvariable=otvetk, state = DISABLED)
    otvet.place(x=150, y=165)

label = Label(text="Сумма:")
label.place(x=105, y=162.5)
    
but=Button(root, padx=5, pady=1, font=5)
but.place(x=130, y=200)
but["text"]="Посчитать"
but.bind("<Button-1>", Sum)

root.mainloop()