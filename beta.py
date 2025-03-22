import tkinter as tk
import tkinter.messagebox


def pop_up_message(header, info):
    tkinter.messagebox.showinfo(header, info)


def click_on_search():
    f = open('database.txt', 'r', encoding="utf-8")
    database = []
    # add each line as a list of fields in list
    for line in f:
        line = line.rstrip("\n")
        line_list = line.split(';')
        database.append(line_list)
    entry_title = title_entry.get().lower()
    entry_author = author_entry.get().lower()
    entry_isbn = isbn_entry.get().lower()
    entry_type = type_entry.get().lower()

    count = 0
    # loop through entries and see if search requests match up with database information
    for item in database:
        for field in item:
            if entry_title in field.lower() and entry_title != '':
                result_index = database.index(item)
                result_list = database[result_index]
                result_string = f"{result_list[0]}\n {result_list[1]}\n {result_list[2]}\n {result_list[3]}"
                pop_up_message("results", result_string)
                break
            if entry_author in field.lower() and entry_author != '':
                result_index = database.index(item)
                result_list = database[result_index]
                result_string = f"{result_list[0]}\n {result_list[1]}\n {result_list[2]}\n {result_list[3]}"
                pop_up_message("results", result_string)
                break
            if entry_isbn in field.lower() and entry_isbn != '':
                result_index = database.index(item)
                result_list = database[result_index]
                result_string = f"{result_list[0]}\n {result_list[1]}\n {result_list[2]}\n {result_list[3]}"
                pop_up_message("results", result_string)
                break
            if entry_type in field.lower() and entry_type != '':
                result_index = database.index(item)
                result_list = database[result_index]
                result_string = f"{result_list[0]}\n {result_list[1]}\n {result_list[2]}\n {result_list[3]}"
                pop_up_message("results", result_string)
                break
            if True:
                count += 1
            # possible improvement: don't find a match if some information but not all matches with database information
    if count == (len(database)*4):
        pop_up_message("message", "Couldn't find this item")  # better way to do this??
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
    # get entries and put them together in file format
    item_new = f"title: {entry_title}; author: {entry_author}; isbn: {entry_isbn}; type: {entry_type}\n"
    database.append(item_new)
    output = "\n".join(database)
    f.close()
    # open file again and write the output (database list with added item)
    add = open('database.txt', 'w', encoding="utf-8")
    add.write(output)
    pop_up_message("message", "successfully added!")
    add.close()


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


# possible improvement: add third option to edit an entry


window = tk.Tk()
window.title("Library")
window.geometry("210x350")

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


window.mainloop()
