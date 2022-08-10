def on_button_pressed_a():
    basic.show_number(randint(0, 9))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global letter, list2
    letter = randint(1, 5)
    list2 = ["A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z"]
    if letter == 1:
        basic.show_string("" + (list2._pick_random()))
    elif letter == 2:
        basic.show_string("" + (list2._pick_random()))
    elif letter == 3:
        basic.show_string("" + (list2._pick_random()))
    elif letter == 4:
        basic.show_string("" + (list2._pick_random()))
    elif letter == 5:
        basic.show_string("" + (list2._pick_random()))
    elif letter == 6:
        basic.show_string("" + (list2._pick_random()))
    elif letter == 7:
        basic.show_string("" + (list2._pick_random()))
    elif letter == 8:
        basic.show_string("" + (list2._pick_random()))
    else:
        basic.show_string("" + (list2._pick_random()))
input.on_button_pressed(Button.B, on_button_pressed_b)

list2: List[str] = []
letter = 0
basic.show_string("#")

def on_forever():
    pass
basic.forever(on_forever)
