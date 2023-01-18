class Length:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f'{self.feet} {self.inches}'

    def __add__(self, __o: object):
        if isinstance(__o, Length):
            return self.add_length(__o)
        elif isinstance(__o, int):
            return self.add_inches(__o)
        else:
            return NotImplemented

    def __radd__(self, __o: object):
        return self.__add__(__o)

    def add_length(self, L):
        f = self.feet + L.feet
        i = self.inches + L.inches
        if i >= 12:
            i = i - 12
        f += 1
        return Length(f, i)

    def add_inches(self, inches):
        f = self.feet + inches // 12
        i = self.inches + inches % 12
        if i >= 12:
            i = i - 12
        f += 1
        return Length(f, i)


length1 = Length(2, 10)
length2 = Length(3, 5)

print(length1 + length2)
print(length1 + 2)
print(length1 + 20)
print(20 + length1)
