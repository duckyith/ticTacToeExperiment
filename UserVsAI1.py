from objects import Game
from AI1 import AIplay,playerInput

#Run to play against the AI yourself
GAME = Game()
GAME.printGame()
while True:
  if playerInput(GAME) == False:
    break
  if AIplay(GAME,False) == False:
    break
#[0, 1, 2]
#[3, 4, 5]
#[6, 7, 8]
#"quit" to exit