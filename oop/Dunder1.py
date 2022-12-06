from os import system
import
system("clear")

class Automobile:

    def __init__(self,name):
        self.__name = name
        self.__year = None

    @property # getter
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_value):
        self.__name = new_value

    def __str__(self):
        return "It's an Automobile"

    def __floordiv__(self,x):
        return 50//x


x = Automobile(name="BMW")
x.name = "ppp"

print(x//2)


    