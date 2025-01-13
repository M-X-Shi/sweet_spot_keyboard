# Write your code here :-)
# code.py for sweet spot keyboard

print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.holdtap import HoldTap
from kmk.modules.sticky_mod import StickyMod
from kmk.modules.combos import Combos, Chord

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
combos = Combos()
keyboard.modules.append(combos)
keyboard.modules.append(StickyMod())

keyboard.col_pins = (board.GP1, board.GP2, board.GP5, board.GP7, board.GP28, board.GP27,
                     board.GP21, board.GP17, board.GP9, board.GP10, board.GP13, board.GP15)
keyboard.row_pins = (board.GP0, board.GP16, board.GP18, board.GP20, board.GP22, board.GP26)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# layer modifiers and holdtap keys
SPC_L1 = KC.LT(1, KC.SPC, prefer_hold=False)    # space when tapped, layer1 when held
ENT_L1 = KC.LT(1, KC.ENT, prefer_hold=False)    # enter when tapped, layer1 when held

E_SFT = KC.HT(KC.E, KC.LSFT, prefer_hold=False) # e when tapped, left shift when held
I_SFT = KC.HT(KC.I, KC.RSFT, prefer_hold=False) # i when tapped, right shift when held
SLSH_SFT = KC.HT(KC.SLSH, KC.RSFT, prefer_hold=False) # / when tapped, right shift when held

F_CTL = KC.HT(KC.F, KC.LCTL, prefer_hold=False) # f when tapped, left control when held
J_CTL = KC.HT(KC.J, KC.RCTL, prefer_hold=False) # j when tapped, right control when held

W_ALT = KC.HT(KC.W, KC.LALT, prefer_hold=False) # w when tapped, left alt when held
O_ALT = KC.HT(KC.O, KC.RALT, prefer_hold=False) # o when tapped, right alt when held

# switch between open windows, same as hold alt then tap tab
SW = KC.SM(kc=KC.TAB, mod=KC.LALT)

# some operators
NEQ  = send_string('!= ')
PTR  = send_string('->')

# provided using an IDE or a powerful text editor as vscode that features code completion
# key sequences
key_sequences = {
    'newline':          simple_key_sequence((KC.END, KC.ENT)),                  # moving the cursor to the end, then enter
    'statement_c':      simple_key_sequence((KC.END, KC.SCLN, KC.ENT)),         # making current line a C statement, then enter. also valid in C++, Java and C#
    'block_c':          simple_key_sequence((KC.END, KC.ENT, KC.LCBR, KC.ENT)), # C syntactic code block
    'block_java':       simple_key_sequence((KC.END, KC.SPC, KC.LCBR, KC.ENT)), # Java syntactic code block
    'block_python':     simple_key_sequence((KC.END, KC.COLN, KC.ENT)),         # Python syntactic code block
    'vscode_shortcuts': simple_key_sequence((KC.LCTL(KC.K), KC.LCTL(KC.S))),    # control-k then control-s, open shortcuts page in VSCode
}

BLOCK = key_sequences['block_java'] # syntactic code block

combos.combos = [
    # format: Chord((key1, key2), key_sequence),
    # note: key1 and key2 must be in the keyboard.keymap below
    #Chord((KC.K, KC.L), key_sequences['newline']),             # tapping k and l simultaneously implements newline
    #Chord((KC.K, KC.S), key_sequences['vscode_shortcuts']),    # tapping k and s simultaneously implements vscode_shortcuts
    #Chord((KC.R, J_CTL), send_string('return ')),              # tapping r and j simultaneously inputs string 'return '
    #Chord((KC.S, KC.D), BLOCK),                                # tapping s and d simultaneously inputs syntactic code block


]

_______ = KC.NO

keyboard.keymap = [
    # layer0
    [KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
     KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,
     KC.TAB,  KC.Q,    W_ALT,   E_SFT,   KC.R,    KC.T,    KC.Y,    KC.U,    I_SFT,   O_ALT,   KC.P,    KC.BSPC,
     KC.CAPS, KC.A,    KC.S,    KC.D,    F_CTL,   KC.G,    KC.H,    J_CTL,   KC.K,    KC.L,    KC.SCLN, KC.QUOT,
     KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  SLSH_SFT,_______,
     KC.LCTL, KC.NO,   KC.LWIN, KC.LALT, ENT_L1,  KC.NO,   SPC_L1,  KC.RWIN, KC.RALT, KC.NO,   KC.DEL,  _______,],

    # layer1
    [KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.LBRC, KC.RBRC, KC.BSLS, KC.PIPE, KC.NO,   KC.TILD, KC.GRV,  KC.LCBR, KC.RCBR, KC.NO,   KC.NO,
     SW,      KC.NO,   KC.NO,   KC.PGUP, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.UP,   KC.NO,   KC.NO,   KC.DEL,
     KC.NO,   KC.NO,   KC.HOME, KC.PGDN, KC.END,  KC.ESC,  KC.NO,   KC.LEFT, KC.DOWN, KC.RGHT, KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.INS,   _______,],

    # layer2
    [KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______,],
]

if __name__ == '__main__':
    keyboard.go()
