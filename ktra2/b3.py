class Vehicle():
    def __init__(self, make):
        self.make=make
    def description(self) ->str:
        return (self.make)
class Car(Vehicle):
    def __init__(self, make, model:str):
        super().__init__(make)
        self.model= model
    def description(self) ->str:
        return super().description() + (self.model)
class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make,model)
        self.battery_size= battery_size
    def description(self) ->str:
        return super().description()+ (self.battery_size)

vehicle= Vehicle("toyota")
car= Car("honda ", "civic")
electricCar= ElectricCar("vinfast ", "vf5 ","2day")

print(vehicle.description())
print(car.description())
print(electricCar.description())