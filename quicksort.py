import random
import time

#Generamos la lista con 10 000 numero random entre 1 y 100 000
randomList = random.sample(range(0,100000), 10000)
print(randomList)

#Empezamos el cronometro
start_time = time.time()

#Algoritmo de ordenamiento quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista.pop()

        items_higher = []
        items_lower = []

        for item in lista:
            if item > pivot:
                items_higher.append(item)
            else:
                items_lower.append(item)
        
        return quicksort(items_lower) + [pivot] + quicksort(items_higher)

print(quicksort(randomList))

#Terminamos el cronometro y hacemos el delta correspondiente para obtener el tiempo transcurrido
end_time = time.time() - start_time
print(end_time)