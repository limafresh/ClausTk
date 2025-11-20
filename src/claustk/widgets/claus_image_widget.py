import tkinter as tk

from PIL import Image, ImageTk


class ClausImageWidget(tk.Canvas):
    def __init__(self, master, image_path: str, image_size=1, **kwargs):
        super().__init__(master, highlightthickness=0, **kwargs)

        self.load_image(image_path, image_size)

    def load_image(self, image_path, image_size):
        self.delete("all")

        _image = Image.open(image_path)

        self._image = _image.resize((int(_image.width * image_size), int(_image.height * image_size)))

        self.configure(width=self._image.width, height=self._image.height)

        self._image_tk = ImageTk.PhotoImage(self._image)
        self.create_image(0, 0, image=self._image_tk, anchor="nw")
