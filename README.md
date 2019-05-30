# Remote-Control

A program that detects button presses using an IR receiver with an Arduino and sends that data to a python script that simualtes keyboard presses. Uses include using puase/play/fast forwar/rewind for controlling media on VLC media player.

## Setup

1. Upload the Arduino C++ file found in the setup folder to your arduino and connect the IR sensor to pin 8 (or connect it to annother pin and modify the ```#define RECEIVER_PIN``` on line 3 of the Arduino code)
2. Open the remote_frequencies.json file using a text editor
3. Open the serial window within the Ardino IDE (ctrl+shift+m)
4. Press the buttons on the remote and reccord the corresponding frequency in the json file. Save that file once finished.
5. Upload the main Arduino C++ file found in the arduino_remote_control foler and launch the remote_conrol.py script.
