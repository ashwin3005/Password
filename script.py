import random

# reading w.txt
with open('w.txt') as f:
    words = [line.rstrip() for line in f]


symbols = '!@#$%&<>?'
alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'

random_word = random.sample(words, 1)    #list


a = random_word[0]
b = random.choice(list(num))
c = random.choice(list(alpha))
d = random.choice(list(symbols))

coin = random.randint(0,1)     # flipping a coin

password = []


if coin == 1:
    password.extend([a.upper(),b,c,d])
else:
    password.extend([a,b,c.upper(),d])

random.shuffle(password)

password = ''.join([str(elem) for elem in password])
  
print(password)      # print the password
