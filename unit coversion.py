import tkinter as tk
from tkinter import ttk

def convert():
    value = float(entry.get())
    unit = combo_var.get()

    if unit == "Centimeter to Feet":
        result = value / 30.48
    elif unit == "Feet to Inches":
        result = value * 12
    elif unit == "Square Feet to Square Meters":
        result = value * 0.092903
    elif unit == "Square Feet to Hectares":
        result = value * 0.0000092903
    elif unit == "Square Feet to Acres":
        result = value * 0.0000229568
    else:
        result = "Invalid conversion"

    result_label.config(text=f"Result: {result:.4f} {unit.split()[-1]}")

# Create the main window
window = tk.Tk()
window.title("Unit Converter")
window.configure(bg="#ADD8E6")

# Create and configure the entry widget
entry = ttk.Entry(window, width=15)
entry.grid(row=0, column=0, padx=10, pady=10)

# Create and configure the combo box
units = ["Centimeter to Feet", "Feet to Inches", "Square Feet to Square Meters",
         "Square Feet to Hectares", "Square Feet to Acres"]
combo_var = tk.StringVar(value=units[0])
unit_combo = ttk.Combobox(window, textvariable=combo_var, values=units)
unit_combo.grid(row=0, column=1, padx=10, pady=10)

# Create and configure the convert button
convert_button = ttk.Button(window, text="Convert", command=convert)
convert_button.grid(row=0, column=2, padx=10, pady=10)

# Create and configure the result label
result_label = ttk.Label(window, text="Result: ")
result_label.grid(row=1, column=0, columnspan=3, pady=10)

# Run the Tkinter event loop
window.mainloop()
