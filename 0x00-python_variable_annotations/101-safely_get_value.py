#!/usr/bin/env python3
"""Module for safely getting a value from a dictionary with a default."""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Safely get a value from a dictionary with a default.

    Args:
        dct (Mapping): The input dictionary
        key (Any): The key to look up
        default (Union[T, None]): The default value to return if key not found

    Returns:
        Union[Any, T]: The value from the dictionary or the default
    """
    if key in dct:
        return dct[key]
    else:
        return default
