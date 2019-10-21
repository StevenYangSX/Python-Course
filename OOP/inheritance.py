class Person(object):
    # __slots__ = (.....)

    def __init__(self, age, name):
        
        self._name = name
        self._age = age 
    
    @property
    def name(self):
        return name
    
    @name.setter
    def name(self, name):
        self._name = name

    def watch_mv(self):
        if self._age >18 :
            print("can watch PG-18 movie")
        else:
            print("Can only watch BaoBao")

#Inheritance class from class person
class Student(Person):
    def __init__(self, age, name, grade):
        super().__init__(age, name)
        self.grade = grade
    
    # @property
    # def grade(self):
    #     return grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def disPlayStudent(self):
        print(f"student {self._name} , age = {self._age} in grade: {self.grade}" )


def main():
    p = Person( 30,"Hey")
    s = Student( 16,"Hey", 1)
    p.watch_mv()
    s.watch_mv()
    s.disPlayStudent()

main()