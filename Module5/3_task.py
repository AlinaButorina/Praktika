import csv


def search_books_by_year_range(filename, start_year, end_year):
    found_books = []
    try:
        start_year = int(start_year)
        end_year = int(end_year)
        if start_year > end_year:
            print("Некорректный запрос: начальный год больше конечного года")
            return
    except ValueError:
        print("Некорректный запрос: введены некорректные годы")
        return

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            year = int(row[2])
            if start_year <= year <= end_year:
                found_books.append(row)

    if found_books:
        print(f"Книги, выпущенные в промежутке {start_year}-{end_year}:")
        for book in found_books:
            print(f"Название: {book[0]}, Автор: {book[1]}")
    else:
        print("Нет книг в указанном промежутке годов")


filename = "books.csv"

start_year = input("Введите начальный год: ")
end_year = input("Введите конечный год: ")
search_books_by_year_range(filename, start_year, end_year)
