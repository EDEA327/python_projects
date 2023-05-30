import tkinter as tk

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
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro GUI")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)
count_down(5)

start_btn = tk.Button(text="Start", highlightthickness=0)
start_btn.grid(column=0, row=3)

reset_btn = tk.Button(text="Reset", highlightthickness=0)
reset_btn.grid(column=3, row=3)

check_mrk = tk.Label(text="✅", fg=GREEN, bg=YELLOW)
check_mrk.grid(column=1, row=3, pady=20)

window.mainloop()
