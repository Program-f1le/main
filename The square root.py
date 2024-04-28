import tkinter
import math

window = tkinter.Tk()
window.geometry('500x500')
window.resizable(False, False)

def koreni_2(a, b, c):
   D = (b ** 2) - (4 * a * c)
   if D > 0:
       x1 = (-b - math.sqrt(D)) / (2 * a)
       x2 = (-b + math.sqrt(D)) / (2 * a)
       return f'Первый корень {x1}, Второй корень {x2}'
   else:
       return 'Корень уравнения: ', -b / 2 * a

def reyte():
    a1 = tkinter.Label(window, text= koreni_2(a, b, c))
    a1.grid(row=4, column=1)

def get():
    global a
    a = int(entry1.get())
    return a

def get1():
    global b
    b = int(entry2.get())
    return b

def get2():
    global c
    c = int(entry3.get())
    return c

def all():
    get()
    get1()
    get2()
    koreni_2(a, b, c)
    reyte()

lable1 = tkinter.Label(window, text='a = ')
lable1.grid(row= 0, column=0)

entry1 = tkinter.Entry(window)
entry1.grid(row= 0, column=1)


button1 = tkinter.Button(window, text= 'Вывести ответ', command= all)
button1.grid(row= 3, column=1)

lable2 = tkinter.Label(window, text='b = ')
lable2.grid(row= 1, column=0)

entry2 = tkinter.Entry(window)
entry2.grid(row= 1, column=1)

lable3 = tkinter.Label(window, text='c = ')
lable3.grid(row= 2, column=0)

entry3 = tkinter.Entry(window)
entry3.grid(row= 2, column=1)

window.mainloop()