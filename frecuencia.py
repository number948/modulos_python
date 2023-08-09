#scribe un programa que lea un archivo de texto y utilice el módulo collections para contar la 
#frecuencia de cada palabra en el archivo. Luego, muestra las palabras más comunes y su frecuencia.

from collections import Counter

nombre_archivo = 'archivo.txt'
with open(nombre_archivo, 'r') as archivo:
    contenido_archivo = archivo.read()
    palabras = contenido_archivo.split()

contador_palabras = Counter(palabras)

print(contador_palabras)

#algo esta mal con la lectura del archivo, enfoquemonos en eso primero.