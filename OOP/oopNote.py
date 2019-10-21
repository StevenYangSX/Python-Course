'''OOP NOTES'''

class Student(object):

    #slots   :    restrict constructor: what attribute can user setup.
    __slots__ = ("_name","_age","_email")

    # constructor
    def __init__(self, name, age, email): 
        self._name = name
        self._age = age
        self._email = email

    #getter
    @property
    def getName(self):
        return self._name
    @property
    def getEmail(self):
        return self._email

    #setter
    @age.setter
    def age(self, num):
        self.age = num

            
    def display(self):
        print(f"student name: {self.name},  age is {self.age}")



student1 = Student("ggg",18, "sdf@gmail.com")

student1.display()