class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount

# account1 = BankAccount("Tyler")    
# account2 = BankAccount("Joseph")

# account1.deposit(25)
# account2.deposit(15)

# account1.withdraw(5)
# account2.withdraw(3)

# account1.display()
# account2.display()

class Book:
    def __init__(self, isbn, title, author, publisher, pages: int, price: int, copies: int) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher       
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print(f"""
        ISBN: {self.isbn}
        TITLE: {self.title} 
        PRICE: {self.price}
        COPIES: {self.copies}
        \n""")

    def in_stock(self):
        return True if self.copies > 0 else False

    def sell(self):
        self.copies -= 1 if self.copies > 0 else print("The book is Out of stock.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 50 < new_price < 1000:
            self._price = new_price
        else:
            raise ValueError('The price should be between 50$ and 1000$')

class Fraction:
    def __init__(self, nr: int, dr: int = 1) -> None:
        self.nr = nr
        self.dr = dr

        if self.dr < 0:
            self.dr *= -1
            self.nr *= -1

    def show(self) -> None:
        print(f"{self.nr}/{self.dr}")

    def multiply(self, x) -> None:
        if isinstance(x, int):
            x = Fraction(x) 
        
        return Fraction(self.nr * x.nr, self.dr * x.dr)

    def add(self, x) -> None:
        if isinstance(x, int):
            x = Fraction(x)

        return Fraction((self.nr*x.dr + x.nr*self.dr), (self.dr*x.dr))

if __name__ == '__main__':
    book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
    book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
    book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
    book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

    books = [book1, book2, book3, book4]

    for book in books:
        book.display()

    print([j.title for j in books if j.author == 'Jack'])

    f1 = Fraction(2,3)
    f1.show()
    f2 = Fraction(3,4)
    f2.show()
    f3 = f1.multiply(f2)
    f3.show()
    f3 = f1.add(f2)
    f3.show()
    f3 = f1.add(5) 
    f3.show()
    f3 = f1.multiply(5) 
    f3.show()