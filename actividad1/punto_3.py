# Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random
rango=10
list=[]
for i in range(rango):
  n=random.randrange(1,20)
  list.append(n)
print(list)