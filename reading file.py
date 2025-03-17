import tkinter as tk

def click_on_search(event):
    if entry_title in titles:  # combine all entries and check if in database??
        find =  # index that all entries apply to??
        newstring = mylist[find].split(';')
        for i in range(len(newstring)):
            print(newstring[i])  # indented??
    else:
        print("Couldn't find this item")

def click_on_add(event):
    mylist.append(f"title: {entry_title}; author: {author_entry}; isbn: {isbn_entry}; type: {type_entry}")
    f.write(mylist)  # one line for each item?? how many lines??

def click_on_delete(event):
    delete =  # index that all entries apply to??
    del mylist[delete]
    f.write(mylist)  # one line for each item?? how many lines??


window = tk.Tk()
window.title("Library")

# create widgets
header = tk.Label(text="Welcome!")
title_label = tk.Label(text="Title:")
title_entry = tk.Entry()
author_label = tk.Label(text="Author:")
author_entry = tk.Entry()
isbn_label = tk.Label(text="ISBN:")
isbn_entry = tk.Entry()
type_label = tk.Label(text="Type:")
type_entry = tk.Entry()
add_button = tk.Button(window, text='Add Entry', width=16)
delete_button = tk.Button(window, text='Delete Entry', width=16)
search_button = tk.Button(window, text='Search', width=16)
exit_button = tk.Button(window, text='Exit', width=16, command=window.destroy)

# place widgets
header.place(x=70, y=10)
title_label.place(x=10, y=40)
title_entry.place(x=55, y=40)
author_label.place(x=10, y=70)
author_entry.place(x=55, y=70)
isbn_label.place(x=10, y=100)
isbn_entry.place(x=55, y=100)
type_label.place(x=10, y=130)
type_entry.place(x=55, y=130)
add_button.place(x=40, y=180)
delete_button.place(x=40, y=220)
search_button.place(x=40, y=260)
exit_button.place(x=40, y=300)

search_button.bind("<Button-1>", click_on_search())
add_button.bind("<Button-1>", click_on_add())
delete_button.bind("<Button-1>", click_on_delete())

with open('database.txt', 'r+', encoding="utf-8") as f:
    mylist = []
    # add each line as an item (string) in list
    for line in f:
        line = line.rstrip("\n")
        mylist.append(line)
    titles = []
    authors = []
    isbns = []
    types = []
    try:
        for i in range(len(mylist)):
            titles.append(mylist[i].split(';')[0])
            authors.append(mylist[i].split(';')[1])
            isbns.append(mylist[i].split(';')[2])
            types.append(mylist[i].split(';')[3])
    except:
        pass
    entry_title = title_entry.get().lower()
    entry_author = author_entry.get().lower()
    entry_isbn = isbn_entry.get().lower()
    entry_type = type_entry.get().lower()

window.mainloop()
