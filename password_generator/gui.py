import tkinter as tk
from tkinter import messagebox
from password_module import generate_password, estimate_strength
try:
    import pyperclip
except Exception:
    pyperclip = None

def on_generate():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid", "Length must be an integer")
        return

    try:
        pwd = generate_password(
            length=length,
            use_upper=upper_var.get(),
            use_lower=lower_var.get(),
            use_digits=digits_var.get(),
            use_symbols=symbols_var.get()
        )
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    result_var.set(pwd)
    strength_var.set("Strength: " + estimate_strength(pwd))

def on_copy():
    if not result_var.get():
        messagebox.showerror("Error", "Generate a password first!")
        return

    if pyperclip:
        pyperclip.copy(result_var.get())
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showerror("Error", "pyperclip not installed")

root = tk.Tk()
root.title("Password Generator")
root.geometry("480x230")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Length:").grid(row=0, column=0, sticky="w")
length_entry = tk.Entry(frame, width=6)
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1, sticky="w")

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(frame, text="Upper", variable=upper_var).grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame, text="Lower", variable=lower_var).grid(row=1, column=1, sticky="w")
tk.Checkbutton(frame, text="Digits", variable=digits_var).grid(row=1, column=2, sticky="w")
tk.Checkbutton(frame, text="Symbols", variable=symbols_var).grid(row=1, column=3, sticky="w")

tk.Button(frame, text="Generate", command=on_generate).grid(row=2, column=0, pady=8)
tk.Button(frame, text="Copy", command=on_copy).grid(row=2, column=1, pady=8)

result_var = tk.StringVar(value="")
strength_var = tk.StringVar(value="Strength: -")

tk.Label(frame, textvariable=result_var, font=("Consolas", 12)).grid(row=3, column=0, columnspan=4, pady=(8,0))
tk.Label(frame, textvariable=strength_var).grid(row=4, column=0, columnspan=4, pady=(4,0))

root.mainloop()
