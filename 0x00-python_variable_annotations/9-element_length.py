#!/usr/bin/env python3
"""Module for getting lengths of elements in an iterable."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of elements in an iterable.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences

    Returns:
        List[Tuple[Sequence, int]]:
        List of tuples containing sequences and their lengths
    """
    return [(i, len(i)) for i in lst]
