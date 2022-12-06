'''
    By amirkho.ir
    GitHub repo:
'''

from os import system
from traceback import print_tb
system("clear") # or "cls" to clear the terminal



class Student:

    def __init__(self,stu_name,stu_code):

        self.stu_name = stu_name
        self.stu_code = stu_code

    def show_detail(self):
        print(f" Name: {self.stu_name} \n Code: {self.stu_code}" , end="")


    def register(self): # register Student attributes to data.txt file

        result_to_save = "Student Name: " + self.stu_name + "\n" + "Student Code: " + self.stu_code + "\n" + "="*40 + "\n"

        with open("data.txt" , mode='a' , encoding="utf-8") as file:
            file.write(result_to_save)
        

stu1 = Student(stu_name="Amir" , stu_code="1234567890")
stu1.show_detail()
stu1.register()

stu2 = Student("Ali","8765230914")
stu2.register()