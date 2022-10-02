print('introduce un número entero: ')
numero = input()
if not numero.isdigit():
    print('el argumento introducido no es válido, tiene que ser un numero entero positivo')
else:
    longitud_numero =len(numero)
    numero = [*numero]
    for posicion, digito in enumerate(numero):
        print(('0' * posicion) + digito + ('0' * (longitud_numero - 1)))
        longitud_numero -= 1 
