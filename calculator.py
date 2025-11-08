"""
Pastel Calculator (Smart Input + Original Colors)
-------------------------------------------------
Author: Elaheh Akbarian
Created: 2025-11-08
-------------------------------------------------
Features:
- Basic operations: +, -, *, /
- Pretty GUI with soft pastel theme (blue, pink, green)
- Smart input: no double operators or multiple dots
- Shows result in an entry field
- Displays "Error" for invalid input or division by zero
-------------------------------------------------
Requires: Python 3.x, Tkinter
"""

import tkinter as tk

# --- Original Pastel Theme Colors ---
BG_COLOR = "#f8f9fa"          # Light background
BTN_NUM_COLOR = "#dbe7f0"     # Soft blue for numbers
BTN_OP_COLOR = "#f7d9d9"      # Light pink for operators
BTN_EQ_COLOR = "#d9f7dc"      # Light green for equal button
BTN_CLEAR_COLOR = "#f2c6c6"   # Slightly darker pink for clear
TEXT_COLOR = "#333333"
ENTRY_BG = "#ffffff"

# --- Functions ---

def on_click(value):
    current = entry.get()

    # Prevent two operators in a row
    if value in '+-*/':
        if not current or current[-1] in '+-*/':
            return

    # Prevent multiple dots in the same number
    if value == '.':
        parts = current.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()
        last_num = parts[-1] if parts else ''
        if '.' in last_num:
            return

    entry.insert(tk.END, value)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        expression = entry.get()
        if expression and expression[-1] in '+-*/':
            expression = expression[:-1]
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# --- Main window ---
root = tk.Tk()
root.title("Pastel Calculator")
root.config(bg=BG_COLOR)
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), bd=5, justify="right", bg=ENTRY_BG, fg=TEXT_COLOR)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# --- Buttons layout ---
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=34, height=2, bg=BTN_EQ_COLOR, fg=TEXT_COLOR,
                        font=("Arial", 14, "bold"), command=calculate)
        btn.grid(row=row, column=col, columnspan=4, padx=5, pady=8)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=7, height=2, bg=BTN_CLEAR_COLOR, fg=TEXT_COLOR,
                        font=("Arial", 14), command=clear)
        btn.grid(row=row, column=col, padx=5, pady=5)
    else:
        color = BTN_NUM_COLOR if text.isdigit() or text == '.' else BTN_OP_COLOR
        btn = tk.Button(root, text=text, width=7, height=2, bg=color, fg=TEXT_COLOR,
                        font=("Arial", 14), command=lambda t=text: on_click(t))
        btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()