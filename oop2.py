class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def drive(self):
        return "Vroom!!"
    
    def stop(self):
        return("Scrrr")
    
    def play_music(self):
        return("Boom, Boom")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        Car.__init__(self, make, model, year)

    def charge(self):
        return f"I'm charging my {self.make} {self.model}"


myCar = Car("Tesla" , "CyberTruck" , 2023 )
myElectricCar  = ElectricCar("Kia", "Z", "2022")

print(myCar.drive())
print(myElectricCar.charge())