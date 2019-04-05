class Philosopher:

  seat = 0
  isEating = False
  leftFork = 0
  rightFork = 0

  def __init__(self):
    self.isEating = False

  def setSeat(self, index):
    self.seat = index

  def grabForks(self, forks):

    # Get Right Fork index
    rightFork = self.seat - 1
    if (rightFork < 0):
      rightFork = len(forks) - 1
    print("trying right fork: " + str(rightFork))

    # Get Left Fork index
    leftFork = self.seat
    if (leftFork >= len(forks)):
      leftFork = 0
    print("trying left  fork: " + str(leftFork))

    # Check if forks are available to grab
    if (not forks[rightFork].isInUse and
        not forks[leftFork].isInUse):

      print("grabbing forks: " + str(leftFork) + " and " + str(rightFork))

      # Grab the right fork
      forks[rightFork].setUser(self.seat)
      self.rightFork = rightFork

      # Grab the left fork
      forks[leftFork].setUser(self.seat)
      self.leftFork = leftFork

      self.isEating = True

    return forks

  # normal print
  def __str__(self):
    result = ""
    result += "PHIL " + str(self.seat) + ": "
    # result += "eating" if self.isEating else "not eating"

    if (self.isEating):
      result += "eating with forks " \
        + "left fork " + str(self.leftFork) + " and " \
        + "right fork " + str(self.rightFork)
    else:
      result += "not eating"

    return result

  # for pprint'ing (not needed, just calls __str__)
  def __repr__(self):
    return str(self)
