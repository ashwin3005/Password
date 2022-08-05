import random

with open('w.txt') as f:
    
    words = [line.rstrip() for line in f]

# printing elements from list
print(random.sample(words, 5))

