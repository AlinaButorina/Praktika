import csv


def write_books_csv(filename):
    books = [
        ["Преступление и наказание", "Фёдор Достоевский", 1866],
        ["Портрет Дориана Грея", "Оскар Уайльд", 1890],
        ["Маленький принц", "Экзюпери", 1942],
        ["Важные годы", "Мэг Джей", 2012],
        ["Искусство любить", "Эрих Фромм", 1956]
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Книга", "Автор", "Год выпуска"])
        writer.writerows(books)


filename = "books.csv"
write_books_csv(filename)
