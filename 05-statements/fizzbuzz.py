# Basic FizzBuzz
for n in range(100):
    s = ''

    if n % 3 == 0:
        s += 'Fizz'
    
    if n % 5 == 0:
        s += 'Buzz'

    if len(s) == 0:
        s = str(n)

    print(s)
        

# List Comprehensions
def fizzbuzz(n):
    return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, n+1)]

print( fizzbuzz(15) )