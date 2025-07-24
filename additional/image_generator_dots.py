from PIL import Image, ImageDraw

size = 2048
radius = 80
step = 320
margin = 200

image = Image.new("L", (size, size), 0)
draw = ImageDraw.Draw(image)

for y in range(margin, size, step):
    for x in range(margin, size, step):
        draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=255)

image.save("lithosim_input.png", compress_level=0)
