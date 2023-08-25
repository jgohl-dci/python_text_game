import random
water = 10

gonna_die = 0

for i in range(10 + 1):
    number = random.randrange(0, 2)
    gonna_die = gonna_die + number
    print(number)

print(gonna_die)
if gonna_die >= 5:
    print('You drink a little bit from the well and feel refreshed!')
    water += 1
else:
    print('You drink a little bit from the well. After a while your stomach starts to grumble.')
    print('Maybe it was a bad idea to drink this water.')