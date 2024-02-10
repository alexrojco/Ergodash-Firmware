# LEFT
import board

from kmk.modules.split import SplitSide

class varList():
    col_pins = (
        board.GP29,
        board.GP28,
        board.GP27,
        board.GP26,
        board.GP22,
        board.GP20,
        board.GP23,
    )
    row_pins = (
        board.GP4,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
    )

    ss = SplitSide.LEFT 