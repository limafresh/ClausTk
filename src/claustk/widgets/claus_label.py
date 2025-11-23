import tkinter as tk
import tkinter.font as tkfont

from PIL import Image, ImageTk


class ClausLabel(tk.Canvas):
    def __init__(
        self,
        master,
        width=150,
        height=30,
        text="ClausLabel",
        font=("Arial", 11),
        justify="center",
        bg_color="transparent",
        fg_color=None,
        cursor="",
        **kwargs,
    ):
        tk.Canvas.__init__(
            self,
            master,
            width=width,
            height=height,
            highlightthickness=0,
            **kwargs,
        )

        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.justify = justify
        self.bg_color = bg_color
        self.fg_color = master.contrast_color if fg_color is None else fg_color
        self.cursor = cursor

        self.delete("all")

        self._create_label()

        self.bind("<Configure>", self._create_bg)

    def _create_bg(self, event=None):
        self.delete("label_bg")

        if self.bg_color == "transparent":
            w, h = self.master.winfo_width(), self.master.winfo_height()
            full_bg = Image.new("RGB", (w, h))
            bw, bh = self.master._background.width, self.master._background.height
            for x in range(0, w, bw):
                for y in range(0, h, bh):
                    full_bg.paste(self.master._background, (x, y))

            x, y, w, h = self.winfo_x(), self.winfo_y(), self.winfo_width(), self.winfo_height()
            cropped = full_bg.crop((x, y, x + w, y + h))
            self.bg_piece = ImageTk.PhotoImage(cropped)

            self.create_image(0, 0, image=self.bg_piece, anchor="nw", tags="label_bg")
            self.tag_lower("label_bg")
        else:
            self.configure(bg=self.bg_color)

    def _create_label(self):
        font_obj = tkfont.Font(font=self.font)
        lines = self.text.split("\n")

        max_width = max(font_obj.measure(line) for line in lines)
        line_height = font_obj.metrics("linespace")
        total_height = line_height * len(lines)

        self.width = max_width + 10
        self.height = total_height + 6
        self.configure(width=self.width, height=self.height)

        self.create_text(
            self.width / 2,
            self.height / 2,
            text=self.text,
            font=self.font,
            fill=self.fg_color,
            tags="label",
            anchor="center",
            justify=self.justify,
        )

        self.configure(cursor=self.cursor)

    def config(self, **kwargs):
        self.delete("label")
        if "width" in kwargs:
            self.width = kwargs["width"]
            self.configure(width=self.width)
        if "height" in kwargs:
            self.height = kwargs["height"]
            self.configure(height=self.height)
        if "text" in kwargs:
            self.text = kwargs["text"]
        if "font" in kwargs:
            self.font = kwargs["font"]
        if "justify" in kwargs:
            self.justify = kwargs["justify"]
        if "bg_color" in kwargs:
            self.bg_color = kwargs["bg_color"]
        if "fg_color" in kwargs:
            self.fg_color = kwargs["fg_color"]
        if "cursor" in kwargs:
            self.cursor = kwargs["cursor"]
        self._create_label()

    def cget(self, key):
        if key == "width":
            return self.width
        elif key == "height":
            return self.height
        elif key == "text":
            return self.text
        elif key == "font":
            return self.font
        elif key == "justify":
            return self.justify
        elif key == "bg_color":
            return self.bg_color
        elif key == "fg_color":
            return self.fg_color
        elif key == "cursor":
            return self.cursor
        else:
            raise KeyError(f"Unknown option: '{key}'")
