# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:14:13 2019

@author: jordan loll

Creating a cards library / deck
"""
import random
from PIL import Image, ImageDraw

#Local Path

local_path =r"C:\Users\jorda\Documents\PythonPrograms\Questar\Git_Stuff\Quest-Game"
#local_path = r"C:\Users\xTheC\Desktop\Quest\Quest-Game"
image_path = local_path+"\Images"

# Create the deck

# class for format of each card   # weapons/armor need a 'slot' on each character
class card:
    def __init__(self, n = "none", i = 'none', t = "none", st = "0", d = "none"):
        self.title = n
        self.image = i
        self.type = t
        self.stats = st
        self.desc = d

# Weapons, Armor, and any other cards types we need
# Perhaps make a class for each type of card instead of one generic form

#images
im_sw = Image.open(image_path+"\sword.png")
    
# Weapons
sword = card("Sword", im_sw, "1-Handed Weapon", 10, "Sharp Steel")
spear = card("Spear", "image", "2-Handed Weapon", 30, "Deadly at a Distance")

# Armor
shield = card("Kite Shield", "shield image", "1-Handed", 20, "Impenetrable")


#print(sword.title, sword.type)
#print(sword.stats, shield.desc, spear.image)
sword.image.show()

# Jordan is the best