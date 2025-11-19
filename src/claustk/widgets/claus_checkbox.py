import tkinter as tk


class ClausCheckbox(tk.Checkbutton):
    def __init__(self, master, **kwargs):
        defaults = {
            "bg": master.avg_color,
            "fg": master.contrast_color,
            "text": "ClausCheckBox",
            "font": ("Arial, 11"),
            "highlightthickness": 0,
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
