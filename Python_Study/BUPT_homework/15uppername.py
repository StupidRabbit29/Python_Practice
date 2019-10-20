from collections import Counter
import re

number = int(input())
books = []

while number != 0:
    book = input()
    books.append(book)
    number = number - 1


books = sorted(books, key=lambda x: "".join((Counter(x) & Counter(x.upper())).keys()))
books = sorted(books, key=lambda x: (re.sub(u"[^\u0041-\u005a]", "", x)))

for book in books:
    print(book)
