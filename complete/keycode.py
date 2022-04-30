string = "never gonna give you up"

key_dict = {
        "a":"0x04",
        "b":"0x05",
        "c":"0x06",
        "d":"0x07",
        "e":"0x08",
        "f":"0x09",
        "g":"0x0A",
        "h":"0x0B",
        "i":"0x0C",
        "j":"0x0D",
        "k":"0x0E",
        "l":"0x0F",
        "m":"0x10",
        "n":"0x11",
        "o":"0x12",
        "p":"0x13",
        "q":"0x14",
        "r":"0x15",
        "s":"0x16",
        "t":"0x17",
        "u":"0x18",
        "v":"0x19",
        "w":"0x1A",
        "x":"0x1B",
        "y":"0x1C",
        "z":"0x1D",
        " ":"0x2C"
}
result=""
for c in string:
    result+=key_dict[c]+","

print(result)
