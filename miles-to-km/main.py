import tkinter as tk


def convert_miles_to_km() -> None:
    """Converts the value in miles_entry to kilometers and updates the result_label"""
    miles: float = float(miles_entry.get())
    km: float = miles * 1.609
    if miles_entry.get() != " ":
        result_label.config(text=f"{km:.2f}")


# Create the main window
root: tk.Tk = tk.Tk()
root.title("Miles to Km converter")
root.config(padx=20, pady=20)

# Create the input and output widgets
miles_entry: tk.Entry = tk.Entry(width=7, fg="gray")
miles_entry.insert(0, "")
miles_entry.grid(column=1, row=0)

is_equal_label: tk.Label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result_label: tk.Label = tk.Label(text="0")
result_label.grid(column=1, row=1)

miles_label: tk.Label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label: tk.Label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

# Create the button to trigger the conversion
calculate_button: tk.Button = tk.Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

# Start the main event loop
root.mainloop()
