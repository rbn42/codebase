from PIL import Image
from PIL import ImageDraw
i = Image.new('P', (540, 480))
im = i
img = i
print(i.palette)
im.putpalette([
    0, 0, 0,  # black background
    255, 0, 0,  # black background
    255, 0, 0,  # index 1 is red
    255, 255, 0,  # index 2 is yellow
    255, 153, 0,  # index 3 is orange
])

pixels = img.load()  # create the pixel map
for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i, j] = 0  # (i * img.size[1] + j) % 5

im.save("out.png")
import scipy.misc
i = scipy.misc.imread('out.png')
print(i.shape)
print(i[:3, :3])
