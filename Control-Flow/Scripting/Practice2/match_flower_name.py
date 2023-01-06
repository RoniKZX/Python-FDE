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
def createFlowerDict(filename='flowers.txt') -> dict:
    flowersDict = {}

    with open(filename, 'r') as flowers:
        for flower in flowers:
            flower = flower.split(': ')
            flowersDict[flower[0].capitalize()] = flower[1].strip().title()

    return flowersDict

def main() -> None:
    flowerDict = createFlowerDict()
    fullName = input("Enter your First [space] Last name only: ")
    firstName = fullName.split(' ')[0][0].capitalize()

    print(f'Unique flower name with the first letter ({firstName[0].capitalize()}): {flowerDict[firstName[0]]}')

# print the desired output
main()