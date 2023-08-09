#Crea un módulo llamado generador_usuario que genere nombres de usuario únicos basados en nombres y apellidos ingresados por el usuario. 
#El módulo debe garantizar que no haya nombres de usuario duplicados y puede incluir un número aleatorio al final para resolver conflictos.

import random

def generador_usuario():
    usuario = input("ingrese nombre y ap:")

    num_random = random.randint(0, 9)
    numero = str(num_random)

    concatenacion = usuario + numero #esto es un string
    #quitarle espacios en blanco a un string
    cadena_sin_espacios = concatenacion.replace(" ", "")

    lista_provisoria = list(cadena_sin_espacios)
    #shuffle solo se puede usar en listas porque utiliza mutabilidad para mover de lugar los elementos y string es una estructura inmutable
    random.shuffle(lista_provisoria)
    
    #volver a string
    separador = ""
    numero = separador.join(lista_provisoria)

    print(numero)

generador_usuario()