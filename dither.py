# Student Name:Shuhang Xue/ Yilun Liu
# HW5 ditter
# Aaron Bauer
# 2019 Fall CS111


import matplotlib.pyplot as plt


image = plt.imread("beach_portrait.png")[:, :, :3]

for row in image:
    for pixel in row:
        mean = pixel.mean()
        for i in range(len(pixel)):             # Make the picture gray.
            pixel[i] = mean


def dither(image):
    image_dither = image.copy()                 # copy the gray image.
    number_lines = len(image)                   # Compute the length of the lines and size of the volume.
    number_columns = len(image[0])
    for i in range(len(image_dither)):          # 1. Loop over all pixels as always, from top to bottom and within each row, from left to right.
        for j in range(len(image_dither[i])):
            if image_dither[i, j, 0] > 0.5:         # Perform the operation on the copied image. 
                image_dither[i, j] = 1.0               # 2. if its value is larger than 0.5, then set it to 1.0 (pure white). Otherwise, set it to 0 (pure black)
                error = image[i, j, 0] - image_dither[i, j, 0]
                if j+1 <= number_columns - 1:
                    image_dither[i, j+1] += error * 7/16            # 3. Distribute this pixel’s error to adjacent pixels.
                if j+1 <= number_columns - 1 and i+1 <= number_lines - 1:
                    image_dither[i+1, j+1] += error * 1/16
                if i+1 <= number_lines - 1:
                    image_dither[i+1, j] += error * 5/16
                if i+1 <= number_lines - 1 and j-1 <= 0:
                    image_dither[i+1, j-1] += error * 3/16
            else:
                image_dither[i, j] = 0
                error = image[i, j, 0] - image_dither[i, j, 0]
                if j+1 <= number_columns - 1:
                    image_dither[i, j+1] += error * 7/16
                if j+1 <= number_columns - 1 and i+1 <= number_lines - 1:
                    image_dither[i+1, j+1] += error * 1/16
                if i+1 <= number_lines - 1:
                    image_dither[i+1, j] += error * 5/16
                if i+1 <= number_lines - 1 and j-1 <= 0:
                    image_dither[i+1, j-1] += error * 3/16

    return image_dither

plt.imsave("beach_portrait_dither.png", dither(image))
