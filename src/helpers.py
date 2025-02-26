from typing import Callable
from datetime import datetime as dt
import pandas as pd
import numpy as np
import itertools

PATH_TO_LOAD = 'src/Decks/to_load/'
PATH_LOADED = 'src/Decks/loaded/'

HALF_DECK_SIZE = 26

players = [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]
ALL_MATCHUPS = list(itertools.combinations(players, 2))

def debugger_factory(show_args = True) -> Callable:
    def debugger(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            if show_args:
                print(f'{func.__name__} was called with:')
                print('Positional arguments:\n', args)
                print('Keyword arguments:\n', kwargs)
            t0 = dt.now()
            results = func(*args, **kwargs)
            print(f'{func.__name__} ran for {dt.now() - t0}')
            return results
        return wrapper
    return debugger