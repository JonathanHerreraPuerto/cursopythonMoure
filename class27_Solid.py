from abc import ABC, abstractmethod
"""
Solid: Principio  Abierto-Cerrado (OCP)
"""

class Form:
    
    # def draw_square(self):
    #     print("Dibujar un cuadrado")
        
    # def draw_circule(self):
    #     print("Dibujar un circulo")
    
    def draw(self):
        pass

class Square(Form):
    def draw(self):
        print("dibuja un cuadrado")
        
class Circle(Form):
    def draw(self):
        print("dibuja un círculo")
        
class Triangle(Form):
    def draw(self):
        print("dibuja un triangulo")   
        
"""
Extra
""" 

class Operation(ABC):
    @abstractmethod
    def execute(self,a,b):
        pass
    
    
class Addition(Operation):
    def execute(self,a,b):
        return a + b        
                                   
class Substration(Operation):
    def execute(self,a,b):
        return a - b                                   
                    
class Multiplication(Operation):
    def execute(self,a,b):
        return a * b

class Division(Operation):
    def execute(self,a,b):
        return a / b
    
class Power(Operation):
    def execute(self,a,b):
        return a ** b    
    
class Calculator:
    def __init__(self) -> None:
        self.operations={}
        
    def add_operation(self,name,operation):
        self.operations[name]= operation        

    def calculate(self, name, a,b):
        if name not in self.operations:
            raise ValueError(f"La operación {name} no está soportada")
        return self.operations[name].execute(a,b)

calculator = Calculator()
calculator.add_operation("Addition", Addition())
calculator.add_operation("Substration", Substration())
calculator.add_operation("Multiplication", Multiplication())
calculator.add_operation("Division", Division())
calculator.add_operation("Power", Power())
    
print(calculator.calculate("Addition", 10,3))    
print(calculator.calculate("Substration", 10,3))    
print(calculator.calculate("Multiplication", 10,3))    
print(calculator.calculate("Division", 10,3))    
print(calculator.calculate("Power", 10,3))    
                                        