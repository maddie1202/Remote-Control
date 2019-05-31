import serial
import json
import re
from pynput.keyboard import Key, Controller, KeyCode

def press_key(button):
    with open ("button_config.json", "r") as json_file:
        json_str = json_file.read()
        configs = json.loads(json_str)

        try:
            with open ("virtual_key_codes.json", "r") as json_file:
                json_str = json_file.read()
                codes = json.loads(json_str)

            keyboard = Controller()
            keys = configs[button]

            if type(keys) is list:
                for key in keys:
                    keyboard.press(KeyCode(codes[key]))
                for key in keys:
                    keyboard.release(KeyCode(codes[key]))
            else:
                keyboard.press(KeyCode(codes[keys]))
                keyboard.release(KeyCode(codes[keys]))


        except KeyError:
            print("Error,", button, "not configured")


with open ("remote_frequencies.json", "r") as json_file:
    json_str = json_file.read()
    frequencies = json.loads(json_str)

arduino = serial.Serial("COM3", 115200, timeout=.1)
last_frequency = 0

while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars

    if data:
        matches = re.findall("b'(\d+)'", str(data))
        frequency = matches[0]

        if frequency == frequencies["Hold"]:
            frequency = last_frequency
        else:
            last_frequency = frequency

        try:
            button = frequencies[frequency]
            print(frequencies[frequency])
        except KeyError:
            print("Error, ", frequency, " not recognized.")
            continue

        press_key(button)

        if button == "Power" :
            exit()
