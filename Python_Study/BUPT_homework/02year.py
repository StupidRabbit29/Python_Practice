year = input()
year = int(year)

if year%4 == 0 and year%100 != 0 or year%100 == 0 and year%400 == 0:
    print("Yes")
else:
    print("No")