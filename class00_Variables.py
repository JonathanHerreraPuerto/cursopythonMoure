# para generar comentarios se utiliza "#" esto es para una linea de codigo que se este desarrollando en python

"""
Para generar comentarios en varias lineas de codigo se utiliza triple comilla doble " o simple '
y lo que se encuentre entre estas lineas, se toma como comentario. 
"""
'''
Lo que se encuentra entre comillas triples no afecta al codigo, es decir
que se consideran como notas del programador o el programa.
'''

'''
Tipos de Variables
para definir una variable lo debemos realizar de la siguiente manera.
'''
my_variable = "Mi variable"# por convención en Python las variables de dos palabras o más de separan con un guión bajo
my_variable = "Nuevo valor de mi variable"

MY_CONSTANT = "Mi constante" # por convención, dado que en Python no existen constantes definidas

"""Tipos de datos primitivos"""
my_int = 1 # int= significa que es un valor númerico de tipo entero 
my_float = 1.5 # float= significa que es un valor númerico de tipo decimal
my_bool= True # tipo de dato booleano= que puede ser verdadero o falso
my_bool= False
my_str= "mi cadena de texto" #tipo de dato string o de texto, significa que el dato que se ingrese se considera como texto
my_other_string = 'Mi otra cadena de texto'# adicional la variable definida debe estar entre comilla simples '' o comillas dobles ""

print("Hola! el lenguaje de programación que he decidido aprender es Python")

print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_str))