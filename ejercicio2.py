#Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
#Guarda en una variable numero_magico el valor 12345679 (sin el 8)
#Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
#Multiplica el numero_usuario por 9 en sí mismo
#Multiplica el numero_magico por el numero_usuario en sí mismo
#Finalmente muestra el valor final del numero_magico por pantalla

from sys import float_repr_style

numero_magico = 12345679
numero_usuario = input("introduce un numero entre el 1 y el 9: ")
numero_usuario = int(numero_usuario)
numero_usuario = numero_usuario * 9
numero_magico2 = numero_magico * numero_usuario
print(numero_magico2)
