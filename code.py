print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes

from kb import varList

# Initialize Keyboard
keyboard = KMKKeyboard()

keyboard.debug_enabled = False

# Setup HoldTap
from kmk.modules.holdtap import HoldTap
holdtap = HoldTap()
holdtap.tap_time = 300

keyboard.modules.append(holdtap)


# Setup Split
from kmk.modules.split import Split, SplitType
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
from kmk.modules.layers import Layers
layers = Layers()
keyboard.modules.append(layers)

# Setup Ctrl GUI Swap
from kmk.modules.cg_swap import CgSwap
cg_swap = CgSwap()
keyboard.modules.append(cg_swap)
OS_SWAP = KC.CG_TOGG

# Setup Media Keys
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

# Setup Combos
from kmk.modules.combos import Combos, Chord
combos = Combos()
keyboard.modules.append(combos)

combos.combos = [
    Chord((KC.Q, KC.W, KC.E, KC.R), KC.TO(5)),      # QWER to switch to the gaming Layer
    Chord((KC.U, KC.I, KC.O, KC.P), KC.TO(6)),      # QWER to switch to the Colemak Layer
    Chord((KC.N1, KC.N2, KC.N3, KC.N4), KC.TO(0))   # 1234 to go back
]



MOMENT1 = KC.MO(1)


_______ = KC.TRNS
ENT_CMD = KC.HT(KC.ENT, KC.LGUI)
SPC_SFT = KC.HT(KC.SPC, KC.LSFT)


# Thumb layer keys
ENT_SYM = KC.HT(KC.ENT, KC.MO(2), prefer_hold=False)
BSPC_NM = KC.HT(KC.BSPC, KC.MO(3), prefer_hold=False)
SPC_NAV = KC.HT(KC.SPC, KC.MO(4), prefer_hold=False)

# QWERTY home row mods
A_SUPER = KC.HT(KC.A, KC.LCTL, prefer_hold=False)
S_SUPER = KC.HT(KC.S, KC.LALT, prefer_hold=False)
D_SUPER = KC.HT(KC.D, KC.LGUI, prefer_hold=False)
F_SUPER = KC.HT(KC.F, KC.LSFT, prefer_hold=False)

J_SUPER = KC.HT(KC.J, KC.RSFT, prefer_hold=False)
K_SUPER = KC.HT(KC.K, KC.RGUI, prefer_hold=False)
L_SUPER = KC.HT(KC.L, KC.RALT, prefer_hold=False)
SPC_SUP = KC.HT(KC.SCLN, KC.RCTL, prefer_hold=False)

# Colemak home row mods
A_SUCOL = KC.HT(KC.A, KC.LCTL, prefer_hold=False)
R_SUCOL = KC.HT(KC.R, KC.LALT, prefer_hold=False)
S_SUCOL = KC.HT(KC.S, KC.LGUI, prefer_hold=False)
T_SUCOL = KC.HT(KC.T, KC.LSFT, prefer_hold=False)

N_SUCOL = KC.HT(KC.N, KC.RSFT, prefer_hold=False)
E_SUCOL = KC.HT(KC.E, KC.RGUI, prefer_hold=False)
I_SUCOL = KC.HT(KC.I, KC.RALT, prefer_hold=False)
O_SUCOL = KC.HT(KC.O, KC.RCTL, prefer_hold=False)


XXXXXXX = KC.NO

# M custom buttons
UNDO = KC.LGUI(KC.Z)
from kmk.modules.macros import Delay, Macros, Tap
macros = Macros()
keyboard.modules.append(macros)
ZOOM = KC.MACRO(
    Tap(KC.LGUI(KC.LSFT(KC.A))),
    Tap(KC.LGUI(KC.LSFT(KC.V)))
)




# Old main thumb cluster    
#                    KC.DEL,       XXXXXXX,
# ENT_CMD, SPC_SFT, KC.BSPC,       KC.TAB,  SPC_SFT,  ENT_CMD,


