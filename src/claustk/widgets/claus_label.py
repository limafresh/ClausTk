import tkinter as tk


class ClausLabel(tk.Label):
    def __init__(self, master, **kwargs):
        defaults = {
            "bg": master.avg_color,
            "fg": master.contrast_color,
            "text": "ClausLabel",
            "font": ("Arial, 11"),
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
