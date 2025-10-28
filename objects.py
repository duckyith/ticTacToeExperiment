import numpy as np
import copy

class Space:
  def __init__(self, Xcord, Ycord, value, blocks):
    self.Xcord = Xcord
    self.Ycord = Ycord
    self.value = value
    self.blocks = blocks

  def markX(self):
    self.value = 1

  def markO(self):
    self.value = 4

  def markBlank(self):
    self.value = 0

  def printSpace(self,all):
    if (self.value == 0):
      val = "-"
    if (self.value == 1):
      val = "X"
    if (self.value == 4):
      val = "O"
    if (all):
      print(self.Xcord,self.Ycord,":",val)
    else:
      return val

class Game:
  def __init__(self):
    self.TL = Space(0,0,0,[1,4,7])
    self.TM = Space(0,1,0,[1,5])
    self.TR = Space(0,2,0,[1,6,8])
    self.ML = Space(1,0,0,[2,4])
    self.MM = Space(1,1,0,[2,5,7,8])
    self.MR = Space(1,2,0,[2,6])
    self.BL = Space(2,0,0,[3,4,8])
    self.BM = Space(2,1,0,[3,5])
    self.BR = Space(2,2,0,[3,6,7])
    self.OW = 0
    self.XW = 0
    self.XB = 0

    self.spaces = [self.TL,self.TM,self.TR,self.ML,self.MM,self.MR,self.BL,self.BM,self.BR]

  def printGame(self):
    gameBoard = np.array([
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-'],
    ])
    for space in self.spaces:
      gameBoard[space.Xcord][space.Ycord] = space.printSpace(0)
    print(gameBoard)

  def copy(self):
    new_game = Game()
    new_game.OW = self.OW
    new_game.XW = self.XW
    new_game.XB = self.XB

    new_game.spaces = [copy.copy(space) for space in self.spaces]

    new_game.TL = new_game.spaces[0]
    new_game.TM = new_game.spaces[1]
    new_game.TR = new_game.spaces[2]
    new_game.ML = new_game.spaces[3]
    new_game.MM = new_game.spaces[4]
    new_game.MR = new_game.spaces[5]
    new_game.BL = new_game.spaces[6]
    new_game.BM = new_game.spaces[7]
    new_game.BR = new_game.spaces[8]

    return new_game