from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(user_input.get())
    km = miles * 1.6
    result_label.config(text=f"{km}")


user_input = Entry(width=7)
user_input.grid(row=0, column=1)

miles_label = Label(text="miles")
miles_label.grid(row=0, column=2)


equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

kilometer_label = Label(text="kilometers")
kilometer_label.grid(row=1, column=2)


calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(row=2, column=1)


window.mainloop()
