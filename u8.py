class Book:
    def __init__(self, name, page_count, price):
        self.name = name
        self.page_count = page_count
        self.price = price

    def get_pages(self):
        self.page_count += 10

    def get_price(self):
        if self.page_count > 100:
            self.price /= 2

books = [
    Book("Kitob 1", 90, 20.0),
    Book("Kitob 2", 85, 15.0),
    Book("Kitob 3", 120, 30.0),
    Book("Kitob 4", 75, 10.0),
    Book("Kitob 5", 110, 25.0)
]

for book in books:
    book.get_pages()
    book.get_price()

print("\nYangilangan kitob ma'lumotlari:")
for book in books:
    print(f"Kitob nomi: {book.name}, Sahifa soni: {book.page_count}, Narxi: {book.price:.2f}")
