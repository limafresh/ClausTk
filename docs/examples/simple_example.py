import claustk


def click_btn():
    print("Merry Christmas and Happy New Year!")


root = claustk.ClausWindow()

button = claustk.ClausRoundedButton(root, text="Click me!", command=click_btn)
button.pack(padx=10, pady=10)

root.happynewyear()
