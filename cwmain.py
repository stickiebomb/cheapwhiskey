import tkinter as tk

# main
root = tk.Tk()
root.title("cw v0.02")

# icon
root.iconbitmap('pfp (1).ico')

# add text
label = tk.Label(root, text="Oops! You're here early! I'm still working on this.")
label.pack(pady=20)

# run
root.mainloop()
