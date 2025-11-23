import claustk


def press(key):
    current = line_edit.get()
    if key == "=":
        try:
            result = str(eval(current))
            line_edit.delete(0, "end")
            line_edit.insert("end", result)
        except Exception:
            line_edit.delete(0, "end")
            line_edit.insert("end", "Error")
    elif key == "C":
        line_edit.delete(0, "end")
    else:
        line_edit.insert("end", key)


root = claustk.ClausWindow(background="gifts")
root.title("Calculator")

line_edit = claustk.ClausLineEdit(root, font=(None, 15), justify="right")
line_edit.pack(fill="x", padx=5, pady=20)

buttons_frame = claustk.ClausFrame(root, background="santa_clauses")
buttons_frame.pack()

row, column = 0, 0

buttons = [
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "*",
    "C",
    "0",
    "=",
    "/",
]

for button_text in buttons:
    button = claustk.ClausRoundedButton(
        buttons_frame,
        width=50,
        height=50,
        radius=20,
        text=button_text,
        font=20,
        command=lambda key=button_text: press(key),
    )
    button.grid(row=row, column=column, padx=5, pady=5)

    if button_text in ["+", "-", "*", "/"]:
        button.config(bg_color="orange")
    elif button_text == "=":
        button.config(bg_color="blue")
    else:
        button.config(bg_color="#6e6e6e")

    column += 1
    if column == 4:
        column = 0
        row += 1

root.happynewyear()
