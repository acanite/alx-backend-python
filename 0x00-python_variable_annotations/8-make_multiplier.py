#!/usr/bin/env python3
"""
This module contains the definition of make_multiplier which returns a callable
function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a callable function that returns the multiple of the multiplier
    argument and the value passed to it
    """
    def times_multiplier(factor: float) -> float:
        """
        Return multiplier * factor
        """
        return multiplier * factor
    return times_multiplier
