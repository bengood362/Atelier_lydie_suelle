# Board; lock is not simulated
# Board.py
from BoardGrid import BoardGrid
from Bonus import BonusColor, BonusType
class Board:
  def __init__(self, shape=4, bonus_colors=[], bonus_types=[], requirements=[]):
    # NOTE: example of bonus color: ((coordX, coordY), (color, bonus_value))
    self.shape = shape
    self.board = []
    for j in range(shape):
      tmp = []
      for i in range(shape):
        grid = BoardGrid()
        c = filter(lambda x: (j,i) in x, bonus_colors)
        t = filter(lambda x: (j,i) in x, bonus_types)
        if len(c)!=0:
          bonus_color = c[0][1][0]
          bonus_color_value = c[0][1][1]
          grid.add_color(BonusColor(bonus_color, bonus_color_value))
        if len(t)!=0:
          bonus_type = t[0][1][0]
          bonus_type_value = t[0][1][1]
          grid.add_type(BonusType(bonus_type, bonus_type_value))
        tmp.append(grid)
      self.board.append(tmp)
    self.requirements = requirements
  def add_requirement(self, requirement):
    self.requirements.append(requirement)
    return self
  def test_requirement(self):
    for req in self.requirements:
      pass
  # base on board setting
  def calculate_score(self):
    pass
  # 2x2 ONLY
  def print_bonus_color_board(self, padding=2):
    for j in range(self.shape):
      code_buffer = '|'
      for i in range(self.shape):
        code_buffer += self.board[j][i].getcc(padding=padding)
        code_buffer += '|'
      val_buffer = '|'
      for i in range(self.shape):
        val_buffer += self.board[j][i].getcv(padding=padding)
        val_buffer += '|'
      print ('+'+'-'*padding)*(len(code_buffer)/(padding+1))+'+'
      print code_buffer
      print val_buffer
    print ('+'+'-'*padding)*(len(code_buffer)/(padding+1))+'+'
  # 2x2 ONLY
  def print_bonus_type_board(self, padding=2):
    for j in range(self.shape):
      code_buffer = '|'
      for i in range(self.shape):
        code_buffer += self.board[j][i].gettc(padding=padding)
        code_buffer += '|'
      val_buffer = '|'
      for i in range(self.shape):
        val_buffer += self.board[j][i].gettv(padding=padding)
        val_buffer += '|'
      print ('+'+'-'*padding)*(len(code_buffer)/(padding+1))+'+'
      print code_buffer
      print val_buffer
    print ('+'+'-'*padding)*(len(code_buffer)/(padding+1))+'+'
  def print_board(self, padding=2):
    for j in range(self.shape):
      code_buffer = '|'
      for i in range(self.shape):
        code_buffer += self.board[j][i].get_current_color(padding=padding)
        code_buffer += '|'
      val_buffer = '|'
      for i in range(self.shape):
        val_buffer += ' '*padding
        val_buffer += '|'
      print ('+'+'-'*padding)*(len(code_buffer)/(padding+1))+'+'
      print code_buffer
      print val_buffer
    print ('+'+'-'*padding)*(len(code_buffer)/(padding+1))+'+'
  def get_possible_offset(self, attr):
    return (self.shape-attr.height, self.shape-attr.width)
  def get_shape(self):
    return (self.shape, self.shape)
  def apply_attr(self, attr, (offset_x, offset_y)):
    # offset: [coordX, coordY]
    if(((offset_x + attr.height) > self.shape) or ((offset_y + attr.width) > self.shape)):
      raise Exception("Board:apply_attr: Cannot have offset ({0}, {1})".format(offset_x, offset_y))
    for (x,y) in attr.coords:
      self.board[x+offset_x][y+offset_y].set_current_color(attr.color)
    return self
