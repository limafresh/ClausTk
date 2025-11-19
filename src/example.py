import claustk


def click_btn():
    text_edit.insert("end", "Button clicked!\n")


root = claustk.ClausWindow(background="christmas_trees")
root.title("ClausTk Example")
root.geometry("800x600")

frame = claustk.ClausFrame(root, background="santa_clauses")
frame.pack(padx=10, pady=10, side="left", fill="y")

label = claustk.ClausLabel(frame)
label.pack(padx=10, pady=10)

button = claustk.ClausButton(frame, command=click_btn)
button.pack(padx=10, pady=10)

click_me = claustk.ClausButton(frame, text="Click Me!", bg="blue", command=click_btn)
click_me.pack(padx=10, pady=10)

line_edit = claustk.ClausLineEdit(frame)
line_edit.pack(padx=10, pady=10, side="bottom")
line_edit.insert("end", "Hello!")

frame2 = claustk.ClausFrame(root)
frame2.pack(padx=10, pady=10, side="left", fill="both", expand=True)

blured_frame = claustk.ClausFrame(frame2, bg_blur=20)
blured_frame.pack(padx=10, pady=10)

radiobutton = claustk.ClausRadiobutton(blured_frame)
radiobutton.pack(padx=10, pady=10)

radiobutton2 = claustk.ClausRadiobutton(blured_frame)
radiobutton2.pack(padx=10, pady=10)

info_label = claustk.ClausLabel(blured_frame, text="Yes, you can blur the background in ClausTk")
info_label.pack(padx=10, pady=10)

text_edit = claustk.ClausTextEdit(frame2)
text_edit.pack(padx=10, pady=10)

frame3 = claustk.ClausFrame(root, background="snowflakes")
frame3.pack(padx=10, pady=10, side="right")

label2 = claustk.ClausLabel(frame3)
label2.pack(padx=10, pady=10)

checkbox = claustk.ClausCheckbox(frame3)
checkbox.pack(padx=10, pady=10)

rounded_button = claustk.ClausRoundedButton(frame3, command=click_btn)
rounded_button.pack(padx=10, pady=10)

slider = claustk.ClausSlider(frame3)
slider.pack(padx=10, pady=10)

root.happynewyear()
