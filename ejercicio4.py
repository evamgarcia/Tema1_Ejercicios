#Ejercicio 4

#Durante la planificación de un proyecto se han acordado una lista de tareas. 
# Para cada una de estas tareas se ha asignado un orden de prioridad 
#(cuanto menor es el número de orden, más prioridad).
#¿Eres capaz de crear una estructura del tipo cola con todas las tareas
#ordenadas pero sin los números de orden?
#Sugerencia
#Para ordenar automáticamente una lista es posible utilizar el método .sort(), 
#deberias probarlo.



#He creado una lista de tareas inventada
tareas = [
    '5: Hacer el prototipo final',
    '2: LLevar los materiales al almacen',
    '3: Montar la maquera',
    '1: Comprar los materiales',
    '4: Hacer pruebas'
]
tareas.sort()
for tarea in tareas:
    print(tarea)
    