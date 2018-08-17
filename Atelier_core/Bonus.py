# Bonus.py
class BonusColor:
  possible_color = ['None','r','g','b','y','p']
  def __init__(self, bonus_color='None', bonus_value=0):
    if(bonus_color not in BonusColor.possible_color):
      raise Exception("BonusColor:__init__: No such color: {0}".format(bonus_color))
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
      raise Exception("BonusType:__init__: No such type: {0}".format(bonus_type))
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