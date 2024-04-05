from screeninfo import get_monitors

width = get_monitors()[0].width
height = get_monitors()[0].height

print("width: %s, Height: %s" % (width, height))