#Implement a generator called squares to yield the square of all numbers from (a) to (b).
#  Test it with a "for" loop and print each of the yielded values.

def sq(a, b):
    for i in range(a, b+1):
        yield i*i

a = int(input())
b = int(input())

for num in sq(a, b):
    print(num)