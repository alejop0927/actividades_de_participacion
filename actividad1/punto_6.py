#Crear un programa que calcule la suma de los números en una lista dada
lista_1=[1,2,3,4,5]
lista_2=[2,3,4,5,6]
sum=[x + y for x, y in zip(lista_1,lista_2)]
print(sum)

