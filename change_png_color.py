# source: https://stackoverflow.com/questions/3752476/python-pil-replace-a-single-rgba-color

from PIL import Image
import numpy as np
    
def x():

    im = Image.open('test.png')
    im = im.convert('RGBA')

    data = np.array(im)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

    # Replace white with red... (leaves alpha values alone...)
    # Hue icon use RGB(16, 16, 16)
    black_areas = (red == 16) & (blue == 16) & (green == 16)
    data[..., :-1][black_areas.T] = (200, 200, 200) # Transpose back needed

    im2 = Image.fromarray(data)
    im2.save('test_white.png')
    im2.show()

if __name__ == "__main__":
    x()