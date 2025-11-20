import tkinter as tk


class ClausRadiobutton(tk.Radiobutton):
    def __init__(self, master, **kwargs):
        defaults = {
            "bg": master.avg_color,
            "fg": master.contrast_color,
            "selectcolor": master.avg_color,
            "text": "ClausRadioButton",
            "font": ("Arial, 11"),
            "highlightthickness": 0,
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
