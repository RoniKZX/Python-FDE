class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age # self.age is actually a call to the setter

    def display(self):
        print(self.name, self.age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age # Here is the real atttribute
        else:
            raise ValueError('Age must be between 20 and 80')

if __name__ == '__main__':
    p = Person('Tyler', 30)
    p.display()