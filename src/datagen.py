import numpy as np
from src.helpers import *

import numpy as np
import pandas as pd
import os
import itertools

def get_decks(n_decks: int,
              seed: int, 
              half_deck_size: int = HALF_DECK_SIZE 
              ) -> tuple[np.ndarray, np.ndarray]:
    """
    Efficiently generate `n_decks` shuffled decks using NumPy.
    
    Returns:
        decks (np.ndarray): 2D array of shape (n_decks, num_cards), 
        each row is a shuffled deck.
    """
    init_deck = [0]*half_deck_size + [1]*half_deck_size
    decks = np.tile(init_deck, (n_decks, 1))
    rng = np.random.default_rng(seed)
    rng.permuted(decks, axis=1, out=decks)
    return decks

def save_decks(seed:int,
               n_decks:int = 100_000, 
               half_deck_size: int = HALF_DECK_SIZE
              ) -> str:
    path = PATH_TO_LOAD + f"seed_{seed}.npy"
    loaded_path = PATH_LOADED + f"seed_{seed}.npy"
    if os.path.exists(path) or os.path.exists(loaded_path):
        print('Seed already used')
        return None
    decks = get_decks(n_decks, seed, half_deck_size)
    np.save(path, decks)
    return path

def read_decks(path):
    return np.load(path)

def save_scores(TRICK_WINS, TRICK_LOSSES, TRICK_TIES, CARDS_WINS, CARDS_LOSSES, CARDS_TIES):
    TRICK_WINS.to_csv('src/Scores/TRICK_WINS.csv')
    TRICK_LOSSES.to_csv('src/Scores/TRICK_LOSSES.csv')
    TRICK_TIES.to_csv('src/Scores/TRICK_TIES.csv')
    CARDS_WINS.to_csv('src/Scores/CARDS_WINS.csv')
    CARDS_LOSSES.to_csv('src/Scores/CARDS_LOSSES.csv')
    CARDS_TIES.to_csv('src/Scores/CARDS_TIES.csv')
    return

def read_scores():
    if len(os.listdir('src/Scores/'))<6:
        all_labels = [str([0,0,0]), str([0,0,1]), str([0,1,0]), str([0,1,1]), str([1,0,0]), str([1,0,1]), str([1,1,0]), str([1,1,1])]
        row_labels = all_labels[:7]
        column_labels = all_labels[1:]
        empty_data = [[0]*7]*7

        TRICK_WINS = pd.DataFrame(empty_data, index=row_labels, columns=column_labels)
        TRICK_LOSSES = pd.DataFrame(empty_data, index=row_labels, columns=column_labels)
        TRICK_TIES = pd.DataFrame(empty_data, index=row_labels, columns=column_labels)
        CARDS_WINS = pd.DataFrame(empty_data, index=row_labels, columns=column_labels)
        CARDS_LOSSES = pd.DataFrame(empty_data, index=row_labels, columns=column_labels)
        CARDS_TIES = pd.DataFrame(empty_data, index=row_labels, columns=column_labels)
    
    TRICK_WINS = pd.read_csv('src/Scores/TRICK_WINS.csv', index_col=0)
    TRICK_LOSSES = pd.read_csv('src/Scores/TRICK_LOSSES.csv', index_col=0)
    TRICK_TIES = pd.read_csv('src/Scores/TRICK_TIES.csv', index_col=0)
    CARDS_WINS = pd.read_csv('src/Scores/CARDS_WINS.csv', index_col=0)
    CARDS_LOSSES = pd.read_csv('src/Scores/CARDS_LOSSES.csv', index_col=0)
    CARDS_TIES = pd.read_csv('src/Scores/CARDS_LOSSES.csv', index_col=0)
    return TRICK_WINS, TRICK_LOSSES, TRICK_TIES, CARDS_WINS, CARDS_LOSSES, CARDS_TIES