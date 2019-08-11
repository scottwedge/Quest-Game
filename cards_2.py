# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 13:21:59 2019

@author: jordan loll

Card classes
"""
from PIL import Image

path = r"C:\Users\jorda\Documents\PythonPrograms\Questar"

class ranks:
    def __init__(self, t = "none", i = 'none', s = "0"):
        self.title = t
        self.image = i
        self.stats = s

class foe:
    def __init__(self, t = "none", i = 'none', s = "0", d = "none"):
        self.title = t
        self.image = i
        self.stats = s
        self.desc = d

class ally:
    def __init__(self, t = "none", i = 'none', s = "0", d = "none"):
        self.title = t
        self.image = i
        self.stats = s
        self.desc = d

class equipment:
    def __init__(self, t = "none", i = 'none', p = "none", s = "0", l = "unknown"):
        self.title = t
        self.image = i
        self.type = p
        self.stats = s
        self.slot = l

#class quest:
#    stages
#    reward

print("Hello")
# Ranked Classes
sq = ranks("Squire", 'image', 5)
kn = ranks("Knight", 'image', 10)
ch = ranks("Champion", 'image', 20)


# Enemies

# Green Knight
im_gk = Image.open(path+r"\gk.jpg")
g_knight = foe("Green Knight", im_gk, 40, "Bertilak de Hautdesert is transformed into the Green Knight by Morgan le Fay, \na traditional adversary of King Arthur, in order to test his court.")
print(g_knight.stats)
#g_knight.image.show()

# Dragon
im_drg = Image.open(path+r"\dragon.jpg")
dragon = foe("Dragon", im_drg, 70, "Beware")
#dragon.image.show()


# Allies
im_sl = Image.open(path+r"\lance.jpg")
sr_lance = ally("Sir Lancelot", im_sl, 20, "He lances, alot.")
#sr_lance.image.show()


# Equipment
im_sw = Image.open(path+r"\sword.png")
sword = equipment("Sword", im_sw, "weapon", 10, "1 hand")

im_helm = Image.open(path+r"\helmet.jpg")
helmet = equipment("Helment", im_helm, "armor", 5, "head")

im_hor = Image.open(path+r"\horse.jpg")
horse = equipment("Horse", im_hor, "weapon", 10, "stead")