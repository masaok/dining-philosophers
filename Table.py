class Table:

  philosophers = []
  forks = []

  def __init__(self, philosophers, forks):
    self.philosophers = philosophers
    self.forks = forks

    for index in range(len(self.philosophers)):
      self.philosophers[index].setSeat(index)
      self.forks[index].setPosition(index)

  def eat(self):
    # for p in self.philosophers:
    for index in range(len(self.philosophers)):
      print("PHIL " + str(index) + " trying to grab forks")
      p = self.philosophers[index]
      # print(p)

      # Philosopher attempts to grab adjacent forks
      self.forks = p.grabForks(self.forks)      

  def __str__(self):
    result = "\n"
    index = 0
    # for p in self.philosophers:
    for index in range(len(self.philosophers)):
      p = self.philosophers[index]
      f = self.forks[index]

      result += str(p) + "\n"
      result += str(f) + "\n"
      # result += "\n"

      index += 1

    return result