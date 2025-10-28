from objects import Game
from AI2 import ModifiedAIplay

#Run to play out all possible games from your branch
GAME1 = Game()
GAME1.printGame()
final_x,final_o,final_d = ModifiedAIplay(GAME1,0,0,0,'X')
print(f'x wins: {final_x}, o wins: {final_o}, draws: {final_d}')