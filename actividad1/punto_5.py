# Crear una función que convierta grados Fahrenheit a grados Celsius.
def convgradosfahrenheit(grados):
    return (9/5*grados)+32
grados=int(input("ingrese los grados:"))
F=convgradosfahrenheit(grados)
print("Fahrenheit",F)
def gradoscels():
    return 5/9*(F-32)
G=gradoscels()
print("celsius",G)