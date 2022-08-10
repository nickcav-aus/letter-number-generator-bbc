input.onButtonPressed(Button.A, function () {
    basic.showNumber(randint(0, 9))
})
input.onButtonPressed(Button.B, function () {
    letter = randint(1, 5)
    list2 = [
    "A",
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
    "Z"
    ]
    if (letter == 1) {
        basic.showString("" + (list2._pickRandom()))
    } else if (letter == 2) {
        basic.showString("" + (list2._pickRandom()))
    } else if (letter == 3) {
        basic.showString("" + (list2._pickRandom()))
    } else if (letter == 4) {
        basic.showString("" + (list2._pickRandom()))
    } else if (letter == 5) {
        basic.showString("" + (list2._pickRandom()))
    } else if (letter == 6) {
        basic.showString("" + (list2._pickRandom()))
    } else if (letter == 7) {
        basic.showString("" + (list2._pickRandom()))
    } else if (letter == 8) {
        basic.showString("" + (list2._pickRandom()))
    } else {
        basic.showString("" + (list2._pickRandom()))
    }
})
let list2: string[] = []
let letter = 0
basic.showIcon(IconNames.Ghost)
basic.forever(function () {
	
})
