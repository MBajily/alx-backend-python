#!/usr/bin/env python3
"""Module for zooming arrays with type checking."""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom in on an array by repeating each element.

    Args:
        lst (Tuple): The input tuple
        factor (int): The zoom factor

    Returns:
        List: The zoomed array
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
