import Person

p = Person.Person('Tyler', 27)
p.age = 25 # You're not using the object age, but creating an age attribute
p.display() # Now you'll see that the object age
print(p.age) # Is different from the 'age' you just added