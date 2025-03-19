import tkinter as tk


def click_on_search():
    f = open('database.txt', 'r', encoding="utf-8")
    mylist = []
    # add each line as an item (string) in list
    for line in f:
        line = line.rstrip("\n")
        linelist = line.split(';')
        mylist.append(linelist)
    entry_title = title_entry.get().lower()
    entry_author = author_entry.get().lower()
    entry_isbn = isbn_entry.get().lower()
    entry_type = type_entry.get().lower()
    for item in mylist:
        for field in item:
            if entry_title in field.lower() and entry_title != '':
                find = mylist.index(item)
                newstring = mylist[find]
                for i in range(len(newstring)):
                   print(newstring[i])
                break
            if entry_author in field.lower() and entry_author != '':
                find = mylist.index(item)
                newstring = mylist[find]
                for i in range(len(newstring)):
                    print(newstring[i])
                break
            if entry_isbn in field.lower() and entry_isbn != '':
                find = mylist.index(item)
                newstring = mylist[find]
                for i in range(len(newstring)):
                    print(newstring[i])
                break
            if entry_type in field.lower() and entry_type != '':
                find = mylist.index(item)
                newstring = mylist[find]
                for i in range(len(newstring)):
                    print(newstring[i])
                break
            # else:
                # print("Couldn't find this item")  # is not working??
    f.close()


def click_on_add():
    f = open('database.txt', 'r+', encoding="utf-8")
    mylist = []
    # add each line as an item (string) in list
    for line in f:
        line = line.rstrip("\n")
        mylist.append(line)
    entry_title = title_entry.get().lower()
    entry_author = author_entry.get().lower()
    entry_isbn = isbn_entry.get().lower()
    entry_type = type_entry.get().lower()
    newitem = f"title: {entry_title}; author: {entry_author}; isbn: {entry_isbn}; type: {entry_type}\n"
    # mylist.append(f"title: {entry_title}; author: {entry_author}; isbn: {entry_isbn}; type: {entry_type}")
    f.write(newitem)  # one line for each item?? how many lines??
    f.close()


def click_on_delete():
    f = open('database.txt', 'r+', encoding="utf-8")
    mylist = []
    # add each line as an item (string) in list
    for line in f:
        line = line.rstrip("\n")
        mylist.append(line)
    # delete =  # index that all entries apply to??
    # del mylist[delete]
    f.write(str(mylist))  # one line for each item?? how many lines??
    f.close()


window = tk.Tk()
window.title("Library")
window.geometry("200x350")

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
add_button = tk.Button(window, text='Add Entry', width=16, command=lambda: click_on_add())
delete_button = tk.Button(window, text='Delete Entry', width=16, command=lambda: click_on_delete())
search_button = tk.Button(window, text='Search', width=16, command=lambda: click_on_search())
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



"""
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
"""

window.mainloop()
