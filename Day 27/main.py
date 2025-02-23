from tkinter import *

def button_clicked():
    my_label.config(text="Button got clicked")
    inputValue = input.get()
    print(inputValue)

window = Tk()

window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=20 ,pady=20)

my_label = Label(text="Label", font=("Lato", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)

button = Button(text="Click me!", command=button_clicked)
button.grid(row=1,column=0)

input = Entry(width=10)
input.grid(row=2, column=0)


window.mainloop()
