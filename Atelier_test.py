# Atelier_test.py
import Atelier_core as Atelier
# ------------- Check gameboard ------------- #
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
board.print_bonus_color_board(padding=4)
print ("\n###########################")
print ("# This is the  type_board #")
print ("###########################\n")
board.print_bonus_type_board(padding=4)
# ------------- End check gameboard ------------- #

# ------------- Check attribute ------------- #
attr = Atelier.Attribute(color='r',coords=[(0,1),(1,3),(2,0),(2,3)])
# new_attr = attr.CW_rotate()
# new_attr.print_attr()
# new_attr2 = attr.ACW_rotate()
# new_attr2.print_attr()
# attr2 = Atelier.Attribute(color='r',coords=[(0,1),(1,3),(2,0),(2,3)])
# attr3 = Atelier.Attribute(color='y',coords=[(0,1),(1,3),(2,0),(2,3)])
# attr4 = Atelier.Attribute(color='r',coords=[(0,1),(1,3),(2,0),(2,3),(0,0)])
# attr5 = Atelier.Attribute(color='r',coords=[(0,1),(1,3),(2,0),])
# assert attr.is_equal(attr2), "attr should be same as attr2"
# assert (not attr.is_equal(attr3)), "attr should have different color with attr3"
# assert (not attr.is_equal(attr4)), "attr have 1 less element than attr4"
# assert (not attr.is_equal(attr5)), "attr have 1 more element than attr5"
# print ("Should have 4 rotation type")
# for a in attr.get_all_rotation():
#   a.print_attr()
# print ("Should have 2 rotation type")
attr6 = Atelier.Attribute(color='y',coords=[(0,0),(1,1)])
# for a in attr6.get_all_rotation():
#   a.print_attr()
attr7 = Atelier.Attribute(color='y',coords=[(0,0)])
# print ("Should have 1 rotation type")
# for a in attr7.get_all_rotation():
#   a.print_attr()
attr8 = Atelier.Attribute(color='r',coords=[(0,0),(0,1),(1,0)])
print 'board shape: {0}'.format(board.get_shape())
attr.print_attr()
print board.get_possible_offset(attr)
attr6.print_attr()
print board.get_possible_offset(attr6)
attr7.print_attr()
print board.get_possible_offset(attr7)
board.apply_attr(attr7, (4,4)) # Should have error
board.apply_attr(attr8, (1,1))
board.apply_attr(attr6, (0,0))
board.apply_attr(attr7, (3,3))
board.print_board()
# ------------- End check attribute ------------- #