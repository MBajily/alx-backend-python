#!/usr/bin/env python3
"""Module for creating a tuple from a string and number."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple from a string and a number.

    Args:
        k (str): The string to use as first element
        v (Union[int, float]): The number to square for second element

    Returns:
        Tuple[str, float]: Tuple containing string and squared number
    """
    return (k, float(v ** 2))
