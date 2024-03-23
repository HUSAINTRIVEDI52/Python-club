import random
x = random.randint(1,90)
print(x)
mylist = ['rock','paper','scissor']
y=random.choice(mylist)
print(y)
cards = [1,2,3,4,5,6,7,8,9,'j','k','q','a']
random.shuffle(cards)
print(cards)