import tkinter as tk


class ClausMenu(tk.Menu):
    def __init__(self, master, **kwargs):
        toplevel = master.winfo_toplevel()
        widget = toplevel if isinstance(toplevel, (tk.Tk, tk.Toplevel)) else master
        bg, fg = None, None

        if widget == toplevel:
            try:
                bg = master.avg_color
                fg = master.contrast_color
            except Exception:
                pass

        if widget == master:
            try:
                bg = widget["bg"]
                fg = widget["fg"]
            except Exception:
                pass

        defaults = {"bg": bg, "fg": fg, "font": ("Arial, 11"), "tearoff": 0}
        defaults.update(kwargs)

        super().__init__(widget, **defaults)

        if widget == toplevel:
            try:
                widget.config(menu=self)
            except Exception:
                pass
