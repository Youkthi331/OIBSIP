# gui.py
import tkinter as tk
from tkinter import messagebox
from bmi_module import calculate_bmi, bmi_category

def on_calculate():
    try:
        w = float(weight_entry.get().strip())
        h = float(height_entry.get().strip())
        if w <= 0 or h <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Enter positive numeric values for weight (kg) and height (m).")
        return

    bmi = calculate_bmi(w, h)
    cat = bmi_category(bmi)
    result_var.set(f"BMI: {bmi}  |  {cat}")

def on_clear():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_var.set("BMI: -")

root = tk.Tk()
root.title("BMI Calculator")
root.resizable(False, False)
root.geometry("320x180")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(expand=True, fill="both")

tk.Label(frame, text="Weight (kg)").grid(row=0, column=0, sticky="w", pady=(0,6))
weight_entry = tk.Entry(frame, width=20)
weight_entry.grid(row=0, column=1, pady=(0,6))

tk.Label(frame, text="Height (m)").grid(row=1, column=0, sticky="w", pady=(0,6))
height_entry = tk.Entry(frame, width=20)
height_entry.grid(row=1, column=1, pady=(0,6))

calc_btn = tk.Button(frame, text="Calculate", width=12, command=on_calculate)
calc_btn.grid(row=2, column=0, pady=(8,4))

clear_btn = tk.Button(frame, text="Clear", width=12, command=on_clear)
clear_btn.grid(row=2, column=1, pady=(8,4))

result_var = tk.StringVar(value="BMI: -")
tk.Label(frame, textvariable=result_var, font=("Arial", 10, "bold")).grid(row=3, column=0, columnspan=2, pady=(8,0))

root.mainloop()
