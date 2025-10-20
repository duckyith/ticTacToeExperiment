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

  def checkBlock(self,block):
    if self.blocks.contains(block):
      return True
    else:
      return False

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