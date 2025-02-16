#Create a generator that generates the squares of numbers up to some number N.
def sq(n):
    for i in range(n+1):
        yield i*i

n=int(input())
for num in sq(n):
    print(num)

