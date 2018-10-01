####################################################################################################
# SELF REFERENCE
####################################################################################################

class A:
    # RIGHT: Enclose type in string if self-referencing. If you don't, Python v3.6 or lower
    # will complain!
    @classmethod
    def factory(cls) -> 'A':
        return A()

    def say_hello(self):
        print('hello')

my_a = A.factory()
my_a.say_hello()

####################################################################################################
# FORWARD REFERENCE
####################################################################################################

def my_func(my_b: 'B') -> None:
    pass

class B:
    pass
    
my_func(B())