class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value and self.right != None:
      self.right.insert(value)

    elif value <= self.value and self.left != None:
      self.left.insert(value)

    elif value > self.value and self.right == None:
      self.right = BinarySearchTree(value)

    elif value <= self.value and self.left == None:
      self.left = BinarySearchTree(value)

  def contains(self, target):

    if target == self.value:
      return True

    elif target > self.value:
      if self.right == None:
        return False
      else:
        return self.right.contains(target)

    elif target < self.value:
      if self.left == None:
        return False
      else:
        return self.left.contains(target)

  def get_max(self):
    if self.right == None:
      return self.value
    else:
      return self.right.get_max()


