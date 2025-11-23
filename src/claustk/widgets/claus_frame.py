import os
import sys
import tkinter as tk

from PIL import Image, ImageFilter, ImageTk


def _resource(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class ClausFrame(tk.Canvas):
    def __init__(
        self, master, background: str = "christmas_trees", bg_fragmentation: int = 3, bg_blur: int = 0, **kwargs
    ):
        super().__init__(master, **kwargs)

        if isinstance(master, (tk.Tk, tk.Toplevel)):
            self.configure(highlightthickness=0)
            self.pack(fill="both", expand=True)
        else:
            self.configure(highlightthickness=1, highlightbackground="white", highlightcolor="white")

        _background = Image.open(_resource(f"assets/{background}.png"))

        if bg_blur > 0:
            _background = _background.filter(ImageFilter.GaussianBlur(radius=bg_blur))

        self._background = _background.resize(
            (int(_background.width / bg_fragmentation), int(_background.height / bg_fragmentation))
        )
        self._background_tk = ImageTk.PhotoImage(self._background)

        self.avg_color = self._average_color(self._background)
        self.contrast_color = self._contrast_color_from_avg(self.avg_color)

        self.bind("<Configure>", self._tile_background)

    def _tile_background(self, event):
        self.delete("bg")
        w, h = event.width, event.height
        tw, th = self._background_tk.width(), self._background_tk.height()

        for x in range(0, w, tw):
            for y in range(0, h, th):
                self.create_image(x, y, image=self._background_tk, anchor="nw", tags="bg")

    def _average_color(self, img: Image.Image):
        small_img = img.resize((50, 50))
        pixels = list(small_img.getdata())
        r = sum(p[0] for p in pixels) // len(pixels)
        g = sum(p[1] for p in pixels) // len(pixels)
        b = sum(p[2] for p in pixels) // len(pixels)
        return f"#{r:02x}{g:02x}{b:02x}"

    def _contrast_color_from_avg(self, hex_color: str):
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        luminance = 0.299 * r + 0.587 * g + 0.114 * b

        return "black" if luminance > 128 else "white"
