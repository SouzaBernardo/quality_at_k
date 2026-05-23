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
        :return: None, None
        """
        try:
            self.image = Image.open(image_path)
        except:
            print("Error loading image: ", image_path)
            return None
        return self.image

    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        :return: None
        """
        try:
            self.image = Image.open(save_path)
            self.image.save('image_path', Image.mode_RGB)
        except:
            print("Error saving image: ", save_path)
            return None

    def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        try:
            self.image = Image.open(self.load_image('test.jpg'))
            self.image = self.image.resize((width, height))
            self.image = self.image.resize((width, height), Image.mode_RGB)
        except:
            print("Error resizing image: ", self.load_image('test.jpg'))
            return

    def rotate_image(self, degrees):
        """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        :return: str, the new path of the image
        """
        new_path = self.save_image(self.load_image('test.jpg'))
        new_path = f"{self.image.filename}.jpg"
        return new_path

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        :return: None
        """
        try:
            self.image = Image.open(self.load_image('test.jpg'))
            self.image = self.image.resize((width, height))
            self.image = self.image.resize((width, height), Image.mode_RGB)
            self.image = self.image.rotate_image(degrees=self.rotate_image(self.load_image('test.jpg')))
            self.image = self.image.adjust_brightness(factor=factor)
            self.save_image(self.load_image('test.jpg'))
        except:
            print("Error adjusting brightness: ", self.load_image('test.jpg'))
            return None