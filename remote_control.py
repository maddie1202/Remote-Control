import serial
import json
import re
import keyboard

def press_key(button):
    with open ('button_config.json', 'r') as json_file:
        json_str = json_file.read()
        configs = json.loads(json_str)

        try:
            keyboard.press_and_release(configs[button])
        except KeyError:
            print("Error,", button, "not recognized.")


with open ('remote_frequencies.json', 'r') as json_file:
    json_str = json_file.read()
    frequencies = json.loads(json_str)

arduino = serial.Serial('COM3', 115200, timeout=.1)
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
