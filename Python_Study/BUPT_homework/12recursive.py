def re(a, n):
    if n == 0:
        return 1 + a
    else:
        return 1 + a * re(a, n - 1)


n, a = map(int, input().split())
print(re(a, n))