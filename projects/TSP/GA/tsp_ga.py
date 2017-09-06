import random
import time
import statistics
import itertools
import functools

#------------------- Representing Cities--------------------------#
class Point(complex):
    """Cities are represented as Points,
    which are a subclass of complex numbers."""


    x = property(lambda p: p.real)
    y = property(lambda p: p.imag)

City = Point


def Cities(n, width=900, height=600, seed=1234):
    "Make a set of n cities, each with random coordinates within a (width x height) rectangle."
    random.seed(seed * n)
    return frozenset((City(random.randrange(width), random.randrange(height))
                     for c in range(n)))


#-------------------Distance Between two cities ------------------#
def distance(A, B):
    """Function to calculate the distance between two points"""
    return abs(A - B)


#------------------------ Tours----------------------------------#
def alltours(cities):
    """Return a list of tours, each a permutation of cities, but
    each one starting with the same city.

    So let's arbitrarily say that all tours must start with the first city in
    the set of cities. We'll just pull the first city out, and then tack
    it back on to all the permutations of the rest of the cities.
    This helps us keep all non-redundant tours only.
    """
    start = first(cities)
    return [[start] + Tour(rest)
           for rest in itertools.permutations(cities - {start})]

def first(collection):
    """Start iterating over collection, and return the first element
    """
    return next(iter(collection))

Tour = list  # Tours are implemented as lists of cities.




if __name__ == "__main__":
    cities = Cities(3)
    print(cities)
    print(alltours(cities))
