import numpy
from PIL import Image, ImageDraw


class CircleImageCreator:
    def __init__(self, image_path: str, save_to_path: str = "image_storage/result.png"):
        self._image_path = image_path
        self.save_to_image_path = save_to_path

    def _image_rounder(self):
        """
        Rounds the resulting image.
        :return:
        """
        try:
            image = Image.open(self._image_path).convert("RGB")
        except (Exception, BaseException):
            raise
        numpy_image = numpy.array(image)
        height, weight = image.size
        alpha_size = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(alpha_size)
        draw.pieslice([0, 0, height, weight], 0, 360, fill=255)
        numpy_alpha_size = numpy.array(alpha_size)
        numpy_image = numpy.dstack((numpy_image, numpy_alpha_size))
        Image.fromarray(numpy_image).save(self.save_to_image_path)

    def _resize_image(self, size: int, resample: int):
        """
        Resize image.
        :param size: PIL thumbnail size.
        :param resample: PIL thumbnail resample.
        :return:
        """
        image = Image.open(self.save_to_image_path)
        image.thumbnail((size, resample))
        image.save(self.save_to_image_path)

    def create_default_image_for_sightly_cv(self, size: int = 300, resample: int = 300):
        """
        Create default circle image.
        :param size:
        :param resample:
        :return: Result image path.
        """
        self._image_rounder()
        self._resize_image(size, resample)
        return self.save_to_image_path
