import tkinter

window = tkinter.Tk()

window.title("GUI")
window.geometry("300x100")

label1 = tkinter.Label(window, text="Value 01", font=("Arial Bold", 10))
label1.grid(column=0, row=0)

label2 = tkinter.Label(window, text="Value 02", font=("Arial Bold", 10))
label2.grid(column=0, row=1)

label3 = tkinter.Label(window, text="Answer:", font=("Arial Bold", 10))
label3.grid(column=2, row=0)

label4 = tkinter.Label(window, text="", font=("Arial Bold", 10))
label4.grid(column=3, row=0)

txt1 = tkinter.Entry(window, width=10)
txt1.grid(column=1, row=0)

txt2 = tkinter.Entry(window, width=10)
txt2.grid(column=1, row=1)
def clickedb1():
    label4.config(text=str(float(txt1.get()) + float(txt2.get())))


def clickedb2():
    label4.config(text=str(float(txt1.get()) - float(txt2.get())))


def clickedb3():
    label4.config(text=str(float(txt1.get()) * float(txt2.get())))


def clickedb4():
    label4.config(text=str(float(txt1.get()) / float(txt2.get())))


button1 = tkinter.Button(window, text="Add", bg="yellow", command=clickedb1)
button1.grid(column=0, row=2)

button2 = tkinter.Button(window, text="Sub", bg="yellow", command=clickedb2)
button2.grid(column=1, row=2)

button3 = tkinter.Button(window, text="Mul", bg="yellow", command=clickedb3)
button3.grid(column=2, row=2)

button4 = tkinter.Button(window, text="Div", bg="yellow", command=clickedb4)
button4.grid(column=3, row=2)

window.mainloop()