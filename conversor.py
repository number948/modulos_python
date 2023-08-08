#Escribe un módulo llamado conversor que contenga funciones para convertir entre diferentes unidades. 
#Por ejemplo, puedes tener funciones para convertir de grados Celsius a Fahrenheit, de kilómetros a millas, 
#de metros a pies, etc. Luego, desde otro archivo, importa este módulo y utiliza sus funciones para realizar conversiones.

#metros a pies
def metros_a_pies(num1):
  pies = num1/ 0.3048 
  redondeado = round(pies, 1)
  print(num1,"es igual a",redondeado, "pies") 

#kilometros a millas
def kilometros_a_millas(km):
  millas = km * 0.62137
  redondeado = round(millas, 4)
  print(km,"km, son igual a ", redondeado, "millas") 

#celsius a fahrenheit
def celsius_a_fahrenheit(celsius):
  fahrenheit = (celsius*1.8) + 32 
  print(celsius,"°C es igual a: ", fahrenheit,"°F")