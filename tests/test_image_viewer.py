import unittest
import numpy as np
from PIL import Image
from time import time

from nbgizmos import ImageViewer


class TestImageViewer(unittest.TestCase):

    # def test_image_switch_speed(self, time_bar=500, image_size=(1000, 1000), num_switches=10):
    #     """Expect the time between image switching to be below 500ms."""
    #     # create two useable images
    #     non_pil_image = np.random.randint(0, 255, size=image_size, dtype='uint8')
    #     pil_image = Image.fromarray(non_pil_image)
    #     images = [pil_image, pil_image]

    #     # create instance of ImageViewer
    #     image_viewer = ImageViewer(images)

    #     start_time = time()
    #     for i in range(num_switches):
    #         # go to index updates the internal index and displays image
    #         image_viewer._go_to_index(None, (i+1) % 2)  # add 1 bc it starts at 0
    #     total_time = time() - start_time

    #     avg_time = total_time / num_switches

    #     self.assertLess(avg_time, time_bar)

    def test_pil_image_input(self, image_size=(1000, 1000)):
        """Give PIL Image inputs to class."""
        # create two useable images
        non_pil_image = np.random.randint(0, 255, size=image_size, dtype="uint8")
        pil_image = Image.fromarray(non_pil_image)
        images = [pil_image, pil_image]

        # create instance of ImageViewer
        _ = ImageViewer(images)  # this should NOT fail

    @unittest.expectedFailure
    def test_non_pil_image_input(self, image_size=(1000, 1000)):
        """Give non-PIL image input class."""
        non_pil_image = np.random.randint(0, 255, size=image_size, dtype=int)

        images = [non_pil_image, non_pil_image]

        # create instance of ImageViewer
        _ = ImageViewer(images)  # this should fail here


if __name__ == "__main__":
    unittest.main()
