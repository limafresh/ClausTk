import tkinter as tk


class ClausSlider(tk.Scale):
    def __init__(self, master, **kwargs):
        defaults = {
            "bg": master.avg_color,
            "fg": master.contrast_color,
            "font": ("Arial", 11),
            "highlightthickness": 0,
            "orient": "horizontal",
            "troughcolor": "white",
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
