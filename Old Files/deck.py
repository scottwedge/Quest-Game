# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:03:33 2019

@author: jordan loll

card handling
"""
# adventure deck = 125
# 49 weapons, 50 foes, 8 tests, 10 allies

# story deck = 28
# 13 quests, 4 tournaments, 11 events

# rank deck = 12
# 4 of each lvl
# Don't think we need this

# hand start = 12 adv cards 
#(never hold more than 12), play or discard

import random

adv_deck = []
for i in range(125):
    adv_deck.append(i)

st_deck = []
for i in range(28):
    st_deck.append(i)

#print(adv_deck)
#Map Adventure Deck index# to card name (card ID# later)
for i,_ in enumerate(adv_deck):
        #Equip
        if adv_deck[i] < 2:
           adv_deck[i] = "Excalibur"
        elif adv_deck[i] < 8:
           adv_deck[i] = "Lance"   
        elif adv_deck[i] < 16:
           adv_deck[i] = "Battle-Ax" 
        elif adv_deck[i] < 32:
           adv_deck[i] = "Sword"
        elif adv_deck[i] < 43:
           adv_deck[i] = "Horse"
        elif adv_deck[i] < 49:
           adv_deck[i] = "Dagger"
        #Foes
        elif adv_deck[i] < 50:
           adv_deck[i] = "Dragon"
        elif adv_deck[i] < 52:
           adv_deck[i] = "Giant"
        elif adv_deck[i] < 56:
           adv_deck[i] = "Mordred"
        elif adv_deck[i] < 58:
           adv_deck[i] = "Green Knight" 
        elif adv_deck[i] < 61:
           adv_deck[i] = "Black Knight"
        elif adv_deck[i] < 67:
           adv_deck[i] = "Evil Knight" 
        elif adv_deck[i] < 75:
           adv_deck[i] = "Saxon Knight"   
        elif adv_deck[i] < 82:
           adv_deck[i] = "Robber Knight"  
        elif adv_deck[i] < 87:
           adv_deck[i] = "Saxons" 
        elif adv_deck[i] < 91:
           adv_deck[i] = "Boars"
        elif adv_deck[i] < 99:
           adv_deck[i] = "Thieves"
        #Tests
        elif adv_deck[i] < 101:
           adv_deck[i] = "Test of Valor"
        elif adv_deck[i] < 103:
           adv_deck[i] = "Test of Tempation" 
        elif adv_deck[i] < 105:
           adv_deck[i] = "Test of Morgan Le Fey" 
        elif adv_deck[i] < 107:
           adv_deck[i] = "Test of the Questing Beast"  
        #Allies
        elif adv_deck[i] == 107:
           adv_deck[i] = "Sir Galahad"
        elif adv_deck[i] == 108:
           adv_deck[i] = "Sir Lancelot"
        elif adv_deck[i] == 109:
           adv_deck[i] = "Sir Lancelot"
        elif adv_deck[i] == 110:
           adv_deck[i] = "King Arthur"
        elif adv_deck[i] == 110:
           adv_deck[i] = "Sir Tristan"
        elif adv_deck[i] == 111:
           adv_deck[i] = "Sir Pelinore"
        elif adv_deck[i] == 112:
           adv_deck[i] = "Sir Gawain"
        elif adv_deck[i] == 113:
           adv_deck[i] = "Sir Percival" 
        elif adv_deck[i] == 114:
           adv_deck[i] = "Queen Guinevere"
        elif adv_deck[i] == 115:
           adv_deck[i] = "Queen Iseult"
        elif adv_deck[i] == 116:
           adv_deck[i] = "Merlin"
        #Armor
        elif adv_deck[i] > 116:
           adv_deck[i] = "Armor"   
print(adv_deck)        
#================================================================
#print(st_deck)
#Map Story Deck index# to card name (card ID# later)
for i,_ in enumerate(st_deck):
        #Equip
        if st_deck[i] == 0:
           st_deck[i] = "Search for the Holy Grail"
        elif st_deck[i] == 1:
           st_deck[i] = "Test of the Green Knight"   
        elif st_deck[i] == 2:
           st_deck[i] = "Search for the Questing Beast" 
        elif st_deck[i] == 3:
           st_deck[i] = "Defend the Queen's Honor"
        elif st_deck[i] == 4:
           st_deck[i] = "Rescue the Fair Maiden"
        elif st_deck[i] == 5:
           st_deck[i] = "Journey Through the Enchanted Forest"
        elif st_deck[i] < 8:
           st_deck[i] = "Vanquish King Arthur's Enemies"
        elif st_deck[i] == 8:
           st_deck[i] = "Slay the Dragon"
        elif st_deck[i] < 11:
           st_deck[i] = "Boar Hunt"
        elif st_deck[i] < 13:
           st_deck[i] = "Repel the Saxon Raiders"
        #Tournaments   
        elif st_deck[i] == 13:
           st_deck[i] = "Tournament at Camelot"
        elif st_deck[i] == 14:
           st_deck[i] = "Tournament at Orkney"
        elif st_deck[i] == 15:
           st_deck[i] = "Tournament at Tintagel" 
        elif st_deck[i] == 16:
           st_deck[i] = "Tournament at York"
        #Events
        elif st_deck[i] < 19:
           st_deck[i] = "King's Recognition"
        elif st_deck[i] < 21:
           st_deck[i] = "Queen's Favor"
        elif st_deck[i] < 23:
           st_deck[i] = "Court Called to Camelot"
        elif st_deck[i] == 23:
           st_deck[i] = "Pox" 
        elif st_deck[i] == 24:
           st_deck[i] = "Plague"
        elif st_deck[i] == 25:
           st_deck[i] = "Chivalrous Deed"
        elif st_deck[i] == 26:
           st_deck[i] = "Prosperity throughout the Realm" 
        elif st_deck[i] == 27:
           st_deck[i] = "King's Call to Arms"    
print(st_deck)  
#================================================================
numPlayer = 2
pl1_hand = []
pl2_hand = []
i = 0
while  i<11:
       #Somehow the deck empties here lol 
       draw = random.choice(adv_deck)
       pl1_hand.append(draw)
       adv_deck.remove(draw)
       draw = random.choice(adv_deck)
       pl2_hand.append(draw)
       adv_deck.remove(draw)
print(pl1_hand)    
print(pl2_hand)   

   