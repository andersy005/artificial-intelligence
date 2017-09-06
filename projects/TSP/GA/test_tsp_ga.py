import tsp_ga as tsp

cities =  tsp.Cities(5)
tours = tsp.alltours(cities)

def test_cities():
    assert isinstance(cities, frozenset)


def test_alltours():
    assert len(tours) == 24

def test_tour_length():
    assert tsp.tour_length(tours) != None

def test_plot():
    pass
