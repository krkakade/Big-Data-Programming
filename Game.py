#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:20:13 2019

@author: komal
"""

import random
from time import sleep
from CardsDeck import cards


#Game Intro and begining
print("******GOT TRUMP CARDS GAME******")
print("Total number of cards are :",len(cards))
print("---This Game can be played by only 2 players!---")
print("--- Value of each characterstic lies between the range 1 to 100 ---")
print("Lets begin the game...")
begin_game = input("Shall we begin the Game? ")

while begin_game != "yes":
    print("Please input yes to proceed")
    begin_game = input("Shall we begin the Game? (yes/no)")
    
random.shuffle(cards)
playerDeck = []
computerDeck = []
outdatedDeck = []

# Deal the cards
while len(cards) > 0:
    playerDeck.append(cards.pop(0))
    computerDeck.append(cards.pop(0))
    

playerTurn = True
godspellcountp = 0
godspellcountc = 0
rspellcountc = 0
rspellcountp = 0
p1points=0
p2points=0
ra=0
rb=0

while len(playerDeck) > 0 and len(computerDeck) > 0:
    sleep(1)

    if playerTurn == True:
        
        playerCard = playerDeck.pop(0)
        outdatedDeck.append(playerCard)
        print("PLAYER1 CARD")
        print("Name:", playerCard.name)
        print("1. Strength:", playerCard.Strength)
        print("2. Loyalty:", playerCard.Loyalty)
        print("3. Evilness:", playerCard.Evilness)
        print("4. Intelligence:", playerCard.Intelligence)
        print("5. Power:", playerCard.Power)
        
        answer = int(input("Player1, choose the characterstic you want to challenge with!! "))
       
        while answer not in range(1,6):
            answer = int(input("Not a valid answer, please try again: "))
        
       
        #player1 god spell
        if (godspellcountp == 0  and len(computerDeck) > 1 and ra == 0):
            godspell = input("Player1, do you want to use GOD SPELL? (yes/no) : ")
            if (godspell == "yes" and godspellcountp == 0):
                godspellcountp = 1
                p2cards = len(computerDeck)
                print("No of cards in Player2 deck:", p2cards)
                cardno = input("Which card number from Player2 deck? ")
                if (rspellcountc == 0 and len(outdatedDeck) > 1):
                    rspell1 = input("Player2, do you want to use RESURRECT SPELL? (yes/no) :")
                    if (rspell1 == "yes" and rspellcountc == 0):
                        z2 = random.randint(1,len(outdatedDeck))
                        mn = outdatedDeck.pop(int(z2)-1)
                        computerDeck.insert(0,mn)
                        choice = input("Player1: a. Force new card \n b. Force earlier card ")
                        if (choice == "a"):
                            computerCard = computerDeck.pop(0)
                            outdatedDeck.append(computerCard)
                            rspellcountc = 1
                        else:    
                            computerCard = computerDeck.pop(int(cardno)-1)
                            outdatedDeck.append(computerCard)
                            rspellcountc = 1
                    else:
                        computerCard = computerDeck.pop(int(cardno)-1)
                        outdatedDeck.append(computerCard)
                else:
                    computerCard = computerDeck.pop(int(cardno)-1)
                    outdatedDeck.append(computerCard)                     
            else:
                computerCard = computerDeck.pop(0)
                outdatedDeck.append(computerCard)         
        else:
            computerCard = computerDeck.pop(0)
            outdatedDeck.append(computerCard) 

        if (rspellcountp == 0 and len(outdatedDeck) > 1 and ra == 0):
            rspell = input("Player1, do you want to use RESURRECT SPELL? (yes/no) ")
            if (rspell == "yes" and rspellcountp == 0):
                z1 = random.randint(1,len(outdatedDeck))
                playerCard = outdatedDeck.pop(int(z1)-1)
                outdatedDeck.append(playerCard)
                rspellcountp = 1
                ra = 1
            else:
                playerCard = playerDeck.pop(0)
                outdatedDeck.append(playerCard)
        else:
            playerCard = playerDeck.pop(0)
            outdatedDeck.append(playerCard)
            
            
        print("PLAYER2 CARD")
        print("Name:", computerCard.name)
        print("1. Strength:", computerCard.Strength)
        print("2. Loyalty:", computerCard.Loyalty)
        print("3. Evilness:", computerCard.Evilness)
        print("4. Intelligence:", computerCard.Intelligence)
        print("5. Power:", computerCard.Power)    
        
    else:
        
        print("PLAYER2 CARD")
        print("Name:", computerCard.name)
        print("1. Strength:", computerCard.Strength)
        print("2. Loyalty:", computerCard.Loyalty)
        print("3. Evilness:", computerCard.Evilness)
        print("4. Intelligence:", computerCard.Intelligence)
        print("5. Power:", computerCard.Power)
        
        answer = int(input("choose the characterstic you want to challenge with!! "))
        print("Player2 chooses", answer)
        
        #Player2 god spell
        if (godspellcountc == 0 and len(playerDeck) > 1 and rb == 0):
            gspell1 = input("Player2, do you want to play God Spell? yes or no: ")
            if (gspell1 == "yes" and godspellcountc == 0):
                godspellcountc = 1
                p2cards = len(playerDeck)
                print("No of cards in Player1 deck:", p2cards)
                cardno1 = input("Which card number from Player1 deck? ")
                if (rspellcountp == 0 and len(outdatedDeck) > 1):
                    rspell = input("Player1, do you want to play Resurrect Spell? yes or no: ")
                    if (rspell == "yes" and rspellcountp == 0):
                        z1 = random.randint(1,len(outdatedDeck))
                        nm = outdatedDeck.pop(int(z1)-1)
                        playerDeck.insert(0,nm)
                        choice1 = input("Player2: a. Force resurrected card or b. Force earlier choice ")
                        if (choice1 == "a"):
                            playerCard = playerDeck.pop(0)
                            outdatedDeck.append(playerCard)
                            rspellcountp = 1
                        else:
                            playerCard = playerDeck.pop(int(cardno1)-1)
                            outdatedDeck.append(playerCard)
                            rspellcountp = 1
                    else:
                        playerCard = playerDeck.pop(int(cardno1)-1)
                        outdatedDeck.append(playerCard)
                else:                 
                    playerCard = playerDeck.pop(int(cardno1)-1)
                    outdatedDeck.append(playerCard)
            else:
                playerCard = playerDeck.pop(0)
                outdatedDeck.append(playerCard)

        
        else:
            playerCard = playerDeck.pop(0)
            outdatedDeck.append(playerCard)
                                   
        #player2 resurrect spell
        if (rspellcountc == 0 and len(outdatedDeck) > 1 and rb == 0):
            rspell1 = input("Player2, do you want to play Resurrect Spell? yes or no: ")
            if (rspell1 == "yes" and rspellcountc == 0):
                z2 = random.randint(1,len(outdatedDeck))
                computerCard = outdatedDeck.pop(int(z2)-1)
                outdatedDeck.append(computerCard)
                rspellcountc = 1
                rb = 1
            else:
                computerCard = computerDeck.pop(0)
                outdatedDeck.append(computerCard)

        else:
            computerCard = computerDeck.pop(0)
            outdatedDeck.append(computerCard)
        
        
        print("PLAYER1 CARD")
        print("Name:", playerCard.name)
        print("1. Strength:", playerCard.Strength)
        print("2. Loyalty:", playerCard.Loyalty)
        print("3. Evilness:", playerCard.Evilness)
        print("4. Intelligence:", playerCard.Intelligence)
        print("5. Power:", playerCard.Power)
        
    playerWins = False
    #comparing cards of player1 and player2
    if answer == 1:
        playerWins = (playerCard.Strength < computerCard.Strength)
    elif answer == 2:
        playerWins = (playerCard.Loyalty > computerCard.Loyalty)
    elif answer == 3:
        playerWins = (playerCard.Evilness > computerCard.Evilness)
    elif answer == 4:
        playerWins = (playerCard.Intelligence > computerCard.Intelligence)
    elif answer == 5:
        playerWins = (playerCard.Power > computerCard.Power)

    sleep(1)
    
    #who wins the point?
    if playerWins:
        print("***Player1 gets 1 point!!***\n\n")
        p1points=p1points+1      
        playerTurn = True
    else:
        print("***Player2 gets 1 point!!***\n\n")
        p2points=p2points+1
        playerTurn = False

sleep(2)

#who wins the game?
if p1points<p2points:
    print("PLAYER2 is the Winner!")
elif p1points>p2points:
    print("PLAYER1 is the Winner!")
else:
    print("OOops.... It's a tie!")
 

sleep(2)

#print points of player1 and player2 
print("Player1 points: ", p1points)
print("Player2 points: ", p2points)
print("Number of cards in Outdated Deck: ", len(outdatedDeck))
