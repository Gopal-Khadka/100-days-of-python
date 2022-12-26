import tkinter
window=tkinter.Tk()
window.title("Hello")
window.minsize(width=600,height=600)

# # label
# my_label=tkinter.Label(text="I am a label",font=("Ubuntu",20,"bold"))
# my_label.pack()
# my_label["text"]="harry xaina"
# my_label.config(text="nope")

# button
def button_click():
    my_label=tkinter.Label(text=input_data.get())
    my_label.pack()
button=tkinter.Button(text="dont click me",command=button_click)
button.pack()

# entry
input_data=tkinter.Entry(width=11)
input_data.pack()



window.mainloop()