import random

hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
print("Random HEX color:", hex_color)
