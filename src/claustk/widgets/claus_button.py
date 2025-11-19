import tkinter as tk


class ClausButton(tk.Button):
    def __init__(self, master, **kwargs):
        defaults = {
            "bg": "green",
            "fg": "white",
            "text": "ClausButton",
            "font": ("Arial", 11),
            "highlightthickness": 0,
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
