"""Image-handling module that displays photos to the user."""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def display_image(image_name):
    try:
        img = mpimg.imread(image_name)
    except FileNotFoundError:
        print("AAAAAAAAAAAA")
    else:
        plt.imshow(img)
        plt.axis("off")
        plt.show()

display_image("mdowaid")