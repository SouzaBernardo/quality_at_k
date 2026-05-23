from PIL import Image, ImageEnhance

class ImageProcessor:
    """
    This is a class to process image, including loading, saving, resizing, rotating, and adjusting the brightness of images.
    """

    def __init__(self):
        """
        Initialize self.image
        """
        self.image = None

    def load_image(self, image_path):
        """
        Use Image util in PIL to open a image
        :param image_path: str, path of image that is to be
        >>> processor.load_image('test.jpg')
        >>> processor.image
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
        """
        return self.image

    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        >>> processor.load_image('test.jpg')
        >>> processor.save_image('test2.jpg')
        """
        return self.image

    def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        return self.image.resize((width, height))

    def rotate_image(self, degrees):
        """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        """
        return self.image.rotate(degrees)

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        """
        return self.image.adjust_brightness(factor)


# Create an instance of the ImageProcessor class
image_Processor = ImageProcessor()

# Load an image into the processor
image_Processor.load_image('test.jpg')

# Save the image to a new file
image_Processor.save_image('processed_test.jpg')

# Resize the image
image_Processor.resize_image(300, 300)

# Rotate the image
image_Processor.rotate_image(90)

# Adjust the brightness of the image
image_Processor.adjust_brightness(0.5)

# Save the processed image to a new file
image_Processor.save_image('processed_test_rotated.jpg')