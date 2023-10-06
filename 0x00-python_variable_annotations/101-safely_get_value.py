#!/usr/bin/env python3
"""
This method contains the definition for safely_get_value which is a
type-annotated function
"""
from typing import Dict, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Dict, key: Any, default: T) -> Union[Any, T]:
    """
    Returns an object in the dictionary that maps to the specified key, else
    return the specified default or None
    """
    if key in dct:
        return dct[key]
    else:
        return default
