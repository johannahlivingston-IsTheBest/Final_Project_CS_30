##############################################################################
# Title: photos
# Date: 12/17/2025
##############################################################################
"""Image-handling module that displays photos to the user."""
##############################################################################
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from exceptions import ImageError


def display_image(image_name):
    try:
        img = mpimg.imread(image_name)
    except FileNotFoundError:
        raise ImageError(f"Failed to generate image '{image_name}'")
    else:
        plt.imshow(img)
        plt.axis("off")
        plt.show()

display_image("silly-cat-photo.jpg")
