class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []
    
  def enqueue(self, item):
    self.storage.insert(0, item)
  
  def dequeue(self):
    return self.storage.pop() if len(self.storage) > 0 else None

  def len(self):
    return len(self.storage)
