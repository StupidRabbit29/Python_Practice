C = input()
number = int(input())
answer = []
for i in range(number):
    string = input()
    temp = string.upper()
    if(temp.count(C.upper()) >= 3):
        answer.append(string)
for i in range(len(answer)):
    print(answer.pop())
