from PIL import Image, ImageEnhance, ImageChops
class ImageProcessor: 
    def __init__(self):
        """
        Initialize self.image
        """
        self.image = None



    def load_image(self, image_path):
        """
        Use Image util in PIL to open an image
        :param image_path: str, path of the image that is to be loaded
        >>> processor.load_image('test.jpg')
        >>> processor.image
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
        """
        self.image = Image.open(image_path)


    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        >>> processor.load_image('test.jpg')
        >>> processor.save_image('test2.jpg')
        """
        if self.image is not None:
            self.image.save(save_path)
        else:
            print("No image has been loaded.")
    

    def resize_image(self, width, height):
        """
        Resize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image is not None:
            self.image = self.image.resize((width, height))
    

    def rotate_image(self, degrees):
        """
        Rotate the image if it has been loaded
        :param degrees: float, the degrees that the image will be rotated
        """
        if self.image is not None:
            self.image = self.image.rotate(degrees)
        else:
            print("No image has been loaded.")
    

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
        if self.image is not None:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)
        else:
            print("No image loaded. Please load an image first using the 'load_image' method.")