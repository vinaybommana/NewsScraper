import os
import json
import tkinter as tk
import sys

sys.path.append(os.path.abspath(os.path.join("..", "Hindu")))

from HinduScraper import HinduScraper

# load configs
working_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join("../configs.json")) as w:
    config_data = json.load(w)


root = tk.Tk()
option = tk.IntVar()

dropdown_option = tk.StringVar()

choices = ['The Hindu', 'NewYork Times']
dropdown_option.set(choices[0])


# 1 latest
# 2 specific
option.set(1)  # latest

welcome_frame = tk.Frame(root, width=600, height=400)
welcome_frame.pack()

welcome_label = tk.Label(welcome_frame, text="Welcome to Editorial Scraper", padx=20)
welcome_label.grid(row=0, column=1)

popup_menu = tk.OptionMenu(welcome_frame, dropdown_option, *choices)
popup_menu.grid(row=3, column=1)

tk.Radiobutton(welcome_frame, text="Latest", padx=20, variable=option,
               value=1).grid(row=4, column=1)
tk.Radiobutton(welcome_frame, text="Specific", padx=20, variable=option,
               value=2).grid(row=5, column=1)


def search_function(*args):
    editorial_text = ""
    editorial_window = tk.Toplevel(root)
    if dropdown_option.get() == 'The Hindu':
        if option.get() == 1:
            # latest editorials
            editorial_text = HinduScraper(config_data['hindu-url'], "l").read_editorials()
        elif option.get() == 2:
            # specific editorials
            pass
        pass
    elif dropdown_option.get() == 'NewYork Times':
        pass
    display = tk.Text(editorial_window, borderwidth=3, relief="sunken", height=100, width=100)
    display.config(font=("Arial", 12), undo=True, wrap='word')
    display.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    # display = tk.Label(editorial_window, text=editorial_text, padx=20, pady=10)
    display.pack()
    display.insert(tk.END, editorial_text)


tk.Button(welcome_frame, text="Go", padx=20,
          command=search_function).grid(row=6, column=1)

root.mainloop()
