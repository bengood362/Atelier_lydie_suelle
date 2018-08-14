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
  def getf(self, padding=1):
    if(self.bonus_color == 'None'):
      return ' '*padding
    else:
      res = self.bonus_color[:padding]
      return res + ' '*(padding-len(res))
  def getv(self, padding=2):
    if(self.bonus_color == 'None'):
      return ' '*padding
    else:
      if (len(str(self.bonus_value)) == 2):
        return ' '*(padding-2)+str(self.bonus_value)
      else:
        return ' '*(padding-1)+'{0}'.format(self.bonus_value)

class BonusType:
  # Currently quality and inheritance are not in use
  possible_type = ['None', 'Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Quality', 'Inheritance', 'Effect']
  def __init__(self, bonus_type='None', bonus_value=0):
    if(bonus_type not in BonusType.possible_type):
      raise Err("BonusType:__init__: No such type: {0}".format(bonus_type))
    self.bonus_type = bonus_type
    self.bonus_value = bonus_value
  def getf(self, padding=2):
    if(self.bonus_type == 'None'):
      return ' '*padding
    else:
      res = self.bonus_type[:padding]
      return res + ' '*(padding-len(res))
  def getv(self, padding=2):
    if(self.bonus_type == 'None'):
      return ' '*padding
    else:
      if (len(str(self.bonus_value)) == 2):
        return ' '*(padding-2)+str(self.bonus_value)
      else:
        return ' '*(padding-1)+'{0}'.format(self.bonus_value)

class BoardGrid:
  def __init__(self, bonus_color=None, bonus_type=None, current_color=None):
    self.bonus_color = bonus_color
    self.bonus_type = bonus_type
    self.current_color = current_color
  def add_color(self, bonus_color):
    self.bonus_color = bonus_color
  def add_type(self, bonus_type):
    self.bonus_type = bonus_type
  def getcc(self, padding=1):
    if(self.bonus_color):
      return self.bonus_color.getf(padding)
    else:
      return ' '*padding
  def getcv(self, padding=2):
    if(self.bonus_color):
      return self.bonus_color.getv(padding)
    else:
      return ' '*padding
  def gettc(self, padding=2):
    if(self.bonus_type):
      return self.bonus_type.getf(padding)
    else:
      return ' '*padding
  def gettv(self, padding=2):
    if(self.bonus_type):
      return self.bonus_type.getv(padding)
    else:
      return ' '*padding
  def __str__(self):
    return ' ' if self.current_color is None else self.current_color
  def set_current_color(self, color):
    self.current_color = color
    return self
  def get_current_color(self, padding=2):
    return (' '*padding) if self.current_color is None else (self.current_color+' '*(padding-1))

# x: height, y: width, different with real world's mathematics, because I am bad at programming
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
      raise Err("Board:apply_attr: Cannot have offset ({0}, {1})".format(offset_x, offset_y))
    for (x,y) in attr.coords:
      self.board[x+offset_x][y+offset_y].set_current_color(attr.color)
    return self
# ingredient
class Attribute:
  possible_color = {'r': 1, 'g': 2, 'b': 3, 'y': 4, 'p': 5}
  # + width, height
  def __init__(self, color='r', coords=[]):
    # NOTE: coords: [(coordX1, coordY1), (coordX2, coordY2)]
    if(color not in Attribute.possible_color):
      raise Err("Attribute:__init__: No such color: {0}".format(color))
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
  def is_equal(self, attr):
    coords_self = self.coords[:]
    coords_other = attr.coords[:]
    color_self = self.color
    color_other = attr.color
    if(color_self != color_other):
      return False
    for coord_self in coords_self:
      for coord_other in coords_other:
        try:
          coords_self.remove(coord_other)
        except ValueError:
          return False
    if(len(coords_self) == 0):
      return True
    else:
      return False
  def get_all_rotation(self):
    result=[self]
    attr1=self.CW_rotate()
    attr2=attr1.CW_rotate()
    attr3=attr2.CW_rotate()
    # The result can either be [1, 2, 4]
    if(self.is_equal(attr1)):
      return [self]
    elif(self.is_equal(attr2)):
      return [self, attr1]
    else:
      return [self, attr1, attr2, attr3]
  def print_attr(self):
    s = '+'+'-'*self.width+'+\n'
    for i in range(self.height):
      s += '|'
      for j in range(self.width):
        s += self.color if (i,j) in self.coords else '.'
      s += '|\n'
    s += '+'+'-'*self.width+'+'
    print(s)
    return self

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
