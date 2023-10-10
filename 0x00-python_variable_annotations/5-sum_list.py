#!/usr/bin/env python3
"""
This module contains the definition of 'sum_list' a type-annotated function
that accepts a list of floats and returns their sum
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the list of floats in the 'input_list' argument
    """
    return sum(input_list)
