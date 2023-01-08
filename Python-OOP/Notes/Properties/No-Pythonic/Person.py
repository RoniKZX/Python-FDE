class Person:
    def __init__(self, name, age) -> None:
        self.name = name

        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError('Age must be between 20 and 80')

    def display(self):
        print(self.name, self._age)

    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 and 80')

    def get_age(self):
        return self._age

if __name__ == '__main__':
    p = Person('Joseph', 30)
    p.display()
