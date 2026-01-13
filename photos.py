##############################################################################
# Title: photos
# Date: 12/19/2025
##############################################################################
"""Image-handling module that displays photos to the user."""
##############################################################################
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pathlib


class ImageError(Exception):
    """Error when image fails to display."""
    def __init__(self, msg):
        self.msg = msg


def display_image(image_name):
    """Display an image on the screen.
    
    Parameters:
        image_name (str): name of image without file path
    """
    images_folder = pathlib.Path("Images")
    image_path = images_folder / image_name
    if image_path.exists():
        img = mpimg.imread(image_path)
        plt.imshow(img)
        plt.axis("off")
        plt.show()
    else:
        raise ImageError(f"Failed to generate image '{image_name}'. Did you forget the file extension (.jpg, .png)?")


if __name__ == "__main__":
    display_image("silly-cat-photo.jpg")
