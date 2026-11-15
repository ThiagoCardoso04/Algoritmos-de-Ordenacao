import random
import time

# Algoritmo: Bubble Sort (Ordenação por Bolha)
# Compara elementos adjacentes (vizinhos) e os troca se estiverem na ordem errada.
# O maior elemento "flutua" para o final da lista a cada passagem completa.

# VANTAGENS:
# 1. Fácil de entender e implementar.
# 2. Pode ser otimizado para parar se a lista já estiver ordenada.

# DESVANTAGENS:
# 1. Complexidade de tempo O(n²) em todos os casos.
# 2. Faz muitas trocas na memória, sendo ineficiente para listas grandes.

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

if __name__ == "__main__":
    lista = []
    for _ in range(100000):
        lista.append(random.randint(0, 100000))

    inicio = time.time()
    bubble_sort(lista)
    fim = time.time()

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    print("\nPrimeiros 100 elementos:", lista[:100])
    print("Últimos 100 elementos:", lista[-100:])
    
    # print(lista)
