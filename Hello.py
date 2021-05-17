import math
def f(n):
    if(n<10) :
        return n
    else :
        return f(n/10)+(n%10)*pow(10.0,round(math.log(n,10)))

a=f(3423)
b=math.log(3423,10)
print(a)
print(round(b))




