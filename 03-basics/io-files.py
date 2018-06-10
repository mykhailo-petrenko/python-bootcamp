import os

path = os.path.abspath('../data/test.txt')
print(f'Hello IO with files: {path}')

with open(path) as myfile:
    print('\n====')
    print(myfile.readlines())
    print('\n====')
    print(myfile.read())
    print('\n====')
    myfile.seek(10)
    print(myfile.read())
    print('\n====')

# Throws an error
# myfile.readlines()
