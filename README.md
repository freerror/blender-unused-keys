# Finding Unused Keybinds in Blender

## Getting the Current Keybinds from Blender

Run this within the Python Scripting Interface with the system console open (Window | Toggle System Console):

```python
from bpy import context as C
from bpy import data as D


result = []
keymaps = C.window_manager.keyconfigs.active.keymaps
for key in keymaps.keys():
    for item in keymaps[key].keymap_items:
            result.append({"type": item.type, "ctrl": item.ctrl, "shift": item.shift, "alt": item.alt})

# Make sure this path exists at the root of the drive blender is running on / system root
with open("/tmp/out.txt", 'w') as f:
    f.write(str(result))
```

This will get the whole keymap, not just custom keys.

## Run the Python Script over the Keymap

Copy the output from the `out.txt` file to be the value of the variable `keymap` in `blender_all_standard_keys.py`.

Finally, run `blender_find_unused_keys.py` with python in this directory, e.g.: `python ./blender-unused-keys/blender_find_unused_keys.py`

Unused keyboard shortcuts will be saved to unused_binds.txt and displayed in the console.
