# Delete obj , attrib , class


class Person:
    
    def __init__(self,name='',age=0):
        self.name = name
        self.age = age

    
    def show_info(self):
        
       
       # class method
       print(f'name is {self.name} age is {self.age}')


       
p1 = Person(name="Amir",age=21)
p1.show_info()

del p1.age  # delete attributes

p1.show_info()

del Person	# delete class
