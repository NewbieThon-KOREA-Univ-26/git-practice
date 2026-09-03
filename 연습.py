from tkinter import *


window = None
display_label = None
expression =""


def setup_gui():
   global window
   global display_label
   window = Tk()
   window.title('')


   display_label = Label(window, text='0', anchor='e', relief=SUNKEN, width=15, font='Arial 20')
   display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


   btn1 = Button(window, text='1',width=5, height=2, font='Arial 15', command=lambda:press(1))
   btn2 = Button(window, text='2', width=5, height=2, font='Arial 15', command=lambda:press(2))
   btn3 = Button(window, text='3',width=5, height=2, font='Arial 15', command=lambda:press(3))
   btn4 = Button(window, text='4',width=5, height=2, font='Arial 15', command=lambda:press(4))
   btn5 = Button(window, text='5',width=5, height=2, font='Arial 15', command=lambda:press(5))
   btn6 = Button(window, text='6',width=5, height=2, font='Arial 15', command=lambda:press(6))
   btn7 = Button(window, text='7',width=5, height=2, font='Arial 15', command=lambda:press(7))
   btn8 = Button(window, text='8',width=5, height=2, font='Arial 15', command=lambda:press(8))
   btn9 = Button(window, text='9',width=5, height=2, font='Arial 15', command=lambda:press(9))
   btn0 = Button(window, text='0',width=5, height=2, font='Arial 15', command=lambda:press(0))


   clearBtn = Button(window, text='C', width=5, height=2, font='Arial 15', command=press_clear)
   resultBtn = Button(window, text='=', width=5, height=2, font='Arial 15', command=press_result)
   addBtn = Button(window, text='+', width=5, height=2, font='Arial 15', command=lambda:press('+'))
   subBtn = Button(window, text='-', width=5, height=2, font='Arial 15', command=lambda:press('-'))
   mulBtn = Button(window, text='*', width=5, height=2, font='Arial 15', command=lambda:press('*'))
   divBtn = Button(window, text='/', width=5, height=2, font='Arial 15', command=lambda:press('/'))


   btn1.grid(row=1, column=0)
   btn2.grid(row=1, column=1)
   btn3.grid(row=1, column=2)
   btn4.grid(row=2, column=0)
   btn5.grid(row=2, column=1)
   btn6.grid(row=2, column=2)
   btn7.grid(row=3, column=0)
   btn8.grid(row=3, column=1)
   btn9.grid(row=3, column=2)
   btn0.grid(row=4, column=1)


   clearBtn.grid(row=4, column=0)
   resultBtn.grid(row=4, column=2)
   addBtn.grid(row=1, column=3)
   subBtn.grid(row=2, column=3)
   mulBtn.grid(row=3, column=3)
   divBtn.grid(row=4, column=3)


def press(num):
   global expression
   expression += str(num)
   display_label['text'] = expression




def press_clear():
   global expression
   expression = ''
   display_label['text'] = '0'




def press_result():
   global expression
   display_label['text'] = str(eval(expression))
   expression = ''




setup_gui()
window.mainloop()
