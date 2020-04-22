# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:10:48 2019

@author: jordan loll

Practice setting up a turn based simulation
"""
class menu:
    def __init__(self):
        self.
        
        print("Welcome to Questar!")
        print("Choose from the following options.")
        print("\nStart New game\nRules\nOptions\n")
        choice = input(" ")
        choice = choice.title()
        if choice == "Start New game":
            print('Game on')
        elif choice == "Rules":
            print("Dems da rules")
        elif choice == "Options":
            print("OPT")
        else:
            print("Invalid choice")

class hero:
    def __init__(self, n = 'Unknown', h = 0, a = 0, lvl = 1):
        self.name = n
        self.hp = h
        self.armor = a
        self.level = lvl
    
    def getHeroStats(self):
        print("Name: {0} \nHealth: {1}\nArmor: {2} \nLevel: {3}".format(self.name, self.hp, self.armor, self.level))

    def Hero_Setup(n1, n2):
        p1 = hero(n1, 10, 5)
        p1.getHeroStats()
        print()
        p2 = hero(n2, 20, 1)
        p2.getHeroStats()

class turn:
    def startAuto(self):
        print("You drew a card")
        print("It is your turn, what would you like to do?")
    
    def options(self):
         move = input("Quest, Tourny, or Level Up?")
         if move == "Quest":
             print("Let the quest begin")
         else:
             print(move)
        



Play = True

while Play == True:
    try:
        hero.Hero_Setup("Fred", "Greg")
        print()
        t = turn()
        t.startAuto()
        t.options()
        
        
        Play = False
    except:
        print("Didn't work")
        Play = False
    