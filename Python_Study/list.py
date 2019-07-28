classmates=['Mike', 'Jim', 'Black']
print(len(classmates))

print(classmates[1])
print(classmates[2])
print(classmates[-1])
classmates.append('Zhu')

print(classmates[3])
classmates.insert(1, 'Fu')
classmates.pop()
classmates.pop(1)

classmates[len(classmates)-1]='Zhu'
print(classmates[len(classmates)-1])

L=['python', ['C', 'C++'], 'java']
print(L[1][0])

#list是可变对象，我们对它排序
classmates.sort()
print(classmates)

