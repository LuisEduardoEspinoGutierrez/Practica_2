import time
import random
import matplotlib.pyplot as plt

def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    else:
        pivot = arreglo[0]
        less = [x for x in arreglo[1:] if x <= pivot]
        greater = [x for x in arreglo[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Crear los 100 arreglos
arreglos = []
for _ in range(100):
    arreglo = [random.randint(1, 100) for _ in range(1000)]
    arreglos.append(arreglo)

execution_times = []

for i, arreglo in enumerate(arreglos):
    start_time = time.time()
    arreglos_ordenados = quicksort(arreglo)
    end_time = time.time()
    tiempo_transcurrido = end_time - start_time
    execution_times.append(tiempo_transcurrido)
    #print(f"Arreglo {i+1}: {arreglo}")
    #print(f"Arreglo ordenado: {arreglos_ordenados}")
    #print(f"Tiempo de ejecución de ordenación {i+1}: {tiempo_transcurrido} segundos")

# grafica
plt.bar(range(1, 101), execution_times)
plt.xlabel("Ejecución")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de ejecución de mi_programa_a_medir")
plt.show()
