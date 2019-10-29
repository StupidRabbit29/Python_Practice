#demo0709.py
import csv
BasePath='c:\\data\\'
def writecsv(filepath):
    with open(filepath, 'w', newline='') as csvfile:
        f_csv = csv.DictWriter(csvfile,fieldnames=('姓名','语文'))
        f_csv.writeheader()             #在文件中写入标题行
        rows = [{'姓名': '赵六', '语文': 86}, {'姓名': '孙七', '语文': 95}]
        f_csv.writerows(rows)           #在文件中写入两行数据。

def readcsv(filepath):
    with open(filepath, 'r',newline='') as csvfile:
        f_csv = csv.DictReader(csvfile,fieldnames=('姓名','语文'))
        header = next(f_csv)
        print(header.values())   #这里的header是字典类型变量，用vlaue取得字典的值而不是键
        for row in f_csv:
            print(row.values())  #读出文件中的两行数据，row也是字典数据。

if __name__ == '__main__':
     writecsv(BasePath + 'scores.csv')
     readcsv(BasePath + 'scores.csv')
