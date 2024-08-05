# Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división.
x=int(input("escribe el primer numero:"))
y=int(input("escribe el segundo numero:"))
def cal_suma(x,y):
    return x+y
def cal_resta(x,y):
    return x-y
def cal_multi(x,y):
    return x*y
def cal_divi(x,y):
    return x/y

print(f"el resultado de las operaciones de los numeros {x} y {y} son: suma:{cal_suma(x,y)} resta:{cal_resta(x,y)} multiplicacion:{cal_multi(x,y)} division{cal_divi(x,y)}")
