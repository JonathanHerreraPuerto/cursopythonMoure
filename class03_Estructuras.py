"""
Estructuras del lenguaje Python
"""

"""Listas"""

my_list : list= ["Ska-p", "Fabulosos_Cadillac's","Panteon_Rococo","Cafeta_cvba"]
print(my_list)

my_list.append("La_Maldita_Vecindad") #Inserción o adición 
print(my_list)
#.append se utiliza para adicionar un campo a una lista

my_list.remove("Ska-p") #Eliminación 
print(my_list)
#.remove se utiliza para eliminar un campo de una lista, 
#especificando el nombre de cicho campo a eliminar

print(my_list[1]) #Acceso
# Muestra el elemento que se encuentra en la posición 1
# recordar que el sistema inicia a contar desde cero [0,1,2,3,...]

my_list[1]= "Vicentico" #Actualización
print(my_list)
# Se posiciona en el número del elemento indicado de la lista 
# y lo remplaza por uno nuevo.

my_list.sort() #Ordena la lista
print(my_list) 
# En nuestro caso la ordena por orden alfabético

print(type(my_list))
 
"""Tuplas"""
#son estructuras inmutables, lo que quiere decir que no pueden modificarse

my_tuple :tuple  = ("Jonathan", "Herrera_Puerto","Jhonny","30")
print(my_tuple[1]) # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # Ordenar
print(type(my_tuple))

# Sets
# Es una estructura en la cual se pueden ingresar datos para su consulta.
# no permite la insercion de un mismo dato, ya que su caracteristica principal
# es la de una lectura rapida a la hora de una busqueda de datos
# no devuelve datos ordenados, no los puede ordenar.
my_set: set = {"Jonathan", "Herrera_Puerto","Jhonny","30"}
print(type(my_set))
my_set.add("jonathan11930@hotmail.com") #Insertar
my_set.remove("Herrera_Puerto")# Eliminar
print(my_set)
my_set = set(sorted(my_set)) # No se puede ordenar
print(my_set)
print(type(my_set)) 

print("---------------------------------------")

""" Diccionario"""
# cuenta con clave y dato de nominado por dos puntos (:)
# Clave  Dato
# "name":"Ana"
# 
my_dict: dict ={
    "name":"Jonathan",
    "surname":"Herrera_Puerto",
    "alias":"Jhonny",
    "age":"30"
}
my_dict["email"]='jonathan11930@hotmail.com' #Inserción / Adicion
print(my_dict)
del my_dict["surname"]#Eliminar
print(my_dict)
print(my_dict["name"]) # Acceso
my_dict["age"]="33" #Actualizar
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenar
print(my_dict)
print(type(my_dict))

print("----------------------------")

"""
Extra
"""

def my_agenda():
    
    agenda ={}
    
    def insert_contact():
        phone = input("Introduce el número del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <=11:
            agenda[name] = phone
        else:
            ("Debes introduciir un  número de telefono con menos de 11 digitos.")
    
    
    while True:
        
        print("1. Buscar Contacto")
        print("2. Agregar Contacto")
        print("3. Actualizar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")
        
        option = input("\n Seleciona una opcion: ")
        
        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
                            
            case "2":
                name = input("introduce el nombre del contacto: ")
                insert_contact()
                            
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
                    
            case "4":
                name = input("Introduce el contacto a eliminar.")
                if name in agenda:
                    del agenda [name]
                else:
                 print  (f"el contacto {name} no existe.")                 
                    
            case "5":
                print("Saliendo de la agenda.")    
                break
            case _:
                print("opcion no válida. Elige una opcion  del 1 al 5.")    
    
my_agenda()    
    