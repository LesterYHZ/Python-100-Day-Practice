"""
文字版守望先锋
"""
from abc import ABCMeta, abstractmethod
from random import randint, randrange
import time,os

class Fighter(object,metaclass=ABCMeta):
    __slots__ = ('_name','_hp')

    def __init__(self,name,hp):
        self._name = name
        self._hp = hp
    
    @property
    def name(self):
        return self._name
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,hp):
        self._hp = hp if hp>=0 else 0
    @property
    def alive(self):
        return self._hp>0
    @abstractmethod
    def attack(self,other):
        pass

class Overwatch(Fighter):
    __slots__ = ('_name','_hp','_mp')

    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp

    def attack(self,other):
        other.hp -= randint(15,25)

    def ultimate(self,other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp*3//4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self,others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10,15)
            return True
        else:
            return False
    
    def resume(self):
        point = randint(1,10)
        self._mp += point
        return point

    def __str__(self):
        return 'Overwatch Member %s\n' % self._name + \
            'Health Point: %d\n' % self._hp + \
                'Magic Point: %d\n' % self._mp

class Talon(Fighter):
    __slots__ = ('_name','_hp')

    def attack(self,other):
        other.hp -= randint(10,20)
    
    def __str__(self):
        return 'Talon Member %s\n' % self._name + \
            'Health Point: %d\n' % self._hp

def is_any_alive(Talon):
    for member in Talon:
        if member.alive>0:
            return True
    return False

def select_alive_one(Talon):
    Talon_len = len(Talon)
    while True:
        index = randrange(Talon_len)
        member = Talon[index]
        if member.alive>0:
            return member

def display_info(Overwatch,Talon):
    print(Overwatch)
    for member in Talon:
        print(member, end=' ')

def main():
    tracer = Overwatch('Tracer',1000,120)
    reaper = Talon('Reaper',250)
    doomfist = Talon('Doomfist',400)
    moira = Talon('Moira',200)
    sombra = Talon('Sombra',200)

    talon_members = [reaper,doomfist,moira,sombra]

    fight_round = 1

    while tracer.alive and is_any_alive(talon_members):
        print('\n=========Round %02d=========\n' % fight_round)
        talon = select_alive_one(talon_members)
        skill = randint(1,10)
        if skill<=6:
            print('%s used normal attack on %s' % (tracer.name,talon.name))
            tracer.attack(talon)
            print('%s recoverd her MP by %d' % (tracer.name,tracer.resume()))
        elif skill<=9:
            if tracer.magic_attack(talon_members):
                print('%s used her skill attack on %s' % (tracer.name,talon.name))
            else:
                print('%s failed to use her skill attack' % tracer.name)
        else:
            if tracer.ultimate(talon):
                print('%s used her ultimate on %s' % (tracer.name,talon.name))
            else:
                print('%s used her normal attack on %s' % (tracer.name,talon.name))
                print('%s recoverd her MP by %d' % (tracer.name,tracer.resume()))
        if talon.alive > 0:
            print('%s stricked back on %s\n' % (talon.name,tracer.name))
            talon.attack(tracer)
        display_info(tracer,talon_members)
        fight_round += 1
        time.sleep(1.5)
        os.system('cls')
    print('\n=========Fight Ended=========\n')
    if tracer.alive>0:
        print('Overwatch Member %s Won!' % tracer.name)
    else:
        print('Talon Won!')
    
if __name__ == '__main__':
    main()
