from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

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
start_button = Button(text="Start", command=lambda: print("Start clicked"), bg=GREEN, fg="white", font=(FONT_NAME, 12, "bold"))
start_button.grid(row=2, column=0, padx=(0, 20))

reset_button = Button(text="Reset", command=lambda: print("Reset clicked"), bg=RED, fg="white", font=(FONT_NAME, 12, "bold"))
reset_button.grid(row=2, column=2, padx=(20, 0))

# Checkmarks at the bottom
checkmark = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark.grid(row=3, column=1, pady=(20, 0))

window.mainloop()
