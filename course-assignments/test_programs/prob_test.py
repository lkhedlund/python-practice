# testing probability

import random

prompt = input("Number between 1-100: ")
probX = int(prompt)
probY = 100 - int(prompt)

print("X: %r, Y: %r" % (probX, probY))

print("Chance of one of two things happening")

choices = ["X"] * probX + ["Y"] * probY
print(choices)
print(random.choice(choices))
