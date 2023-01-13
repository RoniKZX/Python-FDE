class Fraction:
    def __init__(self, nr: int, dr: int = 1) -> None:
        self.nr = nr
        self.dr = dr

        if self.dr < 0:
            self.dr *= -1
            self.nr *= -1

        self._reduce()

    def show(self) -> None:
        print(f"{self.nr}/{self.dr}")

    def multiply(self, x) -> None:
        if isinstance(x, int):
            x = Fraction(x) 
        
        f = Fraction(self.nr * x.nr, self.dr * x.dr)
        return f

    def add(self, x) -> None:
        if isinstance(x, int):
            x = Fraction(x)

        f = Fraction((self.nr*x.dr + x.nr*self.dr), (self.dr*x.dr))
        return f

    # Highest Common Factor
    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s

    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        
        if h == 0:
            return

        self.nr //= h.nr
        self.dr //= h.dr

class SalesPerson:
    total_revenue = 0
    names = []
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(name)

    def make_sale(self,money):
        self.sales_amount += money
        SalesPerson.total_revenue += money

    def show(self):
        print(self.name, self.age, self.sales_amount)

# class Employee:
#     domains = set()
#     allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

#     def __init__(self,name,email: str):
#         self.name = name
#         self.email = email
#         Employee.domains.add(email[email.index('@') + 1:])
    
#     def display(self):
#         print(self.name, self.email)

class Employee:
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self,name,email):
        self.name = name
        domain = email[email.index('@') + 1:]
        if domain not in Employee.allowed_domains:
            raise RuntimeError('Invalid email')
        
        self.email = email

    def display(self):
        print(self.name, self.email)

e1 = Employee('John','john@gmail.com')
e2 = Employee('Jack','jack@yahoo.com')
e3 = Employee('Jill','jill@outlook.com')
e4 = Employee('Ted','ted@yahoo.com')
e5 = Employee('Tim','tim@xmail.com')

# e1 = Employee('John','john@gmail.com')
# e2 = Employee('Jack','jack@yahoo.com')
# e3 = Employee('Jill','jill@outlook.com')
# e4 = Employee('Ted','ted@yahoo.com')
# e5 = Employee('Tim','tim@gmail.com')
# e6 = Employee('Mike','mike@yahoo.com')

# s1 = SalesPerson('Bob', 25)
# s2 = SalesPerson('Ted', 22)
# s3 = SalesPerson('Jack', 27)

# s1.make_sale(1000)
# s1.make_sale(1200)
# s2.make_sale(5000)
# s3.make_sale(3000)
# s3.make_sale(8000)

# s1.show()
# s2.show()
# s3.show()

# print(SalesPerson.total_revenue, SalesPerson.names)