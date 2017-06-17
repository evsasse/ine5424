from algo1 import algo1
from algo2 import algo2

def draw(values):
    for value in values:
        print('.'*int(value))


MAX = 79

original = list(range(MAX*2))
original.reverse()
original = [max(i%MAX, (i*2)%MAX) for i in original]

print('-- ORIGINAL -- ')
draw(original)
input()

# print('-- ALGO 1 - 30 -- ')
# _algo1 = algo1(original, 30)
# draw(_algo1)
# input()

print('-- ALGO 1 - 60 -- ')
_algo1 = algo1(original, 60)
draw(_algo1)
input()

# print('-- ALGO 1 - 90 -- ')
# _algo1 = algo1(original, 90)
# draw(_algo1)
# input()

# print('-- ALGO 2 - 30 -- ')
# _algo2 = algo2(original, 30)
# draw(_algo2)
# input()

print('-- ALGO 2 - 60 -- ')
_algo2 = algo2(original, 60)
draw(_algo2)
input()

# print('-- ALGO 2 - 90 -- ')
# _algo2 = algo2(original, 90)
# draw(_algo2)
# input()