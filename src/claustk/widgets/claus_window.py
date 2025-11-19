import os
import sys
import tempfile
import tkinter as tk

from PIL import Image, ImageTk

from .claus_background_canvas import ClausBackgroundCanvas


def _resource(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class ClausWindow(ClausBackgroundCanvas):
    def __init__(self, background: str = "christmas_trees", bg_fragmentation: int = 3, **kwargs):
        self._master = tk.Tk()
        self._master.title("ClausWindow")
        self._master.geometry("600x400")

        super().__init__(self._master, **kwargs)
        self.pack(fill="both", expand=True)

        _background = Image.open(_resource(f"assets/{background}.png"))
        self._background = _background.resize(
            (int(_background.width / bg_fragmentation), int(_background.height / bg_fragmentation))
        )
        self._background_tk = ImageTk.PhotoImage(self._background)

        self.seticon(_resource("assets/icon.png"))

    def seticon(self, file_path: str):
        if os.name == "nt":
            img = Image.open(file_path)

            fd, ico_path = tempfile.mkstemp(suffix=".ico")
            os.close(fd)

            img.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (256, 256)])

            self._master.iconbitmap(ico_path)
        else:
            self._master.iconphoto(True, tk.PhotoImage(file=file_path))

    def title(self, value: str):
        self._master.title(value)

    def geometry(self, value: str):
        self._master.geometry(value)

    def happynewyear(self):
        self._master.mainloop()

    def cget(self, key):
        if key == "width":
            return self._master.width
        elif key == "height":
            return self._master.height
        else:
            raise KeyError(f"Unknown option: '{key}'")
