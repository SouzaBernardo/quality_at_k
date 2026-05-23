from PIL import Image, ImageEnhance, ImageChops
class ImageProcessor: 
    def __init__(self):
        """
        Initialize self.image
        """
        self.image = None



    def load_image(self, image_path):
        
        self.image = Image.open(image_path)


    def save_image(self, save_path):


    def resize_image(self, width, height):


    def rotate_image(self, degrees):


    def adjust_brightness(self, factor):