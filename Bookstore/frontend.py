from tkinter import *
from Bookstore import backend

def clear_entries():
    e1_title.delete(0, END)
    e2_year.delete(0, END)
    e3_author.delete(0, END)
    e4_ISBN.delete(0, END)
    lb.delete(0,END)

def view():
    lb.delete(0,END)
    for i in backend.view():
        lb.insert(END,i)

def insert():
    backend.insert(int(ISBN.get()),title.get(), author.get(), int(year.get()))
    lb.delete(0, END)
    lb.insert(END, "ENTRY RECORD INSERTED SUCCESSFULLY")
    lb.insert(2,"ISBN = {}, Title = {}, Author= {}, Year = {} ".format(ISBN.get(),title.get(), author.get(),year.get()))
    e1_title.delete(0, END)
    e2_year.delete(0, END)
    e3_author.delete(0, END)
    e4_ISBN.delete(0, END)

def search():
    lb.delete(0, END)
    for row in backend.search(title.get(),author.get(),year.get(),ISBN.get()):
        lb.insert(END,row)

def update():
    e2_year.insert(0,'0')
    lb.delete(0,END)
    backend.update(int(ISBN.get()),title.get(),author.get(),int(year.get()))
    e2_year.delete(0,END)
    lb.insert(END,"RECORD UPDATED SUCCESSFULLY")

def delete():
    lb.delete(0,END)
    backend.delete(int(ISBN.get()))
    lb.insert(END,"RECORD DELETED SUCCESSFULLY")


window = Tk()
window.title("BookStore")

# Describing lables
l1_title = Label(window,text = 'Title')
l1_title.grid(row=0,column=0)

l2_year = Label(window,text ='Year' )
l2_year.grid(row=1,column=0)

l3_author = Label(window,text ='Author' )
l3_author.grid(row=0,column=2)

l4_ISBN = Label(window,text = 'ISBN')
l4_ISBN.grid(row=1,column=2)

# Describing entries
title= StringVar()
e1_title = Entry(window, textvariable=title)
e1_title.grid(row=0, column=1)

year= StringVar()
e2_year = Entry(window, textvariable=year)
e2_year.grid(row=1, column=1)

author= StringVar()
e3_author = Entry(window, textvariable=author)
e3_author.grid(row=0, column=3)

ISBN= StringVar()
e4_ISBN = Entry(window, textvariable=ISBN)
e4_ISBN.grid(row=1, column=3)

# Describing ListBox
lb = Listbox(window,width=35,height=10)
lb.grid(row=3,column = 0,rowspan=5,columnspan=2)

# Describing scrollBars
sby = Scrollbar(window,orient="vertical")
sby.grid(row=3,column=2,ipady=50,rowspan=5)
sbx = Scrollbar(window,orient = "horizontal")
sbx.grid(row=8,column =0,columnspan=2,ipadx=80)

# Configuring Listbox and Scrollbars
lb.configure(yscrollcommand=sby.set,xscrollcommand=sbx.set)
sby.configure(command=lb.yview)
sbx.configure(command=lb.xview)


# Describing Buttons
b0_clear = Button(window,text='CLEAR All',width=15,command= clear_entries)
b0_clear.grid(row=2,column=3)

b1_view = Button(window,text='VIEW All',width=15,command= view)
b1_view.grid(row=3,column=3)

b2_search = Button(window,text='SEARCH',width=15,command= search)
b2_search.grid(row=4,column=3)

b3_add = Button(window,text='INSERT RECORD',width=15,command = insert)
b3_add.grid(row=5,column=3)

b4_update = Button(window,text='UPDATE RECORD',width=15, command = update)
b4_update.grid(row=6,column=3)

b5_delete = Button(window,text='DELETE RECORD',width=15,command = delete)
b5_delete.grid(row=7,column=3)

b6_close = Button(window,text='CLOSE',width=15,command= window.destroy)
b6_close.grid(row=8,column=3)

window.mainloop()

