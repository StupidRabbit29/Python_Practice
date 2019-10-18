number = int(input())
name = {}
for i in range(number):
    a, b = input().split()
    if b in name:
        name[b] = name[b] + (a,)
    else:
        name[b] = (a,)
test = input()
# print(name[test])
temp = list(name[test])
temp.sort()
for i in range(len(temp)):
    print(temp[i])