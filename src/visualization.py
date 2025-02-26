from src.helpers import *
from src.datagen import *
from src.processing import *

import matplotlib.pyplot as plt
import seaborn as sns

def gen_heatmap():
    all_labels = [str([0,0,0]), str([0,0,1]), str([0,1,0]), str([0,1,1]), str([1,0,0]), str([1,0,1]), str([1,1,0]), str([1,1,1])]
    
    all_wins = pd.DataFrame([[None]*8]*8, index=all_labels, columns=all_labels)
    TRICK_WINS, TRICK_LOSSES, TRICK_TIES, CARDS_WINS, CARDS_LOSSES, CARDS_TIES = read_scores()
    for row in (all_labels):
        for col in (all_labels):
            if row in (TRICK_WINS.T).columns and col in TRICK_WINS.columns and not np.isnan(TRICK_WINS.loc[row,col]) and TRICK_WINS.loc[row,col]!=0:
                all_wins.loc[row,col] = (TRICK_WINS/(TRICK_WINS+TRICK_LOSSES+TRICK_TIES)).loc[row,col]
            if row in (TRICK_LOSSES.T).columns and col in TRICK_LOSSES.columns and not np.isnan(TRICK_LOSSES.loc[row,col]) and TRICK_LOSSES.loc[row,col]!=0:
                all_wins.loc[col, row] = (TRICK_LOSSES/(TRICK_WINS+TRICK_LOSSES+TRICK_TIES)).loc[row,col]
    
    plt.figure(figsize=(10, 9))
    mask = all_wins.isnull()
    all_wins = all_wins.fillna(-1)
    sns.heatmap(round(100*all_wins,1), annot=True, mask = mask, cmap='Reds', cbar_kws={'label': 'PLayer 1 Win Percentage'})
    plt.title('Penneys Game Win Percentage Heatmap')
    plt.yticks(rotation=0)
    plt.xlabel('Player 2')
    plt.ylabel('Player 1')
    plt.show
    plt.savefig('src/heatmap.png')
    return all_wins