#Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
#La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
#Error: Imposible añadir elementos duplicados => [elemento].
#Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.

# Completa el ejercicio aquí
def agregar_una_vez(lista,el):
    if el in lista:
        raise ValueError('Imposible añadir elementos duplicados => [elementos]')
    else:
        lista.append(el)
        return lista

elementos = [1, 5, -2]

agregar_una_vez(elementos, 3)


            

