"""
Operadores
"""

#Operadores aritméticos
print(f"Suma: 10 + 3 = {10+3} ")
print(f"Resta: 10 - 3 = {10-3} ")
print(f"Multiplicacón: 10 * 3 = {10-3} ")
print(f"División: 10 / 3 = {10/3} ")
print(f"Módulo: 10 % 3 = {10%3} ")
print(f"Exponente: 10 ** 3 = {10**3} ")
print(f"División Entera: 10 // 3 = {10//3} ")

#Operadores de igualdad
print(f"Igualdad: 10==3 es {10==3} ")
print(f"Desigualdad: 10==3 es {10==3} ")
print(f"Mayor que: 10 > 3 es {10 > 3} ")
print(f"Menor que: 10 < 3 es {10 < 3} ")
print(f"Mayor igual que: 10 >= 3 es {10 > 10} ")
print(f"Menor igual que: 10 <= 3 es {10 < 3} ")

#Operadores logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4} ")
# operador AND verifica que las dos condiciones sean correctas e iguales
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4} ")
# Operador OR verifica que una de las dos condiciones sea verdad
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14} ")
# Operador NOT niega una sentencia y la reemplaza como verdadera

print("------------------------------------------------------")
#Operadores de Asignación
my_number = 11 # en este caso el simbolo = asigna el valor a la variable my_number
print(my_number)
 
my_number += 1 # Suma y asignación
print(my_number)

my_number -= 1 # Resta y asignación
print(my_number)

my_number *= 2 # Multiplicación y asignación
print(my_number)

my_number /= 2 # División y asignación
print(my_number)
 
my_number %= 2 # Módulo y asignación
print(my_number)

my_number **= 1 # Exponente y asignación
print(my_number)

my_number //= 1 # División Entera y asignación
print(my_number)

print("-------------------------------------------")

#Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")
    
#Operadores de Pertenencia
print(f"'j' in 'jonathan'= {'j' in 'jonathan'} ")    
print(f"'p' not in 'jonathan'= {'p' in 'jonathan'} ")    
    
#Operadores de bit

a = 10 #1010
b = 3 #0011

print(f"AND: 10 & 3 = {10 & 3} ") #0010   
print(f"OR: 10 | 3 = {10 | 3} ") #1011   
print(f"XOR: 10 ^ 3 = {10 ^ 3} ") #1001   
print(f"NOT: ~10 = {~10} ") #1001   
print(f"Desplazamiento  a la derecha: 10 >> 2 = {10>>2} ") #1001   
print(f"Desplazamiento  a la izquierda: 10 >> 2 = {10<<2} ") #1001   

"""
Estructuras de control
"""
# Condicionales

my_string = "HerreraPuerto"

if my_string == "Jonathan":
    print("my_string es 'Jonathan'")
    
elif  my_string == "HerreraPuerto":
    print("my_string es 'HerreraPuerto'")

else:
    print("my_string no es 'Jonathan' ni 'HerreraPuerto'")    
     
print("-----------------------------")
#Iterativas

for i in range(11):
    print(i)
    i = 0
    
while i <=10:
    print(i)
    i+=1         
    
#manejo de excepciones

try:
     print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")
    
"""
Extra
"""                 
for number in range (10,56):
    if number % 2 == 0 and number !=16 and number % 3 !=0:
        print(number)