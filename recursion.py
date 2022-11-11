'''def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

num = fact(21)
print(num)



x = lambda a,b : a*b*(a+b)
num = x(5,10)

print(num)'''


def name(x):
    return lambda a,b,c: (a*x*b-a*x*c)*a*x*c

num = name(10)
print(num(5))
print(num(4))
print(num(9))