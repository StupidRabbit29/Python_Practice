number = int(input())
books = []

while number != 0:
    book = input().split()
    for i in range(1, 7):
        book[i] = int(book[i])
    books.append(book)
    number = number - 1

books = sorted(books, key=lambda x: (-x[5], x[2], x[3], x[4], x[1], x[6]), reverse=True)
for book in books:
    print(book[0], book[1], book[2], book[3], book[4], book[5], book[6])
