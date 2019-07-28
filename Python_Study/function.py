import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

#空函数
#注意pass可以用作占位符，先不写内容，但能正常运行程序
def nop():
    pass

#返回多个值
def move(x, y, step, angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx, ny

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b*b-4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b*b-4*a*c)) / (2*a)
    return x1, x2

def power(x, n=2):
    s = 1
    while n>0:
        n = n - 1
        s = s * x
    return s

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def clac(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def clac(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    print('name:',name,'age:',age,'other:',kw)

def person2(name, age, *, city, job):
    print(name, age, city, job)

def product(x, y=1, *other):
    result = x * y
    for n in other:
        result = result * n
    return result

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def fack_iter(num, product):
    if num == 1:
        return product
    else:
        return fact_iter(num - 1, product * num)

def fact2(n):
    return fact_iter(n, 1)


#汉诺塔

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)