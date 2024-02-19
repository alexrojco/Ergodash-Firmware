print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.hid import HIDModes
from kmk.modules.split import Split, SplitType
from kmk.modules.holdtap import HoldTap

from kb import varList

# Initialize Keyboard
keyboard = KMKKeyboard()

keyboard.debug_enabled = False

# Setup HoldTap
holdtap = HoldTap()
holdtap.tap_time = 300

keyboard.modules.append(holdtap)


# Setup Split 
split = Split(
    split_flip=True,
    uart_flip=True,
    split_type=SplitType.UART,
    data_pin=board.GP3,
    use_pio=True)

keyboard.modules.append(split)


# Setup MCU pins
keyboard.col_pins = varList.col_pins
keyboard.row_pins = varList.row_pins
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Setup Layers
layers = Layers()
keyboard.modules.append(layers)


MOMENT1 = KC.MO(1)


_______ = KC.TRNS
ENT_CMD = KC.HT(KC.ENT, KC.LGUI)
SPC_SFT = KC.HT(KC.SPC, KC.LSFT) 
XXXXXXX = KC.NO
UNDO = KC.LGUI(KC.Z)
OS_SWAP = KC.CG_TOGG

keyboard.keymap = [
    # Qwerty
    [
        KC.ESC,  KC.N1,	  KC.N2,   KC.N3,   KC.N4,   KC.N5,  KC.MINS,                           KC.EQL,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.BSPC,  
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   KC.LBRC,                           KC.RBRC, KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    UNDO,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   KC.BSLS,                           KC.SLSH, KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, XXXXXXX,  
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,           KC.DEL,         XXXXXXX,            KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.QUOT, XXXXXXX,
        MOMENT1, KC.LCTL, KC.LALT, KC.LGUI,         ENT_CMD, SPC_SFT, KC.BSPC,       KC.TAB,  SPC_SFT,  ENT_CMD,              KC.LEFT, KC.DOWN, KC.UP, KC.RGHT,
    ],
    # Function Layer
    [
        OS_SWAP, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,                            XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,                           XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, KC.BRID, KC.BRIU, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX,      XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX, XXXXXXX, XXXXXXX,      XXXXXXX, XXXXXXX, XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
    ],
    # Media Layer
    [
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX,      XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX, XXXXXXX, XXXXXXX,      XXXXXXX, XXXXXXX, XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
    ],
]

if __name__ == '__main__':
    # keyboard.go(hid_type=HIDModes.USB)
    keyboard.go()