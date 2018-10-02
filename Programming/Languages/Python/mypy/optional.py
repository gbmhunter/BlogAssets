from typing import Any, Dict, Optional

###################################################################################################
# OPTIONAL CLASS VARIABLE
###################################################################################################
class A:
    my_var: Optional[str]= None

    def __init__(self) -> None:
        self.my_var = 'hello'

###################################################################################################
# TYPE DECLARATION BEFORE INITIALIZATION
###################################################################################################
class B:
    def __init__(self) -> None:
        # Can declare variable type first, and initialise it later
        self.my_var: str
        # Now initialize it
        self.my_var = 'hello'


###################################################################################################
# USING isinstance TO PREVENT TYPE ERRORS 
###################################################################################################
def accepts_optional(key: Optional[str]):
    my_dict: Dict[str, Any] = dict()

    # WRONG
    # try:
    #     print(my_dict[key])
    # except KeyError:
    #     pass

    # RIGHT
    if isinstance(key, str):
        print(my_dict[key])

###################################################################################################
# MYPY SMART ENOUGH TO REALISE str IS NOT NONE 
###################################################################################################

def test(my_str: Optional[str]):
    if my_str is None:
        my_str = 'abc'

    # GOOD: mypy recognizes that my_str cannot be None here
    my_str2: str = my_str     