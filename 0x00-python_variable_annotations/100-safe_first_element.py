#!/usr/bin/env python3
"""
This module contains the function definition for 'safe_first_element'
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of lst if it's not empty
    """
    if lst:
        return lst[0]
    else:
        return None
