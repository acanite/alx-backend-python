#!/usr/bin/env python3
from typing import Dict, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Dict, key: Any, default: T) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
