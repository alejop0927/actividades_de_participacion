#  Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.
palabra=str(input("ingresa la palabra:"))
palabra_invertida=palabra[::-1]
if palabra == palabra_invertida:
    print("la palabra es palindromo")
else:
    print("la palabra no es polindromo")