import serial
import json
import re
import keyboard

def press_key(button):
    with open ('button_config.json', 'r') as json_file:
        json_str = json_file.read()
        configs = json.loads(json_str)

        if(button != "button not found"):
            keyboard.press_and_release(configs[button])
        else:
            print("button not found")

with open ('remote_frequencies.json', 'r') as json_file:
    json_str = json_file.read()
    frequencies = json.loads(json_str)

arduino = serial.Serial('COM3', 115200, timeout=.1)
last_frequency = 65535

while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars

    if data:
        matches = re.findall("b'(\d+)'", str(data))
        frequency = matches[0]

        print(frequency)

        if frequency == '65535':
            frequency = last_frequency
        else:
            last_frequency = frequency

        button = frequencies.get(frequency, "button not found")
        press_key(button)
