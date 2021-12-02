n = int(input())
book_count = {}

for i in range(n) :
    book = input()
    if book in book_count :
        book_count[book] += 1
    else :
        book_count[book] = 1

book_count = sorted(book_count.items(), key=lambda x:(-x[1], x[0]))

print(book_count[0][0])
