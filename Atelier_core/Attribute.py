# Attribute.py
class Attribute:
  possible_color = {'r': 1, 'g': 2, 'b': 3, 'y': 4, 'p': 5}
  # + width, height
  def __init__(self, color='r', coords=[]):
    # NOTE: coords: [(coordX1, coordY1), (coordX2, coordY2)]
    if(color not in Attribute.possible_color):
      raise Exception("Attribute:__init__: No such color: {0}".format(color))
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
