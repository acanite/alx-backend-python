#!/usr/bin/env python3
"""
This module contains the function definition for sum_mixed_list which takes a
list of possibly two types, integers or floats and returns their sum as float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return sum of numbers in mxd_lst
    """
    return sum(mxd_lst)
