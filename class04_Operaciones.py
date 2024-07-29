"""
Operaciones
"""
s1= "Hola"
s2= "Python"

# Concatenación
print(s1+","+ " "+s2+"!")

# Repetición
print(s1*3)

# Indexación
print(s1[0]+s1[1])

#Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:5])
print(s2[2:])
print(s2[:2])
print(s2[0:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("a","i"))

# División
print(s2.split("t"))

# Mayúsculas, Minúsculas y primera en mayúsculas y todas en mayúsculas
print(s1.upper())
print(s1.lower())
print("jonathan".title())
print("jonathan".capitalize())

# Eliminación de espacios al principio y al final
print(" Jonathan Herrera Puerto ".strip()+ "JONATHAN")

# Busqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3="jonathan11930"

# Búsqueda de posición
print("Jonathan Herrera Puerto".find("Puerto"))
print("Jonathan Herrera Puerto".find("Herrera"))
print("Jonathan Herrera Puerto".find("H"))
print("Jonathan Herrera Puerto".lower().find("u"))

# Busqueda de Ocurrencias
print(s3.lower().count("1"))

# Formateo
print("Saludo: {}, lenguaje: {}!".format(s1,s2))

# Interpolación
print(f"saludo:{s1}, lenguaje {s2}!")

# Transformacion en lista de caracteres
print(list(s3))

# Transformacionde lista en cadena
l1 = [s1,",",s2,"!"]
print("-".join(l1))

# Tranformaciones númericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5="123456.123"
s5=float(s5)
print(s5)

# Comprobaciones Varias
s4 ="123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
Extra
"""

def check(word1:str,word2:str):
    
    # Palíndromos
    print(f"¿{word1} es un palindromo? {word1 == word1[::-1]}")
    print(f"¿{word2} es un palindromo? {word2 == word2[::-1]}")
    
    # Anagramas
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")
    
    # Isogramas
    def isogram(word: str) -> bool:
        word_dict =dict()
        for character in word1:
            word_dict[character] = word_dict.get(character,0) + 1
                
        isogram =True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram    
    
    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")
    
check("radar","pythonpythonpython")
#check("amor","roma")

