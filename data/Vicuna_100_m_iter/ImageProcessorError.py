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
        :param image_path: str, path of image that is to be loaded
        :return: None
        >>> processor.load_image('test.jpg')
        >>> processor.image
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>

    def save_image(self, save_path):
        # Open the image
        image = Image.open(self.image)
    
        # Save the image with the given path
        image.save(save_path)

    def resize_image(self, width, height):
        """
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image is not None:
            image = Image.open(self.image)
            image = image.resize((width, height))
            image = image.convert("RGB")
            self.image = image

    def rotate_image(self, degrees):
            """
            rotate image if image has opened
            :param degrees: float, the degrees that the image will be rotated
            """
            if self.image is not None:
                image = Image.open(self.image)
                image = image.rotate(degrees)
                image = image.convert("RGB")
                self.image = image

    def adjust_brightness(self, factor):
        """
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        """
        if self.image is not None:
            image = Image.open(self.image)
            image = image.filter(ImageFilter.BRIGHTNESS, factor)
            image = image.convert("RGB")
            self.image = image