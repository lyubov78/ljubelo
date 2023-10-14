# TODO Найдите количество книг, которое можно разместить на дискете
# Объем дискеты
size = 1.44  # Мб
size_one_symbols = 4  # байта

# Параметры книги
pages = 100
lines = 50
symbols = 25

# Объем одной книги
size_book_byte = pages * lines * symbols * 4
size_book_Mbyte = (size_book_byte / 1024) / 1024

total_books = int(size // size_book_Mbyte)

print("Количество книг, помещающихся на дискету:", total_books)
