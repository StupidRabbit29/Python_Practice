#demo0707.py
BasePath='c:\\data\\'
import csv
with open(BasePath+'table4.csv', 'r', encoding="utf-8") as csvfile:
    f_csv = csv.reader(csvfile, delimiter=',')
    print(f_csv.line_num)
    print('--------Header--------')
    print(next(f_csv))    #f_csv是一个迭代对象,next函数从迭代对象中找出下一个项目
    print('--------Data-----------')
    for row in f_csv:
        print(row)
    print(f_csv.dialect)
    print(f_csv.line_num)