#Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
#pero no debe repetirse ningún elemento en la nueva lista:
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_final = []
for x in lista_1:
    if x in lista_2:
        lista_final.append(x)
        lista_2.remove(x)
print(lista_final)