from typing import Tuple

###################################################################################################
# VARYING LENGTH TUPLE
###################################################################################################

# Using the ... operator to specify a Tuple of varying length
def print_values(my_tuple: Tuple[int, ...]) -> None:
    for value in my_tuple:
        print(value)

print_values((1, 2, 3))