from PIL.Image import Image
from typing import Sequence
import ipywidgets as widgets
import matplotlib.pyplot as plt


class ImageViewer:
    def __init__(self, images: Sequence[Image], keep_axis: bool = False):
        """A lightweight image viewer designed for use in interactive notebook.

        This class requires `%matplotlib widget` to be enabled within the notbook session.

        Args:
            pil_images (list of PIL images): A list of PIL images.
            keep_axis (bool, optional): Display the upper and lower ticks of axis when displaying
                                        image. Defaults to False.
        """

        assert len(images) > 0, "List of images cannot be empty."
        assert all(isinstance(i, Image) for i in images), "All images must be PIL.Image type."

        self.index = 0
        self.images = images
        self.num_images = len(images)
        self._keep_axis = keep_axis

        # create the initial UI and display the first image
        self._create_ui()
        self._update_image()

    def _create_ui(self):
        """Create initial UI for image viewer."""
        plt.ioff()
        self.fig = plt.figure()
        plt.ion()

        # display first image in list
        self.im = plt.imshow(self.images[0])

        # remove margins, axis, header, footer
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.margins(0, 0)

        if self._keep_axis:
            plt.axis("off")
            plt.gca().xaxis.set_major_locator(plt.NullLocator())
            plt.gca().yaxis.set_major_locator(plt.NullLocator())

        self.fig.canvas.footer_visible = False
        self.fig.canvas.header_visible = False

        # create status label
        self._status = widgets.Label(value=f"Image [{self.index+1}/{self.num_images}]:")

        # create buttons
        self._prev_button = widgets.Button(
            description="",
            disabled=False,
            button_style="",  # 'success', 'info', 'warning', 'danger' or ''
            tooltip="Previous",
            icon="arrow-left",  # (FontAwesome names without the `fa-` prefix)
            layout=widgets.Layout(width="80px", height="28px"),
        )
        self._next_button = widgets.Button(
            description="",
            disabled=False,
            button_style="",  # 'success', 'info', 'warning', 'danger' or ''
            tooltip="Next",
            icon="arrow-right",
            layout=widgets.Layout(width="80px", height="28px"),
        )

        # add functions to buttons
        self._prev_button.on_click(self._prev_button_event)
        self._next_button.on_click(self._next_button_event)

        # skip to image
        self._skip_to_index = widgets.Text(
            value="",
            placeholder="Type in image index",
            description="",
            disabled=False,
            layout=widgets.Layout(width="150px", height="28px"),
        )
        self._skip_button = widgets.Button(
            description="",
            disabled=False,
            button_style="",
            tooltip="Skip to image.",
            icon="search",
            layout=widgets.Layout(width="80px", height="28px"),
        )

        self._skip_button.on_click(self._go_to_index)

        # create bottom bar
        bottom_bar = widgets.HBox(
            [
                self._status,
                self._prev_button,
                self._next_button,
                self._skip_to_index,
                self._skip_button,
            ]
        )

        self._ui = widgets.VBox(children=(self.fig.canvas, bottom_bar))
        display(self._ui)

    def _update_status(self):
        """Update the status label with the current image index."""
        self._status.value = f"Image [{self.index+1}/{self.num_images}]:"

    def _prev_button_event(self, event):
        """Load the previous image in list and display.

        Args:
            event ([type]): The widget that is connected to this event function. Currently unused.

        """
        self._update_index(-1)
        self._update_image()

    def _next_button_event(self, event):
        """Load the next image in list and display.

        Args:
            event ([type]): The widget that is connected to this event function. Currently unused.
        """
        self._update_index(1)
        self._update_image()

    def _update_index(self, update_val):
        """Handles updating the image index so that boundary errors dont occur.

        Args:
            update_val (int): The value to update the image index by.
        """
        self.index += update_val
        self.index = max(0, min(self.index, self.num_images - 1))

    def _go_to_index(self, event):
        """Update image index and draw image.

        Args:
            event ([type]): The widget that is connected to this event function. Currently unused.
        """
        self.index = int(self._skip_to_index.value) - 1
        self._update_index(0)
        self._update_image()

    def _update_image(self):
        """Draw image at image index on the canvas UI."""
        image = self.images[self.index]

        self._update_status()

        self.im.set_data(image)
        self.fig.canvas.draw_idle()
