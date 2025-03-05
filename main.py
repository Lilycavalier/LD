import tkinter as tk

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

def on_left_click(event):
    print(f"Left click at ({event.x}, {event.y})")

def on_right_click(event):
    print(f"Right click at ({event.x}, {event.y})")

def on_mouse_motion(event):
    print(f"Mouse moved to ({event.x}, {event.y})")


# window = tk.Tk()
# window.title("Library")

# create widgets
# header = tk.Label(text="Welcome!")
# title_label = tk.Label(text="Title:")
# title_entry = tk.Entry()
# author_label = tk.Label(text="Author:")
# author_entry = tk.Entry()
# isbn_label = tk.Label(text="ISBN:")
# isbn_entry = tk.Entry()
# type_label = tk.Label(text="Type:")
# type_entry = tk.Entry()
# exit_button = tk.Button(window, text='Exit', width=16, command=window.destroy)

# place widgets
# header.place(x=70, y=10)
# title_label.place(x=10, y=40)
# title_entry.place(x=55, y=40)
# author_label.place(x=10, y=70)
# author_entry.place(x=55, y=70)
# isbn_label.place(x=10, y=100)
# isbn_entry.place(x=55, y=100)
# type_label.place(x=10, y=130)
# type_entry.place(x=55, y=130)
# exit_button.place(x=40, y=160)


# window.bind("<KeyPress>", on_key_press)
# window.bind("<Button-1>", on_left_click)
# window.bind("<Button-3>", on_right_click)
# window.bind("<Motion>", on_mouse_motion)

with open('database.txt', 'r', encoding="utf-8") as f:
    lst = []
    for line in f:
        line = line.rstrip("\n")
        lst =+ lst

# window.mainloop()
