import os
"""
Manejo de Ficheros
"""

file_name ="Jonathan.txt"

with open(file_name,"w")as file:
    file.write("Jonathan\n")
    file.write("30\n")
    file.write("Python\n")

with open(file_name,"r") as file:
    print(file.read())
    
os.remove(file_name)    

"""
Extra
"""
file_name="Jona_shop.txt"

open(file_name, "a")

while True:
    
    print("1. Añadir Producto")
    print("2. Consultar Producto")
    print("3. Actualizar Producto")
    print("4. Borrar Producto")
    print("5. Mostar Productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")
    
    option=input("selecciona una opción: ")
    
    if option =="1":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")

    elif option =="2":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
                
    elif option =="3":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
        
    elif option =="4":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
         
        
    elif option =="5":
        with open(file_name,"r") as file:
            print(file.read())
            
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
    
    elif option =="7":
        name = input("Nombre: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break
        print(total)
        
    elif option =="8":
        
        os.remove(file_name)
        break
    else:
        print("Selecciona una de las opciones disponibles.")
    