import random

# Choosing one random word
with open('w.txt') as f:
    words = [line.rstrip() for line in f]
random_word = random.sample(words, 1)    # Choose one random word

# Symbols, Alphabet, Number
symbols = '!@#$%&<>?'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'

randomWord = random_word[0]
number = random.choice(list(num))
alpha = random.choice(list(alphabet))
symbols = random.choice(list(symbols))

# randomWord LowerCase or UpperCase
coin = random.randint(0,1)     # flipping a coin
password = []

if coin == 1:
    password.extend([randomWord.upper()])
else:
    password.extend([randomWord])

# alpha LowerCase or UpperCase
coin = random.randint(0,1)     # flipping a coin

if coin == 1:
    password.extend([number,alpha.upper(),symbols])
else:
    password.extend([number,alpha,symbols])

# Shuffle Order
random.shuffle(password)

password = ''.join([str(elem) for elem in password])

print(password)      # print the password