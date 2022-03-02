# Приложение Сапер сделано по мотивам https://www.youtube.com/watch?v=nWjrZtskIWs часть первая
import tkinter as tk

ROWS = 15
COLUMNS = 7

# создание окна средствами tkinter
window = tk.Tk()

buttons = []
for row_count in range(ROWS):
    temp = []
    for columns_count in range(COLUMNS):
        btn = tk.Button(window, width=3, font='calibre 15 bold')
        temp.append(btn)
    buttons.append(temp)

for row_count in range(ROWS):
    for columns_count in range(COLUMNS):
        btn = buttons[row_count][columns_count]
        btn.grid(row=row_count, column=columns_count)

window.mainloop()  #
