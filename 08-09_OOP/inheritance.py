"""
When we want to create a new class based on a class that already exists, we
can directly let the new class inherit the old properties and methods so 
we don't need to write more and unnecessary codes. The old class is called
"parent" class and the new one is called "child" class. 

Other than simply copying the old properties and methods, a child class can
also define its own new properties and methods. Thus, a child class usually 
has more capabilities than its parent class. 
"""

class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age
    
    def play(self):
        print('%s is playing Overwatch.' % self._name)

    def watch_porn(self):
        if self._age>=18:
            print('%s is watching FOW Studio animation hehehe.' % self._name)
        else:
            print('%s is watching Disney cartoon.' % self._name)

class Student(Person):
    # Student is a child class of Person
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade = grade
    
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        self._grade = grade
    
    def study(self,course):
        print('%s in %s grade is studying %s' % (self._name,self._grade,course))

class Teacher(Person):
    # Teacher is a child class of Person
    def __init__(self,name,age,title):
        super().__init__(name,age)
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title
    
    def teach(self,course):
        print('%s %s is teaching %s.' % (self._title,self._name,course))

def main():
    stu = Student('Hana Song',15,'2nd')
    stu.study('Math')
    stu.watch_porn()

    t = Teacher('Morrison',46,'Captain')
    t.teach('Math')
    t.watch_porn()

if __name__ == '__main__':
    main()