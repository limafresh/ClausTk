import tkinter as tk


class ClausLineEdit(tk.Entry):
    def __init__(self, master, **kwargs):
        defaults = {
            "font": ("Arial", 11),
            "highlightthickness": 0,
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
