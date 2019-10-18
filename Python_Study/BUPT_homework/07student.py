number = 0
number = int(input())
students = {}
while number != 0:
    temp = input().split()
    choice = int(temp[0])
    if choice == 1:
        if temp[1] in students:
            print('Students already exist')
        else:
            students[temp[1]] = (temp[2], int(temp[3]), int(temp[4]), int(temp[5]))
            print('Add success')
    elif choice == 2:
        if temp[1] in students:
            students.pop(temp[1])
            print('Delete success')
        else:
            print('Students do not exist')
    elif choice == 3:
        if temp[1] in students:
            students[temp[1]] = (students[temp[1]][0], int(temp[2]), int(temp[3]), int(temp[4]))
            print('Update success')
        else:
            print('Students do not exist')
    else:
        if temp[1] in students:
            print('Student ID:'+temp[1])
            print('Name:'+students[temp[1]][0])
            score = students[temp[1]][1] + students[temp[1]][2] + students[temp[1]][3]
            print('Average Score:%.1f'%(score/3))
        else:
            print('Students do not exist')
    number -= 1