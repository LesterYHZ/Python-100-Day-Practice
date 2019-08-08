class Person(object):
    # Apparently, we can add as many properties as we want in main()
    # to the class variables. Or we can use __slots__ to limit the properties
    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
        # _variable name indicates that the author doesn't want this property
        # to be 100% public yet doesn't want to make it completely private
        # either
        self._name = name
        self._age = age
    
    # Since the author doesn't recommend a direct access from the outside of 
    # the class, to get access to the properties, we may use getter and setter
    @property
    def name(self):
        # getter
        return self._name

    @property
    def age(self):
        # getter
        return self._age

    @age.setter
    def age(self, age):
        # setter helps to alter the properties in the class
        self._age = age
    
    def play(self):
        if self._age <= 18:
            print('%s is playing chess.' % self._name)
        else:
            print('%s is playing galgames.' % self._name)

def main():
    person = Person('Hana Song', 19)
    person.play()
    person.age = 15
    person.play()
    # person.name = 'Meiling Zhou'
    # that's not gonna work since there is no setter for name property
    person._gender = 'F'
    # person._ismywaifu = True
    # Even though that Hana Song is my waifu is the truth, because of
    # __slots__, we are not able to define another property called 
    # _ismywaifu
    # 我不管我不管宋哈娜就是我老婆！！！o((>ω< ))o

if __name__ == '__main__':
    main()