# Ingredient.py
class Ingredient:
  def __init__(self, attributes=[]):
    self.attributes = []
    for attr in attributes:
      self.attributes.append(attr)