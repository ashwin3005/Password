import random

f = None
def name():
    a = input("enter your full name without space first letter in capitalize [firstname_lastname] ")
    f = a
    
name()

if f[0] is f.upper():
    pswd()
else:
    print("enter name again due to unfulfilled criteria")
    name()
def pswd():
    b = random.randrange(99)
    c = random.randrange(99)
    paswrd = " "
    for i in range(0,len(a)):
        paswrd += a[len(a) - i-1]
    password = paswrd + "@" + str(b)+str(c)
    print(password)


