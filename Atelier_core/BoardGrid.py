# BoardGrid.py
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
