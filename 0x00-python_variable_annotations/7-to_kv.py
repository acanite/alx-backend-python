#!/usr/bin/env python3
"""
This module contains the definition of the type-annotates the function 'to_kv'
which returns a tuple of a string and a float
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return tuple of k and square of v
    """
    return (k, (v * v))
