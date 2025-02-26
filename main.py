from src.helpers import *
from src.datagen import *
from src.processing import *
from src.visualization import *

print('What do you want to do? Enter:\n(1) To gererate and play new decks\n(2) To play all unloaded decks\n(3) To play specific unloaded deck\n(4) Show Heatmap')
start = int(input())
if start == 1:
    print('Provide Seed')
    seed = int(input())
    print('Provide number of decks')
    num_decks = int(input())
    path = save_decks(seed, num_decks)
    play_all_decks(path)
elif start == 2:
    for path in os.listdir('src/Decks/to_load'):
        play_all_decks(str('src/Decks/to_load/' +path))
elif start == 3:
    print('Which deck?\n')
    print(os.listdir('src/Decks/to_load/'))
    path = str(input())
    play_all_decks(str('src/Decks/to_load/' + path))
elif start == 4:
    print(gen_heatmap())
else:
    print('Invalid Input')
print('End')
    
    #### Fixes to Add
## Save scores for every seed
## Get everything out of pandas and to numpy
## switch csv -> npy
## Just make a class?
## Do I need 3 7x7 arrays or can I use 1 8x8?
## Automatically get new seed instead of input
## Fix visualization