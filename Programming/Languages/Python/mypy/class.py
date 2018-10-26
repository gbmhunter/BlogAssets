from typing import List

class Animal:
    pass

class Cat(Animal):
    pass

# RIGHT: Of course!
animals: List[Animal] = [Animal(), Animal()]

# RIGHT: Of course!
cats: List[Cat] = [Cat(), Cat()]

# WRONG: List[T] is invariant, cannot assign List[Animal] to List[Cat]
wrong_1: List[Cat] = animals

# WRONG: List[T] is invariant, cannot assign List[Animal] to List[Cat]
wrong_2: List[Animal] = cats

# RIGHT: A list can store elements which are subtypes
animal_type_stores_cats: List[Animal] = [Cat(), Cat()]

# WRONG: A list cannot store elements which are supertypes
cat_type_stores_animals: List[Cat] = [Animal(), Animal()]