#Crea un módulo llamado fechas que contenga funciones para calcular la diferencia entre dos fechas y determinar si un año es bisiesto o no.
#Importa este módulo desde otro archivo y utiliza sus funciones para realizar operaciones relacionadas con fechas.

#calcular diferencia entre dos fechas
from datetime import datetime 
def dif(fecha1, fecha2):
    diferencia = fecha1 - fecha2
    solo_dias = diferencia.days
    print(solo_dias,"dias")


#verificar si un año es bisiesto o no, hay que verificar si es año bisiesto el año 
def es_bisiesto(year):
    #segun chat gpt un año es bisiesto si es divisible por 4, en los casos en que tambien sea divisible por 100 pero no entre 400
    if year % 4 == 0 or year % 100 != 0 and year % 400 == 0: # en caso de que el año no sea divisible por 100 también debe ser divisible por 400 para ser bisiesto, debe cumplir esas condicioned
        print(f"{year} es bisiesto")
    else:
        print(f"{year} no es bisiesto")



#por que no funciona el pasarle la fecha por parametro en formato datetime, no funcioanaba porqeu estaba "llamando a la funciona aca, pero solo debe ser donde ocupamos el modulo creado."