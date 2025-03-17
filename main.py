import tkinter as tk

# build window
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

# open window
window.mainloop()
