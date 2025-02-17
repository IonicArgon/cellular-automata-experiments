import numpy as np
from enum import Enum

class State(Enum):
    NOOP = 0
    SENSE = 1
    BROADCAST = 2
    

class Cell:
    def __init__(self, initial_state, initial_colour):