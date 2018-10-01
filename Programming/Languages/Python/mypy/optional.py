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
