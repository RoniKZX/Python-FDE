"""
Question: Create a function that opens the flowers.txt,
reads every line in it, and saves it as a dictionary.

The main (separate) function should take user input
(user's first name and last name) and parse the user input
to identify the first letter of the first name.

It should then use it to print the flower name with
the same first letter (from dictionary created in the
first function).

Sample Output:

>>> Enter your First [space] Last name only: Bill Newman
>>> Unique flower name with the first letter: Bellflower
"""

# Write your code here
def getUserName() -> str:
    userName = input("Enter your First [space] Last name only: ")
    return userName.split(' ')

def createFlowerDict(filename='flowers.txt') -> dict:
    flowersDict = {}

    with open(filename, 'r') as flowers:
        for flower in flowers:
            flower = flower.split(': ')
            flowersDict[flower[0]] = flower[1].strip().title()

    return flowersDict

def getUniqueFlower(flowers: dict, userName: str) -> str:
    uniqueFlower = ''
    for letter, flower in flowers.items():
        if userName[0][0] == letter:
            uniqueFlower = f'Unique flower name with the first letter ({letter}): {flower}'
            break

    print(uniqueFlower)

# print the desired output
userName = getUserName()
flowers = createFlowerDict()
getUniqueFlower(flowers, userName)
