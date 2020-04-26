# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:26:34 2019

@author: Ben Loll
"""
import random 
import player_library
from rank_library import squire
from rank_library import knight
from rank_library import champion  
        
"""CODE RUNS FROM HERE DOWN"""
num_players = 3
game_over = 'false'
if num_players == 2:
        player_one = player_library.initialize_Player(1)
        player_two = player_library.initialize_Player(2)
elif num_players == 3:
        player_one = player_library.initialize_Player(1)
        player_two = player_library.initialize_Player(2)
        player_three = player_library.initialize_Player(3)
elif num_players == 4:
        player_one = player_library.initialize_Player(1)
        player_two = player_library.initialize_Player(2)
        player_three = player_library.initialize_Player(3)
        player_four = player_library.initialize_Player(4)

while game_over == 'false':
       shieldsWon = random.randint(1,5)
       player = random.randint(1,num_players)
       winner = ""
       if player == 1:
        player_library.levelUp(player_one,shieldsWon)
        game_over = player_one.victory
        winner = player_one.name
       elif player == 2: 
        player_library.levelUp(player_two,shieldsWon)
        game_over = player_two.victory
        winner = player_two.name
       elif player == 3:
        player_library.levelUp(player_three,shieldsWon)
        game_over = player_three.victory
        winner = player_three.name
       elif player == 4: 
        player_library.levelUp(player_four,shieldsWon)   
        game_over = player_four.victory
        winner = player_four.name
print(winner+' has become a knight of the round table and has won the game')