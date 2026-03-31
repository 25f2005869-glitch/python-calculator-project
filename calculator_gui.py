# ============================================
# Calculator (GUI Version)
# Author: Saloni Tiwari
# Topic: Tkinter + Functions
# ============================================

import tkinter as tk
from tkinter import messagebox

# ========================================
# Functions
# ========================================
def add():
    calculate(lambda x, y: x + y, "+")

def subtract():
    calculate(lambda x, y: x - y, "-")

def multiply():
    calculate(lambda x, y: x * y, "*")

def divide():
    try:
        calculate(lambda x, y: x / y, "/")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")


def calculate(operation, symbol):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        result = operation(num1, num2)
        result_var.set(f"{num1} {symbol} {num2} = {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")


# ========================================
# GUI Setup
# ========================================
root = tk.Tk()
root.title("Calculator")
root.geometry("350x300")

tk.Label(root, text="Simple Calculator", font=("Arial", 14, "bold")).pack(pady=10)

# Input Fields
tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Add", width=10, command=add).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Subtract", width=10, command=subtract).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Multiply", width=10, command=multiply).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Divide", width=10, command=divide).grid(row=1, column=1, padx=5, pady=5)

# Result
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, fg="blue").pack(pady=10)

# Run App
root.mainloop()