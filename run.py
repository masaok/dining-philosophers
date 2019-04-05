#!/usr/bin/env python3

from Philosopher import Philosopher
from Table import Table
from Fork import Fork

# Initialize the philosophers and forks
philosophers = []
forks = []
for count in range(5):
  p = Philosopher()
  f = Fork()
  philosophers.append(p)
  forks.append(f)

# Initialize the table
table = Table(philosophers, forks)

# Display initial state
print(table)

# Allow all philosophers to attempt to eat
table.eat()

# Display next state
print(table)