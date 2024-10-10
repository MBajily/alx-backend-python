#!/usr/bin/env python3
"""Module for creating a function that multiplies a float by multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by multiplier.

    Args:
        multiplier (float): The multiplier to use

    Returns:
        Callable[[float], float]:
        A function that multiplies a float by multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
