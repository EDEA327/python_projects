import tkinter as tk

root = tk.Tk()
root.title("Miles to Km converter")
root.minsize(width=500, height=500)

# entry
entry = tk.Entry(width=40, fg="gray")
entry.insert(0, "0")
entry.grid(column=1, row=0)

# label
is_equal = tk.Label(text="is equal to")
is_equal.grid(column=0, row=1)

result = tk.Label(text="0")
result.grid(column=1, row=1)

miles = tk.Label(text="Miles")
miles.grid(column=2, row=0)

km = tk.Label(text="Km")
km.grid(column=2, row=1)

# button
calculate_button = tk.Button(text="calculate")

root.mainloop()
