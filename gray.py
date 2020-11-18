# Student Name:Shuhang Xue/ Yilun Liu
# HW5 grayscale
# Aaron Bauer
# 2019 Fall CS111


import matplotlib.pyplot as plt

# beach_portrait.png is an RGB image, so image is a 3D array with 3 values at each pixel location
# the slice is to remove an unnecessary alpha channel, if present

image = plt.imread("beach_portrait.png")[:, :, :3]

for line in image:
    for pixel in line:               # Loop over every pixel inside
        mean = pixel.mean()             # Compute the average of elements in each pixel
        for i in range(len(pixel)):
            pixel[i] = mean


# YOUR CODE HERE TO COVERT image TO GRAYSCALE


# save the data in gray_image as a grayscale image to a file called beach_portrait_gray.png

plt.imsave("beach_portrait_gray.png", image)
