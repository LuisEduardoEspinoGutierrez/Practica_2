import time
import random
import matplotlib.pyplot as plt

def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    else:
        pivote = sum(arreglo) / len(arreglo)  # calcular media
        izq = [x for x in arreglo if x < pivote]
        der = [x for x in arreglo if x > pivote]
        return quicksort(izq) + [pivote] * arreglo.count(pivote) + quicksort(izq)

def tiempo():

    execution_times = []  # arreglo

    # generar los 100 arreglos
    for i in range(100):
        arreglo = [random.randint(1, 100) for _ in range(1000)]
        inicio = time.time()
        resultado = quicksort(arreglo)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        execution_times.append(tiempo_transcurrido)

        #print(f"Arreglo",[i+1]," :",arreglo)
        #print(f"Arreglo ordenado ",[i+1]," ;",resultado)
        #print(f"Tiempo de ejecución de ordenación ",[i+1]," :",tiempo_transcurrido," segundos")

    # grafica
    plt.bar(range(1, 101), execution_times)
    plt.xlabel("Ejecución")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Tiempo de ejecución de mi_programa_a_medir")
    plt.show()

tiempo()
