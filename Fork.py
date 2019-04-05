class Fork:

  isInUse = False
  postion = 0
  user = 0

  def __init__(self):
    self.isInUse = False

  def setPosition(self, index):
    self.position = index

  def setUser(self, index):
    self.user = index
    self.isInUse = True

  def __str__(self):
    result = ""
    result += "FORK " + str(self.position) + ": "
    # result += "in use" if self.isInUse else "not in use"
    if (self.isInUse):
      result += "in use by philosopher " + str(self.user)
    else:
      result += "not in use"
    return result
