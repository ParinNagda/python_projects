from tkinter import *

def convertTemperature():
    degree = float(degree_input.get())
    farhenheit = (degree * 9/5) + 32
    answer.config(text=farhenheit)

window = Tk()
window.title("Degree to Fahrenheit")
window.config(pady=20, padx=20)

degree_input = Entry(width=7)
degree_input.grid(row=0, column=1)

degree_label = Label(text="Degree")
degree_label.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

answer = Label()
answer.grid(row=1, column=1)

fahrenheit_label = Label(text="Fahrenheit")
fahrenheit_label.grid(row=1, column=2)

calculate_button = Button(text="Convert", command=convertTemperature)
calculate_button.grid(row=2, column=1)


window.mainloop()