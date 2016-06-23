from PIL import Image
from PIL import ImageDraw
i = Image.new('RGB', (540, 480))
im = i
img = i

pixels = img.load()  # create the pixel map
for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i, j] = 0, 0, 0  # (i * img.size[1] + j) % 5

im.save("out.png")
import scipy.misc
i = scipy.misc.imread('out.png')
print(i.shape)
print(i[:3, :3])
