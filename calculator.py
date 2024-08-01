import tkinter as tk

# Function to update the input field
def update_expression(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')

# Function to clear the input field
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for the input
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

# Create and place buttons
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=evaluate_expression)
    elif button == '.':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: update_expression(b))
    elif button == 'C':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=clear_entry)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: update_expression(b))
    
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create and place clear button
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear_entry)
clear_button.grid(row=row_val, column=col_val, columnspan=4)

# Run the application
root.mainloop()
