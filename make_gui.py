import tkinter as tk

root = tk.Tk()
option = tk.IntVar()

option.set(1)  # latest

welcome_frame = tk.Frame(root, width=600, height=400)
welcome_frame.pack()

welcome_label = tk.Label(welcome_frame, text="Welcome to Editorial Scraper", padx=20)
welcome_label.pack(side="top")

tk.Radiobutton(welcome_frame, text="Latest", padx=20, variable=option, value=1).pack(side="top")
tk.Radiobutton(welcome_frame, text="Specific", padx=20, variable=option, value=2).pack(side="top")

print(option.get())

root.mainloop()
