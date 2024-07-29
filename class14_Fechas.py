"""
Fechas
"""
from datetime import datetime

now = datetime.now()
birth_date= datetime(1993, 11, 5, 1,10,0)

print(now)
print(birth_date)

# years = now - birth_date
# print(years)

difference = now - birth_date
print(type(difference))

print(f"Tengo {difference.days//365} años.")

"""
Extra
"""

# Día, Mes, Año.
print(birth_date.strftime("%d /%m /%y"))
print(birth_date.strftime("%d /%m /%Y"))

# Horas, minutos y segundos
print(birth_date.strftime("%H:%M:%S"))

# Día del año
print(birth_date.strftime("%j"))

# Día de la semana
print(birth_date.strftime("%A"))

# Nombre del mes
print(birth_date.strftime("%h"))
print(birth_date.strftime("%B"))

# Reperesentación por defecto del local
print(birth_date.strftime("%c"))
print(birth_date.strftime("%x"))
print(birth_date.strftime("%X"))

# AM/PM
print(birth_date.strftime("%p"))
