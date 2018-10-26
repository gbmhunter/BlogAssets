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

###################################################################################################
# CORRECTLY CHECKING FOR NONE IN CLASS INITIALIZATION
###################################################################################################

class Test:
    def __init__(self, my_str: Optional[str]) -> None:
        self.my_str = my_str

        # BAD: mypy doesn't recognize that self.my_str won't be None
        if my_str is None:
            self.my_str = 'abc'

        my_str2: str = self.my_str # ERROR HERE
    
class Test2:
    def __init__(self, my_str: Optional[str]) -> None:
        self.my_str = my_str

        # GOOD: mypy recognizes that self.my_str won't be None
        if self.my_str is None:
            self.my_str = 'abc'

        my_str2: str = self.my_str # No error here