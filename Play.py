import numpy as np
from Game import Game
import random

#AI makes its move based on possible moves and game state
#makes a list of all moves, shortens it to available moves
#if there are no moves left, draw
#checks for no special conditions, choose random move
#Otherwise handle condition
#print new game state after move
def AIplay(G):
  possible = [0,1,2,3,4,5,6,7,8]
  choice = 0
  UpdatePossibleMoves(G,possible)
  if len(possible) == 0:
    print("Draw")
    G.printGame()
    return False
  XWins,OWins,XBlock = updateFlags(G)
  if (XWins == 0) and (OWins == 0) and (XBlock == 0):
    choice = random.choice(possible)
  elif XWins != 0:
    print("You Win!")
    G.printGame()
    return False
  elif OWins != 0:
    choice = AIchoice(G,possible,OWins)
    print("You Lose!")
    G.spaces[choice].markO()
    G.printGame()
    return False
  elif XBlock != 0:
    choice = AIchoice(G,possible,XBlock)
  else:
    print("Error")
    G.printGame()
    return False
  G.spaces[choice].markO()
  G.printGame()

#iterates through possible list and checks the blocks of associated spaces
def AIchoice(G,p,flag):
  for i in range(len(p)):
    if flag in G.spaces[p[i]].blocks:
      return p[i]

#Shortens the list to moves not yet taken
def UpdatePossibleMoves(G,p):
  for i in range (8,-1,-1):
    if G.spaces[i].value != 0:
      p.pop(i)

#secial conditions for output
def updateFlags(G):
  XWins = check(G,3)
  OWins = check(G,8)
  XBlock = check(G,2)
  return XWins, OWins, XBlock

#this returns the row/column/diagonal of interest or 0 if no forced moves
#I really wanted to do loops instead of 8 "if" statements
#check the rows (j is first 0 so adds 0, then 3, then 6)
#+1 on return because 0 code confuses it with default
#same principle but reverse i and j for columns
#diagonals have unique cases
def check(G,val):
  for j in range(3):
    total = 0
    for i in range(3):
      total += (G.spaces[i+(j*3)].value)
    if total == val:
      return j+1
  for j in range(3):
    total = 0
    for i in range(3):
      total += (G.spaces[j+(i*3)].value)
    if total == val:
      return j+4
  if G.spaces[0].value + G.spaces[4].value + G.spaces[8].value == val:
    return 7
  if G.spaces[2].value + G.spaces[4].value + G.spaces[6].value == val:
    return 8
  return 0

#creates, then shortens list of possible moves
#attempts to turn input into integer
#quit functionality
#checks if input is within the list of possible moves
#if not good input, re-prompts
#if good input, marks X in space (input)
def playerInput(G):
  possible = [0,1,2,3,4,5,6,7,8]
  UpdatePossibleMoves(G,possible)
  userIn = input()
  try:
    userIn = int(userIn)
  except:
    if userIn == "quit":
      return False
    print("Please choose a number")
    playerInput(G)
    return
  if userIn in possible:
    G.spaces[userIn].markX()
  else:
    print("Not in range, choose from")
    print(possible)
    playerInput(G)
    return
  
#initiates game and prints it. Then enters game loop
#broken either by game end or user quit
GAME = Game()
GAME.printGame() 
while True:
  if playerInput(GAME) == False:
    break
  if AIplay(GAME) == False:
    break
#[0, 1, 2]
#[3, 4, 5]
#[6, 7, 8]
#"quit" to exit