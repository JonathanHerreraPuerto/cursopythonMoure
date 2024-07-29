"""
Funciones y Alcance

funciones creadas por el usuario
"""

#Funciones Simples
# def = significa que se crea una funcion la cual se puede definir a partir de una o más funciones
def greet():
    print("Hola Jonathan! ")
    

greet()

#Funcion con retorno    
# Ejecuta una logica y devuelve algo, como un resultado o mensaje

def return_greed():
    return "¿Como estas?"
print(return_greed())

# funcion con argumento
# se le pueden pasar paramentros a una funcion, como operaciones

def arg_greet(name):
    print(f"Hola, {name}!")
    
arg_greet("Andrea")

#Con Argumentos

def args_greet(greet, name):
    print(f"{greet},{name}!")
    
args_greet(name="Andrea",greet="Hi") 
#se puede alterar el orden de los parametros, definiendo cual es cada uno.

#Con argumento predeterminado

def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")
    
default_arg_greet("Briana")
default_arg_greet()  

# Con argumentos y Return

def return_args_greet(greet,name):
    return f"{greet},{name}!"

print(return_args_greet("Hi","Carol"))

# Return con varios valores

def multiple_return_greet():
    return "Que'Tal","Daria"

greet , name = multiple_return_greet()
print(greet)
print(name)            

# Con número variable de argumentos
#paraindicar que una variable puede tener mas de un argumento se indica antes 
# con asterisco * mas el nombre de la variable
def Variable_arg_greet(*names):
      for name in names:
          print(f"hola,{name}!")
          
Variable_arg_greet("Emily","Fabiola","Gabriela","Helena","Johanna")

# Con número variable de argumentos con palabra clave
# indicando dos asteriscos antes del nombre de la varible indicara que este 
# argumento tendra adicional un aplabra clave 

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola,{value}({key})!")
        
variable_key_arg_greet(
    language="Python",
    name="kimberly",
    alias="Kym",
    age=24
) 

"""
Funciones dentro de funciones
"""       
def outer_funcion():
    def inner_function():
        print("Función interna: Hola, Python!")
    inner_function()
    
outer_funcion()        

"""
Funciones del lenguaje (built-in)
"""
# Funciones propias del lenguaje como:
# son las funciones con las cuales cuenta el lenguaje de prohramación
# en este caso Python. 
# print("") la cual imprime en consola
# .upper() modifica el texto mostrandolo todo en mayúsculas

print(len("Jonathan"))
print(type(36))
print("Jonathan".upper())

"""
Variables Locales y Globales
"""
# Variable Gobal. son definidas en el codigo y pueden ser llamada o utilizada
# dentro de una función o clase 

# Variable local: son definidas dentro de una función o clase, 
# solamentepueden ser utilizadas dentro de la misma función o clase.

global_var = "Python"

def hello_python():
    local_var= "Hola"
    print(f"{local_var}, {global_var}")
    
print(global_var)
#print(local_var) No se puede acceder desde fuera de la función 
hello_python()

print("---------------------------------")

"""
Extra
Este esjerccio se conoce como Fizz Buzz
"""  
def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2) 
        
        elif number % 5 ==0:
            print(text_2)
        elif number % 3 == 0:
            print(text_1)
                
        else:    
            print(number)
            count += 1
    return count
        
print(print_numbers("Texto 1","Texto 2"))