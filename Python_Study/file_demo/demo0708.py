#demo0708.py
BasePath='c:\\data\\'
import csv
def writecsv1(filepath):
    with open(filepath, 'a',newline='',encoding="utf-8") as csvfile:
        rows = [('赵六',86,97),('孙七',95,95)]
        f_csv = csv.writer(csvfile)
        f_csv.writerows(rows)           #在文件末尾写入两行数据。

if __name__ == '__main__':
        writecsv1(BasePath + 'table.csv')
