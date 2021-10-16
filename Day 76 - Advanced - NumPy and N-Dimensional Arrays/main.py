# Code for Day 76

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image

###################################################################################################

my_1d_array = np.array([1.1, 9.2, 8.1, 4.7])
# print(my_1d_array.ndim)

my_2d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(my_2d_array.ndim)
# print(my_2d_array[1, 2])
# print(my_2d_array[0, :])

mystery_array = np.array(
    [
        [
            [0, 1, 2, 3],
            [4, 5, 6, 7]
        ],
        [
            [7, 86, 6, 98],
            [5, 1, 0, 4]
        ],
        [
            [5, 36, 32, 48],
            [97, 0, 27, 18]
        ]
    ]
)

# print(mystery_array.ndim)
# print(mystery_array.shape)
# print(mystery_array[2, 1, 3])
# print(mystery_array[:, :, 0])

###################################################################################################

a = np.arange(10, 30)
# print(a)

# print(a[-3:])
# print(a[3:6])
# print(a[12:])
# print(a[::2])

# print(np.flip(a))

b = np.array([6, 0, 9, 0, 0, 5, 0])
# print(np.nonzero(b))

c = np.random.random((3, 3, 3))
# print(c.shape)

x = np.linspace(0, 100, num=9)
# print(x)

y = np.linspace(start=3, stop=3, num=9)
# plt.plot(x, y)
# plt.show()

noise = np.random.random((128, 128, 3))
# print(noise.shape)
# plt.imshow(noise)
# plt.show()

###################################################################################################

a1 = np.array(
    [
        [1, 3],
        [0, 1],
        [6, 2],
        [9, 7]
    ]
)

b1 = np.array(
    [
        [4, 1, 3],
        [5, 8, 5]
    ]
)

c = np.matmul(a1, b1)
# print(c, c.shape)

###################################################################################################

# img = misc.face()
img = np.array(Image.open('yummy_macarons.jpg'))


# plt.imshow(img)
# plt.show()

# print(type(img), img.shape, img.ndim)

sRGB = img / 255
grey_vals = np.array([0.2126, 0.7152, 0.0722])
img_gray = np.matmul(sRGB, grey_vals)
# plt.imshow(img_gray, cmap='gray')
# plt.show()

# plt.imshow(np.flip(img_gray), cmap='gray')
# plt.show()

# plt.imshow(np.rot90(img), cmap='gray')
# plt.show()

# plt.imshow(255 - img)
# plt.show()
