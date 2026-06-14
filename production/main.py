import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.extensions.direct_pins import DirectPins

keyboard = KMKKeyboard()

keyboard.modules.append(Macros())

pins = DirectPins()
pins.pinmap = [
    board.D10,
    board.D9,
    board.D8,
]
keyboard.modules.append(pins)

IF_ELSE = KC.MACRO(
    "if () {\n\n} else {\n\n}",
    KC.LEFT, KC.LEFT, KC.LEFT, KC.LEFT,
    KC.LEFT, KC.LEFT, KC.LEFT, KC.LEFT,
    KC.LEFT, KC.LEFT, KC.LEFT, KC.LEFT,
    KC.LEFT, KC.LEFT, KC.LEFT, KC.LEFT,
    KC.LEFT, KC.LEFT, KC.LEFT
)

FOR_LOOP = KC.MACRO(
    "for (int i = 0; i < ; i++) {\n\n}",
    KC.LEFT, KC.LEFT, KC.LEFT, KC.LEFT,
    KC.LEFT, KC.LEFT, KC.LEFT, KC.LEFT,
    KC.LEFT, KC.LEFT, KC.LEFT
)

DEBUG_PRINT = KC.MACRO(
    'System.out.println("DEBUG: ");',
    KC.LEFT, KC.LEFT, KC.LEFT
)

keyboard.keymap = [[
    IF_ELSE,
    FOR_LOOP,
    DEBUG_PRINT,
]]

if __name__ == "__main__":
    keyboard.go()
