import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from tsp_ga import *

cities =  Cities(5)
tours = alltours(cities)

def test_cities():
    assert isinstance(cities, frozenset)


def test_alltours():
    assert len(tours) == 24

def test_tour_length():
    assert tour_length(tours) != None

def test_plot():
    pass
