import re
"""
Expresiones Regulares
"""

def find_numbers(text:str) -> list:
    return re.findall(r"\d+", text)# tambien se puede realizar la misma operacion con el siguiente rango [0-9]+

print(find_numbers("Este es el ejerccio 16 realizado el día 25/07/2024."))

"""
Extra
"""

# Validacion de email
def validate_email(email:str) ->bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))

print(validate_email("jonathan11930@hotmail.com"))


# Validacion de Telefóno
def validate_phone(phone:str) ->bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))

print(validate_phone("+57 310 123 4567"))   

# Validacion de Url
def validate_url(url:str) ->bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))

print(validate_url("https://www.jonathan.edu"))   