from tkinter import *

root = Tk()
root.title("Friendly Calculator")
root.geometry("340x460")
root.configure(bg="#202124")

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

equation = StringVar()

entry = Entry(root, textvariable=equation, font=("Segoe UI",22),
              bd=8, insertwidth=2, width=18, borderwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=20)

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('=',4,2),('+',4,3)
]

for (text,row,col) in buttons:
    if text == "=":
        Button(root,text=text,width=7,height=3,font=("Segoe UI",14),
               bg="#4CAF50",fg="white",
               command=equalpress).grid(row=row,column=col,padx=5,pady=5)
    else:
        Button(root,text=text,width=7,height=3,font=("Segoe UI",14),
               bg="#303134",fg="white",
               command=lambda t=text: press(t)).grid(row=row,column=col,padx=5,pady=5)

Button(root,text="C",width=15,height=2,font=("Segoe UI",12),
       bg="#EA4335",fg="white",
       command=clear).grid(row=5,column=0,columnspan=2,pady=10)

Button(root,text="⌫",width=15,height=2,font=("Segoe UI",12),
       bg="#FBBC05",fg="black",
       command=backspace).grid(row=5,column=2,columnspan=2,pady=10)

root.mainloop()
