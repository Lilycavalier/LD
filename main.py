import tkinter as tk

def click_on_search(event):  # event??
    entry = entry.get()  # from all four entries??
    string = "\n".join(s for s in mylist if entry.lower() in s.lower())
    newstring = string.split(';')
    for i in range(len(newstring)):
        print(newstring[i])  # indented??
    if any(entry in sub for sub in mylist) is False:
        print("Couldn't find this item")
        check = input("Do you want to add it to the database?")



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


# window.bind("<KeyPress>", on_key_press)
# entry.bind("<Button-1>", self.delete(0, end))
# search_button.bind("<Button-1>", click_on_search())
# window.bind("<Button-3>", on_right_click)
# window.bind("<Motion>", on_mouse_motion)

with open('database.txt', 'r', encoding="utf-8") as f:
    mylist = []
    # add each line as an item (string) in list
    for line in f:
        line = line.rstrip("\n")
        mylist.append(line)
    # item1 = lst[0].split(';')
    # print(item1)



window.mainloop()
