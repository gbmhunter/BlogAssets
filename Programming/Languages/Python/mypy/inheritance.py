from typing import List

class A:
    pass

class B(A):
    def b_fn(self, msg: str) -> None:
        print(str)

class C(B):
    pass

def print_b(b_obj: B):
    b_obj.b_fn('hello')

# RIGHT: We can add instances of the exact declared type of the list
print_b(B())

# RIGHT: We can also add instances of B since it is a subclass of A
print_b(C())

# WRONG: We can't add instance of A since it is superclass of B
print_b(A()) 