import tkinter as tk

def button_click(symbol):
    if symbol == 'Clear':
        entry.delete(0, tk.END)
    elif symbol == '=':
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    else:
        entry.insert(tk.END, symbol)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '+'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '*'),
    ('0', '.', '=', '/'),
    ('Clear',)
]

button_colors = {
    '+': 'orange',
    '-': 'orange',
    '*': 'orange',
    '/': 'orange',
    '=': 'green',
    'Clear': 'red',
}

row_index = 1

for row in buttons:
    col_index = 0
    for symbol in row:
        color = button_colors.get(symbol, 'yellow')
        btn = tk.Button(root, text=symbol, padx=40, pady=20, bg=color,
                        command=lambda s=symbol: button_click(s))
        btn.grid(row=row_index, column=col_index, padx=5, pady=5)
        col_index += 1
    row_index += 1

root.mainloop()
