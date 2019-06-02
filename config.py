from pynput.keyboard import Key, Controller, KeyCode

remote_configs = {
	"41565" : "Power",
	"25245" : "Vol+",
	"57885" : "Func/Stop",
	"8925" : "Rewind",
	"765" : "Pause/Play",
	"49725" : "Fast Forward",
	"57375" : "Down Arrow",
	"43095" : "Vol-",
	"36975" : "Up Arrow",
	"26775" : "0",
	"39015" : "EQ",
	"45135" : "St/Rept",
	"12495" : "1",
	"6375" : "2",
	"31365" : "3",
	"4335" : "4",
	"14535" : "5",
	"23205" : "6",
	"17085" : "7",
	"19125" : "8",
	"21165" : "9",
	"Hold" : "65535"
}

button_configs = {
    "Pause/Play" : "space",
    "Vol+" : "up_arrow",
    "Vol-"  : "down_arrow",
    "Fast Forward" : "right_arrow",
    "Rewind" : "left_arrow",
    "Power" : "alt+f4",
    "EQ" : "f"
}

key_configs = {
    "space" : Key.space,
    "up_arrow" : Key.up,
    "down_arrow" : Key.down,
    "left_arrow" : Key.left,
    "right_arrow" : Key.right,
    "f" : "f",
    "alt+f4" : [Key.alt, Key.f4]
}
