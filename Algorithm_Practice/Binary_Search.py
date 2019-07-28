def GetList():
    L = []
    print('Please input your list to search from:')
    #L = input()
    L.append(input('List:'))
    return L

print('Welcome to Binary Search')
L = GetList()

print(L)
print('Please input the number you want to search:')
number = input('number:')
