color_dict = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc",
    "antiquewhite3": "#cdc0b0",
    "antiquewhite4": "#8b8378",
    "aquamarine1": "#7fffd4",
    "aquamarine2": "#76eec6",
    "aquamarine4": "#458b74",
    "azure1": "#f0ffff",
}

def translate_color(color):
    if color == "":
        return "No color entered"
    elif color in color_dict:
        return color_dict[color]
    else:
        return "Color not found"

print(translate_color("aquamarine1"))