import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
    board.D7,
    board.D8,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

i2c = busio.I2C(board.SCL, board.SDA)

display_driver = SSD1306(
    i2c=i2c,
    device_address=0x3C,
    width=128,
    height=32,
)

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text="9-Key Macro Pad", x=0, y=0),
        TextEntry(text="Layer: {layer}", x=0, y=16),
    ],
)

keyboard.extensions.append(display)

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.E,
        KC.F,
        KC.G,
        KC.H,
        KC.MACRO(
            Press(KC.LCTL),
            Tap(KC.C),
            Release(KC.LCTL),
        ),
    ]
]

if __name__ == "__main__":
    keyboard.go()
