import os
import sys
import tempfile
import tkinter as tk

from PIL import Image

from .claus_frame import ClausFrame


def _resource(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class ClausWindow(ClausFrame):
    def __init__(self, **kwargs):
        self._master = tk.Tk()
        self._master.title("ClausWindow")

        super().__init__(self._master, **kwargs)
        self.pack(fill="both", expand=True)

        self.seticon(_resource("assets/icon.png"))

    def seticon(self, file_path: str):
        if os.name == "nt":
            img = Image.open(file_path)

            fd, ico_path = tempfile.mkstemp(suffix=".ico")
            os.close(fd)

            img.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (256, 256)])

            self._master.iconbitmap(ico_path)
            os.remove(ico_path)
        else:
            self._master.iconphoto(True, tk.PhotoImage(file=file_path))

    def happynewyear(self):
        self._master.mainloop()

    def __getattr__(self, name):
        return getattr(self._master, name)
