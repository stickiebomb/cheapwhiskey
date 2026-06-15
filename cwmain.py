import tkinter as tk

# main
root = tk.Tk()
root.title("cw v0.02")

# window size
root.geometry("300x250")

# icon
root.iconbitmap("niko.ico")

# add text
label = tk.Label(
    root,
    text="""Oops! You're here early!
I'm still working on this.
You can close this window now.
This is our official website: cheapwhiskey.straw.page/
We don't currently have anything on it.
Ask me on discord if you want to help with this project!

@officialstickie"""
)
label.pack(pady=50)

# run
root.mainloop()
