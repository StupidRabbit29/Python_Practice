def mirror(a):
    left = str(a)
    right = left[::-1]
    if left == right:
        return True
    else:
        return False


def prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


a, b = map(int, input().split())
for i in range(a, b + 1):
    if mirror(i) and prime(i):
        print(i)
