from tkinter import *

FONT = ("Arial", 24)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


def button_clicked():
    km = float(input.get()) * 1.609
    result_label.config(text=f"{km}")

# Label


mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)

# Entry

input = Entry(width=10)
input.grid(column=1, row=0)

# Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
