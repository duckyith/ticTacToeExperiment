import numpy as np
from Space import Space


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