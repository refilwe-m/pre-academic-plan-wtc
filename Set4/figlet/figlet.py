from sys import argv,exit
from pyfiglet import figlet_format, Figlet
from random import choice

cmd_args = argv
fonts = Figlet().getFonts()
#text = input("Input: ")
if len(cmd_args) == 1:
    text = input("Input: ")
    _font = choice(fonts)
    output = figlet_format(text=text,font=_font)
elif len(cmd_args) == 3:
    [_,font_key,font] = argv
    if font_key not in ['-f','--font'] or font not in fonts:
        exit("Invalid usage")
    text = input("Input: ")
    output = figlet_format(text=text,font=font)
else:
    exit("Invalid usage")

print(output)
