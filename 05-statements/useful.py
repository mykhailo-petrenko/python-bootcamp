
# range generator
for n in range(0, 10, 2):
    print(n)

print(list(range(5)))

# enumerate
word = 'Hello Dolly'
for (index, letter) in enumerate(word):
    print(f'{index}: {letter}')

# zip
l1 = [1,2,3,4]
l2 = ['a', 'b', 'c', 'd']
l3 = [222,3333,4444,555,666,777]
for item in zip(l1, l2, l3):
    print(item)

# in
print(1 in [2,3,4])
print('b' in 'beta')
print('key1' in {'key1': 123})

# min/max
nums = [21,2,65,3,7]
print(min(nums))
print(max(nums))

# random
from random import shuffle

mylist = list(range(10))
print(mylist)
shuffle(mylist)
print(mylist)

from random import randint
print(randint(10, 60))
