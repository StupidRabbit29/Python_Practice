import pandas
round = int(input())
score = 0
while round != 0:
    a, b = map(int, input().split())
    if a==3 and (b==0 or b==1):
        score += 3
    elif a==3 and b==2:
        score += 2
    elif a==2 and b==3:
        score += 1
    round -= 1
print(score)
