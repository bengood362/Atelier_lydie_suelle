# Atelier_core.py
color = {'r': 1, 'g': 2, 'b': 3, 'y': 4, 'p': 5}

class Err(Exception):
  pass
# Board; lock is not simulated
class BonusColor:
  possible_color = ['None','r','g','b','y','p']
  def __init__(self, bonus_color='None', bonus_value=0):
    if(bonus_color not in BonusColor.possible_color):
      raise Err("BonusColor:__init__: No such color: {0}".format(bonus_color))
    self.bonus_color = bonus_color
    self.bonus_value = bonus_value
  def getf(self):
    if(self.bonus_color == 'None'):
      return ' '
    else:
      return self.bonus_color[:1]
  def getv(self):
    if(self.bonus_color == 'None'):
      return '  '
    else:
      if (len(str(self.bonus_value)) == 2):
        return str(self.bonus_value)
      else:
        return ' {0}'.format(self.bonus_value)

class BonusType:
  # Currently quality and inheritance are not in use
  possible_type = ['None', 'Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Quality', 'Inheritance', 'Effect']
  def __init__(self, bonus_type='None', bonus_value=0):
    if(bonus_type not in BonusType.possible_type):
      raise Err("BonusType:__init__: No such type: {0}".format(bonus_type))
    self.bonus_type = bonus_type
    self.bonus_value = bonus_value
  def getf(self):
    if(self.bonus_type == 'None'):
      return '  '
    else:
      return self.bonus_type[:2]
  def getv(self):
    if(self.bonus_type == 'None'):
      return '  '
    else:
      if (len(str(self.bonus_value)) == 2):
        return str(self.bonus_value)
      else:
        return ' {0}'.format(self.bonus_value)

class BoardGrid:
  def __init__(self, bonus_color=None, bonus_type=None, current_color=None):
    self.bonus_color = bonus_color
    self.bonus_type = bonus_type
    self.current_color = current_color
  def add_color(self, bonus_color):
    self.bonus_color = bonus_color
  def add_type(self, bonus_type):
    self.bonus_type = bonus_type
  def getcc(self):
    if(self.bonus_color):
      return self.bonus_color.getf()
    else:
      return ' '
  def getcv(self):
    if(self.bonus_color):
      return self.bonus_color.getv()
    else:
      return '  '
  def gettc(self):
    if(self.bonus_type):
      return self.bonus_type.getf()
    else:
      return '  '
  def gettv(self):
    if(self.bonus_type):
      return self.bonus_type.getv()
    else:
      return '  '

class Board:
  def __init__(self, shape=4, bonus_colors=[], bonus_types=[], requirements=[]):
    # NOTE: example of bonus color: ((coordX, coordY), (color, value))
    self.shape=shape
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
  def test_requirement(self):
    for req in self.requirements:
      pass
  # base on board setting
  def calculate_score(self):
    pass
  # 2x2 ONLY
  def print_color_board(self):
    for j in range(self.shape):
      code_buffer = '|'
      for i in range(self.shape):
        code_buffer += self.board[j][i].getcc()
        code_buffer += ' |'
      val_buffer = '|'
      for i in range(self.shape):
        val_buffer += self.board[j][i].getcv()
        val_buffer += '|'
      print '+--'*(len(code_buffer)/3)+'+'
      print code_buffer
      print val_buffer
    print '+--'*(len(code_buffer)/3)+'+'
  # 2x2 ONLY
  def print_type_board(self):
    for j in range(self.shape):
      code_buffer = '|'
      for i in range(self.shape):
        code_buffer += self.board[j][i].gettc()
        code_buffer += '|'
      val_buffer = '|'
      for i in range(self.shape):
        val_buffer += self.board[j][i].gettv()
        val_buffer += '|'
      print '+--'*(len(code_buffer)/3)+'+'
      print code_buffer
      print val_buffer
    print '+--'*(len(code_buffer)/3)+'+'

# ingredient
class Attribute:
  def __init__(self, color='r', coords=[]):
    # NOTE: coords: [(coordX1, coordY1), (coordX2, coordY2)]
    maxX = max(zip(*coords)[0])
    maxY = max(zip(*coords)[1])
    minX = min(zip(*coords)[0])
    minY = min(zip(*coords)[1])
    self.color = color
    self.height = maxX-minX+1
    self.width = maxY-minY+1
    x_off = minX
    y_off = minY
    self.coords = map(lambda (x,y): (x-x_off, y-y_off), coords)
  def CW_rotate(self):
    new_coords = []
    for coord in self.coords:
      (x,y) = coord
      new_x = y
      new_y = self.height-x
      new_coords.append((new_x, new_y))
    return Attribute(color=self.color, coords=new_coords)
  def ACW_rotate(self):
    new_coords = []
    for coord in self.coords:
      (x,y) = coord
      new_x = self.width-y
      new_y = x
      new_coords.append((new_x, new_y))
    return Attribute(color=self.color, coords=new_coords)
  def print_attr(self):
    print self.color
    for coord in self.coords:
      print coord

class Ingredient:
  def __init__(self, attributes=[]):
    self.attributes = []
    for attr in attributes:
      self.attributes.append(attr)

# change color or nearby piece
class Catalyst:
  pass

#
class Medium:
  pass

# skills
class Requirement:
  pass
