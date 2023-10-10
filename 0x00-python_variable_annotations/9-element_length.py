#!/usr/bin/env python3
"""
This module contains a type-annotated function 'element_length' that returns
a tuple of each item in a list and  the length of that element
"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return list of tuple of each element and its length in lst
    """
    return [(i, len(i)) for i in lst]
