"""
Example of read/write properties
"""

class Employee:
    def __init__(self, name, password, salary) -> None:
        self._name = name
        self._password = password
        self._salary = salary
    
    # Read only
    @property
    def name(self):
        return self._name

    @property
    def password(self):
        raise AttributeError('Password not readable')

    # Write only
    @password.setter
    def password(self, new_password): # Constructor function overload
        self._password = new_password

    # With a getter and a setter
    # The salary becomes a r/w attribute
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

e = Employee('Tyler', 'TopFan', 7000)