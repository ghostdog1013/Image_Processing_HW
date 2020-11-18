# Student Name:Shuhang Xue/ Yilun Liu
# HW5 blue_screen
# Aaron Bauer
# 2019 Fall CS111

# We did the OPTIONAL Improved Blue Screening
# We commented out the required part. We leave the better version open below
# When running the program, it should provide the optimized version of the assignment.



import matplotlib.pyplot as plt
import numpy as np


# oz_bluescreen and meadow are a RGB images, so image and background are 3D arrays
# and have 3 values at every pixel location
# the slice is to remove an unnecessary alpha channel, if present

image = plt.imread("oz_bluescreen.png")[:, :, :3]
background = plt.imread("meadow.png")[:, :, :3]



# for i in range(len(image)):
#     for j in range(len(image[i])):
#         if image[i, j, 2] > (image[i, j, 0] + image[i, j, 1]):
#             image[i, j] = background[i, j]




for i in range(len(image)):
    for j in range(len(image[i])):
        if image[i, j, 2] > (image[i, j, 0] + image[i, j, 1]) * 0.9 and image[i, j, 2] > 0.15:
            image[i, j] = background[i, j]      # The first conditional optimizes the viweing of the background
                                                # grass (eliminating blue dots on the grass). The second conditional
                                                # optimizes the flaw on that person's face and clothes.  



# save the modified image to a new file called oz_meadow.png
plt.imsave("oz_meadow.png", image)
