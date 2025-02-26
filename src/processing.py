from src.helpers import *
from src.datagen import *

import numpy as np
import pandas as pd
from tqdm import tqdm
import os

def scoreGame(p1, p2, deck:np.array, half_deck_size: int = HALF_DECK_SIZE):
    '''
    Function to score game between two players. Outputs total tricks and cards for both players.
    '''
    
    end = 2 # index of most recent card
    p1_tricks = 0
    p2_tricks = 0
    p1_cards = 0
    p2_cards = 0
    last_trick_index = -1 #index of end previous trick # begins at -1 because deck is 0-51
    for end in range (2,2*HALF_DECK_SIZE):
        # Skips if last trick was taken in previous 2 cards
        if end < last_trick_index+3:
            continue
        
        # Checks if p1 takes the trick
        elif deck[end-2] == p1[0] and deck[end-1] == p1[1] and deck[end] == p1[2]:
            # print(f'p1 trick at {end}')

            #Update total tricks and cards
            p1_tricks+=1
            p1_cards = p1_cards + end - last_trick_index
            # print(p1_cards)
            
            # Update last_trick_index
            last_trick_index = end

        elif deck[end-2] == p2[0] and deck[end-1] == p2[1] and deck[end] == p2[2]:

            #Update total tricks and cards
            p2_tricks+=1
            p2_cards += end-last_trick_index
            # print(p2_cards)
            
            # Update last_trick_index
            last_trick_index = end
            
    return p1_tricks, p1_cards, p2_tricks, p2_cards

def run_all_games(deck, all_matchups = ALL_MATCHUPS):
    TRICK_WINS, TRICK_LOSSES, TRICK_TIES, CARDS_WINS, CARDS_LOSSES, CARDS_TIES = read_scores()
    '''
    Function runs all possible matchups on given deck, updates WINS, LOSSES, and TIES
    '''
    for matchup in all_matchups:
        p1_tricks, p1_cards, p2_tricks, p2_cards = scoreGame(matchup[0], matchup[1], deck)
        
        if p1_tricks > p2_tricks:
            TRICK_WINS.loc[str(matchup[0]), str(matchup[1])] += 1
        elif p1_tricks < p2_tricks:
            TRICK_LOSSES.loc[str(matchup[0]), str(matchup[1])] += 1
        elif p1_tricks == p2_tricks:
            TRICK_TIES.loc[str(matchup[0]), str(matchup[1])] += 1

        if p1_cards > p2_cards:
           CARDS_WINS.loc[str(matchup[0]), str(matchup[1])] += 1
        elif p1_cards < p2_cards:
           CARDS_LOSSES.loc[str(matchup[0]), str(matchup[1])] += 1
        elif p1_cards == p2_cards:
           CARDS_TIES.loc[str(matchup[0]), str(matchup[1])] += 1
    return TRICK_WINS, TRICK_LOSSES, TRICK_TIES, CARDS_WINS, CARDS_LOSSES, CARDS_TIES

def play_all_decks(path):
    if path == None:
        return
    decks = read_decks(path)
    TRICK_WINS, TRICK_LOSSES, TRICK_TIES, CARDS_WINS, CARDS_LOSSES, CARDS_TIES = read_scores()
    for deck in tqdm(decks):
            new_TW, new_TL, new_TT, new_CW, new_CL, new_CT = run_all_games(deck, all_matchups = ALL_MATCHUPS)

            TRICK_WINS += new_TW
            TRICK_LOSSES += new_TL
            TRICK_TIES += new_TT

            CARDS_WINS += new_CW
            CARDS_LOSSES += new_CL
            CARDS_TIES += new_CT
    save_scores(TRICK_WINS, TRICK_LOSSES, TRICK_TIES, CARDS_WINS, CARDS_LOSSES, CARDS_TIES)
    os.rename(path, path.replace(PATH_TO_LOAD, PATH_LOADED))
    return

    