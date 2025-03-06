import tkinter as tk

def click_on_search(event):
    print(f"Key pressed: {event.keysym}")

def click_on_field(self, end):
    self.delete(0, end)



window = tk.Tk()
window.title("Library")

# create widgets
header = tk.Label(text="Welcome!")
search_label = tk.Label(text="Search:")
entry = tk.Entry(width=30)
placeholder = "search for name, author, isbn, or type"
entry.insert(0, placeholder)
# author_label = tk.Label(text="Author:")
# author_entry = tk.Entry()
# isbn_label = tk.Label(text="ISBN:")
# isbn_entry = tk.Entry()
# type_label = tk.Label(text="Type:")
# type_entry = tk.Entry()
search_button = tk.Button(window, text='Search', width=10)
exit_button = tk.Button(window, text='Exit', width=10, command=window.destroy)

# place widgets
header.place(x=95, y=10)
search_label.place(x=10, y=40)
entry.place(x=55, y=40)
# author_label.place(x=10, y=70)
# author_entry.place(x=55, y=70)
# isbn_label.place(x=10, y=100)
# isbn_entry.place(x=55, y=100)
# type_label.place(x=10, y=130)
# type_entry.place(x=55, y=130)
search_button.place(x=40, y=70)
exit_button.place(x=130, y=70)


# window.bind("<KeyPress>", on_key_press)
entry.bind("<Button-1>", click_on_field(entry, len(placeholder)))
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
