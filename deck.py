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
for i in range(126):
    adv_deck.append(i)

#print(adv_deck)

st_deck = []
for i in range(29):
    st_deck.append(i)

numPlayer = 2

pl1_hand = []
draw = random.choice(adv_deck)
pl1_hand.append(draw)
adv_deck.pop(draw)
print(pl1_hand)
print(adv_deck)
#for i in range(numPlayer + 1):
