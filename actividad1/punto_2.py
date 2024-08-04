# Escribir una función que calcule el área de un círculo dado su radio.

def calculadora(pi,radio):
       return pi*(radio**2)
pi=3.14
radio=float(input("ingrese valor de radio:"))

area=calculadora(pi,radio)

print("el area total es:",area)