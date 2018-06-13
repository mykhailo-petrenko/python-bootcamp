mylist = [1,2,3,4,5,6]

square = lambda n: n**2

print( list(map(square, mylist)) )

is_even = lambda n: n%2==0

print( list(filter(is_even, mylist)) )


print( list(map(lambda n: n**3, mylist)) )

print( list(filter(lambda n: n%2!=0, mylist)) )
