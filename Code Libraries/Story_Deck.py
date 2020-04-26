# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:46:41 2020

@author: jordan loll

Questar Document 2
    
This program is intended to be imported by other files

Story Deck
    13 Quests
    4 Tournaments
    11 Events
"""
Story_Deck = {}

#  Quests

class quest:
    def __init__(self, t = "none", y = "none", s = 2, f = "none"):
        self.title = t
        self.type = y
        self.stages = s
        self.foe = f

<<<<<<< Updated upstream
Story_Deck['quest1'] = quest("Search for the Holy Grail", "quest", s = 5, f = "all")
Story_Deck['quest2'] = quest("Test of the Green Knight", "quest", s = 4, f = "Green knight")
Story_Deck['quest3'] = quest("Search for the Questing Beast", "quest", s = 4)
Story_Deck['quest4'] = quest("Defend the Queen's Honor", "quest", s = 4, f = "all")
Story_Deck['quest5'] = quest("Rescue the Fair Maiden", "quest", s = 3, f = "Black knight")
Story_Deck['quest6'] = quest("Journey through the Enchanted Forest", "quest", s = 3, f = "Evil Knight")
Story_Deck['quest7'] = quest("Vanquish King Arthur's Enemies", "quest", s = 3)
Story_Deck['quest8'] = quest("Vanquish King Arthur's Enemies", "quest", s = 3)
Story_Deck['quest9'] = quest("Slay the Dragon", "quest", s = 3, f = "Dragon")
Story_Deck['quest10'] = quest("Boar Hunt", "quest", f = "Boar")
Story_Deck['quest11'] = quest("Boar Hunt", "quest", f = "Boar")
Story_Deck['quest12'] = quest("Repel the Saxon Raiders", "quest", f = ("Saxon Knight", "Saxons"))
Story_Deck['quest13'] = quest("Repel the Saxon Raiders", "quest", f = ("Saxon Knight", "Saxons"))
=======
Story_Deck['q1'] = quest("Search for the Holy Grail",            "quest", s = 5, f = "all")
Story_Deck['q2'] = quest("Test of the Green Knight",             "quest", s = 4, f = "Green knight")
Story_Deck['q3'] = quest("Search for the Questing Beast",        "quest", s = 4)
Story_Deck['q4'] = quest("Defend the Queen's Honor",             "quest", s = 4, f = "all")
Story_Deck['q5'] = quest("Rescue the Fair Maiden",               "quest", s = 3, f = "Black knight")
Story_Deck['q6'] = quest("Journey through the Enchanted Forest", "quest", s = 3, f = "Evil Knight")
Story_Deck['q7'] = quest("Vanquish King Arthur's Enemies",       "quest", s = 3)
Story_Deck['q8'] = quest("Vanquish King Arthur's Enemies",       "quest", s = 3)
Story_Deck['q9'] = quest("Slay the Dragon",                      "quest", s = 3, f = "Dragon")
Story_Deck['q10'] = quest("Boar Hunt",                           "quest", f = "Boar")
Story_Deck['q11'] = quest("Boar Hunt",                           "quest", f = "Boar")
Story_Deck['q12'] = quest("Repel the Saxon Raiders",             "quest", f = ("Saxon Knight", "Saxons"))
Story_Deck['q13'] = quest("Repel the Saxon Raiders",             "quest", f = ("Saxon Knight", "Saxons"))
>>>>>>> Stashed changes


# Tournament

class tournament:
    def __init__(self, t = "Tournament", y = "tournament", bs = 0):
        self.title = t
        self.type = y
        self.bonus_shields = bs

<<<<<<< Updated upstream
Story_Deck['tournament1'] = tournament(bs = 0)
Story_Deck['tournament2'] = tournament(bs = 1)
Story_Deck['tournament3'] = tournament(bs = 2)
Story_Deck['tournament4'] = tournament(bs = 3)
=======
Story_Deck['t1'] = tournament(bs = 0)
Story_Deck['t2'] = tournament(bs = 1)
Story_Deck['t3'] = tournament(bs = 2)
Story_Deck['t4'] = tournament(bs = 3)
>>>>>>> Stashed changes



# Events

class event:
    def __init__(self, t = 'none', y = 'none', e = 'none'):
        self.title = t
        self.type = y
        self.effect = e

<<<<<<< Updated upstream
Story_Deck['event1'] = event("King's Recognition", 'event', "Next player(s) to complete a quest will recieve 2 extra shield")
Story_Deck['event2'] = event("King's Recognition", 'event', "Next player(s) to complete a quest will recieve 2 extra shield")
Story_Deck['event3'] = event("Queen's Favor", 'event', "The lowest ranked player(s) immediately recieve two adventure cards")
Story_Deck['event4'] = event("Queen's Favor", 'event', "The lowest ranked player(s) immediately recieve two adventure cards")
Story_Deck['event5'] = event("Court Called to Camelot", 'event', "All allies must be discarded")
Story_Deck['event6'] = event("Court Called to Camelot", 'event', "All allies must be discarded")
Story_Deck['event7'] = event("Pox", 'event', "ALl players except the one drawing this card lose 1 shield")
Story_Deck['event8'] = event("Plague", 'event', "Drawer loses 2 shields if possible")
Story_Deck['event9'] = event("Chivalrous Deed", 'event', "Player(s) with both the lowest rank and least amount of shileds, recieves 3 shields")
Story_Deck['event10'] = event("Prosperity Throught the Realm", 'event', "All players may immediately draw 2 Adventure Cards")
Story_Deck['event11'] = event("King's Call to Arms", 'event', "The highest ranked player(s) must place 1 weapon in the discard pile. If unable to do so, 2 Foe Cards must be discarded")
=======
Story_Deck['e1'] = event("King's Recognition",             'event', "Next player(s) to complete a quest will recieve 2 extra shield")
Story_Deck['e2'] = event("King's Recognition",             'event', "Next player(s) to complete a quest will recieve 2 extra shield")
Story_Deck['e3'] = event("Queen's Favor",                  'event', "The lowest ranked player(s) immediately recieve two adventure cards")
Story_Deck['e4'] = event("Queen's Favor",                  'event', "The lowest ranked player(s) immediately recieve two adventure cards")
Story_Deck['e5'] = event("Court Called to Camelot",        'event', "All allies must be discarded")
Story_Deck['e6'] = event("Court Called to Camelot",        'event', "All allies must be discarded")
Story_Deck['e7'] = event("Pox",                            'event', "All players except the one drawing this card lose 1 shield")
Story_Deck['e8'] = event("Plague",                         'event', "Drawer loses 2 shields if possible")
Story_Deck['e9'] = event("Chivalrous Deed",                'event', "Player(s) with both the lowest rank and least amount of shileds, recieves 3 shields")
Story_Deck['e10'] = event("Prosperity Throught the Realm", 'event', "All players may immediately draw 2 Adventure Cards")
Story_Deck['e11'] = event("King's Call to Arms",           'event', "The highest ranked player(s) must place 1 weapon in the discard pile. If unable to do so, 2 Foe Cards must be discarded")


"""
for i in Story_Deck:
    print(i, Story_Deck[i].title)
"""
>>>>>>> Stashed changes
