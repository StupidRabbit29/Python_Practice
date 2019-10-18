a, b = map(int, input().split())
if a == b:
    print("The two numbers are equal.")
elif a < b:
    print("The larger number is %d, the smaller number is %d."%(b,a))
else:
    print("The larger number is %d, the smaller number is %d."%(a,b))