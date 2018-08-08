# Atelier_test.py
import Atelier_core as Atelier

bonus_color = [
  ((0,0),('r',1)),
  ((1,1),('r',1)),
  ((3,0),('r',-1))
]
bonus_type = [
  ((3,3),('Sun',1)),
  ((2,2),('Mars',2)),
  ((0,3),('Quality',-5))
]
board = Atelier.Board(shape=4, bonus_colors=bonus_color, bonus_types=bonus_type)
print ("\n###########################")
print ("# This is the color_board #")
print ("###########################\n")
board.print_color_board()
print ("\n###########################")
print ("# This is the  type_board #")
print ("###########################\n")
board.print_type_board()