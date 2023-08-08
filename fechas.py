#Crea un módulo llamado fechas que contenga funciones para calcular la diferencia entre dos fechas y determinar si un año es bisiesto o no.
#Importa este módulo desde otro archivo y utiliza sus funciones para realizar operaciones relacionadas con fechas.

#calcular diferencia entre dos fechas
from datetime import datetime 
def dif(fecha1, fecha2):
    diferencia = fecha1 - fecha2
    solo_dias = diferencia.days
    print(solo_dias,"dias")


#verificar si un año es bisiesto o no, hay que verificar si es año bisiesto el año 
def es_bisiesto(mes):
    

    return


#por que no funciona el pasarle la fecha por parametro en formato datetime, no funcioanaba porqeu estaba "llamando a la funciona aca, pero solo debe ser donde ocupamos el modulo creado."