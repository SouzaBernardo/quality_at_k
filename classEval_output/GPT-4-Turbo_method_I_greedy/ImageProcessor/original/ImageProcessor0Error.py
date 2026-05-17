from PIL import Image, ImageEnhance, ImageChops
class ImageProcessor: 
    def __init__(self):
        """
        Initialize self.image
        """
        self.image = None


    def load_image(self, image_path):
        """
        Use Image util in PIL to open a image
        :param image_path: str, path of image that is to be
        """
        try:
            self.image = Image.open(image_path)
        except IOError:
            print("Unable to load image")
        return self.image
    def save_image(self, save_path):
        """
        Save image to a path if image has been opened
        :param save_path: str, the path that the image will be saved
        """
        if self.image is not None:
            try:
                self.image.save(save_path)
                print(f"Image saved at {save_path}")
            except IOError:
                print("Unable to save image")
        else:
            print("No image loaded to save")
    def resize_image(self, width, height):
        """
        Resize the image if image has been opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image is not None:
            try:
                self.image = self.image.resize((width, height))
                print(f"Image resized to {width}x{height}")
            except Exception as e:
                print(f"Unable to resize image: {e}")
        else:
            print("No image loaded to resize")
    def rotate_image(self, degrees):
        """
        Rotate the image if image has been opened.
        :param degrees: float, the degrees that the image will be rotated
        """
        if self.image is not None:
            try:
                self.image = self.image.rotate(degrees)
                print(f"Image rotated by {degrees} degrees")
            except Exception as e:
                print(f"Unable to rotate image: {e}")
        else:
            print("No image loaded to rotate")
    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
        if self.image is not None:
            try:
                enhancer = ImageEnhance.Brightness(self.image)
                self.image = enhancer.enhance(factor)
                print(f"Brightness adjusted by a factor of {factor}")
            except Exception as e:
                print(f"Unable to adjust brightness: {e}")
        else:
            print("No image loaded to adjust brightness")
