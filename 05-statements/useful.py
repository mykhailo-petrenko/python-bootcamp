
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