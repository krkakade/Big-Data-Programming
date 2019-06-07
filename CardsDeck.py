#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:56:37 2019

@author: komal
"""

#create cards for the game 
class Card:
    def __init__(self, name, Strength, Loyalty, Evilness, Intelligence, Power):
        self.name = name
        self.Strength = Strength
        self.Loyalty = Loyalty
        self.Evilness = Evilness
        self.Intelligence = Intelligence
        self.Power = Power
     
cards = []

cards.append(Card(name="Arya Stark",
                  Strength=80,
                  Loyalty=99,
                  Evilness=60,
                  Intelligence=95,
                  Power=75)) 

cards.append(Card(name="Jon Snow",
                  Strength=95,
                  Loyalty=100,
                  Evilness=50,
                  Intelligence=90,
                  Power=80))

cards.append(Card(name="Daenerys Targaryen",
                  Strength=70,
                  Loyalty=90,
                  Evilness=80,
                  Intelligence=96,
                  Power=99))

cards.append(Card(name="Cersei Lannister",
                  Strength=75,
                  Loyalty=50,
                  Evilness=95,
                  Intelligence=94,
                  Power=90))

cards.append(Card(name="Bran Stark",
                  Strength=20,
                  Loyalty=98,
                  Evilness=30,
                  Intelligence=97,
                  Power=78))

cards.append(Card(name="Sansa Stark",
                  Strength=65,
                  Loyalty=89,
                  Evilness=78,
                  Intelligence=91,
                  Power=79))

cards.append(Card(name="Ramsay Bolton",
                  Strength=90,
                  Loyalty=10,
                  Evilness=100,
                  Intelligence=88,
                  Power=73))

cards.append(Card(name="Tyrion Lannister",
                  Strength=75,
                  Loyalty=86,
                  Evilness=55,
                  Intelligence=98,
                  Power=77))

cards.append(Card(name="Melisandre",
                  Strength=35,
                  Loyalty=50,
                  Evilness=91,
                  Intelligence=86,
                  Power=88))

cards.append(Card(name="Joffrey Baratheon",
                  Strength=55,
                  Loyalty=20,
                  Evilness=99,
                  Intelligence=66,
                  Power=89))

cards.append(Card(name="Brienne of Tarth",
                  Strength=94,
                  Loyalty=100,
                  Evilness=89,
                  Intelligence=71,
                  Power=68))

cards.append(Card(name="Lord Varys",
                  Strength=60,
                  Loyalty=70,
                  Evilness=53,
                  Intelligence=97,
                  Power=70))

cards.append(Card(name="Jamie Lannister",
                  Strength=83,
                  Loyalty=50,
                  Evilness=94,
                  Intelligence=68,
                  Power=65))

cards.append(Card(name="Sandor Clegane",
                  Strength=93,
                  Loyalty=80,
                  Evilness=73,
                  Intelligence=69,
                  Power=62))

cards.append(Card(name="Petyr Baelish",
                  Strength=82,
                  Loyalty=10,
                  Evilness=91,
                  Intelligence=92,
                  Power=71))

cards.append(Card(name="Margaery Tyrell",
                  Strength=50,
                  Loyalty=60,
                  Evilness=52,
                  Intelligence=93,
                  Power=87))

