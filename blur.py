# Student Name:Shuhang Xue/ Yilun Liu
# HW5 blur
# Aaron Bauer
# 2019 Fall CS111

import matplotlib.pyplot as plt

# beach_portrait_gray.png is an RGB image, so image is a 3D array with 3 values at each pixel location
# the slice is to remove an unnecessary alpha channel, if present

image = plt.imread("beach_portrait.png")[:, :, :3]


def blur(img, radius):
    # YOUR CODE HERE TO PRODUCE AND RETURN A NEW array THAT IS A BLURRED VERSION OF img
    new_img = img.copy()
    for i in range(len(img)):
        for j in range(len(img[i])):

            average_red = img[max(0, i - radius) : max(0, i + radius), max(0, j - radius) : max(0, j + radius), 0].mean()
            average_green = img[max(0, i - radius) : max(0, i + radius), max(0, j - radius) : max(0, j + radius), 1].mean()
            average_blue = img[max(0, i - radius) : max(0, i + radius), max(0, j - radius) : max(0, j + radius), 2].mean()

            new_img[max(0, i - radius) : max(0, i + radius), max(0, j - radius) : max(0, j + radius), 0] = average_red
            new_img[max(0, i - radius) : max(0, i + radius), max(0, j - radius) : max(0, j + radius), 1] = average_green
            new_img[max(0, i - radius) : max(0, i + radius), max(0, j - radius) : max(0, j + radius), 2] = average_blue

            # The 'max' function prevents any errors when slicing on the border.
            # The three 'average' variables are computed and assigned as the mean of the surrounding pixels.
            # The 'copy' on line 16 forces the operation (computation of the means) only on the original image, preventing blurring the image multiple times.

    return new_img

plt.imsave("beach_portrait_blur.png", blur(image, 3))
