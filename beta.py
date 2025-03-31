import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

'''
This version is a little more advanced than the requirements of the assignment.
It allows you to also edit entries.
'''


def pop_up_message(subject, info):
    tkinter.messagebox.showinfo(subject, info)


def click_on_search():
    f = open('database.txt', 'r', encoding="utf-8")
    database = []
    # add each line as a list of fields in list (without the label!!)
    for line in f:
        line = line.rstrip("\n")
        line_list = line.split(';')
        line_list_stripped = []
        for item in line_list:
            ix = item.index(":") + 2
            item = item[ix:len(item)]
            line_list_stripped.append(item)
        database.append(line_list_stripped)
    entry_title = title_entry.get().lower()
    entry_author = author_entry.get().lower()
    entry_isbn = isbn_entry.get().lower()
    entry_type = type_entry.get().lower()

    count = 0
    # loop through entries and see if search requests match up with database information
    for item in database:
            if entry_title in item[0].lower() or entry_title == '':
                tt = "match"
                if entry_author in item[1].lower() or entry_author == '':
                    au = "match"
                    if entry_isbn in item[2].lower() or entry_isbn == '':
                        ib = "match"
                        if entry_type in item[3].lower() or entry_type == '':
                            tp = "match"
                        else:
                            tp = ""
                    else:
                        ib = ""
                else:
                    au = ""
            else:
                tt = ""
            if tt == "match" and au == "match" and ib == "match" and tp == "match":
                result_index = database.index(item)
                result_list = database[result_index]
                result_string = f"title: {result_list[0]}\n author: {result_list[1]}\n isbn: {result_list[2]}\n type: {result_list[3]}"
                pop_up_message("results", result_string)
            else:
                count += 1
    if count == (len(database)):
        pop_up_message("message", "Couldn't find this item")
    f.close()


def click_on_add():
    f = open('database.txt', 'r+', encoding="utf-8")
    database = []
    # add each line as a list of fields in list
    for line in f:
        line = line.rstrip("\n")
        database.append(line)
    entry_title = title_entry.get().lower()
    entry_author = author_entry.get().lower()
    entry_isbn = isbn_entry.get().lower()
    entry_type = type_entry.get().lower()
    # get entries and put them together in file format (if item not already in database)
    if f"title: {entry_title}; author: {entry_author}; isbn: {entry_isbn}; type: {entry_type}" not in database:
        item_new = f"title: {entry_title}; author: {entry_author}; isbn: {entry_isbn}; type: {entry_type}\n"
        database.append(item_new)
        output = "\n".join(database)
        f.close()
        # open file again and write the output (database list with added item)
        add = open('database.txt', 'w', encoding="utf-8")
        add.write(output)
        pop_up_message("message", "successfully added!")
        add.close()
    else:
        pop_up_message("message", "item is already in database")
        f.close()


def click_on_delete():
    f = open('database.txt', 'r', encoding="utf-8")
    database = []
    # add each line as an item (string) in list
    for line in f:
        line = line.rstrip("\n")
        database.append(line)
    entry_title = title_entry.get().lower()
    entry_author = author_entry.get().lower()
    entry_isbn = isbn_entry.get().lower()
    entry_type = type_entry.get().lower()
    try:
        # find item in database that user wants to delete
        for item in database:
            if entry_title in item and entry_author in item and entry_isbn in item and entry_type in item:
                delete = database.index(item)
                break
        del database[delete]
        output = "\n".join(database)
        f.close()
        # open file again and write the output (database list without deleted item)
        delete = open('database.txt', 'w', encoding="utf-8")
        delete.write(output)
        pop_up_message("message", "successfully deleted!")
        delete.close()
    except:
        pop_up_message("message", "this item is not in the library")


def click_on_edit():
    f = open('database.txt', 'r', encoding="utf-8")
    database = []
    # add each line as a list of fields in list (without the label!!)
    for line in f:
        line = line.rstrip("\n")
        line_list = line.split(';')
        line_list_stripped = []
        for item in line_list:
            ix = item.index(":") + 2
            item = item[ix:len(item)]
            line_list_stripped.append(item)
        database.append(line_list_stripped)
    # improvement: if entry left blank don't make any changes

    def open_new_window(data):
        # Toplevel object which will be treated as a new window
        window = tk.Toplevel(main)
        # sets the title of the Toplevel widget
        window.title("")
        # sets the geometry of toplevel
        window.geometry("280x280")

        def select(win, box, e1, e2, e3, e4):
            f = open('database.txt', 'r', encoding="utf-8")
            database = []
            # add each line as an item (string) in list
            for line in f:
                line = line.rstrip("\n")
                database.append(line)
            # delete this entry from the list
            del database[box]
            # get new entries and put them together in file format
            item_new = f"title: {e1}; author: {e2}; isbn: {e3}; type: {e4}\n"
            database.append(item_new)
            output = "\n".join(database)
            # open file and write the output (database list with edited item)
            edit = open('database.txt', 'w', encoding="utf-8")
            edit.write(output)
            pop_up_message("message", "successfully edited!")
            edit.close()
            win.destroy()

        text = tk.Label(window, text="Please select the entry you want to edit!")
        combo_box = ttk.Combobox(window, width=30, values=data)
        text2 = tk.Label(window, text="Now type in your edits...")
        title_label2 = tk.Label(window, text="Title:")
        title_entry2 = tk.Entry(window)
        author_label2 = tk.Label(window, text="Author:")
        author_entry2 = tk.Entry(window)
        isbn_label2 = tk.Label(window, text="ISBN:")
        isbn_entry2 = tk.Entry(window)
        type_label2 = tk.Label(window, text="Type:")
        type_entry2 = tk.Entry(window)
        select_button = tk.Button(window, text='Edit', width=16,
                                  command=lambda: select(window, combo_box.current(), title_entry2.get(),
                                                         author_entry2.get(), isbn_entry2.get(), type_entry2.get()))

        combo_box.set("Select...")

        text.place(x=30, y=10)
        combo_box.place(x=35, y=40)
        text2.place(x=65, y=70)
        title_label2.place(x=40, y=100)
        title_entry2.place(x=90, y=100)
        author_label2.place(x=40, y=130)
        author_entry2.place(x=90, y=130)
        isbn_label2.place(x=40, y=160)
        isbn_entry2.place(x=90, y=160)
        type_label2.place(x=40, y=190)
        type_entry2.place(x=90, y=190)
        select_button.place(x=70, y=220)
    open_new_window(database)


main = tk.Tk()
main.title("Library")
main.geometry("210x400")

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
add_button = tk.Button(main, text='Add Entry', width=16, command=lambda: click_on_add())
delete_button = tk.Button(main, text='Delete Entry', width=16, command=lambda: click_on_delete())
search_button = tk.Button(main, text='Search', width=16, command=lambda: click_on_search())
exit_button = tk.Button(main, text='Exit', width=16, command=main.destroy)
edit_button = tk.Button(main, text='Edit Entry', width=16, command=lambda: click_on_edit())

# place widgets
header.place(x=75, y=10)
title_label.place(x=10, y=40)
title_entry.place(x=60, y=40)
author_label.place(x=10, y=70)
author_entry.place(x=60, y=70)
isbn_label.place(x=10, y=100)
isbn_entry.place(x=60, y=100)
type_label.place(x=10, y=130)
type_entry.place(x=60, y=130)
add_button.place(x=45, y=180)
delete_button.place(x=45, y=220)
search_button.place(x=45, y=260)
exit_button.place(x=45, y=300)
edit_button.place(x=45, y=340)


main.mainloop()
