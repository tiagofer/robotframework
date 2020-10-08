from typing import Optional, Union

def with_optional_argument(arg: Optional[int], expected='unexpected'):
    assert arg == expected

def unescaped_optionalism(arg: Optional[float]=None):
    assert isinstance(arg, float)

def union_of_int_float_and_string(arg: Union[int, float, str], expected):
    assert arg == expected