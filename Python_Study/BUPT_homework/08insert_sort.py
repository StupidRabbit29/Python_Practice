number = int(input())
array = input().split()
for i in range(number):
    array[i] = int(array[i])
for i in range(1, number):
    temp = array[0:i+1]
    temp.sort()
    array[0:i+1] = temp
    for j in range(number-1):
        print(array[j], end=' ')
    print(array[-1])