'''
    Simple OOP python code
    By Donya Qavami
    Edited by Amirhossein Khosravi
'''

import os 
os.system("clear") # or "cls" To clear the Terminal 


class Automobile:


    def __init__(self, car_name = "" , speed = 0):

        self.car_name = car_name
        self.speed = float(speed)
        self.result_string = str(speed)+ " km/h " # To show and define it is km/h


    def speed_conversion_m_to_s(self):
        
        self.speed = self.speed/3.6
        self.result_string = str(self.speed)+ " m/s " # To show and define it is m/s
        

    def announce(self):
    
        print(f" Car name: {self.car_name} \n speed: {self.result_string} ")


# create an object of Automobile
my_car = Automobile(car_name = "BMW" , speed = 200)
# speed conversionn km/h to m/s and save it in result_string
my_car.speed_conversion_m_to_s()
# show finall information of my_car 
my_car.announce()

