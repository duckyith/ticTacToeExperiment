import random

def AIplay(G,debug):
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

  if debug == True:
    print(possible)
    print(choice)
    print(XWins,OWins,XBlock)

def AIchoice(G,p,flag):
    for i in range(len(p)):
      if flag in G.spaces[p[i]].blocks:
        return p[i]
    return p[0]

def UpdatePossibleMoves(G,p):
  for i in range (8,-1,-1):
    if G.spaces[i].value != 0:
      p.pop(i)

def updateFlags(G):
  XWins = check(G,3)
  OWins = check(G,8)
  XBlock = check(G,2)
  return XWins, OWins, XBlock

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