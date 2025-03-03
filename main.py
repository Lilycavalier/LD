import tkinter as tk

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

def on_left_click(event):
    print(f"Left click at ({event.x}, {event.y})")

def on_right_click(event):
    print(f"Right click at ({event.x}, {event.y})")

def on_mouse_motion(event):
    print(f"Mouse moved to ({event.x}, {event.y})")


window = tk.Tk()
window.title("Library")

# create widgets
label = tk.Label(text="Welcome!")

# place widgets
label.place(x=100, y=10)


# window.bind("<KeyPress>", on_key_press)
# window.bind("<Button-1>", on_left_click)
# window.bind("<Button-3>", on_right_click)
# window.bind("<Motion>", on_mouse_motion)

window.mainloop()
