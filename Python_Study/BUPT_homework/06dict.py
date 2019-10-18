wordnum = 0
wordnum = int(input())
dog_2_cat = {}
while wordnum !=0:
    a, b = input().split()
    dog_2_cat[b] = a
    wordnum -= 1
while True:
    dogword = input()
    if dogword == 'dog':
        break
    else:
        if dogword in dog_2_cat:
            print(dog_2_cat[dogword])
        else:
            print('dog')