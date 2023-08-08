'''Crea un módulo llamado adivinanza que contenga una función que genere un número aleatorio entre 1 y 100,
y luego permita al usuario adivinar el número. El módulo debe proporcionar pistas para indicar si el número
ingresado es mayor o menor que el número generado. El juego debe continuar hasta que el usuario adivine correctamente'''
import random

def num_aleatorio():
  
  num_random = random.randint(1, 100)
  print(num_random)

  
  while True:
    #no funcionada lo de pedir de nuevo el numero porque la linea de input la tenia fuera del while!!!! RECORDAR QUE CADA VEZ DEBE PEDIR AL USUARIO INGRESAR NUMERO, si o esta el input dentro del while no puede
    usuario = input("adivine un numero: ")
    num_usuario = int(usuario)
  
    if num_usuario == num_random:
      print("ganaste!")
      break
    elif num_usuario < num_random:
      print("el numero que elegiste es menor al numero")
    else:
      print("el numero que elegiste es mayor al numero")
    
 #me falta el paso en que no le achunta el numero pero debe seguir intentando hasta que lo logre.
num_aleatorio()


