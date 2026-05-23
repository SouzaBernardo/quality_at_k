from PIL import Image, ImageEnhance
class ImageProcessor: 
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
            image = Image.open(image_path)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None, None
    
        self.image = image
        return image, None

    def save_image(self, save_path):
        if self.image is not None:
            self.image.save(save_path, Image.mode('RGB'))

    def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image is None:
            # Load the image
            self.load_image('test.jpg')
    
        # Resize the image
        self.save_image('resize_image.jpg')
        self.rotate_image(90)
        self.adjust_brightness(1.0)
        self.save_image('resize_image_ adjusted.jpg')

    def rotate_image(self, degrees, factor=1.0):
        """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        :param factor: float, the brightness adjustment
        """
        if not self.image:
            self.image = ImageProcessor()
        
        self.image.resize_image((self.image.width, self.image.height), (int(self.image.width * factor), int(self.image.height * factor)))
        
        self.image.save_image('rotated_image.jpg')

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
        if self.image is None:
            return
        
        image = self.image
        image = image.convert('L')  # convert image to grayscale
        image = image.convert('RGB')  # convert back to RGB
        
        new_image = image.convert('RGB')  # convert to new image
        new_image = new_image.convert('L')  # convert to grayscale
        
        new_image = new_image.convert('RGB')  # convert back to RGB
        
        new_image = new_image.convert('B')  # adjust brightness
        
        new_image = new_image.convert('RGB')  # convert back to RGB
        
        new_image = self.image.convert('RGB')  # convert back to original image
        
        if factor == 0.0:
            new_image = image
        elif factor == 1.0:
            new_image = new_image
        else:
            raise ValueError("Invalid brightness factor")
        
        self.image = new_image