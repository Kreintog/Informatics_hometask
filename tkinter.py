from tkinter import *
from tkinter import messagebox
from math import *


# специальная функция - отрисовка канваса по параметрам
def my_action():
    
    frm = int(e1.get())
    to   = int(e2.get())
    color = v.get()
    for i in range( frm, to):
        canvas.create_line(i,10*sin(i)+150, i+1, 10*sin(i)+150, fill=color , width=10)

        
# а теперь за главное окно будет отвечать переменная master
master = Tk()
master.title('Рисуем')


canvas = Canvas(master, width=800, height=400, background='black')
canvas.grid(column=0, row=1)


# виджет Label - просто надпись
l1 = Label(master, text='t0')
l1.grid(row=2, column=0, sticky='e')
l2 = Label(master, text='t1')
l2.grid(row=3, column=0, sticky='e')

# виджет Entry - поле ввода текстовой информации. 
e1 = Entry(master)
e2 = Entry(master)
v = StringVar()
e3 =Radiobutton(master,text = 'red', variable = v, value = 'red')
e4 =Radiobutton(master,text = 'blue', variable = v, value = 'blue')
e5 =Radiobutton(master,text = 'green', variable = v, value = 'green')

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid()
e4.grid()
e5.grid()


# виджет Button() - кнопка с текстом, нажатие на которую вызывает 
# выполнение команды-функции, переданной в параметрах. Сама функция
# описана 19 строками выше
b1 = Button(master, text="Draw!", command = my_action)
b1.grid(row=4, column = 1)

master.mainloop()