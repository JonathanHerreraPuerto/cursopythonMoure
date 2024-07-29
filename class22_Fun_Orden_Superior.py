from functools import reduce
from datetime import datetime
"""
Funciones de Orden Superior
"""

# Funcion como argumento

def apply_func(func,x):
    return func(x)

print(apply_func(len,"Jonathan"))

# Retorno de funcion

def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplier =apply_multiplier(2)
print(multiplier(5))

# Sistema

numbers = [1,3,4,2,5]

# Map()

def apply_double(n):
    return n * 2
print(list(map(apply_double, numbers)))


# Filter

def is_even(n):
    return n% 2== 0
print(list(filter(is_even,numbers)))


# Sorted()

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x:-x))


#reduce()

def suma(x,y):
    return x + y
print(reduce(suma, numbers)) # PROBLEMA PORQUE ESTABA SOBREESCRIBIENDO SUM EN LA FUNCIÓN DE ABAJO 

"""
Extra
"""

students =[
    {"name": "Diana","birthdate":"12-10-1996", "grades":[5,9,7, 6,10]},
    {"name": "Jonathan","birthdate":"05-11-1993", "grades":[6,8,6, 7,8]},
    {"name": "Maria","birthdate":"18-07-1997", "grades":[9,8,9, 8,10]},
    {"name": "Paola","birthdate":"10-05-1999", "grades":[9,9,9,10,10]}
]

# Media
def average(grades):
    return sum(grades) / len(grades)

print(list(map(lambda student:{
    "name":student["name"],
    "average": average (student["grades"])}, students)))

# Mejores

print(list
      (map(lambda student:
        student["name"],
        filter(lambda student: average (student["grades"]) >= 9, students))))

# Fecha de nacimiento ordenada

print(sorted(students, key=lambda student: datetime.strptime(student["birthdate"],"%d-%m-%Y"), reverse=True))

# Calificacion mas alta

print(list(map(lambda student: max(student["grades"]),students)))