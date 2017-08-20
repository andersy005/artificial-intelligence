import random
from agents import Agent 

random.seed("airtificial-seed")

def test_agent():
    a = Agent()
    assert isinstance(a, Agent)
