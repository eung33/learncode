# -*- coding: utf-8 -*-

# import libraries
import tkinter as tk

# create and start main gui
gui = tk.Tk()
gui.title('My GUI Calculator')


# define functions

# create entry box
entry_box = tk.Entry(gui, width=50, borderwidth=5)
entry_box.grid(row=0,column=0,columnspan=4, padx=40, pady=1)

#create buttons
button_1 = tk.Button(gui, text='1',padx=25,pady=15)
button_2 = tk.Button(gui, text='2',padx=25,pady=15)
button_3 = tk.Button(gui, text='3',padx=25,pady=15)
button_4 = tk.Button(gui, text='4',padx=25,pady=15)
button_5 = tk.Button(gui, text='5',padx=25,pady=15)
button_6 = tk.Button(gui, text='6',padx=25,pady=15)
button_7 = tk.Button(gui, text='7',padx=25,pady=15)
button_8 = tk.Button(gui, text='8',padx=25,pady=15)
button_9 = tk.Button(gui, text='9',padx=25,pady=15)


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

# run main gui
gui.mainloop()