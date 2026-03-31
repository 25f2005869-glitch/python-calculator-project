# ============================================
# Calculator PRO (GUI)
# Author: Saloni Tiwari
# Topic: Tkinter + Scientific Calculator
# ============================================

import tkinter as tk
from tkinter import messagebox
import math

# ========================================
# Functions
# ========================================
history = []

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)

        result_var.set(result)
        history.append(f"{expression} = {result}")
        update_history()

    except Exception:
        messagebox.showerror("Error", "Invalid Expression")


def clear():
    entry.delete(0, tk.END)
    result_var.set("")


def add_to_entry(value):
    entry.insert(tk.END, value)


def scientific(func):
    try:
        value = float(entry.get())
        result = func(value)
        result_var.set(result)
        history.append(f"{func.__name__}({value}) = {result}")
        update_history()
    except:
        messagebox.showerror("Error", "Invalid Input")


def update_history():
    history_box.delete(0, tk.END)
    for item in history[-10:]:
        history_box.insert(tk.END, item)


# ========================================
# GUI Setup
# ========================================
root = tk.Tk()
root.title("Calculator PRO")
root.geometry("400x500")

# Entry
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Keyboard Enter support
entry.bind("<Return>", lambda event: calculate())

# Result
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, fg="blue").pack()

# Buttons Frame
frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for i, row in enumerate(buttons):
    for j, val in enumerate(row):
        if val == '=':
            tk.Button(frame, text=val, width=5, height=2,
                      command=calculate).grid(row=i, column=j)
        else:
            tk.Button(frame, text=val, width=5, height=2,
                      command=lambda v=val: add_to_entry(v)).grid(row=i, column=j)

# Clear Button
tk.Button(root, text="Clear", command=clear, bg="red", fg="white").pack(pady=5)

# Scientific Buttons
sci_frame = tk.Frame(root)
sci_frame.pack(pady=5)

tk.Button(sci_frame, text="√", width=5,
          command=lambda: scientific(math.sqrt)).grid(row=0, column=0)

tk.Button(sci_frame, text="sin", width=5,
          command=lambda: scientific(math.sin)).grid(row=0, column=1)

tk.Button(sci_frame, text="cos", width=5,
          command=lambda: scientific(math.cos)).grid(row=0, column=2)

tk.Button(sci_frame, text="log", width=5,
          command=lambda: scientific(math.log)).grid(row=0, column=3)

# History
tk.Label(root, text="History").pack()

history_box = tk.Listbox(root, height=8)
history_box.pack(fill=tk.BOTH, padx=10, pady=5)

# Run
root.mainloop()