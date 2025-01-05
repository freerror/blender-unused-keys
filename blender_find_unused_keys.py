from typing import Any

from blender_all_standard_keys import keymap

all_bind_types = {
    "TWO",
    # "MOUSESMARTZOOM",
    "DEL",
    "F",
    "I",
    "G",
    "E",
    "NUMPAD_8",
    "NUMPAD_2",
    # "NDOF_MOTION",
    # "NDOF_BUTTON_BOTTOM",
    "LEFTMOUSE",
    "H",
    "Y",
    "NUMPAD_7",
    "ONE",
    # "NDOF_BUTTON_LEFT",
    # "NDOF_BUTTON_ROLL_CCW",
    "Z",
    "R",
    "W",
    "COMMA",
    "S",
    "HOME",
    "NUMPAD_9",
    "NUMPAD_6",
    # "NDOF_BUTTON_FIT",
    "A",
    # "NUMPAD_MINUS",
    "T",
    "WHEELINMOUSE",
    "NUMPAD_1",
    "THREE",
    "J",
    "L",
    # "APP",
    # "TRACKPADPAN",
    # "TIMER1",
    "N",
    "NUMPAD_5",
    "V",
    "NUMPAD_PLUS",
    "MINUS",
    "K",
    "U",
    # "MOUSEROTATE",
    # "TRACKPADZOOM",
    "O",
    "P",
    "RIGHTMOUSE",
    "NUMPAD_3",
    # "NDOF_BUTTON_RIGHT",
    "NUMPAD_0",
    "X",
    "SLASH",
    # "Q",
    # "NDOF_BUTTON_BACK",
    "NUMPAD_SLASH",
    "C",
    "EQUAL",
    # "NDOF_BUTTON_TOP",
    # "TAB",
    # "NDOF_BUTTON_FRONT",
    # "NDOF_BUTTON_ROLL_CW",
    "PERIOD",
    "D",
    "M",
    "NUMPAD_PERIOD",
    "MIDDLEMOUSE",
    "ACCENT_GRAVE",
    "NUMPAD_4",
    "B",
    "WHEELOUTMOUSE",
}

# all_possible_binds = [dict(i) for i in list(set([tuple(bind.items()) for bind in keymap]))]

all_bind_options = [
    (('type', 'REPLACE'), ('ctrl', 0), ('shift', 0), ('alt', 0)),
    (('type', 'REPLACE'), ('ctrl', 1), ('shift', 0), ('alt', 0)),
    (('type', 'REPLACE'), ('ctrl', 0), ('shift', 1), ('alt', 0)),
    (('type', 'REPLACE'), ('ctrl', 0), ('shift', 0), ('alt', 1)),
    (('type', 'REPLACE'), ('ctrl', 1), ('shift', 1), ('alt', 0)),
    (('type', 'REPLACE'), ('ctrl', 1), ('shift', 0), ('alt', 1)),
    (('type', 'REPLACE'), ('ctrl', 0), ('shift', 1), ('alt', 1)),
    (('type', 'REPLACE'), ('ctrl', 1), ('shift', 1), ('alt', 1)),
]

sorted_type_options = sorted(all_bind_types)

all_possible_binds = []

for item in all_bind_options:
    for type_option in sorted_type_options:
        generated_option = dict(item)
        generated_option["type"] = type_option
        all_possible_binds.append(generated_option)

used_binds_set = set()

for item in keymap:
    used_binds_set.add(tuple(item.items()))

used_binds = [dict(item) for item in used_binds_set]

unused_binds = []

for bind in all_possible_binds:
    if bind not in used_binds:
        unused_binds.append(bind)

def get_mods(bind: dict[str, Any]):
    mods = []
    if bind["ctrl"]:
        mods.append("Ctrl")
    if bind["alt"]:
        mods.append("Alt")
    if bind["shift"]:
        mods.append("Shift")
    return " + ".join(mods)

pretty_unused = ""
pretty_unused += ("Unused Binds:\n")
for bind in unused_binds:
    mods = get_mods(bind)
    if mods:
        pretty_unused += f"{get_mods(bind)} + {bind['type']}\n"
    else:
        pretty_unused += f"{bind['type']}\n"

with open("unused_binds.txt", 'w') as f:
    f.write(pretty_unused)

print(pretty_unused)