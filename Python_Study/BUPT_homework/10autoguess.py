number = int(input())
command = []
for i in range(number):
    command.append(input())
command.sort()
test = input()
for item in command:
    if item[0:len(test)] == test:
        print(item)