from tkinter import *
from math import sqrt

l = ['+', '-', 'mod', '/', '//', '*']

a = ''
b = ''
r = ''
t = ''
c = False

def k(m: str):
    for i in range(len(m) - 1, -1, -1):
        if m[i] == ' ':
            break
        else:
            m = m[:-1]
        return m
def gget(n: str):
    global a, b, r, c, t
    if c:
        if n == '+/-':
            if b[0] == '-':
                b = b[1::]
            else:
                b = '-' + b
        elif n == 'sqrt':
            if '.' in b:
                b = float(b)
                t = k(t)
                b = str(sqrt(b))
                t += b
            else:
                b = int(b)
                t = k(t)
                b = str(sqrt(b))
                t += b
        elif n in l:
            ...
        elif n == 'del':
            if b != '':
                b = b[:-1]
                t = t[:-1]
            else:
                r = ''
                c = False
                t = t[:-3]
        elif n == '=' and b == '':
            ...
        elif n == '=' and b != '':
            if '.' in b:
                b = float(b)
            else:
                b = int(b)
            if r == '+':
                t = str(a + b)
            elif r == '-':
                t = str(a - b)
            elif r == '*':
                t = str(a * b)
            elif r == '/':
                t = str(a / b)
            elif r == '//':
                t = str(a // b)
            a = ''
            b = ''
            r = ''
            c = False
        else:
            b += n
            t += n

    else:
        if n == '=':
            ...
        elif n == 'sqrt':
            if '.' in a:
                a = float(a)
            else:
                a = int(a)
            t = str(sqrt(a))
            a = str(sqrt(a))

        elif n == 'del':
            a = a[:-1]
            t = a

        elif n == '+/-':
            if a[0] == '-':
                a = a[1::]
                t = a[1::]
            else:
                a = '-' + a
                t = '-' + a
        elif n in l and a == '':
            ...
        elif n in l:
            c = True
            a = str(a)

            if '.' in a:
                a = float(a)
            else:
                a = int(a)
            r = n
            t += " " + r + ' '
        else:
            a += n
            t += n
def gget1():
    global t
    gget('1')
    la.configure(text=t)


def gget2():
    global t
    gget('2')
    la.configure(text=t)


def gget3():
    global t
    gget('3')
    la.configure(text=t)


def gget4():
    global t
    gget('4')
    la.configure(text=t)


def gget5():
    global t
    gget('5')
    la.configure(text=t)


def gget6():
    global t
    gget('6')
    la.configure(text=t)


def gget7():
    global t
    gget('7')
    la.configure(text=t)


def gget8():
    global t
    gget('8')
    la.configure(text=t)


def gget9():
    global t
    gget('9')
    la.configure(text=t)


def gget0():
    global t
    gget('0')
    la.configure(text=t)

def ggetp():
    global t
    gget('+')
    la.configure(text=t)

def ggetm():
    global t
    gget('-')
    la.configure(text=t)

def ggetr():
    global t
    gget('=')
    la.configure(text=t)
    t = ''

def ggetz():
    global t
    gget('.')
    la.configure(text=t)

def ggetd():
    global t
    gget('/')
    la.configure(text=t)

def ggetym():
    global t
    gget('*')
    la.configure(text=t)

def ggetdd():
    global t
    gget('//')
    la.configure(text=t)

def ggets():
    global t
    gget('sqrt')
    la.configure(text=t)

def ggetde():
    global t
    gget('del')
    la.configure(text=t)

def ggetpm():
    global t
    gget('+/-')
    la.configure(text=t)

w = Tk()
w.title('Калькулятор')
w.geometry('286x316')
w.resizable(False, False)

la = Label(w, text='0', width= 35, height=2, anchor='w', font=('Arial', 10))
la.grid(row= 0, column= 0,columnspan= 4)

b7 = Button(w, text='7', height=3, command=gget7).grid(row= 2, column= 0, stick='we')

b8 = Button(w, text='8', height=3, command=gget8).grid(row= 2, column= 1, stick='we')

b9 = Button(w, text='9', height=3, command=gget9).grid(row= 2, column= 2, stick='we')

bd = Button(w, text='/', height=3, width=3, command=ggetd).grid(row= 1, column= 1, stick='we')

b4 = Button(w, text='4', height=3, command=gget4).grid(row= 3, column= 0, stick='we')

b5 = Button(w, text='5', height=3, command=gget5).grid(row= 3, column= 1, stick='we')

b6 = Button(w, text='6', height=3, command=gget6).grid(row= 3, column= 2, stick='we')

b1 = Button(w, text='1', height=3, command=gget1).grid(row= 4, column= 0, stick='we')

b2 = Button(w, text='2', height=3, command=gget2).grid(row= 4, column= 1, stick='we')

b3 = Button(w, text='3', height=3, command=gget3).grid(row= 4, column= 2, stick='we')

bpm = Button(w, text='+/-', height=3, command=ggetpm).grid(row= 5, column= 0, stick='we')

b0 = Button(w, text='0', height=3, command=gget0).grid(row= 5, column= 1, stick='we')

bz = Button(w, text=',', height=3, command=ggetz).grid(row= 5, column= 2, stick='we')

br = Button(w, text='=', height=3, command=ggetr).grid(row= 5, column= 3, stick='we')

bp = Button(w, text='+', height=3, command=ggetp).grid(row= 4, column= 3, stick='we')

bm = Button(w, text='-', height=3, command=ggetm).grid(row= 2, column= 3, stick='we')

bym = Button(w, text='*', height=3, command=ggetym).grid(row= 3, column= 3, stick='we')

bdd = Button(w, text='//', height=3, command=ggetdd).grid(row= 1, column= 0, stick='we')

bs = Button(w, text='sqrt', height=3, command=ggets).grid(row= 1, column= 2, stick='we')

bde = Button(w, text='del', height=3, command=ggetde).grid(row= 1, column= 3, stick='we')

w.mainloop()
