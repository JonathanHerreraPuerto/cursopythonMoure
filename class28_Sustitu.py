"""
Principio de sustitucion  de Liscov (LSP)
"""

# Incorrecto

# class Bird:
#     def fly(self):
#         return "Flying"

# class Chicken(Bird):
#     def fly(self):
#         raise Exception("Los pollos no vuelan")
    
# bird =Bird()
# bird.fly()
# chicken= Chicken()
# chicken.fly()        
    
# Correcto

class Bird:
    def move(self):
        return "moving"

class Chicken(Bird):
    def move(self):
        return "walking"

bird = Bird()
print(bird.move())
chicken=Chicken()
print(chicken.move())    


"""
Extra
"""

class Vehicle:
    
    def __init__(self, speed=0):
        self.speed = speed
        
    def accelerate(self, increment):
        self.speed +=   increment
        print(f"Velocidad:{self.speed} Km/h")        
    
    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <=0:
            self.speed = 0
        print(f"Velocidad:{self.speed} Km/h") 
        
        
class Car(Vehicle):
    def accelerate(self, increment):
        print("El coche está acelerando")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print("El coche está frenando")
        super().brake(decrement)
    
class Bicycle(Vehicle):
    def accelerate(self, increment):
        print("la bicilceta está acelerando")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print("la bicicleta está frenando")
        super().brake(decrement)

class Motorcycle(Vehicle):
    def accelerate(self, increment):
        print("La moto está acelerando")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print("La moto está frenando")
        super().brake(decrement)                        
        
        
def test_vehicle(vehicle):
    vehicle.accelerate(2)
    vehicle.brake(1)    
        
car = Car()
bicycle=Bicycle()
motorcycle=Motorcycle()                

test_vehicle(car)        
test_vehicle(bicycle)        
test_vehicle(motorcycle)        