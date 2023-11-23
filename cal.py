import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
app = tk.Tk()
app.title("Calculator")

# Entry widget for input/output
entry = tk.Entry(app, width=16, font=('Arial', 18), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(app, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda btn=button: on_button_click(btn) if btn != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(app, text='C', padx=20, pady=20, font=('Arial', 14), command=clear_entry).grid(row=row_val, column=col_val, columnspan=2)

# Run the app
app.mainloop()
