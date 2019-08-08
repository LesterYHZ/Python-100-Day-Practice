"""
Previously, the methods we defined in the class are object methods, i.e. 
these methods send message to the object. Yet sometimes we don't need to 
send messages to the object but still need a method to do somthing, and
in this case, we use a static method.

For example, let's define a class called Triangle. This class has some
methods such as computing permeter and area, but before defining the triangle,
we need to determine whether the three input lengths can actually form
a triangle. So, we need to use a static method to do this. 
"""
from math import sqrt

class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and b+c>a and a+c>b

    def perimeter(self):
        return self._a+self._b+self._c

    def area(self):
        half = self.perimeter()/2
        return sqrt(half*(half-self._a)*(half-self._b)*(half-self._c))

def main():
    a,b,c = 3,4,1
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        print(t.area())
    else:
        print('Can\'t form a triangle')

if __name__ == '__main__':
    main()
