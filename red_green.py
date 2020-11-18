# Student Name:Shuhang Xue/ Yilun Liu
# HW5 red_green
# Aaron Bauer
# 2019 Fall CS111

import matplotlib.pyplot as plt


image = plt.imread("beach_portrait.png")[:, :, :3]


for i in range(len(image)):
    for j in range(len(image[i])):
        average_red_green = (image[i, j, 0] + image[i, j, 1]) / 2
        image[i, j, 0] = average_red_green              # Compute the average of the value of red and green in each pixel.
        image[i, j, 1] = average_red_green              # Set that average to each red and green.



plt.imsave("beach_portrait_red_green.png", image)
