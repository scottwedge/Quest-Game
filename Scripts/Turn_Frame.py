# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:22:06 2019

@author: jordan loll

Turn Skeleton for Quest
"""
import random
import time

def character(one, two):
    titles = ["Mighty", "Powerful", "Clever", "Swift"]
    t1 = random.choice(titles)
    t2 = random.choice(titles)
    n1 = input("Player "+str(one)+" enter your name: ")
    name1 = ("The " + t1 +" " + str(n1) + "!")
    n2 = input("Player "+str(two)+" enter your name: ")
    name2 = ("The " + t2 + " " + str(n2) + "!")
    return(name1, name2)

def CoinToss(name):
    coin = ["heads", "tails"]
    call = input(str(name) + ", please call the toss: ")
    result = random.choice(coin)
    if call == result:
        return("won")
    else:
        return("lost")
    
class hero:
    def __init__(self, n = 'Unknown', h = 0, a = 0, lvl = 1):
        self.name = n
        self.hp = h
        self.armor = a
        self.level = lvl
    
    def getHeroStats(self):
        print("Name: {0} \nHealth: {1}\nArmor: {2} \nLevel: {3}".format(self.name, self.hp, self.armor, self.level))

def main():
    # Introduction
    print("\nWelcome to Quest")
    time.sleep(2)
    print("This is a simple two player game")
    
    # Name Characters
    n1, n2 = character(1, 2)
    print(n1, "and", n2, "have entered the Arena")
    
    pl_1 = hero(n1, 100,10,1)
    pl_2 = hero(n2, 100,10,1)
    
    
    # Choose who goes first
    p1, p2 = False, False
    
    result = CoinToss("Jordan") 
    if result == "won":
        p1 = True
    else:
        p2 = True
    
    print()
    print("Game Begin")
    time.sleep(2)
    
    
    # Taking Turns
    while p1 == True:
        print("Player 1's Turn")
        print(pl_1.name, "has", pl_1.hp, "health.")
        p1 = False
    
    while p2 == True:
        print("Player 2's Turn")
        print(pl_2.name, "has", pl_2.hp, "health.")
        p2 = False

main()
   
        
        
        
        