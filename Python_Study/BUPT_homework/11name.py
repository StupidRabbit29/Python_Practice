number = int(input())
name = []
for i in range(number):
    name.append(input().split())
test = input()
answer = []
for item in name:
    if item[1] == test:
        answer.append(item[0])
answer.sort()
for item in answer:
    print(item)