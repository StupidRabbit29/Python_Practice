from collections import Counter
import re

number = int(input())
books = []

while number != 0:
    book = input()
    books.append(book)
    number = number - 1


books = sorted(books, key=lambda x: "".join((Counter(x) & Counter(x.upper())).keys()))
# 上面这种方法样例可以通过，但是提交结果为答案错误
books = sorted(books, key=lambda x: (re.sub(u"[^\u0041-\u005a]", "", x)))

for book in books:
    print(book)
