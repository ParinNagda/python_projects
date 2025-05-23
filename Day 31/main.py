from tkinter import  *
import pandas
import random

from numpy.ma.core import filled

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/french_words.csv")
    data_dict = og_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

def read_letters():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(background_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(background_image, image=card_back_img)


def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    read_letters()


window = Tk()
window.title("Flash Card")
flip_timer = window.after(3000, func=flip_card)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)




card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

background_image = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400,150, text="Title", font=("Lato", 40, "italic"))
card_word = canvas.create_text(400,263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=read_letters)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


read_letters()


window.mainloop()