keyboard.keymap = [
    # Qwerty
    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,  KC.MINS,                           KC.EQL,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.BSPC,  
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   KC.LBRC,                           KC.RBRC, KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    UNDO,
        KC.CAPS, A_SUPER, S_SUPER, D_SUPER, F_SUPER, KC.G,   KC.BSLS,                           KC.QUOT, KC.H,    J_SUPER, K_SUPER, L_SUPER, SPC_SUP, ZOOM,  
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,           KC.DEL,         XXXXXXX,            KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, XXXXXXX,
        MOMENT1, KC.LCTL, KC.LALT, KC.LGUI,         ENT_SYM, SPC_NAV, BSPC_NM,      MOMENT1,  KC.SPC,  KC.ENT,              KC.LEFT, KC.DOWN, KC.UP, KC.RGHT,
    ],
    # Function Layer
    [
        OS_SWAP, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,                            XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,                           XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, KC.BRIU, KC.VOLU, KC.MFFD, XXXXXXX, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, KC.RSFT, KC.RGUI, KC.RALT, KC.RCTL, XXXXXXX, 
        XXXXXXX, KC.BRID, KC.VOLD, KC.MRWD, XXXXXXX, XXXXXXX,         XXXXXXX,      XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, XXXXXXX, KC.MUTE, KC.MPLY,         XXXXXXX, XXXXXXX, XXXXXXX,      XXXXXXX, XXXXXXX, XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
    ],
    # Symbol Layer
    [
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.LPRN, KC.RPRN, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                         XXXXXXX, XXXXXXX, KC.GRV,  XXXXXXX, KC.LBRC, KC.RBRC, XXXXXXX, 
        XXXXXXX, KC.LCTL, KC.LALT, KC.LGUI, KC.LSFT, XXXXXXX, XXXXXXX,                         XXXXXXX, XXXXXXX, KC.MINS, KC.EQL,  KC.SCLN, KC.QUOT, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX,      XXXXXXX,             XXXXXXX, XXXXXXX, KC.COMM, KC.DOT, KC.SLSH, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX, XXXXXXX, XXXXXXX,      XXXXXXX, KC.SPC, XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
    ],
    # Num Layer
    [
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, KC.N7,   KC.N8,   KC.N9,   KC.SLSH, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, KC.N4,   KC.N5,   KC.N6,   KC.ASTR, XXXXXXX, 
        XXXXXXX, KC.LCTL, KC.LALT, KC.LGUI, KC.LSFT, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, KC.N1,   KC.N2,   KC.N3,   KC.MINS, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX,      XXXXXXX,             XXXXXXX, KC.N0,   KC.DOT,  KC.COLN, KC.PLUS, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX, XXXXXXX, XXXXXXX,      XXXXXXX, KC.SPC, XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
    ],
    # Nav Layer
    [
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, KC.LCTL, KC.LALT, KC.LGUI, KC.LSFT, XXXXXXX, XXXXXXX,                          XXXXXXX, XXXXXXX, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX,      XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,         XXXXXXX, XXXXXXX, XXXXXXX,      XXXXXXX, KC.SPC, XXXXXXX,             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
    ],
    # Gaming Layer
    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,  KC.MINS,                           KC.EQL,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.BSPC,  
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   KC.LBRC,                           KC.RBRC, KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    UNDO,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   KC.BSLS,                           KC.SLSH, KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, XXXXXXX,  
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,           KC.DEL,         XXXXXXX,            KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.QUOT, XXXXXXX,
        MOMENT1, KC.LCTL, KC.LGUI, KC.LALT,        KC.LCTL, KC.SPC, XXXXXXX,      XXXXXXX, XXXXXXX, XXXXXXX,            KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, 
    ],
    # Colemak Layer
    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,  KC.MINS,                           KC.EQL,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.BSPC,  
        KC.TAB,  KC.Q,    KC.W,    KC.F,    KC.P,    KC.G,   KC.LBRC,                           KC.RBRC, KC.J,    KC.L,    KC.U,    KC.Y,    KC.SCLN,    UNDO,
        KC.CAPS, A_SUCOL, R_SUCOL, S_SUCOL, T_SUCOL, KC.D,   KC.BSLS,                           KC.QUOT, KC.H,    N_SUCOL, E_SUCOL, I_SUCOL, O_SUCOL, ZOOM,  
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,           KC.DEL,         XXXXXXX,            KC.K,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, XXXXXXX,
        MOMENT1, KC.LCTL, KC.LALT, KC.LGUI,         ENT_SYM, SPC_NAV, BSPC_NM,      MOMENT1,  KC.SPC,  KC.ENT,              KC.LEFT, KC.DOWN, KC.UP, KC.RGHT,
    ],
]

if __name__ == '__main__':
    # keyboard.go(hid_type=HIDModes.USB)
    keyboard.go()