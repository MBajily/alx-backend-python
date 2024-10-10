#!/usr/bin/env python3
"""Module for safely getting first element of a sequence."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safely get the first element of a sequence.

    Args:
        lst (Sequence[Any]): The input sequence

    Returns:
        Union[Any, None]: The first element of sequence or None if empty
    """
    if lst:
        return lst[0]
    else:
        return None
