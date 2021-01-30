import os
import subprocess
import time

DEVICE_TO_FIND = "Ltd Alps Touchpad"

CMD_SET_ONSCREEN_KEYBOARD_STATUS = "gsettings set org.gnome.desktop.a11y.applications screen-keyboard-enabled "
CMD_ENABLE_ONSCREEN_KEYBOARD = CMD_SET_ONSCREEN_KEYBOARD_STATUS + "true"
CMD_DISABLE_ONSCREEN_KEYBOARD = CMD_SET_ONSCREEN_KEYBOARD_STATUS + "false"


def str_to_bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def is_keyboard_connected():
    result = subprocess.check_output("lsusb").decode("utf8")
    if result.find(DEVICE_TO_FIND) != -1:
        return True
    else:
        return False


def is_onscreen_keyboard_enabled():
    res = subprocess.check_output(["gsettings",
                                   "get",
                                   "org.gnome.desktop.a11y.applications",
                                   "screen-keyboard-enabled"]).decode("utf8")
    res = res.split("\n")[0]
    return str_to_bool(res)


if __name__ == '__main__':
    while True:
        if is_keyboard_connected():
            print("Keyboard Connected")
            if is_onscreen_keyboard_enabled():
                print("Disabled Onscreen Keyboard")
                os.system(CMD_DISABLE_ONSCREEN_KEYBOARD)
        else:
            print("Keyboard Disconnected")
            if not is_onscreen_keyboard_enabled():
                print("Enabling Onscreen Keyboard")
                os.system(CMD_ENABLE_ONSCREEN_KEYBOARD)
        time.sleep(2)

