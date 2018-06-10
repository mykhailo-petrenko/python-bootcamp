
# Tuples and arrays are iterable
it = (1,2,3)

for e in it:
    print (e)

# String iterator
# s = 'Hello Dolly'
# for l in s:
#     print(l)

# Unpacking
pairs = [(1,2,9), (3,4,19), (5,6,44), (7,8,55)]
for a,b,c in pairs:
    print(a)
    print(b)

# Dictionary iteration
d = {
    'k1': 'One',
    'k2': 'Two',
    'k3': 'Three'
}
# Keys
for k in d:
    print(k)
# Values
for v in d.values():
    print(v)
# Pairs
for k, v in d.items():
    print(f'{k}: {v}')