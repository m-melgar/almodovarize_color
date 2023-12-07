from typing import Union
import colorsys
import numpy as np
from PIL import Image


def hex2rgb(hex_value: str) -> tuple:
    """
    Converts hexadecimal color code to rgb value.
    :param hex_value: (str)
            String with hexadecimal color value
    :return:
    """
    h = hex_value.strip("#")
    rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    return rgb


def rgb2hex(rgb: tuple) -> str:
    """
    Converts RGB color value to hexadecimal
    :param rgb: tuple
            RGB color code
    :return:
    """
    r, g, b = rgb
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def almodovarize_color(colorcode: Union[str, tuple]) -> tuple:
    """
    Increase color saturation by code
    :param colorcode: str or tuple
            Color code in RGB or hexadecimal format
    :return:
    """

    assert type(colorcode) is str or tuple, f"Colorcode must be type str or tuple, not {type(colorcode)}"

    if type(colorcode) is str:
        r, g, b = hex2rgb(colorcode)
    else:
        r, g, b = colorcode

    r, g, b = r / 255, g / 255, b / 255
    hsv = colorsys.rgb_to_hsv(r, g, b)

    h, s, v = hsv
    s = 1.0

    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    r, g, b = round(r * 255), round(g * 255), round(b * 255)

    return r, g, b


def save_color(color: tuple, height: int = 200, width: int = 200, output_name: str = "image_color.jpeg") -> None:
    """
    Saves color given code into an image.
    :param color: tuple
            RGB color code
    :param height: int
            Output image height in pixels
    :param width: int
            Output image height in pixels
    :param output_name: str
            Output file name.
    :return:
    """
    image_blank = np.ones((height, width, 3))
    image_blank = image_blank * color
    image_blank = image_blank.astype(np.uint8)

    image = Image.fromarray(image_blank)
    image.save(output_name)


if __name__ == '__main__':
    color = almodovarize_color("#ad9fc0")
    print(rgb2hex(color))

    save_color(color=color, height=200, width=200)

    # height, width, channels = (200, 200, 3)
    # image_blank = np.ones((height, width, channels))
    # image_blank = image_blank * color
    # image_blank = image_blank.astype(np.uint8)
    #
    # image_filename = "image_color.jpeg"
    # image = Image.fromarray(image_blank)
    # image.save(image_filename)
