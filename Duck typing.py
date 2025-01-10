class Car:
    def wheel(self,):
        print("car has four wheel")

    def color(self):
        print("car has white color")

class Bike:
    def wheel(self,):
        print("bike has 2 wheel ")

    def color(self):
        print("bike has black color")

def start(car):
    car.wheel()
    car.color()
    print("information is displaying")
bike1=Bike()
start(bike1)