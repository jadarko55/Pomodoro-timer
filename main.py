from tkinter import *
import pygame
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# Initialize pygame mixer for sound
pygame.mixer.init()

def play_sound():
    try:
        pygame.mixer.music.load("censor-beep.mp3")  
        pygame.mixer.music.play()
    except pygame.error:
        print("Could not play sound file. Make sure 'censor-beep.mp3' exists in the project folder.")

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig("timer", text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    REPS += 1
    
    # Play MP3 sound when session starts
    play_sound()

    if REPS % 8 == 0:
        count_down(canvas, long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(canvas, short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(canvas, work_sec)
        timer_label.config(text="Work", fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(canvas, count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig("timer", text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, canvas, count - 1)
    else:
        start_timer()
        if REPS % 2 == 1:  # Only add checkmark after work sessions (odd REPS)
            checkmark.config(text="✔" * ((REPS + 1) // 2))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label at the top
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1, pady=(0, 20))

# Canvas with tomato image in the center
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"), tag="timer")
canvas.grid(row=1, column=1, pady=20)

# Buttons in a row below the canvas
start_button = Button(text="Start", command=start_timer, bg=GREEN, fg="white", font=(FONT_NAME, 12, "bold"))
start_button.grid(row=2, column=0, padx=(0, 20))

reset_button = Button(text="Reset", command=reset_timer, bg=RED, fg="white", font=(FONT_NAME, 12, "bold"))
reset_button.grid(row=2, column=2, padx=(20, 0))

# Checkmarks at the bottom
checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark.grid(row=3, column=1, pady=(20, 0))

window.mainloop()
