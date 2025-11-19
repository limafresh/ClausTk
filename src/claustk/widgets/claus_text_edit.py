import tkinter as tk


class ClausTextEdit(tk.Text):
    def __init__(self, master, **kwargs):
        defaults = {
            "width": 40,
            "height": 5,
            "font": ("Arial, 11"),
            "highlightthickness": 0,
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
