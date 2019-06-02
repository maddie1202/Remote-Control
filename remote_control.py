import serial
import json
import re
from pynput.keyboard import Key, Controller, KeyCode
import config

def interpret_remote_input(remote_input, last_input):
    remote_input = check_for_holding(remote_input, last_input)

    button = config.remote_configs.get(remote_input, "key not found")

    if(button == "key not found"):
        raise KeyError("Remote error, ", remote_input, "not recognized.")
    else:
        print(button)
        return button

def check_for_holding(current_input, last_input):
    if(current_input == config.remote_configs["Hold"]):
        return last_input
    else:
        return current_input

def interpret_button_press(button):
    remote_key_name = config.button_configs.get(button, "key not found")

    if(remote_key_name == "key not found"):
        raise KeyError("Button error", button, "not configured.")
    else:
        print(remote_key_name)
        return remote_key_name


def interpret_key(remote_key_name):
    key_codes = config.key_configs.get(remote_key_name, "key not found")

    if(key_codes == "key not found"):
        raise KeyError("Key error,", remote_key_name, "not configured.")
    else:
        press_key(key_codes)


def press_key(key_codes):
    keyboard = Controller()

    if type(key_codes) is list:
        for key_code in key_codes:
            keyboard.press(key_code)

        for kye_code in key_codes:
            keyboard.release(key_codes)
    else:
        keyboard.press(key_codes)
        keyboard.release(key_codes)


arduino = serial.Serial("COM3", 115200, timeout=.1)

while True:
    last_input = ""
    arduino_input = arduino.readline()[:-2] #the last bit gets rid of the new-line chars

    if arduino_input:
        matches = re.findall("b'(\d+)'", str(arduino_input))
        remote_input = matches[0]
        button = ""

        try:
            button = interpret_remote_input(remote_input, last_input)
            key = interpret_button_press(button)
            interpret_key(key)

            last_input = remote_input
        except KeyError as ke:
            print(ke)

        if button == "Power":
            break

arduino.close()
