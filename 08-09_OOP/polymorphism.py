"""
After inhereiting methods in the parent class, a child class can alter, 
or "override", the old methods to a new version so that a different task
can be accomplished. When we are using these child classes with various 
versions of the methods, we have poly-morphism. 
"""

from abc import ABCMeta, abstractmethod

class Pet(object,metaclass = ABCMeta):
    def __init__(self,nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    # Dog is a child class of Pet, yet in this case we have a 
    # new version of make_voice method
    def make_voice(self):
        print('%s: wawawawawawa!!!!' % self._nickname)

class Cat(Pet):
    def make_voice(self):
        print('%s: meow~~~ :3' % self._nickname)

def main():
    pets = [Dog('Uzi'),Cat('GarField'),Dog('Odi')]
    for pet in pets:
        pet.make_voice()

if __name__ == "__main__":
    main()