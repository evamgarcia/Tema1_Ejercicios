#Dadas dos listas, debes generar una tercera con todos los elementos 
# que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_final = []
for i in lista_1:
    for i in lista_2:
        lista_final.append(i)
        lista_2.remove(i)
print(lista_final)