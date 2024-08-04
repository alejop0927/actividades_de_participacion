# Escribir una función que calcule el factorial de un número dado.

def factorial_n(numero):
  if numero ==0:
    return 1
  factorial=1
  for i in range(1,numero +1):
     factorial*=i
  return factorial
    
  
numero=int(input("ingresa el numero:"))
print(f"el factorial es:{factorial_n(numero)}")