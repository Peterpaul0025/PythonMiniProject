import tkinter as tk

# Function to update expression in the text entry box
def press(num):
    entry.insert(tk.END, num)

# Function to evaluate the final expression
def equalpress():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Main window
w = tk.Tk()
w.title("Calculator")
w.resizable(False, False)

# Entry field
entry = tk.Entry(w, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(w, text=text, height=2, width=8, font=("Arial", 16), 
                  command=equalpress).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(w, text=text, height=2, width=8, font=("Arial", 16),
                  command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(w, text='C', height=2, width=35, font=("Arial", 16), command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# Run the GUI
w.mainloop()
