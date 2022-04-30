from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

WORK_MIN = 25
# WORK_MIN = .10            # for testing
SHORT_BREAK_MIN = 5
# SHORT_BREAK_MIN = .05     # for testing
LONG_BREAK_MIN = 20
# LONG_BREAK_MIN = .15      # for testing
reps = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(my_timer)
    global reps
    reps = 0
    title_label.config(text="Timer!", fg="#533E85")
    canvas.itemconfig(timer_text, text="--:--")
    completed_check_marks.config(text="Reps: ", fg="#533E85", font=12)


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():

    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    if reps % 8 == 0:
        title_label.config(text="Break!", fg="#041562")
        countdown(long_break)
    elif reps % 2 == 0:
        title_label.config(text="Break!", fg="#11468F")
        countdown(short_break)
    else:
        title_label.config(text="Work! ", fg="#DA1212")
        countdown(work_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    count_min = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, countdown, count - 1)
    if count == 0:
        window.bell()
        start_timer()
        completed_checks = ""
        work_sessions = math.floor(reps/2)
        for times in range(work_sessions):
            completed_checks += "✔"
        completed_check_marks.config(text=f"Reps: {completed_checks}", bg="#FFB72B", fg="#533E85", font=12)

# ---------------------------- UI SETUP ------------------------------- #


# window configurations
window = Tk()
window.title("Work and Learn Efficiently!")
window.config(padx=50, pady=20, bg="#FFB72B")

title_label = Label(text="Timer!", bg="#FFB72B", fg="#533E85", font=("Ariel", 35, "bold"))
title_label.grid(column=2, row=1)

# Pomodoro/Tomato image
canvas = Canvas(width=220, height=240, bg="#FFB72B", highlightbackground="#FFB72B")   # highlightthickness=0 also works
background_photo = PhotoImage(file="tomato3.png")
canvas.create_image(110, 115, image=background_photo)
timer_text = canvas.create_text(100, 130, text="--:--", fill="#533E85", font=("Ariel", 24, "bold"))
canvas.grid(column=2, row=2)

# start button
button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=1, row=3)

# reset button
button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=3, row=3)

# check-marks to denote completed work sessions
completed_check_marks = Label(text="Reps: ", bg="#FFB72B", fg="#533E85", font=12)
completed_check_marks.grid(column=2, row=4)



window.mainloop()
