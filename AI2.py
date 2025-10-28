from AI1 import UpdatePossibleMoves,updateFlags,AIchoice

def ModifiedAIplay(G,x,o,d,Turn):
  possible = [0,1,2,3,4,5,6,7,8]
  choice = 0
  full_x = x
  full_o = o
  full_d = d
  UpdatePossibleMoves(G,possible) #The game stat run will still need to process the board to see what moves are available because of the previous move
  G.printGame()

  if len(possible) == 0: #no longer printing anything, preparing for recursion, return draw stat + 1
    print('draw!')
    print(full_x, full_o, full_d+1)
    return full_x, full_o, full_d+1

  XWins,OWins,XBlock = updateFlags(G)
  print(XWins,OWins,XBlock)

  if Turn == 'X':
    if XBlock != 0:
      print(full_x+1,full_o,full_d)
      return full_x+1,full_o,full_d #X won, back out and add results
    elif OWins != 0:
      print(f"Possible moves: {possible}")
      print(f"Flag being checked: {OWins}") # or OWins, depending on the elif block
      choice = AIchoice(G,possible,OWins) #choice overwritten
      print(f"choice: {choice}")

      G.spaces[choice].markX()
      print('running forced recursion for O')
      dx, do, dd = ModifiedAIplay(G,0,0,0,'O')
      full_x += dx
      full_o += do
      full_d += dd
      print(f'updated after forced children: {full_x},{full_o},{full_d}')
      return full_x,full_o,full_d
    elif OWins == 0 and XBlock == 0:
      dx, do, dd = TryAllPaths(G,possible,0,0,0,'X')
      full_x += dx
      full_o += do
      full_d += dd
      print(f'updated after all paths: {full_x},{full_o},{full_d}')
      return full_x,full_o,full_d

  elif Turn == 'O':
    if OWins != 0:
      print(full_x,full_o+1,full_d)
      return full_x,full_o+1,full_d #O won, back out and add results
    elif XBlock != 0:
      print(f"Possible moves: {possible}")
      print(f"Flag being checked: {XBlock}") # or OWins, depending on the elif block
      choice = AIchoice(G,possible,XBlock) #choice overwritten
      print(f"choice: {choice}")

      G.spaces[choice].markO()
      print('running forced recursion for X')
      dx, do, dd = ModifiedAIplay(G,0,0,0,'X')
      full_x += dx
      full_o += do
      full_d += dd
      print(f'updated after forced children: {full_x},{full_o},{full_d}')
      return full_x,full_o,full_d
    elif OWins == 0 and XBlock == 0:
      dx, do, dd = TryAllPaths(G,possible,0,0,0,'O')
      full_x += dx
      full_o += do
      full_d += dd
      print(f'updated after all paths: {full_x},{full_o},{full_d}')
      return full_x,full_o,full_d
  return 
  


def TryAllPaths(G,p,x,o,d,Turn):
  total_x = x
  total_o = o
  total_d = d
  choice = 0

  for i in range(len(p)): #exausts the whole list of possible options recursively adding the game results
    newGAME = G.copy()
    choice = p[i]
    print(p)
    if Turn == 'X':
      newGAME.spaces[p[i]].markX()
      print(f'running {i} recursion for O')
      dx, do, dd = ModifiedAIplay(newGAME,x,o,d,'O')
      total_x += dx
      total_o += do
      total_d += dd
      print(f'AllPathsConclusion: {total_x},{total_o},{total_d}')

    elif Turn == 'O':
      newGAME.spaces[p[i]].markO()
      print(f'running {i} recursion for O')
      dx, do, dd = ModifiedAIplay(newGAME,x,o,d,'X')
      total_x += dx
      total_o += do
      total_d += dd
      print(f'AllPathsConclusion: {total_x},{total_o},{total_d}')

  return total_x,total_o,total_d