"""
SOLID: Principio de Inversion de Dependencias (DIP)
"""

from abc import ABC, abstractmethod

# Sin DIP

class Switch:
    print("Enciende la lámpara")
    
    def turn_on(self):
        print("Enciende la lámpara")

    def turn_off(self):
        print("Apaga la Lámpara")
    
class Lamp:
    
    def __init__(self) -> None:
        self.switch =Switch()
        
    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()
            
lamp=Lamp()
lamp.operate("on")                        
lamp.operate("off")

# Con DIP

class AbstractSwitch:
    def turn_on(self):
        pass   
    
    def turn_off(self):
        pass
            
class LampSwitch(AbstractSwitch):
    
    def turn_on(self):
        print("Enciende la lámpara")   
    
    def turn_off(self):
        print("Apaga la Lámpara")
    

class Lamp:
    
    def __init__(self, switch:AbstractSwitch) -> None:
        self.switch =switch
        
    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()    
    
lamp=Lamp(AbstractSwitch())
lamp.operate("on")                        
lamp.operate("off")
                             
"""
Extra
"""  

class Notifier(ABC):
    def send(self, message: str):
        pass
    
class EmailNotifier(Notifier):
    def send(self, message:str):
        print(f"Enviando email con texto: {message}")    

class PushNotifier(Notifier):
    def send(self, message:str):
        print(f"Enviando Push con texto: {message}")    

class SMSNotifier(Notifier):
    def send(self, message:str):
        print(f"Enviando SMS con texto: {message}")
        
class NotificationService:
    def __init__(self, notifier:Notifier) -> None:
        self.notifier=notifier
        
    def notify(self, message:str):
        self.notifier.send(message)
        
service = NotificationService(EmailNotifier())
#service = NotificationService(PushNotifier())
#service = NotificationService(SMSNotifier())
service.notify("Hola, notificador!")                        
                               
                             