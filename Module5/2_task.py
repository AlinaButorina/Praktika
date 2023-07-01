import csv


def add_books(filename, num_records):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        for _ in range(num_records):
            book = []
            book.append(input("Введите название книги: "))
            book.append(input("Введите имя автора: "))
            book.append(int(input("Введите год выпуска: ")))
            writer.writerow(book)


def search_books_by_author(filename, author):
    found_books = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1] == author:
                found_books.append(row)

    if found_books:
        print(f"Книги автора {author}:")
        for book in found_books:
            print(f"Название: {book[0]}, Год выпуска: {book[2]}")
    else:
        print(f"Нет книг автора {author}")


filename = "books.csv"

num_records = int(input("Введите количество записей для добавления: "))
add_books(filename, num_records)

author = input("Введите имя автора, чтобы найти его книги: ")
search_books_by_author(filename, author)
