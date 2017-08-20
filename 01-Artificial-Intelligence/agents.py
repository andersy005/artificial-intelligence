"""Implement Agents and Environments (Chapters 1-2).
The class hierarchies are as follows:
Thing ## A physical object that can exist in an environment
    Agent
        Wumpus
    Dirt
    Wall
    ...
Environment ## An environment holds objects, runs simulations
    XYEnvironment
        VacuumEnvironment
        WumpusEnvironment
An agent program is a callable instance, taking percepts and choosing actions
    SimpleReflexAgentProgram
    ...
EnvGUI ## A window with a graphical representation of the Environment
EnvToolbar ## contains buttons for controlling EnvGUI
EnvCanvas ## Canvas to display the environment of an EnvGUI
"""

import numpy as np 
import collections
import copy 


class Thing:
    """This represents any physical object that can appear in an Environment.
    You subclass Thing to get the things you want. Each thing can have a
    .__name__  slot (used for output only)."""
    def __repr__(self):
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))

    def is_alive(self):
        """Things that are 'alive' should return true."""
        return hasattr(self, 'alive') and self.alive

    def show_state(self):
        """Display the agent's internal state. Subclasses should override."""
        print("I don't know how to show_state.")

    def display(self, canvas, x, y, width, height):
        """Display an image of this Thing on the canvas."""
        # Do we need this?
        pass


class Agent(Thing):
    """An Agent is a subclass of Thing with one required slot,
    .program, which should hold a function that takes one argument, the
    percept, and returns an action. (What counts as a percept or action
    will depend on the specific environment in which the agent exists.)
    Note that 'program' is a slot, not a method. If it were a method,
    then the program could 'cheat' and look at aspects of the agent.
    It's not supposed to do that: the program can only look at the
    percepts. An agent program that needs a model of the world (and of
    the agent itself) will have to build and maintain its own model.
    There is an optional slot, .performance, which is a number giving
    the performance measure of the agent in its environment."""

    def __init__(self, program=None):
        self.alive = True
        self.bump = False
        self.holding = []
        self.performance = 0
        if program is None or not isinstance(program, collections.Callable):
            print("Can't find a valid program for {}, falling back to default.".format(
                self.__class__.__name__))

            def program(percept):
                return eval(input('Percept={}; action? '.format(percept)))

        self.program = program

    def can_grab(self, thing):
        """Returns True if this agent can grab this thing.
        Override for appropriate subclasses of Agent and Thing."""
        return False

def TraceAgent(agent):
        """Wrap the agent's program to print its input and output. This will let
         you see what the agent is doing in the environment."""
        old_program = agent.program 

        def new_program(percept):
            action = old_program(percept)
            print('{} perceives {} and does {}'.format(agent, percept, action))
            return action 

        agent.program = new_program
        return agent 

        


