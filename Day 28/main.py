from tkinter import *

import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps+=1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_seconds)
        title_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count >= 0:
        global timer
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✓"
        check_mark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
# ✓
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 34, "bold"), bg=YELLOW)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start",  highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",  highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_label = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME,15,"bold"))
check_mark_label.grid(row=3, column=1)

window.mainloop()