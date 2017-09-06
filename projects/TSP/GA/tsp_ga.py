import random
import time
import statistics
import itertools
import functools
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('seaborn')
import numpy as np




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


def tour_length(tours):
    "The total of distances between each pair of consecutive cities in the tour."
    dist_air = []
    for i in range(len(tours)):
        dist_air.append(sum([distance(tours[i][j], tours[i][j-1]) for j in range(len(tours[i]))]))

    return dist_air



#---------------------- Plotting------------------------------------#
def plot_tour(tour):
    "Plot the cities as circles and the tour as lines between them."
    plot_lines(list(tour) + [tour[0]])

def plot_lines(points, style='bo-'):
    "Plot lines to connect a series of points."
    plt.plot([p.x for p in points], [p.y for p in points], style)
    plt.axis('scaled'); plt.axis('off')
    plt.show()



if __name__ == "__main__":
    cities = Cities(5)
    #print(cities)
    #print(alltours(cities))
    tour_length(alltours(cities))
    for i in alltours(cities):
        plot_tour(i)
