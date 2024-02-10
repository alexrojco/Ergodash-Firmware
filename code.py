print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.hid import HIDModes
from kmk.modules.split import Split, SplitType

from kb import varList


keyboard = KMKKeyboard()

keyboard.tap_time = 320
keyboard.debug_enabled = True

# split = Split(
#             split_side=varList.ss,
#             # split_side=None,
#             split_flip=False,
#             split_target_left=True,
#             # data_pin=board.GP1,
#             # data_pin2=board.GP0,
#             data_pin=board.GP3,
#             # uart_interval=20,
#             # split_type=SplitType.UART,
#             # uart_flip=True,
#             # use_pio=True
#             )

split = Split(
    split_flip=True,
    uart_flip=True,
    split_type=SplitType.UART,
    data_pin=board.GP3,
    use_pio=True)
layers = Layers()

keyboard.modules.append(layers)
keyboard.modules.append(split)


# Initialize Keyboard

# Setup MCU pins
keyboard.col_pins = varList.col_pins
keyboard.row_pins = varList.row_pins
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Setup Layers
MOMENT1 = KC.MO(1)

_______ = KC.TRNS
XXXXXXX = KC.NO
UNDO = KC.LGUI(KC.Z)

keyboard.keymap = [
    # Qwerty
    [
        KC.ESC,  KC.N1,	  KC.N2,   KC.N3,   KC.N4,   KC.N5,  KC.MINS,                           KC.EQL,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.BSPC,  
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   KC.LBRC,                           KC.RBRC, KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    UNDO,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   KC.BSLS,                           KC.SLS,  KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, XXXXXXX,  
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,           KC.DEL,        XXXXXXX,             KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.QUOT, XXXXXXX,
        MOMENT1, KC.LCTL, KC.LALT, KC.LGUI,         KC.LGUI, KC.SPC, KC.BSPC,       KC.TAB,  KC.SPC,  KC.ENT,              KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
    ],
    # Function Layer
    [
        XXXXXXX, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,                            XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,                           XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, KC.BRID, KC.BRIU, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX,      XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX, XXXXXXX, XXXXXXX,      XXXXXXX, XXXXXXX, XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
    ],
]

if __name__ == '__main__':
    # keyboard.go(hid_type=HIDModes.USB)
    keyboard.go()