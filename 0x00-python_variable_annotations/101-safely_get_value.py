#!/usr/bin/env python3
"""
This module contains the definition for 'safely_get_values' which safely
retieves the value in the dictionary that maps to the specified key if it
exists, else it returns the specified default
"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """
    Return value mapping t okey if it exists, else return default
    """
    if key in dct:
        return dct[key]
    else:
        return default
