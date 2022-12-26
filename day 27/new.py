import string
from tkinter import *
wn=Tk()
wn.title("Tkinter Gui")
wn.minsize(width=600,height=600)
wn.config(padx=20,pady=20)

entry=Entry(width=40)
entry.insert(END,string="write sthg")
entry.grid(row=1,column=2)

txt_box=Text(height=10,width=20)
txt_box.focus()
txt_box.insert(END,"Write it")
txt_box.grid(row=0,column=3)

def scale_used(value):
    print(value)
scale=Scale(from_=0,to=100,command=scale_used)
scale.grid(row=1,column=0)

spinbox=Spinbox(from_=0,to=10,width=5)
spinbox.grid(row=1,column=2)

check_box=Checkbutton(text="is ticked")
check_box.grid(row=9,column=5)


# radiobutton1=Radiobutton(text="Opt 1",value=1)
# radiobutton2=Radiobutton(text="Opt 2",value=2)
# radiobutton1.pack()
# radiobutton2.pack()

# list_box=Listbox(width=20)
# alphas=["a","b","c","d"]
# for item in alphas:
#     list_box.insert(alphas.index(item),item)
# list_box.pack()

wn.mainloop()