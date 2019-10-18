a, b = map(float, input().split())
bmi = a / (b ** 2)

if bmi < 18.5:
    print('A:%.2f'%bmi)
elif bmi >= 18.5 and bmi < 24:
    print('B:%.2f'%bmi)
elif bmi >= 24 and bmi < 28:
    print('C:%.2f'%bmi)
elif bmi >= 28:
    print('D:%.2f'%bmi)