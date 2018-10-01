from typing import Any, Dict, List, Union

# Type alias for a long, complicated type
MyTypeAlias = Union[str, Dict[str, Any], List[int]]

def my_fn(my_var: MyTypeAlias) -> None:
    pass