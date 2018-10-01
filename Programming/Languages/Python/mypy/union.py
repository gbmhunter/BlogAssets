from typing import Union

my_union: Union[str, int] = 'abc'

# RIGHT: Union of stricter type can be assigned to union of looser type
my_looser_union: Union[str, int, float] = my_union

# WRONG: Union of looser type cannot be assigned to union of stricter type
my_tighter_union: Union[str] = my_union