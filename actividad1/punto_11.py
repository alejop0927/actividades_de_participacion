# Crear un programa que genere una lista de números pares entre 1 y 100.

rango=100
listica=[]
for i in range(rango):
  n=i
  n+=1
  if n%2 ==0:
   listica.append(n)
print(listica)