import board 

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.capsword import CapsWord
from storage import getmount

keyboard = KMKKeyboard()
# keyboard.debug_enabled = True

# keyboard.tap_time which defines how long KC.TT and KC.LT will wait 
# before considering a key "held" (see layers.md).
keyboard.tap_time = 150 # ms

# [[ MODULES ]] ---------------------------------------------------
# SPLIT: http://kmkfw.io/docs/split_keyboards/
# decide side based on label assigned to the storage of the board
# CIRCUITPYL is the left side, CIRCUITPYR is the right side
side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
split = Split(
    split_side=side,
    split_type=SplitType.UART,
    data_pin=board.TX,
    data_pin2=board.RX,
    use_pio=True,
    uart_flip=True)
keyboard.modules.append(split)

# HOLDTAP: http://kmkfw.io/docs/holdtap
holdtap = HoldTap()
holdtap.tap_time = 150 # set a custom tap timeout in ms
keyboard.modules.append(holdtap)

# LAYERS: http://kmkfw.io/docs/layers/
keyboard.modules.append(Layers())

# MOUSE KEYS: http://kmkfw.io/docs/mouse_keys/
keyboard.modules.append(MouseKeys())

# CAPS WORD: http://kmkfw.io/docs/capsword
caps_word=CapsWord()
# caps_word.keys_ignored.append(KC.SPC)  # to ignore space
keyboard.modules.append(caps_word)
# -----------------------------------------------------------------

# [[ LAYERS ]] ----------------------------------------------------
# HOLDTAP MODS: http://kmkfw.io/docs/holdtap#custom-holdtap-behavior
# KC.HT(KC.TAP, KC.HOLD, prefer_hold=True, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.NONE)
H_A_GUI = KC.HT(KC.A, KC.LGUI, tap_interrupted=True, tap_time=220)
H_S_ALT = KC.HT(KC.S, KC.LALT, tap_interrupted=True)
H_D_CTL = KC.HT(KC.D, KC.LCTRL, tap_interrupted=True)
H_F_SFT = KC.HT(KC.F, KC.LSHIFT, tap_interrupted=True)

H_SC_GUI = KC.HT(KC.SCOLON, KC.RGUI, tap_interrupted=True)
H_L_ALT  = KC.HT(KC.L, KC.RALT, tap_interrupted=True)
H_K_CTL  = KC.HT(KC.K, KC.RCTRL, tap_interrupted=True)
H_J_SFT  = KC.HT(KC.J, KC.RSHIFT, tap_interrupted=True)

# HOLDTAP LAYERS: http://kmkfw.io/docs/layers#keycodes
L_TAB_NAV = KC.LT(1, KC.TAB)
L_ESC_NUM = KC.LT(2, KC.ESC)
L_ENT_SYM = KC.LT(3, KC.ENT)
# -----------------------------------------------------------------

# [[ KEYMAP ]] ----------------------------------------------------
# KEYCODES: http://kmkfw.io/docs/keycodes/
____ = KC.TRNS
XXXX = KC.NO

miryoku = [
    # 0: BASE
    [
        KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,
        H_A_GUI,    H_S_ALT,    H_D_CTL,    H_F_SFT,    KC.G,       KC.H,       H_J_SFT,    H_K_CTL,    H_L_ALT,    H_SC_GUI,
        KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.SLASH,
        XXXX,       KC.CW,      L_TAB_NAV,  L_ESC_NUM,  KC.BSPACE,  KC.SPC,     L_ENT_SYM,  KC.BSPACE,  KC.LSHIFT,  XXXX,
    ],
    # 1: NAV LAYER
    [
        XXXX,       XXXX,       XXXX,       XXXX,       XXXX,       KC.MS_LEFT, KC.MS_DOWN, KC.MS_UP,   KC.MS_RIGHT,XXXX,
        KC.LGUI,    KC.LALT,    KC.LCTRL,   KC.LSHIFT,  XXXX,       KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   KC.CAPSLOCK,
        XXXX,       XXXX,       XXXX,       XXXX,       XXXX,       KC.HOME,    KC.PGDN,    KC.PGUP,    KC.END,     XXXX,
        XXXX,       XXXX,       XXXX,       XXXX,       XXXX,       KC.MB_RMB,  KC.MB_LMB,  KC.MB_MMB,  XXXX,
    ],
    # 2: NUM LAYER
    [
        XXXX,       XXXX,       XXXX,       XXXX,       XXXX,       KC.LBRC,    KC.N7,      KC.N8,      KC.N9,      KC.RBRC,
        KC.LGUI,    KC.LALT,    KC.LCTRL,   KC.LSHIFT,  XXXX,       KC.EQUAL,   KC.N4,      KC.N5,      KC.N6,      KC.SCOLON,
        XXXX,       XXXX,       XXXX,       XXXX,       XXXX,       KC.BSLASH,  KC.N1,      KC.N2,      KC.N3,      KC.GRAVE,
        XXXX,       XXXX,       XXXX,       XXXX,       XXXX,       KC.MINUS,   KC.N0,      KC.DOT,     XXXX,
    ],
    # 3: SYM NUM LAYER
    [
        XXXX,       XXXX,       XXXX,       XXXX,       XXXX,       KC.LBRC,    KC.N7,      KC.N8,      KC.N9,      KC.RBRC,
        KC.LGUI,    KC.LALT,    KC.LCTRL,   KC.LSHIFT,  XXXX,       KC.EQUAL,   KC.N4,      KC.N5,      KC.N6,      KC.SCOLON,
        XXXX,       XXXX,       XXXX,       XXXX,       XXXX,       KC.BSLASH,  KC.N1,      KC.N2,      KC.N3,      KC.GRAVE,
        XXXX,       XXXX,       XXXX,       XXXX,       XXXX,       KC.UNDS,   KC.N0,      KC.DOT,     XXXX,
    ],
]

keyboard.keymap = miryoku
# -----------------------------------------------------------------

if __name__ == '__main__':
    keyboard.go()
