import tsp_ga as tsp

cities =  tsp.Cities(5)

def test_cities():
    assert isinstance(cities, frozenset)


def test_alltours():
    assert len(tsp.alltours(cities)) == 24
