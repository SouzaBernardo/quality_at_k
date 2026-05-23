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
        :return: PIL.Image.Image
        """
        self.image = Image.open(image_path)
        return self.image

    def save_image(self, save_path):
        if self.image:
            image = self.image
            image = image.resize(int(width), int(height))
            image = image.rotate(degrees)
            image = image.brightness(factor)
            image.save(save_path)

    def resize_image(self, width, height):
        """
        Resize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image:
            image = self.image
            width = int(width)
            height = int(height)
            new_width = image.size[0]
            new_height = image.size[1]
            if new_width > width:
                new_width = width
                new_height = int(new_width / new_width * height)
            elif new_height > height:
                new_height = height
                new_width = int(new_height * width / new_height)
            image = Image.open(image)
            image = image.resize((new_width, new_height))
            self.image = image

    def rotate_image(self, degrees):
        """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(90)
        >>> processor.rotate_image(90)
        """
        if self.image:
            image = Image.open(self.image)
            image = image.rotate(degrees)
            self.image = image.save(self.image)

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
        if self.image is not None:
            image = Image.open(self.image)
            image = image.convert('RGB')
            image = image.filter(ImageFilter.GRAYSCALE)
            image = image.point(lambda p: (p[0]*factor, p[1]*factor))
            image.save('temp.png')
            self.image = 'temp.png'